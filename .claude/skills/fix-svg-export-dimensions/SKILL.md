---
name: fix-svg-export-dimensions
description: Fixes standalone SVG/PNG exports from ds-skills-explorer.html that render undersized because the exported <svg> has no explicit width/height. Use when the explorer's Download SVG or Download PNG buttons produce files that look tiny or blank outside the browser.
---

# Fix SVG export dimensions

## The bug

`ds-skills-explorer.html` draws the radar chart into `<svg id="chart" viewBox="0 0
1120 700">` (no `width`/`height` attributes) and relies on CSS
(`#chart { width:100%; height:auto }`) to size it on the page.

The `standaloneSvg()` function clones that same `<svg>` node for both the
"Download SVG" and "Download PNG" buttons:

```js
function standaloneSvg() {
  const clone = svg.cloneNode(true);
  clone.setAttribute("xmlns", svgNS);
  el("rect", { x: 0, y: 0, width: 1120, height: 700, fill: css("--surface-1") }, clone)
  clone.insertBefore(clone.lastChild, clone.firstChild);
  return new XMLSerializer().serializeToString(clone);
}
```

The page's CSS never travels with the exported file. An SVG with only a
`viewBox` and no `width`/`height` falls back to the spec default intrinsic
size (commonly 300×150) when opened standalone — double-clicked, dragged into
Illustrator/Word, or loaded as an `<img>` outside this page. The PNG export
happens to look fine because `downloadPng` explicitly draws to a
2240×1400 canvas regardless of the source's intrinsic size — but the raw SVG
download does not get that protection.

## The fix

In `standaloneSvg()`, set explicit `width`/`height` on the cloned root that
match the `viewBox` dimensions, before serializing:

```js
function standaloneSvg() {
  const clone = svg.cloneNode(true);
  clone.setAttribute("xmlns", svgNS);
  clone.setAttribute("width", "1120");
  clone.setAttribute("height", "700");
  el("rect", { x: 0, y: 0, width: 1120, height: 700, fill: css("--surface-1") }, clone)
  clone.insertBefore(clone.lastChild, clone.firstChild);
  return new XMLSerializer().serializeToString(clone);
}
```

Keep the two numbers in sync with the `viewBox` on `<svg id="chart">` — if
that viewBox ever changes, update this function too.

## How to verify

1. Open `ds-skills-explorer.html` in a browser.
2. Click **Download SVG**.
3. Open the downloaded `*-radar.svg` file directly in a new browser tab (not
   embedded in a page with sizing CSS) — it should render at full size, not
   ~300×150.
4. Confirm the file's root `<svg>` element now contains
   `width="1120" height="700"` alongside its `viewBox`.
