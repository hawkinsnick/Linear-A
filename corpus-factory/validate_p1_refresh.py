"""Validate revision-bound P1 status receipts; optionally replay immutable Git blobs."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def validate(root=ROOT,checkouts=None,register=None,work=None):
    root=Path(root)
    reg=register if register is not None else json.loads((root/'corpus-factory/fleet-gap-register.json').read_text())
    work=work if work is not None else json.loads((root/'corpus-factory/p1-current-work.json').read_text())
    members=json.loads((root/'combined-ai-skill/registry/corpus-projects.json').read_text())['members']
    expected={x['repository'] for x in members}
    if len(reg['members'])!=len(expected) or {'hawkinsnick/'+m['repo'] for m in reg['members']}!=expected:
        raise ValueError('fleet membership drift')
    replayed=0
    for member in reg['members']:
        receipt=member['current_evidence'];repo='hawkinsnick/'+member['repo']
        if receipt['repository']!=repo or not receipt['artifacts'] or len(receipt['source_commit'])!=40:
            raise ValueError('missing member authority receipt')
        paths=set()
        for item in receipt['artifacts']:
            p=Path(item['path'])
            if p.is_absolute() or '..' in p.parts or item['path'] in paths or len(item['sha256'])!=64:
                raise ValueError('unsafe duplicate or unhashed authority')
            paths.add(item['path'])
            if checkouts:
                blob=subprocess.check_output(['git','show',receipt['source_commit']+':'+item['path']],cwd=Path(checkouts)/member['repo'])
                if hashlib.sha256(blob).hexdigest()!=item['sha256']:raise ValueError('stale pinned member authority')
                replayed+=1
    if work['scientific_acceptance_granted'] is not False or work['all_p1_closed'] is not False:
        raise ValueError('unsupported universal closure or acceptance')
    if work['registry_refresh_status']!='COMPLETE_18_MEMBER_REVISION_BOUND_REFRESH':
        raise ValueError('refresh disposition missing')
    if len(work['native_followups'])!=3 or {x['repository'] for x in work['native_followups']}!={'hawkinsnick/'+n for n in ['Phrygian','Eteocypriot','Sidetic']}:
        raise ValueError('native follow-up membership drift')
    for row in work['native_followups']:
        p=root/row['snapshot_path'];raw=p.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=row['snapshot_sha256']:raise ValueError('stale follow-up snapshot')
        packet=json.loads(raw)
        if packet['repository']!=row['repository'] or any(packet['limits'][k]!=0 for k in ['canonical_readings_added','physical_identities_certified','independent_reviews_added']):
            raise ValueError('follow-up identity or promotion')
        if len(packet['cases'])!=row['cases']:raise ValueError('follow-up accounting drift')
        if checkouts:
            blob=subprocess.check_output(['git','show',row['source_commit']+':'+row['native_path']],cwd=Path(checkouts)/row['repository'].split('/')[-1])
            if blob!=raw:raise ValueError('native snapshot differs from immutable source')
    if not work['remaining_work'] or any(not x['evidence_needed'] or not x['next_action'] for x in work['remaining_work']):
        raise ValueError('open work lacks actionable evidence requirement')
    return {'status':'PASS_REVISION_BOUND_P1_REFRESH','members':len(expected),'authority_blobs_replayed':replayed,'native_followups':3,'all_p1_closed':False,'scientific_acceptance_granted':False}
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--checkouts',type=Path);a=p.parse_args();print(json.dumps(validate(checkouts=a.checkouts)))
