# Data Scientist Skills Inventory — 2026 Revision

A refreshed skills inventory for data scientists, updating the *Data Science in
Practice* framework (Guide / Builder / Architect / Visionary) for the era of
generative AI and AI agents — plus an interactive radar-chart explorer for
plotting individual and team profiles.

![Skills radar](ds-skills-radar.svg)

## Why this exists

The original inventory was built when the scarce skills were building models
from scratch and writing the code by hand. Both have been substantially
compressed by foundation models. This revision keeps the radar-chart form the
original talk established — so old team portraits and new ones stay comparable —
while reworking what the axes measure:

| Change | Detail |
|---|---|
| **Machine Learning / Deep Learning → AI Foundations** | Value has moved from building networks to *adapting* foundation models (prompting, retrieval, fine-tuning, distillation) and knowing when a foundation model, a classical model, or a statistical model is the right instrument. |
| **New axis: AI Agents & Frameworks** | Working *through* AI rather than merely on it: decomposing problems for delegation, writing specifications, orchestrating agentic workflows (agent SDKs, MCP, RAG), supervising the result. The biggest multiplier on the wheel. |
| **SQL & data access → folded into Data Engineering** | With AI writing most first-draft queries, standalone SQL fluency no longer justifies its own spoke. |
| **Evaluation and ethics → rungs, not spokes** | When AI produces the code and the prose, verification becomes the core technical act — so it is baked into the 0–4 ladders of both AI axes rather than sitting beside them. |
| **Programming de-emphasized** | The scarce skill is reading, reviewing, and verifying code (much of it AI-generated) plus architecture judgment — not syntax fluency. |

## The nine axes

| Cluster | Axes |
|---|---|
| Analytical core | Statistics & Modeling |
| AI | AI Foundations *(absorbs ML/DL)* · **AI Agents & Frameworks** *(new)* |
| Engineering | Programming · Data Engineering *(absorbs SQL & data access)* |
| Human interface | Visualization · Communication · Storytelling · Domain Knowledge |

Human interface intentionally carries the most axes: it is where data scientists
differentiate as AI compresses the technical floor.

Every axis is scored **0–4**, from coursework-only to frontier-advancing. Full
rung-by-rung ladders for the changed axes are in
[`skills-assessment.md`](skills-assessment.md).

## The archetypes

Six presets ship with the explorer, encoding the framework's cast of characters:

| Preset | Shape |
|---|---|
| **The Guide** (Stage 1) | Human interface–heavy; now needs AI Agents nearly as much as Storytelling |
| **The Builder** (Stage 2–3) | Data Engineering plus the verification rungs of AI Foundations |
| **The Architect** (Stage 3–4) | The engineering axes plus governance as adoption scales |
| **The Visionary** (Stage 4–5) | Lives at the top of both AI axes |
| **The Toolmaker** | AI-axes specialist who equips 10× analysts |
| **Balanced 2026 DS** | The default well-rounded profile |

## What's in the repo

| File | What it is |
|---|---|
| [`ds-skills-explorer.html`](ds-skills-explorer.html) | **Interactive explorer.** Single self-contained file — no build, no dependencies. Open it in a browser. |
| [`ds-skills-radar.svg`](ds-skills-radar.svg) | Standalone vector radar of the sample profile, hand-editable, sized for projection. |
| [`make_svg.py`](make_svg.py) | Generator for the SVG. Skills, values, and clusters are a plain Python list at the top. |
| [`skills-assessment.md`](skills-assessment.md) | The taxonomy: what changed and why, the 0–4 rung ladders, implications for the archetypes, and what was considered and set aside. |
| [`vis-design-rationale.md`](vis-design-rationale.md) | Why the visualization looks and behaves the way it does — including an honest accounting of radar charts' weaknesses and how each is managed. |

## Using the explorer

Open `ds-skills-explorer.html` in any modern browser — it is a single file with
no dependencies, so downloading the repo (or just that one file) is enough.

- **Sliders are the input, the radar is the output.** Nine sliders, 0–4 in 0.5
  steps, grouped under the same cluster headings as the chart, with the numeric
  value always visible — you never have to decode the chart to read a value.
- **Presets** load any archetype in one click. Touching a slider flips the
  selector to "Custom", so a preset never silently misdescribes what's shown.
- **Comparison** overlays a second profile as a dashed, unfilled polygon — the
  core rhetorical move of the talk ("your team today vs. what Stage 4 needs").
- **Export** downloads the current chart as SVG (vector, editable) or PNG
  (paste into slides), and "Copy values" gives you the raw numbers.
- **Light and dark** are both hand-tuned; the chart follows your OS theme.

## Editing the graphics

The SVG is meant to be modified. Either edit it directly — it ships with named
groups (`rings`, `axes`, `cluster-arcs`, `profile`, `labels`, `new-badges`), a
how-to-edit comment block, and per-axis comments — or change the data and
regenerate:

```bash
python3 make_svg.py     # stdlib only; writes ds-skills-radar.svg next to the script
```

Edit the `SKILLS` and `CLUSTERS` lists at the top of `make_svg.py` to change
axes, values, or cluster colors. The explorer mirrors this: its `SKILLS` and
`PRESETS` arrays are the single place axes and archetypes are defined, and
everything else derives from them.

## Design notes worth knowing

Radar charts are a weak general-purpose form — areas mislead, axis order is
arbitrary, and comparing many shapes gets muddy. They earn their keep in one
situation: a multi-dimensional portrait of a **single entity** against a
**shared, bounded scale**, where the *shape* is the message. That is exactly
this use case. The known weaknesses are managed rather than ignored:

- Axis order is semantic, not arbitrary — axes are grouped into four clusters so
  adjacent spokes are related, and a "technical" profile bulges on one side of
  the wheel instead of producing a random star.
- Comparison is capped at two profiles, never a pile of translucent polygons.
- The enclosed area isn't asked to carry quantity: vertex dots and 0–4 rings
  keep values readable, and the fill stays light so it reads as gestalt.

Colors come from a validated palette checked for lightness band, chroma floor,
and color-vision-deficiency separation in both light and dark modes; where a
cluster color falls below the contrast floor, it is always paired with a text
legend so color never carries meaning alone. Full reasoning in
[`vis-design-rationale.md`](vis-design-rationale.md).

## Status

This is a working revision intended for discussion and use in teaching and team
planning — not a settled standard. Issues and pull requests are welcome,
particularly on the rung ladders. Two axes were deliberately *not* created
(standalone AI Evaluation and Ethics/Governance); if either becomes a hiring
differentiator worth plotting on its own, that is the first thing to revisit.

## License

[MIT](LICENSE) — use, adapt, and remix freely. Attribution to the Vanderbilt
Data Science Institute is appreciated.
