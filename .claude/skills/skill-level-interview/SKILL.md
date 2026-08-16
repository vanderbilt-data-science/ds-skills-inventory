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

Run end-to-end once against a real interview (issue #16) — interview,
scoring, archetype matching, and results page all worked as written,
including the "your own shape" archetype fallback on an early-career
profile where no preset was within 1.0 mean difference.

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

For each axis, finalize the tentative score from the interview log against
the ladder text in `skill-level-rubric.md` §3 — re-read the rows for that
axis now rather than relying on memory of how the conversation felt.

### Placing the number

- Start from the highest level where the evidence log actually clears the
  bar: the ladder's "you are here when" text is satisfied, and for level ≥1
  a real artifact was named.
- Drop to the half step below when the evidence is real but not yet
  independent or consistent — the same half-step rule used live in the
  interview.
- If the person's own framing outran their evidence — confident language,
  no artifact, no failure story — place at the level the evidence supports,
  not the level they implied. This is where the ceiling illusion gets
  corrected; it has to happen here, after the conversation, because
  correcting it live would have told them what you were scoring for.
- Carry the `evidenced` / `estimated` tag through unchanged. Don't upgrade
  it just because you're now more confident in your own read — that tag
  describes the evidence, not your conclusion.

### The two §4 adjustments

Apply these only after every axis has a base score, using the rubric's own
§4 formulas.

**Programming.** Combine the interview's two dial scores:
`axis = min(mean(A, B), B + 1)`. Report the combined number as the axis
score, but keep A and B individually in the notes — "agentic delivery is a
4, unaided fluency is a 1" and a flat "2" are the same number and a
completely different story, and the next-steps section (§4 below) needs the
real one.

**AI Agents & Frameworks.** Using the recency answer gathered in the
interview, subtract 0.5 for every six months since their last sustained
hands-on period with current tooling, floored at 1 if they were ever at 2 or
above. No decay if they're currently active. Record the raw, pre-decay score
in the notes too — "you're rusty" and "you never got here" call for
different next steps.

### Output of this phase

A finalized nine-value vector, in the axis order
`[stats, aifound, agents, prog, dataeng, viz, comm, story, domain]` (matches
the rubric's §6 archetype-vector order), where each axis carries:

- the score (half-steps allowed)
- `evidenced` or `estimated`
- a one-line rationale — the artifact, or the named absence of one
- for Programming and AI Agents specifically, the pre-adjustment components
  (A/B, or the raw pre-decay score)

This vector is what archetype matching and the results page (§3 and §4
below) consume.

## 3. Archetype matching

Uses the six presets and the matching procedure defined in
`skill-level-rubric.md` §6. Re-read that table now rather than from memory —
the preset vectors are exactly the kind of thing that's easy to transpose a
digit in, and a wrong preset value silently produces a wrong nearest match.

### Procedure

1. Take the finalized nine-value vector from §2 (Scoring) above.
2. For each of the six presets, compute the mean absolute difference: sum
   `|your_score - preset_score|` across the nine axes, divide by 9.
3. The preset with the smallest mean difference is the nearest archetype.
4. If two presets land within 0.2 of each other, report both — "you sit
   between X and Y." The rubric calls this common and fine; it is not a tie
   that needs breaking.
5. If every preset's mean difference exceeds 1.0, report "your own shape"
   instead of forcing a match to the closest-but-still-far preset. The
   rubric explicitly sanctions this outcome, and picking a bad match here
   would relabel real information (a genuinely unusual profile) as noise.

### Output

Carry forward: the nearest archetype name(s), the mean-difference value(s),
and the specific axes where the person diverges most from that archetype.
The results page's next-steps section (§4 below) needs the divergence, not
just the label — "a Builder except two levels behind on Communication" is
the useful sentence, not "you're a Builder."

## 4. Producing results

Assemble the finalized data from §2 (Scoring) and §3 (Archetype matching)
into the JSON shape documented in `scripts/render_results.py`'s docstring —
nine axes in the fixed order, each axis carrying its score, its
`evidenced`/`estimated` tag, a one-line rationale, and a next-step note (see
below) — plus the archetype match. Then run:

```
python3 scripts/render_results.py <input.json> <output.html>
```

This calls `render_radar_svg()` from the repo's `make_svg.py` (the same
function that draws the site's own chart, see the `make_svg.py` refactor)
and writes a standalone, self-contained results page: radar, archetype
match, and a per-axis notes table.

### Writing the next-step note

For each axis, name the single most useful thing to do next — concretely,
the gap between what the evidence log showed and the next rung's "you are
here when" text in `skill-level-rubric.md` §3. "Ship one Skill someone else
installs" beats "get better at agents." If the axis is `estimated` rather
than `evidenced`, the honest next step is often just naming the artifact
that's missing, not a bigger ambition.

### Handing it back

Once the page is written, hand the file to the person directly — attach or
send it rather than only describing it in chat, since the radar chart is the
point of this whole exercise. If the running environment has no file-delivery
mechanism, at minimum give them the file path and read the notes table back
to them in the conversation.
