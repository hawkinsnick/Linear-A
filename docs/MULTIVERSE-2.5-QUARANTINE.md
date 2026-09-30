# Historical Linear A 2.5 quarantine and replacement

The historical implementation remains scientifically invalid. Its active entry point now refuses all runs; its code is preserved under `scripts/history/` for audit only. No historical 2.5 output is supporting evidence.

The replacement is `scripts/run_structural_sensitivity_v1.py`, governed by the separately frozen `research/structural-sensitivity-repair-v1.json`. It uses per-word k/L probability and sum p(1-p) variance, actual joint boundary permutations, two declared diagnostic views, fixed-family Holm correction, and shared document-cluster bootstrap draws. Exact and synthetic negative controls are tested before historical-corpus execution.

This is a conditional same-corpus sensitivity repair: the candidates were originally selected using this corpus. Multiplicity correction does not reverse that selection bias. No prospective, linguistic or independent-replication claim follows. The frozen 3.1 cohort remains sealed.
