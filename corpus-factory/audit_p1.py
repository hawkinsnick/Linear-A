#!/usr/bin/env python3
"""Inspect declared fleet checkouts, preserving native units and evidence limits."""
import argparse,hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inspect(root,repository):
 name=repository.split('/')[-1];r=root/name
 if not (r/'.git').exists():raise ValueError('missing checkout: '+name)
 origin=subprocess.check_output(['git','remote','get-url','origin'],cwd=r,text=True).strip()
 if not origin.rstrip('/').removesuffix('.git').endswith('/'+repository):raise ValueError('wrong checkout origin: '+name)
 cfg=json.loads((r/'research/collection-readiness-inputs.json').read_text())
 if cfg['repository']!=repository:raise ValueError('wrong collection repository')
 x=subprocess.run(['python','scripts/build_collection_handoff.py'],cwd=r,capture_output=True,text=True)
 if x.returncode:raise ValueError('collection replay failed: '+name+' '+x.stderr)
 ledger=json.loads((r/'research/collection-work-ledger.json').read_text())
 if ledger.get('scientific_approval_granted') is not False:raise ValueError('collection must not grant scientific approval')
 rights=[p for p in ['DATA-LICENSE-MATRIX.md','docs/RIGHTS.md','docs/RIGHTS-AND-LICENSING.md','LICENSING.md','THIRD-PARTY-NOTICES.md','research/rights-source-matrix.json'] if (r/p).is_file()]
 interop=[p.as_posix() for p in [*r.glob('schemas/*interoperab*'),*r.glob('analysis/*epidoc*'),*r.glob('scripts/*epidoc*'),*r.glob('tests/*epidoc*')] if p.is_file()]
 interop=sorted(p[len(str(r))+1:] for p in interop)
 pins=sorted(set(cfg['source_files']+[x['path'] for x in cfg['record_sets'] if not x.get('local_only')]+['research/collection-readiness-inputs.json','research/collection-work-ledger.json','review/collection-packet.json','scripts/build_collection_handoff.py']+rights+interop))
 return {'repository':repository,'checkout_base_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=r,text=True).strip(),'native_input_sha256':{p:sha(r/p) for p in pins},'record_views':ledger['record_views'],'collection_tasks':len(ledger['tasks']),'rights_authority_paths':rights,'rights_acceptance':'COMPONENT_LEVEL_REVIEW_REQUIRED; FILE_PRESENCE_IS_NOT_PERMISSION','interoperability_paths':interop,'interoperability_acceptance':'NO_FLEET_WIDE_EPIDOC_CONFORMANCE_CLAIM; NATIVE_SCOPES_AND_LIMITS_APPLY','review_packet':'review/collection-packet.json','expert_acceptance':'NOT_GRANTED_BY_THIS_AUDIT'}
def build(checkouts):
 reg=json.loads((ROOT/'combined-ai-skill/registry/corpus-projects.json').read_text())
 repos=[m['repository'] for m in reg['members']]
 if len(repos)!=len(set(repos)) or any(x.endswith(('/Egyptian-Hieroglyphic-Corpus','/LightroomIsSlow')) for x in repos):raise ValueError('invalid scope')
 return {'schema_version':'1.0','scope':'Declared 18 language repositories; base commits plus exact input hashes identify snapshots, including local repairs. Not an assertion of unmodified commit trees.','closure_rule':'Software replay does not close scholarly, rights or independent-review gates. Views are not summed as unique objects.','members':[inspect(checkouts,x) for x in repos]}
def main():
 a=argparse.ArgumentParser();a.add_argument('--checkouts',type=Path,required=True);a.add_argument('--write',action='store_true');args=a.parse_args();d=build(args.checkouts.resolve());p=ROOT/'corpus-factory/p1-evidence-snapshot.json';b=json.dumps(d,indent=2,ensure_ascii=False)+'\n'
 if args.write:p.write_text(b)
 elif not p.exists() or p.read_text()!=b:raise SystemExit('P1 evidence snapshot stale; inspect changed inputs before --write')
 print('PASS: source-bound fleet snapshot; no scholarly approval granted')
if __name__=='__main__':main()
