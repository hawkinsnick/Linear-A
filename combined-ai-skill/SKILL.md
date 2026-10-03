---
name: combined-corpus-research
description: Vendor-neutral evidence-first orchestration skill across the registered corpus projects.
version: 1.5.0
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
