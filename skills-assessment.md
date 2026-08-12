# Data Scientist Skills Inventory — 2026 Revision

Assessment and final taxonomy for updating the skills inventory from the
*Data Science in Practice* framework (Guide / Builder / Architect / Visionary),
reflecting the shift brought by generative AI and AI agents.

## 1. What changed and why

**The old "Machine Learning/Deep Learning" axis becomes AI Foundations.**
The old axis ran from *experience with non-class projects* up to *expertise
creating novel deep learning solutions*. Building networks from scratch is no
longer the center of gravity: most applied value now comes from adapting
foundation models (prompting, retrieval, fine-tuning, distillation) and from
knowing when a foundation model, a classical model, or a statistical model is
the right instrument. CNN/RNN theory has moved from "core rung" to
"specialist rung." Classical ML remains a workhorse — one tool among several.

**One genuinely new axis: AI Agents & Frameworks.** The defining new skill of
this era is working *through* AI, not merely *on* it: decomposing problems for
delegation, writing effective specifications, orchestrating agentic workflows
with current frameworks (agent SDKs, MCP, RAG pipelines), and supervising the
result. The original deck's repeated "Practice with AI!" annotations were
pointing here. It is the biggest multiplier skill on the wheel — it raises
effective capacity on every other axis.

**Evaluation is core training, not a separate axis.** When AI produces the
code, the analysis, and the prose, the human's core technical act becomes
verification — designing evals, error analysis, detecting hallucination and
silent failure. Rather than a tenth spoke, this is baked into the rungs of
both AI axes (see the ladders below). Ethics/governance is treated the same
way: it appears in the upper rungs of AI Foundations, and in regulated
domains it surfaces through Domain Knowledge.

**SQL & data access folds into Data Engineering.** SQL stood alone when it
was a universal consumption skill with a low bar. With AI writing most
first-draft queries, standalone SQL fluency no longer justifies its own
spoke; the 0–4 ladder of a single Data Engineering axis covers the spread
from "can get the data they need" to "designs pipelines and platforms."

**De-emphasized, not deleted: Programming.** The scarce skill is now
*reading, reviewing, and verifying* code (much of it AI-generated) plus
architecture judgment — not syntax fluency or boilerplate speed.

## 2. The 9-axis inventory

| Cluster | Axes |
|---|---|
| Analytical core | Statistics & Modeling |
| AI | AI Foundations *(absorbs ML/DL)* · AI Agents & Frameworks *(new)* |
| Engineering | Programming · Data Engineering *(absorbs SQL & data access)* |
| Human interface | Visualization · Communication · Storytelling · Domain Knowledge |

Human interface intentionally carries the most axes: it is where data
scientists differentiate as AI compresses the technical floor.

## 3. Rung ladders for the changed axes (0–4)

These four are the summary ladders — the axes whose *definitions* changed.
Behaviorally anchored ladders for **all nine** axes, with evidence anchors,
calibration rules, and the self-assessment procedure, are in
[`skill-level-rubric.md`](skill-level-rubric.md).

### AI Foundations
| Level | Description |
|---|---|
| 0 | Coursework only |
| 1 | Has applied classical ML and off-the-shelf foundation models to real (non-class) problems |
| 2 | Solid across major methods; runs error analysis and basic evals; sound model-selection judgment |
| 3 | Deep grasp of model behavior and limits; designs eval suites; fine-tuning/adaptation; responsible-AI judgment (bias, privacy, model risk) |
| 4 | Advances the frontier — novel methods, research-grade work |

### AI Agents & Frameworks
| Level | Description |
|---|---|
| 0 | Chat-style use only |
| 1 | Productive daily delegation — effective prompts and specifications, knows what to hand off vs. do by hand |
| 2 | Builds retrieval and tool-use workflows with current frameworks (agent SDKs, MCP, RAG) |
| 3 | Designs multi-step/multi-agent systems with built-in evals, guardrails, and monitoring; supervises parallel agents |
| 4 | Creates novel agent architectures or frameworks |

### Data Engineering (incl. SQL & data access)
| Level | Description |
|---|---|
| 0 | No hands-on data access experience |
| 1 | Can get the data they need — SQL basics (AI-assisted), APIs, warehouse queries |
| 2 | Working knowledge of warehouses/lakes; sound joins; data-quality checks |
| 3 | Builds pipelines and orchestration; ensures quality at scale |
| 4 | Designs data platforms — streaming, very large scale, specialized infrastructure |

### Programming (revised emphasis)
| Level | Description |
|---|---|
| 0 | None |
| 1 | Can produce working analysis code with AI assistance and understand what it does |
| 2 | Reads and reviews code reliably; catches errors in AI-generated code; automates workflows |
| 3 | Sound software architecture; stands up production solutions; feature engineering at scale |
| 4 | Expert systems builder — the separate-engineering-team tier |

## 4. Implications for the archetypes

The **Guide** (Stage 1) now needs AI Agents & Frameworks nearly as much as
Storytelling — Stage 1 organizations start with AI-assisted analysis on day
one. The **Builder** (Stage 2–3) leans on Data Engineering and the
verification rungs of AI Foundations. The **Architect** (Stage 3–4) carries
the engineering axes plus the governance rungs as adoption scales. The
**Visionary** (Stage 4–5) lives at the top of both AI axes. The **Toolmaker**
(from Deep Solutions) is an AI-axes specialist who equips 10x analysts.

## 5. Considered and set aside

- **Product & decision framing** — covered by Domain Knowledge + Storytelling.
- **MLOps/LLMOps** — folded into Data Engineering and the AI axes' upper rungs.
- **Causal inference** — lives inside Statistics & Modeling.
- **Standalone AI Evaluation / Ethics axes** — folded into rungs (see §1);
  revisit if either becomes a hiring differentiator worth plotting on its own.
