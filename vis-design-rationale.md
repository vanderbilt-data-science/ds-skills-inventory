# Skills Radar — Visualization Design Rationale

Why the 2026 skills inventory visualization (`ds-skills-radar.svg` and
`ds-skills-explorer.html`) looks and behaves the way it does.

## Why a radar chart at all

Radar charts are a weak general-purpose form — areas mislead, axis order is
arbitrary, and comparing more than two shapes gets muddy. They earn their
keep in exactly one situation: a **multi-dimensional portrait of a single
entity against a shared, bounded scale**, where the *shape* is the message.
That is precisely the skills-inventory use case, and it is the convention the
original *Data Science in Practice* deck established — the audience already
reads "big lopsided blob toward Communication" as "this is a Guide." Keeping
the form preserves continuity with the talk while everything inside it
modernizes.

The known weaknesses are managed rather than ignored:

- **Axis order is meaningful, not arbitrary.** The nine axes are grouped into
  four clusters (Analytical core → AI → Engineering → Human interface) so
  adjacent axes are semantically related. Correlated skills sitting next to
  each other makes the enclosed shape more honest — a "technical" data
  scientist bulges on one side of the wheel instead of producing a random
  star.
- **Comparison is capped at two.** The explorer allows one profile plus one
  dashed comparison overlay, never a pile of translucent polygons.
- **The area isn't asked to carry quantity.** Vertex dots and the 0–4 rings
  keep the actual values readable; the fill is kept light (22% opacity) so it
  reads as gestalt, not measurement.

## Geometry and scale

The 0–4 scale with four concentric rings matches the original deck's radar,
so old team portraits and new ones stay comparable. Rings are hairline
(`#e1e0d9`) with only the outer ring slightly darker — the grid recedes,
the data polygon dominates. Ring values are labeled once, small and muted,
on the vertical axis rather than on every ring. Axes start at top
(12 o'clock) and run clockwise at 40° intervals (360/9).

## Color

Colors come from a validated palette (the dataviz reference palette), applied
by job:

- **The profile is one series → one hue.** Blue (`#2a78d6` light /
  `#3987e5` dark) fills the polygon; identity is carried by the title and
  legend, not by color-coding values. Text never wears the series color.
- **The comparison overlay is the second categorical slot** (orange), drawn
  dashed and unfilled — visually subordinate, distinguishable by pattern as
  well as hue, so the pair survives color-vision deficiency and grayscale
  printing.
- **Cluster arcs use the first four categorical slots** (blue, orange, aqua,
  yellow) in fixed order. This 4-color sequence was run through the palette
  validator: it passes lightness band, chroma floor, CVD separation
  (worst adjacent pair ΔE 9.1 light / 8.4 dark, above the ≥8 target), and
  the normal-vision floor in both modes. Aqua and yellow sit below 3:1
  contrast on the light surface, which the method permits only with relief —
  hence every arc is paired with a visible text legend and the cluster names
  also appear as slider group headers, so color never carries meaning alone.

## Chart chrome

Ink follows the standard roles: near-black primary ink for axis labels,
secondary gray for subtitles and legends, muted gray for ring numbers.
Text is sized for projection in a large room, not for desktop reading:
axis labels are semibold at roughly 1/12 of chart height (23px in the
1360-wide SVG, 20px in the explorer), so category names stay legible from
the back of the room; only the ring numbers — reference chrome, not
content — stay small.
Typeface is the system sans throughout — no display face — and slider values
use tabular figures so they align as they change. The "NEW" badge on
AI Agents & Frameworks is a small tinted pill rather than a color-coded
label, deliberately quiet: it annotates the taxonomy change without
competing with the data.

## Dark mode

Dark mode is **selected, not inverted**: every color has a hand-picked dark
step from the same ramps (e.g. profile blue moves from `#2a78d6` to
`#3987e5`), validated against the dark surface `#1a1a19`. All chart colors
are read from CSS custom properties at draw time, so the OS theme switch
re-renders the chart correctly, and the four dark-mode cluster colors all
clear 3:1 contrast on the dark surface.

## Interaction design (the explorer)

- **Sliders are the input, the radar is the output.** Direct manipulation
  with immediate feedback makes the tool usable in a live talk — drag three
  sliders and the archetype appears. Sliders are grouped under the same
  cluster headers (with matching color dots) as the chart's arcs, values
  0–4 in 0.5 steps, with the numeric value always visible beside each
  slider — the chart never has to be decoded to know a value.
- **Presets encode the archetypes** (Guide, Builder, Architect, Visionary,
  Toolmaker, plus a Balanced 2026 DS) so the talk's cast of characters is
  one click away; touching any slider flips the preset to "Custom" so a
  preset never silently lies about what's displayed.
- **Comparison** loads any preset as the dashed overlay — the core rhetorical
  move of the talk ("here's your team today vs. what Stage 4 needs") built
  directly into the tool. Both series appear in a legend; hover tooltips on
  vertices and labels show exact values for both.
- **Export produces the vector graphic.** Download SVG serializes the
  currently displayed chart (title, values, overlay) as a standalone file —
  which is how "a good graphic, vector defined, that I can modify" stays
  true for *any* profile, not just the sample one. PNG export covers
  paste-into-slides.

## Editability

The standalone SVG is hand-editable by design: named groups (`rings`,
`axes`, `cluster-arcs`, `profile`, `labels`, `new-badges`), a comment block
at the top explaining the geometry, per-axis comments, and a companion
generator (`make_svg.py`) where skills, values, and clusters are a plain
Python list — change the list, rerun, done. The explorer mirrors this: the
`SKILLS` and `PRESETS` arrays at the top of the file are the single place
axes and archetypes are defined; everything else is derived.
