#!/usr/bin/env python3
"""Check linked edition-route acquisition without promoting readings or objects."""
import argparse,hashlib,json
from pathlib import Path
from acquire_gorila_routes import ROOT,groups,cached,digest
PATH='research/gorila-route-acquisition.json';AUDIT='analysis/gorila-route-audit.json'
def build(root=ROOT,assets=None):
 payload=json.loads((root/PATH).read_text());targets=groups(root)
 assert payload['concordance_sha256']==digest((root/'research/edition-concordance.csv').read_bytes())
 rows=payload['routes'];assert len(rows)==len(targets)==367
 assert len({r['page_url'] for r in rows})==len(rows)
 acquired=0;covered=0
 for row in rows:
  items=targets[row['page_url']]
  assert row['source_record_ids']==[r['source_record_id'] for r in items]
  assert row['volume']==int(items[0]['gorila_volume']) and row['viewer_page']==int(items[0]['gorila_viewer_page'])
  assert row['primary_reading_inspected'] is False and row['physical_object_identity_certified'] is False and row['source_images_redistributed'] is False and row['printed_page_verified'] is None
  if row['status']=='ACQUIRED_LINKED_EDITION_IMAGE_NOT_TEXT_VERIFICATION':
   acquired+=1;covered+=len(items)
   for key in ['html_sha256','image_sha256']:assert len(row[key])==64 and all(c in '0123456789abcdef' for c in row[key])
   assert row['image_bytes']>0 and row['html_bytes']>0
   if assets:assert cached(row,items,assets),'Asset mismatch: '+row['route_id']
  else:assert row['status'] in ['SOURCE_ROUTE_BLOCKED','NOT_COMPLETED_RUNTIME_NETWORK_POLICY'] and row['barrier']
 return {'format':'linear-a-gorila-route-audit-v1','registry_sha256':digest((root/PATH).read_bytes()),'attributed_source_entries':sum(map(len,targets.values())),'distinct_linked_page_routes':len(rows),'acquired_page_routes':acquired,'source_entries_linked_to_acquired_pages':covered,'routes_without_completed_acquisition':len(rows)-acquired,'entries_on_shared_page_routes':sum(len(v) for v in targets.values() if len(v)>1),'reading_verifications_added':0,'physical_identities_certified':0,'image_copies_committed':False,'counting_boundary':'Route URLs, derivative source entries, inscription surfaces and physical objects are distinct units. Acquisition does not verify an entry, printed-page locator or reading.'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--verify-assets',type=Path);args=p.parse_args();b=(json.dumps(build(assets=args.verify_assets),indent=2)+'\n').encode()
 if args.check:assert (ROOT/AUDIT).read_bytes()==b,'Route audit drift'
 else:(ROOT/AUDIT).write_bytes(b)
 print(b.decode())
if __name__=='__main__':main()
