#!/usr/bin/env python3
"""Validate scholarship-link records without reproducing publication text."""
import argparse,json,pathlib
REQ={"citation_id","authors","title","year","linked_entity_ids","claim_scope","rights_status"}
SCOPES={"mentions","transcribes","classifies","dates","provenience","palaeography","metrology","interpretation","comparison","correction"}
def validate(path):
 data=json.loads(path.read_text());rows=data if isinstance(data,list) else data.get("records",[])
 ids=set()
 for r in rows:
  missing=REQ-set(r)
  if missing: raise ValueError(f"missing {sorted(missing)}")
  if r["citation_id"] in ids: raise ValueError("duplicate citation_id")
  ids.add(r["citation_id"])
  if r["claim_scope"] not in SCOPES: raise ValueError("invalid claim_scope")
 return {"records":len(rows),"status":"PASS","boundary":"Bibliographic linkage is not endorsement or independent confirmation."}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("file",type=pathlib.Path);a=p.parse_args();print(json.dumps(validate(a.file)))
