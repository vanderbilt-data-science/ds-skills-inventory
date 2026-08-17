---
name: ds-skills-rubric-scorer
description: Interviews a data scientist through the Vanderbilt DS Institute's 2026 nine-axis skills rubric (Statistics, AI Foundations, AI Agents & Frameworks, Programming, Data Engineering, Visualization, Communication, Storytelling, Domain Knowledge), correctly applies the two adjustments the rubric requires before plotting — the Programming verification cap (two dials, min(mean(A,B), B+1)) and the AI Agents & Frameworks currency decay (-0.5 per 6 months since last sustained hands-on use) — and produces a filled-in portrait plus the value array for ds-skills-explorer.html. Use this whenever someone wants a data-science skills self-assessment, wants to score themselves or a teammate on the "DS skills wheel" / "skills radar" / "skills inventory," mentions the ds-skills-inventory repo, skill-level-rubric.md, or the explorer, or asks anything about the Programming verification cap or AI Agents currency decay specifically — those two computations are easy to get wrong by hand (see ds-skills-inventory issue #37) and should always be run through scripts/score.py rather than done as mental math, even if the person only asks about one axis.
---

# DS Skills Rubric Scorer

Runs the interview-and-score workflow that `skill-level-rubric.md` §6
("Scoring it with an agent") describes, and does the one part that the
rubric's companion tool — `ds-skills-explorer.html` — can't do today: apply
the Programming verification cap and the AI Agents currency decay
correctly, instead of leaving them as hand arithmetic. That gap is
[ds-skills-inventory issue #37](https://github.com/vanderbilt-data-science/ds-skills-inventory/issues/37).
Everything here should feel like the rubric's own recommended exercise,
just packaged so it's repeatable and the arithmetic can't drift.

## Before starting

Read `references/rubric-ladders.md` once — it has the exact probe question,
rungs, and evidence rules for all nine axes, reproduced from
`skill-level-rubric.md`. Don't paraphrase the rungs from memory partway
through the interview; open the reference and read the ladder for the axis
in front of you. The wording (what counts as evidence, what doesn't, the
named miscalibration) is doing real work — it's what stops the interview
from turning into a form someone fills out on autopilot.

If the person has a CV, a GitHub profile, or a project history available,
skim it first. The rubric itself notes that an interviewer who has seen the
commits is a much harder grader than the person would be on their own — it
makes the artifact rule bite instead of being rhetorical.

## The interview

**One axis at a time, in order:** Statistics & Modeling, AI Foundations, AI
Agents & Frameworks, Programming, Data Engineering, Visualization,
Communication, Storytelling, Domain Knowledge. For each:

1. Ask the probe question from the ladder.
2. Let them answer, then push for the specific two things the rubric
   requires before a level counts: **a named artifact** (a thing that
   exists and a person who used it — reference the artifact rule) and **a
   failure mode they caught** (reference the failure-mode rule). Don't
   accept a level until both are named. If they can't produce one within
   the conversational equivalent of twenty seconds, that's the signal to
   drop a half step, not a prompt to keep waiting.
3. Apply the outsider rule as a sanity check when a number feels inflated:
   would a colleague from last quarter give the same score?
4. Record the level (half steps allowed) and the artifact named.

Keep this conversational, not a form. The rubric explicitly says most
people land on more half-steps than whole numbers — don't round for
tidiness. If someone's instinct is to give an easy answer, referencing the
specific evidence they lack ("what's the thing that exists and the person
who used it?") gets a truer number than repeating the question.

### Programming needs two numbers, not one

This is the axis `ds-skills-explorer.html` currently gets wrong by only
offering one slider — see issue #37. Don't ask "what level are you on
Programming." Ask the two dial questions separately, using the full A and B
ladders in the reference file:

- **Dial A (agentic delivery):** what can they get built and shipped by
  directing agents?
- **Dial B (unaided fluency):** what can they read, write, and debug with
  the agent turned off?

Both get named artifacts and failure modes independently — someone can
have a real A=3 story and a real B=1 story, and both need evidence. Do not
compute the combined score yourself; that's what `scripts/score.py` is for
(see below). Once you have the score, tell them plainly whether the cap
was binding — i.e., whether their combined score is lower than the simple
average of their two dials would suggest, and why (reading code well is
what lets you catch what the agent got wrong; you don't get credit above
that for shipping volume alone). That sentence is the actual point of
this axis in the 2026 revision — say it out loud, don't just report a
number.

### AI Agents & Frameworks needs one more number

Ask two extra questions beyond the normal ladder walk:

- How many months since their last *sustained* hands-on period with
  current agent tooling? ("Sustained" — not one demo six months ago; the
  rubric means real, regular delegation.)
- Was their peak level, ever, at 2 or above? (This determines whether the
  decay floor in §4 applies — see the note in `scripts/score.py` about the
  rubric leaving the sub-2 case ambiguous. Ask it as its own question
  rather than assuming; don't infer it from their current raw score, which
  may itself already be depressed by disuse.)

Report both the raw (undecayed) score and the decayed score, and say the
decay amount out loud with the reason: "no other axis on the wheel decays
this way, and the rubric means it — a workflow learned in 2024 is
archaeology if it hasn't been touched since."

## Scoring — always run the script, never do this arithmetic by hand

Once all nine axes (seven direct + two computed) have raw interview
answers, build the input JSON described at the top of
`scripts/score.py` and run it:

```bash
python3 skills/ds-skills-rubric-scorer/scripts/score.py input.json
```

(Or pipe JSON to it with `-` for stdin if that's more convenient than a
temp file.) This computes:

- The Programming score via the verification cap, and whether the cap was
  binding.
- The AI Agents score via currency decay, with the ambiguity flag if the
  person's peak was below 2 (report that flag to them — it's a real gap in
  the published rubric, not a bug in this skill).
- The nearest archetype via mean absolute difference against the six
  presets (Balanced 2026 DS, The Guide, The Builder, The Architect, The
  Visionary, The Toolmaker), including whether two presets are close
  enough that they sit between them, or far enough from all six that
  they're their own shape.
- The 9-value array in explorer order, ready to paste into the sliders at
  `ds-skills-explorer.html` (or read off `copy_values_format`, which
  matches the explorer's own "Copy values" button output).

Never eyeball `min(mean(A,B), B+1)` or the decay arithmetic — that's
exactly the failure mode this skill exists to close. If the script isn't
runnable in the current environment (no Python available), do the
arithmetic by hand as a fallback, show your work, and say plainly that it
wasn't verified by the script, so the person knows to double-check it.

## Calibration pass

Before finalizing, run the three checks in `references/rubric-ladders.md`
("Calibration checks"): ceiling illusion, tool-name substitution, averaging
away the shape. If the nine raw numbers span less than 1.5 total, say so
and re-run the artifact rule on the two highest and two lowest before
moving on — that compression is usually real and worth catching.

## Deliver the portrait

Fill in the YAML template from `references/portrait-template.md` using the
script's output for `scores`, `programming_dials`, `agents_decay`, and
`nearest_archetype`. Ask the person for the remaining human-judgment
fields the script can't compute: `target` (what they're aiming at),
`fast_gaps` / `slow_gaps` (use the gap-timing table in the same reference —
Programming/Data Engineering/AI Agents move in weeks, AI Foundations in
months, the rest in a year or more), `preference` (what they actually
enjoy — the rubric is explicit this matters as much as capability), and
`next_three_moves`.

Give them the finished YAML block, and separately give them the
`explorer_array` values with a one-line reminder: paste those into the
sliders at the live explorer
(https://vanderbilt-data-science.github.io/ds-skills-inventory/ds-skills-explorer.html)
to get the exported SVG, since that export — not this conversation — is
the artifact worth keeping per §6 Step 2 of the rubric.
