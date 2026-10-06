#!/usr/bin/env python3
import json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"scripts"))
import research_api
for resource in research_api.FILES:
    r=research_api.query(resource,limit=2)
    assert r["api_version"]=="1.0" and r["resource"]==resource and len(r["records"])<=2
    assert r["rights"]["license"]=="CC BY-NC-SA 4.0"
    if r["records"]:
        rid=research_api.stable_id(resource,r["records"][0]); one=research_api.query(resource,ids=[rid],limit=10)
        assert len(one["records"])==1 and research_api.stable_id(resource,one["records"][0])==rid
print("research API smoke tests passed")
