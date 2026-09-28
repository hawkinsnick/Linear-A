#!/usr/bin/env python3
"""Compare two decoded SigLA corpus JSON snapshots without interpreting Linear A.

The script reports document/attestation/word-level additions, removals and changed
records. It deliberately does NOT run frozen structural candidates; prospective
outcome testing is a separate stage after this descriptive delta is frozen.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def canon(x):
    return json.dumps(x,ensure_ascii=False,sort_keys=True,separators=(",",":"))

def docmap(c):
    return {str(d["id"]):d for d in c.get("documents",[])}

def word_groups(doc):
    groups={}
    for i,a in enumerate(doc.get("attestations",[])):
        w=a.get("word")
        if w is not None:
            groups.setdefault(str(w),[]).append({"index":i,"sign":a.get("sign"),"kind":a.get("kind")})
    return groups

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("old"); ap.add_argument("current"); ap.add_argument("--out",required=True)
    ap.add_argument("--expected-current-sha256")
    a=ap.parse_args()
    if a.expected_current_sha256 and sha(a.current)!=a.expected_current_sha256:
        raise SystemExit("REFUSING RUN: current snapshot SHA-256 mismatch")
    old,new=load(a.old),load(a.current); om,nm=docmap(old),docmap(new)
    ok,nk=set(om),set(nm)
    common=sorted(ok&nk)
    changed=[k for k in common if canon(om[k])!=canon(nm[k])]
    att_old=sum(len(d.get("attestations",[])) for d in om.values())
    att_new=sum(len(d.get("attestations",[])) for d in nm.values())
    words_old=sum(len(word_groups(d)) for d in om.values())
    words_new=sum(len(word_groups(d)) for d in nm.values())
    detail=[]
    for k in changed:
        od,nd=om[k],nm[k]
        detail.append({
          "id":k,
          "attestations_old":len(od.get("attestations",[])),
          "attestations_current":len(nd.get("attestations",[])),
          "words_old":len(word_groups(od)),
          "words_current":len(word_groups(nd)),
          "metadata_changed":{f:[od.get(f),nd.get(f)] for f in
             ("typology","site","dimensions_cm","period","reference_url","image_path")
             if od.get(f)!=nd.get(f)},
          "attestation_stream_changed":canon(od.get("attestations",[]))!=canon(nd.get("attestations",[]))
        })
    result={
      "schema_version":"2.4.1",
      "old_sha256":sha(a.old),"current_sha256":sha(a.current),
      "documents":{"old":len(om),"current":len(nm),"added":sorted(nk-ok),"removed":sorted(ok-nk),"changed":changed},
      "attestations":{"old":att_old,"current":att_new,"net":att_new-att_old},
      "source_word_groups":{"old":words_old,"current":words_new,"net":words_new-words_old},
      "changed_document_details":detail,
      "candidate_outcomes_evaluated":False
    }
    Path(a.out).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
