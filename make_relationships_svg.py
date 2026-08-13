#!/usr/bin/env python3
"""Generate skills-relationships.svg — editable dependency/overlap diagram
for the nine axes of the 2026 Data Scientist Skills Inventory.

Companion to make_svg.py (the radar). Same palette, same "plain Python list
you edit and rerun" convention. See skills-relationships.md for the analysis
this diagram illustrates.
"""
import os

# ---- palette (from make_svg.py cluster colors) --------------------------
CLUSTER_COLOR = {
    "analytical": "#2a78d6",
    "ai":         "#eb6834",
    "engineering":"#1baf7a",
    "human":      "#eda100",
}
INK = "#0b0b0b"
INK_SOFT = "#52514e"
INK_MUTED = "#898781"
BG = "#fcfcfb"
LINE = "#c3c2b7"

# ---- the six cross-cutting foundational abilities (pill legend) ---------
# key -> (short label shown on the pill, full name for the legend, color)
PILLS = {
    "verify":     ("Verify",     "Verification & evaluation judgment", "#c0392b"),
    "spec":       ("Spec",       "Specification & decomposition",       "#7b5ea7"),
    "uncertain":  ("Uncertain",  "Honest uncertainty & limits",         "#1a8fa3"),
    "audience":   ("Audience",   "Audience translation",                "#c2478c"),
    "systems":    ("Systems",    "Systems & durability",                "#52618f"),
    "domain":     ("Domain",     "Domain-grounded judgment",            "#8a7a3c"),
}

# ---- nodes: key -> (label, x, y, cluster, [pill keys]) -------------------
CARD_W, CARD_H = 240, 92
ROW3, ROW2, ROW1 = 210, 480, 710
NODES = {
    "viz":     ("Visualization",          230, ROW3, "human",       ["audience", "uncertain"]),
    "comm":    ("Communication",          650, ROW3, "human",       ["audience", "uncertain"]),
    "story":   ("Storytelling",          1070, ROW3, "human",       ["audience"]),

    "stats":   ("Statistics & Modeling",  230, ROW2, "analytical",  ["spec", "uncertain", "domain"]),
    "aifound": ("AI Foundations",         650, ROW2, "ai",          ["verify", "uncertain"]),
    "prog":    ("Programming",           1070, ROW2, "engineering", ["verify", "systems"]),

    "dataeng": ("Data Engineering",       440, ROW1, "engineering", ["systems", "domain"]),
    "domaink": ("Domain Knowledge",       860, ROW1, "human",       ["domain", "verify"]),
}
BAND_LABEL = "AI Agents & Frameworks — the multiplier: raises effective capacity on every other axis"
BAND_PILLS = ["verify", "spec", "systems"]
BAND_Y = 872
BAND_H = 88

TIER_CAPTIONS = [
    (ROW3 - 70, "HUMAN INTERFACE — DELIVERY"),
    (ROW2 - 70, "ANALYTICAL & TECHNICAL CORE"),
    (ROW1 - 70, "SUBSTRATE"),
]

# ---- edges: (from, to, style) — numbered on the diagram, spelled out in the
# key below and in skills-relationships.md's build-order table.
# style: "explicit"  = solid arrow, direct language in skill-level-rubric.md
#        "inferred"  = dashed arrow, structural reading, not a direct quote
EDGES = [
    ("dataeng", "stats",   "inferred"),
    ("dataeng", "aifound", "explicit"),
    ("domaink", "stats",   "inferred"),
    ("domaink", "comm",    "inferred"),
    ("stats",   "aifound", "explicit"),
    ("stats",   "viz",     "inferred"),
    ("viz",     "comm",    "inferred"),
]
EDGE_KEY = [
    "Data Engineering → Statistics & Modeling — reliable extracts underlie a defensible spec",
    "Data Engineering → AI Foundations — corpora / retrieval fork (Data Engineering §3)",
    "Domain Knowledge → Statistics & Modeling — knowing what the data can answer",
    "Domain Knowledge → Communication — domain credibility carries the room",
    "Statistics & Modeling → AI Foundations — “Bayesian lens ... AI and ML model behavior” (Statistics §3)",
    "Statistics & Modeling → Visualization — uncertainty must be encoded, not just estimated",
    "Visualization → Communication — the artifact feeds the framing",
]
OVERLAP_EDGES = [
    ("comm", "story", "overlap: audience translation, different mechanism"),
]
# the one edge drawn distinctly: the verification cap tying Programming to
# the AI Agents band (skill-level-rubric.md §4)
CAP_EDGE = ("prog", "verification cap (§4)")

W = 1300
# legend layout is computed once here so the canvas height can be sized to fit
_EK_TITLE_Y = 930
_ROW_H = 20
_EK_ROWS = 4  # ceil(len(EDGE_KEY) / 2 columns)
_PILL_TITLE_Y = _EK_TITLE_Y + 24 + _EK_ROWS * _ROW_H + 30
_LINE_LEGEND_Y = _PILL_TITLE_Y + 26 + 2 * 26 + 24
H = int(_LINE_LEGEND_Y + 30)

def fmt(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")

def esc(s):
    return s.replace("&", "&amp;")

def clip(cx, cy, tx, ty, hw, hh):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = hw / abs(dx) if dx != 0 else float("inf")
    sy = hh / abs(dy) if dy != 0 else float("inf")
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s

def arrowhead(x, y, dx, dy, size=9, color=INK_SOFT):
    import math
    length = math.hypot(dx, dy)
    if length == 0:
        return ""
    ux, uy = dx / length, dy / length
    px, py = -uy, ux
    p1 = (x, y)
    p2 = (x - ux * size + px * size * 0.5, y - uy * size + py * size * 0.5)
    p3 = (x - ux * size - px * size * 0.5, y - uy * size - py * size * 0.5)
    pts = " ".join(f"{fmt(px_)},{fmt(py_)}" for px_, py_ in (p1, p2, p3))
    return f'<polygon points="{pts}" fill="{color}"/>'

out = []
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
            f'font-family="system-ui, -apple-system, \'Segoe UI\', sans-serif">')
out.append("""<!--
  Skills relationship diagram (2026 revision) - editable
  HOW TO EDIT: change NODES / EDGES / PILLS in make_relationships_svg.py and rerun.
  Card fill/border = cluster color (same four as ds-skills-radar.svg).
  Pills below each title = cross-cutting foundational abilities (see legend).
  Solid arrow = "builds on", explicit language in skill-level-rubric.md.
  Dashed arrow = "builds on", structural reading (no direct quote).
  Dotted band arrow = AI Agents & Frameworks as capacity multiplier on every axis.
  Dashed double arrow = "overlaps with", a peer relationship, not a hierarchy.
-->""")
out.append(f'<rect width="{W}" height="{H}" fill="{BG}"/>')

# title
out.append(f'<text x="{W/2:.0f}" y="50" text-anchor="middle" font-size="30" font-weight="700" fill="{INK}">How the Nine Skills Relate</text>')
out.append(f'<text x="{W/2:.0f}" y="78" text-anchor="middle" font-size="16" fill="{INK_SOFT}">Foundational abilities, overlaps (pills), and build order (arrows) — companion to skills-relationships.md</text>')

# tier captions
out.append(f'<g font-size="13" font-weight="700" fill="{INK_MUTED}" text-anchor="middle" letter-spacing="1">')
for y, text in TIER_CAPTIONS:
    out.append(f'<text x="{W/2:.0f}" y="{y}">{esc(text)}</text>')
out.append('</g>')

# multiplier arrow: routed through the clear right margin so it never
# crosses a node (rightmost card right edge sits at 1190; band right edge at 1240)
band_top = BAND_Y
mid_x = W / 2
mult_x = 1215
out.append(f'<g opacity="0.45">')
out.append(f'<line x1="{mult_x}" y1="{band_top}" x2="{mult_x}" y2="100" '
            f'stroke="{CLUSTER_COLOR["ai"]}" stroke-width="8" stroke-dasharray="2 13" stroke-linecap="round"/>')
out.append('</g>')
out.append(arrowhead(mult_x, 100, 0, -1, size=12, color=CLUSTER_COLOR["ai"]))
out.append(f'<text x="{mult_x}" y="88" text-anchor="middle" font-size="12" font-weight="700" '
            f'fill="{CLUSTER_COLOR["ai"]}">multiplies every axis</text>')

def node_center(key):
    _, x, y, _, _ = NODES[key]
    return x, y

# edges (builds-on) — numbered markers, spelled out in EDGE_KEY / the doc
out.append('<g>')
for idx, (a, b, style) in enumerate(EDGES, start=1):
    ax, ay = node_center(a)
    bx, by = node_center(b)
    sx, sy = clip(ax, ay, bx, by, CARD_W / 2, CARD_H / 2)
    ex, ey = clip(bx, by, ax, ay, CARD_W / 2, CARD_H / 2)
    dash = '' if style == 'explicit' else ' stroke-dasharray="6 6"'
    out.append(f'<line x1="{fmt(sx)}" y1="{fmt(sy)}" x2="{fmt(ex)}" y2="{fmt(ey)}" '
                f'stroke="{INK_SOFT}" stroke-width="1.6"{dash}/>')
    out.append(arrowhead(ex, ey, ex - sx, ey - sy, color=INK_SOFT))
    mx, my = (sx + ex) / 2 + (bx - ax) * 0.0, (sy + ey) / 2
    out.append(f'<circle cx="{fmt(mx)}" cy="{fmt(my)}" r="11" fill="{BG}" stroke="{INK_SOFT}" stroke-width="1.4"/>')
    out.append(f'<text x="{fmt(mx)}" y="{fmt(my+4)}" text-anchor="middle" font-size="11.5" '
                f'font-weight="700" fill="{INK_SOFT}">{idx}</text>')
out.append('</g>')

# verification-cap edge: band -> Programming, straight up (same column, no swing)
px, py = node_center("prog")
sx, sy = px, band_top
ex, ey = clip(px, py, sx, sy, CARD_W / 2, CARD_H / 2)
out.append(f'<line x1="{fmt(sx)}" y1="{fmt(sy)}" x2="{fmt(ex)}" y2="{fmt(ey)}" '
            f'stroke="{CLUSTER_COLOR["engineering"]}" stroke-width="1.8" stroke-dasharray="3 6"/>')
out.append(arrowhead(ex, ey, ex - sx, ey - sy, color=CLUSTER_COLOR["engineering"]))
out.append(f'<text x="{fmt(mult_x-20)}" y="{fmt((sy+ey)/2)}" text-anchor="end" font-size="11.5" '
            f'fill="{CLUSTER_COLOR["engineering"]}" font-style="italic">{esc(CAP_EDGE[1])}</text>')

# overlap connector: Communication <-> Storytelling
for a, b, label in OVERLAP_EDGES:
    ax, ay = node_center(a)
    bx, by = node_center(b)
    sx, sy = clip(ax, ay, bx, by, CARD_W / 2, CARD_H / 2)
    ex, ey = clip(bx, by, ax, ay, CARD_W / 2, CARD_H / 2)
    out.append(f'<line x1="{fmt(sx)}" y1="{fmt(sy)}" x2="{fmt(ex)}" y2="{fmt(ey)}" '
                f'stroke="{PILLS["audience"][2]}" stroke-width="2" stroke-dasharray="1 7" stroke-linecap="round"/>')
    out.append(arrowhead(ex, ey, ex - sx, ey - sy, color=PILLS["audience"][2]))
    out.append(arrowhead(sx, sy, sx - ex, sy - ey, color=PILLS["audience"][2]))
    mx, my = (sx + ex) / 2, (sy + ey) / 2
    out.append(f'<text x="{fmt(mx)}" y="{fmt(my - 10)}" text-anchor="middle" font-size="11.5" '
                f'fill="{PILLS["audience"][2]}" font-style="italic">{esc(label)}</text>')

# nodes
for key, (label, x, y, cluster, pills) in NODES.items():
    color = CLUSTER_COLOR[cluster]
    x0, y0 = x - CARD_W / 2, y - CARD_H / 2
    out.append(f'<rect x="{fmt(x0)}" y="{fmt(y0)}" width="{CARD_W}" height="{CARD_H}" rx="12" '
                f'fill="{color}" fill-opacity="0.10" stroke="{color}" stroke-width="1.8"/>')
    out.append(f'<text x="{fmt(x)}" y="{fmt(y0+30)}" text-anchor="middle" font-size="17" '
                f'font-weight="700" fill="{INK}">{esc(label)}</text>')
    # pill row, centered
    widths = [6.5 * len(PILLS[p][0]) + 20 for p in pills]
    gap = 6
    total = sum(widths) + gap * (len(pills) - 1)
    px0 = x - total / 2
    py0 = y0 + 46
    for p, w in zip(pills, widths):
        pc = PILLS[p][2]
        out.append(f'<rect x="{fmt(px0)}" y="{fmt(py0)}" width="{fmt(w)}" height="22" rx="11" '
                    f'fill="{pc}" fill-opacity="0.16" stroke="{pc}" stroke-width="1"/>')
        out.append(f'<text x="{fmt(px0+w/2)}" y="{fmt(py0+15)}" text-anchor="middle" font-size="11.5" '
                    f'font-weight="600" fill="{pc}">{esc(PILLS[p][0])}</text>')
        px0 += w + gap

# multiplier band
bx0, by0 = 60, BAND_Y - BAND_H / 2
out.append(f'<rect x="{bx0}" y="{fmt(by0)}" width="{W-2*bx0}" height="{BAND_H}" rx="14" '
            f'fill="{CLUSTER_COLOR["ai"]}" fill-opacity="0.12" stroke="{CLUSTER_COLOR["ai"]}" stroke-width="1.8"/>')
out.append(f'<text x="{mid_x:.0f}" y="{fmt(by0+30)}" text-anchor="middle" font-size="17" '
            f'font-weight="700" fill="{CLUSTER_COLOR["ai"]}">{esc(BAND_LABEL)}</text>')
band_widths = [6.5 * len(PILLS[p][0]) + 20 for p in BAND_PILLS]
band_total = sum(band_widths) + 6 * (len(BAND_PILLS) - 1)
bpx0 = mid_x - band_total / 2
bpy0 = by0 + 46
for p, w in zip(BAND_PILLS, band_widths):
    pc = PILLS[p][2]
    out.append(f'<rect x="{fmt(bpx0)}" y="{fmt(bpy0)}" width="{fmt(w)}" height="22" rx="11" '
                f'fill="{pc}" fill-opacity="0.16" stroke="{pc}" stroke-width="1"/>')
    out.append(f'<text x="{fmt(bpx0+w/2)}" y="{fmt(bpy0+15)}" text-anchor="middle" font-size="11.5" '
                f'font-weight="600" fill="{pc}">{esc(PILLS[p][0])}</text>')
    bpx0 += w + 6

# legend: numbered build-order key (two columns)
ek_title_y = _EK_TITLE_Y
out.append(f'<text x="60" y="{ek_title_y}" font-size="13" font-weight="700" fill="{INK}">Build-order key (numbered arrows above)</text>')
out.append(f'<g font-size="11.5" fill="{INK_SOFT}">')
row_y0 = ek_title_y + 24
row_h = _ROW_H
for i, text in enumerate(EDGE_KEY):
    col = i // _EK_ROWS
    row = i % _EK_ROWS
    cx0 = 60 + col * 620
    cy0 = row_y0 + row * row_h
    style = EDGES[i][2]
    dash = '' if style == 'explicit' else ' stroke-dasharray="4 4"'
    out.append(f'<circle cx="{cx0+9}" cy="{cy0-4}" r="9" fill="{BG}" stroke="{INK_SOFT}" stroke-width="1.2"/>')
    out.append(f'<text x="{cx0+9}" y="{cy0}" text-anchor="middle" font-size="10.5" font-weight="700" fill="{INK_SOFT}">{i+1}</text>')
    out.append(f'<text x="{cx0+26}" y="{cy0}">{esc(text)}</text>')
out.append('</g>')

# legend: pills (two rows of three)
pill_title_y = _PILL_TITLE_Y
out.append(f'<text x="60" y="{pill_title_y}" font-size="13" font-weight="700" fill="{INK}">Cross-cutting abilities (pills)</text>')
out.append(f'<g font-size="11.5">')
pill_items = list(PILLS.items())
for i, (key, (short, full, color)) in enumerate(pill_items):
    col = i % 3
    row = i // 3
    lx0 = 60 + col * 420
    ly0 = pill_title_y + 26 + row * 26
    w = 6.5 * len(short) + 20
    out.append(f'<rect x="{lx0}" y="{ly0-15}" width="{fmt(w)}" height="20" rx="10" fill="{color}" fill-opacity="0.16" stroke="{color}"/>')
    out.append(f'<text x="{fmt(lx0+w/2)}" y="{ly0}" text-anchor="middle" font-size="11" font-weight="600" fill="{color}">{esc(short)}</text>')
    out.append(f'<text x="{fmt(lx0+w+8)}" y="{ly0}" fill="{INK_SOFT}">{esc(full)}</text>')
out.append('</g>')

ly2 = _LINE_LEGEND_Y
out.append(f'<g font-size="12" fill="{INK_SOFT}">')
out.append(f'<line x1="60" y1="{ly2-4}" x2="95" y2="{ly2-4}" stroke="{INK_SOFT}" stroke-width="1.6"/>')
out.append(f'<text x="102" y="{ly2}">builds on — explicit in rubric</text>')
out.append(f'<line x1="330" y1="{ly2-4}" x2="365" y2="{ly2-4}" stroke="{INK_SOFT}" stroke-width="1.6" stroke-dasharray="6 6"/>')
out.append(f'<text x="372" y="{ly2}">builds on — inferred</text>')
out.append(f'<line x1="580" y1="{ly2-4}" x2="615" y2="{ly2-4}" stroke="{PILLS["audience"][2]}" stroke-width="2" stroke-dasharray="1 7"/>')
out.append(f'<text x="622" y="{ly2}">overlaps with (peer, not hierarchy)</text>')
out.append(f'<line x1="900" y1="{ly2-4}" x2="935" y2="{ly2-4}" stroke="{CLUSTER_COLOR["ai"]}" stroke-width="6" stroke-dasharray="2 8"/>')
out.append(f'<text x="942" y="{ly2}">AI Agents multiplies every axis</text>')
out.append('</g>')

out.append('</svg>')
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "skills-relationships.svg")
svg = "\n".join(out)
open(dest, "w").write(svg)
print("wrote", len(svg), "bytes ->", dest)
