#!/usr/bin/env python3
"""
Deterministic scorer for the Data Scientist Skills Inventory rubric
(skill-level-rubric.md, Vanderbilt DS Institute, 2026 revision).

Exists because ds-skills-explorer.html has no UI for the two rubric
adjustments in §4 (Programming verification cap, AI Agents currency decay),
so they get computed by hand today -- see issue #37. This script is the
part of the fix that should never be done by an LLM doing mental math:
it takes the raw interview answers and produces the exact §4-adjusted
scores, the nearest archetype, and the array the explorer's sliders expect.

Usage:
    python score.py input.json
    python score.py -   # read JSON from stdin

Input JSON shape -- see references/portrait-template.md for what each
field means and how to elicit it from the person being scored:

{
  "name": "Jane Data",
  "date": "2026-08-13",
  "context": "MSDS student, Stage 2 org, aiming at The Builder",
  "axes": {
    "stats": 2.5, "aifound": 2, "dataeng": 2,
    "viz": 2, "comm": 3, "story": 2, "domain": 2
  },
  "programming": {"dial_a": 3, "dial_b": 1.5},
  "agents": {
    "raw": 3,
    "months_since_active": 8,
    "peak_ever": 3
  }
}

`axes` excludes "agents" and "prog" -- those two are computed by this
script from `programming` and `agents` and merged in. `agents.peak_ever`
is optional; if omitted it defaults to `agents.raw` (i.e. "the raw score
IS the peak, nothing higher was ever demonstrated").
"""
import json
import math
import sys

AXIS_ORDER = ["stats", "aifound", "agents", "prog", "dataeng", "viz", "comm", "story", "domain"]

PRESETS = {
    "Balanced 2026 DS": [3, 3, 3, 2, 2, 3, 3, 3, 2],
    "The Guide":        [2, 2, 3, 1, 1, 4, 4, 4, 2],
    "The Builder":      [3, 2, 3, 3, 3, 2, 2, 3, 2],
    "The Architect":    [2, 3, 3, 4, 4, 2, 2, 2, 3],
    "The Visionary":    [3, 4, 4, 2, 2, 2, 3, 3, 4],
    "The Toolmaker":    [2, 4, 4, 3, 2, 2, 2, 1, 2],
}


def clamp(v, lo=0.0, hi=4.0):
    return max(lo, min(hi, v))


def snap_half(v):
    """
    Round to the nearest 0.5, ties rounding up.

    Python's built-in round() uses round-half-to-even ("banker's
    rounding"): round(2.5) == 2, not 3. That's the right default for
    statistics, but it's the wrong default here -- the rubric's scale is
    0-4 in half steps, and a caller has no reason to expect that a
    computed 1.25 (e.g. mean(0.5, 2.0) from the two Programming dials)
    snaps DOWN to 1.0 instead of UP to 1.5 depending on whether the
    doubled value happens to be even. That surprise is exactly the kind
    of silent arithmetic error this script exists to prevent -- it was
    caught by this project's own eval suite (see evals/evals.json,
    eval id 1) before it could reach a real score.
    """
    return math.floor(clamp(v) * 2 + 0.5) / 2


def score_programming(dial_a, dial_b):
    """axis = min(mean(A,B), B+1) -- the verification cap, rubric §4."""
    mean_ab = (dial_a + dial_b) / 2
    cap = dial_b + 1
    score = min(mean_ab, cap)
    return {
        "dial_a": dial_a,
        "dial_b": dial_b,
        "mean": round(mean_ab, 2),
        "cap": round(cap, 2),
        "score": snap_half(score),
        "cap_binding": mean_ab > cap,
    }


def score_agents(raw, months_since_active, peak_ever=None):
    """
    Currency decay, rubric §4: "Subtract 0.5 for every six months since your
    last sustained hands-on period with current tooling, floored at 1 if you
    were ever at 2 or above. No other axis decays this way."

    The rubric text only defines the floor for people who reached 2+ at some
    point. It leaves two things ambiguous, which issue #37 flags explicitly:
      1. What floors someone who peaked below 2 (0, or no floor at all)?
      2. Does "ever at 2+" mean the peak historically, or the score being
         decayed right now?
    This implementation takes the more defensible reading -- floor keys off
    the historical peak (`peak_ever`, defaulting to `raw` when the caller
    has no better number) -- and is explicit in its output about which case
    applied, rather than silently picking an answer. Surface `ambiguous`
    to the person being scored so they know this was a judgment call, not
    settled rubric text.
    """
    if peak_ever is None:
        peak_ever = raw
    periods = months_since_active // 6
    decay_amount = 0.5 * periods
    decayed_raw = raw - decay_amount
    floor_applies = peak_ever >= 2
    floor = 1.0 if floor_applies else 0.0
    decayed = max(decayed_raw, floor) if floor_applies else max(decayed_raw, 0.0)
    decayed = snap_half(decayed)
    return {
        "raw": raw,
        "peak_ever": peak_ever,
        "months_since_active": months_since_active,
        "decay_periods": periods,
        "decay_amount": decay_amount,
        "floor_applies": floor_applies,
        "floor": floor,
        "score": decayed,
        "ambiguous": not floor_applies,
        "ambiguity_note": (
            None if floor_applies else
            "peak_ever < 2, so the rubric's floor clause doesn't cover this case "
            "(see issue #37 on ds-skills-inventory) -- floored at 0 here rather than left undecayed."
        ),
    }


def nearest_archetype(vector):
    dists = {name: sum(abs(a - b) for a, b in zip(vector, preset)) / len(vector)
             for name, preset in PRESETS.items()}
    ranked = sorted(dists.items(), key=lambda kv: kv[1])
    nearest_name, nearest_dist = ranked[0]
    second_name, second_dist = ranked[1]
    between = (second_dist - nearest_dist) <= 0.2
    own_shape = nearest_dist > 1.0
    return {
        "all_distances": {k: round(v, 3) for k, v in dists.items()},
        "nearest": nearest_name,
        "distance": round(nearest_dist, 3),
        "between": [nearest_name, second_name] if between else None,
        "own_shape": own_shape,
    }


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    raw_in = sys.stdin.read() if sys.argv[1] == "-" else open(sys.argv[1], encoding="utf-8").read()
    data = json.loads(raw_in)

    axes = dict(data["axes"])
    prog = score_programming(**data["programming"])
    agents = score_agents(**data["agents"])
    axes["prog"] = prog["score"]
    axes["agents"] = agents["score"]

    missing = [a for a in AXIS_ORDER if a not in axes]
    if missing:
        raise SystemExit(f"missing axis scores: {missing}")

    vector = [axes[a] for a in AXIS_ORDER]
    archetype = nearest_archetype(vector)

    out = {
        "scores": axes,
        "programming_detail": prog,
        "agents_detail": agents,
        "nearest_archetype": archetype,
        "explorer_array": vector,
        "explorer_array_order": AXIS_ORDER,
        "copy_values_format": "\n".join(f"{a}: {axes[a]}" for a in AXIS_ORDER),
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
