# Linear A Open Corpus — 0.5.0-local

0.5.0 establishes the context-aware corpus architecture.

Current SigLA documentation explicitly models document type and metadata and
provides a source-defined Word View in which syllabograms belonging to the same
word are highlighted together. This lets the corpus distinguish a genuine
`source_word` concept from the unresolved `f3` field.

This release includes a small set of current-page context exemplars to validate
the schema. They are **not** an exhaustive or representative metadata import.
Bulk document metadata and source-word rows remain blocked until a reproducible
extractor is validated against the same 802-document snapshot.

The critical invariant is now machine-readable:
`candidate_f3_group != source_word`.

Nothing has been published to GitHub.
