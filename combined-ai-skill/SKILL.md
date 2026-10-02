---
name: combined-corpus-research
description: Vendor-neutral evidence-first orchestration skill across the registered corpus projects.
version: 1.0.0
---

# Combined Corpus Research AI — 1.0

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
