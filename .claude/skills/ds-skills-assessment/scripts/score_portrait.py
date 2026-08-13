#!/usr/bin/env python3
"""
Scoring helper for the ds-skills-assessment skill.

Applies the Programming verification cap and the AI Agents currency-decay
rule from skill-level-rubric.md section 4, and reports nearest-archetype
distances from section 6 step 3. Standard library only.

The archetype vectors below are transcribed from skill-level-rubric.md
section 6 (which itself mirrors ds-skills-explorer.html's PRESETS). If the
rubric's archetype table changes, update ARCHETYPES here to match.
"""
import argparse

AXES = ["stats", "aifound", "agents", "prog", "dataeng", "viz", "comm", "story", "domain"]

ARCHETYPES = {
    "Balanced 2026 DS": [3, 3, 3, 2, 2, 3, 3, 3, 2],
    "The Guide":        [2, 2, 3, 1, 1, 4, 4, 4, 2],
    "The Builder":      [3, 2, 3, 3, 3, 2, 2, 3, 2],
    "The Architect":    [2, 3, 3, 4, 4, 2, 2, 2, 3],
    "The Visionary":    [3, 4, 4, 2, 2, 2, 3, 3, 4],
    "The Toolmaker":    [2, 4, 4, 3, 2, 2, 2, 1, 2],
}


def verification_cap(a, b):
    """axis = min(mean(A,B), B+1) -- rubric section 4."""
    mean_ab = (a + b) / 2
    capped = min(mean_ab, b + 1)
    return capped, mean_ab


def currency_decay(raw, months_stale):
    """Subtract 0.5 per 6 months since last sustained hands-on period,
    floored at 1 if raw was ever >= 2. -- rubric section 4."""
    steps = months_stale // 6
    decayed = raw - 0.5 * steps
    if raw >= 2:
        decayed = max(decayed, 1)
    decayed = max(decayed, 0)
    return decayed


def nearest_archetypes(vector):
    diffs = []
    for name, preset in ARCHETYPES.items():
        mad = sum(abs(a - b) for a, b in zip(vector, preset)) / len(vector)
        diffs.append((mad, name))
    diffs.sort()
    return diffs


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for axis in AXES:
        p.add_argument(f"--{axis}", type=float, default=None,
                        help=f"final adjusted score for {axis} (0-4)")
    p.add_argument("--prog-a", type=float, default=None, help="Programming Dial A (agentic delivery)")
    p.add_argument("--prog-b", type=float, default=None, help="Programming Dial B (unaided fluency)")
    p.add_argument("--agents-raw", type=float, default=None, help="AI Agents raw level before decay")
    p.add_argument("--agents-months-stale", type=float, default=None,
                   help="months since last sustained hands-on period")
    args = p.parse_args()

    prog = args.prog
    if args.prog_a is not None and args.prog_b is not None:
        capped, mean_ab = verification_cap(args.prog_a, args.prog_b)
        print(f"Programming: mean(A={args.prog_a}, B={args.prog_b}) = {mean_ab:.2f}; "
              f"B+1 = {args.prog_b + 1:.2f}; verification-capped score = {capped:.2f}")
        prog = capped

    agents = args.agents
    if args.agents_raw is not None and args.agents_months_stale is not None:
        decayed = currency_decay(args.agents_raw, args.agents_months_stale)
        floor_note = " (floor applied: raw was >= 2)" if args.agents_raw >= 2 and decayed == 1 else ""
        print(f"AI Agents: raw={args.agents_raw}, {args.agents_months_stale:.0f} months stale "
              f"-> decayed score = {decayed:.2f}{floor_note}")
        agents = decayed

    values = {
        "stats": args.stats, "aifound": args.aifound, "agents": agents, "prog": prog,
        "dataeng": args.dataeng, "viz": args.viz, "comm": args.comm, "story": args.story,
        "domain": args.domain,
    }
    missing = [k for k in AXES if values[k] is None]
    if missing:
        print(f"\n(skipping archetype match -- missing: {', '.join(missing)})")
        return

    vector = [values[a] for a in AXES]
    print("\nFinal vector [" + ", ".join(AXES) + "]:")
    print("  " + ", ".join(f"{v:g}" for v in vector))

    print("\nNearest archetypes (mean absolute difference, ascending):")
    ranked = nearest_archetypes(vector)
    for mad, name in ranked:
        print(f"  {mad:.2f}  {name}  {ARCHETYPES[name]}")
    if len(ranked) >= 2 and (ranked[1][0] - ranked[0][0]) <= 0.2:
        print(f"\n  Note: {ranked[0][1]} and {ranked[1][1]} are within 0.2 of each other -- "
              f"the person sits between them (rubric section 6: common and fine).")
    if ranked[0][0] > 1.0:
        print("\n  Note: nearest archetype is still > 1.0 away -- this is its own shape, "
              "worth writing down as such rather than forcing a match.")


if __name__ == "__main__":
    main()
