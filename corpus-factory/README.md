# Corpus Factory v1

The factory standardizes research governance without standardizing away corpus-specific semantics.

The fleet contains the 14 language corpus projects registered in
`combined-ai-skill/registry/corpus-projects.json`. Egyptian Hieroglyphs and
LightroomIsSlow are separate projects and are explicitly excluded.

Run `python corpus-factory/validate_fleet.py` from the repository root to check
that the gap register and Combined AI membership agree. This checks governance
metadata, not the truth or completeness of another project's evidence.

A member passes the benchmark interface when it exposes machine-readable coverage, source lineage, rights, evidence layers, admission/blocking gates, independence state, reproducible validation, and an AI authority profile.

## Admission lifecycle

discover -> identify -> rights-check -> capture/hash or stable locator -> parse -> reconcile identity -> source-check -> independent review where available -> admit -> validate -> bundle

Every transition is explicit. Missing evidence may remain discovered, excluded, disputed, inaccessible, rights-blocked, or unreviewed. Those states are useful data and must not be collapsed into admission.

## Cross-corpus rule

The factory provides compatible infrastructure, not common sign values, languages, chronologies, or decipherments. Native project semantics remain authoritative.
