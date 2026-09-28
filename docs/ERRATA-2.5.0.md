# 2.5.0 statistical errata and inheritance audit

## E-003 — 0.9 internal-position negative control is superseded

The released `analysis/candidate_internal_position_negative_control.csv` compares boundary counts drawn from the broad source-word population with random internal-position counts that can only arise in words having an eligible internal position. Those supports/denominators are not matched.

Accordingly, the historical claim that all 12 candidates "pass" this internal-position negative control is withdrawn. The file remains in history for transparency and must not be used as current evidence.

This correction does **not** by itself invalidate the separate 0.9 type-level permutation multiverse, the 0.8 adversarial screen, or the 1.7 document-cluster bootstrap.

## E-004 — 0.9 Holm table recheck

The displayed 12 raw p-values and `holm_p` values in `analysis/candidate_type_multiverse.csv` are consistent with standard step-down Holm adjustment: sort ascending, multiply by the number of remaining hypotheses, enforce monotonic non-decrease, cap at 1, and restore original order.

The Holm implementation concern is therefore closed for the released table values. This audit does not strengthen the underlying permutation model beyond its original assumptions.
