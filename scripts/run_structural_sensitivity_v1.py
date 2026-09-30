#!/usr/bin/env python3
"""Pinned, conditional structural sensitivity repair; not prospective inference."""
from __future__ import annotations
import argparse,csv,hashlib,json,math,random,statistics
from collections import Counter,defaultdict
from pathlib import Path

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def holm(ps):
    if any(not math.isfinite(p) or not 0<=p<=1 for p in ps):raise ValueError('invalid p-value')
    out=[0.0]*len(ps);previous=0.0
    for rank,i in enumerate(sorted(range(len(ps)),key=lambda i:ps[i])):
        previous=max(previous,min(1.0,(len(ps)-rank)*ps[i]));out[i]=previous
    return out

def moments(words,sign,position):
    if position not in ('initial','final'):raise ValueError('invalid position')
    observed=expected=variance=0.0;occurrences=0
    for sequence in words:
        if not sequence:raise ValueError('empty sequence')
        k=sequence.count(sign);p=k/len(sequence);occurrences+=k
        observed+=sequence[0 if position=='initial' else -1]==sign
        expected+=p;variance+=p*(1-p)
    return {'observed':int(observed),'expected':expected,'variance':variance,'occurrences':occurrences,'z':(observed-expected)/math.sqrt(variance) if variance>0 else None}

def percentile(xs,p):
    if not xs:return None
    return sorted(xs)[max(0,math.ceil(p*len(xs))-1)]

def load_inputs(words_path,candidates_path):
    words=[];ids=set()
    with open(words_path,newline='',encoding='utf-8') as f:
        reader=csv.DictReader(f)
        if not {'word_id','document_id','sign_sequence'}<=set(reader.fieldnames or []):raise ValueError('word columns missing')
        for row in reader:
            if not row['word_id'] or row['word_id'] in ids or not row['document_id']:raise ValueError('word identity invalid')
            ids.add(row['word_id']);seq=tuple(row['sign_sequence'].split())
            if seq:words.append((row['document_id'],seq))
    with open(candidates_path,newline='',encoding='utf-8') as f:candidates=list(csv.DictReader(f))
    if not words or not candidates:raise ValueError('empty analysis input')
    if len({c['candidate_id'] for c in candidates})!=len(candidates):raise ValueError('duplicate candidate')
    if len({(c['sign_id'],c['position']) for c in candidates})!=len(candidates):raise ValueError('duplicate sign/position')
    if any(c['position'] not in ('initial','final') for c in candidates):raise ValueError('invalid position')
    return words,candidates

def view_analysis(sequences,candidates,spec,seed):
    ms=[moments(sequences,c['sign_id'],c['position']) for c in candidates];rng=random.Random(seed)
    threshold=spec['minimum_candidate_occurrences'];eligible=[m['occurrences']>=threshold and m['variance']>0 for m in ms]
    hits=[0]*len(candidates);lookup=defaultdict(list)
    for i,c in enumerate(candidates):lookup[(c['sign_id'],c['position'])].append(i)
    reps=spec['permutation_replicates']
    for _ in range(reps):
        observed=[0]*len(candidates)
        for seq in sequences:
            # Ordered draws without replacement give exactly the initial/final
            # marginal of a uniform permutation, including repeated sign labels.
            a,b=rng.sample(range(len(seq)),2) if len(seq)>1 else (0,0)
            for i in lookup[(seq[a],'initial')]:observed[i]+=1
            for i in lookup[(seq[b],'final')]:observed[i]+=1
        for i,m in enumerate(ms):
            if eligible[i] and observed[i]>=m['observed']:hits[i]+=1
    ps=[(hits[i]+1)/(reps+1) if eligible[i] else 1.0 for i in range(len(ms))];adjusted=holm(ps)
    return [{**m,'eligible':eligible[i],'one_sided_permutation_p':ps[i],'holm_p':adjusted[i],'holm_family_size':len(candidates),'monte_carlo_exceedances':hits[i] if eligible[i] else None,'eligibility_reason':'PASS' if eligible[i] else 'MINIMUM_OCCURRENCES_OR_ZERO_VARIANCE'} for i,m in enumerate(ms)]

def cluster_bootstrap(words,candidates,spec):
    groups=defaultdict(list)
    for doc,seq in words:groups[doc].append(seq)
    ids=sorted(groups);mom={doc:[moments(groups[doc],c['sign_id'],c['position']) for c in candidates] for doc in ids}
    rng=random.Random(spec['cluster_seed']);values=[[] for c in candidates];missing=[0]*len(candidates)
    for _ in range(spec['bootstrap_replicates']):
        weights=Counter(rng.choice(ids) for _ in ids)
        for i in range(len(candidates)):
            obs=sum(weight*mom[d][i]['observed'] for d,weight in weights.items());mu=sum(weight*mom[d][i]['expected'] for d,weight in weights.items());var=sum(weight*mom[d][i]['variance'] for d,weight in weights.items())
            if var>0:values[i].append((obs-mu)/math.sqrt(var))
            else:missing[i]+=1
    return [{'p025_z':percentile(v,.025),'median_z':statistics.median(v) if v else None,'p975_z':percentile(v,.975),'scorable_replicates':len(v),'zero_variance_replicates':missing[i]} for i,v in enumerate(values)]

def analyze(words,candidates,spec):
    token=[seq for _,seq in words];types=sorted(set(token))
    tv=view_analysis(token,candidates,spec,spec['token_permutation_seed']);uv=view_analysis(types,candidates,spec,spec['type_permutation_seed']);boot=cluster_bootstrap(words,candidates,spec)
    return {'word_tokens':len(token),'word_types':len(types),'documents':len({d for d,_ in words}),'results':[{'candidate_id':c['candidate_id'],'sign_id':c['sign_id'],'position':c['position'],'token':tv[i],'type':uv[i],'document_cluster_bootstrap':boot[i]} for i,c in enumerate(candidates)]}

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--spec',type=Path,required=True);ap.add_argument('--words',type=Path,required=True);ap.add_argument('--candidates',type=Path,required=True);ap.add_argument('--out',type=Path,required=True);a=ap.parse_args()
    spec=json.loads(a.spec.read_text())
    if spec['protocol_id']!='structural-sensitivity-repair-v1':raise SystemExit('REFUSING: unknown protocol')
    for p,key in ((a.words,'words_sha256'),(a.candidates,'candidates_sha256')):
        if digest(p)!=spec[key]:raise SystemExit('REFUSING: pinned input digest mismatch')
    if digest(__file__)!=spec['implementation_sha256']:raise SystemExit('REFUSING: pinned implementation digest mismatch')
    if spec['permutation_replicates']!=5000 or spec['bootstrap_replicates']!=5000:raise SystemExit('REFUSING: altered repetition policy')
    words,candidates=load_inputs(a.words,a.candidates)
    if len(candidates)!=12:raise SystemExit('REFUSING: candidate family changed')
    result=analyze(words,candidates,spec)
    result.update({'protocol_id':spec['protocol_id'],'protocol_sha256':digest(a.spec),'implementation_sha256':digest(__file__),'words_sha256':digest(a.words),'candidates_sha256':digest(a.candidates),'permutation_replicates':5000,'bootstrap_replicates':5000,'prospective_outcomes_evaluated':False,'linguistic_claim_allowed':False,'interpretation':spec['interpretation']})
    a.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
if __name__=='__main__':main()
