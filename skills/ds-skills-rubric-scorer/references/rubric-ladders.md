# Rubric Ladders (verbatim from skill-level-rubric.md)

Source of truth: `skill-level-rubric.md` in the ds-skills-inventory repo
(Vanderbilt Data Science Institute, 2026 revision, MIT licensed). This file
reproduces the sections needed to run the interview so the skill works even
when it isn't sitting next to the original repo. If the two ever disagree,
the repo file is authoritative — check it if it's available.

## The four honesty rules (apply throughout)

**The artifact rule.** For any level ≥1 the person must be able to name **a
thing that exists and a person who used it** — a repo, a model in
production, a dashboard someone opens, a talk with an audience, a Skill a
colleague installed. If they can't name it within twenty seconds, drop a
half step. Class projects are level 0 evidence on every axis.

**The failure-mode rule.** They are at level *N* only if they can describe
the characteristic ways work at level *N* goes wrong, and a time they caught
it. Knowing a technique places someone a level below using it under
conditions where it can fail.

**The outsider rule.** Would a colleague from last quarter give the same
number? If the answer needs a paragraph of context, use the number they'd
give.

**The half step.** `x.5` means *past the lower level on real evidence, not
yet consistent or independent at the next one.* It's the honest place for
"I've done it once" and "I can do it when someone sets it up for me." Most
people land on more half steps than whole ones — that's the scale working.

## What the levels mean, generally

| Level | Name | What it means anywhere on the wheel |
|---|---|---|
| **0** | **Exposure** | Coursework, tutorials, demos, reading. Seen it done. No non-class use. |
| **1** | **Applied** | Used it on at least one real problem with real consequences. Works when the path is normal; needs help when it breaks. |
| **2** | **Independent** | Does this reliably alone on real work. Recognizes common failure modes and repairs them. Someone else's work is safe in their hands. |
| **3** | **Designing / leading** | Designs the approach for others, sets the standard, handles novel/hard cases, teaches it. The person others are sent to. |
| **4** | **Frontier** | Advances the state of practice — novel methods, tools others adopt, recognition beyond the organization. |

Not seniority, not a grade. A first-year student can sit at 2 on AI Agents;
a ten-year analyst can sit at 1 on Data Engineering. A 1 is real and
employable on most axes. Three or more 4s is a sign to re-read the artifact
rule — level 4 is rarer than it looks.

---

## The nine ladders

Each gives the probe question, the rungs, what counts as evidence, and the
miscalibration people actually make.

### Statistics & Modeling

> **Probe:** One course, two, or beyond into Bayesian? Can you build the
> model that holds everything else equal — so you can answer whether the
> campaign worked once seasonality and the acquisition are factored out?

| L | You are here when |
|---|---|
| 0 | Coursework or none. Run a test/regression when told which one. |
| 1 | One to two courses' worth. Applied inferential stats or regression to ≥1 real question, with help picking the method; reports effects more confidently than uncertainty. |
| 2 | Chooses and defends the specification yourself — controls confounds, handles seasonality and repeated measures, checks assumptions, reports uncertainty honestly. Comfortable with multiple regression and extensions; has met Bayesian reasoning and can say what a prior is doing. |
| 3 | Uses frequentist and Bayesian where each fits; designs the study, not just the analysis — experiments, quasi-experimental designs, causal identification and its assumptions. Uses a Bayesian lens on AI/ML behavior. Others bring designs before collecting data. |
| 4 | Research-grade. Develops/extends methods, publishes or reviews, consulted beyond the organization. |

Evidence that counts: an analysis whose *specification* changed a decision;
a design written before data existed; a documented "this data cannot answer
that question." Evidence that doesn't: number of models fit, libraries
known, Kaggle placement. Miscalibration: "I've run a lot of models in
Python" is a 1 — AI writes the code now, the specification is the skill.
**Slow axis** — moves by study, not tooling.

### AI Foundations

> **Probe:** Could you explain a transformer to someone — and name a
> decision you would make differently because of what you understand?

| L | You are here when |
|---|---|
| 0 | Uses models without a mechanistic account. Coursework only. |
| 1 | Has applied classical ML and off-the-shelf foundation models to real problems; can explain the machinery at block-diagram level — tokens/embeddings, attention, next-token prediction, pre-training vs. fine-tuning vs. inference. |
| 2 | Solid across major method families; can name which instrument fits (foundation model, classical ML, statistical model, or none). Runs error analysis and basic evals. Can explain why a model hallucinates, what context length costs, what sampling settings change. Decisions cite mechanism, not vibes. |
| 3 | Deep grasp of behavior and limits. Designs eval suites; knows when adaptation (retrieval, fine-tuning, distillation) is worth it; reasons about distribution shift, eval gaming, silent degradation. Responsible-AI judgment — fairness definitions, privacy, model risk, regulatory exposure. Can turn a paper or model card into a decision. |
| 4 | Advances the frontier — novel methods, research-grade work others build on. |

Evidence that counts: a build/buy/wait call and its reasoning; an eval
suite designed; a time AI was recommended *against*. Evidence that doesn't:
following AI news, having opinions about releases. Miscalibration:
explaining attention is level 1, not 2 — level 2 is where understanding
starts changing decisions. Evaluation lives on this axis deliberately.

### AI Agents & Frameworks

> **Probe:** Are you actually delegating real work — and how do you know
> the result is right?

The axis that never finishes; score the **practices**, not product names.

| L | You are here when |
|---|---|
| 0 | Chat-style use only. Paste a question in, copy an answer out. Still running everything. |
| 1 | **Productive daily delegation.** Works inside an agentic harness on real tasks. Writes *specifications* (goal, constraints, acceptance criteria), not requests. Knows what to hand off vs. do by hand. Keeps durable project context. Reviews everything that comes back. |
| 2 | **Builds capability, not just output.** Authors reusable Agent Skills encoding own expertise, used by someone else. Connects agents to real systems (MCP and equivalents); builds retrieval and tool-use workflows. **Verification is in the loop** — tests, expected record counts, acceptance criteria the agent checks itself against. Work is version-controlled and shareable. |
| 3 | **Designs systems of agents.** Multi-step/multi-agent workflows with real orchestration — decomposition, parallel subagents, async/long-running work supervised rather than watched. Evals, guardrails, monitoring designed in (cost/latency budgets, permission boundaries, prompt-injection exposure). Knows how long-running work drifts and how to stop it. Ships packaged capability others install. |
| 4 | Creates novel agent architectures, frameworks, or standards others adopt. |

Evidence that counts: a Skill someone else installed and used; a
specification that produced a working deliverable without them in the loop;
an eval that caught a regression before a human did; an agent run they
killed, and why. Evidence that doesn't: hours in a chat window; a list of
tools with accounts. Miscalibration: shipping something that works but
can't be explained-how-verified is a **1**, not a 2 — verification is the
rung. Level 3–4 practitioners write very little code by hand; that's
expected, which is why Programming carries the verification cap.

**Currency note:** standards here turn over on a scale of months. The
specifics will be stale; the ladder is written so the rungs still hold:
delegate → package capability with verification → design and supervise
systems → invent the pattern.

### Programming

> **Probe:** How many languages — and were you the person people brought
> their bugs to? Then: what have you shipped through an agent that you
> could defend line by line?

Scored on **two dials**, combined — see `../scripts/score.py` and the
Programming step in SKILL.md for how this skill collects and computes it.
The act that never changed is *thinking about how to solve the problem and
knowing when the answer is correct*; what changed is the altitude at which
it's done.

**Dial A — Agentic delivery.** What can be gotten built and shipped by
directing agents.

| A | |
|---|---|
| 0 | None. |
| 1 | Scripts, notebooks, small analyses via an agent; can follow and modify what came back. |
| 2 | Multi-file projects with tests and a real git workflow; can direct a refactor, decompose a build into tasks, tell when the agent went sideways. |
| 3 | Production-grade systems: architecture decisions made and defended, CI, review standards for AI-generated code, several agents in flight at once. |
| 4 | Systems, tooling, or standards other builders adopt. |

**Dial B — Unaided fluency.** What can be read, written, and debugged with
the agent turned off.

| B | |
|---|---|
| 0 | None. |
| 1 | One language; can read a script and change it. |
| 2 | Two-plus languages, or real depth in one. Reads unfamiliar code and locates the bug. Was the person others brought bugs to. |
| 3 | Designs and writes non-trivial software by hand — data structures, performance, debugging under pressure. |
| 4 | Expert engineer; separate-engineering-team tier. |

**Axis score = min( mean(A, B), B + 1 ).** The mean is delivered capability;
`B + 1` is the **verification cap** — capped at one level above what can be
read, because reading code well is what catches what the agent got wrong.
A=4, B=1 scores **2.0**, not 2.5: ships a lot, can't certify any of it.

Evidence that counts: a bug found in AI-written code the tests missed; a
pull request rejected and why; the last thing written by hand and why it
was worth doing that way. Miscalibration (two opposite errors): scoring
high on A because things run, without ever verifying; or scoring low
because "I don't really write code anymore" — if directing agents to
production-quality output *and reviewing it*, that's the skill and it's
credited. What isn't credited is losing the ability to check.

### Data Engineering

> **Probe:** Have you ever gotten data all the way to a dashboard yourself?

Absorbs SQL and data access. "Garbage in, garbage out" no longer holds the
way it did, so the axis forked: for ML solutions, and differently, for AI
solutions.

| L | You are here when |
|---|---|
| 0 | No hands-on data access experience. Someone hands you a file. |
| 1 | Can get the data needed — SQL basics (AI-assisted fine), APIs, file wrangling, warehouse queries. One-off extracts, checked. |
| 2 | Working knowledge of warehouses/lakes. Gets grain and joins right, runs data-quality checks before trusting anything, documents what's learned about a source. Takes data end to end — source to dashboard or model input — alone. Understands both forks: structured pipelines for ML, corpora/indexes/retrieval for AI. |
| 3 | Builds pipelines and orchestration that survive without them — scheduling, idempotency, monitoring, lineage, quality at scale. Handles messy/unstructured sources for AI use; handles access, governance, cost. |
| 4 | Designs platforms — streaming, very large scale, specialized infrastructure. |

Evidence that counts: a pipeline still running, unbabysat for a month; a
data-quality failure caught before a stakeholder saw it; metadata someone
else relied on. Miscalibration: one good AI-written SQL query is a 1 — this
axis is about grain, quality, durability, not query syntax.

*Note on fit, not skill:* a data engineering deliverable can be finished —
the pipeline runs. A pure DS/AI solution never can be; there's always
another increment. Some people find that genuinely uncomfortable and drift
toward this axis — a legitimate discovery about fit, worth noting in the
portrait rather than folding into the number.

### Visualization

> **Probe:** Have you built something genuinely compelling for a real
> problem?

| L | You are here when |
|---|---|
| 0 | Default charts, chart type chosen by habit or library default. |
| 1 | Makes correct, readable charts for real work — right form for the data type, labels, units, scales that don't mislead. |
| 2 | Designs for perception and cognitive load: signal in a channel that pops (position, color) not one that must be searched (shape); categorical counts stay inside working memory; continuous quantities get continuous encodings. Annotates so the chart makes its own point; designs for color-vision deficiency and contrast. |
| 3 | Builds visual *systems* — dashboards and interactive tools that hold up in real use, consistent encodings across a family of views, tuned to audience and medium. Can justify every design decision, including the rejected ones. |
| 4 | Original visual forms or tooling others adopt; recognized design work. |

Evidence that counts: a chart that changed a decision; a redesign and its
reason; a visualization someone else reused. Miscalibration: "I know
Plotly/ggplot/D3" is tool fluency, not this axis. **Slow axis.**

### Communication

> **Probe:** Could you stand up in front of executives and defend it?

| L | You are here when |
|---|---|
| 0 | Reports results informally, to peers, in the order the work was done. |
| 1 | Presents clearly to a friendly technical audience; writes a readable summary. |
| 2 | Presents to non-technical stakeholders and executives: leads with the decision, states uncertainty honestly, takes hard questions without over-claiming. Written work gets acted on. |
| 3 | Builds the case *and* the coalition — negotiating scope, bringing IT/security/legal in as collaborators, getting solutions actually adopted. Sent into the difficult room. |
| 4 | Shapes the conversation beyond the organization — invited talks, published work, external authority. |

Evidence that counts: a decision that changed because of the presentation;
an uncomfortable result delivered intact; a hostile stakeholder who ended
up sponsoring the work. Miscalibration: confidence isn't this axis; being
understood and believed is.

### Storytelling

> **Probe:** Could you explain something complex to a non-technical
> audience as a story?

| L | You are here when |
|---|---|
| 0 | Recites findings in the order produced. |
| 1 | Structures a narrative — setup, tension, resolution — for a report or talk. |
| 2 | Makes genuinely complex material intuitive for a lay audience through concrete story, analogy, example, without falsifying it. Can retarget the same story for different audiences. |
| 3 | Builds the narrative that carries an initiative — the framing others repeat back unprompted. Teaches it. Uses story to move an organization, not just explain a result. |
| 4 | Recognized communicator; framing becomes the shorthand others use. |

Evidence that counts: an analogy someone else repeated back; an audience
that could retell the point the next day; a talk they were invited back
for. Miscalibration: slides are not a story. **Slowest axis on the wheel.**

### Domain Knowledge

> **Probe:** Is there a field you actually know?

| L | You are here when |
|---|---|
| 0 | None. Would need someone to explain what the columns mean. |
| 1 | Knows one domain's vocabulary and main processes well enough to follow a subject-matter expert and ask reasonable questions. |
| 2 | Knows a domain well enough to ask the *right* question, spot a number that cannot be true, challenge a stakeholder's framing. Knows how the work is actually done, where the data comes from and how it gets dirty, the compliance basics. |
| 3 | The domain's own experts treat this person as a peer. Understands incentives, politics, what the numbers do to the people they describe, plus regulatory depth where it applies. |
| 4 | An expert in the domain in their own right, independently of the data science. |

Evidence that counts: a number rejected on domain grounds, and being right
about it; a question asked that the SMEs hadn't thought to ask.
Miscalibration: the most over-claimed axis on the wheel. One project in
healthcare is not healthcare domain knowledge — it's a 1. **If the person
works across several domains, score the strongest and list the others at
their real levels** — averaging destroys the information.

---

## Calibration checks (apply after the raw pass, §5 of the rubric)

**The ceiling illusion.** Can't see a level never met. People without a 3
in the room routinely score themselves 3 because they've hit the edge of
what they've seen. *Antidote:* for each axis, name a specific person
considered a 3 or 4, and say what they do differently. If no one comes to
mind, cap at 2.

**Tool-name substitution.** Listing tools instead of judgment. Every
ladder above is written in terms of decisions made and failures caught
specifically so a list of frameworks can't be mistaken for a level.

**Averaging away the shape.** Scoring ~2.5 everywhere because nothing
feels extreme. Real profiles are lumpy. If the nine numbers span less than
1.5 total, the scores have almost certainly compressed toward the middle —
re-run the artifact rule on the two highest and two lowest.

Two optional checks: **the peer pass** (have a colleague score the same
nine ladders cold, compare — full-level disagreements are the most
informative part of the exercise) and **the evidence audit** (mark each
axis `evidenced` or `estimated`; an estimated 3 and an evidenced 2 are not
the same claim).
