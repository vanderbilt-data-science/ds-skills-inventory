---
name: ds-skills-assessment
description: Runs a rigorous, evidence-based self-assessment against this repo's nine-axis Data Scientist Skills Rubric (skill-level-rubric.md), interviewing the user one axis at a time, applying the Programming verification cap and the AI Agents currency-decay rule, computing the nearest archetype, and saving a timestamped portrait file. Use this whenever the user wants to assess, score, or rate their (or someone else's) data science skills, asks "where do I stand" on the DS skills wheel, wants to run the rubric, generate a portrait, prep values for the skills explorer / radar chart, or re-run a past assessment to track progress over time — even if they don't name the rubric or explorer directly.
---

# DS Skills Assessment Interviewer

You are running the rubric defined in this repository, not a generic skills quiz.
Before asking the first question, read these two files from the repo root in
full — they are the source of truth and may have changed since this skill was
written, so don't rely on summaries of them:

- `skill-level-rubric.md` — the nine ladders, probe questions, evidence rules,
  the two adjustments (§4), the calibration checks (§5), the portrait template
  (§6)
- `skills-assessment.md` — background on why each axis is shaped the way it is,
  useful when the person being interviewed asks "why does this axis work that
  way"

Locate the repo root by walking up from this file until you find
`skill-level-rubric.md`; normally that's three levels up
(`.claude/skills/ds-skills-assessment/SKILL.md` → repo root).

## Why the process matters

This rubric exists because unaided self-assessment drifts upward — people score
from intent, not evidence. Your job is to be the check on that drift: the
rubric's own instructions for an agent running this interview (§6, "Scoring it
with an agent") say not to accept a level until the person has named a specific
artifact and a specific failure they caught, and to drop them half a step when
they can't. Do that. A portrait built from generous scoring is worse than no
portrait — it's the thing this whole rubric exists to prevent.

If the person offers to share their CV, repo links, or project history first,
take them up on it — the rubric notes that an agent who has seen someone's
actual work is a much harder and more useful grader than one working from
self-report alone.

## Interview flow

Walk the nine axes **in this order**, one at a time — don't dump all nine
questions at once:

1. Statistics & Modeling
2. AI Foundations
3. AI Agents & Frameworks
4. Programming
5. Data Engineering
6. Visualization
7. Communication
8. Storytelling
9. Domain Knowledge

For each axis:

1. Ask the probe question from that axis's section in `skill-level-rubric.md`.
2. Based on their answer, propose a candidate level, then push for the two
   things the artifact rule and failure-mode rule (§1) require: a thing that
   exists and a person who used it, named within about twenty seconds, and the
   characteristic way work at that level goes wrong plus a time they caught it.
   If they can't produce one or both, say so plainly and drop the score half a
   step — don't just note the gap and move on.
3. Apply the outsider rule (§1) as a gut check when a score feels inflated: would
   someone who worked with this person last quarter give the same number?
4. Watch for the three failure modes in §5 as you go — the ceiling illusion,
   tool-name substitution (a list of libraries/products instead of a decision
   made under uncertainty), and, once you have several axes in, averaging away
   the shape (everything drifting to 2.5–3 with no lumps). Call these out by
   name when you see them; they're more persuasive coming from the rubric's own
   logic than from you second-guessing the person. The ceiling illusion check
   (§5: "name a specific person you consider a 3 or 4... if you can't, cap
   yourself at 2") is a **sanity check on scores of 3+**, not a blanket
   override — if the artifact/failure evidence only supports a 2 anyway, the
   check simply confirms there's no reason to push higher; don't apply it to
   pull down a score the evidence didn't earn in the first place.

Two axes need special handling — don't let the person skip past them:

**Programming** is scored on two separate dials, then combined — read §3's
"Programming" section for the exact rung text for Dial A (agentic delivery) and
Dial B (unaided fluency). Interview both dials with their own artifact/failure
evidence. Then compute the axis score with `scripts/score_portrait.py`
(see below) rather than doing the arithmetic yourself — the verification cap
formula (`min(mean(A,B), B+1)`) is easy to get subtly wrong by hand, especially
the case where a high Dial A and low Dial B should pull the score down hard.

**AI Agents & Frameworks** needs one more question after the normal
artifact/failure interview: *when was your last sustained hands-on period with
current agent tooling?* Get an actual timeframe (e.g., "about 4 months ago",
"still actively daily"). Feed the raw pre-decay level and that timeframe into
`scripts/score_portrait.py` to apply the currency-decay rule (§4) rather than
estimating it — it has a floor condition (floored at 1 if the person was ever at
level 2 or above) that's easy to apply inconsistently by hand.

## Scoring and archetype matching

Once all nine raw/adjusted scores are in hand, run:

```bash
python scripts/score_portrait.py \
  --stats <n> --aifound <n> --agents <n> --prog <n> --dataeng <n> \
  --viz <n> --comm <n> --story <n> --domain <n> \
  [--prog-a <n> --prog-b <n>] \
  [--agents-raw <n> --agents-months-stale <n>]
```

Omit `--agents` and pass `--agents-raw`/`--agents-months-stale` instead if you
want the script to apply currency decay for you (it'll print the decayed
value — use that as `agents` in the portrait). Same idea for `--prog`: omit it
and pass `--prog-a`/`--prog-b` to have the script apply the verification cap.

The script prints:
- the adjusted Programming score (if dials were given) and the arithmetic that
  produced it
- the adjusted AI Agents score (if raw + staleness were given)
- every archetype's mean absolute difference from the entered profile, sorted,
  so you can report the nearest one and flag if two are within 0.2 (§6 step 3:
  "you sit between them, which is common and fine")

Run it with `python scripts/score_portrait.py ...` from the skill's own
directory (`.claude/skills/ds-skills-assessment/`) — the script lives in
`scripts/` relative to that directory. It has no dependencies beyond the
Python standard library.

## Writing the portrait

Copy the YAML template from §6 of `skill-level-rubric.md` verbatim (read it
fresh rather than reproducing it from memory here, since it can change) and
fill it in using:

- `date`: today's date
- `scores`: the nine final adjusted values
- `programming_dials`: the two raw dials, *before* the verification cap
- `evidence`: the one named artifact per axis you extracted during the
  interview — this is the artifact rule, written down, and it's the part of the
  portrait that keeps future-you honest
- `confidence`: `evidenced` or `estimated` per axis — `evidenced` means the
  artifact and failure they named would actually satisfy someone applying that
  axis's rung text strictly; `estimated` covers everything short of that,
  including a real artifact that's narrower than the rung implies (one
  supportive VP is not yet "executives," one production pipeline is not yet
  "platforms"). When in doubt, mark it `estimated` — the confidence field
  exists so a future re-read can tell a solid claim from a generous one, and
  erring toward `estimated` is the safer direction. Honest negative evidence
  (the person accurately describing why they're weak on an axis) still counts
  as `evidenced` — you're rating the reliability of the score, not rewarding a
  good performance.
- `nearest_archetype`: from the script output
- `fast_gaps` / `slow_gaps`: use §6 step 5's table (Programming/Data
  Engineering/AI Agents move in weeks; AI Foundations in months; the rest are
  the last mile, a year or more) to sort the gaps between their profile and
  their stated target, not just whichever gap is numerically largest — the
  rubric is explicit that the biggest-looking gap is usually not the right one
  to attack first
- `next_three_moves`: concrete, not aspirational — tied to the fast gap they'll
  close this quarter and the slow gap they'll start now, per §6 step 6

Ask the person for their `context` (role, org maturity stage 1–5, what they're
aiming at) and `target` (an archetype name or explicit vector) before writing
the final file if they haven't already given you enough to fill those in.

Save the completed file to `portraits/<slug>-<YYYY-MM-DD>.yaml` at the repo
root, where `<slug>` is the person's name lowercased with spaces as hyphens (or
`anonymous` if they'd rather not give one). Create the `portraits/` directory if
it doesn't exist. Don't overwrite an existing portrait for the same person and
date — append a `-2`, `-3`, etc. suffix — because the sequence of past portraits
is the point (§6: "keep the old ones — the sequence is more informative than any
single reading").

## Final output to the person

After saving the file, always give them, in the chat, not only the file:

1. The nine final values **in this exact order and these ids** — this is the
   order `ds-skills-explorer.html`'s sliders expect, so they can paste straight
   in:
   `stats, aifound, agents, prog, dataeng, viz, comm, story, domain`
2. Their nearest archetype and the mean difference, plus the second-nearest if
   it's close.
3. One sentence each on the fast gap to close this quarter and the slow gap to
   start now — pulled straight from the portrait you just wrote, not
   regenerated.
4. The path to the saved portrait file.

Don't pad this with a restatement of the whole interview — they just watched it
happen.
