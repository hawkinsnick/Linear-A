# Linear A Open Corpus — 0.4.0-rc6-local

RC6 tests whether RC5's enriched pairwise relationships assemble into larger,
recurring structures.

## Motif test
163 recurring 3–6-sign candidates were tested against 300
document-preserving within-document permutations. Candidate thresholds are
>=3 observations for trigrams and >=2 for lengths 4–6.

After BH-FDR correction and additional requirements of at least two confident
occurrences and occurrence in at least two documents, 87 motifs survive.
11 of these occur across at least two site-prefix groups.

These are **structural motifs**, not deciphered words or morphemes.

## Network
RC6 also exports directed weighted sign-network node statistics and forward /
backward conditional probabilities. These identify hubs and constrained
transitions without assigning phonetic or semantic values.

## Nesting
Long motifs are linked to shorter robust submotifs so repeated formula-like
structures can be distinguished from isolated pair effects.

## Caveats
The null model preserves document sign inventories but destroys all local
ordering. Site-prefix grouping is still a heuristic. Document order is not
automatically linguistic token order. Future work should add document-type,
chronology, and explicit word-boundary controls.

Nothing has been published to GitHub and the safe package does not redistribute
the raw SigLA-derived 5,144-row table.
