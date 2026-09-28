#!/usr/bin/env python3
"""Validate 2.4.2 witness assertions and summarize evidential lineage support."""
from __future__ import annotations
import argparse, collections, json
from pathlib import Path

def rows(path):
    out=[]
    for n,line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(),1):
        if line.strip():
            x=json.loads(line); x["_line"]=n; out.append(x)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("assertions")
    ap.add_argument("--out")
    a=ap.parse_args()
    xs=rows(a.assertions)
    ids=[x["assertion_id"] for x in xs]
    if len(ids)!=len(set(ids)): raise SystemExit("REFUSING RUN: duplicate assertion_id")
    groups=collections.defaultdict(list)
    for x in xs:
        key=(x["canonical_document_id"],x.get("locus"),x["assertion_type"],json.dumps(x["value"],sort_keys=True,ensure_ascii=False))
        groups[key].append(x)
    summary=[]
    for key,g in sorted(groups.items(),key=lambda kv:repr(kv[0])):
        lineages=sorted({x["lineage_id"] for x in g})
        sources=sorted({x["source_id"] for x in g})
        summary.append({
          "canonical_document_id":key[0],"locus":key[1],"assertion_type":key[2],
          "value":json.loads(key[3]),"source_count":len(sources),"sources":sources,
          "lineage_count":len(lineages),"lineages":lineages
        })
    result={"schema_version":"2.4.2","assertions":len(xs),"support_groups":summary,
            "rule":"evidential support count is distinct lineage_count, never raw source_count"}
    text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if a.out: Path(a.out).write_text(text,encoding="utf-8")
    else: print(text,end="")
if __name__=="__main__": main()
