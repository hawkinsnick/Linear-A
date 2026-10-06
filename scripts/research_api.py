#!/usr/bin/env python3
"""Read-only researcher API over committed public Linear A source layers."""
import argparse,json,pathlib,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
FILES={"documents":"research/sigla-source-documents.jsonl","source_words":"research/sigla-source-groups.jsonl","signs":"research/sigla-source-signs.jsonl"}
def rows(resource,root=ROOT):
    if resource not in FILES: raise ValueError("unsupported resource")
    with (root/FILES[resource]).open(encoding="utf-8") as f:
        for line in f:
            if line.strip(): yield json.loads(line)
def stable_id(resource,row):
    return row.get({"documents":"source_record_id","source_words":"word_id","signs":"source_sign_key"}[resource])
def query(resource,text=None,ids=None,limit=100,root=ROOT):
    wanted=set(ids or []); q=(text or "").casefold(); out=[]
    for row in rows(resource,root):
        rid=stable_id(resource,row)
        if wanted and rid not in wanted: continue
        if q and q not in json.dumps(row,ensure_ascii=False).casefold(): continue
        out.append(row)
        if len(out)>=limit: break
    return {"api_version":"1.0","resource":resource,"records":out,"provenance":{"source_file":FILES[resource],"authority":"committed public source layer"},"rights":{"license":"CC BY-NC-SA 4.0","attribution":"Preserve per-record provenance"},"warnings":["Source-reported data are not independent epigraphic verification.","Source-defined words are editorial groups, not established linguistic words."] if resource=="source_words" else ["Source-reported data are not independent epigraphic verification."]}
def main():
    p=argparse.ArgumentParser();p.add_argument("resource",choices=FILES);p.add_argument("--text");p.add_argument("--id",action="append",dest="ids");p.add_argument("--limit",type=int,default=100);p.add_argument("--jsonl",action="store_true");a=p.parse_args()
    if not 1<=a.limit<=10000: p.error("--limit must be 1..10000")
    result=query(a.resource,a.text,a.ids,a.limit)
    if a.jsonl:
        for r in result["records"]: print(json.dumps(r,ensure_ascii=False))
    else: print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
