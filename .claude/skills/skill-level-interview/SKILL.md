---
name: skill-level-interview
description: Conducts an adaptive, evidence-based interview to place someone on the 9-axis Data Scientist Skills Inventory (Statistics & Modeling, AI Foundations, AI Agents & Frameworks, Programming, Data Engineering, Visualization, Communication, Storytelling, Domain Knowledge), scores each axis 0-4 per skill-level-rubric.md, and produces a radar-chart results page with next-step notes. Use this skill whenever someone asks to be interviewed, assessed, or evaluated against the ds-skills-inventory rubric, asks "what level am I" on these axes, wants a skills radar/portrait generated from a conversation rather than self-picked numbers, or wants to administer this assessment to someone else.
---

# Skill Level Interview

Places a person on the nine-axis ladder in
[`skill-level-rubric.md`](../../../skill-level-rubric.md) by interviewing them —
never by asking them to pick a number. See that file for the axis definitions,
the four calibration rules (artifact, failure-mode, outsider, half-step), the
§4 adjustments, and the §6 archetypes; this skill is the procedure for
applying them through conversation instead of a self-scored worksheet.

## Status

Scaffold only. Sections below are being filled in incrementally (see the
project's task list / issue #16) — do not treat gaps as finished behavior.

## 1. Interview flow

Before the first question, read `skill-level-rubric.md` §2 and §3 in full. You
need the ladder text and each axis's probe question in mind, but the
interview itself is a conversation, not the rubric's questionnaire read
aloud — reword freely, follow tangents, and skip ahead if someone has already
answered a later question in passing.

### Ground rules (why they matter)

- **Never state a number, level name, or rubric term to the interviewee**
  during the interview — no "0-4", no "Applied/Independent", no "artifact
  rule." The rubric's own §5 names the ceiling illusion and anchoring as the
  main ways self-assessment goes wrong; telling someone what you're scoring
  for lets them perform to it instead of just answering.
- **Never ask "what level would you give yourself" or "how would you rate
  this."** That is the exact self-report this skill exists to replace. Ask
  about the work instead and place them yourself.
- If someone asks mid-interview "so what level is that," deflect once,
  honestly: "Let's finish the interview — I'll show you the full picture at
  the end, with the reasoning."
- Open with a short framing message so this doesn't feel like a trick: tell
  them you'll be asking about specific things they've built or done, not
  asking them to rate themselves, and that some questions will probe the same
  ground from a different angle on purpose — that's normal, answer naturally
  rather than trying to spot the "right" answer.

### Per-axis procedure

Work through the nine axes in the order given in §3 of the rubric (Programming
carries two dials — Agentic delivery and Unaided fluency — ask both). For each
axis:

1. **Open with the axis's probe question**, adapted to conversational
   phrasing and to what you already know about them from earlier answers.
2. **Let them answer in their own words first.** Don't interrupt to steer
   toward evidence yet — the unprompted framing (do they lead with a tool
   name, a project, a feeling of confidence?) is itself a signal.
3. **Apply the four calibration rules as natural follow-ups**, not as a
   checklist recited to them:
   - *Artifact* — "What's a specific example — something that exists, and
     who used it?" If they can't name one within a beat or two, that's
     information, not a prompt to keep fishing.
   - *Failure-mode* — "Where does that kind of work usually go wrong? Has it,
     for you — and how did you catch it?"
   - *Outsider* — "If I asked someone you worked with last quarter to
     describe this, would they say it the same way?"
   - *Half-step* — hold the question open if their evidence sounds like "I've
     done this once" or "I can do it when someone else sets it up" — that's
     the `x.5` case, not a full level either direction.
4. **For Programming**, run Dial A and Dial B as distinct threads — what gets
   shipped through an agent versus what they can read/write/debug unaided —
   since they combine mathematically later and conflating them loses
   information the verification cap needs.
5. **For AI Agents & Frameworks**, also ask when they last did sustained,
   hands-on work with current tooling (not just when they learned it) — the
   currency-decay adjustment in scoring needs a real timeframe, not a vibe.
6. **Move on once you have a placement within a half-step**, or after roughly
   3-5 exchanges, whichever comes first. Don't manufacture certainty an axis
   doesn't have — if evidence stays thin after a fair chance, that's an
   `estimated` placement (§5's evidence audit), not a stalled interview.

### Running log

Keep a per-axis scratchpad as you go — not shown to the interviewee — with:
the tentative score, the strongest quote or paraphrase behind it, and an
`evidenced` / `estimated` tag. This log is the direct input to §2 (Scoring)
and should be complete for all nine axes (ten threads, counting both
Programming dials) before you move to scoring.

## 2. Scoring

TODO (task #3): map transcript evidence to a 0-4 half-step score per axis,
then apply the two §4 adjustments (Programming verification cap, AI Agents
currency decay).

## 3. Archetype matching

TODO (task #4): mean-absolute-difference match against the six §6 presets,
with a "your own shape" fallback.

## 4. Producing results

TODO (task #5): hand off the scored vector to a results page — radar chart,
archetype match, per-axis next-step notes.
