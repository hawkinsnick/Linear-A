#!/usr/bin/env python3
"""Loss-aware exports from committed public source layers."""
import argparse,csv,json,pathlib,sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows
def manifest(fmt,resource,count,losses):
 return {"format":"linear-a-export-manifest-v1","export_format":fmt,"source_snapshot":"committed public SigLA source layer","included_resources":[resource],"record_count":count,"losses":losses,"rights_summary":"CC BY-NC-SA 4.0; preserve per-record attribution/provenance","generator_version":"3.0.18"}
def export_json(resource,out):
 data=list(rows(resource));out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n");return manifest("JSON",resource,len(data),[])
def export_csv(resource,out):
 data=list(rows(resource)); flat=[]
 for r in data: flat.append({"stable_id":r.get("source_record_id") or r.get("word_id") or r.get("source_sign_key"),"record_json":json.dumps(r,ensure_ascii=False,separators=(",",":"))})
 with out.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["stable_id","record_json"]);w.writeheader();w.writerows(flat)
 return manifest("CSV",resource,len(data),["Nested semantics are serialized in record_json rather than normalized columns."])
def main():
 p=argparse.ArgumentParser();p.add_argument("resource",choices=["documents","source_words","signs"]);p.add_argument("format",choices=["json","csv"]);p.add_argument("output",type=pathlib.Path);a=p.parse_args()
 m=export_json(a.resource,a.output) if a.format=="json" else export_csv(a.resource,a.output)
 a.output.with_suffix(a.output.suffix+".manifest.json").write_text(json.dumps(m,indent=2)+"\n")
 print(json.dumps(m))
if __name__=="__main__":main()
