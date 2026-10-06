#!/usr/bin/env python3
import json,pathlib,sys,tempfile
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
import research_api,build_researcher_browser,build_source_context,advanced_query,accounting_check
assert len(research_api.query("documents",limit=3)["records"])==3
idx=build_researcher_browser.build();assert idx["records"] and any(r["resource"]=="documents" for r in idx["records"])
ctx=build_source_context.build();assert all({"document_id","field","source_id","source_locator","source_license_or_rights_status","asserted_value","certainty","lineage_class"}<=set(r) for r in ctx)
st=advanced_query.stats();assert st["groups"]==1401
r=accounting_check.check({"items":[{"quantity":"X"},{"quantity":2}],"stated_total":3},{"_id":"test","X":"1"})
assert r["balanced"] is True
r2=accounting_check.check({"items":[{"quantity":"UNKNOWN"}],"stated_total":3},{"_id":"test"})
assert r2["balanced"] is None and r2["indeterminate_symbols"]==["UNKNOWN"]
print(json.dumps({"status":"PASS_BASELINE_LOGIC","browser_records":len(idx["records"]),"context_assertions":len(ctx),"source_groups":st["groups"]}))
