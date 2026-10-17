#!/usr/bin/env python3
"""Loss-aware exports from committed public source layers."""
import argparse,csv,json,pathlib,hashlib
from urllib.parse import quote
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows, FILES
def sid(r): return r.get("source_record_id") or r.get("word_id") or r.get("source_sign_key")
def digest(path):
 return hashlib.sha256(path.read_bytes()).hexdigest()
def manifest(fmt,resource,count,losses):
 source=ROOT/FILES[resource]
 audit=json.loads((ROOT/"analysis/public-sigla-layer-audit.json").read_text(encoding="utf-8"))
 expected=next(x for x in audit["files"] if x["path"]==FILES[resource])
 if digest(source)!=expected["sha256"]: raise ValueError("Source checksum mismatch")
 return {"format":"linear-a-export-manifest-v2","export_format":fmt,
 "source_snapshot":{"path":FILES[resource],"sha256":expected["sha256"],"upstream_input_sha256":audit["input_sha256"],"upstream_release":audit["upstream_release"]},
 "generator":{"path":"scripts/export_research_layer.py","sha256":digest(pathlib.Path(__file__)),"dependencies":[{"path":"scripts/research_api.py","sha256":digest(ROOT/"scripts/research_api.py")}]},
 "included_resources":[resource],"record_count":count,"losses":losses,
 "rights_summary":"CC BY-NC-SA 4.0; preserve per-record attribution/provenance",
 "epistemic_status":"SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED",
 "warnings":["Source-defined words are editorial groups, not established linguistic words.","Sign labels do not establish Linear A phonetic values or decipherment.","No object-level expert acceptance or independent-source validation is established."],
 "generator_version":"research-readiness-v1"}
def write_export(resource,fmt,out):
 # Verify source bytes before exporting; bind the resulting bytes as well.
 manifest(fmt,resource,0,[])
 fn={"json":export_json,"csv":export_csv,"jsonld":export_jsonld,"epidoc":export_epidoc}[fmt]
 result=fn(resource,out)
 result["output"]={"name":out.name,"sha256":digest(out),"bytes":out.stat().st_size}
 out.with_suffix(out.suffix+".manifest.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 return result
def export_json(resource,out):
 data=list(rows(resource));out.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8");return manifest("JSON",resource,len(data),[])
def export_csv(resource,out):
 data=list(rows(resource))
 with out.open("w",encoding="utf-8",newline="") as f:
  w=csv.DictWriter(f,fieldnames=["stable_id","record_json"]);w.writeheader()
  for r in data:w.writerow({"stable_id":sid(r),"record_json":json.dumps(r,ensure_ascii=False,separators=(",",":"))})
 return manifest("CSV",resource,len(data),["Nested semantics are serialized in record_json rather than normalized columns."])
def export_jsonld(resource,out):
 data=list(rows(resource));graph=[]
 for r in data:
  graph.append({"@id":"urn:linear-a:"+resource+"/"+quote(str(sid(r)),safe=""),"@type":"https://schema.org/CreativeWork","resource":resource,"stableId":sid(r),"record":r})
 obj={"@context":{"stableId":"https://schema.org/identifier","resource":"https://schema.org/additionalType","record":"https://schema.org/subjectOf"},"@graph":graph}
 out.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 return manifest("JSON-LD",resource,len(data),["Project-specific semantics remain nested in record; no external ontology equivalence is asserted."])
def export_epidoc(resource,out):
 import xml.etree.ElementTree as ET
 root=ET.Element("TEI",{"xmlns":"http://www.tei-c.org/ns/1.0"});text=ET.SubElement(root,"text");body=ET.SubElement(text,"body")
 for r in rows(resource):
  div=ET.SubElement(body,"div",{"type":"linearARecord","n":str(sid(r))});ET.SubElement(div,"idno").text=str(sid(r));note=ET.SubElement(div,"note",{"type":"sourceRecordJSON"});note.text=json.dumps(r,ensure_ascii=False,separators=(",",":"))
 data=ET.tostring(root,encoding="unicode");out.write_text('<?xml version="1.0" encoding="UTF-8"?>\n'+data+"\n",encoding="utf-8")
 count=sum(1 for _ in rows(resource))
 return manifest("EpiDoc-compatible TEI XML",resource,count,["Project-specific competing assertions/layout semantics are preserved as sourceRecordJSON, not fully mapped to EpiDoc elements."])
def main():
 p=argparse.ArgumentParser();p.add_argument("resource",choices=["documents","source_words","signs"]);p.add_argument("format",choices=["json","csv","jsonld","epidoc"]);p.add_argument("output",type=pathlib.Path);a=p.parse_args()
 print(json.dumps(write_export(a.resource,a.format,a.output)))
if __name__=="__main__":main()
