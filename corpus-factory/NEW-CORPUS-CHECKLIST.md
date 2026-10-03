# New Corpus Admission Checklist

Use this at repository creation time. A corpus is **staging** until every required box is satisfied.

## 1. Rights and licensing
- [ ] `LICENSE` routes users by material type.
- [ ] `LICENSE-CODE` covers project-original software under the fleet software policy.
- [ ] `LICENSE-CONTENT.md` covers only project-owned copyrightable corpus content.
- [ ] `LICENSING.md` explains reuse and commercial-use boundaries.
- [ ] `NOTICE` identifies important upstream/public-domain/third-party rights.
- [ ] Source-specific rights/provenance are recorded before third-party bytes are redistributed.
- [ ] No project license is asserted over rights the project does not own.

## 2. Individual AI skill
- [ ] `ai-skill/SKILL.md` exists.
- [ ] `ai-skill/references/authority-profile.json` exists.
- [ ] `ai-skill/generated/research-bundle-index.json` exists.
- [ ] A member validator exists and is declared in the master registry.
- [ ] Skill instructions preserve uncertainty, source dependence, exclusions, and rights.

## 3. Master AI
- [ ] Repository appears exactly once in `combined-ai-skill/registry/corpus-projects.json`.
- [ ] Registry declares individual skill, bundle, authority profile, validator, contract and version.
- [ ] Admission block points to `corpus-factory/CORPUS-ADMISSION-CONTRACT.md`.
- [ ] Corpus-factory membership is synchronized with master membership.
- [ ] Relationship text does not imply unsupported linguistic/script relationships.

## 4. Validation and release
- [ ] Individual corpus validator passes.
- [ ] Combined AI structural validator passes.
- [ ] Live fleet admission validator passes against the repository's current `main`.
- [ ] Corpus factory validator passes.
- [ ] Researcher starter/directory rebuild succeeds.
- [ ] Only then may the corpus be described as fleet-integrated/master-AI-ready.
- [ ] Version 1.0.0 is blocked until all admission gates pass.

## Default rule

When a new corpus repository is created, build these gates **before** substantial corpus ingestion. If an upstream license is unclear, quarantine the material or record metadata/locators only until rights are established.
