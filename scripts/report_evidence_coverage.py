#!/usr/bin/env python3
"""Measure evidence population without filling missing values by inference."""
import collections,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
import research_api,build_source_context
def main():
 docs=list(research_api.rows("documents"));ctx=build_source_context.build();by=collections.Counter(x["field"] for x in ctx);covered=collections.defaultdict(set)
 for x in ctx:covered[x["field"]].add(x["document_id"])
 fields=sorted(set(build_source_context.FIELD_MAP)|set(by))
 report={"format":"linear-a-evidence-population-coverage-v1","version":"3.0.20","documents":len(docs),"context":{"assertions":len(ctx),"fields":{f:{"assertions":by[f],"documents":len(covered[f]),"document_coverage":round(len(covered[f])/len(docs),6) if docs else 0} for f in fields}},"scholarship":{"status":"SCHEMA_AND_VALIDATOR_READY_POPULATION_PENDING"},"geospatial":{"status":"VALIDATOR_EXPORT_READY_POPULATION_PENDING"},"rights_boundary":"Missing values remain missing. Coverage measurement never licenses inference, source copying or GORILA-derived extraction."}
 out=ROOT/"analysis/evidence-population-coverage.json";out.write_text(json.dumps(report,indent=2)+"\n");print(json.dumps(report))
if __name__=="__main__":main()
