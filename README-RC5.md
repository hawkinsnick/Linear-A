# Linear A Open Corpus — 0.4.0-rc5-local

RC5 adds statistically controlled structural discovery to the validated corpus.

## Adjacency null model
198 observed adjacent-attestation pairs occurring at least four
times were tested against 500 within-document permutations. This null preserves
each document's sign inventory while destroying local order.

93 positive-enrichment pairs survive Benjamini-Hochberg q <= 0.05 while
also retaining at least three confident-only observations.

These are **structural adjacency candidates**, not words, morphemes or phonetic
sequences.

## Position
Document-level initial/final enrichment is computed for signs with at least
eight occurrences. Position means position in the classified attestation stream,
not word-internal position.

## Site concentration
Normalized Shannon entropy identifies signs concentrated in a small number of
document-prefix site groups. This is descriptive only: archaeological sampling
and document type are obvious confounds.

## Bootstrap
The top 30 sign frequencies receive 95% document-bootstrap intervals from 500
replicates, so concentration in a few prolific documents is visible rather than
hidden behind a single count.

## Methodological guardrails
- certainty counts are retained alongside adjacency candidates
- multiple comparisons receive BH-FDR correction
- no phonetic/semantic interpretation is inferred
- no source uncertainty is silently normalized
- aggregate results only; the restricted full SigLA-derived row table is not
  redistributed

Nothing has been published to GitHub.
