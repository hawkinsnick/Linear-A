#!/usr/bin/env python3
"""Reproducible descriptive queries over source-defined SigLA groups."""
import argparse,collections,json,pathlib,re,math
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows
def docs(): return {r["source_record_id"]:r for r in rows("documents")}
def groups(): return list(rows("source_words"))
def token(att):
 for k in ("display","value","sign","sign_key","number"):
  if k in att and att[k] not in (None,""): return str(att[k])
 return "?"
def sequences():
 d=docs();out=[]
 for g in groups():
  dr=d.get(g["document_id"],{});atts=dr.get("source_fields",{}).get("attestations",[])
  seq=[token(atts[i]) if isinstance(i,int) and i<len(atts) else "?" for i in g["occurrence_indices"]]
  out.append({"word_id":g["word_id"],"document_id":g["document_id"],"sequence":seq})
 return out
def stats():
 s=sequences();lens=collections.Counter(len(x["sequence"]) for x in s);tok=collections.Counter(t for x in s for t in x["sequence"])
 return {"groups":len(s),"group_length_frequency":dict(sorted(lens.items())),"token_frequency":tok.most_common(),"boundary":"Source-defined groups are editorial units; tokens are source display fields, not established phonemes or words."}
def kwic(needle,window=2):
 out=[]
 for x in sequences():
  for i,t in enumerate(x["sequence"]):
   if t==needle: out.append({"word_id":x["word_id"],"document_id":x["document_id"],"left":x["sequence"][max(0,i-window):i],"match":t,"right":x["sequence"][i+1:i+1+window]})
 return out
def collocations(window=1):
 c=collections.Counter();freq=collections.Counter();n=0
 for x in sequences():
  s=x["sequence"];n+=len(s);freq.update(s)
  for i,a in enumerate(s):
   for j in range(i+1,min(len(s),i+window+1)): c[(a,s[j])]+=1
 return [{"a":a,"b":b,"count":v} for (a,b),v in c.most_common()]
def form_families(max_distance=1):
 seq=sequences();buckets=collections.defaultdict(list)
 for x in seq:buckets[len(x["sequence"])].append(x)
 pairs=[]
 for L,b in buckets.items():
  for i,a in enumerate(b):
   for b2 in b[i+1:]:
    d=sum(x!=y for x,y in zip(a["sequence"],b2["sequence"]))
    if d<=max_distance:pairs.append({"a":a["word_id"],"b":b2["word_id"],"distance":d,"length":L})
 return pairs
def pattern(rx):
 r=re.compile(rx,re.I);return [x for x in sequences() if r.search(" ".join(x["sequence"])) or r.search(x["document_id"])]
def main():
 p=argparse.ArgumentParser();g=p.add_mutually_exclusive_group();g.add_argument("--stats",action="store_true");g.add_argument("--pattern");g.add_argument("--kwic");g.add_argument("--collocations",action="store_true");g.add_argument("--form-families",action="store_true");p.add_argument("--window",type=int,default=2);p.add_argument("--max-distance",type=int,default=1);a=p.parse_args()
 if a.kwic is not None:o={"records":kwic(a.kwic,a.window)}
 elif a.collocations:o={"records":collocations(a.window)}
 elif a.form_families:o={"records":form_families(a.max_distance),"warning":"Form similarity is not morphology, etymology or semantics."}
 elif a.pattern:o={"records":pattern(a.pattern)}
 else:o=stats()
 o["method_boundary"]="All sequence operations use source-defined groups and source display fields. Graphotactic/statistical pattern is not phonotactics, morphology, language identification or decipherment."
 print(json.dumps(o,ensure_ascii=False,indent=2))
if __name__=="__main__":main()
