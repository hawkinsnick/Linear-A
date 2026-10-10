# P0 reconciliation — 2026-10-10

This is an evidence-based checkpoint, **not** a claim of completed validation.

## Verified GitHub operations

- Master registry corrected from the non-existent `hawkinsnick/Cretan-hieroglpyhs` spelling to `hawkinsnick/Cretan-hieroglyphs`.
- Registered Lydian, Pisidian, and Sidetic using their available 0.3.1 individual skills, manifests, generated indexes, and bundle validators.
- Phaistos-Disc, Eteocretan, and Eteocypriot have source-state and generated bundle-index files agreeing on the same source commit at inspection time. Agreement alone is not cryptographic validation of every indexed artifact.

## Pending contract migrations — do not silently admit

- `Milyan-Lycian-B`: individual skill, bundle index, authority profile, and validator exist; standard `ai-skill/manifest.json` and `ai-skill/generated/source-state.json` are missing. Its bundle index uses a distinct initial-inventory schema.
- `Archanes-Script`, `Anatolian-Hieroglyphic`, and `Aegean-anomalous`: individual skill, generated index and authority profile exist; standard manifest, source-state and bundle validator are missing. Their current skill formats differ from the 0.3.1 contract.

Do not infer that a generated index implies full source coverage, scholarly acceptance, or compatibility with the master validator. Adapt these projects with source-specific migration and tests rather than overwriting their native schemas.

## Unverified P0 gates

1. Execute repository-native tests and AI bundle validators in a real checkout and capture exit codes and logs.
2. Validate artifact hashes and source-state against Git commit history, including commits made after the referenced source commit.
3. Run combined master validation for the entire registered fleet; no success result has been obtained in this checkpoint.
4. Compare offline worktree commits, untracked files, and outstanding PRs against remote heads. GitHub-only access cannot prove the state of an unavailable offline worktree.

GitHub commit-status results and PR-triggered workflow-run queries for the three priority heads returned empty lists; this is **not** evidence of successful CI.
