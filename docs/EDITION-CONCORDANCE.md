# Linear A edition concordance — Step 1

Every one of the 802 source entries in the authenticated SigLA derivative now has explicit statuses for SigLA, GORILA, Raison–Pope 1980, Raison–Pope 1994 and RILA Supplement 1. This completes current-record accounting; edition resolution remains partial. This is a bibliographic evidence map, not a critical edition or a complete inventory of surviving inscriptions.

Open [the record table](../research/edition-concordance.csv) in a spreadsheet; filter by `source_record_id` or by an edition status. [The audit](../analysis/edition-concordance-audit.json) gives counts and input hashes. [Edition-route evidence](../research/edition-route-evidence.json) records acquisition scope, exact contents locators and unresolved publisher metadata disagreements.

| Evidence class | Source entries | Meaning |
|---|---:|---|
| GORILA page link, with existing primary case pages inspected | 8 | Exact whitespace-only source-ID correspondence to prior AI inspection; no expert autopsy or physical-object certification |
| GORILA page link, not directly inspected in the case audit | 747 | Attributed source locator parsed from the authenticated derivative |
| Source points to RILA Supplement 1 | 24 | Publisher identity confirmed; contents give candidate tablet-section starts, not exact entry matches |
| No usable edition reference | 23 | 19 absent values and 4 literal `missing` values remain explicit |
| Raison–Pope 1980 entry reconciliation unresolved | 802 | Entry-level edition content not acquired; do not infer matches from familiar sigla |
| Raison–Pope 1994 entry reconciliation unresolved | 802 | Publisher record inspected, but entry-level content not acquired |

The last two rows are edition-specific work queues over the same 802 entries, not additional inscriptions. The four mutually exclusive GORILA-routing rows sum to 802. All 802 entries remain directly attributed to the pinned SigLA derivative through unchanged IDs and JSON pointers. No source transcriptions, photographs, drawings or raw payloads are newly published.

## Counting and identity boundaries

- The 755 GORILA URLs break down as volume I: 266, II: 205, III: 246, IV: 24, V: 14. These are source-entry links, not independent objects or inspected pages.
- URL `sp` is a viewer index. Never turn it into a printed page by subtracting a guessed offset. Only the separately registered primary evidence supplies inspected printed-page locators.
- Repeated page links do not merge entries. Face suffixes, fragment letters and plus signs are retained; only whitespace is removed for joins to the existing case audit.
- Thirteen prior case entries have inspected GORILA pages. Ten case entries join eight exact source IDs. U010, U012 and U013 lack exact source-ID joins and therefore are not assigned to a nearby or similarly named row. SY Zb 7 and fraction K retain their separate source/interpretation barriers in the original dossier.
- RILA-S1's publisher totals (1,534 documents / 7,574 signs) are a separate editorial denominator. The present 802 SigLA entries / 5,144 attestations cannot be converted into a completeness percentage against them without reconciling faces, supports, editorial inclusions and sign-count conventions.
- Shared SigLA/GORILA ancestry is not independent replication. No new canonical reading, certified museum identity or scientific-readiness gate follows from this map.

## Reproduce

Supply the authorized exact source asset (SHA-256 `9a5e4783146144fc5ac54c5dc2b372b39cc0e0ea40ca15207243f8c539f03dd8`):

```sh
python scripts/build_edition_concordance.py /path/to/sigla-corpus.json --check
python scripts/build_edition_concordance.py --check
python scripts/test_edition_concordance.py
```

The first command replays every row from the authenticated input and registered evidence. The second checks committed integrity offline. The tests reject dropped or renamed IDs, unsupported Raison–Pope matches, object promotion and locator drift. CI performs the authenticated replay. No prospective cohort outcomes, predictions or calibration gold are read.

## Next acquisition work

1. Acquire lawful Raison–Pope entry/concordance pages and begin exact edition joins; preserve 1980 versus 1994 differences. Publisher metadata alone cannot resolve entries. The 1994 publisher and contemporary review disagree on pagination and the displayed Pope initial; both claims remain attributed.
2. Resolve the 23 unusable references from primary catalogues and publications. A missing source URL does not prove the inscription absent from GORILA or later editions.
3. Inspect RILA-S1 entries for the 24 source-linked records. Its contents identify tablet-section starts at Gournia p. 5, Kea p. 9, Khania p. 13, Knossos p. 33, Petras p. 37, Phaistos p. 45 and Thera p. 49; these are acquisition targets. The general concordance begins at p. xxvi. EFA dates the publication 2025 while Peeters displays 2024; neither assertion is silently replaced.
4. Extend exact GORILA page inspection beyond the current eight source records and resolve the three unjoined inspected case identities before claiming corpus-wide collation.

## Rights and attribution

The source-derived identifier/locator table retains **CC BY-NC-SA 4.0** and attribution to **Ester Salgarella and Simon Castellan, SigLA**, through the authenticated **Ryan Pavlicek/pyaegean** derivative. Original code and documentation follow their repository component terms. Source-specific terms govern; this table is not relicensed by the project's original-content license. Edition metadata and original summaries add no license to redistribute edition text or images.
