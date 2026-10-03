# Combined Corpus Research AI

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
