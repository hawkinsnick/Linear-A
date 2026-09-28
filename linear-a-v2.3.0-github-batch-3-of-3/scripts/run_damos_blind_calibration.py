#!/usr/bin/env python3
"""Frozen DĀMOS-v2 blind calibration gate for Linear A Open Corpus 2.3.

Stage 1 intentionally sees only the pyaegean DĀMOS-v2 derivative fields, especially
`content`. It does not consume DĀMOS morphology/syntax annotations.

This runner is deliberately conservative: it validates the exact frozen asset and
creates a detector-facing corpus plus frozen structural predictions. Gold linguistic
scoring is a separate stage and must use a separately acquired/declared annotation
source; the derivative itself does not contain the full manually annotated morphology.
"""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, math, random, re
from pathlib import Path

EXPECTED_SHA256="eab9ccdfc4324b62f015bccd5e3f917f256cab8c058840842127eadecfbca2d2"

# Conservative Linear-B transliteration tokenization. Editorial/numerical/ideogram
# material is retained in the raw export but excluded from the word-form detector.
WORD_RE=re.compile(r"(?<![A-Za-z0-9*])(?:[a-z][a-z0-9]*(?:-[a-z0-9]+)+)(?![A-Za-z0-9])",re.I)

def sha256(p:Path)->str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1<<20),b""): h.update(b)
    return h.hexdigest()

def syllables(form:str):
    return tuple(x.lower() for x in form.split("-") if x)

def extract_words(doc):
    # Stage-1 observable only. Do not import linguistic labels here.
    content=doc.get("content") or ""
    return [m.group(0) for m in WORD_RE.finditer(content)]

def z_boundary(types, sign, pos):
    obs=mu=var=0.0
    for t in types:
        k=t.count(sign)
        if not k: continue
        p=k/len(t); mu+=p; var+=p*(1-p)
        obs += (t[0] if pos=="initial" else t[-1])==sign
    return (obs-mu)/math.sqrt(var) if var else 0.0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("damos_json",type=Path)
    ap.add_argument("--out",type=Path,default=Path("analysis/2.3_blind"))
    args=ap.parse_args()
    got=sha256(args.damos_json)
    if got != EXPECTED_SHA256:
        raise SystemExit(f"REFUSING RUN: SHA256 {got} != frozen DĀMOS-v2 {EXPECTED_SHA256}")
    obj=json.loads(args.damos_json.read_text(encoding="utf8"))
    docs=obj["documents"]
    args.out.mkdir(parents=True,exist_ok=True)

    rows=[]; bydoc=collections.defaultdict(list)
    for d in docs:
        for i,w in enumerate(extract_words(d)):
            s=syllables(w)
            if len(s)>=1:
                did=str(d.get("id"))
                rows.append((did,i,w," ".join(s)))
                bydoc[did].append(s)
    with (args.out/"detector_input_words.csv").open("w",newline="",encoding="utf8") as f:
        cw=csv.writer(f); cw.writerow(["document_id","token_index","surface_form","syllable_sequence"]); cw.writerows(rows)

    types=set(s for ws in bydoc.values() for s in ws)
    counts=collections.Counter(x for t in types for x in t)
    # Freeze broad positional screen without consulting morphology.
    pred=[]
    for sign,n in sorted(counts.items()):
        if n<8: continue
        for pos in ("initial","final"):
            z=z_boundary(types,sign,pos)
            pred.append({"sign":sign,"position":pos,"type_occurrences":n,"z":z,"screen_z_gt_1_96":z>1.96})
    with (args.out/"FROZEN_PREDICTIONS.csv").open("w",newline="",encoding="utf8") as f:
        cw=csv.DictWriter(f,fieldnames=pred[0].keys() if pred else ["sign","position","type_occurrences","z","screen_z_gt_1_96"])
        cw.writeheader(); cw.writerows(pred)

    # Edge deletion graph on syllable sequences.
    edge=0
    for t in types:
        if len(t)>=2:
            edge += t[1:] in types
            edge += t[:-1] in types

    manifest={
      "stage":"BLIND_PREDICTION_FROZEN",
      "input_sha256":got,
      "documents":len(docs),
      "documents_with_detector_words":sum(bool(x) for x in bydoc.values()),
      "word_tokens":len(rows),
      "word_types":len(types),
      "positional_predictions":len(pred),
      "positive_z_screens":sum(x["screen_z_gt_1_96"] for x in pred),
      "directed_edge_removal_relations":edge,
      "gold_morphology_seen":False,
      "warning":"These are structural predictions, not morphology claims. Do not tune after gold reveal."
    }
    (args.out/"BLIND_RUN.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest,indent=2))

if __name__=="__main__": main()
