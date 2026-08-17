# Portrait template and archetype matching (from skill-level-rubric.md §6)

## Axis order

Everywhere a 9-vector appears (archetype presets, `explorer_array`, the
sliders in `ds-skills-explorer.html`), the order is fixed:

```
[stats, aifound, agents, prog, dataeng, viz, comm, story, domain]
```

## Archetype preset vectors (§6 Step 3)

| Preset | Vector |
|---|---|
| Balanced 2026 DS | `3, 3, 3, 2, 2, 3, 3, 3, 2` |
| The Guide | `2, 2, 3, 1, 1, 4, 4, 4, 2` |
| The Builder | `3, 2, 3, 3, 3, 2, 2, 3, 2` |
| The Architect | `2, 3, 3, 4, 4, 2, 2, 2, 3` |
| The Visionary | `3, 4, 4, 2, 2, 2, 3, 3, 4` |
| The Toolmaker | `2, 4, 4, 3, 2, 2, 2, 1, 2` |

Nearest archetype = smallest mean absolute difference across the 9 axes.
If two are within 0.2 of each other, the person sits between them — common
and fine. A mean difference above 1.0 from every preset means they're their
own shape — also fine, worth writing down as such. `scripts/score.py`
computes this exactly; don't eyeball it.

## Gap-timing table (§6 Step 5) — read gaps against this grain

| Gap on | Moves | What moves it |
|---|---|---|
| Programming, Data Engineering, AI Agents | **Weeks**, visibly, once working with agents seriously | Deliberate delegation on real projects; building and reusing Skills; verifying everything |
| AI Foundations | **Months** | A real course, consolidated by use |
| Statistics & Modeling, Visualization, Communication, Storytelling, Domain | **A year or more** — the last mile | Study plus real projects with real audiences; nothing accelerates these |

The instinct is to attack the biggest gap. The better move is usually:
start the slow axes now (they take a year regardless), and let the fast
axes rise through work already planned.

## Portrait YAML template

Fill this in at the end of the interview and hand it to the person to keep
alongside their exported radar SVG.

```yaml
portrait:
  name:
  date:
  context:            # role, organization maturity stage (1-5), what they're aiming at
  scores:             # 0-4, half steps, POST-adjustment (cap + decay already applied)
    stats:
    aifound:
    agents:
    prog:
    dataeng:
    viz:
    comm:
    story:
    domain:
  programming_dials:  # BEFORE the verification cap
    agentic:
    unaided:
  agents_decay:        # the currency-decay inputs and result, so the number is reproducible later
    raw:
    months_since_active:
    peak_ever:
    decayed:
  evidence:           # one named artifact per axis - the artifact rule, written down
  confidence:         # per axis: evidenced | estimated
  domains:            # scored domain, plus the others at their real levels
  nearest_archetype:  # + mean difference
  target:             # archetype or stage they're aiming at, as a vector
  fast_gaps:          # closable in weeks - prog, dataeng, agents
  slow_gaps:          # the last mile - start now, measure in years
  preference:         # what they actually enjoy; where they'd stop before perfect
  next_three_moves:
```

## Re-running it

Quarterly for the whole wheel; after each new agent-harness generation (at
minimum every six months) for AI Agents specifically, per the decay rule;
and after any project that ended badly, when the gaps are legible and the
artifact rule is easy to apply.
