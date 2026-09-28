# Linear A Open Corpus — 0.4.0-rc4-local

RC4 executes the first structural analyses on the validated local SigLA snapshot.

## Snapshot
- 802 decoded documents; 787 represented in the attestation-level table
- 5144 attestations
- 4712 confident attestations
- 104 erasures
- 7 ghosts

## Certainty robustness
The top-30 classified sign set overlaps in 30/30 positions between
the all-attestation and confident-only analyses. Rank-order Spearman rho across
classified signs present in both sets is 0.9998.

This is a structural robustness result, not a decipherment result.

## Analyses
- aggregate sign frequency
- document-level initial/medial/final position
- adjacent-attestation pairs
- site/document distribution
- certainty sensitivity
- bounded impact statements for unresolved RC3 branches

The adjacency table deliberately says *adjacent attestations*, not linguistic
bigrams: array adjacency can cross uncertain boundaries, numerical material or
other structural divisions.

## External comparison
A 2026 University of Piraeus study has already run frequency, positional and
bigram analyses on a smaller 2,481-token GORILA-derived tablet corpus. RC4's
research target is therefore robustness: a larger SigLA snapshot, native
certainty states, and explicit uncertainty branches.

Nothing has been published to GitHub. The safe RC does not include the raw
5,144-row SigLA-derived table or drawings.
