#!/usr/bin/env python3
"""Build a vendor-neutral, provenance-aware AI research bundle from canonical repo artifacts."""
import csv, hashlib, json, os, subprocess
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/"ai-skill"/"generated"; OUT.mkdir(parents=True,exist_ok=True)
sha=os.environ.get("SOURCE_COMMIT") or subprocess.check_output(["git","rev-parse","HEAD"],cwd=ROOT,text=True).strip()
CANDIDATES=[
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
