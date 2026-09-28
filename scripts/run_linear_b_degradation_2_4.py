#!/usr/bin/env python3
"""Preregistered 2.4 degradation generator. Does not perform gold scoring."""
from __future__ import annotations
import argparse, collections, csv, hashlib, json, random
from pathlib import Path

TARGET_TOKENS=1283
MASTER_SEED=2400001
DAMAGE_LEVELS=(0.0,0.05,0.10,0.20)
REPLICATES=1000
MASK="<MASK>"

def read_words(path):
    bydoc=collections.defaultdict(list)
    with path.open(newline="",encoding="utf8") as f:
        for r in csv.DictReader(f):
            seq=tuple(r["syllable_sequence"].split())
            if seq: bydoc[r["document_id"]].append(seq)
    return bydoc

def choose_documents(bydoc,rng,target=TARGET_TOKENS):
    """Whole-document subset selection with randomized tie-breaking.

    Dynamic programming finds a reachable token total closest to target. A seeded
    shuffle randomizes document order before optimization so equal-quality subsets
    do not always privilege the same documents.
    """
    docs=list(bydoc); rng.shuffle(docs)
    # total -> tuple(document ids). Keep one seeded path for each reachable total.
    states={0:()}
    for d in docs:
        n=len(bydoc[d])
        additions={}
        for total,chosen in list(states.items()):
            nt=total+n
            if nt not in states and nt not in additions:
                additions[nt]=chosen+(d,)
        states.update(additions)
    best_total=min(states, key=lambda total:(abs(target-total), total>target, total))
    return list(states[best_total])

def mask_seq(seq,p,rng):
    masked=tuple(MASK if rng.random()<p else x for x in seq)
    return masked if any(x!=MASK for x in masked) else ()

def diagnostics(words, fully_masked_words=0):
    types=collections.Counter(words)
    return {
      "tokens_observable":len(words),"fully_masked_words":fully_masked_words,
      "types":len(types),
      "hapax_types":sum(n==1 for n in types.values()),
      "recurrent_types":sum(n>=2 for n in types.values()),
      "hapax_fraction":(sum(n==1 for n in types.values())/len(types) if types else None)
    }

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("detector_input_words",type=Path,
      help="Authenticated analysis/2.3_blind/detector_input_words.csv only")
    ap.add_argument("--baseline-manifest",type=Path,required=True,
      help="Authenticated 2.3 BLIND_RUN.json; must declare BLIND_PREDICTION_FROZEN and gold_morphology_seen=false")
    ap.add_argument("--out",type=Path,default=Path("analysis/2.4_degraded"))
    ap.add_argument("--replicates",type=int,default=REPLICATES)
    args=ap.parse_args()
    base=json.loads(args.baseline_manifest.read_text())
    if base.get("stage")!="BLIND_PREDICTION_FROZEN" or base.get("gold_morphology_seen") is not False:
        raise SystemExit("REFUSING RUN: unauthenticated or post-reveal 2.3 baseline manifest")
    bydoc=read_words(args.detector_input_words)
    args.out.mkdir(parents=True,exist_ok=True)
    summary=[]
    conditions=[]
    # Undegraded full corpus is retained as the reference distribution.
    conditions.append(("undegraded", False, 0.0))
    # Scale-only plus combined scale+damage conditions.
    for p in DAMAGE_LEVELS:
        conditions.append(("scale_only" if p == 0 else "scale_plus_damage", True, p))
    # Damage-only conditions preserve the complete document set.
    for p in DAMAGE_LEVELS[1:]:
        conditions.append(("damage_only", False, p))

    for condition_i,(condition,use_scale,p) in enumerate(conditions):
        reps = 1 if condition == "undegraded" else args.replicates
        for rep in range(reps):
            seed=MASTER_SEED + condition_i*1_000_000 + rep
            rng=random.Random(seed)
            chosen=choose_documents(bydoc,rng) if use_scale else list(bydoc)
            raw=[w for d in chosen for w in bydoc[d]]
            masked=[mask_seq(w,p,rng) for w in raw]
            fully_masked=sum(not x for x in masked)
            damaged=[x for x in masked if x]
            row={"condition":condition,"damage_rate":p,"replicate":rep,"seed":seed,
                 "documents":len(chosen),"tokens_before_masking":len(raw)}
            row.update(diagnostics(damaged,fully_masked)); summary.append(row)
    with (args.out/"DEGRADATION_DIAGNOSTICS.csv").open("w",newline="",encoding="utf8") as f:
        cw=csv.DictWriter(f,fieldnames=summary[0].keys());cw.writeheader();cw.writerows(summary)
    manifest={"stage":"DEGRADATION_CORPORA_GENERATED_NOT_SCORED","replicates":args.replicates,
      "damage_levels":DAMAGE_LEVELS,"master_seed":MASTER_SEED,
      "conditions":["undegraded","scale_only","damage_only","scale_plus_damage"],
      "gold_scoring_performed":False,
      "warning":"Generation alone is not a 2.4 calibration result."}
    (args.out/"DEGRADATION_RUN.json").write_text(json.dumps(manifest,indent=2)+"\n")
    print(json.dumps(manifest,indent=2))
if __name__=="__main__": main()
