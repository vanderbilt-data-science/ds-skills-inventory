# Skill Level Rubric — Self-Assessment and Portrait

A rating rubric for the nine axes of the [2026 Data Scientist Skills
Inventory](skills-assessment.md). Its job is to answer one question honestly:
**what level am I on each axis, and what evidence says so?**

The [taxonomy](skills-assessment.md) says what the axes *are*. This document says
how to **place yourself on them**, how to keep the placement honest, and how to
turn nine numbers into a **portrait** — a picture of where you are, where you're
going, and which gaps are weeks of work versus years of it.

Every axis is scored **0–4** in half steps, matching the
[explorer](ds-skills-explorer.html) sliders exactly, so anything you score here
plots directly.

---

## 1. How to use this

**One pass, thirty minutes, out loud if you can.** Walk the nine ladders in
order. For each, read the probe question, find the highest level where you can
name real evidence, and write the number *and the evidence* down. Don't optimize;
the number is only useful if it's true.

Four rules keep it honest:

**The artifact rule.** For any level ≥1 you must be able to name **a thing that
exists and a person who used it** — a repo, a model in production, a dashboard
someone opens, a talk with an audience, a Skill a colleague installed. If you
can't name it within twenty seconds, drop a half step. Class projects are level
0 evidence on every axis; that is what level 0 means.

**The failure-mode rule.** You are at level *N* only if you can describe the
characteristic ways work at level *N* goes wrong, and a time you caught it.
Knowing a technique places you a level below using it under conditions where it
can fail.

**The outsider rule.** Would someone who worked with you last quarter give you
the same number? If your answer needs a paragraph of context, use the number
they'd give.

**The half step.** `x.5` means *past the lower level on real evidence, not yet
consistent or independent at the next one.* It is the honest place for "I've
done it once" and for "I can do it when someone sets it up for me." Most people
land on more half steps than whole ones. That's the scale working.

Then apply the two adjustments in §4 — the **verification cap** on Programming
and the **currency decay** on AI Agents — before you plot anything.

---

## 2. What the levels mean, generally

Every ladder in §3 is a specialization of this one. When a specific rung is
ambiguous, fall back to here.

| Level | Name | What it means anywhere on the wheel |
|---|---|---|
| **0** | **Exposure** | Coursework, tutorials, demos, reading. You have seen it done. No non-class use. |
| **1** | **Applied** | You have used it on at least one real problem with real consequences. It works when the path is normal; you need help when it breaks. |
| **2** | **Independent** | You do this reliably alone on real work. You recognize the common failure modes and repair them. Someone else's work is safe in your hands. |
| **3** | **Designing / leading** | You design the approach for others, set the standard, handle the novel and hard cases, and teach it. You are who people are sent to. |
| **4** | **Frontier** | You advance the state of practice — novel methods, tools others adopt, recognition beyond your organization. |

Two things this scale is deliberately not:

- **Not seniority.** A ten-year analyst can sit at 1 on Data Engineering. A
  first-year student can sit at 2 on AI Agents. Levels track demonstrated
  capability, not tenure or title.
- **Not a grade.** A 1 is a real, useful, employable level on most axes. Nobody
  needs nine 4s, and a profile of all 3s is usually a profile of someone who
  hasn't been honest about one of them.

**Level 4 is rarer than it looks.** On most axes, in most organizations, nobody
is at 4. If you have three or more 4s, re-read the artifact rule.

---

## 3. The nine ladders

Each ladder gives the probe question, the rungs, the evidence that counts, and
the miscalibration people actually make on that axis.

---

### Statistics & Modeling

> **Probe:** *One course, two, or beyond into Bayesian? Can you build the model
> that holds everything else equal — so you can answer whether the campaign
> worked once seasonality and the acquisition are factored out?*

| Level | You are here when |
|---|---|
| **0** | Coursework or none. You can run a test or a regression when told which one to run. |
| **1** | One to two courses' worth. You have applied inferential statistics or regression to at least one real question. You pick the method with help and report effects more confidently than uncertainty. |
| **2** | You choose and defend the specification yourself on real questions — controlling confounds, handling seasonality and repeated measures, checking assumptions, reporting uncertainty honestly. Multiple regression and its extensions are comfortable; you have met Bayesian reasoning and can say what a prior is doing. |
| **3** | You use frequentist and Bayesian methods where each fits, and you design the study, not just the analysis — experiments, quasi-experimental designs, causal identification and its assumptions. You use a Bayesian lens to reason about AI and ML model behavior. Others bring you their designs before collecting data. |
| **4** | Research-grade. You develop or extend methods, publish or review, and are consulted on statistical questions beyond your organization. |

**Evidence that counts:** an analysis whose *specification* changed a decision; a
design you wrote before data existed; a documented time you said "this data
cannot answer that question."
**Evidence that doesn't:** number of models fit, libraries known, Kaggle
placement.
**Miscalibration:** "I've run a lot of models in Python" is a 1. AI writes the
code now; the specification is the skill, and level 2 begins at the point where
you can defend one. This is a **slow axis** — it moves by study, not by tooling.

---

### AI Foundations

> **Probe:** *Could you explain a transformer to someone — and name a decision
> you would make differently because of what you understand?*

| Level | You are here when |
|---|---|
| **0** | You use models without a mechanistic account of them. Coursework only. |
| **1** | You have applied classical ML and off-the-shelf foundation models to real problems, and can explain the machinery at block-diagram level: tokens and embeddings, attention, next-token prediction, pre-training versus fine-tuning versus inference. |
| **2** | You are solid across the major method families and can name which instrument fits — foundation model, classical ML, statistical model, or no model at all. You run error analysis and basic evals. You can explain *why* a model hallucinates, what context length actually costs, and what sampling settings change. Your decisions cite mechanism, not vibes. |
| **3** | Deep grasp of behavior and limits. You design evaluation suites; you know when adaptation (retrieval, fine-tuning, distillation) is worth it and when it isn't; you reason about distribution shift, eval gaming, and silent degradation. Responsible-AI judgment is part of your work — competing fairness definitions, privacy, model risk, regulatory exposure. You can read a paper or model card and turn it into a decision. |
| **4** | You advance the frontier — novel methods, research-grade work that others build on. |

**Evidence that counts:** a build-versus-buy-versus-wait call and the reasoning
behind it; an eval suite you designed; a time you recommended *against* using AI.
**Evidence that doesn't:** following AI news; having opinions about model
releases.
**Miscalibration:** being able to explain attention is level 1, not 2. Level 2 is
where understanding starts changing decisions. Evaluation lives on this axis
deliberately — when AI produces the code and the prose, **verification is the
core technical act**, and it is not a separate spoke.

---

### AI Agents & Frameworks

> **Probe:** *Are you actually delegating real work — and how do you know the
> result is right?*

This is the axis that never finishes, and the one where the rungs move under you.
Score the **practices**, not the product names.

| Level | You are here when |
|---|---|
| **0** | Chat-style use only. You paste a question in and copy an answer out. You are still the one running everything. |
| **1** | **Productive daily delegation.** You work inside an agentic harness on real tasks. You write *specifications* rather than requests — goal, constraints, acceptance criteria — and you know what to hand off versus do by hand. You keep durable project context so the agent doesn't start cold every session. You review everything that comes back. |
| **2** | **You build capability, not just output.** You author reusable **Agent Skills** that encode your own expertise (a data store's soft spots, a workflow, a review standard) so the work is done the same correct way every time, and someone else has used one. You connect agents to real systems (**MCP** and equivalents) and build retrieval and tool-use workflows. Crucially, **verification is in the loop** — tests, expected record counts, acceptance criteria the agent checks itself against — which is the actual difference between chat and an agent. What you build is version-controlled and shareable. |
| **3** | **You design systems of agents.** Multi-step and multi-agent workflows with real orchestration: decomposition, parallel subagents, asynchronous and long-running work you supervise rather than watch. Evals, guardrails, and monitoring are designed in, not bolted on — including cost and latency budgets, permission boundaries, and prompt-injection exposure. You know how long-running agent work drifts and how to stop it. You ship packaged capability that other people in the organization install and use. |
| **4** | You create novel agent architectures, frameworks, or standards — the patterns other people adopt. |

**Evidence that counts:** a Skill someone else installed and used; a
specification you wrote that produced a working deliverable without you in the
loop; an eval that caught a regression before a human did; an agent run you
killed, and the reason.
**Evidence that doesn't:** hours logged in a chat window; a list of tools you
have accounts for.
**Miscalibration:** shipping something that works but that you can't explain how
you verified is a **1**, not a 2 — the verification is the rung. And note the
inversion at the top of this axis: level 3–4 practitioners write very little code
by hand. That is expected, and it is why the Programming axis carries a
verification cap (§4).

**Currency note.** Standards and harnesses in this space turn over on a scale of
months — portable Skill/plugin formats across vendors, MCP as the connective
layer, spec-driven development as the working method, subagent orchestration, and
eval literacy as the differentiating skill are the shape of it as of mid-2026.
The specifics *will* be stale. The ladder is written so that when they change,
the rungs still hold: delegate → package capability with verification → design
and supervise systems → invent the pattern.

---

### Programming

> **Probe:** *How many languages — and were you the person people brought their
> bugs to? Then: what have you shipped through an agent that you could defend
> line by line?*

Programming is at a pivot point, so it is scored on **two dials** and combined.
The act that never changed is *thinking about how to solve the problem and
knowing when the answer is correct*; what changed is the altitude at which you do
it.

**Dial A — Agentic delivery.** What you can get built and shipped by directing
agents.

| A | |
|---|---|
| 0 | None. |
| 1 | Scripts, notebooks, and small analyses via an agent; you can follow what came back and modify it. |
| 2 | Multi-file projects with tests and a real git workflow; you can direct a refactor, decompose a build into tasks, and tell when the agent has gone sideways. |
| 3 | Production-grade systems: architecture decisions you make and defend, CI, review standards specifically for AI-generated code, several agents in flight at once. |
| 4 | Systems, tooling, or standards that other builders adopt. |

**Dial B — Unaided fluency.** What you can read, write, and debug with the agent
turned off.

| B | |
|---|---|
| 0 | None. |
| 1 | One language; you can read a script and change it. |
| 2 | Two or more languages, or real depth in one. You can read unfamiliar code and locate the bug. You were the person others brought their bugs to. |
| 3 | You design and write non-trivial software by hand — data structures, performance, debugging under pressure. |
| 4 | Expert engineer; the separate-engineering-team tier. |

**Axis score = min( mean(A, B), B + 1 ).**

The mean is your delivered capability. The `B + 1` term is the **verification
cap**: you cannot claim more than one level above what you can read, because
reading code well is what lets you catch what the agent got wrong. A profile with
A=4 and B=1 scores 2.0, not 2.5 — that person ships a lot and cannot certify any
of it.

**Evidence that counts:** a bug you found in AI-written code that the tests did
not catch; a pull request you rejected and why; the last thing you wrote by hand,
and why it was worth doing by hand.
**Miscalibration:** the two most common errors are opposite. One is scoring high
on A because things run, without ever having verified them. The other is scoring
low because "I don't really write code anymore" — if you are directing agents to
production-quality output and can review it, that *is* the skill, and this axis
credits it. What it does not credit is losing the ability to check.

---

### Data Engineering

> **Probe:** *Have you ever gotten data all the way to a dashboard yourself?*

Absorbs SQL and data access. "Garbage in, garbage out" no longer holds the way it
did — unstructured and even dirty data can now be put to work — so the axis
forked: you do this **for ML solutions** and, differently, **for AI solutions.**

| Level | You are here when |
|---|---|
| **0** | No hands-on data access experience. Someone hands you a file. |
| **1** | You can get the data you need — SQL basics (AI-assisted is fine), APIs, file wrangling, warehouse queries. One-off extracts that you check. |
| **2** | Working knowledge of warehouses and lakes. You get grain and joins right, run data-quality checks before trusting anything, and document what you learn about a source. You can take data end to end — source to dashboard or to model input — by yourself. You understand both forks: structured pipelines for ML, and corpora, indexes, and retrieval for AI. |
| **3** | You build pipelines and orchestration that survive without you — scheduling, idempotency, monitoring, lineage, quality at scale. You handle messy and unstructured sources for AI use, and you handle access, governance, and cost. |
| **4** | You design platforms — streaming, very large scale, specialized infrastructure. |

**Evidence that counts:** a pipeline still running that you have not babysat in a
month; a data-quality failure you caught before a stakeholder saw it; metadata
you wrote that someone else relied on.
**Miscalibration:** one good AI-written SQL query is a 1. This axis is about
grain, quality, and durability — not query syntax, which is exactly the part that
got compressed.

**A note on fit, not skill:** a data engineering deliverable can be *finished* —
the pipeline runs, the boxes are checked. A pure data science or AI solution
never can be; you always stop before perfect. Some people find that genuinely
uncomfortable and drift toward this axis. That is a legitimate discovery about
fit, and it belongs in your portrait (§6) rather than in this number.

---

### Visualization

> **Probe:** *Have you built something genuinely compelling for a real problem?*

| Level | You are here when |
|---|---|
| **0** | Default charts, chart type chosen by habit or by whatever the library did. |
| **1** | You make correct, readable charts for real work — right form for the data type, labels, units, and scales that don't mislead. |
| **2** | You design for perception and cognitive load: the signal is encoded in a channel that pops (position, color) rather than one that has to be searched (shape); categorical counts stay inside working memory; continuous quantities get continuous encodings. You annotate so the chart makes its own point, and you design for color-vision deficiency and contrast — color never carries meaning alone. |
| **3** | You build visual *systems* — dashboards and interactive tools that hold up in real use, consistent encodings across a family of views, tuned to audience and medium (a room with a projector is not a laptop). You can justify every design decision, including the ones you rejected. |
| **4** | Original visual forms or tooling that others adopt; recognized design work. |

**Evidence that counts:** a chart that changed a decision; a redesign and the
reason for it; a visualization someone else reused.
**Miscalibration:** "I know Plotly / ggplot / D3" is tool fluency, not this axis.
AI will produce the chart; whether it *communicates* is still you. **Slow axis** —
it moves by study of perception and by real audiences.

---

### Communication

> **Probe:** *Could you stand up in front of executives and defend it?*

| Level | You are here when |
|---|---|
| **0** | You report results informally, to peers, in the order you did the work. |
| **1** | You present clearly to a friendly technical audience and write a summary people can read. |
| **2** | You present to non-technical stakeholders and executives: you lead with the decision, state uncertainty honestly, and take hard questions without over-claiming. Your written work gets acted on. |
| **3** | You build the case *and* the coalition — negotiating scope, bringing IT, security, and legal in as collaborators rather than obstacles, and getting solutions actually adopted. You are the person sent into the difficult room. |
| **4** | You shape the conversation beyond your organization — invited talks, published work, external authority. |

**Evidence that counts:** a decision that changed because of how you presented
it; an uncomfortable result you delivered intact; a stakeholder who started
hostile and ended up sponsoring the work.
**Miscalibration:** confidence is not this axis; being understood and believed
is. Level 3 is where getting something *adopted* company-wide lives — which in
practice means security and IT, early and as partners.

---

### Storytelling

> **Probe:** *Could you explain something complex to a non-technical audience as
> a story?*

| Level | You are here when |
|---|---|
| **0** | You recite findings in the order you produced them. |
| **1** | You structure a narrative — setup, tension, resolution — for a report or a talk. |
| **2** | You make genuinely complex material intuitive for a lay audience through concrete story, analogy, and example, without falsifying it. You can retarget the same story for different audiences. |
| **3** | You build the narrative that carries an initiative — the framing other people repeat back to you unprompted. You teach it. You use story to move an organization, not just to explain a result. |
| **4** | Recognized communicator; your framing becomes the shorthand others use. |

**Evidence that counts:** an analogy of yours that someone else repeated back;
an audience that could retell your point the next day; a talk you were invited
back for.
**Miscalibration:** slides are not a story. This is the axis most often scored
from intent rather than effect — and it is the one AI has raised the value of
most, because everyone can now produce the artifact and almost no one can frame
the problem. **Slowest axis on the wheel.**

---

### Domain Knowledge

> **Probe:** *Is there a field you actually know?*

| Level | You are here when |
|---|---|
| **0** | None. You would need someone to tell you what the columns mean. |
| **1** | You know one domain's vocabulary and main processes well enough to follow a subject-matter expert and ask reasonable questions. |
| **2** | You know a domain well enough to ask the *right* question, to spot a number that cannot be true, and to challenge a stakeholder's framing. You know how the work is actually done, where the data comes from and how it gets dirty, and the compliance basics. |
| **3** | The domain's own experts treat you as a peer. You understand incentives, politics, and what the numbers do to the people they describe — plus regulatory depth where it applies. |
| **4** | You are an expert in the domain in your own right, independently of the data science. |

**Evidence that counts:** a number you rejected on domain grounds and were right
about; a question you asked that the SMEs hadn't thought to ask.
**Miscalibration:** the most over-claimed axis on the wheel. One project in
healthcare is not healthcare domain knowledge; it is a 1. Count years and
delivered projects, not exposure. If you work across several domains, **score
your strongest and list the others in the portrait** — a 2 in one domain plus a
1 in three others is a real and useful shape, and averaging it destroys the
information.

---

## 4. The two adjustments

Apply both before plotting.

**The verification cap (Programming).** `axis = min( mean(A,B), B + 1 )`. Stated
plainly: **very advanced data scientists code almost exclusively through agents,
and that is the correct end state — but a well-rounded data scientist keeps the
manual skill, because it is what makes the review real.** Right now the board is
balanced and you need both sides; some employers still ask you to write it by
hand, and reading code well is what lets you catch what the agent got wrong.
The cap encodes exactly that and nothing more.

**Currency decay (AI Agents & Frameworks).** Subtract **0.5 for every six months
since your last sustained hands-on period** with current tooling, floored at 1 if
you were ever at 2 or above. No other axis decays this way. Statistics you
learned in 2019 is still statistics; an agent workflow you learned in 2024 is
archaeology. If you are re-scoring after six quiet months and want to keep the
number, the fix is not an argument — it is a week of real delegation.

---

## 5. Calibrating against yourself

Three failure modes account for nearly every bad self-assessment.

**The ceiling illusion.** You cannot see a level you have never met. People
without a 3 in the room routinely score themselves 3 because they have hit the
edge of what they have seen. Antidote: for each axis, name a specific person you
consider a 3 or 4 and say what they do that you don't. If you can't name one,
cap yourself at 2.

**Tool-name substitution.** Listing tools instead of judgment. Every ladder above
is written in terms of decisions made and failures caught, precisely so that a
list of frameworks can't be mistaken for a level.

**Averaging away the shape.** Scoring 2.5 everywhere because nothing feels
extreme. Real profiles are lumpy. If your nine numbers span less than 1.5 total,
you have almost certainly compressed toward the middle — re-run the artifact rule
on your two highest and two lowest.

Two optional checks worth the time:

- **The peer pass.** Have a colleague who has worked with you score you cold on
  the same nine ladders, then compare. Disagreements of a full level are the most
  informative output of this entire exercise.
- **The evidence audit.** Mark each axis `evidenced` or `estimated`. Carry that
  mark into the portrait. An estimated 3 and an evidenced 2 are not the same
  claim, and only one of them belongs on a résumé.

---

## 6. Building the portrait

The nine numbers are input. The **portrait** is the output — and it is the thing
worth keeping.

**Step 1 — Score and adjust.** Nine ladders, both dials for Programming, then
apply the verification cap and currency decay.

**Step 2 — Plot.** Enter the values in the [explorer](ds-skills-explorer.html),
put your name on the title, and export the SVG. That file is the artifact.

**Step 3 — Match an archetype.** Compute the mean absolute difference between
your vector and each preset, in axis order
`[stats, aifound, agents, prog, dataeng, viz, comm, story, domain]`:

| Preset | Vector |
|---|---|
| Balanced 2026 DS | `3, 3, 3, 2, 2, 3, 3, 3, 2` |
| The Guide | `2, 2, 3, 1, 1, 4, 4, 4, 2` |
| The Builder | `3, 2, 3, 3, 3, 2, 2, 3, 2` |
| The Architect | `2, 3, 3, 4, 4, 2, 2, 2, 3` |
| The Visionary | `3, 4, 4, 2, 2, 2, 3, 3, 4` |
| The Toolmaker | `2, 4, 4, 3, 2, 2, 2, 1, 2` |

Smallest mean difference is your nearest archetype; if two are within 0.2 you sit
between them, which is common and fine. A mean difference above 1.0 from every
preset means you are your own shape — also fine, and worth writing down as such.
The archetypes describe *where you'd thrive*, and they are as much about what you
enjoy as what you can do.

**Step 4 — Overlay a target.** Load the archetype you're aiming at (or the
profile the organization's next maturity stage would require) as the comparison
overlay. The dashed polygon is the assignment.

**Step 5 — Read the gaps against the grain.** This is the part people get wrong.

| Gap on | Moves | What moves it |
|---|---|---|
| **Programming, Data Engineering, AI Agents** | **Weeks.** Visibly, once you're working with agents seriously. | Deliberate delegation on real projects; building and reusing Skills; verifying everything. |
| **AI Foundations** | **Months.** | A real course, then consolidated by use — you understand a model better once you have had to decide with it. |
| **Statistics & Modeling, Visualization, Communication, Storytelling, Domain** | **A year or more.** The last mile. | Study plus real projects with real audiences. Nothing accelerates these. |

So a profile is not only a picture of where you are — read against that grain, it
tells you where the remaining work actually is, **and it is usually not where
people expect.** The instinct is to attack the biggest gap. The better move is
usually: start the slow axes now because they take a year, and let the fast axes
rise through the work you were going to do anyway.

**Step 6 — Write five sentences.** Where you are, what you're aiming at, the one
fast gap you'll close this quarter, the one slow axis you'll start now, and what
you actually enjoy doing. That last one matters as much as the rest, and you
generally won't know it until you've carried real projects.

### Portrait template

Keep this with the exported SVG. Timestamp it, and keep the old ones — the
sequence is more informative than any single reading.

```yaml
portrait:
  name:
  date: 2026-08-12
  context:            # role, organization maturity stage (1-5), what you're aiming at
  scores:             # 0-4, half steps, post-adjustment
    stats:
    aifound:
    agents:
    prog:
    dataeng:
    viz:
    comm:
    story:
    domain:
  programming_dials:  # before the verification cap
    agentic:
    unaided:
  evidence:           # one named artifact per axis - the artifact rule, written down
  confidence:         # per axis: evidenced | estimated
  domains:            # scored domain, plus the others at their real levels
  nearest_archetype:  # + mean difference
  target:             # archetype or stage you're aiming at, as a vector
  fast_gaps:          # closable in weeks - prog, dataeng, agents
  slow_gaps:          # the last mile - start now, measure in years
  preference:         # what you actually enjoy; where you'd stop before perfect
  next_three_moves:
```

### Scoring it with an agent

Appropriately for the axis this revision added, the assessment itself is a good
delegation. Point an agent at this repository and have it interview you:

> Read `skill-level-rubric.md` and `skills-assessment.md`. Interview me one axis
> at a time. For each, ask the probe question, then push for the specific
> artifact and the specific failure I caught — do not accept a level until I have
> named both, and drop me half a step when I can't. Apply the verification cap
> and the currency decay yourself. Then fill in the portrait template, compute my
> nearest archetype, and tell me which gap you'd close first and why.

Have it read your CV, your repositories, and your project history first if you
want the evidence probes to have teeth. An agent that has seen your commits is a
much harder grader than you are.

### Re-running it

- **Quarterly** for the whole wheel.
- **After each new agent harness generation** for AI Agents & Frameworks, and
  at minimum every six months — see the decay rule.
- **After any project that ended badly.** That is when the gaps are legible and
  the artifact rule is easy to apply.

The explorer still has no backend — attempts are saved to your browser's
`localStorage`, not a server — but it now does the recording and playback for
you. Click **Save current as attempt** each time you re-run the wheel; the
**Compare with** dropdown can then overlay any past attempt, not just an
archetype, and **Play growth** morphs your polygon across every saved attempt
in sequence. **Download animated SVG** exports that morph as a standalone,
shareable file once you have two or more attempts saved. Since it's
browser-local, use **Export history (.json)** before switching machines or
browsers, and **Import history (.json)** to bring it back — that's also how a
cohort could pool anonymized attempts, appropriately an exercise on the axis
this revision added.

---

## 7. Using it with a team

The same rubric works for a group, with two changes.

**Score individually, then plot the team as a max, not a mean.** A team's
capability on an axis is roughly its strongest member on that axis, not its
average — one person at 3 on Data Engineering unblocks everyone. Plot both: the
max is what you can do, the mean is your bus factor.

**Read the coverage gaps, not the individual ones.** An axis where nobody exceeds
1 is a hiring or training decision. An axis where exactly one person exceeds 1 is
a risk. An axis where everybody is at 3 is over-investment relative to a wheel
with a hole in it.

For hiring, the ladders make useful interview structure: ask the probe question,
then apply the artifact rule and the failure-mode rule out loud. The candidate
who can name what went wrong and how they caught it is a level above the one with
the longer tool list — which is the entire premise of the 2026 revision. And the
old advice against hiring the generalist has inverted: the constraint that made
that person a poor deal — one human, one task at a time — is the constraint that
has lifted.

---

## 8. Provenance

Grounded in the [taxonomy](skills-assessment.md) and the maturity model behind it
(in use since 2012, described in the [README](README.md)); the live
self-assessment walkthrough from the DSI master's bootcamp (August 2026); the
learning-science conventions of the Vanderbilt MSAI curriculum — behaviorally
anchored levels, mandatory self-assessment beside the external score, evidence
and process as required artifacts, and critical evaluation of AI output as a
first-class scored dimension; and current agentic practice as of mid-2026:
portable Agent Skill and plugin standards across vendors, MCP as the connective
layer, spec-driven development, subagent orchestration and asynchronous
delegation, and eval literacy as the differentiating skill.

**Status: a working rubric, not a settled standard.** The AI Agents & Frameworks
ladder will need revision soonest — by design. The verification cap on
Programming is a deliberate, arguable choice: it will need to be relaxed as the
teeter-totter tips, and the moment to relax it is when employers stop asking
people to write code by hand, not before.

Sources for the currency claims:
[Agent Skills ecosystem 2026](https://agentman.ai/blog/agent-skills-ecosystem-report-2026) ·
[Agent Plugins open standard](https://explainx.ai/blog/agent-plugins-openai-standard-aws-cursor-github-vscode-2026) ·
[Spec-driven development guide](https://www.thebcms.com/blog/spec-driven-development/) ·
[Agentic coding in 2026](https://sourcegraph.com/blog/agentic-coding) ·
[Evals as a data science problem](https://arize.com/blog/ai-evals-are-a-data-science-problem-what-most-teams-get-wrong/) ·
[Data scientist job market 2026](https://365datascience.com/career-advice/data-scientist-job-market/)
