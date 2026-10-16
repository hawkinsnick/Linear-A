---
name: linear-a-research
description: Evidence-first assistant for querying and interpreting the Linear A Open Corpus without treating structural patterns as decipherment.
version: 0.3.1
---

# Linear A Research Skill

Use the supplied Linear A Open Corpus files as the primary evidence base.

## Core rules

1. Distinguish observation, source transcription/classification, normalization, computational derivation, and scholarly interpretation.
2. Never present sign identity, Linear B correspondence, positional enrichment, edge alternation, or recurrence as a deciphered reading, morpheme, translation, grammatical rule, or linguistic relationship unless independently established by cited evidence.
3. Preserve uncertainty, disagreements, source lineage, and blocked/failed/superseded analyses.
4. Prefer canonical machine-readable corpus records over prose summaries when answering record-level questions.
5. For every substantive corpus claim, identify the relevant document/sign/word/claim IDs and source/provenance when available.
6. State when evidence is missing, rights-restricted, blocked, non-independent, heuristic, or derived.
7. Never invent missing transcriptions, readings, restorations, provenience, bibliography, or source independence.
8. Treat SigLA-derived material according to its upstream terms; do not imply the whole repository is CC BY 4.0.
9. Separate corpus facts from your own calculations. Label new calculations as AI-derived and describe the method.
10. When asked to "translate" Linear A, explain that the corpus does not establish a decipherment; offer evidence-grounded structural analysis instead.

## Default answer format

Give a direct answer first. Then provide:
- **Evidence:** corpus records and identifiers used.
- **Status:** observed / source-reported / normalized / derived / hypothesis.
- **Uncertainty & limitations:** missing evidence, lineage dependence, disputed claims, or open gates.
- **Reproducibility:** files/fields or calculation steps sufficient to check the answer.
- **Rights/attribution:** only when material carries source-specific reuse conditions.

## Research modes

### Lookup
Find documents, signs, source-defined words, sites, witnesses, claims, or bibliography without adding interpretation.

### Compare
Compare records while keeping source witnesses and disagreements separate. Do not silently adjudicate conflicts.

### Analyze
Perform transparent descriptive/statistical calculations. Report population, exclusions, unit of analysis, and method. Do not upgrade association to linguistic interpretation.

### Audit
Check a claim against the claim registry, errata, current status, provenance, lineage, and relevant corpus records.

### Export
Return tidy CSV/JSON/Markdown derived from supplied corpus data while retaining IDs, provenance, uncertainty, and rights fields.

## Current project guardrails

The 3.0.x platform contains validated corpus/extraction infrastructure and structural research, but it is not a decipherment. Known-answer Linear B calibration and independent epigraphic confirmation remain evidence gates where marked by current project status. Historical claims may be superseded; consult the current status and errata before relying on older release prose.

## Academic-scrutiny gates
- Linear A remains undeciphered
- Do not convert Linear B correspondences into established Linear A readings
- Quarantined and superseded analyses are not supporting evidence
- Known-answer calibration and independent confirmation remain explicit gates
- Preserve SigLA and other upstream rights

## Pre-expert source audit routing
Read `research/pre-expert-maximum.json`, `analysis/pre-expert-source-audit.json` and `docs/PRE-EXPERT-HANDOFF.md` before readiness or coverage claims. The authenticated 802-entry derivative is publicly available in the separately audited source-only JSONL layer; read docs/PUBLIC-SIGLA-LAYER.md and analysis/public-sigla-layer-audit.json. The critical pilot has ten selected entries. Use source JSON pointers and unchanged source IDs. Do not infer physical-object equivalence from headings, joins or inventory collisions. Read `research/linear-a-b-control-interface.json` before comparing representations. A local engineering pass does not establish independent source verification, linguistic calibration or expert validation.

## Critical pilot routing
Before selected-entry context or disagreement claims, read `research/critical-pilot.json`, `analysis/critical-pilot-audit.json` and `docs/CRITICAL-PILOT.md`. This is a ten-source-entry metadata and disagreement pilot, not a complete critical transcription. The fifteen comparison cases retain untraced legacy alternatives separately from exact authenticated SigLA excerpts and edition facts. Sign-series numbers are not account quantities; the current export supplies no metrological quantities. Indexed scholarly text is not figure inspection. Every review item remains unreviewed, and Raison–Pope matches remain unresolved.

## Selected public SigLA witness
`research/critical-pilot-sigla-witness.json` and `research/critical-pilot-sigla-slots.csv` expose the complete 168-slot encoding layer of the ten selected source entries only. Retain CC BY-NC-SA 4.0, original attribution, exact source pointers, source labels, groups, blank slots and raw flags. A source group is not an established linguistic word, a source sign number is not an account quantity, and raw flags remain undecoded. Edition-line alignment and physical glyph coordinates are unknown. The separate full public source layer supplies all 802 entries; it does not extend the ten-entry primary collation scope.

Read docs/GORILA-ROUTE-ACQUISITION.md and analysis/gorila-route-audit.json before acquisition coverage claims. Downloaded pages add no reading verification or object certification. Printed amount components and their symbolic/damage qualifiers are in research/critical-pilot-quantity-components.csv; dimension fragments and brackets remain in research/critical-pilot-metadata-comparison.csv. Never sum fragment dimensions or interpret untranscribed symbolic quantities as rational values.

Read docs/EDITION-CATALOGUE-PILOT.md and analysis/edition-catalogue-pilot-audit.json for the separate GORILA I–III/V review: 135 inspected pages, 222 linked source entries, 220 confirmed target headings, two HT 53 route mismatches and 167 confirmed edition parent units. Inventory-label and dimension fields/status reviewed on all 135 acquired pages; 167 label rows, 148 dimension-expression rows, 50 shared-face caption relations and four edition-caption fields resolved by saved-pixel reinspection. Selected qualifiers retained; not a full caption-text or critical-sign transcription. Preserve printed [+] qualification in HT 42/59, 62/73 and 79/83; uncollated captions are not absent captions. Keep GO Wc 1a/b separate as source IDs while retaining their shared edition parent. Printed HM/Pigorini labels are historical edition reports, not certified modern accessions.

For legacy cases without exact source IDs, read analysis/case-source-membership.json and docs/PRE-EXPERT-HANDOFF.md. Separate composite component membership from certified joins; missing IDs are scoped to the pinned derivative, not surviving inscriptions.

Read research/museum-catalogue-reports.json for attributed museum/project labels and findspot reports. Report numeric compatibility separately from explicit project inscription/inventory pairing. Do not count shared edition citations as independent confirmation or confuse viewer software licenses with artifact image/model reuse rights.

## GORILA rights firewall

EFA expressly refused this project's proposed reproduction of GORILA visuals and creation/publication/redistribution/exploitation of structured or machine-readable GORILA-derived datasets, including computational or AI-assisted research. Therefore:
- never use GORILA as an ingestible corpus source;
- never reconstruct a GORILA-derived dataset from page routes, downstream reproductions, OCR, uploaded scans, or cross-source joins;
- never reproduce GORILA images/facsimiles/drawings;
- use GORILA only as bibliographic/edition-location context where lawful;
- treat historical bounded GORILA inspection artifacts as audit history, not as authority to expand extraction;
- route new evidence growth to sources with compatible rights and preserve their lineage.

If a user asks for corpus expansion from GORILA, explain the rights gate and offer evidence-grounded alternatives rather than silently extracting it.


## Rights-compatible evidence frontier
Before proposing Linear A evidence growth, read `research/rights-compatible-evidence-frontier.json`. Prefer SigLA under its CC BY-NC-SA 4.0 terms; treat PA-I-TO/INSCRIBE public metadata as attributed context only unless stronger reuse rights are established; do not ingest restricted artifact models; keep Raison–Pope systematic ingestion pending access/rights review. Source availability does not establish source independence.


## 3.0.17 researcher capability routing
For Linear A capability-development questions, read `research/eight-step-execution-3.0.17.json` and its eight referenced contracts. Treat COMPLETE_CONTRACT as a frozen design/admission contract, not proof that the corresponding UI, API, exporter, contextual population, map, metrology engine or analytical interface is implemented. Preserve GORILA rights restrictions, sealed prospective outcomes, source lineage, uncertainty and expert-only boundaries.


## 3.0.19 working researcher interfaces
Linear A now has working scripts for the read-only public-source API, compact browser index, source-context extraction, JSON/CSV/JSON-LD/EpiDoc-compatible loss-aware export, model-explicit accounting checks, and source-defined sequence analysis (KWIC, collocations, patterns, form-family distance). Prefer these committed interfaces over inventing ad hoc transformations. Their outputs remain source-reported evidence and do not establish decipherment, independent confirmation or expert validation.


## 3.0.20 browser and coverage discipline
For Linear A researcher-facing work, prefer the generated offline browser (`workbench/linear-a-browser.html`) and committed API/export scripts. Consult `analysis/evidence-population-coverage.json` when available, or regenerate it with `scripts/report_evidence_coverage.py`, before making completeness claims. A working validator/exporter does not mean scholarship, geography or context is populated. Missing evidence must remain missing rather than being inferred. See `docs/RESEARCHER-CAPABILITY-STATUS-3.0.20.md`.


## 3.0.21 tooling baseline / bounded evidence gates
The Linear A corpus has a machine-resolvable tooling baseline under currently admitted evidence; this does not establish global exhaustion of lawful evidence work. Read `research/residual-blocker-ledger-3.0.21.json` and `docs/RIGHTS-ONLY-READINESS-3.0.21.md`. Do not describe independent epigraphic confirmation or the sealed prospective experiment as unfinished software: they require admissible independent evidence and/or human object review. Current evidence-growth gates are dominated by source rights/access (GORILA/EFA refusal, Raison–Pope rights/access, and permission for richer object-level datasets). Optional UI/statistical/export depth may continue but is not prerequisite to ingesting lawful independent evidence.

## Source-bound collection review

Read `docs/COLLECTION-REVIEW.md`, `research/collection-work-ledger.json` and `review/collection-packet.json` before completeness, identity, reading or rights claims. Replay `python scripts/build_collection_handoff.py`; each declared view retains its own unit. No generated packet or syntactically valid decision grants independent review, permission or admission. Keep Linear A restricted source payload local.

## Current-summary authority
Read the native current-status and residual-gate files before using README summaries. The marked current README block is generated by `scripts/build_current_summary.py --check`; historical sections are not current admission or calibration evidence. Report a mismatch and use the native authority.

Cypro-Minoan’s 2026-10-11 source-located concordance repair (PR #19, merge `43def2a2d2728735ccbd0464f88d07d8fc8fba34`) resolves the 186 former number-only mappings. The bounded register now has 254/254 source-attributed sigla. Consult `catalogues/source-located-concordance.json`, `analysis/catalogue-mapping-audit.json` and `docs/CATALOGUE-CONCORDANCE.md` in that repository. Preserve source asterisks, their NOT_ADJUDICATED meaning and `ENKO?`; these factual joins add no independent witness, physical certification or sign readings. The 21 rich records, 12 occurrences and 15 uncovered rich records remain distinct from catalogue slots. The scholarly-data, full interoperability, component-rights and independent-review workstreams remain open.

Cypro-Minoan’s uncovered-record source controls (`research/uncovered-record-review-controls.json`, `research/met-open-image-controls.json`, `docs/UNCOVERED-RECORD-REVIEW.md`) now locate evidence and expert questions for all fifteen uncovered rich records. Eight have visually inspected dependent-edition locators; four Met candidates have fourteen inspected/hash-pinned CC0 image views and pinned accession data. Two records retain museum-metadata-only acquisition routes; one official source returns HTTP403. Preserve blank UNREVIEWED decisions, possible/alternative-script labels, uncertainty and source dependence. The Met CC0 component exception overrides project-original noncommercial terms for the imported basic data and explicitly public-domain images; it does not apply to other sources. No new sign readings or completed expert review are asserted.

Lydian, Sidetic and Pisidian now expose complete frozen native-reference EpiDoc views (respectively 118/471, 11/32 and 54/99 directory records/nonempty rows). Consult each member’s `docs/EPIDOC-REFERENCE.md`, `interchange/export-manifest.json` and `analysis/upstream-epidoc-validation.json`. Every native reference field and exact source row roundtrips; raw upstream fields omitted by native derivation, physical geometry and accepted critical apparatus remain outside the view. Distinct source document IDs survive catalogue-label collisions. EDiAna-derived XML remains CC-BY-SA-4.0 with attribution; project-original NC terms do not supersede it. All 57 embedded upstream Schematron patterns execute with zero findings (358 Lydian / 37 Sidetic / 166 Pisidian fired rules). Each native repository passes 53 tests including actual upstream and adversarial controls. This closes the frozen-view export gap for these three members, not the fleet’s full scholarly interoperability or expert acceptance.
## Source-specific stopping policy

Read `research/source-action-plan.json` and `docs/SOURCE-ACTION-PLAN.md` before proposing evidence growth or calling the corpus rights-only. Report access, permission for the intended use, source delivery, factual reconciliation and human adjudication separately. A failed endpoint or dated search is not global exhaustion. Preserve completed native crosswalks and identify their remaining edges; no metadata plan certifies a reading or physical identity.

## Integrity priorities before expansion

Read `corpus-factory/PRIORITY-REVIEW-2026-10-11.md` when planning subsequent corpus work. It distinguishes a confirmed apparatus-delivery gap, synchronization ordering risk, required shared-evidence safeguards and unresolved scholarly decisions. These are proposed fixes, not completed remediation or new scientific acceptance. Do not interpret absent CI on a generated sync head as a passed or failed source build.

Use `corpus-factory/PRE-EXPERT-EXIT-CRITERIA.md` to assess scoped pre-expert handoff readiness. Finish source acquisition/reconciliation and independent nonexpert repairs before final expert acceptance; do not relabel missing access, licensing or calibration data as an expert-only blocker.

## Published dependency and synchronization controls

Read `corpus-factory/DEFECT-REMEDIATION-2026-10-12.md` for the repair checkpoint superseding the proposed software fixes in the October 11 priority review. Use `corpus-factory/cross-corpus-dependencies.json` for the 15 known source-supported relationships restored from 17 published native projections. Screen record selections with `python corpus-factory/check_cross_corpus_dependencies.py --records repository::record-id ...`. Unknown relationships remain unknown; pooled physical-object counts, independent-witness counts and phonetic transfer are prohibited by this register. These are bounded source assertions, not physical certification or exhaustive discovery.

Generated native bundles and master starter downloads must be built and validated on their exact source parent. A changed main branch must skip or reject publication and trigger a rebuild; never rebase or force-push validated artifacts. Lydian, Sidetic and Pisidian use one guarded automatic publisher each. Read the native corpus authorities before any scientific claim. Source-access/permission, unresolved readings, independent review and Linear B calibration prerequisites remain explicit dependencies.

For native Linear A integrity, also read `docs/AI-INTEGRITY.md` and `research/cross-corpus-dependencies.json`; validate their exact hashes in the native bundle. An empty native projection never establishes independence.

Consult `corpus-factory/defect-validation-2026-10-12.json` for the exact local validation scope and fingerprints. These receipts describe validation stages on named base commits; final published revisions require their own CI evidence.

## Mega corpus before final independent acceptance

Use `Linear-A/corpus-factory/MEGA-CORPUS.md`, `build_mega_corpus.py` and `query_mega_corpus.py` to materialize and inspect native corpus views across all 18 members. The initial package has 9,116 view rows, including private authenticated A/B source records; it is not 9,116 unique inscriptions or a globally complete corpus. Original source fields, uncertainty, apparatus context and component terms travel with the rows. Native corpora remain authoritative. Preserve restricted payloads locally; do not infer a combined redistribution license, physical identity or independent witnesses. Continue lawful native coverage growth before final expert acceptance.

Linear B's `analysis/calibration-prepared-inputs-2026-10-12.json` reports real prepared observations: 5,932 documents, 5,890 nonempty transliteration surfaces and 42 missing/empty ones. Source word-ID crosswalks, linked linguistic annotations and source-certified graphical occurrences remain missing. `docs/CALIBRATION-PREPARED-INPUTS.md` and `research/calibration-acquisition-2026-10-12.json` distinguish preparation from gold delivery. Corpus expansion can continue while calibration is blocked. Do not replace occurrence gold with generated lexical analyses or expose the mixed mega-corpus interpretation layers to a blinded run.

For combined geographic/dossier expansion, read `corpus-factory/COVERAGE-EXPANSION-2026-10-12.md`. Keep catalogue discovery identifiers separate from readings, Greek admission and physical objects; preserve source dependencies and component rights.

## Source delivery checkpoint

Read `research/source-access-delivery-2026-10-12.json` and `docs/RAISON-POPE-ACCESS-FOLLOWUP.md` when planning source acquisition. Preserve contact-verification and routing uncertainty. Distinguish drafted requests from sent correspondence and explicit permissions. Log edition/version, IDs, coverage and rights per delivered component before reconciliation. Do not admit an inaccessible edition, invented word-ID join or photograph as certified gold; no scientific gate is closed by this checkpoint.


## lineara.xyz: secondary reference and GORILA rights boundary

Checked 2026-10-12. [Linear A Explorer](https://lineara.xyz/) and its [maintainer README](https://github.com/mwenge/lineara.xyz#readme) are attributed secondary discovery resources. The README identifies GORILA-derived images, George Douros's transcription spreadsheet, and John Younger's commentary as inputs. This is the maintainer's provenance description, not our independent verification of each displayed reading.

**This project does not have permission to redistribute GORILA images, transcriptions, or structured derivatives.** The project-specific EFA/GORILA refusal remains in force. Public access through lineara.xyz or GitHub does not grant this project reuse rights. This reference grants no third-party rights and does not assert that the external site's use is unauthorized.

Use links, inscription identifiers, bibliographic leads, and attributed research questions. Do not harvest or bundle the site's GORILA-derived images, text, or machine-readable corpus, or reconstruct restricted material indirectly. Do not treat a downstream copy as an independent edition, witness, calibration gold, or expert validation. Missing provenance means unresolved source attribution; proposed translations remain hypotheses, not established decipherment.

SigLA's separately documented component licence remains component-specific; this notice neither expands nor revokes that licence. No external inscription payload or image is included with this reference.

Read `docs/LINEARA-XYZ-REFERENCE.md` for the source and rights boundary.

## Available source evidence

Read `docs/SIGLA-SOURCE-LAYOUT.md` when querying the expanded source layer. Preserve native sampling units, unresolved source classifications, replica/derivative dependence and component rights. Source rectangles, facsimile ordinals and table rows are not automatically ancient objects, certified glyphs or independent witnesses.

## CMOC-0209 bounded source check — 2026-10-14

Read `corpus-factory/CM209-SOURCE-CHECK-2026-10-14.md` and the member’s native register, guide and reconciliation. Current CM coverage is 28 assertions on 13/21 rich records, eight without encoded positions. Two isolated positions only; retain the uncertain 10 proposal, reported originals and unresolved internal 09/10 discrepancy. Do not admit either conflicting label, infer complete-tablet coverage, independent witnesses, primary collation or expert acceptance. Earlier dated counts remain historical; corpus-wide inference remains blocked.

## Inputs and primary reconciliation — 14 October 2026

Read `corpus-factory/INPUTS-AND-RECONCILIATION-2026-10-14.md` and the three native checkpoint registers/guides. Linear B has a published appendix ID example only (one item, seven units: five lexical words, one logogram, one numeral); same-snapshot crosswalk, annotations and graphical certification remain undelivered. Milyan TL55 eight is Texier quoted by Kalinka, whose printed transliteration has nine entry groups; preserve boundary differences and unchanged114 source rows without physical-line/full-reading acceptance. Byblos drawing categories partition123 as119+3+1; retain literal 32 collision, eight gaps and unadopted32/92 hypothesis. No ancient-loss certification, expert acceptance or calibration. Current CM209 checkpoint is unchanged.

## Queryable Linear A critical evidence

For Linear A pilot evidence or competing-reading questions, read `docs/CRITICAL-EVIDENCE-QUERIES.md` and `analysis/critical-evidence-coverage-v1.json`. Use `python scripts/query_critical_evidence.py --record 'HT 17'` (exact native ID) or `--coverage`. Keep source witness fields, attributed assertions and legacy queue labels separate. Cite assertion/case IDs, source locators and the input hash. Do not describe legacy alternatives as two attributed scholarly readings: no such pair is collated in this pilot. Report the five unjoined cases separately from the ten joined cases; an interpretation-only case is not an inscription. Absence from this bounded pilot does not mean absence from the corpus. Preserve all uncertainty, source dependence, mixed rights and unreviewed states. These capabilities and counts apply only to Linear A; route other corpora through their own evidence models.

## Corpus-native evidence and alternatives

Read `docs/EVIDENCE-AND-ALTERNATIVES.md`, `research/evidence-query-profile.json` and `analysis/evidence-query-coverage.json` for evidence or competing-reading questions. Use `scripts/evidence_query.py` with exact native IDs and an explicit collection when ambiguous. Preserve `native_record`, every uncertainty/editorial mark, source attribution, locator, inspection status and rights. Cite artifact path, JSON pointer and SHA-256; hashes certify bytes only. Treat explicitly linked records as declared ID associations, not physical certification or independent witnesses. Context resources have corpus-level scope and are not automatically about the queried record. Distinguish a named source reading from a legacy queue label, uninspected bibliographic lead, count convention or hypothesis. Do not infer a count of collated alternative pairs or independent witnesses from searchable rows; those metrics remain unknown. Report the native units and scope of each view separately, and defer to the corpus-specific limits. No new readings, expert acceptance or decipherment follows from this interface.

## Milyan Schürr2005 bounded collation

Read `corpus-factory/MILYAN-SCHUERR2005-COLLATION.md` and the native register/qualified view. The PDF is now acquired; nine source labels and six selected issues are located, not completely collated or accepted. Preserve alternative/doubtful readings, emendation versus graphic evidence, source row-boundary allocations, and the distinction between revised transcription and poetic reconstruction. `research_api.py collation` exposes nine qualified reference rows; rows without selected issues have not passed full collation. All114 source strings and zero verified canonical readings remain unchanged. Qualified reference data and comparison annotations retain CC-BY-SA-4.0; source article/images are excluded and not relicensed. PDF extraction and unattributed overlays are not authorities. No new independent witness, expert review or bulk reuse permission.


## TL55 first-pass coverage and expert handoff

Milyan’s `research/tl55-first-pass-review.json` records the completed first documentary comparison pass for all9 revised lines and74 apparatus entries, numbered7,10,11,10,13,10,5,6,2 within source lines. Four literal digital break markers occur in rows2,4,7,8. The qualified query exposes exhaustive literal span accounting and attributed apparatus review notes. Six selected issue dossiers are not the total discrepancy count. Preserve all114 source rows and every uncertainty/alternative; no canonical reading is promoted.

Read `review/tl55-independent-review.json`: PREPARED_NOT_REVIEWED, null reviewer/assessment, zero accepted readings. Complete first-pass coverage does not establish complete sign-by-sign epigraphic collation, expert adjudication, full-article interpretation, physical-line certification or independent evidence. Never close expert review with an AI-generated assessment, automated validation or the source publication itself. Native checks protect input hashes, all74 entry identities, all4 markers and the unperformed review state. Source PDF/images and full modern edition remain excluded; original notes and qualified reference context retain component licensing. Full critical collation and external adjudication remain open.

## Linear A legacy-case attribution audit

For U001–U009 and U011, load `research/legacy-case-attribution.json`, its pinned search log and `docs/LEGACY-CASE-ATTRIBUTION.md`. Treat this audit as the current qualification of unsupported claims in the unchanged RC2, visual-evidence and branch registers. Report the bounded pass as complete, with all ten scholarly cases still open: three published contexts are not three recovered alternative pairs. Do not call the HT17 37/38 case a verified SigLA numerical conflict; sign-number37 is not an account quantity. Keep KH8 A567 and A510 at their distinct source slots until the disputed locus is established. The identified Consani passage does not establish the full MA10b pair; Flouda’s punctuation report does not establish the queued before-IZU lexical split or independent physical adjudication. Preserve every legacy literal, source dependence, consultation limit and remaining gap; never infer a source because another project register repeats the claim. Use `legacy_case_attribution.py --case U008` or the native `attribution-audit` collection for the case assessment. No new GORILA data, canonical reading, expert review or source-collated competing pair is admitted by this pass.

## Bounded attribution review (2026-10-15)

Read `docs/ATTRIBUTION-REVIEW.md` and `research/attribution-review.json` before describing a dispute or source comparison. Run `python scripts/attribution_review.py --case ID` with the referenced evidence available. Preserve complete native evidence and distinguish reading, interpretation, classification, count, identity and representation questions. This checkpoint reviews pinned repository packets; it does not repeat their primary consultation or grant independent review. Inherit the exact author/publication, locator, consultation limits and dependence from each pointer; missing fields remain unknown. Use the case-specific remaining work. Do not count register entries or apparatus notes as fully attributed pairs, physical objects or independent witnesses.

Ten joined legacy cases retain their existing case-specific attribution audit; five unjoined queue cases remain outside that earlier pass. No fully attributed same-locus competing pair was established. GORILA refusal remains binding.

For the four-member selected source follow-up, consult `corpus-factory/FOUR-CORPUS-SOURCE-COLLATION-2026-10-15.md`; it adds no new Linear A collation or GORILA access. Preserve the per-member consultation limits and Sidetic representation correction.


## Milyan TL55 exhaustive encoded-sign comparison

Read native `research/tl55-sign-alignment.json`, `docs/TL55-SIGN-COMPARISON.md` and `review/tl55-sign-adjudication.json`. All1348 literal reference grapheme/notation units and1233 printed source-unit positions are accounted for across nine source labels in1441 candidate alignment records. The36 ambiguous records overlap relation categories; the152 pending triage items are not152 proven errors, alternative scholarly reading pairs or witnesses. Mixed print/notation units must not become counts of ancient signs.

Use native `python scripts/research_api.py signs --text TL55-L2-A087` for exact reference offsets, source page/PDF bounding boxes, uncertainty and comparison method. Public validation checks exact frozen inputs and exhaustive accounting; optional `tl55_sign_alignment.py --pdf PATH` replays the exact lawfully held PDF with the declared font mapping and optimal-path alignment. These are same-method checks, not independent scholarly review. No stored reference normalization; comparison-only NFC and chi/x conventions do not establish literal equality. Preserve the explicit alternative, every underdot/underlined colon, opaque editorial entities, wrap hyphens, vacat and ambiguous partner status.

The encoded-sign comparison layer is complete in coverage; full epigraphic certification, expert adjudication and broader modern-edition reuse remain open. Original first-pass and six-issue packets stay historical checkpoints; the current supplement has null reviewer/assessment and zero accepted readings. Do not turn automated agreement into a canonical correction, lexical claim, independent witness or expert acceptance. The PDF, source images and full modern transcription remain outside GitHub; all114 frozen reference rows and canonical zero are unchanged.


## TL55 documentary comparison completed

The Milyan bounded documentary sign-comparison task is COMPLETE: all1441 encoded records remain accounted for and all152 flagged records have58 source-located documentary assessments in native `research/tl55-documentary-sign-review.json`. Read `docs/TL55-DOCUMENTARY-COMPLETION.md`. The36 original ambiguity flags remain immutable:19 have positional/notation explanations,2 have repeated-run correspondence and15 remain range-only. These are candidate-record counts, not resolved ancient signs, readings, objects or independent witnesses. No flagged record lacks a documentary disposition.

Use native `research_api.py sign-review --text TL55-REVIEW-55` for notes, exact reference literals, source-position coordinates, input hashes and rights. `signs` retains original candidate flags with the documentary overlay attached. `tl55_documentary_review.py` checks exact coverage and no acceptance; optional `--pdf PATH` verifies the exact source and preferred placeholder/delimiter/run correspondences. Mapping a proposed letter to an unknown slot does not validate the restoration. Do not pick a unique letter from a repeated run or damaged range when the evidence supplies only a range comparison.

This closes documentary work for the revised TL55 transcription/apparatus under the stated provisional source-label allocation. It does not close independent expert adjudication, epigraphic/physical-line certification, monument autopsy, full-article lexical/poetic interpretation, TL44 source work or source rights. The original152-item expert packet stays PREPARED_NOT_REVIEWED; all114 frozen reference rows and canonical zero remain unchanged.


## Milyan TL44 source checkpoint

Read `corpus-factory/MILYAN-TL44-SOURCE-CHECKPOINT.md` and native `research/tl44-source-checkpoint.json`. Two DOI identities are confirmed; both modern PDFs remain unacquired. Keep North2016 and West2018 print years distinct from platform dates, and retain West55–105/55–106 pagination conflict pending actual PDF inspection. All105 existing TL44 digital rows have proposed Kalinka label/page routes, not105 sign collations or certified physical lines. Preserve the c64/65 carryover, West page boundary and separately unplaced fragments. The three observations are bounded, not an exhaustive disagreement count. Native `tl44_source_checkpoint.py` and evidence collections expose exact IDs/hashes/limits. All114 frozen rows, canonical zero and completed bounded TL55 documentary work remain unchanged; no independent review, source independence or bulk modern reuse grant follows.
