#!/usr/bin/env python3
"""Loss-aware exports from committed public source layers."""
import argparse,csv,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows
def sid(r): return r.get("source_record_id") or r.get("word_id") or r.get("source_sign_key")
def manifest(fmt,resource,count,losses):
 return {"format":"linear-a-export-manifest-v1","export_format":fmt,"source_snapshot":"committed public SigLA source layer","included_resources":[resource],"record_count":count,"losses":losses,"rights_summary":"CC BY-NC-SA 4.0; preserve per-record attribution/provenance","generator_version":"3.0.19"}
def export_json(resource,out):
 data=list(rows(resource));out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n");return manifest("JSON",resource,len(data),[])
def export_csv(resource,out):
 data=list(rows(resource))
 with out.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["stable_id","record_json"]);w.writeheader()
  for r in data:w.writerow({"stable_id":sid(r),"record_json":json.dumps(r,ensure_ascii=False,separators=(",",":"))})
 return manifest("CSV",resource,len(data),["Nested semantics are serialized in record_json rather than normalized columns."])
def export_jsonld(resource,out):
 data=list(rows(resource));graph=[]
 for r in data:
  graph.append({"@id":"https://example.invalid/linear-a/"+resource+"/"+str(sid(r)).replace(" ","%20"),"@type":"LinearARecord","resource":resource,"stableId":sid(r),"record":r})
 obj={"@context":{"stableId":"https://schema.org/identifier","resource":"https://schema.org/additionalType","record":"https://schema.org/subjectOf"},"@graph":graph}
 out.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n")
 return manifest("JSON-LD",resource,len(data),["Project-specific semantics remain nested in record; no external ontology equivalence is asserted."])
def export_epidoc(resource,out):
 import xml.etree.ElementTree as ET
 root=ET.Element("TEI",{"xmlns":"http://www.tei-c.org/ns/1.0"});text=ET.SubElement(root,"text");body=ET.SubElement(text,"body")
 for r in rows(resource):
  div=ET.SubElement(body,"div",{"type":"linearARecord","n":str(sid(r))});ET.SubElement(div,"idno").text=str(sid(r));note=ET.SubElement(div,"note",{"type":"sourceRecordJSON"});note.text=json.dumps(r,ensure_ascii=False,separators=(",",":"))
 data=ET.tostring(root,encoding="unicode");out.write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+data+"\n")
 count=sum(1 for _ in rows(resource))
 return manifest("EpiDoc-compatible TEI XML",resource,count,["Project-specific competing assertions/layout semantics are preserved as sourceRecordJSON, not fully mapped to EpiDoc elements."])
def main():
 p=argparse.ArgumentParser();p.add_argument("resource",choices=["documents","source_words","signs"]);p.add_argument("format",choices=["json","csv","jsonld","epidoc"]);p.add_argument("output",type=pathlib.Path);a=p.parse_args()
 fn={"json":export_json,"csv":export_csv,"jsonld":export_jsonld,"epidoc":export_epidoc}[a.format];m=fn(a.resource,a.output)
 a.output.with_suffix(a.output.suffix+".manifest.json").write_text(json.dumps(m,indent=2)+"\n");print(json.dumps(m))
if __name__=="__main__":main()
