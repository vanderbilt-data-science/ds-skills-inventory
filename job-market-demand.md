# Cross-Referencing the Skills Inventory with US Job Market Demand

Companion to the [skills inventory](skills-assessment.md) and the
[interactive explorer](ds-skills-explorer.html). Answers a question the
inventory alone can't: *of these nine axes, which does the 2026 US job market
actually reward, and does that differ by role?*

The explorer's **"Compare with"** dropdown includes four **Job Market**
presets — Data Scientist, ML Engineer, Data Analyst, and AI Engineer
(GenAI/Agents) — scored 0–4 on the same axes and scale as your own profile,
so you can overlay your skills directly against role demand.

## Method

Each role's score per axis is a qualitative synthesis of public 2026 US
labor-market reporting: employer job-posting analyses, the BLS Occupational
Outlook Handbook, and industry skills-demand reports (LinkedIn, 365 Data
Science, Axial Search). This is directional signal, not a precision
measurement — job-posting keyword frequency is a proxy for demand, not a
census of it, and reports disagree at the margins. Treat the presets the same
way you'd treat the archetype presets (Guide/Builder/Architect/Visionary/
Toolmaker): a reasoned sketch to calibrate against, not ground truth. Rescore
them yourself if you have better data for your target role or region.

**0** = rarely appears as a requirement · **2** = commonly expected baseline ·
**4** = the role's defining, differentiating skill.

## Findings by axis

- **Statistics & Modeling** — Still a broad baseline (~60% of data scientist
  postings cite statistics), but no longer the differentiator it once was.
  Highest for Data Scientist and Data Analyst roles; lower priority for
  engineering-heavy roles (ML Engineer, AI Engineer) where the model is
  often consumed rather than designed from first principles.
- **AI Foundations** — Machine learning appears in ~69% of data scientist
  postings and deep-learning mentions have roughly doubled year over year.
  Highest for ML Engineer (the model *is* the product) and AI Engineer
  (adapting foundation models); still solidly demanded for Data Scientist.
- **AI Agents & Frameworks** — The fastest-growing category in the market:
  LinkedIn ranked AI Engineer the #1 fastest-growing US job for 2026 (postings
  up ~143% YoY), driven by LangChain, RAG, and agent-workflow skills.
  Highest for AI Engineer by a wide margin; a real but smaller expectation for
  ML Engineer and Data Scientist; least central for Data Analyst (though
  analysts increasingly use GenAI as a co-pilot).
- **Programming** — Production software engineering is central for ML
  Engineer and AI Engineer (shipping and operating systems, MLOps
  pipelines), a working-fluency expectation for Data Scientist, and the
  lightest touch for Data Analyst (mostly SQL/scripting, largely
  AI-assisted).
- **Data Engineering** — SQL is the single most commonly requested skill on
  data science postings (~55%), and cloud/warehouse skills are rising.
  Highest for ML Engineer (pipelines, infra, MLOps) and AI Engineer
  (retrieval/vector infrastructure); a solid floor for Data Scientist and
  Data Analyst.
- **Visualization** — A core, everyday tool for Data Analyst (dashboards,
  Tableau ~42% of postings) and a supporting skill for Data Scientist;
  peripheral for the two engineering-first roles.
- **Communication** — Valued everywhere data meets a decision-maker, but most
  load-bearing for Data Analyst, whose entire output is a business-facing
  answer.
- **Storytelling** — Follows Communication: central for Data Analyst,
  present but secondary for Data Scientist, least central where the output is
  a system rather than a narrative (ML Engineer, AI Engineer).
- **Domain Knowledge** — Matters most where the work is embedded directly in
  a business question (Data Analyst, and to a lesser extent Data Scientist);
  lighter for roles centered on general-purpose infrastructure or models
  (ML Engineer, AI Engineer), though it still shapes what gets built.

## The four role presets

| Axis | Data Scientist | ML Engineer | Data Analyst | AI Engineer (GenAI) |
|---|---|---|---|---|
| Statistics & Modeling | 3 | 2 | 3 | 1 |
| AI Foundations | 3 | 4 | 2 | 3 |
| AI Agents & Frameworks | 2 | 3 | 2 | 4 |
| Programming | 2 | 4 | 1 | 4 |
| Data Engineering | 3 | 4 | 2 | 3 |
| Visualization | 2 | 1 | 4 | 1 |
| Communication | 3 | 2 | 4 | 2 |
| Storytelling | 2 | 1 | 3 | 1 |
| Domain Knowledge | 2 | 2 | 3 | 2 |

## Sources

- [BLS Occupational Outlook Handbook — Data Scientists](https://www.bls.gov/ooh/math/data-scientists.htm)
- [365 Data Science — Data Scientist Job Outlook 2026](https://365datascience.com/career-advice/career-guides/data-scientist-job-outlook-2025/)
- [365 Data Science — Machine Learning Engineer Job Outlook 2026](https://365datascience.com/career-advice/career-guides/machine-learning-engineer-job-outlook-2025/)
- [365 Data Science — AI Engineer Job Outlook 2026](https://365datascience.com/career-advice/career-guides/ai-engineer-job-outlook-2025/)
- [Medium — Analysis of 500 Data Science Job Posts in 2026](https://medium.com/ai-analytics-diaries/i-analyzed-500-data-science-job-posts-in-2026-heres-exactly-what-they-want-eaac5980590b)
- [Axial Search — AI/ML Engineering Jobs in 2026: Analyzing 10,000+ Posts](https://axialsearch.com/insights/ai-ml-engineering-jobs/)
- [Interview Query — LinkedIn: AI Engineering, Prompting & Model Tuning Are the Fastest-Growing Skills in 2026](https://www.interviewquery.com/p/linkedin-ai-engineering-fastest-growing-skills-2026)

## Updating this over time

Labor-market demand moves faster than a maturity-model taxonomy should.
Revisit these four presets roughly annually (or when a source above
publishes a new edition) and update the table, the `PRESETS` entries in
[`ds-skills-explorer.html`](ds-skills-explorer.html), and this document's
sources together so they stay in sync.
