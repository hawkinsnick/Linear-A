# Linear A Open Corpus — 0.4.0-rc8-local

RC8 subjects RC7's variable-slot families to context controls rather than
treating the corpus as homogeneous.

## Controls actually executed
- confident-only recomputation
- conservative source-boundary-state segmentation
- leave-one-site-out recomputation
- independent within-site recurrence

Baseline strong families: 225
Surviving confident-only recomputation: 218
Surviving strict zero-boundary runs: 2
Stable core (certainty + boundary + all-but-at-most-one site leave-out): 1

## Important limitation
Document-type/register control is **not** fabricated. The safe 5,144-row
fingerprint table does not carry a validated document-type field. RC8 therefore
writes an explicit metadata-join requirement instead of guessing types from
document names.

## Interpretation
A family that survives these controls is a more robust distributional pattern,
not automatically morphology, syntax, vocabulary, or a decipherment.

Nothing has been published to GitHub.
