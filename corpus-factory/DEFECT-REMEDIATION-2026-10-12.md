# Defect remediation checkpoint — 2026-10-12

Scope: all 18 registered language repositories; Egyptian Hieroglyphic Corpus and LightroomIsSlow remain excluded. This checkpoint repairs software defects and records evidence dependencies separately. It does not grant scientific acceptance or claim global exhaustion of accessible sources.

## Confirmed defects repaired

- Linear A still used an obsolete post-validation rebase publisher. Its native bundle now uses the tested exact source-parent publisher, with hostile fixtures for source advancement, a concurrent push, unrelated changes, a mismatched source and validation failure.
- The master starter workflow also rebased generated downloads after validation. A separate deterministic publisher now replays expected bytes, allows only builder-declared outputs, checks the remote source parent and relies on atomic fast-forward rejection of a concurrent writer. Immutable release archives remain tied to their original validated source snapshot.
- Lydian, Sidetic and Pisidian had both a guarded sync workflow and a legacy unguarded publisher in native integrity CI. Removed the duplicate publishers and retained method-parity validation in the integrity job. Added workflow regression checks.
- The master dependency registry referred to by all 17 published native skills was missing from Linear A. Restored 15 identical source-supported groups from revision-pinned member projections; replayed every original file hash and JSON pointer. Added master screening and rejection tests, mandatory native/master validation and starter inclusion. Missing links do not establish uniqueness, independence or shared sign values.

## Existing repairs verified

CH/CM qualified assertion-view and reconciliation tests retain primary comparison, missing marks, damage, alternatives and disputed identities. Their original readings are not expanded by this repair. Native source strings, catalogue populations and rights boundaries remain unchanged.

## Remaining evidence dependencies

The two CH material conflicts, three CM sign-position disagreements and unresolved object joins remain explicit scholarly questions. Primary-edition access/permission limitations, unacquired source material and Linear B linguistic/graphical calibration prerequisites remain acquisition dependencies. Phaistos Disc issue #4 requires independent human evidence and remains open. A missing source or permission is not labelled expert-review completion.

## Replay

Run native AI validators, native test suites and the source-parent publisher tests. In Linear A run the master validator and starter tests; `python corpus-factory/check_cross_corpus_dependencies.py --checkouts /path/to/checkouts` replays published member receipts without executing member code. Local verification results and exact source revisions are recorded separately; no test proves independent epigraphic acceptance.

Local verification recorded 181 successful scoped command results across all 18 members, including 24 actual pinned upstream EpiDoc adversarial/integration tests. See `defect-validation-2026-10-12.json` for exact commands, base revisions and native authority fingerprints at validation. Subsequent GitHub CI validates the final published source trees. A local browser run could not start because Chrome is absent and the browser download was unavailable; the required existing GitHub browser job remains active.
