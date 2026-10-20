# Combined Corpus Research AI

**[Every individual skill: directory, execution checks and limits](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/AI-SKILL-VALIDATION-2026-10-20.md).** The canonical master lives in this repository at `combined-ai-skill/SKILL.md`.

**[Check current coverage and readiness first](https://github.com/hawkinsnick/Linear-A/blob/main/corpus-factory/CURRENT-READINESS.md).** Catalogue identities, encoded readings, source comparison and independent acceptance have different scopes. Use the pinned native evidence for your task.

**New: [Follow three worked examples](WORKED-EXAMPLES.md)** — trace a real record, assess an unresolved comparison, and reproduce a calculation. Browser-only and optional AI/Python routes include verified results.

A vendor-neutral, evidence-first research orchestrator for the registered **corpus projects**.

It does not merge the corpora. It routes a question to each project's own AI skill and evidence bundle, preserves that project's provenance, uncertainty, exclusions and rights, and only permits cross-corpus inference after a comparability check.

## Start here

**[Start here: download, upload, and ask your first question](START-HERE.md)**

[Download the starter](downloads/README.md) · [Choose a corpus](CORPUS-DOWNLOADS.md) · [Research prompts](PROMPTS.md)

One text file supplies the master instructions and corpus directory. Add the relevant member evidence for research findings. You do not need Git or Python to get started. The [research workflow](QUICKSTART.md) explains how to trace evidence and record reproducible results.

For the governing research behavior, see [SKILL.md](SKILL.md). For the active projects, see [registry/corpus-projects.json](registry/corpus-projects.json). For cross-corpus limits, see [references/comparability-matrix.md](references/comparability-matrix.md).

## What to give your AI

The beginner route is the [starter text file](downloads/README.md), followed by the member files selected for your question. Confirm what the assistant can read before relying on a result. Uploading context does not connect the assistant automatically to GitHub or install a plugin.

Provide:
1. this `combined-ai-skill` directory;
2. the individual AI-ready bundle for each corpus project relevant to the question; and
3. when practical, the corresponding corpus repository/release so canonical records remain available.

Tell the model: **Use combined-ai-skill/SKILL.md as the orchestration instructions. For every corpus used, load its individual ai-skill/SKILL.md, authority profile and generated research-bundle index before drawing conclusions.**

## What the system can do

It can route ordinary-language questions, trace claims to native corpus evidence, compare coverage and methods, reproduce permitted computations, expose source dependence, and identify what evidence is missing when a comparison is blocked.

It cannot make incompatible evidence comparable, convert interoperability into linguistic evidence, manufacture translations of undeciphered material, treat duplicated sources as independent replication, or override source-specific rights.

## Evidence hierarchy

The Combined skill is never the authority for an inscription, sign, reading or linguistic claim. Authority remains in the member corpus and its sources. The order is:

**canonical corpus/source evidence → individual corpus skill and authority profile → generated AI bundle → Combined orchestration.**

If layers disagree, report the discrepancy and defer to canonical evidence.

## Status words

- **ALLOWED** — the requested operation is supported within documented limits.
- **GATED** — it may proceed only after the named comparability/evidence requirements are satisfied.
- **BLOCKED** — current evidence does not support the requested inference. This is a research result, not a software failure.
- **STALE** — an AI bundle does not represent the expected corpus state; canonical data take precedence.

## Scientific guarantees

The architecture enforces corpus-native evidence authority, explicit cross-corpus comparability, source-independence checks, rights separation, staleness disclosure and adversarial safeguards. Version 1.0 certifies the orchestration contract, not the completeness or correctness of every member corpus.

## Validation

Run `python combined-ai-skill/scripts/validate.py` from the repository root for structural validation. Individual projects must additionally pass their own AI bundle validators. A Combined structural PASS never substitutes for member validation or scholarly review.

Maintainers can rebuild the starter with `python combined-ai-skill/scripts/build_starter.py --write` and verify it with `--check`. The starter workflow also publishes an immutable ZIP for each instruction snapshot; it does not package member corpus data.


## Corpus admission

A new corpus is not fleet-integrated merely because a repository exists. It must pass the [Corpus Fleet Admission Contract](../corpus-factory/CORPUS-ADMISSION-CONTRACT.md):

1. component-specific licensing architecture with upstream rights preserved;
2. an individual corpus AI skill, research-bundle index, authority profile, and validator;
3. explicit membership in the master registry; and
4. structural plus live cross-repository admission validation.

No new corpus is promoted to 1.0.0 before all four gates pass. The live admission validator checks the current `main` tree of every registered repository rather than trusting registry declarations alone.

## New Anatolian reference corpora

Lydian, Sidetic and Pisidian are now routed through their individual corpus skills. Their initial releases provide attributed eDiAna digital source records, not independently collated epigraphic editions. Use each native status file for document/line counts and unresolved identity issues. The shared upstream source remains a dependency, and its CC BY-SA rights remain separate from project-original noncommercial terms.

## Milyan (Lycian B) structurally admitted member
The registry now includes [Milyan-Lycian-B](https://github.com/hawkinsnick/Milyan-Lycian-B) as a structurally admitted corpus using a native-schema contract adapter. Its individual `ai-skill/SKILL.md` and evidence inventory are available, but verified transcriptions and cross-corpus linguistic comparison remain blocked pending edition-level review.

## Current member status and Linear B acquisition
Linear A, Linear B and Milyan generate their current README summaries from native authority files and check them in CI. Keep native release versions separate from capability milestones and historical evidence snapshots. Milyan's frozen reference text is populated; independent primary-edition validation remains open. Linear B's source inspection distinguishes epigraphic EpiDoc export from the separately linked linguistic annotation package needed for calibration. See [the acquisition checkpoint](https://github.com/hawkinsnick/Linear-B/blob/main/docs/CALIBRATION-INPUTS.md); no calibration performance or graphical certification is asserted.

## Source-specific evidence frontier

For Linear A, Linear B, Phrygian, Eteocretan, Lydian and Sidetic, read each repository’s `research/source-action-plan.json` and `docs/SOURCE-ACTION-PLAN.md` before claiming rights-only readiness. Separate endpoint access, permission for the intended operation, source delivery, factual reconciliation and human adjudication. Dated searches do not prove global exhaustion. Respect existing completed crosswalks and their unresolved edges. Linear B’s `docs/CALIBRATION-INTAKE.md` describes private metadata/digest intake only; it does not establish acquired gold, certification or authority to reveal answers. Other members retain their own native stopping authorities; this checkpoint does not certify the entire fleet.

## Source checkpoint and reevaluation — 2026-10-11

Read `corpus-factory/REEVALUATION-2026-10-11.md`, `corpus-factory/source-checkpoints-2026-10-11.json` and `corpus-factory/coverage-denominators.json` before current coverage claims. CH/CM source-qualified coverage has expanded; primary reconciliation and independent acceptance remain open. Other member views are explicitly historical snapshots. Retain native units and source dependency; never sum overlapping views as physical inscriptions.

## Reconciliation-only checkpoint

Read `corpus-factory/RECONCILIATION-ONLY-2026-10-11.md`, `corpus-factory/fleet-enumeration-audit-v2.json` and the member `research/reference-reconciliation-v2.json`/`research/identity-reconciliation-v2.json` before certainty, apparatus or identity claims. Reading coverage is fixed. All 18 declared public native views have immutable enumeration snapshots; restricted A/B inventories remain unacquired. Treat missing primary uncertainty marks, damage notes and conditional alternatives as apparatus limitations of the digital reference. Unknown physical duplication and unresolved source disputes remain explicit. This supersedes earlier descriptions of the other 16 views as merely historical audit imports.

## Integrity priorities before expansion

Read `corpus-factory/PRIORITY-REVIEW-2026-10-11.md` when planning subsequent corpus work. It distinguishes a confirmed apparatus-delivery gap, synchronization ordering risk, required shared-evidence safeguards and unresolved scholarly decisions. These are proposed fixes, not completed remediation or new scientific acceptance. Do not interpret absent CI on a generated sync head as a passed or failed source build.

Use `corpus-factory/PRE-EXPERT-EXIT-CRITERIA.md` to assess scoped pre-expert handoff readiness. Finish source acquisition/reconciliation and independent nonexpert repairs before final expert acceptance; do not relabel missing access, licensing or calibration data as an expert-only blocker.

## Publication and dependency repairs

The [2026-10-12 defect checkpoint](../corpus-factory/DEFECT-REMEDIATION-2026-10-12.md) records source-parent publication guards, removal of duplicate publishers and restoration of the master source-dependency register. These engineering repairs grant no scholarly acceptance.


## Available source layers — 2026-10-12

Read `corpus-factory/AVAILABLE-EVIDENCE-GROWTH-2026-10-12.md`. The earlier verified package contains 10,527 mixed view rows across 18 members; earlier 9,562/9,116 totals describe historical packages. Added views: 802 dependent SigLA layout documents (5,144 source rectangles), two KN Fp 13 museum assertions, and Byblos 123 ordinal reviews plus 38 type-table rows. Preserve source coordinate units, the unresolved HT 6a exporter difference, modern cast status, source chronology, unassigned/competing types, false admission flags and component rights. These additions grant no new reading, independent witness, calibration result or expert acceptance.


## CH/CM source growth — 2026-10-12

Read `corpus-factory/CH-CM-SOURCE-GROWTH-2026-10-12.md` and each member’s source-growth guide and audit. The current package contains 10,759 mixed view rows; earlier totals are historical. CH has 193 dependent DBAS catalogue leads, a 204/331 named-route union, 26 existing context rows, and three unmapped INSCRIBE pages. Script dashes, motif comparisons and CHIC sign numbers are not catalogue/object identifications. CM has nine exact Louvre inventory/edition assertions and primary Tiryns context; TN 241 is a Tracing Networks database ID and footnote 3 is separate. Preserve damage versus identification certainty, source units/qualifiers, publication dates and rights. No new readings, physical witnesses, glyph adjudication or expert acceptance.

[Specialist research-task pilots: executed examples and source prerequisites](../corpus-factory/SPECIALIST-RESEARCH-PILOTS.md).
