# How the Nine Skills Relate

Answers issue [#10](https://github.com/vanderbilt-data-science/ds-skills-inventory/issues/10):
*"Comparing/contrasting different skills — explaining how they build onto one
another."* Companion to [`skills-assessment.md`](skills-assessment.md) (what
the nine axes are) and [`skill-level-rubric.md`](skill-level-rubric.md) (how to
score yourself on them). This document does neither — it looks *across* the
nine axes and asks three questions:

1. What is the one foundational ability each axis is really testing?
2. Which abilities are shared across axes — where does strength on one axis
   predict strength on another?
3. Which axes look alike but aren't, and in what order do they build on each
   other?

**[skills-relationships.svg](skills-relationships.svg)** is the diagram this
document argues for — nodes tagged with the cross-cutting abilities they
share (pills), numbered arrows for build order, keyed below.

## Method

Every claim below traces to specific language in `skill-level-rubric.md` —
its probe questions, "evidence that counts," and "miscalibration" notes are
already written in terms of underlying abilities, not tool names, which is
what makes this kind of comparison possible without inventing new categories.
Each relationship is marked:

- **[explicit]** — the rubric states the connection in words.
- **[inferred]** — a structural reading: two axes clearly depend on the same
  thing, but the rubric doesn't say so directly. Marked so you can disagree
  with it on its own terms.

## 1. One foundational ability per axis

| Axis | The ability underneath the ladder |
|---|---|
| Statistics & Modeling | Defending a *specification* — why this design controls for that confound — before or instead of just fitting a model |
| AI Foundations | Explaining model behavior at a mechanism level well enough to change a decision because of it |
| AI Agents & Frameworks | Delegating through a written specification, then verifying the result yourself rather than trusting that it ran |
| Programming | Reading and reviewing code well enough to certify what an agent produced |
| Data Engineering | Getting data end-to-end to a trustworthy destination, and knowing when it isn't trustworthy yet |
| Visualization | Choosing the encoding that makes the signal visible instead of one that has to be searched for |
| Communication | Being believed by an audience that did not arrive friendly |
| Storytelling | Framing that a listener can retell correctly the next day, without you in the room |
| Domain Knowledge | Knowing enough about how the work is actually done to catch a number that cannot be true |

These are deliberately narrower than the axis names. "Programming" the axis
covers a lot; the *ability the ladder is actually built around* — per the
rubric's own miscalibration note — is verification, not fluency.

## 2. Six abilities that cut across axes

Pulling on the "evidence that counts" and "miscalibration" language across
all nine ladders surfaces the same handful of underlying abilities recurring
under different names. These are the pills in the diagram.

| Ability | What it means | Central to | Rubric language it's drawn from |
|---|---|---|---|
| **Verification & evaluation judgment** | Catching what's wrong before someone else does | AI Foundations, AI Agents & Frameworks, Programming, Domain Knowledge | *"when AI produces the code and the prose, verification is the core technical act"* (AI Foundations); *"verification is in the loop... the actual difference between chat and an agent"* (AI Agents) |
| **Specification & decomposition** | Writing down goal, constraints, and acceptance criteria before the work starts | Statistics & Modeling, AI Agents & Frameworks | *"design the study, not just the analysis"* (Statistics); *"you write specifications rather than requests"* (AI Agents) |
| **Honest uncertainty & limits** | Stating what you don't know as clearly as what you do | Statistics & Modeling, AI Foundations, Visualization, Communication | *"report effects more confidently than uncertainty"* is the level-1 failure (Statistics); *"state uncertainty honestly"* (Communication) |
| **Audience translation** | Converting technical content for a listener who didn't do the analysis | Visualization, Communication, Storytelling | Human-interface cluster grouping; *"whether it communicates is still you"* (Visualization) |
| **Systems & durability** | Building something that keeps working without you standing next to it | AI Agents & Frameworks, Programming, Data Engineering | *"a pipeline still running that you have not babysat in a month"* (Data Engineering); *"production-grade systems... several agents in flight at once"* (Programming) |
| **Domain-grounded judgment** | Knowing enough about the field to challenge the question, not just answer it | Statistics & Modeling, Data Engineering, Domain Knowledge | *"a number you rejected on domain grounds and were right about"* (Domain Knowledge) |

Read as a matrix, **Verification** is the single busiest ability — it sits
under four axes. `skills-assessment.md` §1 says this outright for the two AI
axes: evaluation is "baked into the rungs of both AI axes... rather than a
tenth spoke." Programming and Domain Knowledge aren't named in that sentence,
but they're doing the same act under different words — reading code well
enough to catch what an agent got wrong, and knowing a domain well enough to
catch a number that can't be true, are both verification. Grouping all four
under one pill is this document's synthesis, not a rubric quote — but it's
why "evaluation" never needed its own tenth spoke: it was already going to
show up at least four times.

## 3. Where axes look alike but aren't

**Communication vs. Storytelling.** Both are audience-facing, both start
Level 0 the same way — reporting or reciting results in the order the work
happened, before any shaping — and both share the Audience-translation pill.
They diverge on mechanism: Communication is
argument — you're in the room, taking hard questions, and the win condition
is *adopted*. Storytelling is narrative — you're often *not* in the room, and
the win condition is *retold correctly*. The rubric draws this exact
distinction: Communication's Level 3 is "getting solutions actually
adopted," Storytelling's is "the framing other people repeat back to you
unprompted." Score both highly and you cover the full audience-facing
surface; score one without the other and you can persuade a room but not
survive leaving it (or vice versa).

**Programming vs. AI Agents & Frameworks — related, then inverted.** Early
on these build together: Programming's unaided-fluency dial (Dial B) is what
lets you tell whether an agent's output is right, and AI Agents Level 2 makes
"verification in the loop" a named requirement. But the rubric flags an
explicit **inversion** at the top: "level 3–4 practitioners write very little
code by hand. That is expected, and it is why the Programming axis carries a
verification cap." The two axes are correlated in the middle of the scale and
anti-correlated in the amount of hands-on coding at the top of it — only the
*verification* capability, not the code-writing capability, keeps building.

**Statistics & Modeling vs. AI Foundations — same tool, different object.**
Both use a Bayesian lens (explicit link, edge 5 in the diagram), and both
punish reporting confidence without uncertainty. They contrast in what
they're pointed at: Statistics & Modeling reasons about a population or a
campaign's effect; AI Foundations reasons about a model's behavior — "why a
model hallucinates, what context length actually costs." Someone strong on
one has the *reasoning style* half-transferred to the other, but not the
subject-matter half — which is consistent with the taxonomy keeping them as
separate axes rather than merging them.

**Data Engineering's own fork.** The axis explicitly forks in place rather
than contrasting with a neighbor: "you understand both forks: structured
pipelines for ML, and corpora, indexes, and retrieval for AI." Grain, joins,
and quality checks are the shared foundational ability; which artifact you're
securing (a warehouse table vs. a retrieval index) is what splits.

**The fast/slow contrast, which cuts across all of the above.** The rubric
already groups the nine axes by *how quickly a gap on them closes* (§6, step
5) — Programming, Data Engineering, and AI Agents move in **weeks** through
deliberate delegation; AI Foundations moves in **months** through a real
course; Statistics & Modeling, Visualization, Communication, Storytelling,
and Domain Knowledge move in a **year or more**, "study plus real projects
with real audiences. Nothing accelerates these." This is a second, orthogonal
way to contrast the nine axes — orthogonal to the pills, because two axes can
share a foundational ability (e.g., Statistics and AI Foundations both need
honest uncertainty) while sitting on opposite ends of how fast they're
learnable.

## 4. Build order

The diagram lays this out as three tiers plus one amplifier, read bottom to
top:

**Substrate** (Data Engineering, Domain Knowledge) feeds **Analytical &
technical core** (Statistics & Modeling, AI Foundations, Programming), which
feeds **Human interface — delivery** (Visualization, Communication,
Storytelling). Reliable data and real domain grounding are what make a
statistical specification or a model-selection call defensible in the first
place; the technical core's output — an estimate, an eval result, a working
system — is what Visualization and Communication then have to render for
someone else.

| # | Edge | Type | Why |
|---|---|---|---|
| 1 | Data Engineering → Statistics & Modeling | inferred | A defensible specification needs an extract you already trust |
| 2 | Data Engineering → AI Foundations | **explicit** | The axis's own "for AI" fork — corpora, indexes, retrieval — is the substrate AI Foundations work runs on |
| 3 | Domain Knowledge → Statistics & Modeling | inferred | Knowing what the data can answer is a domain judgment before it's a statistical one |
| 4 | Domain Knowledge → Communication | inferred | Domain credibility is most of what makes a hostile room listen |
| 5 | Statistics & Modeling → AI Foundations | **explicit** | *"You use a Bayesian lens to reason about AI and ML model behavior"* — Statistics & Modeling, Level 3 |
| 6 | Statistics & Modeling → Visualization | inferred | An honestly-quantified uncertainty still has to be encoded, not just estimated |
| 7 | Visualization → Communication | inferred | The chart is the artifact the room actually reacts to |

**AI Agents & Frameworks sits outside the tiers, as a multiplier, not a
rung.** This is explicit in `skills-assessment.md`: *"It is the biggest
multiplier skill on the wheel — it raises effective capacity on every other
axis."* It doesn't feed into one neighbor; it changes the ceiling on all
eight others, which is why the diagram draws it as a band underneath
everything rather than a ninth box in the stack. The one exception drawn
distinctly is the **verification cap** on Programming (§4 of the rubric) —
the specific edge where AI Agents' upper rungs actively *reduce* what
Programming is scored on (hand-written code), rather than amplifying it.

## 5. Using this with the rubric

If you're filling out the portrait template in `skill-level-rubric.md`, this
mapping gives you two consistency checks the ladders don't give you alone:

- **Pill check.** If you scored high on Verification-tagged axes (AI
  Foundations, AI Agents, Programming, Domain Knowledge) but low on all of
  them except one, ask whether that one score is really evidenced — the
  ability is the same across all four, so a real gap of more than a level
  between them is worth a second look under the artifact rule.
- **Build-order check.** A high score on a tier-2 or tier-3 axis with a
  near-zero score on everything feeding it (edges 1–7) is unusual but not
  wrong — it can mean you're operating on data or domain framing someone
  else supplied. Worth naming explicitly in the portrait's `context` field
  rather than leaving it implicit.

## Regenerating the diagram

`skills-relationships.svg` is generated by `make_relationships_svg.py`, the
same convention as `make_svg.py` for the radar: axes, pills, and edges are
plain Python lists at the top of the file — edit and rerun.

```bash
python3 make_relationships_svg.py
```
