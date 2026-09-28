# Linear A Open Corpus — 0.4.0-rc10-local

RC10 is an **f3 boundary-forensics release**, not a claimed final decoding of
SigLA's boundary representation.

## What we established

The reference extractor identifies attestation field `f3` as word-boundary
state and cites `Bound.t = Here | Unsure | Not_here`. Raw inspection shows two
serialized shapes:

- wrapped pair: 3,448 attestations
- direct pair: 1,696 attestations

The normalized integer pair cannot itself be the three-state enum.

### KN Zc 6 case study

KN Zc 6 is exceptionally clear. Its pairs form four runs:

- group-like index 0: positions 0–2
- index 1: positions 0–6
- index 2: positions 0–2
- index 3: positions 0–9

This is consistent with the independently published description of multiple
sign-groups and punctuation around the second group. It is strong **local**
evidence for a position/group-like coordinate interpretation.

## Why the model is not promoted corpus-wide

Across all attestations there are 1708
candidate second-coordinate groups. Only
1359
are zero-based contiguous under the simple model, and duplicate/non-contiguous
coordinates occur.

Those anomalies may have legitimate epigraphic or data-model explanations
(composites, damage, uncertainty, or something else), but RC10 does not guess.

Therefore the global model remains:

**candidate: `(position-like index, group-like index)`**

—not authoritative `(position_within_word, word_index)`.

## Exploratory consequence

Using the candidate second-coordinate grouping produces 144 strong variable-slot
families; 39 survive the confident-only version. These numbers are retained as
an exploratory sensitivity result only and are **not** promoted as source-word
or morphological evidence.

## What RC11 needs

Recover the upstream f3 type/constructor implementation, explain wrapped versus
direct forms, and account for duplicate/non-contiguous pairs. Until then,
document-stream and candidate-group analyses remain separate sensitivity layers.

Nothing has been published to GitHub. Raw SigLA data and the full 5,144-row
derived table are not bundled.
