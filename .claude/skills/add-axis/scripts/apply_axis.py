#!/usr/bin/env python3
"""apply_axis.py — mechanically add a new skill axis (and optionally a new
cluster) to ds-skills-explorer.html and make_svg.py, keeping the two files'
duplicated, differently-shaped data in sync, and verifying the invariants
between them.

Why this exists: the same SKILLS/CLUSTERS/PRESETS data lives twice — as JS
object literals in ds-skills-explorer.html and as Python tuples in
make_svg.py — with different cluster representations (a per-skill index in
JS vs. a contiguous (first, last) range in Python) and six positional preset
arrays that must all stay exactly len(SKILLS) long. These invariants are
silent when broken (wrong values just render), so they're enforced here
instead of via freehand edits.

Usage:
  apply_axis.py --verify
  apply_axis.py --add --id ID --label LABEL --cluster "Cluster Name"
                --values v1,v2,v3,v4,v5,v6
                [--new-cluster-color "#rrggbb"]
                [--new-cluster-dark-color "#rrggbb"]
                [--not-new]

  --values are the six named (non-"Custom") archetype values, in file order:
  Balanced 2026 DS, The Guide, The Builder, The Architect, The Visionary,
  The Toolmaker. Each is 0-4 in 0.5 steps.

  --cluster may name an existing cluster (case-insensitive exact match) or a
  new one. A new cluster requires --new-cluster-color and is always appended
  after all existing clusters; a new axis in an EXISTING cluster is always
  inserted immediately after that cluster's last existing axis, so the
  Python (first, last) range invariant never needs axes to be reordered.
"""
import argparse
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))))))
HTML_PATH = os.path.join(REPO, "ds-skills-explorer.html")
PY_PATH = os.path.join(REPO, "make_svg.py")

PRESET_ORDER = ["Balanced 2026 DS", "The Guide", "The Builder", "The Architect",
                "The Visionary", "The Toolmaker"]

# ---------------------------------------------------------------- JS parsing
CLUSTER_BLOCK_RE = re.compile(r"(const CLUSTERS = \[\n)(.*?)(\n\];\n)", re.DOTALL)
SKILLS_BLOCK_RE = re.compile(r"(const SKILLS = \[ // order = clockwise from top\n)(.*?)(\n\];\n)", re.DOTALL)
ORDER_COMMENT_RE = re.compile(
    r"(// preset values follow SKILLS order:\n// \[)([^\]]*)(\]\n)")
PRESETS_BLOCK_RE = re.compile(r"(const PRESETS = \{\n)(.*?)(\n\};\n)", re.DOTALL)

CLUSTER_ITEM_RE = re.compile(r'\{\s*name:\s*"([^"]+)",\s*varName:\s*"([^"]+)"\s*\}')
SKILL_ITEM_RE = re.compile(
    r'\{\s*id:\s*"([^"]+)",\s*label:\s*"([^"]+)",\s*cluster:\s*(\d+),\s*isNew:\s*(true|false)\s*\},?'
    r'(?:[ \t]*(//[^\n]*))?')
PRESET_ITEM_RE = re.compile(r'"([^"]+)":\s*(null|\[[^\]]*\]),?')

LIGHT_CSS_BLOCK_RE = re.compile(r"(\.viz-root \{\n)(.*?)(\n  \}\n)", re.DOTALL)
DARK_CSS_BLOCK_RE = re.compile(
    r'(:root:where\(:not\(\[data-theme="light"\]\)\) \.viz-root \{\n)(.*?)(\n    \}\n)', re.DOTALL)
CSS_VAR_RE = re.compile(r'^([ \t]*)(--c-[\w-]+):\s*(#[0-9a-fA-F]{3,8});\s*$', re.MULTILINE)


def parse_js(text):
    cm = CLUSTER_BLOCK_RE.search(text)
    clusters = [{"name": n, "varname": v} for n, v in CLUSTER_ITEM_RE.findall(cm.group(2))]

    sm = SKILLS_BLOCK_RE.search(text)
    skills = []
    for m in SKILL_ITEM_RE.finditer(sm.group(2)):
        skills.append({
            "id": m.group(1), "label": m.group(2), "cluster": int(m.group(3)),
            "isnew": m.group(4) == "true", "comment": m.group(5) or "",
        })

    ocm = ORDER_COMMENT_RE.search(text)
    order_ids = [s.strip() for s in ocm.group(2).split(",")] if ocm else [s["id"] for s in skills]

    pm = PRESETS_BLOCK_RE.search(text)
    presets = []  # list of (name, list[float]-or-None) to preserve order
    for name, value in PRESET_ITEM_RE.findall(pm.group(2)):
        if value == "null":
            presets.append((name, None))
        else:
            presets.append((name, [_num(x.strip()) for x in value.strip("[]").split(",")]))

    return {"clusters": clusters, "skills": skills, "order_ids": order_ids, "presets": presets}


def _num(s):
    return float(s) if "." in s else int(s)


def _fmt_num(n):
    return f"{n:g}"


def serialize_js(text, data):
    clusters_txt = "\n".join(
        f'  {{ name: "{c["name"]}", varName: "{c["varname"]}" }},' for c in data["clusters"])
    text = CLUSTER_BLOCK_RE.sub(lambda m: m.group(1) + clusters_txt + m.group(3), text, count=1)

    skill_lines = []
    for s in data["skills"]:
        comment = f"  {s['comment']}" if s["comment"] else ""
        skill_lines.append(
            f'  {{ id: "{s["id"]}", label: "{s["label"]}", cluster: {s["cluster"]}, '
            f'isNew: {"true" if s["isnew"] else "false"} }},{comment}')
    skills_txt = "\n".join(skill_lines)
    text = SKILLS_BLOCK_RE.sub(lambda m: m.group(1) + skills_txt + m.group(3), text, count=1)

    order_txt = ", ".join(data["order_ids"])
    text = ORDER_COMMENT_RE.sub(lambda m: m.group(1) + order_txt + m.group(3), text, count=1)

    preset_lines = []
    for name, values in data["presets"]:
        val_txt = "null" if values is None else "[" + ", ".join(_fmt_num(v) for v in values) + "]"
        preset_lines.append(f'  "{name}": {val_txt},')
    presets_txt = "\n".join(preset_lines)
    text = PRESETS_BLOCK_RE.sub(lambda m: m.group(1) + presets_txt + m.group(3), text, count=1)

    return text


def add_css_var(text, block_re, indent_hint, varname, hex_color):
    m = block_re.search(text)
    block = m.group(2)
    var_matches = list(CSS_VAR_RE.finditer(block))
    indent = var_matches[-1].group(1) if var_matches else indent_hint
    insert_at = var_matches[-1].end() if var_matches else 0
    new_block = block[:insert_at] + f"\n{indent}{varname}: {hex_color};" + block[insert_at:]
    return text[:m.start(2)] + new_block + text[m.end(2):]


# ------------------------------------------------------------- Python parsing
PY_SKILLS_BLOCK_RE = re.compile(
    r"(SKILLS = \[  # \(label, value 0-4, new\?\)  order = clockwise from top\n)(.*?)(\n\]\n)",
    re.DOTALL)
PY_CLUSTERS_BLOCK_RE = re.compile(
    r"(CLUSTERS = \[  # \(name, first axis idx, last axis idx, color\)\n)(.*?)(\n\]\n)", re.DOTALL)

PY_SKILL_ITEM_RE = re.compile(
    r'\("([^"]+)",\s*(\d+(?:\.\d+)?),\s*(True|False)\),?(?:[ \t]*(#[^\n]*))?')
PY_CLUSTER_ITEM_RE = re.compile(r'\("([^"]+)",\s*(\d+),\s*(\d+),\s*"(#[0-9a-fA-F]+)"\),?')


def parse_py(text):
    sm = PY_SKILLS_BLOCK_RE.search(text)
    skills = []
    for m in PY_SKILL_ITEM_RE.finditer(sm.group(2)):
        skills.append({
            "label": m.group(1), "value": _num(m.group(2)), "isnew": m.group(3) == "True",
            "comment": m.group(4) or "",
        })
    cm = PY_CLUSTERS_BLOCK_RE.search(text)
    clusters = []
    for m in PY_CLUSTER_ITEM_RE.finditer(cm.group(2)):
        clusters.append({"name": m.group(1), "i0": int(m.group(2)), "i1": int(m.group(3)),
                          "color": m.group(4)})
    return {"skills": skills, "clusters": clusters}


def serialize_py(text, data):
    skill_lines = []
    for s in data["skills"]:
        comment = f"  {s['comment']}" if s["comment"] else ""
        skill_lines.append(f'    ("{s["label"]}", {_fmt_num(s["value"])}, {s["isnew"]}),{comment}')
    skills_txt = "\n".join(skill_lines)
    text = PY_SKILLS_BLOCK_RE.sub(lambda m: m.group(1) + skills_txt + m.group(3), text, count=1)

    cluster_lines = [f'    ("{c["name"]}", {c["i0"]}, {c["i1"]}, "{c["color"]}"),'
                      for c in data["clusters"]]
    clusters_txt = "\n".join(cluster_lines)
    text = PY_CLUSTERS_BLOCK_RE.sub(lambda m: m.group(1) + clusters_txt + m.group(3), text, count=1)
    return text


# --------------------------------------------------------------------- verify
def verify(js, py):
    errors = []
    n = len(js["skills"])

    for name, values in js["presets"]:
        if values is not None and len(values) != n:
            errors.append(
                f'preset "{name}" has {len(values)} values, expected {n} (== len(SKILLS))')

    js_labels = [s["label"] for s in js["skills"]]
    py_labels = [s["label"] for s in py["skills"]]
    if js_labels != py_labels:
        errors.append(
            "JS SKILLS labels/order != Python SKILLS labels/order:\n"
            f"  JS: {js_labels}\n  PY: {py_labels}")

    covered = set()
    prev_i1 = -1
    for c in py["clusters"]:
        if c["i0"] != prev_i1 + 1:
            errors.append(
                f'Python CLUSTERS "{c["name"]}" range ({c["i0"]},{c["i1"]}) is not contiguous '
                f"with the previous cluster (expected first idx {prev_i1 + 1})")
        if c["i0"] > c["i1"]:
            errors.append(f'Python CLUSTERS "{c["name"]}" has first idx > last idx')
        for i in range(c["i0"], c["i1"] + 1):
            covered.add(i)
        prev_i1 = c["i1"]
    if covered != set(range(n)):
        errors.append(f"Python CLUSTERS ranges cover {sorted(covered)}, expected 0..{n - 1}")

    cluster_of_idx = {}
    for ci, c in enumerate(py["clusters"]):
        for i in range(c["i0"], c["i1"] + 1):
            cluster_of_idx[i] = ci
    for i, s in enumerate(js["skills"]):
        expected = cluster_of_idx.get(i)
        if expected is not None and s["cluster"] != expected:
            errors.append(
                f'JS SKILLS[{i}] ("{s["label"]}") has cluster index {s["cluster"]}, '
                f"but Python CLUSTERS ranges put axis {i} in cluster index {expected} "
                f'("{py["clusters"][expected]["name"]}")')

    balanced = dict(js["presets"]).get("Balanced 2026 DS")
    if balanced is not None:
        for i, s in enumerate(py["skills"]):
            if i < len(balanced) and s["value"] != balanced[i]:
                errors.append(
                    f'make_svg.py SKILLS[{i}] ("{s["label"]}") value {s["value"]} != '
                    f'"Balanced 2026 DS" preset value {balanced[i]} (the static SVG should '
                    "plot the balanced profile)")

    if len(js["order_ids"]) != n:
        errors.append(
            f'the "// preset values follow SKILLS order" comment lists {len(js["order_ids"])} '
            f"ids, expected {n}")
    js_ids = [s["id"] for s in js["skills"]]
    if js["order_ids"] != js_ids:
        errors.append(
            "the preset-order comment ids don't match SKILLS id order:\n"
            f"  comment: {js['order_ids']}\n  SKILLS:  {js_ids}")

    for c in js["clusters"]:
        if not any(pc["name"] == c["name"] for pc in py["clusters"]):
            errors.append(f'JS cluster "{c["name"]}" has no matching Python CLUSTERS entry')
    for pc in py["clusters"]:
        if not any(c["name"] == pc["name"] for c in js["clusters"]):
            errors.append(f'Python cluster "{pc["name"]}" has no matching JS CLUSTERS entry')

    return errors


def check_css_vars(html_text, js_clusters):
    errors = []
    lm = LIGHT_CSS_BLOCK_RE.search(html_text)
    dm = DARK_CSS_BLOCK_RE.search(html_text)
    light_vars = {m.group(2) for m in CSS_VAR_RE.finditer(lm.group(2))} if lm else set()
    dark_vars = {m.group(2) for m in CSS_VAR_RE.finditer(dm.group(2))} if dm else set()
    for c in js_clusters:
        if c["varname"] not in light_vars:
            errors.append(f'cluster "{c["name"]}" varName {c["varname"]} not defined in the '
                          "light .viz-root CSS block")
        if c["varname"] not in dark_vars:
            errors.append(f'cluster "{c["name"]}" varName {c["varname"]} not defined in the '
                          "dark @media CSS block")
    return errors


# ----------------------------------------------------------------------- add
def slugify(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def do_add(args):
    html_text = open(HTML_PATH).read()
    py_text = open(PY_PATH).read()
    js = parse_js(html_text)
    py = parse_py(py_text)

    errs = verify(js, py) + check_css_vars(html_text, js["clusters"])
    if errs:
        print("Baseline verification failed — refusing to add on top of a broken state:",
              file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    warnings = []
    n_before = len(js["skills"])
    values = args.values
    if len(values) != len(PRESET_ORDER):
        print(f"--values must have exactly {len(PRESET_ORDER)} entries "
              f"({', '.join(PRESET_ORDER)}), got {len(values)}", file=sys.stderr)
        return 1

    existing_cluster_idx = None
    for i, c in enumerate(js["clusters"]):
        if c["name"].lower() == args.cluster.lower():
            existing_cluster_idx = i
            break

    if existing_cluster_idx is not None:
        cluster_name = js["clusters"][existing_cluster_idx]["name"]
        # insert right after this cluster's last existing axis
        idxs = [i for i, s in enumerate(js["skills"]) if s["cluster"] == existing_cluster_idx]
        insert_idx = (idxs[-1] + 1) if idxs else n_before
        new_cluster_idx = existing_cluster_idx
    else:
        if not args.new_cluster_color:
            print(f'"{args.cluster}" is not an existing cluster; pass --new-cluster-color '
                  "to create it", file=sys.stderr)
            return 1
        cluster_name = args.cluster
        insert_idx = n_before
        new_cluster_idx = len(js["clusters"])
        js["clusters"].append({"name": cluster_name, "varname": f"--c-{slugify(cluster_name)}"})
        dark_color = args.new_cluster_dark_color
        if not dark_color:
            dark_color = args.new_cluster_color
            warnings.append(
                f"no --new-cluster-dark-color given; reusing {dark_color} for dark mode too — "
                "check contrast against the dark background and adjust the two --c-* lines "
                "in ds-skills-explorer.html if needed")
        py["clusters"].append({"name": cluster_name, "i0": insert_idx, "i1": insert_idx,
                                "color": args.new_cluster_color})

    # shift existing Python cluster ranges that sit at/after the insertion point
    for c in py["clusters"]:
        if c["name"] == cluster_name and existing_cluster_idx is not None:
            c["i1"] += 1
        elif c["i0"] >= insert_idx and c["name"] != cluster_name:
            c["i0"] += 1
            c["i1"] += 1

    is_new_flag = not args.not_new
    js["skills"].insert(insert_idx, {
        "id": args.id, "label": args.label, "cluster": new_cluster_idx,
        "isnew": is_new_flag, "comment": "",
    })
    js["order_ids"].insert(insert_idx, args.id)

    balanced_value = values[0]
    py["skills"].insert(insert_idx, {
        "label": args.label, "value": balanced_value, "isnew": is_new_flag, "comment": "",
    })

    updated_presets = []
    for name, existing_values in js["presets"]:
        if existing_values is None:
            updated_presets.append((name, None))
            continue
        v = list(existing_values)
        pos = PRESET_ORDER.index(name)
        v.insert(insert_idx, values[pos])
        updated_presets.append((name, v))
    js["presets"] = updated_presets

    errs = verify(js, py)
    if errs:
        print("Post-add verification failed — not writing anything:", file=sys.stderr)
        for e in errs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    new_html = serialize_js(html_text, js)
    if existing_cluster_idx is None:
        new_html = add_css_var(new_html, LIGHT_CSS_BLOCK_RE, "    ",
                                js["clusters"][-1]["varname"], args.new_cluster_color)
        new_html = add_css_var(new_html, DARK_CSS_BLOCK_RE, "      ",
                                js["clusters"][-1]["varname"], dark_color)
        css_errs = check_css_vars(new_html, js["clusters"])
        if css_errs:
            print("CSS var insertion failed verification:", file=sys.stderr)
            for e in css_errs:
                print(f"  - {e}", file=sys.stderr)
            return 1

    new_py = serialize_py(py_text, py)

    open(HTML_PATH, "w").write(new_html)
    open(PY_PATH, "w").write(new_py)

    print(f'Added "{args.label}" (id={args.id}) to cluster "{cluster_name}" at axis '
          f"index {insert_idx} of {insert_idx + 1 if existing_cluster_idx is not None else len(js['skills'])}.")
    for w in warnings:
        print(f"WARNING: {w}")
    print("Next: run `python3 make_svg.py` to regenerate ds-skills-radar.svg, then "
          "`apply_axis.py --verify`.")
    return 0


def do_verify():
    html_text = open(HTML_PATH).read()
    py_text = open(PY_PATH).read()
    js = parse_js(html_text)
    py = parse_py(py_text)
    errs = verify(js, py) + check_css_vars(html_text, js["clusters"])
    if errs:
        print(f"FAIL — {len(errs)} invariant violation(s):")
        for e in errs:
            print(f"  - {e}")
        return 1
    print(f"OK — {len(js['skills'])} axes across {len(js['clusters'])} clusters, "
          "all invariants hold.")
    return 0


def parse_values(s):
    return [_num(x.strip()) for x in s.split(",")]


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--verify", action="store_true")
    p.add_argument("--add", action="store_true")
    p.add_argument("--id")
    p.add_argument("--label")
    p.add_argument("--cluster")
    p.add_argument("--values", type=parse_values, default=[])
    p.add_argument("--new-cluster-color")
    p.add_argument("--new-cluster-dark-color")
    p.add_argument("--not-new", action="store_true")
    args = p.parse_args()

    if args.verify:
        return do_verify()
    if args.add:
        missing = [f"--{n}" for n, v in
                   [("id", args.id), ("label", args.label), ("cluster", args.cluster)]
                   if not v]
        if missing or not args.values:
            print(f"--add requires --id, --label, --cluster, and --values "
                  f"(missing: {', '.join(missing) or '--values'})", file=sys.stderr)
            return 1
        return do_add(args)
    p.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
