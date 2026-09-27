#!/usr/bin/env python3
"""Fetch, decode, and normalize SigLA locally; generated upstream data stays gitignored."""
from __future__ import annotations
import argparse, hashlib, json, urllib.request
from datetime import date
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from sigla_marshal import Block, load_database

URL="https://sigla.phis.me/database.js"
LICENSE="CC BY-NC-SA 4.0"
SOURCE="SIGLA"

def scalar(v):
    return v if isinstance(v,(str,int,float)) or v is None else None

def map_items(v):
    if v==0 or not isinstance(v,Block) or len(v.fields)!=5: return
    yield from map_items(v.fields[0]); yield v.fields[1],v.fields[2]; yield from map_items(v.fields[3])

def sign_info(v):
    if not isinstance(v,Block) or len(v.fields)<4: return None
    series,num,vals,ref=v.fields[:4]
    if not isinstance(series,str) or not isinstance(num,int): return None
    values=[]
    if isinstance(vals,Block):
        for x in vals.fields:
            if isinstance(x,Block) and x.fields and isinstance(x.fields[0],str): values.append(x.fields[0])
    ref0=ref.fields[0] if isinstance(ref,Block) and ref.fields else None
    return {"sign_id":f"{series}{num:03d}","series":series,"number":num,"values":values,
            "source_reference":ref0 if isinstance(ref0,str) else None}

def label_info(v):
    if isinstance(v,Block) and len(v.fields)==2:
        inner,confidence=v.fields
        if isinstance(inner,Block) and inner.fields:
            return sign_info(inner.fields[0]), (bool(confidence) if isinstance(confidence,int) else None)
    return None,None

def normalize(path):
    db=load_database(path); data=db.get("data")
    if not isinstance(data,Block) or not data.fields: raise ValueError("unexpected SigLA data shape")
    docs=[]
    for name,wrapped in map_items(data.fields[0]):
        if not isinstance(name,str) or not isinstance(wrapped,Block) or not wrapped.fields: continue
        inner=wrapped.fields[0]
        if not isinstance(inner,Block) or not inner.fields: continue
        meta=inner.fields[0]
        if not isinstance(meta,Block): continue
        kind=scalar(meta.fields[0] if len(meta.fields)>0 else None)
        site=scalar(meta.fields[2] if len(meta.fields)>2 else None)
        period=None
        if len(meta.fields)>7 and isinstance(meta.fields[7],Block) and meta.fields[7].fields: period=scalar(meta.fields[7].fields[0])
        atts=[]; arr=inner.fields[4] if len(inner.fields)>4 else None
        if isinstance(arr,Block):
            for a in arr.fields:
                if not isinstance(a,Block) or len(a.fields)!=8: continue
                sign,confidence=label_info(a.fields[1])
                atts.append({"occurrence_index":scalar(a.fields[2]),"sign_id":sign["sign_id"] if sign else None,
                             "sign_values":sign["values"] if sign else [],"confidence":confidence,
                             "word_boundary_raw":repr(a.fields[3]),"erasure":bool(a.fields[4]),
                             "flag5":bool(a.fields[5]),"ghost":bool(a.fields[6])})
        docs.append({"document_name":name,"document_type":kind,"site":site,"period":period,"attestations":atts,
                     "source_id":SOURCE,"source_record":name,"source_url":"https://sigla.phis.me/","source_license":LICENSE})
    return docs

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--url",default=URL); ap.add_argument("--input",default="data/raw/sigla/database.js")
    ap.add_argument("--output",default="data/generated/sigla_corpus.json"); ap.add_argument("--fetch",action="store_true")
    args=ap.parse_args(); inp=Path(args.input); inp.parent.mkdir(parents=True,exist_ok=True)
    if args.fetch:
        req=urllib.request.Request(args.url,headers={"User-Agent":"Linear-A-Open-Corpus/0.3.0"})
        with urllib.request.urlopen(req,timeout=60) as r: inp.write_bytes(r.read())
    if not inp.exists(): raise SystemExit(f"Missing {inp}. Use --fetch or supply database.js.")
    payload=inp.read_bytes(); out=normalize(inp); outp=Path(args.output); outp.parent.mkdir(parents=True,exist_ok=True)
    meta={"source_id":SOURCE,"source_url":args.url,"retrieved_date":date.today().isoformat(),
          "sha256":hashlib.sha256(payload).hexdigest(),"license":LICENSE,
          "attribution":"Ester Salgarella and Simon Castellan, SigLA: The Signs of Linear A",
          "document_count":len(out),"note":"Generated locally; not a new license grant."}
    outp.write_text(json.dumps({"_meta":meta,"documents":out},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(meta,indent=2))

if __name__=="__main__": main()
