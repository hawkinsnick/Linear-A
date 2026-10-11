"""Keep native coverage units and snapshot ages explicit; never sum unlike views."""
import argparse,hashlib,json,re
from pathlib import Path
R=Path(__file__).resolve().parents[1]
def load(p):return json.loads((R/p).read_text())
def build():
 p='corpus-factory/p1-evidence-snapshot.json';baseline=load(p);fresh=load('corpus-factory/source-checkpoints-2026-10-11.json');byrepo={m['repository']:m for m in fresh['members']}
 if len(byrepo)!=2:raise ValueError('fresh checkpoint membership drift')
 rows=[]
 for m in baseline['members']:
  if m['repository'] in byrepo:
   new=byrepo[m['repository']]
   if not re.fullmatch('[0-9a-f]{40}',new['source_commit'] or ''):raise ValueError('fresh source commit missing')
   views=new['views'];status='FRESH_BOUNDED_SOURCE_CHECKPOINT';source={'commit':new['source_commit'],'path':new['source_path'],'sha256':new['source_sha256']}
  else:
   views=[{'view_id':v['view'],'unit':v['unit'],'enumerated':v['enumerated'],'native_reported_count':v.get('native_reported_count'),'representation':v['representation']} for v in m['record_views']]
   status='HISTORICAL_PINNED_AUDIT_SNAPSHOT_NOT_RECHECKED_IN_THIS_PASS';source={'checkout_base_commit':m['checkout_base_commit'],'snapshot_path':p,'snapshot_sha256':hashlib.sha256((R/p).read_bytes()).hexdigest(),'native_input_sha256':m['native_input_sha256']}
  rows.append({'repository':m['repository'],'freshness':status,'source':source,'views':views,'physical_inscription_population':None,'views_must_not_be_summed':True,'primary_edition_reconciliation_complete':False})
 if len(rows)!=18 or len({m['repository'] for m in rows})!=18:raise ValueError('fleet membership drift')
 return {'schema_version':'1.0','checked':'2026-10-11','scope':'Declared 18 repositories, fresh CH/CM checkpoints plus named historical snapshots for the other 16; not all current main branches.','aggregate_physical_population':None,'aggregate_coverage_percentage':None,'collection_primary_reconciliation_complete':False,'members':rows}
def validate():
 if load('corpus-factory/coverage-denominators.json')!=build():raise ValueError('coverage units, source pins, freshness or population drift')
 return {'status':'PASS_BOUNDED_FLEET_DENOMINATORS','members':18,'fresh_members':2,'aggregate_physical_population':None}
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--write',action='store_true');a=p.parse_args()
 if a.write:(R/'corpus-factory/coverage-denominators.json').write_text(json.dumps(build(),ensure_ascii=False,indent=2)+'\n')
 print(json.dumps(validate()))
