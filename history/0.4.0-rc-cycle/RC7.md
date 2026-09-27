# 0.4.0 RC7 — historical snapshot

Local tree contained 51 files.

Variable-slot/template-family experiment over document-stream windows. Reported 440 candidate families, 224 strong and 166 cross-site-heuristic strong, plus a Hamming-distance-one motif graph.

**Important supersession:** later auditing found that the confident-only construction filtered uncertain signs before recomputing windows, which could bridge across uncertainty. RC7 is retained as historical evidence of the method and the bug, not as the current source-word result.

Audit: 14/14 under the then-current tests.
