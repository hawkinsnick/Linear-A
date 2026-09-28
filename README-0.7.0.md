# Linear A Open Corpus — 0.7.0-local

0.7.0 is the source-word analytical release.

It uses the 1,283 nonempty SigLA-defined Word objects validated in 0.6.0,
rather than inferred document-stream boundaries.

Headline descriptive results:
- 836 distinct source-word types
- 668 hapax types
- 168 recurrent types
- 69 recurrent types represented across at least two legacy heuristic site-prefix groups
- 4,681 Hamming-distance-one links among attested equal-length word types
- 651 form pairs related by one added initial or final sign
- 79 variable-slot families under the explicit recurrence criterion
- 22 positive sign-position enrichments after BH-FDR under 1,000 within-word permutations

The 79 family count is far above its within-word shuffle null
(mean 74.37; empirical upper p 0.0598, 300 permutations), but this is a
distributional result only.

No result in this release is labeled a prefix, suffix, morpheme, case ending,
grammatical rule, phonotactic rule, translation, or decipherment.

`f3` remains analytically separate and unresolved/evidence-tiered.
Nothing has been published to GitHub.

## Site correction

The inherited 0.6 `site_id` field was document-label-prefix derived. It is renamed `site_group_heuristic` here. No canonical source-explicit site claim is made from that field.
