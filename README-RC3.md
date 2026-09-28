# Linear A Open Corpus — 0.4.0-rc3-local

RC3 turns the audited corpus architecture into a branch-aware research platform.

## New result: KN Zc 6
Published archaeological evidence establishes an actual punctuation mark
separating the beginning and end of the second sign-group on KN Zc 6. The same
publication documents the painted, cursive, dextroverse spiral arrangement on
the interior of HM P2630. The physical separator is therefore an observation;
its linguistic function remains interpretation.

## Remaining uncertainty
RC3 does not manufacture resolutions for HT17, HT34, HT49a, KH74, KH8 or
fraction K. Instead, each becomes an explicit branch usable by downstream
analyses.

## Analytical reproducibility
`data/branch_catalog.csv` defines alternate readings/values.
`data/uncertainty_analysis_schema.json` defines how results must record branch
configuration, certainty filters and source snapshot.
`scripts/branch_frequency.py` is a minimal executable frequency runner designed
for a locally generated corpus.

## Sensitivity
Rare/singleton forms such as A567 are maximally sensitive to a single
classification change. Fraction K is mathematically high-impact: 1/10 versus
1/16 differs by 37.5% relative to 1/10. These uncertainties must be branched,
not averaged or silently selected.

No raw SigLA database, copyrighted plate/image corpus, or third-party book is
bundled. Nothing has been published to GitHub.
