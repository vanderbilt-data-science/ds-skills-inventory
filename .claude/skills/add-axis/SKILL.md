---
name: add-axis
description: Add a new skill axis (and, if needed, a new cluster) to the Data Scientist Skills Inventory radar — updates ds-skills-explorer.html, make_svg.py, the regenerated SVG, and the related prose (README, skills-assessment.md, skill-level-rubric.md, _config.yml), then branches, commits, pushes, and opens a PR. Use when the user asks to add a new skill/axis/category to the graph or radar, add a skill type like "Domain Knowledge", or invokes /add-axis. Relates to GitHub issue #26 "Add New Skills to Graph".
---

# /add-axis — add a new skill axis to the radar

This repo's radar data is duplicated in two files with different shapes, plus
prose that hardcodes the axis count in five places. Don't hand-edit these —
use `.claude/skills/add-axis/scripts/apply_axis.py`, which knows the
invariants and refuses to write anything that would break them:

- `ds-skills-explorer.html` — JS `CLUSTERS` (name + CSS var), `SKILLS`
  (`{id, label, cluster: <index>, isNew}`), and six positional `PRESETS`
  arrays that must each stay exactly `SKILLS.length` long.
- `make_svg.py` — the same data as Python tuples, but a cluster is a
  **contiguous `(first, last)` index range**, so a cluster's axes must stay
  adjacent, and every later cluster's range shifts on insert.
- Cluster colors live three places: `--c-*` CSS vars in `ds-skills-explorer.html`
  (once for light, once for dark), and a literal hex in `make_svg.py`.
- `ds-skills-radar.svg` is generated, not hand-edited.

## Step 0 — Preflight

```bash
git status --porcelain   # must be empty; if not, stop and ask the user what to do with it
git fetch origin
git checkout main
git pull --ff-only
python3 .claude/skills/add-axis/scripts/apply_axis.py --verify
```

If `--verify` fails on a clean `main`, stop and report it — don't add on top of
a broken baseline.

## Step 1 — Gather the axis definition

Ask the user (via `AskUserQuestion` if anything below is missing — don't guess
silently on these, a wrong value plots wrong forever):

- **`id`** — short lowercase slug, e.g. `domain2` (must be unique).
- **`label`** — display name, e.g. `"Domain Knowledge"`.
- **`cluster`** — an existing cluster name (`Analytical core`, `AI`,
  `Engineering`, `Human interface`) or a new one. A new cluster additionally
  needs a light-mode hex color (`--new-cluster-color`) and, ideally, a
  dark-mode one (`--new-cluster-dark-color`) — if the user only gives one,
  the script reuses it for both and prints a contrast warning.
- **Six archetype values** (0–4 in 0.5 steps), in this order: `Balanced 2026
  DS`, `The Guide`, `The Builder`, `The Architect`, `The Visionary`, `The
  Toolmaker`. Propose defaults from each archetype's description in
  `README.md`'s "The archetypes" section, but have the user confirm — these
  numbers *are* the feature.
- Whether to mark it `isNew` (default yes for a freshly added axis; pass
  `--not-new` to override).

## Step 2 — Apply the mechanical edits

```bash
python3 .claude/skills/add-axis/scripts/apply_axis.py --add \
  --id <id> --label "<label>" --cluster "<cluster>" \
  --values <balanced>,<guide>,<builder>,<architect>,<visionary>,<toolmaker> \
  [--new-cluster-color "#rrggbb"] [--new-cluster-dark-color "#rrggbb"] \
  [--not-new]

python3 make_svg.py
python3 .claude/skills/add-axis/scripts/apply_axis.py --verify
```

The script inserts the new axis immediately after its cluster's last existing
axis (or appends a new cluster at the end), extends all six presets at the
matching index, and — for a new cluster — appends the JS `CLUSTERS` entry and
adds the CSS var to both the light and dark blocks. It re-verifies before and
after writing. If it exits non-zero, stop and fix the reported issue; don't
patch around it by hand.

## Step 3 — Update the prose

The axis count and per-axis content appear outside the data files too. Update,
in this order:

1. **`skill-level-rubric.md`** — insert a new `### <Label>` ladder into
   `## 3. The <N> ladders` at the position matching axis order. Follow the
   existing template exactly (use `### Domain Knowledge` as the model):
   a `> **Probe:**` blockquote, a `| Level | You are here when |` table with
   rungs 0–4, then `**Evidence that counts:**` (and, where it adds signal,
   `**Evidence that doesn't:**`) and `**Miscalibration:**` lines, then a `---`
   separator. Draft this from the axis's purpose — it's a first pass for a
   human to sanity-check, not a final answer.
2. Every `nine`/`Nine`/`9` that names the *old* axis count, across `README.md`,
   `skills-assessment.md`, `skill-level-rubric.md`, and `_config.yml` — replace
   with the correct number **spelled out as a word** (e.g. "nine" → "ten"), not
   a digit, to match the surrounding prose style. Also update the cluster
   tables in `README.md`'s "The nine axes" section and
   `skills-assessment.md`'s "The 9-axis inventory" section to list the new
   axis under its cluster.
3. If a new cluster was added, also add it to those same cluster tables and to
   any place all four cluster names are enumerated.

## Step 4 — Eyeball the render

Open `ds-skills-radar.svg`. `make_svg.py`'s `LABEL_R = R + 78` and the legend
width heuristic (`widths = [10.5 * len(n) + 42 ...]`) were tuned for 9 axes /
4 clusters — with more axes or a long label, labels can crowd or the legend
can overflow the 1360px canvas. If so, adjust those constants and regenerate;
note any such retuning in the PR description rather than leaving it silent.

## Step 5 — Branch, commit, push, open a PR

```bash
BRANCH="add-axis-<id>"
git checkout -b "$BRANCH"
git add -A
git commit -m "$(cat <<'EOF'
Add <Label> axis to the skills radar

Adds the <Label> axis to the <Cluster> cluster across the explorer,
the SVG generator, and the regenerated radar. Extends all six archetype
presets and drafts a 0-4 rubric ladder.

Refs #26

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
EOF
)"
git push -u origin "$BRANCH"
```

Then open the PR:

```bash
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  gh pr create --base main --head "$BRANCH" \
    --title "Add <Label> axis to the skills radar" \
    --body "$(cat <<'EOF'
Adds the <Label> axis (id \`<id>\`) to the <Cluster> cluster.

- Updates \`ds-skills-explorer.html\` and \`make_svg.py\` (data + regenerated
  \`ds-skills-radar.svg\`), extending all six archetype presets.
- Updates axis-count prose in README.md, skills-assessment.md,
  skill-level-rubric.md, and _config.yml.

**Needs human review before merge:** the \`### <Label>\` rubric ladder in
\`skill-level-rubric.md\` is AI-drafted, not calibrated against real evidence.
<list any layout retuning from Step 4 here, or remove this line>

Refs #26
EOF
)"
else
  echo "gh is not installed/authenticated — open a PR manually:"
  echo "https://github.com/vanderbilt-data-science/ds-skills-inventory/compare/main...$BRANCH?expand=1"
fi
```

`gh` is not installed on this machine as of the last check, so expect to hit
the fallback — that's fine, just hand the user the URL. Do **not** silently
install `gh` or otherwise change the user's environment to make the primary
path succeed.

Never force-push, never skip `--verify`, and never edit the data blocks in
`ds-skills-explorer.html` or `make_svg.py` by hand when the script can do it —
that's exactly the class of silent misalignment this skill exists to prevent.
