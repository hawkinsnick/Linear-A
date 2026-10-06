#!/usr/bin/env python3
"""Populate source-reported context assertions without inference."""
import csv,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows
FIELD_MAP={"site":["site","find_place","findplace"],"document_type":["type","document_type"],"dimensions":["dimensions","size"],"period":["period","date"],"support":["support","material"]}
def first(d,keys):
    for k in keys:
        if k in d and d[k] not in (None,""): return d[k],k
    return None,None
def build(root=ROOT):
    out=[]
    for r in rows("documents",root):
        f=r.get("source_fields",{});prov=r.get("provenance",{})
        for field,keys in FIELD_MAP.items():
            val,key=first(f,keys)
            if key:
                out.append({"document_id":r["source_record_id"],"field":field,"asserted_value":val,"source_field":key,"source_id":"SigLA authenticated derivative","source_locator":prov.get("json_pointer"),"source_license_or_rights_status":prov.get("license"),"certainty":"SOURCE_REPORTED","lineage_class":"SAME_SIGLA_SOURCE_LAYER"})
    return out
def main():
    out=ROOT/"research/source-context-assertions.jsonl"
    out.write_text("".join(json.dumps(r,ensure_ascii=False,separators=(",",":"))+"\n" for r in build()))
    print("wrote",out)
if __name__=="__main__":main()
