# Linear A Open Corpus — 0.6.0-local

0.6.0 is the first source-word-aware release.

It decodes SigLA's explicit serialized Word objects independently of the
unresolved `f3` field and populates current document type, find-place, and
optional period metadata for all 802 decoded documents.

Snapshot results:
- 802 documents
- 5,144 attestations
- 1,401 serialized Word objects
- 1,283 nonempty source words used in sequence analyses
- 118 empty Word objects retained but excluded from sequence statistics
- 6/6 independent current-page word-count checks agree
- 121 recurring within-word directed pairs tested
- 54 positive pairs survive BH q <= 0.05 under 500 within-word permutations
- zero unmapped current find-place labels in the explicit site mapping audit

These are structural results over SigLA-defined words, not claims of
decipherment, morphology, syntax, phonotactics, or semantic interpretation.

`f3` remains unresolved/evidence-tiered and analytically separate.

Nothing has been published to GitHub.
