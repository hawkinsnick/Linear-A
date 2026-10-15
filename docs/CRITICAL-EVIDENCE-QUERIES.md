# Querying evidence and alternatives — 2026-10-15

This first implementation makes the existing Linear A critical pilot queryable. It adds no source acquisition, canonical reading, physical observation, restoration, independent confirmation or expert acceptance. The pilot is problem-selected, not a representative sample of Linear A or the other corpora.

## Use

From the repository root:

```sh
python scripts/query_critical_evidence.py --record 'HT 17'
python scripts/query_critical_evidence.py --record 'HT 49a'
python scripts/query_critical_evidence.py --coverage
python scripts/test_critical_evidence_query.py
```

Output is JSON. IDs must match the pilot exactly: `HT17` is not silently merged into `HT 17`, and faces are not collapsed. Absence from this pilot is not absence from the corpus or historical record.

Each dossier separates the source-reported record, complete SigLA attestation slots, attributed editorial assertions, source/page locators, and legacy queue cases. Assertions retain IDs, source levels, limitations and locator details. Edition locators retain printed and viewer page numbers, inspection status and source lineage. The original input SHA-256 is included for reproducibility; a checksum verifies bytes, not historical accuracy. Existing pilot validation runs before every query.

## Measured starting point

The replayable report is `analysis/critical-evidence-coverage-v1.json`:

- 10 source entries with 168 source attestation slots, including blank and uncertain slots.
- 51 attributed assertions about metadata, edition presentation and other explicitly identified fields; these are not 51 alternative readings.
- 15 legacy queue cases: 10 linked to pilot entries, 5 without a pilot entry join. The latter are retained explicitly in the coverage output, including one interpretation-only metrology case that is not an inscription.
- Zero pairs of alternatives individually collated to attributed scholarly witnesses within this pilot; zero expert-validated records. This is not a claim that scholarship contains no attributed alternatives.

For HT 17, U001 records `37 vs 38`, but its disposition says the attribution of 37 remains untraced. The source excerpt list is empty for this quantity case. The separate edition assertion of 38 must not be used to invent a source for 37 or a quantity field in the SigLA witness. Likewise, untranslated raw flags are not damage observations, and source slot indices are not inscription line numbers.

## Next evidence task

Trace each alternative in the 10 joined cases to a specific author/edition, exact locator, literal reading, and the extent of actual consultation. Record source lineage and distinguish editorial differences, segmentation alternatives, damage, restorations and model hypotheses. Require explicit alignment before comparing readings at the same position. Preserve unresolved attribution when the evidence cannot be obtained. The five unjoined cases need identity or interpretation review before source collation.

Extend this workflow to other corpora only through their native evidence models. Do not project this pilot's counts, fields or acceptance state onto other members.

## Rights and boundaries

The tool reads already committed evidence and preserves its existing mixed rights statement; it introduces no permission to ingest GORILA, reproduce plates, or redistribute restricted content. SigLA-derived witness material retains attribution to Ester Salgarella and Simon Castellan, its pyaegean intermediary, and CC BY-NC-SA 4.0 terms. See `SOURCE-POLICY.md`, `DATA-LICENSE-MATRIX.md` and the source pilot. Historical consultation records do not imply permission for new extraction. This query output is a view of the same evidence, not another independent witness.

## Completed bounded attribution pass

The [ten-case audit](LEGACY-CASE-ATTRIBUTION.md) now qualifies the ten joined cases. Dossiers include `current_attribution_audit` beside unchanged legacy literals. All cases retain explicit evidence gaps; the historical registers do not supply missing source authors or same-locus alignment.
