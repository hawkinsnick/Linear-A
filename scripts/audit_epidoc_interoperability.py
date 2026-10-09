#!/usr/bin/env python3
"""Audit the current Linear A TEI exporter against the fleet EpiDoc contract."""
import json, pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
contract=json.loads((ROOT/"corpus-factory/schemas/epidoc-interoperability-contract.json").read_text())
report={
 "schema_version":"1.0","checked":"2026-10-06","contract_version":contract["schema_version"],
 "exporter":"scripts/export_research_layer.py",
 "status":"PARTIAL_NOT_YET_EPIDOC_CONFORMANT",
 "mapped_now":["record identity via div@n/idno","complete native record preserved as sourceRecordJSON note"],
 "missing_structured_mapping":["TEI header/availability/licence","object/support description","findspot/provenance","dating","structured edition text","bibliography","typed external identifiers","revision history","structured damage/restoration/uncertainty"],
 "round_trip":{"native_payload_preserved":True,"semantic_structured_round_trip":"NOT_IMPLEMENTED"},
 "rights":{"current_manifest_mentions SigLA CC BY-NC-SA 4.0","fleet_rights_allowlist_test":"NOT_IMPLEMENTED"},
 "conclusion":"Existing output is TEI XML carrying a lossless JSON payload, but must not be represented as full EpiDoc interoperability until structured mappings, validation and semantic round-trip gates pass."
}
out=ROOT/"analysis"/"epidoc-interoperability-audit.json";out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report))
