#!/usr/bin/env python3
"""Build a vendor-neutral, provenance-aware AI research bundle from canonical repo artifacts."""
import csv, hashlib, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"ai-skill"/"generated"; OUT.mkdir(parents=True,exist_ok=True)
sha=os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
CANDIDATES=[('sidetic_abydos_edition_comparison', 'corpus-factory/SIDETIC-ABYDOS-EDITION-COMPARISON-2026-10-16.md')]+[("milyan_tl44_source_checkpoint", "corpus-factory/MILYAN-TL44-SOURCE-CHECKPOINT.md")]+[('four_corpus_source_collation', 'corpus-factory/FOUR-CORPUS-SOURCE-COLLATION-2026-10-15.md'), ('four_corpus_source_collation', 'corpus-factory/source-collation-2026-10-15.json'), ('four_corpus_source_collation', 'corpus-factory/validate_source_collation_20261015.py'), ('four_corpus_source_collation', 'corpus-factory/test_source_collation_20261015.py'), ('four_corpus_source_collation', 'corpus-factory/source-collation-snapshots/Cypro-Minoan-2026-10-15.json'), ('four_corpus_source_collation', 'corpus-factory/source-collation-snapshots/Lydian-2026-10-15.json'), ('four_corpus_source_collation', 'corpus-factory/source-collation-snapshots/Sidetic-2026-10-15.json'), ('four_corpus_source_collation', 'corpus-factory/source-collation-snapshots/Pisidian-2026-10-15.json')]+[('fleet_attribution_review', 'corpus-factory/ATTRIBUTION-REVIEW.md'), ('fleet_attribution_review', 'corpus-factory/attribution-review-rollout.json'), ('fleet_attribution_review', 'corpus-factory/validate_attribution_reviews.py'), ('fleet_attribution_review', 'corpus-factory/test_attribution_reviews.py'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Linear-A.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Cypro-Minoan.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Linear-B.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Cretan-hieroglyphs.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Phaistos-Disc.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Byblos-syllabary.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Cypriot-syllabic-Greek.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Eteocypriot.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Eteocretan.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Lycian-and-Carian.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Phrygian.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Anatolian-Hieroglyphic.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Archanes-Script.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Aegean-anomalous.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Lydian.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Sidetic.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Pisidian.json'), ('fleet_attribution_snapshot', 'corpus-factory/attribution-review-snapshots/Milyan-Lycian-B.json')]+[('attribution_review', 'research/attribution-review.json'), ('attribution_review', 'analysis/attribution-review-audit.json'), ('attribution_review', 'docs/ATTRIBUTION-REVIEW.md'), ('attribution_review', 'scripts/attribution_review.py'), ('attribution_review', 'scripts/test_attribution_review.py')]+[('legacy_attribution_register', 'research/legacy-case-attribution.json'), ('legacy_attribution_search_log', 'research/legacy-case-source-searches.json'), ('legacy_attribution_audit', 'analysis/legacy-case-attribution-audit.json'), ('legacy_attribution_guide', 'docs/LEGACY-CASE-ATTRIBUTION.md'), ('legacy_attribution_validator', 'scripts/legacy_case_attribution.py'), ('legacy_attribution_tests', 'scripts/test_legacy_case_attribution.py')]+[('fleet_evidence_query_guide', 'corpus-factory/EVIDENCE-AND-ALTERNATIVES.md'), ('fleet_evidence_query_rollout', 'corpus-factory/evidence-query-rollout.json'), ('native_evidence_profile', 'research/evidence-query-profile.json'), ('native_evidence_coverage', 'analysis/evidence-query-coverage.json'), ('native_evidence_query', 'scripts/evidence_query.py'), ('native_evidence_query_tests', 'scripts/test_native_evidence_query.py'), ('native_evidence_guide', 'docs/EVIDENCE-AND-ALTERNATIVES.md')]+[("milyan_primary_collation","corpus-factory/MILYAN-SCHUERR2005-COLLATION.md")]+[("critical_evidence_query", "scripts/query_critical_evidence.py"), ("critical_evidence_coverage", "analysis/critical-evidence-coverage-v1.json"), ("critical_evidence_query_guide", "docs/CRITICAL-EVIDENCE-QUERIES.md")]+[("input_reconciliation_guide","corpus-factory/INPUTS-AND-RECONCILIATION-2026-10-14.md")]+[("CM209_source_check","corpus-factory/CM209-SOURCE-CHECK-2026-10-14.md")]+[("ch_cm_source_growth","corpus-factory/CH-CM-SOURCE-GROWTH-2026-10-12.md"),("ch_cm_actual_build","corpus-factory/ch-cm-source-growth-build-2026-10-12.json")]+[("evidence_growth_guide","corpus-factory/AVAILABLE-EVIDENCE-GROWTH-2026-10-12.md"),("evidence_growth_receipt","corpus-factory/mega-corpus-evidence-growth-2026-10-12.json")]+[["available_evidence_growth", "research/sigla-source-layout.json"], ["available_evidence_growth", "analysis/sigla-layout-audit.json"], ["available_evidence_growth", "research/sigla-layout-source-inspection.json"], ["available_evidence_growth", "scripts/build_sigla_layout_layer.py"], ["available_evidence_growth", "docs/SIGLA-SOURCE-LAYOUT.md"]]+[("secondary_reference_rights", "docs/LINEARA-XYZ-REFERENCE.md"), ("master_secondary_reference_instructions", "combined-ai-skill/SKILL.md")]+[("source_delivery_guide", "corpus-factory/SOURCE-DELIVERY-2026-10-12.md"), ("source_delivery_worklist", "corpus-factory/source-delivery-worklist-2026-10-12.json")]+[("source_access_and_delivery", "research/source-access-delivery-2026-10-12.json"), ("source_delivery_requests", "docs/RAISON-POPE-ACCESS-FOLLOWUP.md")]+ [("coverage_expansion_guide", "corpus-factory/COVERAGE-EXPANSION-2026-10-12.md"), ("coverage_expansion_actual_receipt", "corpus-factory/mega-corpus-expansion-build-2026-10-12.json"), ('mega_corpus_actual_receipt', 'corpus-factory/mega-corpus-build-2026-10-12.json'),('mega_corpus_guide', 'corpus-factory/MEGA-CORPUS.md'), ('mega_corpus_builder', 'corpus-factory/build_mega_corpus.py'), ('mega_corpus_query', 'corpus-factory/query_mega_corpus.py')]+[('defect_validation_receipts', 'corpus-factory/defect-validation-2026-10-12.json'),('native_skill_instructions', 'ai-skill/SKILL.md'),('cross_corpus_dependencies', 'research/cross-corpus-dependencies.json'), ('ai_integrity_guide', 'docs/AI-INTEGRITY.md'), ('master_cross_corpus_dependencies', 'corpus-factory/cross-corpus-dependencies.json'), ('defect_remediation_checkpoint', 'corpus-factory/DEFECT-REMEDIATION-2026-10-12.md')]+[
 ("pre_expert_exit_criteria","corpus-factory/PRE-EXPERT-EXIT-CRITERIA.md"),
 ("integrity_priority_review","corpus-factory/PRIORITY-REVIEW-2026-10-11.md"),("source_action_plan","research/source-action-plan.json"),("source_action_guide","docs/SOURCE-ACTION-PLAN.md")]+[
 ("generated_current_summary","README.md"),("current_summary_builder","scripts/build_current_summary.py"),("p1_reconciliation","docs/P1-RECONCILIATION-2026-10-11.md"),("p1_evidence_snapshot","corpus-factory/p1-evidence-snapshot.json"),("p1_validation_results","corpus-factory/p1-validation-results.json")]+[("collection_work_ledger","research/collection-work-ledger.json"),("collection_review_packet","review/collection-packet.json"),("collection_review_guide","docs/COLLECTION-REVIEW.md")]+[
 ("edition_catalogue_pilot","research/edition-catalogue-pilot.json"),
 ("edition_catalogue_audit","analysis/edition-catalogue-pilot-audit.json"),
 ("edition_catalogue_comparison","research/edition-catalogue-comparison.csv"),
 ("edition_catalogue_guide","docs/EDITION-CATALOGUE-PILOT.md"),
 ('public_sigla_layer_audit', 'analysis/public-sigla-layer-audit.json'),
 ('public_sigla_documents', 'research/sigla-source-documents.jsonl'),
 ('public_sigla_groups', 'research/sigla-source-groups.jsonl'),
 ('public_sigla_signs', 'research/sigla-source-signs.jsonl'),
 ('public_sigla_guide', 'docs/PUBLIC-SIGLA-LAYER.md'),
 ('gorila_route_acquisition', 'research/gorila-route-acquisition.json'),
 ('gorila_route_audit', 'analysis/gorila-route-audit.json'),
 ('gorila_route_guide', 'docs/GORILA-ROUTE-ACQUISITION.md'),
 ('critical_quantity_components', 'research/critical-pilot-quantity-components.csv'),
 ('critical_metadata_comparison', 'research/critical-pilot-metadata-comparison.csv'),

 ("critical_pilot_sigla_witness","research/critical-pilot-sigla-witness.json"),
 ("critical_pilot_sigla_slots","research/critical-pilot-sigla-slots.csv"),
 ("critical_pilot","research/critical-pilot.json"),
 ("critical_pilot_audit","analysis/critical-pilot-audit.json"),
 ("critical_disagreement_comparison","research/critical-disagreement-comparison.csv"),
 ("critical_pilot_review_queue","reviews/critical-pilot-review.tsv"),
 ("critical_pilot_guide","docs/CRITICAL-PILOT.md"),
 ("edition_concordance","research/edition-concordance.csv"),
 ("edition_concordance_audit","analysis/edition-concordance-audit.json"),
 ("edition_routes","research/edition-route-evidence.json"),
 ("edition_concordance_guide","docs/EDITION-CONCORDANCE.md"),
 ("bounded_primary_collation","analysis/pre-expert-primary-collation.json"),
 ("pre_expert_contract","research/pre-expert-maximum.json"),
 ("pre_expert_source_audit","analysis/pre-expert-source-audit.json"),
 ("review_handoff","docs/PRE-EXPERT-HANDOFF.md"),
 ("comparison_contract","research/linear-a-b-control-interface.json"),
 ("current_status","analysis/current-status.json"),("audit","exports/audit.json"),
 ("coverage","data/coverage.json"),("claims","release/CLAIM-REGISTRY.csv"),
 ("corpus_json","exports/corpus.json"),("corpus_jsonl","exports/corpus.jsonl"),
 ("greek_subset","exports/greek-subset.json"),("eteocypriot_components","exports/eteocypriot-components.json"),
 ("rights_matrix","DATA-LICENSE-MATRIX.md"),("rights","docs/RIGHTS.md"),
 ("rights_and_licensing","docs/RIGHTS-AND-LICENSING.md"),("notice","NOTICE"),("third_party","THIRD-PARTY-NOTICES.md")
]
CANDIDATES += [("software_p0_audit_guide", "corpus-factory/P0-REAUDIT-2026-10-16.md"), ("software_p0_validation_receipts", "corpus-factory/p0-validation-2026-10-16.json")]
CANDIDATES += [('current_p1_evidence', 'corpus-factory/fleet-gap-register.json'), ('current_p1_evidence', 'corpus-factory/p1-current-work.json'), ('current_p1_evidence', 'corpus-factory/P1-EXECUTION-2026-10-16.md'), ('current_p1_evidence', 'corpus-factory/validate_p1_refresh.py'), ('current_p1_evidence', 'corpus-factory/test_p1_refresh.py'), ('p1_native_followup', 'corpus-factory/p1-followup-snapshots/Phrygian.json'), ('p1_native_followup', 'corpus-factory/p1-followup-snapshots/Eteocypriot.json'), ('p1_native_followup', 'corpus-factory/p1-followup-snapshots/Sidetic.json')]
CANDIDATES += [("p1_validation_receipts", "corpus-factory/p1-validation-2026-10-16.json")]
CANDIDATES += [('human_validation_routing', 'corpus-factory/p1-human-readiness.json'), ('human_validation_routing', 'corpus-factory/HUMAN-VALIDATION-ROUTE.md'), ('human_validation_routing', 'corpus-factory/validate_human_readiness.py'), ('human_validation_routing', 'corpus-factory/test_human_readiness.py'), ('human_validation_routing', 'corpus-factory/p1-human-validation-results.json')]
CANDIDATES += [('research_readiness', p) for p in ['docs/NORTHWESTERN-RESEARCH-READINESS.md', 'analysis/research-readiness.json', 'scripts/research_readiness.py', 'scripts/test_research_readiness.py', 'scripts/build_research_package.py', 'scripts/export_research_layer.py', 'scripts/build_source_context.py', 'analysis/evidence-population-coverage.json']]
CANDIDATES += [('researcher_walkthrough', p) for p in [
 'combined-ai-skill/WORKED-EXAMPLES.md', 'scripts/walkthrough_count.py',
 'docs/examples/researcher-walkthrough/ARKH-1a.json',
 'docs/examples/researcher-walkthrough/U008.json',
 'docs/examples/researcher-walkthrough/counts.json']]

CANDIDATES += [("research_delivery", p) for p in ['scripts/research_delivery.py','scripts/test_research_delivery.py','docs/RESEARCH-DELIVERY.md','analysis/research-delivery.json']]
CANDIDATES += [('northwestern_program', p) for p in ['corpus-factory/NORTHWESTERN-RESEARCH-PROGRAM.md','corpus-factory/federated_research.py','corpus-factory/test_federated_research.py','corpus-factory/research-delivery-fleet.json','corpus-factory/northwestern-exercises.json','corpus-factory/northwestern-validation.json','corpus-factory/northwestern-published-revisions.json']]
CANDIDATES += [('northwestern_requirements', p) for p in ['corpus-factory/northwestern-work-program.json','corpus-factory/validate_northwestern_program.py','corpus-factory/test_northwestern_program.py']]
CANDIDATES += [('northwestern_publication', p) for p in ['corpus-factory/verify_federated_snapshot.py','corpus-factory/northwestern-hosted-leaf-checks.json']]


CANDIDATES += [("specialist_task_pilot", p) for p in ['scripts/task_pilot.py', 'scripts/test_task_pilot.py', 'docs/RESEARCH-TASK-PILOT.md', 'analysis/task-pilot-example.json', 'research/task-pilot.json']]
CANDIDATES += [("specialist_task_pilot_master", "corpus-factory/SPECIALIST-RESEARCH-PILOTS.md")]
CANDIDATES += [("bounded_source_study", p) for p in ['research/source-study-2026-10-17.json', 'scripts/source_study.py', 'scripts/test_source_study.py', 'docs/SOURCE-STUDY-2026-10-17.md', 'review/source-study-packet.json', 'review/source-study-response.json', 'analysis/source-study-audit.json']]
CANDIDATES += [("source_study_master_route", "corpus-factory/SOURCE-STUDIES-2026-10-17.md")]
artifacts=[]
for role,rel in CANDIDATES:
 p=ROOT/rel
 if p.is_file():
  b=p.read_bytes(); artifacts.append({"role":role,"path":rel,"sha256":hashlib.sha256(b).hexdigest(),"bytes":len(b)})
bundle={"schema_version":"0.3.1","skill_version":"0.3.1","source_commit":sha,
 "generated_at_utc":datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
 "canonical_repository":True,
 "contract":{"corpus_is_authoritative":True,"missing_means_unknown":True,"cross_corpus_equivalence_requires_explicit_evidence":True,
 "preserve_uncertainty":True,"preserve_source_independence":True,"preserve_rights":True},
 "artifacts":artifacts}
(OUT/"research-bundle-index.json").write_text(json.dumps(bundle,indent=2)+"\n",encoding="utf-8")
(OUT/"source-state.json").write_text(json.dumps({"schema_version":"1.0","source_commit":sha,"skill_version":"0.3.1","bundle_index":"ai-skill/generated/research-bundle-index.json"},indent=2)+"\n",encoding="utf-8")
print(f"Indexed {len(artifacts)} canonical artifacts at {sha}")
