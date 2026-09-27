# 0.8.0 RC cycle

## RC1 — type deduplication
Repeated exact word tokens were prevented from driving positional significance. Each unique source-word type was counted once and sign order was permuted within type.

## RC2 — leave-one-out stability
All 22 candidates were retested after excluding each document and each legacy heuristic site-prefix group in turn.

## RC3 — dominant-form ablation
For every candidate, all tokens of the most frequent exact word type carrying that boundary sign were removed.

## RC4 — context sensitivity
Document-type and period breakdowns were retained as descriptive controls. The site-prefix grouping is explicitly noncanonical.

## RC5 — interpretation firewall
The 22 original signals split into 12 strict survivors and 10 downgraded/context-sensitive signals. Attested-remainder relations remain formal/distributional observations only; no affix semantics are assigned.
