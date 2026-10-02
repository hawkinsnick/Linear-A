#!/usr/bin/env python3
"""Check gap-register membership against the canonical Combined AI registry."""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EXCLUDED = {"Egyptian-Hieroglyphic-Corpus", "LightroomIsSlow"}
RULE = "Parity is rigor and traceability under surviving evidence, never equal row counts."


def validate(register, combined):
    errors = []
    required = {"repo", "evidence_depth", "coverage_state", "top_gap"}
    seen = set()
    for i, member in enumerate(register.get("members", [])):
        missing = {key for key in required if not member.get(key)}
        if missing:
            errors.append(f"member {i} missing {sorted(missing)}")
        name = member.get("repo")
        if name in seen:
            errors.append(f"duplicate repo {name}")
        seen.add(name)
    repositories = [m.get("repository", "") for m in combined.get("members", [])]
    if not repositories or any(not name.startswith("hawkinsnick/") for name in repositories):
        errors.append("invalid or empty Combined AI corpus membership")
    if len(repositories) != len(set(repositories)):
        errors.append("duplicate repository in Combined AI registry")
    expected = {name.split("/", 1)[-1] for name in repositories}
    if expected - seen:
        errors.append(f"missing fleet members: {sorted(expected - seen)}")
    if seen - expected:
        errors.append(f"unregistered fleet members: {sorted(seen - expected, key=str)}")
    if EXCLUDED & (seen | expected):
        errors.append(f"separate projects included in corpus fleet: {sorted(EXCLUDED & (seen | expected))}")
    exclusions = {m.get("repo") for m in register.get("excluded_projects", []) if m.get("reason")}
    if exclusions != EXCLUDED:
        errors.append("separate-project exclusions must name Egyptian and Lightroom with reasons")
    if register.get("rule") != RULE:
        errors.append("parity rule changed")
    return errors


def main():
    register = json.loads((ROOT / "corpus-factory/fleet-gap-register.json").read_text())
    combined = json.loads((ROOT / "combined-ai-skill/registry/corpus-projects.json").read_text())
    errors = validate(register, combined)
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(register['members'])} corpus projects; membership matches Combined AI; separate projects excluded")
    return 0


if __name__ == "__main__":
    sys.exit(main())
