#!/usr/bin/env python3
"""Structurally validate a text-to-skill-interpreter observation log.

Standard library only, matching the rest of this repo's tooling. Not a
general JSON Schema engine -- it checks exactly the shape defined in
schema/observation-log.schema.json, so the two files must be kept in sync
by hand if the schema changes.

Usage: python3 validate_log.py <path-to-log.json>
"""
import json
import sys

AXES = {"stats", "aifound", "agents", "prog", "dataeng", "viz", "comm", "story", "domain"}
CONFIDENCES = {"low", "medium", "high"}
SOURCE_TYPES = {"interview_transcript", "written_reflection", "mock_interview_qa"}
RULES = {
    "artifact_rule",
    "failure_mode_rule",
    "outsider_rule",
    "half_step",
    "verification_cap",
    "currency_decay",
}


def fail(errors, path, message):
    errors.append(f"{path}: {message}")


def is_level(x):
    return isinstance(x, (int, float)) and 0 <= x <= 4 and (x * 2) == int(x * 2)


def validate(doc):
    errors = []

    session = doc.get("session")
    if not isinstance(session, dict):
        fail(errors, "session", "missing or not an object")
        session = {}
    for field in ("date", "subject_id", "source_type"):
        if field not in session:
            fail(errors, "session", f"missing required field '{field}'")
    if "source_type" in session and session["source_type"] not in SOURCE_TYPES:
        fail(errors, "session.source_type", f"must be one of {sorted(SOURCE_TYPES)}")

    observations = doc.get("observations")
    if not isinstance(observations, list):
        fail(errors, "observations", "missing or not an array")
        observations = []
    for i, obs in enumerate(observations):
        p = f"observations[{i}]"
        if not isinstance(obs, dict):
            fail(errors, p, "not an object")
            continue
        for field in ("axis", "observed_level", "confidence", "evidence_snippet", "rules_applied"):
            if field not in obs:
                fail(errors, p, f"missing required field '{field}'")
        if obs.get("axis") not in AXES:
            fail(errors, f"{p}.axis", f"must be one of {sorted(AXES)}")
        if "observed_level" in obs and not is_level(obs["observed_level"]):
            fail(errors, f"{p}.observed_level", "must be 0-4 in half steps")
        if obs.get("confidence") not in CONFIDENCES:
            fail(errors, f"{p}.confidence", f"must be one of {sorted(CONFIDENCES)}")
        if not obs.get("evidence_snippet"):
            fail(errors, f"{p}.evidence_snippet", "must be a non-empty string")
        rules = obs.get("rules_applied")
        if not isinstance(rules, list) or not rules:
            fail(errors, f"{p}.rules_applied", "must be a non-empty array")
        else:
            bad = [r for r in rules if r not in RULES]
            if bad:
                fail(errors, f"{p}.rules_applied", f"unknown rule(s) {bad}, must be subset of {sorted(RULES)}")

    adjustments = doc.get("adjustments", [])
    if not isinstance(adjustments, list):
        fail(errors, "adjustments", "must be an array if present")
        adjustments = []
    for i, adj in enumerate(adjustments):
        p = f"adjustments[{i}]"
        if not isinstance(adj, dict):
            fail(errors, p, "not an object")
            continue
        for field in ("axis", "baseline_score", "proposed_score", "delta"):
            if field not in adj:
                fail(errors, p, f"missing required field '{field}'")
        if adj.get("axis") not in AXES:
            fail(errors, f"{p}.axis", f"must be one of {sorted(AXES)}")
        if "proposed_score" in adj and not is_level(adj["proposed_score"]):
            fail(errors, f"{p}.proposed_score", "must be 0-4 in half steps")
        baseline = adj.get("baseline_score")
        if baseline is not None and not (isinstance(baseline, (int, float)) and 0 <= baseline <= 4):
            fail(errors, f"{p}.baseline_score", "must be null or a number 0-4")
        if (
            baseline is not None
            and "proposed_score" in adj
            and "delta" in adj
            and abs((adj["proposed_score"] - baseline) - adj["delta"]) > 1e-9
        ):
            fail(errors, f"{p}.delta", "must equal proposed_score - baseline_score")

    insufficient = doc.get("insufficient_evidence", [])
    if not isinstance(insufficient, list):
        fail(errors, "insufficient_evidence", "must be an array if present")
    else:
        bad = [a for a in insufficient if a not in AXES]
        if bad:
            fail(errors, "insufficient_evidence", f"unknown axis/axes {bad}")

    return errors


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    with open(sys.argv[1]) as f:
        doc = json.load(f)
    errors = validate(doc)
    if errors:
        print(f"INVALID -- {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
    print(f"OK -- {len(doc.get('observations', []))} observation(s) validated")


if __name__ == "__main__":
    main()
