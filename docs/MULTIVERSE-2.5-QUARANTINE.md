# Historical Linear A 2.5 quarantine and replacement

The historical implementation remains scientifically invalid. Its active entry point now refuses all runs; its code is preserved under `scripts/history/` for audit only. No historical 2.5 output is supporting evidence.

The replacement is `scripts/run_structural_sensitivity_v1.py`, governed by the separately frozen `research/structural-sensitivity-repair-v1.json`. It uses per-word k/L probability and sum p(1-p) variance, actual joint boundary permutations, two declared diagnostic views, fixed-family Holm correction, and shared document-cluster bootstrap draws. Exact and synthetic negative controls are tested before historical-corpus execution.

This is a conditional same-corpus sensitivity repair: the candidates were originally selected using this corpus. Multiplicity correction does not reverse that selection bias. No prospective, linguistic or independent-replication claim follows. The frozen 3.1 cohort remains sealed.

## Executed repair

The protocol was published in commit `145094811b34e5675cd7e5ee5c56f5060c4f4614` before the replacement corpus run. Two full runs produced identical result bytes. `analysis/structural-sensitivity-repair-v1-result.json` reports all twelve candidates and both diagnostic views, with counts, effects, permutation p-values, fixed-family Holm corrections and document-bootstrap quantiles. `analysis/structural-sensitivity-repair-v1-execution.json` records protocol/result hashes and the repeat check.

The corpus has 1,283 nonempty source words, 836 types and 451 contributing documents. Six candidates exceed the historical 1.96 lower-bootstrap-z diagnostic. This threshold comparison is descriptive and conditional on prior candidate selection; it does not establish a linguistic confidence interval, independent replication or prospective success.

Reproduce the fixed run:

```sh
python scripts/run_structural_sensitivity_v1.py --spec research/structural-sensitivity-repair-v1.json --words data/source_words.csv --candidates data/candidate_registry_0.9.csv --out /tmp/structural-result.json
```

Inputs and derived data retain their SigLA CC BY-NC-SA 4.0 obligations.
