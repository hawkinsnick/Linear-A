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

## Milyan admission checkpoint (2026-10-08)
`hawkinsnick/Milyan-Lycian-B` is registered provisionally. Route Milyan/Lycian B questions to its `ai-skill/SKILL.md`; current evidence is three bibliographic segment records for two monuments, with zero verified transcriptions. Do not treat it as admitted or use it for text-level cross-corpus inference until critical edition collation, rights review and bundle validation pass. Milyan is not synonymous with Lycian A.

Milyan update: member research API now provides bibliographic inventory search, empty line-layer KWIC, coverage and JSON/CSV exports. Its source-reconciliation matrix explicitly blocks all unverified readings; zero KWIC hits cannot establish lexical absence. Follow the individual Milyan skill and bundle index for current evidence state.
