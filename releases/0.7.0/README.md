# Linear A Open Corpus — 0.7.0

0.7.0 is the source-word analytical release.

It uses the 1,283 nonempty SigLA-defined Word objects validated in 0.6.0 rather than inferred document-stream boundaries.

Headline results:
- 836 distinct source-word types
- 668 hapax types
- 168 recurrent types
- 4,681 Hamming-distance-one links among attested equal-length word types
- 651 form pairs related by one added initial or final sign
- 79 variable-slot families under the explicit recurrence criterion
- 22 positive sign-position enrichments after BH-FDR under 1,000 within-word permutations

The variable-slot family count has a within-word shuffle-null mean of 74.37 and empirical upper-tail p=0.0598 (300 permutations). It is therefore reported as a distributional candidate pattern, not a significant morphological result.

No result is labeled a prefix, suffix, morpheme, case ending, grammatical rule, phonotactic rule, translation or decipherment.

f3 remains analytically separate and unresolved/evidence-tiered.

Site correction: the inherited 0.6 site_id field was document-label-prefix derived. Public 0.7 documentation calls it site_group_heuristic and does not treat it as canonical source-explicit site metadata.
