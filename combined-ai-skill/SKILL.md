---
name: combined-corpus-research
description: Vendor-neutral evidence-first orchestration skill across the registered corpus projects.
version: 1.3.0
---

# Combined Corpus Research AI — 1.4

This is an orchestrator over independent corpus projects. It is not a corpus, a decipherment system, or a license umbrella.

## Mandatory routing
1. Identify which registered corpus project(s) can answer the question.
2. Load each project's individual SKILL.md and generated research-bundle index before using its evidence.
3. Treat each corpus's native identifiers, evidence model, uncertainty, exclusions, rights, and scientific gates as authoritative.
4. For a single-corpus question, defer to that corpus skill unless cross-corpus context is necessary.
5. For cross-corpus questions, run each corpus analysis independently first, then compare only fields whose semantics are demonstrably compatible.

## Evidence firewall
Never infer common sign value, language relationship, borrowing, chronology, morphology, decipherment, or independent replication from interoperability, visual similarity, string similarity, positional statistics, shared tooling, or repository membership alone.

A shared upstream source, edition, transcription tradition, code path, derived dataset, or duplicated witness is not independent evidence. State dependencies.

## Comparison gate
Before comparing corpora, report:
- research question;
- corpora included and why;
- unit of comparison in each corpus;
- whether units are semantically comparable;
- representation layer being compared;
- source-independence status;
- uncertainty/exclusion rules;
- rights constraints;
- known blockers.

If comparability is not established, stop at a descriptive side-by-side account and label the inferential comparison BLOCKED.

## Claim discipline
Classify substantive statements as corpus fact, source/editorial assertion, reproducible computation, scholarly interpretation, AI-derived analysis, or unknown/blocked. Never upgrade one class into another silently.

## Citation and reproducibility
Use stable corpus/record/claim identifiers and source locators when available. Name the corpus project and repository artifact supporting material claims. For AI-derived calculations, state inputs, exclusions and method sufficiently to reproduce.

## Rights firewall
Rights remain source- and corpus-specific. Never treat inclusion in this combined skill as permission to redistribute content. Prefer references/locators over reproduction when rights are unclear or restrictive.

## Staleness
Check each participating project's generated source-state. A stale or absent bundle must be disclosed; canonical corpus files take precedence.

## Default answer shape
Answer the research question directly, then provide Evidence by corpus; Comparability; Result/status; Uncertainty and blockers; Reproducibility; Rights/attribution where relevant.

## Translation/decipherment
For undeciphered or poorly understood material, do not manufacture translations or phonetic readings. For deciphered scripts/languages, preserve editorial uncertainty and do not transfer established values to other scripts without explicit evidence.

## Scope
The active project set is defined by registry/corpus-projects.json. New corpus projects join only through explicit registry entries and must provide an individual skill plus the shared research contract.

## Evidence-growth routing
For members with an `evidence_growth_state` in the registry, read the member's current-status and authority-profile artifacts before reporting coverage or readiness. Treat growth targets as plans, not achieved evidence. Never infer increased scientific readiness from repository version, archive size, or source count alone; only canonical admission and verification gates can change claim status.

## Fleet benchmark
Use `references/fleet-benchmark.md` when discussing corpus maturity or evidence acceleration. Linear A is the governance/reproducibility benchmark, not a linguistic donor. Parity means comparable rigor and usability under the evidence actually surviving for each corpus, never equal record counts.

## Corpus Factory benchmark
Before making fleet-wide maturity, coverage, or readiness claims, consult `../corpus-factory/fleet-gap-register.json` and `../corpus-factory/schemas/benchmark-status.schema.json`. Treat each member's `top_gap` as an unresolved research dependency, not a deficit that may be filled by inference. A corpus can satisfy parity with few surviving objects if coverage/accounting, provenance, rights, uncertainty, validation, independence, and AI authority are complete.

## Pre-Expert Maximum routing
When a registered member exposes `pre_expert_maximum_path`, consult that artifact before proposing expert review or describing unfinished work. Complete or explicitly disposition machine/source work first. Treat `human_only_boundary` as decisions that must not be silently resolved by the AI. A PRE_EXPERT_MAXIMUM contract is a work-boundary contract, not a claim that the corpus is scientifically complete or expert validated.

## New comparative members
Anatolian Hieroglyphic is a comparative control, Archanes is an early-Cretan disagreement-aware corpus, and Aegean Anomalous is a neutral quarantine layer. Never use their co-registration to imply common language, sign identity, descent or decipherment.

## Lydian, Sidetic and Pisidian reference routing
Treat these new members as attributed eDiAna digital reference layers until their native gates admit primary-edition/object verification. Count source document IDs separately from response grouping titles and physical objects; labels may collide, and ID zero is valid. Preserve source headings, uncertainty, edition references and response row pointers. Source grammar and language assignments remain source assertions. The source snapshots and derived reference records retain CC BY-SA 4.0; project-original noncommercial terms do not override upstream permissions. Shared eDiAna/edition lineage does not provide independent replication across projects.

For Lydian, Sidetic and Pisidian, consult `analysis/record-admission.json`, `research/admission-policy.json`, `research/edition-dependencies.json` and `research/source-issues.json` before analytical claims. Use `analysis/benchmark-status.json` for scoped coverage and `research/source-frontier.json` for later publications. Bibliography searches are candidates; missing row citations must remain visible. Syntactic uncertainty flags do not adjudicate damaged signs. Snapshot hash binding and regression tests establish engineering integrity, not independent epigraphic verification.

## Collection expert validation handoff
Read `EXPERT-REVIEW.md` when preparing specialist validation. For members exposing `review_manifest_path`, read the current manifest and selected record packets before drafting a request. Bind requests to the evidence fingerprint and record hashes. Cite source inspections separately from independent reviews; disclose missing edition locators and access barriers. Preserve reviewer decisions by dimension. Do not fabricate reviewer identity, treat structural validation as authenticated expertise, or auto-admit evidence. Other members retain their native review protocols; do not assume the new three-member packet format exists fleet-wide.
## Linear A / Linear B pre-expert handoff
Read each member's `analysis/pre-expert-source-audit.json`, `docs/PRE-EXPERT-HANDOFF.md`, and `research/linear-a-b-control-interface.json`. Local materialization is distinct from public record admission. Source-record counts are not physical-object counts; source-defined groups are not adjudicated linguistic words. Open source-collation or aligned-gold gates prevent claims of a completed pre-expert ceiling. Continue machine/source work until the native contract records a supported terminal disposition.

For corpus-development work, apply `references/pre-expert-standing-order.md`.

## Lydian, Sidetic and Pisidian source work

Read each member’s `research/source-worklist.json` before preparing an exhaustive handoff. It accounts for every frozen record and citation while preserving unresolved edition joins. Consult linked source checks for precise locators and attributed competing readings. Inscription numbers may differ between editions; matching numbers alone do not establish identity. Museum inventory references in a publication are dated source assertions until independently reconciled. Acquired PDFs and targeted checks do not establish complete collation, redistribution permission or expert review.

## Linear A GORILA rights firewall

For Linear A, EFA has expressly refused this project's proposed reproduction of GORILA visual material and creation/publication/redistribution/exploitation of structured or machine-readable GORILA-derived datasets, including AI-assisted and non-commercial research outputs. The orchestrator must not route GORILA into ingestion, reconstruction, extraction, or redistribution workflows. It may be cited as bibliographic/edition-location context where lawful. Historical bounded inspection artifacts are audit history only. This member-specific restriction overrides any generic fleet preference for source acquisition.


For Linear A evidence-growth work, also read `../research/rights-compatible-evidence-frontier.json`; it is the member-specific source-admission routing table after the EFA GORILA decision.


## 3.0.17 researcher capability routing
For Linear A capability-development questions, read `research/eight-step-execution-3.0.17.json` and its eight referenced contracts. Treat COMPLETE_CONTRACT as a frozen design/admission contract, not proof that the corresponding UI, API, exporter, contextual population, map, metrology engine or analytical interface is implemented. Preserve GORILA rights restrictions, sealed prospective outcomes, source lineage, uncertainty and expert-only boundaries.


## 3.0.19 working researcher interfaces
Linear A now has working scripts for the read-only public-source API, compact browser index, source-context extraction, JSON/CSV/JSON-LD/EpiDoc-compatible loss-aware export, model-explicit accounting checks, and source-defined sequence analysis (KWIC, collocations, patterns, form-family distance). Prefer these committed interfaces over inventing ad hoc transformations. Their outputs remain source-reported evidence and do not establish decipherment, independent confirmation or expert validation.


## 3.0.20 browser and coverage discipline
For Linear A researcher-facing work, prefer the generated offline browser (`workbench/linear-a-browser.html`) and committed API/export scripts. Consult `analysis/evidence-population-coverage.json` when available, or regenerate it with `scripts/report_evidence_coverage.py`, before making completeness claims. A working validator/exporter does not mean scholarship, geography or context is populated. Missing evidence must remain missing rather than being inferred. See `docs/RESEARCHER-CAPABILITY-STATUS-3.0.20.md`.


## 3.0.21 pre-expert maximum / rights-dominant gate
The Linear A corpus has reached its machine-resolvable pre-expert maximum under currently admitted evidence. Read `research/residual-blocker-ledger-3.0.21.json` and `docs/RIGHTS-ONLY-READINESS-3.0.21.md`. Do not describe independent epigraphic confirmation or the sealed prospective experiment as unfinished software: they require admissible independent evidence and/or human object review. Current evidence-growth gates are dominated by source rights/access (GORILA/EFA refusal, Raison–Pope rights/access, and permission for richer object-level datasets). Optional UI/statistical/export depth may continue but is not prerequisite to ingesting lawful independent evidence.


## Corpus-family browser standard
Corpus-family repositories should expose an offline browser generated from an explicit rights-reviewed allowlist. Standard sister-project paths are `research/browser-sources.json`, `scripts/build_corpus_browser.py`, and generated `workbench/corpus-browser.html`; Linear A may use its richer native `workbench/linear-a-browser.html`. Never recursively sweep data directories into a browser. Treat browser admission as redistribution: verify source/record rights and provenance first. A browser is an access surface, not decipherment or expert validation.


## Collection >9 evidence gate
For collection-strength assessments, treat 9.0 as the current minimum target, but never manufacture a score from repository polish. A member earns >9 only when its lawful evidence depth, coverage accounting, source-lineage independence/reconciliation, object/text identity controls, uncertainty/disagreement handling, rights provenance, reproducible validation and researcher interfaces are all strong relative to the surviving evidence. If evidence growth is constrained by protected critical editions, unpublished fascicles, inaccessible object evidence or expert-only adjudication, report the member as externally gated rather than inflating its score. Current remediation members include Cypriot Syllabic Greek, Sidetic, Lycian/Carian/Milyan and Anatolian Hieroglyphic; consult each native pre-expert/GT9 artifact before rating.


## Collection-wide >9 floor
The corpus fleet uses a >9 scholarly-readiness graduation gate. A member does not graduate by version number, file count, or tooling alone. Assess lawful primary/critical evidence depth, declared coverage versus the scholarly universe, source independence and lineage, object/text identity reconciliation, uncertainty/disagreement controls, reproducibility, rights provenance, and expert-review boundaries. Corpora below the gate remain in remediation until evidence depth supports graduation or a concrete rights/access/expert dependency prevents further lawful machine-resolvable progress. Never inflate a score to hide an external blocker.

## Milyan software admission checkpoint (2026-10-10)
`hawkinsnick/Milyan-Lycian-B` is structurally admitted through the native-schema research-contract adapter. Route Milyan/Lycian B questions to its `ai-skill/SKILL.md`; current evidence is three bibliographic segment records for two monuments, with zero verified transcriptions. Text-level cross-corpus inference remains blocked pending critical edition collation and source-specific rights review. Replay native and master validation before claiming synchronized software admission. Milyan is not synonymous with Lycian A.

Milyan update: member research API now provides bibliographic inventory search, empty line-layer KWIC, coverage and JSON/CSV exports. Its source-reconciliation matrix explicitly blocks all unverified readings; zero KWIC hits cannot establish lexical absence. Follow the individual Milyan skill and bundle index for current evidence state.

## Byblos rights-dominant routing

For Byblos Syllabary evidence-growth or readiness questions, consult the member repository's `analysis/preexpert-residual-ledger.json` and `docs/RIGHTS-DOMINANT-READINESS.md`. Under its currently lawfully admitted evidence, the identified non-rights pre-expert machine/source work has been exhausted. The dominant acquisition dependencies are lawful access to Dunand 1945/1978, authoritative object/accession witnesses, and applicable upstream terms for provider sequence/encoding reuse. Keep the fourteen A-N publication labels distinct from physical-object counts and keep OCBI rendered rows distinct from inscription counts. Independent epigraphic review remains downstream and must not be simulated.


## Eteocretan rights-wall routing

For Eteocretan readiness and evidence-growth work, consult the member repository's `research/pre-expert-maximum.json`, `research/residual-blocker-ledger.json`, and `research/rights-wall-audit-2026-10-06.md`. Guarducci III has a confirmed public digital access route through University of Crete Anemi, but access does not itself authorize redistribution or systematic structured derivative use. Duhoux 1982, complete Dreros primary evidence, authoritative object/accession evidence, and source-specific reuse terms remain evidence-growth gates. Preserve Praisos classification conflicts, Dreros location uncertainty, and Azoria candidate/item denominators; never convert derivative witnesses into independent ancient observations or admit readings merely because a source is downloadable.



### Eteocretan four-front closure
The member repository now also controls Duhoux's 13-text universe as an attributed target denominator, a conservative Praisos/IC publication crosswalk, an Azoria discovery denominator of 17 inscribed sherds with only two individually represented handle candidates, and a Dreros witness genealogy. Do not synthesize the unresolved Azoria items, copy Duhoux's protected critical edition, or count dependent editions/transcriptions as independent witnesses. Further canonical growth requires new lawful source/institutional evidence before human epigraphic adjudication.


## Phrygian maximum pre-expert routing

The Phrygian member's former rights-only assessment has been narrowed. Protected systematic extraction from Brixhe-Lejeune, Obrador-Cursach and uncertain-rights digital editions remains rights-gated, but lawful public record-level identity/object metadata reconciliation remains open. Consult `research/catalogue-denominator-control.json`, `research/subcorpus-source-genealogy.json`, `research/public-object-metadata-lane.json`, and `research/residual-blocker-ledger.json`.

Keep CIPPh/modern catalogue/TITUS/UD/TM denominators distinct; TITUS headings are not unique-inscription counts; Mysian comparison material is not automatically Phrygian evidence; dependent digital corpora do not constitute independent epigraphic witnesses. Canonical readings remain sealed until source-level verification.



### Phrygian public-evidence expansion
The member repository now has a broader monumental Old Phrygian factual-metadata lane and a publisher-hosted Kerkenes K-01 inspection route. Keep catalogue namespaces explicit (notably the W-11 / MPhr-01 collision) and use OIP 135 for attributed factual excavation/catalogue/inventory controls only under its source-specific rights boundary. Downloadable access is not blanket permission to redistribute protected figures, prose or critical text.



### Phrygian Gordion/Kerkenes small-object controls
The member corpus now distinguishes Penn Museum's institutional Gordion discovery categories (11 stone inscriptions; 245 graffiti, primarily on vessels) from TM/TITUS/UD denominators and from the monumental-index layer. It also tracks OIP 148 as a publisher-hosted Kerkenes pot-mark/graffiti context route. Do not turn category counts into exact unique-object totals, classify all marks as Phrygian language, or count repeated publication of the same evidence as independent witnesses.


## Fleet EpiDoc and universal identity standards

Two collection-wide interoperability contracts are normative for new corpus engineering:
- `corpus-factory/schemas/epidoc-interoperability-contract.json`: native records remain authoritative; EpiDoc exports must be loss-aware, rights-aware, mapping-audited and round-trip tested for declared reversible fields.
- `corpus-factory/schemas/universal-identity-graph-contract.json`: external IDs and object/text/edition/place relationships are provenance-bearing assertions, not string joins.

Never infer physical identity from matching catalogue labels, adjacent numbers, inherited digital links, shared coordinates or visual resemblance. Preserve negative/disputed identity edges. EpiDoc encoding establishes interoperability only; it does not establish reading correctness, source independence, decipherment or expert review.



### Interoperability rollout status — 2026-10-06
Linear A: existing TEI exporter audited as PARTIAL_NOT_YET_EPIDOC_CONFORMANT; native JSON payload is preserved but structured EpiDoc mapping/validation/round-trip and rights allowlist gates remain. A rights-aware source identity graph is seeded; GORILA remains historical audit/bibliographic-only under the project-specific refusal.

Linear B: existing source-ID-preserving EpiDoc importer is an engineering strength, but fleet conformance remains open pending a real authenticated annotated source export, mapping/loss reports, export path and round-trip tests. A DĀMOS/source identity graph is seeded without equating source IDs with physical tablets.


Cypro-Minoan: fleet pilot separates physical object, text-bearing surface, inscription/potmark and sign-occurrence assertions. EpiDoc export remains unimplemented; partial occurrence coverage and authority-specific sign labels must remain explicit.

Cretan Hieroglyphic: fleet pilot separates CHIC catalogue identity, INSCRIBE-derived context, critical reading assertions and sign classes. EpiDoc export remains unimplemented; alternative script classification, writing/iconographic uncertainty and zero asserted native phonetic values must survive serialization.

## Eteocypriot, Eteocretan and Phaistos Disc denominator safeguards
For Eteocypriot distinguish digital edition entries, editorial components, archaeological objects and independent witnesses; shared Cypriot Greek source copies are not replication. For Eteocretan distinguish inscriptions, alternative reading versions, source rows and analytically admitted tokens (currently zero in the documented baseline). For Phaistos Disc preserve the historical 241 versus project 242 slot-count disagreement, and never count two faces as two independent objects. Consult each member's current README and `ai-skill/SKILL.md` before reporting these numbers. These documentation safeguards do not themselves update generated source-state fingerprints or establish independent review.

## Native-schema admission adapters
Anatolian Hieroglyphic, Archanes Script, Aegean Anomalous and Milyan use `ai-skill/generated/fleet-contract-index.json` alongside their native bundle. Replay the member validator and master admission validator before claiming synchronized admission. These adapters hash declared native authorities and preserve source-specific rights, exclusions and uncertainty. Admission does not certify readings, object identities, source independence or human expert review. For Phaistos Disc, read the machine-replayed `analysis/acceptance-2.0.json`; receipt or schema validity is not human acceptance.

## Six-workstream P1 reconciliation

Read `docs/P1-RECONCILIATION-2026-10-11.md` and `corpus-factory/p1-evidence-snapshot.json` before fleet-wide closure claims. All eighteen members declare source-bound collection ledgers and review packets in the registry. Replay each native collection builder before using its packet. Respect separate native record units, restricted local derivatives and unresolved primary-source work. Rights authority presence is not permission; an interoperability artifact is not full EpiDoc conformance; a valid decision template is not independent human acceptance. The six recovered workstreams are not six identified GitHub issues. Never invent their ticket numbers or report evidence-dependent gates closed from software checks.

## P1 closure assessment

The declared baseline and eighteen-member common handoff coverage are complete. Scholarly data coverage, full interoperability, documentary rights acceptance and independent review retain their documented open criteria. Cypro-Minoan now has executable expected-hash verification and upstream RNG plus all 57 embedded Schematron patterns for its partial 12-occurrence pilot; read its validation receipt and pins. Do not extrapolate that result to full corpus conformance or human acceptance. Phaistos Disc issue 4 remains the actual open GitHub issue. Report workstream status and live ticket state separately.

### Verified Phrygian catalogue and reference interchange
Phrygian PR 11 (merge `6f0be30df492acdb6b07c05507d9e3f991156314`) closes the factual K-01 catalogue crosswalk and frozen-reference export validation gaps. Read `research/k01-catalogue-concordance.json`, `interchange/export-manifest.json`, `research/interoperability-identity-graph.json` and `analysis/upstream-epidoc-validation.json`. Eight catalogue entries carry fourteen identification labels. The introduction and entry descriptions use incompatible piece counts; unique physical count remains unknown. Catalogue/concordance XI is retained alongside the contents-page IX discrepancy. No certified physical joins or independent review are added.

All 203 frozen UD reference records (1,921 tokens; 162 distinct source TM labels) round-trip every native record field through EpiDoc. Pinned upstream RNG and all 57 embedded Schematron patterns pass with 613 fired rules and zero findings. This closes that finite reference-view validation gate, not full critical-edition coverage. UD-derived XML retains CC-BY-SA-4.0 attribution. OIP 135 factual metadata has a separate source-specific rights boundary; public access and the publisher license do not grant model-training permission. Protected prose, images and critical readings are not incorporated. Scientific data gaps, other component rights and independent acceptance remain open at their documented scopes.

### Milyan reference population and inspected edition controls
Merged Milyan PRs 4 and 5 populate two frozen eDiAna digital catalogue entries and 114 source text rows: TL 44c has 34, TL 44d 71, and TL 55 nine. The byte-pinned raw source and row locators preserve exact strings and original annotations. Explicit reference-layer API queries offer literal KWIC, JSON and CSV. Canonical/provisional queries remain separate and verified canonical readings remain zero. This is the same source lineage as the Lycian-and-Carian cached Milyan partition; never double-count its rows or call these independent witnesses.

Route through `docs/EDIANA-REFERENCE.md`, `research/reference-manifest.json`, `research/ediana-reference-crosswalk.json`, `research/primary-edition-locator-control.json` and `analysis/upstream-epidoc-validation.json`. Reference-derived components retain CC-BY-SA-4.0 with original eDiAna hyperlinks and primary-edition attribution; project-original NC terms do not override them. Exact source text and every derived row field round-trip through EpiDoc. Pinned upstream RNG and all 57 embedded Schematron patterns execute, with 348 fired rules and zero findings. This validates the full declared frozen reference view, not a complete independently collated corpus.

Visual Kalinka 1901 scan inspection establishes precise printed/PDF page locators. Preserve the historical TL55 eight-line description versus nine digital source rows without forcing physical-line joins. Exact historical reading comparison remains open. A broad source bibliography and an exact text-page locator are different claims. Public primary access does not create an independent witness or human acceptance. No claim that the fleet has reached its pre-expert maximum follows from this checkpoint.

## Current member summaries and calibration acquisition
For Linear A, Linear B and Milyan, use the generated marked current README summary together with its native status authorities; distinguish native release versions from later tooling checkpoints. Historical sections do not override current gates. Milyan is structurally admitted and has a populated reference layer, while canonical verified readings remain absent. For Linear B acquisition, require the separate linguistic annotation package linked to document/word-occurrence IDs: the described DĀMOS EpiDoc export omits those analyses. A graphical benchmark remains separately gated. Never infer calibration performance from source acquisition or importer checks.

Cypro-Minoan’s 2026-10-11 source-located concordance repair (PR #19, merge `43def2a2d2728735ccbd0464f88d07d8fc8fba34`) resolves the 186 former number-only mappings. The bounded register now has 254/254 source-attributed sigla. Consult `catalogues/source-located-concordance.json`, `analysis/catalogue-mapping-audit.json` and `docs/CATALOGUE-CONCORDANCE.md` in that repository. Preserve source asterisks, their NOT_ADJUDICATED meaning and `ENKO?`; these factual joins add no independent witness, physical certification or sign readings. At that earlier checkpoint there were 21 rich records, 12 occurrences and 15 uncovered rich records, distinct from catalogue slots. The later source checkpoint below supersedes those occurrence/coverage counts with 16 occurrences on nine records and 12 currently uncovered records. The scholarly-data, full interoperability, component-rights and independent-review workstreams remain open.

Cypro-Minoan’s uncovered-record source controls (`research/uncovered-record-review-controls.json`, `research/met-open-image-controls.json`, `docs/UNCOVERED-RECORD-REVIEW.md`) now locate evidence and expert questions for all fifteen uncovered rich records. Eight have visually inspected dependent-edition locators; four Met candidates have fourteen inspected/hash-pinned CC0 image views and pinned accession data. Two records retain museum-metadata-only acquisition routes; one official source returns HTTP403. Preserve blank UNREVIEWED decisions, possible/alternative-script labels, uncertainty and source dependence. The Met CC0 component exception overrides project-original noncommercial terms for the imported basic data and explicitly public-domain images; it does not apply to other sources. No new sign readings or completed expert review are asserted.

Lydian, Sidetic and Pisidian now expose complete frozen native-reference EpiDoc views (respectively 118/471, 11/32 and 54/99 directory records/nonempty rows). Consult each member’s `docs/EPIDOC-REFERENCE.md`, `interchange/export-manifest.json` and `analysis/upstream-epidoc-validation.json`. Every native reference field and exact source row roundtrips; raw upstream fields omitted by native derivation, physical geometry and accepted critical apparatus remain outside the view. Distinct source document IDs survive catalogue-label collisions. EDiAna-derived XML remains CC-BY-SA-4.0 with attribution; project-original NC terms do not supersede it. All 57 embedded upstream Schematron patterns execute with zero findings (358 Lydian / 37 Sidetic / 166 Pisidian fired rules). Each native repository passes 53 tests including actual upstream and adversarial controls. This closes the frozen-view export gap for these three members, not the fleet’s full scholarly interoperability or expert acceptance.
## Source-specific evidence frontier

For Linear A, Linear B, Phrygian, Eteocretan, Lydian and Sidetic, read each repository’s `research/source-action-plan.json` and `docs/SOURCE-ACTION-PLAN.md` before claiming rights-only readiness. Separate endpoint access, permission for the intended operation, source delivery, factual reconciliation and human adjudication. Dated searches do not prove global exhaustion. Respect existing completed crosswalks and their unresolved edges. Linear B’s `docs/CALIBRATION-INTAKE.md` describes private metadata/digest intake only; it does not establish acquired gold, certification or authority to reveal answers. Other members retain their own native stopping authorities; this checkpoint does not certify the entire fleet.

## Source checkpoint and reevaluation — 2026-10-11

Read `corpus-factory/REEVALUATION-2026-10-11.md`, `corpus-factory/source-checkpoints-2026-10-11.json` and `corpus-factory/coverage-denominators.json` before current coverage claims. CH/CM source-qualified coverage has expanded; primary reconciliation and independent acceptance remain open. Other member views are explicitly historical snapshots. Retain native units and source dependency; never sum overlapping views as physical inscriptions.

## Reconciliation-only checkpoint

Read `corpus-factory/RECONCILIATION-ONLY-2026-10-11.md`, `corpus-factory/fleet-enumeration-audit-v2.json` and the member `research/reference-reconciliation-v2.json`/`research/identity-reconciliation-v2.json` before certainty, apparatus or identity claims. Reading coverage is fixed. All 18 declared public native views have immutable enumeration snapshots; restricted A/B inventories remain unacquired. Treat missing primary uncertainty marks, damage notes and conditional alternatives as apparatus limitations of the digital reference. Unknown physical duplication and unresolved source disputes remain explicit. This supersedes earlier descriptions of the other 16 views as merely historical audit imports.

The supplementary Donnelly 2020 pp. 104–105 / Fig. 3 inspection confirms the already encoded Louvre AM 1639 attribution. The legacy probable status and Masson figure lineage are retained. A comparison with ADD##219 does not establish shared object identity; the numbered catalogue join remains absent and no occurrence is added. The native receipt/control is `research/donnelly-existing-assertion-check.json`.

## Integrity priorities before expansion

Read `corpus-factory/PRIORITY-REVIEW-2026-10-11.md` when planning subsequent corpus work. It distinguishes a confirmed apparatus-delivery gap, synchronization ordering risk, required shared-evidence safeguards and unresolved scholarly decisions. These are proposed fixes, not completed remediation or new scientific acceptance. Do not interpret absent CI on a generated sync head as a passed or failed source build.

Use `corpus-factory/PRE-EXPERT-EXIT-CRITERIA.md` to assess scoped pre-expert handoff readiness. Finish source acquisition/reconciliation and independent nonexpert repairs before final expert acceptance; do not relabel missing access, licensing or calibration data as an expert-only blocker.

## Published dependency and synchronization controls

Read `corpus-factory/DEFECT-REMEDIATION-2026-10-12.md` for the repair checkpoint superseding the proposed software fixes in the October 11 priority review. Use `corpus-factory/cross-corpus-dependencies.json` for the 15 known source-supported relationships restored from 17 published native projections. Screen record selections with `python corpus-factory/check_cross_corpus_dependencies.py --records repository::record-id ...`. Unknown relationships remain unknown; pooled physical-object counts, independent-witness counts and phonetic transfer are prohibited by this register. These are bounded source assertions, not physical certification or exhaustive discovery.

Generated native bundles and master starter downloads must be built and validated on their exact source parent. A changed main branch must skip or reject publication and trigger a rebuild; never rebase or force-push validated artifacts. Lydian, Sidetic and Pisidian use one guarded automatic publisher each. Read the native corpus authorities before any scientific claim. Source-access/permission, unresolved readings, independent review and Linear B calibration prerequisites remain explicit dependencies.

Consult `corpus-factory/defect-validation-2026-10-12.json` for the exact local validation scope and fingerprints. These receipts describe validation stages on named base commits; final published revisions require their own CI evidence.

## Mega corpus before final independent acceptance

Use `Linear-A/corpus-factory/MEGA-CORPUS.md`, `build_mega_corpus.py` and `query_mega_corpus.py` to materialize and inspect native corpus views across all 18 members. The initial package has 9,116 view rows, including private authenticated A/B source records; it is not 9,116 unique inscriptions or a globally complete corpus. Original source fields, uncertainty, apparatus context and component terms travel with the rows. Native corpora remain authoritative. Preserve restricted payloads locally; do not infer a combined redistribution license, physical identity or independent witnesses. Continue lawful native coverage growth before final expert acceptance.

Linear B's `analysis/calibration-prepared-inputs-2026-10-12.json` reports real prepared observations: 5,932 documents, 5,890 nonempty transliteration surfaces and 42 missing/empty ones. Source word-ID crosswalks, linked linguistic annotations and source-certified graphical occurrences remain missing. `docs/CALIBRATION-PREPARED-INPUTS.md` and `research/calibration-acquisition-2026-10-12.json` distinguish preparation from gold delivery. Corpus expansion can continue while calibration is blocked. Do not replace occurrence gold with generated lexical analyses or expose the mixed mega-corpus interpretation layers to a blinded run.

## Full dossier and geographic discovery views

Read `corpus-factory/COVERAGE-EXPANSION-2026-10-12.md` for Anatolian and Cypriot expansion questions. Query the 287 Anatolian dossier entries with their source bibliography and uncertainty. Keep the 210 Cypriot legacy squeeze identifiers separate from the 592 parsed digital-edition entries and Greek admission/frequency populations. Preserve cast/fragment labels and unknown language/object joins. Do not turn the package's 9,562 mixed rows into a unique-inscription or independent-witness total.

## Source delivery before expert review

Use `corpus-factory/SOURCE-DELIVERY-2026-10-12.md` and its worklist for Raison–Pope, Dunand and Linear B input acquisition. Keep lawful access, source delivery, component permissions, exact alignment and scholarly acceptance separate. Respect native restrictions; preserve routing uncertainty and drafted-versus-sent status. No missing-source payload or permission was acquired by this checkpoint. Follow native intake checks before inspecting calibration answers.
