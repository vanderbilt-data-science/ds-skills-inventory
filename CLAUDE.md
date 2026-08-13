# CLAUDE.md

Guidance for Claude Code (or any agent) working in this repository.

## What this repo is

The **Data Scientist Skills Inventory** — a 2026 revision of a nine-axis skills
taxonomy for data scientists, plus tooling to plot and self-assess against it.
No app, no server, no build step. Everything is static files: Markdown for the
taxonomy/rubric, self-contained HTML for the interactive tools, one Python
script (stdlib only) to regenerate the static SVG.

Read [`README.md`](README.md) first — it explains the nine axes, the six
archetypes, and how the pieces fit together. [`skills-assessment.md`](skills-assessment.md)
is the taxonomy rationale; [`skill-level-rubric.md`](skill-level-rubric.md) is
the behaviorally-anchored 0–4 rating rubric all the tooling implements.

## Key files

| File | Role |
|---|---|
| `README.md` | Entry point — axes, archetypes, how to use everything. |
| `skills-assessment.md` | Taxonomy rationale: what changed from the old framework and why. |
| `skill-level-rubric.md` | **Source of truth for scoring.** Rung-by-rung ladders for all nine axes, the four calibration rules (artifact / failure-mode / outsider / half-step), the Programming verification cap, the AI Agents currency decay, and the archetype-matching procedure. Any scoring logic in the HTML tools must trace back to this file. |
| `ds-skills-explorer.html` | Interactive radar-chart explorer — nine sliders, presets, comparison overlay, SVG/PNG export. Manual self-rating, no calibration logic. |
| `baseline-skill-test.html` | Scored quiz version of the rubric — ladder questions per axis, automatic artifact/failure-mode/outsider/verification-cap/currency-decay adjustments, then plots the result on the same radar chart and exports an SVG + YAML portrait. |
| `make_svg.py` | Regenerates `ds-skills-radar.svg` from the `SKILLS`/`CLUSTERS` lists at the top of the file. Stdlib only: `python3 make_svg.py`. |
| `ds-skills-radar.svg` | Standalone hand-editable radar of the sample profile (named SVG groups: `rings`, `axes`, `cluster-arcs`, `profile`, `labels`, `new-badges`). |
| `vis-design-rationale.md` | Why the radar chart looks and behaves the way it does. |

## Conventions when editing

- **No build system.** `ds-skills-explorer.html` and `baseline-skill-test.html`
  are single files — inline `<style>` and `<script>`, no bundler, no external
  requests, no dependencies. Keep it that way; they need to work offline and
  off a USB stick.
- **The nine axes are canonical and ordered.** Both HTML tools and `make_svg.py`
  each define their own `SKILLS` array in the same fixed order:
  `[stats, aifound, agents, prog, dataeng, viz, comm, story, domain]`. This
  order is also the vector order used for the archetype presets in
  `skill-level-rubric.md` §6 and the README. If you add/reorder an axis, update
  it consistently across all three files plus the rubric and README tables.
- **Theming.** Both HTML tools share the same CSS-variable scheme (`--surface-1`,
  `--page`, `--series-1`/`--series-2`, `--c-analytical`/`--c-aiera`/`--c-eng`/
  `--c-human`, etc.), driven by `prefers-color-scheme` with a `data-theme`
  override hook. Reuse these variables rather than introducing new hard-coded
  colors, so the tools stay visually consistent and both themes stay correct.
- **Radar-drawing code is duplicated on purpose.** `ds-skills-explorer.html`
  and `baseline-skill-test.html` each carry their own copy of the SVG polar
  helpers (`pt`, `angle`, `el`, `drawChart`/`draw`) rather than sharing a
  module, to preserve the single-file-no-dependencies property. When fixing a
  rendering bug, check whether it applies to both files.
- **Scoring changes belong in `skill-level-rubric.md` first.** If a rung
  wording, calibration rule, or adjustment formula (verification cap, currency
  decay) needs to change, update the rubric prose, then propagate the change
  into `baseline-skill-test.html`'s data/scoring functions. Don't let the two
  drift.
- **`skills-assessment.md` and `skill-level-rubric.md` are living documents,
  not settled standards** (see each file's own "Status" section) — the AI
  Agents & Frameworks axis in particular is expected to need revision soonest.

## Previewing

Everything renders by opening the HTML files directly in a browser — no
server needed:

```bash
open ds-skills-explorer.html
open baseline-skill-test.html
```

To regenerate the static SVG after editing `make_svg.py`:

```bash
python3 make_svg.py
```

## Git remotes in this local clone

- `origin` → `nickperrotta27/ds-skills-inventory` (personal fork, push access).
- `upstream` → `vanderbilt-data-science/ds-skills-inventory` (source of truth,
  read-only — no push access). Fetch from `upstream` to pick up changes;
  push branches to `origin`; open PRs from `origin` branches against
  `upstream:main` when a change is ready to propose.
