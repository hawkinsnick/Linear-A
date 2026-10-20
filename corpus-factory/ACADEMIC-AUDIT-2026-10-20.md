# Adversarial academic desk review — 20 October 2026

## Verdict

**Reject a claim that this collection is already a comprehensive, independently validated critical corpus or a validated engine for comparative linguistic discovery. Consider a carefully scoped infrastructure/resource paper after major revision.**

The central vulnerability is epistemic: faithful reproduction of an attributed digital source is repeatedly available where independent confirmation of the ancient evidence is not. A working interface to an uncertain source remains an interface to an uncertain source. The project often states that distinction correctly; those disclaimers prevent misrepresentation but do not supply the missing evidence.

This is a deliberately hostile methodological review, not an actual independent PhD specialist's endorsement or rejection. It identifies what a skeptical reviewer can substantiate. It does not invent misconduct or treat absent evidence as proof of false readings. No new canonical reading, object identification, permission, linguistic result or expert acceptance is granted.

## Scope and method

The audit froze the current default branches of all 18 registered corpus members and the newly published standalone master. Exact revisions are in [the revision manifest](academic-audit-revisions-2026-10-20.json). The separate Egyptian project and unrelated photography/endurance projects are excluded. The standalone master now exists and passed its master-plus-18-native-workflow validation in this audit; an earlier report that its destination was unavailable is historical, not a present objection.

This is a collection-wide desk audit with deeper executable probes of Linear A structural analysis, duplicated Milyan and Cypriot source views, three reference corpora's admission states, Cretan Hieroglyphic/Cypro-Minoan coverage, and Phaistos acceptance. It is **not** an exhaustive independent line-by-line collation of every edition, photograph, glyph, rights instrument or scholarly publication.

The reproducible [probe script](academic_audit_probe.py) and [results](academic-audit-probes-2026-10-20.json) pin the 17 probe inputs. Statements based only on a native audit are identified below; recomputed statistics are separate from source assertions. New sensitivity diagnostics are post hoc and cannot become confirmatory results.

Run from Linear A:

```sh
python corpus-factory/academic_audit_probe.py --checkouts /path/to/corpora --compare corpus-factory/academic-audit-probes-2026-10-20.json
```

Severity below is **claim-relative academic severity**, not a software P0 label. A defect fatal to a claim of validated linguistic inference need not prevent publication of a transparent source-reference resource.

## 1. Primary-source verification is insufficient for a critical-edition claim — critical for that claim

A reviewer would ask: *Which actual readings have been independently checked, by whom, against which edition or object, and what was the disagreement rate?*

The native Lydian, Sidetic and Pisidian admission files contain **183 digital records and 602 source lines in total, with zero records admitted under their stricter analytical policy**. All three retain unresolved primary-edition/object/review prerequisites. This does not mean their upstream text is worthless or false. It means their integrity and reference-use claims are materially narrower than a new critical edition. In Phrygian, the explicit-lineage audit records **3 of 162 source-ID groups** with record-specific edition lineage, **159 unjoined groups**, and zero independently collated lineages. A corpus-level upstream bibliography is not a record-level edition/locus citation.

Evidence: [analysis/record-admission.json](https://github.com/hawkinsnick/Lydian/blob/deb4c7d3a094fdcb9e34206964dc150738cd2c70/analysis/record-admission.json); [analysis/record-admission.json](https://github.com/hawkinsnick/Sidetic/blob/0a58cdfdd82fdbcb4964b90ba068ae21576792aa/analysis/record-admission.json); [analysis/record-admission.json](https://github.com/hawkinsnick/Pisidian/blob/23925bd586857b13715a11d7a38aea3a78d8e307/analysis/record-admission.json); [analysis/explicit-source-lineage-audit.json](https://github.com/hawkinsnick/Phrygian/blob/0f469d2b9e50cb5c55315993c41a0af3c3aae3d3/analysis/explicit-source-lineage-audit.json).

**Required response:** publish bounded record-level comparison results and a genuinely external specialist audit with exact source access, uncertainty, disagreements, corrections and denominators. If those are unavailable, describe the release as an attributed digital reference collection. Do not require every infrastructure record to become a new edition before useful reference publication; require the narrower claim to remain explicit.

## 2. Coverage is deep in selected places and shallow elsewhere — major

Recomputed/native-authority examples:

| Layer | Declared coverage | What it does not establish |
|---|---|---|
| Cretan Hieroglyphic | 331 catalogue identities; 13 reading versions on six entries | Complete readings for 331 objects; the six include different source strata |
| Cypro-Minoan | 254 control slots; 21 rich records; 28 encoded assertions on 13 rich records | Representative sign frequencies, full-tablet coverage or 254 transcriptions |
| Linear A critical pilot | 10 problem-selected entries; 51 attributed assertions | A representative corpus error estimate |
| Cypriot Greek | 592 digital entries; 170 source-interpreted Greek, 149 with clear tokens | All 592 being Greek inscriptions or a world-corpus denominator |
| Byblos | 39 catalogue records; native status records zero transcriptions/verified core sequences | A populated critical transcription corpus |
| Eteocretan | 12 attributed reading versions; zero analysis-eligible rows in its audit | Twelve independently admitted inscriptions |

These are different units. A percentage such as 13/21 is confined to the selected rich-record layer; it must not be re-expressed as 13/254 physical-object coverage. The availability of lawful digitized sources may determine what is included. Without inclusion/exclusion accounting by period, genre, site, material and source family, cross-corpus results can reflect acquisition and editorial practice rather than ancient distributions.

Evidence: [analysis/current-status.json](https://github.com/hawkinsnick/Cretan-hieroglyphs/blob/4e5704e62c966220ef7b85feaa8205c61a3f3540/analysis/current-status.json); [analysis/occurrence-coverage-v1.json](https://github.com/hawkinsnick/Cypro-Minoan/blob/185ef0a44222281fbde53589185f8b647ad85313/analysis/occurrence-coverage-v1.json); [analysis/critical-evidence-coverage-v1.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/analysis/critical-evidence-coverage-v1.json); [exports/audit.json](https://github.com/hawkinsnick/Cypriot-syllabic-Greek/blob/148e335c3f68c790b5850fea75c7fa37835d971c/exports/audit.json); [analysis/current-status.json](https://github.com/hawkinsnick/Byblos-syllabary/blob/16ffb1a32044c92cbd69d991adffc7be797621f5/analysis/current-status.json); [exports/audit.json](https://github.com/hawkinsnick/Eteocretan/blob/5f947f3c551d5123f5d6f9134a0785821e2200a3/exports/audit.json).

**Required response:** publish native inclusion frames and missingness by stratum before any frequency/generalization claim. Pilot counts are useful if described as pilot counts. The collection's deliberately null aggregate physical-population/coverage fields are correct and must stay null until a defensible denominator exists.

## 3. Repository multiplicity can create pseudoreplication — critical for independence claims

I verified **byte-identical Milyan source files** in the Lycian-and-Carian and Milyan-Lycian-B repositories: SHA-256 `e53dca3df71f06af95c0091646ee0d1b20fe6c78c1a24ac0f9b9e49cadd425a0`, containing **114 nonempty source text rows**. I also verified that **all 25 Eteocypriot source IDs occur in the 592-entry broader Cypriot index**.

These overlaps may be entirely appropriate as research views. They provide neither additional inscriptions nor independent corroboration. A repository namespace prevents key collisions; it does not establish evidential independence. A reviewer could dismantle an argument that counts agreement between these views as replication, or pools them as independent observations.

Evidence: probe source-overlap results; [research/reference-manifest.json](https://github.com/hawkinsnick/Milyan-Lycian-B/blob/b0ee68112c25f89891bd2ba05c5830d816608975/research/reference-manifest.json); [data/raw/ediana/milyan-1-0.json](https://github.com/hawkinsnick/Lycian-and-Carian/blob/d0f87ce131d4a905f6de5e9bfd4c612849a4f4ea/data/raw/ediana/milyan-1-0.json); the two pinned Cypriot `exports/corpus.json` inputs.

**Required response:** use source-family/witness/physical-unit dependence groups in every analysis, with explicit duplicate-view exclusions or shared weighting. Do not force uncertain physical identities into deduplication just to obtain a clean total. The native warning against summing heterogeneous view rows is a real mitigation, not evidence that every downstream user will honor it.

## 4. Historical Linear A candidates do not constitute confirmatory discoveries — critical for confirmatory claims

The frozen structural repair explicitly says its **12 candidates were selected using the same historical corpus**. Its Holm correction addresses the displayed fixed family and expressly does not undo that selection. Resampling the same corpus does not manufacture a new dataset or make the initial selection independent. The prospective-membership audit finds **7 of the 24 frozen cohort labels already present in v3**, with historical analytical-input identity not established; prospective scoring remains prohibited.

The data support a conditional exploratory statement about the chosen historical representation. They do not support a clean discovery/replication narrative. The disclosure is scientifically responsible; the missing independent test remains missing.

Evidence: [research/structural-sensitivity-repair-v1.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/research/structural-sensitivity-repair-v1.json); [analysis/prospective-independence-audit-v1.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/analysis/prospective-independence-audit-v1.json).

**Required response:** reconstruct exact pre-analysis exposure/input history or use an admissible genuinely untouched cohort under a frozen selection/scoring plan. Do not silently delete the seven overlapping labels or treat a rerun as prospective confirmation.

## 5. The structural null does not identify morphology or language — critical for those interpretations

The implemented null permutes signs within **source-defined word groups**, preserving length and sign multiset. Rejecting that null demonstrates a positional departure from that exchangeability assumption. It does not distinguish morphology from formulaic administrative patterns, names, orthographic conventions, source segmentation, material/genre composition or other structured processes. Calling a source-defined group a word in storage does not independently establish a linguistic word boundary.

I recomputed **1,401 serialized groups, 1,283 nonempty groups, 836 distinct nonempty sequences and 668 hapax types**. The latter is approximately 79.9% of types, so many proposed generalizations would rely on sparse sequence evidence. The 118 empty source groups require accounting; they must not be silently converted into linguistic zeroes or discarded without scope disclosure.

Evidence: [data/source_words.csv](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/data/source_words.csv); [scripts/run_structural_sensitivity_v1.py](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/scripts/run_structural_sensitivity_v1.py); probe results.

**Required response:** state the precise structural estimand; report effect sizes and uncertainty under competing genre/formula/representation models; execute admissible known-answer/degraded controls before assigning linguistic significance. No translation, morpheme or cross-script value is established by this statistic.

## 6. Dependence and composition need better stress tests — major, not a demonstrated numerical collapse

The historical bootstrap uses **451 exact source-document labels**. I found **79 label families containing both an `a` and a `b` record**, including matching HT tablet labels. Treating exact labels as clusters does not establish independence across faces, scribes, archive batches or formula families. Nevertheless, matching labels alone are not enough to certify physical joins.

I therefore ran a clearly heuristic, post hoc sensitivity grouping: merge only exact matching a/b label pairs, reducing the diagnostic cluster count to **372**. I used the same 5,000 bootstrap replicates and seed. The number exceeding the project's historical lower-z diagnostic convention remains **6 of 12**, unchanged. This convention is not a valid standalone significance test, and the protocol itself disclaims that interpretation.

Composition is also concentrated: **749/1,283 nonempty tokens (58.4%) carry the HT prefix**. Removing that prefix leaves **534 tokens**, and all 12 selected candidates retain positive enrichment relative to the same permutation expectation. For illustration, AB008-initial z changes from approximately 14.07 to 11.76; AB081-initial from 7.36 to 2.07. These post hoc values do not establish replication or significance. They show that this crude attack did **not** erase the directional pattern.

**Required response:** authority-supported physical-object clustering and broader source/site/genre/scribe sensitivity are still needed. Do not assert that this audit disproved the patterns. Do not promote my unverified a/b groupings into a canonical object crosswalk.

## 7. The known-answer validation is designed but not executed — critical for validated-method claims

Linear B supplies 5,932 source records and 5,890 nonempty transcription surfaces, but the known-answer experiment has no admitted aligned linguistic gold and no scored result. Graphical controls and associated alignment remain separate source-delivery dependencies. A prediction-freeze tool and synthetic rejection tests show engineering readiness, not sensitivity, specificity, calibration or linguistic usefulness on real ground truth.

Evidence: [research/experiment-gates.json](https://github.com/hawkinsnick/Linear-B/blob/314638026db8eac689e10b0a7193ffef0d996a07/research/experiment-gates.json); [analysis/current-status.json](https://github.com/hawkinsnick/Linear-B/blob/314638026db8eac689e10b0a7193ffef0d996a07/analysis/current-status.json); [docs/CALIBRATION-INPUTS.md](https://github.com/hawkinsnick/Linear-B/blob/314638026db8eac689e10b0a7193ffef0d996a07/docs/CALIBRATION-INPUTS.md).

**Required response:** acquire admissible aligned inputs; freeze predictions before gold exposure; execute declared evaluation and publish per-case errors and negative controls. Until then, validated linguistic method is not an available claim.

## 8. The legacy disagreement collection is not yet an attributed critical apparatus — major

The joined Linear A attribution audit examines **10 cases and preserves 20 alternative strings**, but establishes **zero two-source same-locus competing pairs**. All ten retain specific evidence gaps. The earlier queue has no per-row named scholar, publication and locus; some older root CSV rows still use `resolved_classification` or independent-witness wording that later audits qualify. The current query interface correctly calls these legacy project queue cases rather than authenticated pairs.

A hostile reviewer would ask where the alternatives actually came from and whether each purported dispute exists in the cited scholarship. I cannot infer fabrication from missing attribution. I can refuse to treat untraced alternatives as evidence of scholarly disagreement.

Evidence: [analysis/legacy-case-attribution-audit.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/analysis/legacy-case-attribution-audit.json); [research/legacy-case-attribution.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/research/legacy-case-attribution.json); [data/rc2_case_register.csv](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/data/rc2_case_register.csv); [research/evidence-query-profile.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/research/evidence-query-profile.json).

**Required response:** establish both source witnesses and their common locus, or maintain an explicitly non-evidentiary quarantine. Superseded root data must remain visibly subordinated to current qualification in every distribution path. Preserving correction history is appropriate; allowing an old row to masquerade as current scholarship is not.

## 9. Working AI retrieval is not independently established academic answer accuracy — major

The native functional validator retrieves the **first record of each nonempty declared collection**, checks its source pointer/payload, checks hashes and rejects missing IDs. This is useful deterministic contract testing. It is not a probability sample of difficult questions or a blind academic grading exercise. The documented fresh-context model exercises are explicitly non-blinded development exercises; the raw logs are not all independently inspectable in the public corpus.

A source pointer can faithfully return an erroneous source assertion. Agreement with that same stored record is not an external correctness criterion. No cross-platform accuracy, hallucination rate or calibrated abstention probability follows from these checks. The new master correctly sets those claims to false.

Evidence: [scripts/validate_ai_skill.py](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/scripts/validate_ai_skill.py); [corpus-factory/AI-SKILL-VALIDATION-2026-10-20.md](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/corpus-factory/AI-SKILL-VALIDATION-2026-10-20.md); [manifest.json](https://github.com/hawkinsnick/Master-Corpus-AI-Skill/blob/618016f165e4414d3869fa0e1eb6a16dde7907c9/manifest.json).

**Required response:** freeze a task set with difficult IDs, conflicting editions, absent evidence, uncertain signs, rights-sensitive requests and meaningful adversarial prompts; obtain source-qualified blinded grading; compare with direct source lookup and another baseline; publish models, prompts, versions, errors and exclusions. Do not demand source permissions or private test answers be published unlawfully to achieve transparency.

## 10. Review packets and fine-grained comparison counts are not completed peer validation — major

Phaistos records **242 slots and 61 groups**, but its acceptance authority reports **zero accepted external reviews**, **196 ordinals not individually certified**, no fine-detail certification and no accepted final 2.0 release. Elsewhere, example source-study responses contain blank reviewer identities and `DRAFT_NOT_REVIEWED`. These are honest prepared instruments, not completed review evidence. Similarly, hundreds of apparatus flags or thousands of encoded comparison records measure work granularity, not independent discoveries or inscriptions.

Evidence: [analysis/acceptance-2.0.json](https://github.com/hawkinsnick/Phaistos-Disc/blob/d8665ef0be10ea95af15e6df1cb01a55c23b7722/analysis/acceptance-2.0.json); [review/source-study-response.json](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/review/source-study-response.json); [research/reference-manifest.json](https://github.com/hawkinsnick/Milyan-Lycian-B/blob/b0ee68112c25f89891bd2ba05c5830d816608975/research/reference-manifest.json).

**Required response:** record separately attributable per-target reviews and actual decisions with evidence consulted, expertise, independence, conflicts and uncertainty. An inconclusive decision is valid. Do not make expert endorsement a substitute for reproducible source evidence, or a blanket requirement for publishing a clearly labelled digital reference layer.

## 11. Component rights constrain scientific reproducibility and the blanket noncommercial objective — major scope constraint

The source layers intentionally carry different upstream terms. The eDiAna layers state CC BY-SA 4.0, whereas SigLA-derived material carries CC BY-NC-SA 4.0, and original project components have separate terms. Creative Commons' official BY-SA deed permits commercial sharing/adaptation subject to its conditions and prohibits additional restrictions; its BY-NC-SA deed has a NonCommercial condition. Consequently, the project cannot promise that all upstream BY-SA material becomes noncommercial simply by being included here. This is a limit on the blanket objective, **not a finding that the current component notices violate the licenses**.

The private A/B build boundary and excluded protected sources also mean not every evidence route is equally accessible to an outside reproducer. A public hash or a citation does not supply the underlying source bytes, rights or object access. Inaccessibility limits verification; it is not permission to reconstruct restricted datasets indirectly.

Evidence: native component notices; [corpus-factory/MEGA-CORPUS.md](https://github.com/hawkinsnick/Linear-A/blob/d0e2ca335230c358cb0d95e6ddd188dd2455ca8d/corpus-factory/MEGA-CORPUS.md); official [BY-SA deed](https://creativecommons.org/licenses/by-sa/4.0/) and [BY-NC-SA deed](https://creativecommons.org/licenses/by-nc-sa/4.0/), inspected 20 October 2026. This audit is not exhaustive legal clearance.

**Required response:** keep component-level attribution and reuse notices attached to exports, distinguish lawful public/private reconstruction routes, and describe the achievable licensing scope precisely. Do not erase upstream permissions to satisfy a project-wide preference.

## 12. Added scholarly value needs a measured demonstration — major for superiority claims

Routing, provenance wrappers, exports, uncertainty preservation and reproducible source lookups are plausible useful contributions. The inspected validation artifacts do not establish that this system helps a qualified researcher produce a more accurate apparatus, detect a real new edition discrepancy, or complete a task faster/more reliably than direct use of the upstream scholarly resources. Internal end-to-end exercises establish workflow operation; they do not establish academic superiority.

**Required response:** choose three bounded specialist tasks, compare against direct upstream/manual workflows with the same permitted evidence, and publish corrections found, task failures, time/effort and external assessment. A transparent negative result is more persuasive than another unsupported maturity label.

## What survived the hostile audit

- The current standalone master is real, names the 18 members and passed its documented operational check with all 18 native checkouts.
- The repositories explicitly separate source assertions, unknowns, strict analytical admission and expert acceptance in many important places. Zero admitted records is not hidden by a green source hash.
- The two new coarse Linear A stress diagnostics did not overturn the bounded historical pattern summary. I found no basis here to label those results fraudulent or mathematically refuted.
- Versioned correction, source-specific licensing and refusal to invent missing gold are strengths a fair hostile reviewer must acknowledge. These safeguards are part of the resource's legitimate value.

## Required revision order

1. **Specify the publication claim.** Ship a citable, bounded attributed-reference/infrastructure release; withhold critical-edition, validated-inference and calibrated-AI claims until their evidence exists.
2. **Prove one difficult scholarly use case.** Obtain exact source pairs and loci for a small critical apparatus, or a source-qualified external audit of a defined stratum. Record unresolved cases rather than invent completion.
3. **Execute the known-answer control when admissible inputs exist.** Keep blind inputs and predictions sealed until the frozen procedure permits evaluation.
4. **Model dependence and selection explicitly.** Group duplicate source views and qualified witness families; report missingness and sensitivity to supported object/site/genre units. Use heuristic groupings only as labelled diagnostics.
5. **Evaluate AI answers with an external criterion.** Keep source retrieval tests, model behavior tests and scholarly validation as three separate result classes.

The skeptical conclusion is not that the collection has no value. It is that its defensible present contribution is research infrastructure over attributed, unevenly verified sources. That is substantially narrower than comprehensive independent validation or a demonstrated advance in decipherment.
