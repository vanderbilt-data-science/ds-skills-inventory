#!/usr/bin/env python3
"""Generate ds-skills-radar.svg — an editable vector radar of the 2026 DS skills inventory."""
import math
import os

# ---- data -------------------------------------------------------------------
SKILLS = [  # (label, value 0-4, new?)  order = clockwise from top
    ("Statistics & Modeling", 3, False),
    ("AI Foundations", 3, False),          # absorbs the old Machine Learning/DL axis + evaluation
    ("AI Agents & Frameworks", 3, True),
    ("Programming", 2, False),
    ("Data Engineering", 2, False),        # absorbs SQL & data access
    ("Visualization", 3, False),
    ("Communication", 3, False),
    ("Storytelling", 3, False),
    ("Domain Knowledge", 2, False),
]
CLUSTERS = [  # (name, first axis idx, last axis idx, color)
    ("Analytical core", 0, 0, "#2a78d6"),
    ("AI", 1, 2, "#eb6834"),
    ("Engineering", 3, 4, "#1baf7a"),
    ("Human interface", 5, 8, "#eda100"),
]
N = len(SKILLS)
CX, CY, R = 680.0, 490.0, 280.0     # center, max radius (value 4)
RINGS = [1, 2, 3, 4]
ARC_R = R + 42                       # cluster arc radius
LABEL_R = R + 78

def pt(i, r):
    a = -math.pi / 2 + 2 * math.pi * i / N
    return CX + r * math.cos(a), CY + r * math.sin(a)

def fmt(x):
    return f"{x:.1f}".rstrip("0").rstrip(".")

def esc(s):
    return s.replace("&", "&amp;")

out = []
out.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1360 960" font-family="system-ui, -apple-system, \'Segoe UI\', sans-serif">')
out.append("""<!--
  Data Scientist Skills Inventory (2026) - editable radar
  HOW TO EDIT:
  * Skill values: edit the single <polygon id="profile"> points list below.
    Each vertex i sits at radius value/4 * 280 from center (520,440), angle
    -90deg + i*(360/9)deg clockwise, in the axis order listed in <g id="axes">.
    Easiest: regenerate with make_svg.py after changing values there.
  * Labels: plain <text> elements in <g id="labels">.
  * Colors: search-and-replace the hex values; cluster arcs use
    #2a78d6 / #eb6834 / #1baf7a / #eda100.
  * Delete <g id="cluster-arcs"> or <g id="new-badges"> if not wanted.
-->""")
out.append(f'<rect width="1360" height="960" fill="#fcfcfb"/>')

# title
out.append('<g id="title">')
out.append(f'<text x="680" y="56" text-anchor="middle" font-size="32" font-weight="700" fill="#0b0b0b">Data Scientist Skills Inventory</text>')
out.append(f'<text x="680" y="86" text-anchor="middle" font-size="18" fill="#52514e">2026 revision — 9 axes, scale 0–4</text>')
out.append('</g>')

# rings
out.append('<g id="rings" fill="none" stroke="#e1e0d9" stroke-width="1">')
for v in RINGS:
    dash = ' stroke="#c3c2b7"' if v == 4 else ''
    out.append(f'<circle cx="{fmt(CX)}" cy="{fmt(CY)}" r="{fmt(R*v/4)}"{dash}/>')
out.append('</g>')
# ring value labels (small, on the top axis)
out.append('<g id="ring-labels" font-size="14" fill="#898781" text-anchor="middle">')
for v in RINGS:
    out.append(f'<text x="{fmt(CX+14)}" y="{fmt(CY - R*v/4 + 5)}">{v}</text>')
out.append('</g>')

# axes
out.append('<g id="axes" stroke="#e1e0d9" stroke-width="1">')
for i, (name, _, _) in enumerate(SKILLS):
    x, y = pt(i, R)
    out.append(f'<line x1="{fmt(CX)}" y1="{fmt(CY)}" x2="{fmt(x)}" y2="{fmt(y)}"/><!-- {name} -->')
out.append('</g>')

# cluster arcs
out.append('<g id="cluster-arcs" fill="none" stroke-width="5" stroke-linecap="round">')
for name, i0, i1, color in CLUSTERS:
    step = 360 / N
    a0 = -90 + i0 * step - 14
    a1 = -90 + i1 * step + 14
    x0 = CX + ARC_R * math.cos(math.radians(a0)); y0 = CY + ARC_R * math.sin(math.radians(a0))
    x1 = CX + ARC_R * math.cos(math.radians(a1)); y1 = CY + ARC_R * math.sin(math.radians(a1))
    large = 1 if (a1 - a0) > 180 else 0
    out.append(f'<path d="M {fmt(x0)} {fmt(y0)} A {ARC_R} {ARC_R} 0 {large} 1 {fmt(x1)} {fmt(y1)}" stroke="{color}"/><!-- {name} -->')
out.append('</g>')

# cluster legend (bottom, centered)
out.append('<g id="cluster-legend" font-size="18">')
widths = [10.5 * len(n) + 42 for n, *_ in CLUSTERS]
total = sum(widths)
lx = CX - total / 2
ly = 926
for (name, i0, i1, color), w in zip(CLUSTERS, widths):
    out.append(f'<circle cx="{fmt(lx+7)}" cy="{fmt(ly-6)}" r="7" fill="{color}"/>')
    out.append(f'<text x="{fmt(lx+22)}" y="{fmt(ly)}" fill="#52514e">{esc(name)}</text>')
    lx += w
out.append('</g>')

# profile polygon
pts = " ".join(f"{fmt(pt(i, R*v/4)[0])},{fmt(pt(i, R*v/4)[1])}" for i, (_, v, _) in enumerate(SKILLS))
out.append(f'<!-- profile values: ' + ", ".join(f"{n}={v}" for n, v, _ in SKILLS) + ' -->')
out.append(f'<polygon id="profile" points="{pts}" fill="#2a78d6" fill-opacity="0.22" stroke="#2a78d6" stroke-width="2" stroke-linejoin="round"/>')
out.append('<g id="profile-dots" fill="#2a78d6">')
for i, (_, v, _) in enumerate(SKILLS):
    x, y = pt(i, R * v / 4)
    out.append(f'<circle cx="{fmt(x)}" cy="{fmt(y)}" r="4"/>')
out.append('</g>')

# axis labels
out.append('<g id="labels" font-size="23" font-weight="600" fill="#0b0b0b">')
badges = []
for i, (name, v, is_new) in enumerate(SKILLS):
    a = -math.pi / 2 + 2 * math.pi * i / N
    x = CX + LABEL_R * math.cos(a); y = CY + LABEL_R * math.sin(a)
    c, s = math.cos(a), math.sin(a)
    anchor = "middle"
    if c > 0.35: anchor = "start"
    if c < -0.35: anchor = "end"
    dy = 8
    if s < -0.85: dy = 0
    if s > 0.85: dy = 20
    out.append(f'<text x="{fmt(x)}" y="{fmt(y+dy)}" text-anchor="{anchor}">{esc(name)}</text>')
    if is_new:
        bw = 52
        bx = x - bw / 2
        if anchor == "start": bx = x
        if anchor == "end": bx = x - bw
        by = y + dy + 12
        badges.append((bx, by, bw))
out.append('</g>')
out.append('<g id="new-badges">')
for bx, by, bw in badges:
    out.append(f'<rect x="{fmt(bx)}" y="{fmt(by)}" width="{bw}" height="24" rx="12" fill="#eb6834" fill-opacity="0.14"/>')
    out.append(f'<text x="{fmt(bx+bw/2)}" y="{fmt(by+17)}" text-anchor="middle" font-size="14" font-weight="700" fill="#a63c14">NEW</text>')
out.append('</g>')

out.append('</svg>')
dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ds-skills-radar.svg")
open(dest, "w").write("\n".join(out))
print("wrote", len("\n".join(out)), "bytes ->", dest)
