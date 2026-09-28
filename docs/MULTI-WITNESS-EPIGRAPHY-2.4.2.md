# 2.4.2 — Multi-witness epigraphic layer

## Objective
Represent multiple readings and contextual assertions about the same Linear A object without silently collapsing them into one transcription.

## Invariants
1. Canonical document identity is an object/crosswalk layer, not a claim that all sources agree.
2. Every reading or contextual statement is a source-specific assertion.
3. Agreement from sources with shared upstream ancestry is never counted as independent epigraphic confirmation.
4. Disagreement is stored explicitly; normalization may classify notation-only differences but never deletes the source forms.
5. Resolution requires a recorded rationale and may remain open.
6. Rights travel with each assertion. Repository availability does not establish redistribution permission.
7. The 2.3/2.4 frozen experiments and the 2.4.1 prospective cohort remain unchanged.

## Core records
- `document-identity`: canonical object identity plus source aliases and match basis.
- `witness-assertion`: one source making one claim at a defined locus.
- `source-lineage`: ancestry and independence class.
- `witness-disagreement`: explicit competing assertions and adjudication state.

## Evidence counting
Independent support is counted by independent lineage, not by number of websites or files. Two digital projects that reproduce the same upstream edition can provide useful cross-representation validation while contributing only one epigraphic lineage for evidential counting.

## Scope
2.4.2 builds the representation and validator. It does not declare any undeciphered reading linguistically correct and does not promote majority vote into an epigraphic truth rule.
