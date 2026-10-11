"""Replay all declared native view inventories without inferring physical populations."""
import argparse,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def build():
 p='corpus-factory/fleet-enumeration-audit-v2.json';audit=load(p)
 if hashlib.sha256(json.dumps(audit,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()!='e4806a2604eed10c8b5d586168be943087a11ee8abf6426650bb61bdf1e214c7':raise ValueError('audited native enumeration/receipts changed')
 registry=load('combined-ai-skill/registry/corpus-projects.json');expected={m['repository'] for m in registry['members']};rows=[]
 if {m['repository'] for m in audit['members']}!=expected or len(audit['members'])!=18:raise ValueError('fleet membership mismatch')
 for m in audit['members']:
  if not re.fullmatch('[0-9a-f]{40}',m['snapshot_commit']):raise ValueError('source commit missing')
  if m['consistency_issues']:raise ValueError('unresolved native inventory inconsistency')
  seen=set()
  for v in m['views']:
   if v['view_id'] in seen or not v['unit']:raise ValueError('duplicate or untyped view')
   seen.add(v['view_id'])
   if v['status']=='EXACT_PUBLIC_VIEW_ENUMERATED':
    ids=v['included_ids']
    if len(ids)!=v['denominator'] or len(set(ids))!=len(ids) or v['duplicate_ids']!=[]:raise ValueError('native view duplicate/count drift')
    if v['path'] not in m['receipts_sha256']:raise ValueError('unlocated source view')
   elif v['status']=='RESTRICTED_LOCAL_VIEW_NOT_ACQUIRED':
    if v['included_ids'] is not None or v['denominator'] is not None:raise ValueError('restricted inventory fabricated')
   else:raise ValueError('unreplayed declared view')
  rows.append({'repository':m['repository'],'freshness':'FRESH_NATIVE_VIEW_ENUMERATION_AT_IMMUTABLE_COMMIT','source':{'commit':m['snapshot_commit'],'snapshot_path':p,'snapshot_sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'native_input_sha256':m['receipts_sha256']},'views':m['views'],'physical_inscription_population':None,'views_must_not_be_summed':True,'primary_edition_reconciliation_complete':False})
 return {'schema_version':'2.0','checked':'2026-10-11','scope':'All 18 registered repositories, immutable current main snapshots at inspection; declared public view rows fully enumerated. Restricted derivatives remain unacquired, with no invented identities.','aggregate_physical_population':None,'aggregate_coverage_percentage':None,'collection_primary_reconciliation_complete':False,'members':rows}
def validate():
 if load('corpus-factory/coverage-denominators.json')!=build():raise ValueError('coverage units, source pins, freshness or population drift')
 return {'status':'PASS_FLEET_DECLARED_VIEW_ACCOUNTING','members':18,'fresh_members':18,'restricted_views_unacquired':2,'aggregate_physical_population':None}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.write:(R/'corpus-factory/coverage-denominators.json').write_text(json.dumps(build(),ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(validate()))
