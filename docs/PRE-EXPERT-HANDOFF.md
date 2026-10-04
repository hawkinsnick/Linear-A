# Pre-expert validation handoff — Linear-A

This package records a reproducible engineering audit of the exact supplied derivative snapshot. It is not expert validation, independent source confirmation, or a claim of complete surviving inscription coverage. Current disposition: **PRE_EXPERT_HANDOFF_SOURCE_DEPENDENCIES_REMAIN**. Consult `research/pre-expert-maximum.json` for individual unfinished gates.

## Reproduce

From the repository root, supply your authorized local sigla-corpus.json snapshot:

```sh
python scripts/build_pre_expert_audit.py /path/to/sigla-corpus.json
python scripts/validate_pre_expert_audit.py
python scripts/test_pre_expert_audit.py
```

The importer refuses bytes that differ from the pinned checksum. Outputs under `data/generated/pre-expert/` are deliberately ignored by git and retain CC BY-NC-SA 4.0 source provenance. `records.json` preserves stable source IDs, source fields and exact JSON pointers. The public `analysis/pre-expert-source-audit.json` contains counts, missingness and derivative hashes. These outputs are deterministic and do not read prospective cohorts, predictions, experiment outcomes or gold.

## Reviewer workflow

1. Reproduce the audit and inspect the source-specific representation boundaries.
2. Review local record/source pointers and the canonical source itself for any selected claim.
3. Keep editorial disagreements, source dependencies and missing fields visible.
4. Use `research/linear-a-b-control-interface.json` before cross-script analysis.
5. Record an expert decision as a separate attributed assertion; never overwrite a source witness silently.

## Rights and scope

Repository-original tooling follows the repository software terms. SigLA/DAMOS fields and local derivatives retain upstream rights and attribution. The full authenticated derivative now has a licensed public source-only JSONL layer; the ten-entry witness remains a separately scoped critical pilot. No primary-edition image is republished. Historical statistical artifacts and their pinned inputs are untouched. Engineering reproducibility does not authorize scoring a sealed experiment.

## Linear A boundaries

802 source document entries; 5,144 attestations; 1,401 source word groups; 376 source sign entries. Source display labels are not deciphered phonetic values. Four occurrence sign keys are absent from the supplied sign inventory; 388 occurrences have no series/number key. Preserve them as source gaps. Conventional metrological quantities are not supplied by SigLA. The 15 disagreement cases remain separately tracked; no new linguistic or metrological adjudication is claimed. `unresolved-source-locators.json` is local. The root CSV scaffolds do not become a public source export.

## Bounded primary collation

`analysis/pre-expert-primary-collation.json` records identified primary pages inspected for 13 of the 15 existing case entries. GORILA I page 35 explicitly reports 38 for HT 17; this is an edition-level check, not an object-level ruling. The other inspected cases retain competing labels and segmentation. SY Zb 7 still lacks a verified primary image locator. Fraction K remains a model/interpretation boundary. All physical readings remain unadjudicated by experts. No images are republished.

## Validation performed

Exact source checksums matched. Record exports and aggregate audits reproduced byte-for-byte on repeat. Current-state, source accounting, AI-bundle and existing Python regression checks passed. Linear B's existing real-source mapping audit and invented-field corruption checks also passed. CI now replays the source audit from the pinned public release asset. Remote CI results are tracked separately from this local validation.

## Whole-snapshot edition accounting

Read [the Step 1 concordance guide](EDITION-CONCORDANCE.md) before coverage or edition-equivalence claims. All 802 source entries have edition-specific statuses, including 755 attributed GORILA page links, 24 later-publication links and 23 unusable references. Existing primary inspection joins ten case entries to eight source records; three inspected case identities remain unjoined. Both Raison–Pope editions remain entry-level unresolved. The public concordance contains source-derived identifiers and bibliographic locators under retained CC BY-NC-SA 4.0, not source readings or raw records. This does not alter historical audit denominators or sealed scientific experiments.

## Critical metadata and disagreement checkpoint

Read [the critical pilot dossier](CRITICAL-PILOT.md) for ten exact source entries, 51 source-bound assertions (46 primary edition reports and five attributed scholarly reports), plus 41 editorial amount components on six entries, and fifteen preserved disagreement comparisons. The twenty consulted GORILA page images include nineteen target pages and one blank adjacent-page negative check. This is bounded metadata collation, not a complete critical transcription. No physical join, restoration, inventory certification, independent object confirmation or expert decision has been added.

The comparison layer corrects the **attribution status** of the old HT 17 quantity-37 claim: the authenticated SigLA export does not supply account quantities. A sign-series number 37 identifies TI, not that quantity. The legacy alternative is retained, and the edition-level 38 finding does not adjudicate the physical inscription. The blank 25-item review sheet names the next source checks and requires attributed decisions. Replay commands and the exact access barriers are in the dossier.

## Public selected-source encoding layer

The ten-entry pilot now includes all **168 source attestation slots** (119 source-classified syllables, 23 logograms, 18 blank slots and eight fraction slots) and **41 source editorial groups** in a licensed JSON witness and standalone CSV. Exact snapshot-qualified pointers and original attestation fields are preserved, including uncertain labels and raw flags. These are SigLA source classifications; they do not establish physical sign counts, linguistic values or graphical alignment with edition lines. Both exports retain upstream CC BY-NC-SA 4.0 and attribution. All 802 source entries now have a separate public source-only JSONL export; the original raw snapshot is not bundled. Full multi-edition critical transcription remains open.

## Full public source layer and route accounting

Read [PUBLIC-SIGLA-LAYER.md](PUBLIC-SIGLA-LAYER.md) for direct downloads and byte-exact replay. Read [GORILA-ROUTE-ACQUISITION.md](GORILA-ROUTE-ACQUISITION.md) for 135 acquired page routes, the distinct 222 linked entry count, and the runtime policy interruption. Download availability does not add reading verification.

## GORILA II catalogue-label pilot

The separate [edition-label review](EDITION-CATALOGUE-PILOT.md) covers all 135 acquired pages: 222 linked entries, 220 confirmed target headings and two unresolved HT 53 route mismatches. Its 167 confirmed edition parent units are not certified physical objects. Inventory-label and dimension fields/status reviewed on all 135 acquired pages; 167 label rows, 148 dimension-expression rows, 50 shared-face caption relations and four edition-caption fields resolved by saved-pixel reinspection. Selected qualifiers retained; not a full caption-text or critical-sign transcription. No sign adjudication or modern accession verification is claimed.

## Review cases outside exact source-ID joins

[The reproducible source-membership report](../analysis/case-source-membership.json) distinguishes three different situations. HT Zd 157+156 is a legacy composite case with two separate authenticated source records, HT Zd 157 and HT Zd 156; neither is relabelled as a combined record and their readings are not concatenated. PK Za 8, PR Za 1 and SY Zb 7 have no exact ID in this pinned 802-entry derivative. This is a snapshot coverage boundary, not evidence that these inscriptions are absent from primary editions. Fraction K is an interpretation case rather than a document ID.

The existing primary-page inspection records for PK Za 8 and PR Za 1 remain separately attributable. Their earlier image digests remain recorded, but those image files were not found in the current workspace during this continuation; no new visual inspection or fresh asset verification is claimed for them. The HT Zd composite remains a review question, not a certified object join.

Reproduce with `python scripts/build_case_source_membership.py --check`. This report adds membership accounting without changing the critical pilot's ten-entry denominator or its unreviewed decisions.

## SY Zb 7 retrieval barriers checked 2026-10-04

A search-indexed scholarly candidate is Montecchi's 2024 chapter, “Design and Origins of Linear A Picture-Based Signs”, DOI 10.1093/oso/9780198908746.003.0010. It mentions SY Zb 7, but no primary entry, figure or reading was verified from these retrieval attempts. The [Bologna repository PDF](https://cris.unibo.it/retrieve/ace556f3-9a7d-4db0-8d30-5b37fdd7ab1e/OUP_writing.pdf) timed out through the retrieval tool. The [Florence repository PDF](https://flore.unifi.it/retrieve/81004007-8df7-4755-b33f-86622e603a2d/Ferrara-Montecchi-Val%C3%A9rio_OUP_2024.pdf) returned HTTP 403. The [publisher chapter](https://academic.oup.com/book/58672/chapter/485388397) redirected to a CDN resource inaccessible through that tool. These are route-specific retrieval barriers, not proof of a paywall, legal prohibition or source absence. No download or source-image verification is claimed; the primary-locator gate remains open.

## Museum and digitization-project catalogue reports

[The attributed catalogue comparison](../research/museum-catalogue-reports.json) adds four narrowly scoped candidates. Museo delle Civiltà lists MPE 81951 from Haghia Triada; this is compatible with HT 29's historical Pigorini 81951 caption, but the museum text does not itself identify HT 29. The edition's HM 9 (moulage) remains a cast report. Bologna's INSCRIBE page explicitly pairs HT 114 with inventory 83735 and reports Casa del Lebete, room 9, LM IB, with digitization in November 2020. Its citation to GORILA I pp.186–187 is preserved, so agreement is not counted as independent confirmation.

PA-I-TO's viewer index separately lists HT 29, HT 114 r/v and HT 118. Only the index and rights paragraph were inspected. INSCRIBE and PA-I-TO require prior written permission to reproduce or publish their artifact datasets; no image, mesh, texture or 2D+/3D dataset was acquired or republished. Viewer-software licensing does not grant artifact-data reuse. No sign sequence or proposed interpretation is imported from these pages.

Run `python scripts/check_museum_catalogue_reports.py`. Exact web URLs and field/section locators remain in the comparison; no raw HTML digest or current object-identity certification is invented. All prior expert gates remain open.

The expanded INSCRIBE metadata check explicitly pairs HT 29 with 81951 and preserves its **Villa, room 59?** question mark. HT 118 is paired with 83734 and Casa del Lebete, room 9; its GORILA I pp.200–201 citation remains explicit. KH 8 is paired with inventory 8 and Chania, odos Katre, citing GORILA III pp.32–33. The project's LM I and the pinned SigLA LM IB remain separate reported chronologies. No model measurement, source-independence claim or physical-identity certification follows from these metadata pairs.
