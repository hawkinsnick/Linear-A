"""Replay published source checkpoints and compare saved aggregate receipts."""
import argparse,json,re,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def verify(checkouts):
    d=json.loads((ROOT/'corpus-factory/northwestern-published-revisions.json').read_bytes())
    expected={m['repository'] for m in json.loads((ROOT/'combined-ai-skill/registry/corpus-projects.json').read_bytes())['members']}
    if len(d['members'])!=len(expected) or {m['repository'] for m in d['members']}!=expected or d['expert_acceptance_added'] is not False:
        raise ValueError('published checkpoint membership or acceptance drift')
    for m in d['members']:
        if not re.fullmatch('[0-9a-f]{40}',m['source_commit']):raise ValueError('invalid source checkpoint')
        root=Path(checkouts)/m['repository'].split('/')[-1]
        if subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip()!=m['source_commit']:
            raise ValueError('checkout is not the published source checkpoint: '+m['repository'])
    # A historical study must execute its pinned adapter, not today's changed package API.
    historical=Path(checkouts).resolve()/'Linear-A'
    script=historical/'corpus-factory/federated_research.py'
    if subprocess.run(['git','diff','--quiet','HEAD','--'],cwd=historical).returncode:
        raise ValueError('modified historical Linear-A adapter/source')
    for mode,receipt in [('--audit','research-delivery-fleet.json'),('--exercises','northwestern-exercises.json')]:
        result=subprocess.run([sys.executable,str(script),'--checkouts',str(Path(checkouts).resolve()),mode],cwd=historical,capture_output=True,text=True,check=True)
        if json.loads(result.stdout)!=json.loads((ROOT/'corpus-factory'/receipt).read_bytes()):
            raise ValueError('published frozen replay drift: '+receipt)
    return {'status':'PASS_18_PUBLISHED_SOURCE_CHECKPOINTS_AND_FIVE_EXERCISES','members':len(expected),'expert_acceptance_added':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--checkouts',required=True,type=Path);a=p.parse_args();print(json.dumps(verify(a.checkouts)))
