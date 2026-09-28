# 2.3 — Frozen known-answer Linear B calibration

## Purpose

Test whether the structural machinery developed on Linear A can recover observable
linguistic structure in deciphered Linear B without tuning to the answers.

## Frozen input

`damos-corpus-v2/damos-corpus.json`

Expected SHA-256:

`eab9ccdfc4324b62f015bccd5e3f917f256cab8c058840842127eadecfbca2d2`

The derivative contains transliterations and core document metadata. It is not treated
as the gold morphology source.

## Stage A — blind structural run

1. Verify the exact SHA-256. Wrong bytes abort the run.
2. Extract detector-facing word forms from `content`.
3. Run positional and edge-form screens without morphology, lemma, translation, or
   grammatical labels.
4. Freeze `FROZEN_PREDICTIONS.csv` and `BLIND_RUN.json`.
5. No tuning is permitted after the reveal without declaring a new experiment.

## Stage B — gold reveal

Acquire and version a DĀMOS linguistic-annotation export independently. Record its
snapshot/provenance. Map only script-visible morphology to frozen predictions.
Ambiguous/multiple analyses remain ambiguous.

Score at minimum:
- true structural detections with script-visible morphological support;
- structural detections lacking gold support;
- gold morphology visible in spelling but missed;
- gold morphology not observably distinguished by Linear B spelling.

The fourth class is not detector failure.

## Current status

`READY_FOR_PINNED_INPUT_BYTES`

The GitHub release identity and digest are independently verified, but the signed
release asset could not be transferred into this execution sandbox. No calibration
performance result is claimed.
