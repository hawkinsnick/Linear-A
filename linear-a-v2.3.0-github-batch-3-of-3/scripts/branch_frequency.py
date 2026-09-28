#!/usr/bin/env python3
"""Branch-aware frequency runner for Linear A Open Corpus.
Input CSV must contain document_id and sign_id. Optional certainty column.
A branch file can replace one scoped observation for sensitivity runs.
"""
import argparse,csv,json,collections
def load(path):
    with open(path,encoding="utf-8") as f:return list(csv.DictReader(f))
def main():
    p=argparse.ArgumentParser()
    p.add_argument("observations")
    p.add_argument("--certainty",choices=["all","confident"],default="all")
    p.add_argument("--output",default="frequency_result.json")
    a=p.parse_args()
    rows=load(a.observations)
    if a.certainty=="confident":
        rows=[r for r in rows if r.get("certainty","").lower() in ("confident","certain","1","true")]
    c=collections.Counter(r["sign_id"] for r in rows if r.get("sign_id"))
    result={"analysis":"sign_frequency","certainty_filter":a.certainty,"n":sum(c.values()),
            "unique_signs":len(c),"counts":dict(sorted(c.items()))}
    with open(a.output,"w",encoding="utf-8") as f:json.dump(result,f,indent=2)
if __name__=="__main__":main()
