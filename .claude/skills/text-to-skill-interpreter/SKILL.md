---
name: text-to-skill-interpreter
description: Adjusts a data scientist's 9-axis skill self-assessment using narrative interview or reflection text, instead of (or in addition to) direct slider values. Reads free-text answers to reflection/mock-interview questions, scores them against the ladders in skill-level-rubric.md, and emits a structured JSON observation log with per-axis observed level, confidence, and evidence — plus proposed score adjustments against a baseline portrait. Use whenever a user gives narrative/reflective text about their work and wants their self-assessment checked, scored, or adjusted from that text rather than from numbers they typed themselves.
---

# Text-to-Skill Interpreter

Implements issue #17: turn narrative text (interview answers, written
reflections) into evidence-backed adjustments to a
[9-axis skill portrait](../../../skill-level-rubric.md), rather than relying
only on numbers the person picked themselves.

This skill has no UI and produces no chart. Its output is a JSON log — see
[`schema/observation-log.schema.json`](schema/observation-log.schema.json) —
meant to be applied to a portrait (§6 of `skill-level-rubric.md`) or plotted
in the explorer by hand. Someone else's job is turning the log into pixels;
this skill's job is turning text into a defensible number and a receipt for
it.

## Why this is an agent skill, not a script

Placing someone on a rung is a judgment call — it requires reading a
paragraph, deciding whether it clears the **artifact rule** (a named thing a
named person used), and telling a level-1 claim ("I know what a transformer
is") from a level-2 one ("that's why I decided against fine-tuning"). That is
exactly the kind of evaluation this repository already delegates to an agent
in `skill-level-rubric.md` §6, "Scoring it with an agent." This skill is that
delegation, formalized: the instructions below **are** the interpreter: there
is no separate parser to keep in sync with the rubric, because the rubric
file is read directly, every time.

## Inputs

1. **The rubric.** Read [`skill-level-rubric.md`](../../../skill-level-rubric.md)
   in full before scoring anything — the nine ladders (§3), the two
   adjustments (§4), and the three calibration failure modes (§5). Re-read it
   per session; do not rely on memory of a prior run.
2. **The narrative text.** One of:
   - Free-form written reflection.
   - Mock-interview transcript (Q&A).
   - Answers to the nine probe questions in §3 of the rubric, asked one axis
     at a time if the user hasn't already written something.
3. **Optional baseline.** A prior portrait's `scores:` block (see the
   template in `skill-level-rubric.md` §6) to diff against. Without one,
   `observed_level` is reported with no `baseline_score` or `delta`.

If there is no narrative text yet, elicit it: ask the probe question for one
axis at a time (§3 of the rubric has the exact question for each), the same
way the rubric's own "Scoring it with an agent" prompt describes — push for
the specific artifact and the specific failure caught before accepting a
level.

## Procedure

1. **Segment the text by axis.** A sentence can speak to more than one axis
   (a debugging story is Programming *and* possibly AI Foundations); an axis
   can be supported by more than one sentence. Tag every segment with the
   axis key(s) it's evidence for:
   `stats · aifound · agents · prog · dataeng · viz · comm · story · domain`.
2. **Score each supported axis against its ladder** (rubric §3). For each:
   - Find the **highest rung with real evidence in the text** — not the
     rung the person's tone implies.
   - Apply the **artifact rule**: no named thing + named user in the text →
     cap at the rung below, and drop a half step if the text only asserts
     capability without naming either.
   - Apply the **failure-mode rule**: crediting rung *N* requires the text to
     describe how work at that level goes wrong and a time the speaker
     caught it — not just that they know the technique.
   - Apply the **half step** (`x.5`) when the text clears the lower rung but
     is a one-off, or dependent on someone else setting it up.
   - Watch for the axis-specific miscalibrations the rubric calls out
     explicitly (e.g. "I've run a lot of models" → Statistics 1, not 2;
     "I know Plotly" → tool fluency, not Visualization; one project in a
     domain → Domain Knowledge 1, not higher). Quote the rubric's own
     miscalibration line in `rationale` when it applies — it's the sharpest
     available justification.
3. **Set confidence**, independent of the level:
   - `high` — a specific, checkable artifact and a specific failure caught.
   - `medium` — a named artifact but no failure mode, or vice versa.
   - `low` — plausible but generic; would not survive the outsider rule
     ("would a colleague from last quarter give the same number?").
   Low confidence is a valid, useful output — it is not a reason to omit the
   observation, only a reason not to auto-apply it (see step 5).
4. **Apply the two special adjustments where the text supports them:**
   - **Programming verification cap.** If the text distinguishes agent-
     directed delivery from unaided fluency, score dial A and dial B
     separately per rubric §3/§4 and compute
     `axis = min(mean(A,B), B+1)`. If the text doesn't separate the two
     dials, score the single `prog` axis conservatively and note in
     `rationale` that the cap could not be verified from this text alone.
   - **Agents currency decay.** If the text gives or implies a date for the
     last sustained hands-on period with agent tooling, apply the −0.5 per
     six months rule (floored at 1 if ever ≥2) and record the decay in
     `rationale`. If no date is recoverable from the text, do not guess —
     leave `agents` undecayed and say so.
5. **Compute adjustments against the baseline**, if one was supplied:
   `delta = observed_level − baseline_score`. Do **not** propose an
   adjustment (omit the axis from `adjustments`) when confidence is `low`
   and `|delta| ` would exceed 0.5 — a low-confidence read shouldn't move a
   score by more than half a step. State this explicitly when it happens.
6. **List axes the text touched but couldn't score** (mentioned, but no
   artifact, no failure mode, nothing quotable) in `insufficient_evidence`
   rather than forcing a number — this is the text-based equivalent of the
   rubric's instruction to drop a level when you can't name evidence within
   twenty seconds.
7. **Emit the JSON log** conforming to
   [`schema/observation-log.schema.json`](schema/observation-log.schema.json).
   Validate structurally with
   [`scripts/validate_log.py`](scripts/validate_log.py) before returning it:
   `python3 scripts/validate_log.py <path-to-log.json>`.
8. **Follow with a short plain-text summary** (not part of the JSON): which
   axes moved, by how much, and the one piece of evidence you'd point to if
   challenged on each. This is the human-readable receipt; the JSON is the
   machine-readable one.

## Output shape (see schema for the authoritative version)

```json
{
  "session": {
    "date": "2026-08-13",
    "subject_id": "example-student",
    "source_type": "written_reflection",
    "baseline_portrait_ref": null
  },
  "observations": [
    {
      "axis": "agents",
      "observed_level": 1.5,
      "confidence": "medium",
      "evidence_snippet": "I wrote a spec for the migration script and reviewed the diff before merging",
      "rules_applied": ["artifact_rule", "half_step"],
      "rationale": "Names a real artifact (the migration script) but no described failure mode caught, so short of independent level 2."
    }
  ],
  "adjustments": [],
  "insufficient_evidence": ["domain"]
}
```

A fuller worked example is in
[`examples/example-observation-log.json`](examples/example-observation-log.json).

## Explicit non-goals

- No sentiment analysis, keyword matching, or embedding similarity — every
  score must trace to a rubric rung and a rule in §3–4, applied by reading
  the text, not by pattern-matching it.
- No silent auto-application to a portrait file. This skill proposes
  adjustments; a human (or an explicit follow-up step) decides whether to
  write them into their portrait.
- No numeric-only input. If the "narrative" is really just a list of
  self-picked numbers, this is the wrong skill — that's what the explorer
  sliders and the plain rubric walkthrough are for.
