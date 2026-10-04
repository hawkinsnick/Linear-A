# Linear A critical pilot and review handoff

10 declared source entries, not 10 certified objects; bounded critical metadata and disagreement pilot, not a complete critical transcription.

Eight exact source entries behind the existing inspected disagreement cases, plus ARKH 2 and KN Zb 40 to add Arkhanes, another vessel form and a quantity-bearing tablet. Convenience/problem-driven selection, not a representative sample.

## Reproduce

```sh
python scripts/build_critical_pilot.py /path/to/sigla-corpus.json --check
python scripts/build_critical_pilot.py --check
python scripts/build_critical_pilot.py --check --verify-assets /path/to/lawfully-acquired-assets
python scripts/test_critical_pilot.py
```

The first command verifies the pinned source bytes, every selected context field and every excerpt pointer. The second replays committed views without acquiring source files. Page hashes identify the consulted images; automated replay cannot certify their epigraphic content.

## Boundaries and review queue

Ten source entries span five source-reported sites and three source-reported forms. Entries, surfaces, photographs, editorial groups and physical objects are separate units. No full critical transcription, object-level join or independent expert approval is claimed. Unknown context, join and restoration fields remain explicit.

Raison–Pope remains entry-level unresolved. The earlier Step 1 concordance reports its original eight exact inspected source entries; this separate pilot adds ARKH 2 and KN Zb 40 and new field-level assertions. Historical counts are not overwritten.

Use [the blank 25-item review sheet](../reviews/critical-pilot-review.tsv) and [the attributed comparison CSV](../research/critical-disagreement-comparison.csv). Every decision is UNREVIEWED. Record a subsequent decision as a separate attributed assertion with reviewer, date, locator, scope and source dependence; do not overwrite these witness assertions.

## Source-bound entry dossiers

### HT 15

Authenticated SigLA pointer `/documents/77`; source-reported site **Haghia Triada**, form **Tablet**, period **LM IB**; dimensions (source order) `[5.1,6.9,0.9]`; 12 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 16 | GORILA 1, printed p. 30, viewer 66: Target entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=66); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| dimension_caption | 5,10 × 6,90 × 0,90 cm | GORILA 1, printed p. 30, viewer 66: Target entry dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=66); PRIMARY_EDITION_REPORTED; Source order and brackets retained; axis meanings, restoration and physical joins are not inferred. No sum of fragment dimensions. |
| numbered_rows | [1,2,3,4,5] | GORILA 1, printed p. 31, viewer 67: Upper target diplomatic presentation; numbered rows are not linguistic words or object counts. (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=67); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| printed_damage_commentary | Row 3 numeral commentary allows additional/reconstructed strokes or a larger quantity; row 5 is marked vestigia. | GORILA 1, printed p. 31, viewer 67: Comment below upper tracing and vestigia label on row 5 (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=67); PRIMARY_EDITION_REPORTED; The printed 570 is retained as an integer component; commentary does not certify a complete physical amount. |
| editorial_quantity_components | [{"edition_group":"1–2","integer_component":684,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"2–3","integer_component":570,"symbolic_component_status":"ABSENT","terminal_status":"EDITION_COMMENTARY_QUESTIONS_COMPLETENESS","note":"Printed 570; row 3 commentary raises reconstruction/additional numeral strokes or larger amount."},{"edition_group":"4 / second amount","integer_component":400,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""}] | GORILA 1, printed p. 31, viewer 67: Lower grouped target presentation; repeated row numbers disambiguated by amount order (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=67); PRIMARY_EDITION_REPORTED; Arabic integer components only. Non-Arabic quantity signs are left untranscribed; no rational fraction, restored tail, total, balance or SigLA quantity mapping is inferred. |

Source encoding diagnostics: `{"editorial_groups":3,"blank_slots":1,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### HT 17

Authenticated SigLA pointer `/documents/91`; source-reported site **Haghia Triada**, form **Tablet**, period **LM IB**; dimensions (source order) `[4.6,5.6,0.7]`; 11 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 23 | GORILA 1, printed p. 34, viewer 70: Target entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=70); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| dimension_caption | 4,60 × 5,60 × 0,70 cm | GORILA 1, printed p. 34, viewer 70: Target entry dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=70); PRIMARY_EDITION_REPORTED; Source order and brackets retained; axis meanings, restoration and physical joins are not inferred. No sum of fragment dimensions. |
| numbered_rows | [1,2,3,4] | GORILA 1, printed p. 35, viewer 71: Upper HT 17 entry (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=71); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| vacat_rows | [4] | GORILA 1, printed p. 35, viewer 71: HT 17 row 4; HT 18 lower panel excluded (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=71); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| editorial_quantities | [{"edition_group":"1–2","quantity":38},{"edition_group":"2","quantity":10},{"edition_group":"3","quantity":5}] | GORILA 1, printed p. 35, viewer 71: Upper HT 17 grouped rows (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=71); PRIMARY_EDITION_REPORTED; Printed edition numbers; the lower HT 18 entry is excluded. The legacy quantity 37 is retained as an untraced project alternative. |
| editorial_quantity_components | [{"edition_group":"1–2","integer_component":38,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"2","integer_component":10,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3","integer_component":5,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""}] | GORILA 1, printed p. 35, viewer 71: Lower target grouped presentation (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=71); PRIMARY_EDITION_REPORTED; Re-expresses the already inspected edition quantities as explicit components; not additional independent evidence. |

Source encoding diagnostics: `{"editorial_groups":3,"blank_slots":1,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### HT 34

Authenticated SigLA pointer `/documents/116`; source-reported site **Haghia Triada**, form **Tablet**, period **LM IB**; dimensions (source order) `[5.0,7.6,0.9]`; 29 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 22 | GORILA 1, printed p. 64, viewer 100: Target entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=100); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| dimension_caption | 5,00 × 7,60 × 0,90 cm | GORILA 1, printed p. 64, viewer 100: Target entry dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=100); PRIMARY_EDITION_REPORTED; Source order and brackets retained; axis meanings, restoration and physical joins are not inferred. No sum of fragment dimensions. |
| damage_presentation | A central region is hatched as missing in the edition drawing. | GORILA 1, printed p. 64, viewer 100: Right-hand facsimile (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=100); PRIMARY_EDITION_REPORTED; Drawing convention observation only; lost sign count and restored content remain unknown. |
| numbered_rows | [1,2,3,4,5,6,7] | GORILA 1, printed p. 65, viewer 101: Upper target diplomatic presentation; numbered rows are not linguistic words or object counts. (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=101); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| printed_damage_commentary | Lower presentation includes an open ending after 200 and uncertain bracketed continuation after 30. | GORILA 1, printed p. 65, viewer 101: Lower entry rows 3 and 6 (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=101); PRIMARY_EDITION_REPORTED; No restoration is imported; suffixes and symbolic quantity signs remain unresolved. |
| editorial_quantity_components | [{"edition_group":"3 / first amount","integer_component":200,"symbolic_component_status":"ABSENT","terminal_status":"OPEN_BRACKET","note":""},{"edition_group":"3 / second amount","integer_component":2,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"4 / amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"5","integer_component":245,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / first amount","integer_component":100,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / second amount","integer_component":70,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / third amount","integer_component":30,"symbolic_component_status":"ABSENT","terminal_status":"UNCERTAIN_BRACKETED_CONTINUATION","note":"Bracketed continuation is retained as uncertain; no reconstructed unit count added."},{"edition_group":"7 / first amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"7 / second amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""}] | GORILA 1, printed p. 65, viewer 101: Lower grouped target presentation; repeated row numbers disambiguated by amount order (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=101); PRIMARY_EDITION_REPORTED; Arabic integer components only. Non-Arabic quantity signs are left untranscribed; no rational fraction, restored tail, total, balance or SigLA quantity mapping is inferred. |

Source encoding diagnostics: `{"editorial_groups":4,"blank_slots":3,"fraction_slots":7,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### HT 49a

Authenticated SigLA pointer `/documents/136`; source-reported site **Haghia Triada**, form **Tablet**, period **LM IB**; dimensions (source order) `[5.5,9.2,0.7]`; 32 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 55 | GORILA 1, printed p. 92, viewer 128: Target entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=128); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| dimension_caption | 5,50 × [3,00]+[6,20] × 0,70 cm | GORILA 1, printed p. 92, viewer 128: Target entry dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=128); PRIMARY_EDITION_REPORTED; Source order and brackets retained; axis meanings, restoration and physical joins are not inferred. No sum of fragment dimensions. |
| numbered_rows | [1,2,3,4,5,6,7,8] | GORILA 1, printed p. 93, viewer 129: Upper target diplomatic presentation; numbered rows are not linguistic words or object counts. (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=129); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| printed_damage_labels | ["sup. mut.","inf. mut.","vest."] | GORILA 1, printed p. 93, viewer 129: Upper and lower entry; marginal labels and vestigia markers (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=129); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| editorial_quantity_components | [{"edition_group":"2","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"OPEN_BRACKET","note":""},{"edition_group":"3 / first amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3 / second amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"4","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"OPEN_BRACKET","note":""},{"edition_group":"5","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / first amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / second amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6 / third amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"6–7","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"7 / first amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"7 / second amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"8 / first amount","integer_component":5,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"8 / second amount","integer_component":4,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"8 / third amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"OPEN_BRACKET","note":""}] | GORILA 1, printed p. 93, viewer 129: Lower grouped target presentation; repeated row numbers disambiguated by amount order (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=1&sp=129); PRIMARY_EDITION_REPORTED; Arabic integer components only. Non-Arabic quantity signs are left untranscribed; no rational fraction, restored tail, total, balance or SigLA quantity mapping is inferred. |

Source encoding diagnostics: `{"editorial_groups":12,"blank_slots":7,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### KH 74

Authenticated SigLA pointer `/documents/466`; source-reported site **Khania**, form **Tablet**, period **LM IB**; dimensions (source order) `[3.6,3.6,1.2]`; 7 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| dimension_caption | [3,60] × [3,60] × 1,20 cm | GORILA 3, printed p. 92, viewer 116: Upper entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=116); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| damage_caption | Upper edge is cut, as described by the edition. | GORILA 3, printed p. 92, viewer 116: Upper entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=116); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| numbered_rows | [1,2] | GORILA 3, printed p. 93, viewer 117: Upper target diplomatic presentation; numbered rows are not linguistic words or object counts. (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=117); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| printed_damage_labels | ["inf. mut."] | GORILA 3, printed p. 93, viewer 117: Upper KH 74 entry only; KH 75 and KH 76 panels excluded (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=117); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |

Source encoding diagnostics: `{"editorial_groups":3,"blank_slots":1,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### KH 8

Authenticated SigLA pointer `/documents/475`; source-reported site **Khania**, form **Tablet**, period **LM IB**; dimensions (source order) `[7.7,6.8,1.3]`; 15 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| dimension_caption | [7,70] × [6,80] × 1,30 cm | GORILA 3, printed p. 32, viewer 56: Dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=56); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| damage_caption | Lower edge is cut, as described by the edition. | GORILA 3, printed p. 32, viewer 56: Caption below drawing (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=56); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| numbered_rows | [1,2,3,4] | GORILA 3, printed p. 33, viewer 57: Upper target diplomatic presentation; numbered rows are not linguistic words or object counts. (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=57); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| printed_damage_labels | ["sup. mut."] | GORILA 3, printed p. 33, viewer 57: Target KH 8 entry (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=57); PRIMARY_EDITION_REPORTED; Edition presentation checked by AI; no physical autopsy, independent source or expert approval. |
| editorial_quantity_components | [{"edition_group":"2 / first amount","integer_component":2,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"2 / second amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3 / first amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3 / second amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3 / third amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"4 / first amount","integer_component":null,"symbolic_component_status":"PRESENT_UNTRANSCRIBED","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"4 / second amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"4 / third amount","integer_component":1,"symbolic_component_status":"ABSENT","terminal_status":"OPEN_BRACKET","note":""}] | GORILA 3, printed p. 33, viewer 57: Lower grouped target presentation; repeated row numbers disambiguated by amount order (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=57); PRIMARY_EDITION_REPORTED; Arabic integer components only. Non-Arabic quantity signs are left untranscribed; no rational fraction, restored tail, total, balance or SigLA quantity mapping is inferred. |

Source encoding diagnostics: `{"editorial_groups":3,"blank_slots":3,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### MA 10b

Authenticated SigLA pointer `/documents/651`; source-reported site **Mallia**, form **Tablet**, period **MM IIIB**; dimensions (source order) `[8.5,2.5,2.8]`; 10 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| surface_presentation | The edition heading is MA 10, with photographs labelled a, b, c and d; this source record refers to b. | GORILA 5, printed p. 50, viewer 102: Second photograph labelled b (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=5&sp=102); PRIMARY_EDITION_REPORTED; A face label is not an independent object; no equivalence of other source records is asserted. |
| inventory_label | A. Nik. M. 7336 | GORILA 5, printed p. 51, viewer 103: Bottom caption of MA 10 drawing page (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=5&sp=103); PRIMARY_EDITION_REPORTED; Printed inventory label only; no modern accession certification or object autopsy. |
| dimension_caption | [8,50] × 2,50 × 2,80 cm | GORILA 5, printed p. 51, viewer 103: Bottom parent-object caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=5&sp=103); PRIMARY_EDITION_REPORTED; Parent MA 10 bar dimensions, not separately measured face b. Brackets and source order retained. |
| object_form_caption | Barre à quatre faces | GORILA 5, printed p. 51, viewer 103: Bottom caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=5&sp=103); PRIMARY_EDITION_REPORTED; The edition describes a four-faced bar; the SigLA source classifies the selected entry as Tablet. Distinct descriptions are preserved without replacing either. |
| edition_counting_unit | {"entry_unit":"face b","parent_edition_heading":"MA 10","caption_form":"four-faced bar","published_face_labels":["a","b","c","d"],"physical_identity_certified":false} | GORILA 5, printed p. 51, viewer 103: Drawing b among four labelled faces under MA 10 (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=5&sp=103); PRIMARY_EDITION_REPORTED; Edition-level face relationship only; not four certified objects or a new physical join. |

Source encoding diagnostics: `{"editorial_groups":1,"blank_slots":1,"fraction_slots":1,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### KN Zc 6

Authenticated SigLA pointer `/documents/644`; source-reported site **Knossos**, form **Cup**, period **MM III?**; dimensions (source order) `null`; 23 source attestations. These are source encodings, not independently counted physical signs.

Find context: ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| layout_presentation | Interior curved inscription shown in two vessel photographs; the following page supplies a curved drawing and linearized presentation. | GORILA 4, printed p. 119, viewer 161: Two photographs (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=4&sp=161); PRIMARY_EDITION_REPORTED; No glyph coordinates, linguistic boundaries or expert reading order established. |
| layout_presentation | Curved facsimile above a linearized presentation with dot marks. | GORILA 4, printed p. 120, viewer 162: Upper drawing and bottom transcription (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=4&sp=162); PRIMARY_EDITION_REPORTED; No exact sign boundary or linguistic word segmentation is adjudicated. |
| inventory_label | HM P2630 | Flouda 2013, DOI 10.5334/bai.h: Original p. 160 (indexed publication), reprint Figure 15a caption; public reprint evidence https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.02:_Introduction_and_Figures; https://socialsci.libretexts.org/@api/deki/files/26432/Screen_Shot_2019-11-08_at_4.05.57_PM.png?revision=1; ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT; Attributed Flouda report checked in a public scholarly HTML reprint. Figure 15 was inspected separately; original PDF not acquired. No independent source lineage, modern inventory certification or exact linguistic boundary asserted. |
| rim_diameter_cm | 8.4 | Flouda 2013, DOI 10.5334/bai.h: Original p. 160 (indexed publication), reprint Figure 15a caption; public reprint evidence https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.02:_Introduction_and_Figures; https://socialsci.libretexts.org/@api/deki/files/26432/Screen_Shot_2019-11-08_at_4.05.57_PM.png?revision=1; ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT; Attributed Flouda report checked in a public scholarly HTML reprint. Figure 15 was inspected separately; original PDF not acquired. No independent source lineage, modern inventory certification or exact linguistic boundary asserted. |
| find_context | House basement at Knossos, reported jointly for cups KN Zc 6–7. | Flouda 2013, DOI 10.5334/bai.h: Original p. 160 (indexed publication), reprint Alignment and Directionality, opening cup paragraph; public reprint evidence https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.04:_Linear_A_-_The_social_and_cultural_construction_of_Neopalatial_literacy; ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT; Attributed Flouda report checked in a public scholarly HTML reprint. Figure 15 was inspected separately; original PDF not acquired. No independent source lineage, modern inventory certification or exact linguistic boundary asserted. |
| reading_layout | Author reports an outward dextroverse spiral, with sign tops towards the cup base. | Flouda 2013, DOI 10.5334/bai.h: Original p. 162 (indexed publication), reprint Alignment and Directionality, reading-order and punctuation paragraph; public reprint evidence https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.04:_Linear_A_-_The_social_and_cultural_construction_of_Neopalatial_literacy; ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT; Attributed Flouda report checked in a public scholarly HTML reprint. Figure 15 was inspected separately; original PDF not acquired. No independent source lineage, modern inventory certification or exact linguistic boundary asserted. |
| punctuation | Author reports punctuation delimiting the second sign group of KN Zc 6. | Flouda 2013, DOI 10.5334/bai.h: Original p. 162 (indexed publication), reprint Alignment and Directionality, reading-order and punctuation paragraph; public reprint evidence https://socialsci.libretexts.org/Bookshelves/Anthropology/Archaeology/Book:_Writing_as_Material_Practice_-_Substance_Surface_and_Medium_(Piquette_et_al.)/08:_Materiality_of_Minoan_Writing-_Modes_of_Display_and_Perception_(Georgia_Flouda)/8.04:_Linear_A_-_The_social_and_cultural_construction_of_Neopalatial_literacy; ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT; Attributed Flouda report checked in a public scholarly HTML reprint. Figure 15 was inspected separately; original PDF not acquired. No independent source lineage, modern inventory certification or exact linguistic boundary asserted. |

Source encoding diagnostics: `{"editorial_groups":4,"blank_slots":1,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### ARKH 2

Authenticated SigLA pointer `/documents/2`; source-reported site **Arkhanes**, form **Tablet**, period **LM I**; dimensions (source order) `[4.9,7.5,0.7]`; 23 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 1673 | GORILA 3, printed p. 6, viewer 30: Target entry caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=30); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| dimension_caption | 4,90 × 7,50 × 0,70 cm | GORILA 3, printed p. 6, viewer 30: Target entry dimension caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=30); PRIMARY_EDITION_REPORTED; Source order and brackets retained; axis meanings, restoration and physical joins are not inferred. No sum of fragment dimensions. |
| numbered_rows | [1,2,3,4,5,6] | GORILA 3, printed p. 7, viewer 31: Upper diplomatic drawing (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=31); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| editorial_quantities | [{"edition_group":"1–2","quantity":5},{"edition_group":"2–3","quantity":12},{"edition_group":"3–4","quantity":6},{"edition_group":"5–6","quantity":4}] | GORILA 3, printed p. 7, viewer 31: Lower grouped edition presentation (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=31); PRIMARY_EDITION_REPORTED; Printed edition numbers; not sign-series numbers, linguistic words or physical numeral adjudications. |
| editorial_quantity_components | [{"edition_group":"1–2","integer_component":5,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"2–3","integer_component":12,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"3–4","integer_component":6,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""},{"edition_group":"5–6","integer_component":4,"symbolic_component_status":"ABSENT","terminal_status":"NO_MARKED_LOSS","note":""}] | GORILA 3, printed p. 7, viewer 31: Lower target grouped presentation (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&sp=31); PRIMARY_EDITION_REPORTED; Re-expresses the already inspected edition quantities as explicit components; not additional independent evidence. |

Source encoding diagnostics: `{"editorial_groups":6,"blank_slots":0,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

### KN Zb 40

Authenticated SigLA pointer `/documents/642`; source-reported site **Knossos**, form **Pithoid jar**, period **LM II**; dimensions (source order) `null`; 6 source attestations. These are source encodings, not independently counted physical signs.

Find context: NOT_SOURCE_COLLATED_IN_THIS_PILOT. Joins: UNASSESSED. Restorations: NO_NEW_RESTORATION_ENTERED. Modern inventory identity unverified.

| Field | Attributed assertion | Exact locator and boundary |
|---|---|---|
| inventory_label | HM 21391 | GORILA 4, printed p. 83, viewer 125: Caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=4&sp=125); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| vessel_caption | Pithoid jar | GORILA 4, printed p. 83, viewer 125: Caption (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=4&sp=125); PRIMARY_EDITION_REPORTED; Edition-level assertion; no physical autopsy or certified modern inventory identity. |
| numbered_rows | [1,2] | GORILA 4, printed p. 83, viewer 125: Numbered transcription rows (https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=4&sp=125); PRIMARY_EDITION_REPORTED; Two presentations on one edition page are not independent witnesses or two inscriptions. |

Source encoding diagnostics: `{"editorial_groups":2,"blank_slots":0,"fraction_slots":0,"account_quantity_field":"NOT_SUPPLIED","line_and_glyph_coordinates":"NOT_SUPPLIED","raw_flags":"PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS"}`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.

## Fifteen unresolved comparisons

Legacy alternatives are preserved project queue strings. They do not become verified Raison–Pope, GORILA or SigLA witness readings merely by appearing here. Exact authenticated excerpts and inspected edition facts are separate columns in the CSV.

| Case | Project alternatives | Current source-bound assessment |
|---|---|---|
| U001 / HT17 | 37 vs 38 | GORILA prints 38, 10 and 5 in the HT 17 panel. Legacy quantity 37 remains untraced: this SigLA export supplies no account quantities. Its sign number 37 denotes TI, not a numeral quantity. This does not prove the origin of the legacy error or adjudicate the object. |
| U002 / HT15 | L4L4 vs L3L3 | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U003 / HT17 | private-use/variant vs *164A | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U004 / HT34 | SI*516 vs SII | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U005 / HT34 | MIJAI vs MIJARU | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U006 / HT49a | SUKI vs SU + VESST | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U007 / KH74 | SI*805MI vs SI*301MI | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U008 / KH8 | QA2PU vs *510 | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U009 / MA10b | TI*412VAS vs *404TI | Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict. |
| U010 / HTZd157+156 | TAJA\|K vs TAJAK | No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question. |
| U011 / KNZc6 | single group vs split before IZU | SigLA supplies four source editorial groups. Flouda p. 162 reports punctuation around the second sign group. Neither establishes the legacy exact split before IZU; source blank and label *79 are preserved without equating them to a restored sign or linguistic boundary. |
| U012 / PKZa8 | JASAUNAKANASI vs JASA\|UNAKANASI | No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question. |
| U013 / PRZa1 | TANASUTEKE vs TANASUTE\|KE | No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question. |
| U014 / SYZb7 | RAKINISE vs RAKI\|NISE | No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question. |
| U015 / fraction K | 1/16 vs 1/10 | No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question. |

## Acquisition barriers and negative evidence

GORILA IV viewer page 126 is blank, has no printed page number and is not a continuation of KN Zb 40. It has no entry binding or field assertions. Multiple representations of an inscription in GORILA share the same edition lineage.

Flouda 2013, pp. 160 and 162: initially consulted indexed publication text was supplemented by direct public LibreTexts reprint HTML and Figure 15 inspection. Panel a is KN Zc 6; panel b is KN Zc 7 and excluded. The separately inspected Figure 16a ring image is excluded from cup assertions. Publisher, institutional PDF and OAPEN direct routes returned HTTP 403; the web PDF parser also rejected its 15,064,351-byte size. The original PDF remains unacquired; no access control was bypassed. Flouda cites GORILA and is not presumed an independent object witness. Exact reprint URLs and acquired-byte hashes are in the source record.

## Remaining scholarly work

1. Verify the edition captions and quantities against the linked primary pages; distinguish source errors from object readings.
2. Trace each legacy alternative to its exact witness and locator; do not equate project alternatives with verified edition readings.
3. Verify fragment/face joins, restorations and modern inventory identities against catalogue or object evidence.
4. Acquire a lawful Raison–Pope edition and establish entry-level crosswalks before claiming parity.
5. Expand the critical transcription and graphical uncertainty layer beyond this bounded metadata pilot.

## Rights and attribution

Ester Salgarella and Simon Castellan, SigLA, via Ryan Pavlicek/pyaegean sigla-corpus-v4. Mixed dossier retains source-specific terms: SigLA metadata/excerpts CC BY-NC-SA 4.0; original brief annotations and tools under repository contribution terms; no GORILA pages, full transcriptions or Flouda text reproduced. No new grant over third-party material.

## Downloadable source witness

[Selected SigLA witness JSON](../research/critical-pilot-sigla-witness.json) and [the 168-slot source CSV](../research/critical-pilot-sigla-slots.csv) retain every attestation field for the ten selected source entries, including empty labels, raw flags, fractions and source editorial groups. Stable attestation IDs are snapshot-qualified exact JSON pointers. Edition line alignment and physical glyph coordinates remain unknown. This is a complete selected-source encoding export, not a full multi-edition critical transcription or an expert reading.

Both exports retain SigLA CC BY-NC-SA 4.0 and attribution to Ester Salgarella and Simon Castellan via Ryan Pavlicek/pyaegean. The remainder of the 802-entry source snapshot is not bundled by this pilot.

## Quantity components and metadata reconciliation

[Quantity component ledger](../research/critical-pilot-quantity-components.csv) preserves 41 positioned amount observations on six entries. `complete_printed_integer_json` is null whenever a symbolic component, marked loss or edition-commentary uncertainty is present. A complete printed integer is an edition fact, never a certified complete physical amount. No fractions are assigned rational values and no amounts are summed. Row numbers are edition grouping locators, not quantities or source word IDs. The seven earlier quantity facts for HT 17 and ARKH 2 are re-expressed in this ledger, not counted as independent new evidence.

[Metadata comparison](../research/critical-pilot-metadata-comparison.csv) keeps bracketed dimensions and fragment expressions. HT 49a has a source scalar 9.2 beside an edition fragment expression [3,00]+[6,20]; the expression is deliberately not normalized to a restored measurement. MA 10b is face b of the edition heading MA 10, whose caption describes a four-faced bar with inventory label A. Nik. M. 7336 and bracketed parent-object dimension [8,50]. This is an edition face relationship, not a certified museum identity.

Every entry has an explicit quantity-collation status. Absence of normalized amount transcription on a consulted presentation does not establish absence of physical numerals. Arabic amounts from neighboring KH 75/76 and HT 18 panels are excluded.
