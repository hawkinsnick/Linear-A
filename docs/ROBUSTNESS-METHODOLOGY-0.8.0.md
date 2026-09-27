# 0.8.0 positional robustness methodology

0.8.0 begins with the 22 positive source-word positional enrichments surviving BH-FDR in 0.7.0 and subjects them to adversarial controls.

A signal receives `strict_robust=true` only if all of the following hold:
1. It remains significant after deduplicating exact source-word types and permuting sign order within each unique type (1,000 permutations; BH q<=.05).
2. Its analytic enrichment z remains >1.96 after leaving out every individual document in turn.
3. Its enrichment z remains >1.96 after leaving out every legacy heuristic site-prefix group in turn. This is sensitivity analysis, not canonical geography.
4. Its enrichment z remains >1.96 after removing every token of the single most frequent exact word type carrying that sign at that boundary.

The composite threshold is deliberately severe. It is an adversarial robustness screen, not a probability that a linguistic interpretation is true.

Document-type and period breakdowns are descriptive. No positional signal is called a prefix, suffix, morpheme, case marker, phonotactic rule or decipherment.

The `site_group_heuristic` field is not canonical site metadata and must not be interpreted as source-explicit geography.
