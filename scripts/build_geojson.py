#!/usr/bin/env python3
"""Validate provenance-aware geospatial records and emit GeoJSON."""
import argparse,json,pathlib
REQ={"geo_id","label","entity_type","latitude","longitude","coordinate_uncertainty_m","geometry_source","source_locator","certainty","rights_status","linked_document_ids"}
def convert(path):
 rows=json.loads(path.read_text());features=[]
 for r in rows:
  miss=REQ-set(r)
  if miss: raise ValueError(f"missing {sorted(miss)}")
  lat,lon=float(r["latitude"]),float(r["longitude"])
  if not(-90<=lat<=90 and -180<=lon<=180): raise ValueError("invalid coordinate")
  props={k:v for k,v in r.items() if k not in ("latitude","longitude")}
  features.append({"type":"Feature","id":r["geo_id"],"geometry":{"type":"Point","coordinates":[lon,lat]},"properties":props})
 return {"type":"FeatureCollection","features":features,"boundary":"Coordinates are attributed assertions with explicit uncertainty, not excavation-level precision unless source states so."}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("file",type=pathlib.Path);p.add_argument("--output",type=pathlib.Path);a=p.parse_args();g=convert(a.file);s=json.dumps(g,ensure_ascii=False,indent=2)+"\n";a.output.write_text(s) if a.output else print(s,end="")
