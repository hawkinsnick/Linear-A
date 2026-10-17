"""Replay bounded human/source-authority routing, without certifying readiness."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def validate(root=ROOT,checkouts=None,data=None):
    root=Path(root);d=data if data is not None else json.loads((root/'corpus-factory/p1-human-readiness.json').read_text())
    expected={m['repository'] for m in json.loads((root/'combined-ai-skill/registry/corpus-projects.json').read_text())['members']}
    if d['format']!='corpus-p1-human-validation-routing-v1' or len(d['members'])!=len(expected) or {m['repository'] for m in d['members']}!=expected:raise ValueError('routing membership drift')
    if any(d[k] is not False for k in ['human_validation_performed','all_p1_closed','all_source_work_complete']):raise ValueError('unsupported human or source completion claim')
    replayed=0
    for m in d['members']:
        if m['whole_corpus_human_only_readiness']!='NOT_CERTIFIED' or m['expert_review_performed'] is not False or m['source_exhaustion_claimed'] is not False or m['native_acceptance_controls_remain_required'] is not True:raise ValueError('native acceptance bypass or unperformed review')
        if len(m['source_commit'])!=40 or not m['native_prerequisites'] or not m['remaining_work_categories'] or not m['native_review_inputs']:raise ValueError('missing scoped prerequisites or input binding')
        paths=set()
        for p in m['native_review_inputs']:
            if Path(p['path']).is_absolute() or '..' in Path(p['path']).parts or p['path'] in paths or len(p['sha256'])!=64:raise ValueError('unsafe duplicate or unhashed review input')
            paths.add(p['path'])
            if checkouts:
                raw=subprocess.check_output(['git','show',m['source_commit']+':'+p['path']],cwd=Path(checkouts)/m['repository'].split('/')[-1])
                if hashlib.sha256(raw).hexdigest()!=p['sha256']:raise ValueError('stale pinned native review input')
                packet=json.loads(raw)
                if p['path'].endswith('human-request.json'):
                    if packet['status']!='PREPARED_NOT_REVIEWED' or packet['decisions'] or packet['scientific_approval_granted'] is not False:raise ValueError('prepared request falsely treated as review')
                replayed+=1
    work=d['new_documentary_work']
    if (work['reference_rows_accounted'],work['codepoint_spans'],work['literal_boundary_contexts'])!=(105,199,47) or work['new_accepted_readings']!=0 or work['new_independent_reviews']!=0:raise ValueError('documentary units or acceptance drift')
    return {'status':'PASS_SCOPED_HUMAN_ROUTING_NOT_ACCEPTANCE','members':len(expected),'native_review_inputs_replayed':replayed,'human_validation_performed':False,'whole_corpus_readiness_certified':False}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path);a=p.parse_args();print(json.dumps(validate(checkouts=a.checkouts)))
