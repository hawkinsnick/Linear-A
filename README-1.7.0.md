# 1.7.0 — document-resampled robustness

The twelve frozen positional signals are stress-tested by resampling whole documents
rather than treating word tokens as independent observations. Across 1,000 document
cluster-bootstrap replicates, **6 / 12**
have a 2.5th-percentile enrichment z above 1.96.

This is a robustness sensitivity interval over corpus composition. It is not a
confidence interval for a linguistic interpretation.
