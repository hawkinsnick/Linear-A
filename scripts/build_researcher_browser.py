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
    idx=write_browser();print("wrote browser with",len(idx["records"]),"records")
if __name__=="__main__":main()

def html(index):
    payload=json.dumps(index,ensure_ascii=False,separators=(",",":")).replace("<","\\u003c").replace("&","\\u0026")
    return """<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>Linear A researcher browser</title>
<style>body{font:16px system-ui;max-width:1200px;margin:auto;padding:24px;background:#f6f4ed;color:#18302d}input,select{font:inherit;padding:10px;margin:6px}table{width:100%;border-collapse:collapse;background:white}th,td{padding:9px;border-bottom:1px solid #ddd;text-align:left;vertical-align:top}th{position:sticky;top:0;background:#e8efea}.notice{padding:14px;background:#fff2d8;border-left:4px solid #a87920}.scroll{overflow:auto;max-height:70vh}</style>
<h1>Linear A researcher browser</h1><p class="notice">Source-reported searchable evidence. This browser does not establish decipherment, linguistic wordhood, source independence or expert epigraphic verification.</p>
<label>Search <input id="q" type="search" placeholder="document, sign, site, source field"></label><label>Resource <select id="r"><option value="">All</option><option>documents</option><option>source_words</option><option>signs</option></select></label><p id="n"></p><div class="scroll"><table><thead><tr><th>ID</th><th>Resource</th><th>Summary</th><th>Rights</th></tr></thead><tbody id="rows"></tbody></table></div>
<script id="data" type="application/json">"""+payload+"""</script><script>'use strict';const D=JSON.parse(document.getElementById('data').textContent),$=x=>document.getElementById(x);function draw(){let q=$('q').value.toLowerCase(),r=$('r').value,a=D.records.filter(x=>(!r||x.resource===r)&&(!q||JSON.stringify(x).toLowerCase().includes(q)));$('rows').replaceChildren();for(const x of a.slice(0,1000)){let tr=document.createElement('tr');for(const v of [x.id,x.resource,JSON.stringify(x),x.rights||'see source record']){let td=document.createElement('td');td.textContent=v;tr.append(td)}$('rows').append(tr)}$('n').textContent=a.length+' matches'+(a.length>1000?' (first 1000 shown)':'')}$('q').oninput=draw;$('r').onchange=draw;draw();</script>"""
def write_browser(root=ROOT):
    idx=build(root)
    (root/"analysis/researcher-browser-index.json").write_text(json.dumps(idx,ensure_ascii=False,separators=(",",":"))+"\n")
    (root/"workbench/linear-a-browser.html").write_text(html(idx))
    return idx
