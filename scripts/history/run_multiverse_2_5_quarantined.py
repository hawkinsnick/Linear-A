#!/usr/bin/env python3
"""2.5 structural multiverse for the 12 frozen sign/position candidates."""
from __future__ import annotations
import argparse,csv,json,math,random,statistics
from collections import Counter,defaultdict
from pathlib import Path

def read_words(p):
 out=[]
 with open(p,encoding="utf-8",newline="") as f:
  for r in csv.DictReader(f):
   seq=tuple(x for x in r["sign_sequence"].split() if x)
   if seq: out.append((r["document_id"],seq))
 return out
def read_candidates(p):
 with open(p,encoding="utf-8",newline="") as f:return [(r["sign_id"],r["position"]) for r in csv.DictReader(f)]
def zscore(words,s,pos):
 W=len(words); total=sum(sum(x==s for x in seq) for _,seq in words)
 if not W or not total:return 0.0
 obs=sum(seq[0 if pos=="initial" else -1]==s for _,seq in words)
 p=1.0/W*sum(1/len(seq) for _,seq in words) * W # mean chance per occurrence under uniform within-word position
 exp=total*p
 var=max(total*p*(1-p),1e-12)
 return (obs-exp)/math.sqrt(var)
def holm(ps):
 order=sorted(range(len(ps)),key=lambda i:ps[i]); out=[0.0]*len(ps); prev=0.0;m=len(ps)
 for rank,i in enumerate(order):
  v=min(1.0,(m-rank)*ps[i]);prev=max(prev,v);out[i]=prev
 return out
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--words",default="data/source_words.csv");ap.add_argument("--candidates",default="data/candidate_registry_0.9.csv");ap.add_argument("--out",required=True);ap.add_argument("--reps",type=int,default=5000);a=ap.parse_args()
 words=read_words(a.words);cands=read_candidates(a.candidates); docs=defaultdict(list)
 for d,s in words:docs[d].append((d,s))
 unique=[("TYPE",s) for s in sorted({s for _,s in words})]
 rng=random.Random(2500001);docids=sorted(docs)
 rows=[]
 for sign,pos in cands:
  full=zscore(words,sign,pos);typ=zscore(unique,sign,pos);zs=[]
  for _ in range(a.reps):
   sample=[]
   for d in (rng.choice(docids) for __ in docids):sample.extend(docs[d])
   zs.append(zscore(sample,sign,pos))
  zs.sort();lo=zs[int(.025*(len(zs)-1))];med=statistics.median(zs);hi=zs[int(.975*(len(zs)-1))]
  rows.append({"sign_id":sign,"position":pos,"token_z":full,"type_z":typ,"cluster_p025_z":lo,"cluster_median_z":med,"cluster_p975_z":hi,"cluster_lower_gt_1_96":lo>1.96})
 result={"version":"2.5.0","word_tokens":len(words),"unique_types":len(unique),"documents":len(docids),"bootstrap_replicates":a.reps,"seed":2500001,"results":rows,"interpretation":"structural robustness; not morphology"}
 Path(a.out).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__":main()
