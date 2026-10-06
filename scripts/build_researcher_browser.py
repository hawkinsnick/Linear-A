#!/usr/bin/env python3
"""Build a compact researcher-browser index from rights-compatible committed layers."""
import json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows,stable_id
def compact(resource,row):
    if resource=="documents":
        f=row.get("source_fields",{})
        return {"id":stable_id(resource,row),"resource":resource,"title":f.get("name") or f.get("id") or stable_id(resource,row),"site":f.get("site") or f.get("find_place"),"type":f.get("type") or f.get("document_type"),"reference_url":row.get("public_reference_url"),"classification":row.get("classification"),"rights":row.get("provenance",{}).get("license")}
    if resource=="source_words":
        return {"id":row["word_id"],"resource":resource,"document_id":row["document_id"],"occurrence_indices":row["occurrence_indices"],"definition":row["definition"],"rights":row.get("provenance",{}).get("license")}
    f=row.get("source_fields",{})
    return {"id":row["source_sign_key"],"resource":resource,"display":f.get("display"),"series":f.get("series"),"number":f.get("number"),"source_value":f.get("value"),"reference":f.get("ref"),"rights":row.get("provenance",{}).get("license")}
def build(root=ROOT):
    rec=[]
    for resource in ("documents","source_words","signs"):
        rec.extend(compact(resource,r) for r in rows(resource,root))
    return {"format":"linear-a-researcher-browser-index-v1","boundary":"Source-reported searchable index; not decipherment or independent epigraphic verification.","records":rec}
def main():
    out=ROOT/"analysis/researcher-browser-index.json";out.write_text(json.dumps(build(),ensure_ascii=False,separators=(",",":"))+"\n")
    print("wrote",out)
if __name__=="__main__":main()
