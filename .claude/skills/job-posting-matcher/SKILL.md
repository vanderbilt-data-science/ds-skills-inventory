---
name: job-posting-matcher
description: Score a pasted job posting against this repo's 9-axis data-scientist skills rubric (skill-level-rubric.md) and compare it to the user's own completed skill portrait to compute a match score and a prioritized, fast-vs-slow gap breakdown. Use this whenever the user pastes or references a job posting/listing and asks anything like "how well do I match this job," "am I qualified for this role," "what am I missing for this position," "should I apply to this," or "how do my skills stack up against this posting" — even if they don't say "rubric," "portrait," or "match score" explicitly. Requires the user's own completed portrait (skill-level-rubric.md §6 scores block) to compare against; if they don't have one, say so and ask for it rather than guessing their skill level.
---

# Job Posting Matcher

Score a job posting against the ds-skills-inventory rubric, then compare it to the user's own skill portrait to answer "how well do I actually match this job, and what's genuinely missing."

## Why this exists

`skill-level-rubric.md` already has a rigorous way to place a *person* on nine axes: the ladders in §3, evidence-based, artifact-anchored. This skill applies that same rigor to a *job posting* instead of a person's spoken answers — same ladders, same "no evidence, no credit" discipline — so the two vectors end up directly comparable on the scale the rest of this repo already uses.

## Before you start: two required inputs

1. **The user's own portrait.** A completed self-assessment following the portrait template in `skill-level-rubric.md` §6 — specifically its `scores:` block (nine 0–4 values, half-steps allowed, already adjusted per §4's verification cap and currency decay). This skill does not interview the user or estimate these scores itself. If the user hasn't given you a portrait, ask for it — don't guess, and don't quietly substitute a "reasonable" profile. A portrait without evidence behind it defeats the entire point of the rubric.
2. **The job posting text.** Ask the user to paste the posting (title, description, requirements). Very short or vague postings — a one-line title, no real requirements — usually don't carry enough evidence to score honestly. Say so rather than inventing detail to fill in the gaps.

## Step 1 — Load the rubric

Read `skill-level-rubric.md` at the root of this repository — specifically §3 (the nine ladders) and §6 (Step 3's archetype-matching method, Step 5's axis-speed table). Read `skills-assessment.md` too if any axis's scope is ambiguous from the ladder alone (e.g., exactly what "Data Engineering" covers now that SQL folded into it). Also confirm the canonical axis order and labels from `ds-skills-explorer.html`'s `SKILLS` array (near the top of its `<script>` block) — your output in Step 4 must match these labels exactly, verbatim, including punctuation: "AI Agents & Frameworks", not "AI Agents and Frameworks" or just "Agents".

## Step 2 — Score the posting

For each of the nine axes, read its full ladder in §3 — the rung descriptions, the "evidence that counts" / "evidence that doesn't" notes, and the miscalibration warning — and ask: what in *this posting's actual text* would place it at each rung?

- **Score 0–4, whole numbers only** — not the half-steps a person's self-assessment uses. A posting's text is coarser evidence than someone's own lived account of their work; a whole number is the honest level of precision here, and a half-step would be false confidence.
- **No textual evidence for an axis → score it 0.** Don't infer a Storytelling requirement from "communicates well" alone if there's nothing about audience or narrative; don't infer Bayesian statistics from "data-driven." Apply the same discipline the rubric's artifact rule applies to people: if you can't point at the phrase, it doesn't count.
- **Write a one-line justification per axis**, naming the specific phrase or requirement that drove the score (or "no evidence in posting" for a 0). This is what makes the score checkable instead of a black box — show it in your output, don't compute it silently and only report the number.

## Step 3 — Compute the match

- **Per-axis gap** = job score − portrait score, for all nine axes. Positive means the posting wants more than the user currently has; negative means the user exceeds what's asked.
- **Match score** = mean absolute gap across all nine axes — the exact method `skill-level-rubric.md` §6 Step 3 already uses for archetype matching. Lower is closer; say so explicitly when you report it, since a number like "3.2" reads as good to someone who doesn't know the scale is inverted.
- **Speed classification**, for every axis with a nonzero gap, using §6 Step 5's table:
  - **Fast (weeks):** Programming, Data Engineering, AI Agents & Frameworks
  - **Medium (months):** AI Foundations
  - **Slow (year+, the "last mile"):** Statistics & Modeling, Visualization, Communication, Storytelling, Domain Knowledge

  Lead your written summary with the slow-axis gaps even when they're numerically smaller than a fast-axis gap — that's the rubric's own "read against the grain" point (§6 Step 5): a slow gap needs to start now regardless of size, while a fast gap will likely close through ordinary work with the role.

## Step 4 — Output

Give the user, in this order:

1. **A short written verdict** — the match score (with the "lower = closer" reminder), then 2–4 sentences naming the axes that matter most: the biggest slow-axis gap (the thing to start now) and the biggest fast-axis gap (will likely close quickly regardless) — not a flat ranked list of all nine.
2. **A per-axis table** — axis, user's score, job's required score, gap, direction, speed class, one-line justification for the job's score.
3. **Two paste-ready blocks**, each nine lines of `Label: value` using the exact labels from Step 1 (e.g. "Statistics & Modeling: 3"), clearly labeled so the user knows exactly where each goes in the explorer's "Load values" panel:

   Paste this into **Load values → Target: Portrait (base profile)**:
   ```
   Statistics & Modeling: 3
   AI Foundations: 3
   AI Agents & Frameworks: 3
   Programming: 2
   Data Engineering: 2
   Visualization: 3
   Communication: 3
   Storytelling: 3
   Domain Knowledge: 2
   ```

   Paste this into **Load values → Target: Comparison overlay** (name the series after the job title):
   ```
   Statistics & Modeling: 4
   AI Foundations: 3
   AI Agents & Frameworks: 2
   Programming: 3
   Data Engineering: 3
   Visualization: 2
   Communication: 3
   Storytelling: 1
   Domain Knowledge: 3
   ```

Do not reformat, abbreviate, round differently, or reorder these two blocks relative to what Step 1 established — the explorer's parser matches on exact label text per line. Extra whitespace is harmless; a renamed, abbreviated, or reordered axis label means that axis silently fails to load.
