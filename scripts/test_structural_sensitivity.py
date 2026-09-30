#!/usr/bin/env python3
"""Synthetic and exact-enumeration statistical regressions; no corpus outcomes."""
import itertools,math,json
from run_structural_sensitivity_v1 import moments,holm,view_analysis,cluster_bootstrap,analyze
seq=('A','A','B');m=moments([seq],'A','initial')
assert m['observed']==1 and abs(m['expected']-2/3)<1e-12 and abs(m['variance']-2/9)<1e-12
values=[float(p[0]=='A') for p in itertools.permutations(seq)]
assert abs(sum(values)/len(values)-m['expected'])<1e-12
assert abs(sum((x-m['expected'])**2 for x in values)/len(values)-m['variance'])<1e-12
assert moments([('A',)],'A','final')['z'] is None
assert holm([.01,.04,.03])==[.03,.06,.06]
for ps in [[-1],[float('nan')],[2]]:
    try:holm(ps)
    except ValueError:pass
    else:raise AssertionError('invalid p-value accepted')
candidates=[{'candidate_id':'A-initial','sign_id':'A','position':'initial'},{'candidate_id':'Z-final','sign_id':'Z','position':'final'}]
spec={'minimum_candidate_occurrences':1,'permutation_replicates':199,'bootstrap_replicates':99,'cluster_seed':10,'token_permutation_seed':11,'type_permutation_seed':12}
words=[('D1',('A','B'))]*10+[('D2',('B','A'))]*10
x=analyze(words,candidates,spec);assert x==analyze(words,candidates,spec)
assert x['results'][1]['token']['one_sided_permutation_p']==1 and not x['results'][1]['token']['eligible']
for row in x['results']:
    for key in ('token','type'):
        assert 0<=row[key]['one_sided_permutation_p']<=row[key]['holm_p']<=1
        assert row[key]['holm_family_size']==2
    b=row['document_cluster_bootstrap'];assert b['scorable_replicates']+b['zero_variance_replicates']==99
# Symmetric exact null: observed at expectation; no enrichment is manufactured.
m=moments([('A','B'),('B','A')],'A','initial');assert m['z']==0
# Strongly enriched synthetic case exercises real permutations and family correction.
x=view_analysis([('A','B')]*20,candidates,spec,11)
assert x[0]['one_sided_permutation_p']<=.05 and x[0]['holm_p']>=x[0]['one_sided_permutation_p']
print(json.dumps({'status':'PASS','checks':['exact repeated-sign moments','homogeneous zero-variance refusal','Holm arithmetic','invalid p refusal','seed determinism','absent-sign negative control','symmetric negative control','shared permutation output','cluster replicate accounting','synthetic enrichment sensitivity']}))
