#!/usr/bin/env python3
"""Federate registered native evidence without merging populations or authority."""
import argparse
import copy
import io
import json
from pathlib import Path
import sys
import zipfile

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import research_delivery as native


def members(checkouts):
    checkouts=Path(checkouts).resolve()
    registry=json.loads((ROOT/'combined-ai-skill/registry/corpus-projects.json').read_bytes())['members']
    seen=set();out=[]
    for member in registry:
        repo=member['repository']
        if repo in seen or repo in ('hawkinsnick/LightroomIsSlow','hawkinsnick/Egyptian-Hieroglyphic-Corpus'):
            raise ValueError('duplicate or excluded member')
        seen.add(repo);root=checkouts/repo.split('/')[-1]
        # Shared adapter must be the exact tested implementation, not guessed compatibility.
        for path in ('scripts/evidence_query.py','scripts/research_delivery.py'):
            if native.sha(native.local(root,path).read_bytes())!=native.sha((ROOT/path).read_bytes()):
                raise ValueError('native adapter version mismatch: '+repo+' '+path)
        report=native.check(root)
        if report['repository']!=repo: raise ValueError('member identity mismatch')
        out.append((repo,root,report))
    return out


def audit(checkouts):
    results=[]
    for repo,root,r in members(checkouts):
        results.append({'repository':repo,'delivery_report_sha256':native.sha((root/native.REPORT).read_bytes()),
                        'profile_sha256':native.sha((root/'research/evidence-query-profile.json').read_bytes()),
                        'collections':r['collections'],'scholarly_limits':r['scholarly_limits'],
                        'delivery_status':r['status'], 'expert_acceptance_added':False})
    return {'format':'federated-research-readiness-v1','members':results,
            'scope':'Selected public native evidence views of all registered language members.',
            'all_scholarly_p0_p1_closed':False, 'expert_acceptance_added':False,
            'model_behavior_empirically_validated':False,'unique_object_count':None,
            'boundary':native.BOUNDARY}


def query(checkouts,text='',identity=None,repository=None,collection=None,limit=20):
    if not 1<=limit<=1000:raise ValueError('limit must be 1..1000')
    available=members(checkouts)
    if repository and repository not in {r for r,_,_ in available}:raise ValueError('unknown repository')
    results=[];counts=[]
    for repo,root,_ in available:
        if repository and repo!=repository:continue
        e=native.Evidence(root)
        if collection and collection not in e.collections:
            if repository:raise ValueError('unknown collection')
            continue
        for name,c in e.collections.items():
            if collection and name!=collection:continue
            matched=0
            for row in c['records']:
                if identity is not None and row['id']!=identity:continue
                if text.casefold() not in json.dumps(row['value'],ensure_ascii=False).casefold():continue
                matched+=1
                if len(results)<limit:
                    results.append({'key':[repo,name,row['id']], 'native_unit':c['spec']['unit'],
                                    'scope':c['spec']['scope'],'provenance':e.provenance(c['spec']['path'],row['pointer']),
                                    'native_record':copy.deepcopy(row['value']),
                                    'scholarly_limits':e.profile['scholarly_limits'],
                                    'context_resources':[e.provenance(p) for p in e.artifacts],
                                    'individual_skill_path':'ai-skill/SKILL.md'})
            counts.append({'repository':repo,'collection':name,'native_unit':c['spec']['unit'],'matched_view_rows':matched})
    return {'records':results,'returned_view_rows':len(results),'matches_by_native_collection':counts,
            'truncated':sum(c['matched_view_rows'] for c in counts)>len(results),
            'physical_identity_join_performed':False,'unique_object_count':None,
            'independent_witness_count':None,'scientific_approval_granted':False,
            'boundary':native.BOUNDARY}


def exercises(checkouts):
    ms=members(checkouts); output=[]
    repo,root,_=ms[0];e=native.Evidence(root)
    name=next(n for n,c in e.collections.items() if c['records']);row=e.collections[name]['records'][0]
    dossier=native.answer(name,row['id'],root)
    native.validate_answer(dossier,name,row['id'],root)
    output.append({'exercise':'1 Trace an exact source record','repository':repo,'collection':name,'id':row['id'],
                   'source':dossier['dossier']['provenance'],'result':'PASS_EXACT_NATIVE_DOSSIER'})
    q=query(checkouts,text='?',limit=1000)
    assert q['unique_object_count'] is None and not q['physical_identity_join_performed']
    output.append({'exercise':'2 Search across corpora without pooling','query':'?',
                   'matched_collections':[c for c in q['matches_by_native_collection'] if c['matched_view_rows']],
                   'result':'PASS_NAMESPACED_SOURCE_RETRIEVAL'})
    # Literal marker search is a retrieval demo, not classification of damage.
    checked=0
    cache={repo:native.Evidence(root) for repo,root,_ in ms}
    for result in q['records']:
        member_root=Path(checkouts)/result['key'][0].split('/')[-1]
        d=cache[result['key'][0]].dossier(result['key'][2],result['key'][1])
        assert result['native_record']==d['native_record'];checked+=1
    output.append({'exercise':'3 Preserve literal uncertainty/editorial notation',
                   'matched_records_checked':checked,'interpretation_of_question_mark':'NOT_ASSUMED',
                   'result':'PASS_NATIVE_PAYLOAD_EQUALITY'})
    packages=[]
    for repo,root,_ in ms:
        raw=native.package(root);assert raw==native.package(root)
        with zipfile.ZipFile(io.BytesIO(raw)) as z:
            manifest=json.loads(z.read('research-package-manifest.json'))
            for f in manifest['files']:assert native.sha(z.read(f['path']))==f['sha256']
        packages.append({'repository':repo,'sha256':native.sha(raw),'bytes':len(raw)})
    output.append({'exercise':'4 Reproduce local research packages','packages':packages,'result':'PASS_REPEAT_BUILD_AND_MEMBER_HASHES'})
    draft=native.review_template(name,row['id'],Path(checkouts)/ms[0][0].split('/')[-1])
    try:native.validate_review(draft,Path(checkouts)/ms[0][0].split('/')[-1])
    except ValueError:pass
    else:raise AssertionError('draft admitted')
    output.append({'exercise':'5 Prepare feedback without manufacturing acceptance','target':draft['target'],
                   'result':'PASS_DRAFT_CREATED_AND_REJECTED_AS_COMPLETED_REVIEW',
                   'real_review_performed':False})
    return {'format':'northwestern-five-research-exercises-v1','exercises':output,
            'new_readings':0,'expert_acceptance_added':False,
            'scope':'Reproducible workflows over current native views; not new historical conclusions or empirical LLM evaluation.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',required=True,type=Path)
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--audit',action='store_true');mode.add_argument('--search')
    mode.add_argument('--id');mode.add_argument('--exercises',action='store_true')
    p.add_argument('--repository');p.add_argument('--collection');p.add_argument('--limit',type=int,default=20)
    p.add_argument('--output',type=Path);a=p.parse_args()
    if a.audit:r=audit(a.checkouts)
    elif a.exercises:r=exercises(a.checkouts)
    else:r=query(a.checkouts,a.search or '',a.id,a.repository,a.collection,a.limit)
    text=json.dumps(r,ensure_ascii=False,indent=2)+'\n'
    if a.output:a.output.write_text(text,encoding='utf-8')
    else:print(text,end='')

if __name__=='__main__':main()
