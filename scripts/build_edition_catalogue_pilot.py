#!/usr/bin/env python3
"""Replay inspected edition labels without certifying modern object identities."""
import argparse,csv,hashlib,io,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
INPUT='research/edition-catalogue-pilot.json'
def digest(b):return hashlib.sha256(b).hexdigest()
def build(payload,root=ROOT,assets=None):
 routes={r['route_id']:r for r in json.loads((root/'research/gorila-route-acquisition.json').read_text())['routes']}
 assert payload['physical_identities_certified']==payload['independent_expert_reviews']==0
 assert payload['raison_pope_entry_joins']=='UNRESOLVED'
 pages={p['route_id']:p for p in payload['pages']};assert len(pages)==4
 entries=payload['entries'];assert len(entries)==20 and len({e['source_record_id'] for e in entries})==20
 assert [(p['viewer_page'],p['printed_page']) for p in pages.values()]==[(64,2),(66,4),(67,5),(68,6)]
 for key,p in pages.items():
  r=routes[key];assert r['volume']==p['volume']==2 and p['viewer_page']==r['viewer_page'] and p['page_url']==r['page_url'] and p['image_sha256']==r['image_sha256'] and p['image_bytes']==r['image_bytes'] and p['images_redistributed'] is False
  assert [e['source_record_id'] for e in entries if e['route_id']==key]==r['source_record_ids']
  if assets:
   b=(assets/(key+'.jpg')).read_bytes();assert digest(b)==p['image_sha256'] and len(b)==p['image_bytes']
 for e in entries:
  assert e['physical_object_identity_certified'] is e['current_museum_accession_verified'] is e['reading_adjudicated'] is False
  assert e['classification']=='PRIMARY_EDITION_REPORTED' and e['source_license']=='CC BY-NC-SA 4.0' and e['source_attribution']
  if e['source_record_id'].startswith('GO'):
   assert e['edition_parent_unit']=='GO Wc 1' and e['edition_panel_label'] in ['a','b'] and e['catalogue_caption_label']=='HM 83' and e['edition_counting_unit']=='LABELLED_PANEL_OF_ONE_EDITION_ENTRY'
  else:
   assert e['edition_panel_label'] is None and e['edition_parent_unit']==e['source_record_id'] and e['caption_dimensions'] is None
 rows=[{**e,'gorila_volume':pages[e['route_id']]['volume'],'gorila_printed_page':pages[e['route_id']]['printed_page'],'gorila_viewer_page':pages[e['route_id']]['viewer_page'],'page_url':pages[e['route_id']]['page_url'],'image_sha256':pages[e['route_id']]['image_sha256']} for e in entries]
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
 audit={'format':'linear-a-edition-catalogue-audit-v1','input_sha256':digest((json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode()),'consulted_primary_pages':4,'source_entries':20,'edition_parent_units':len({e['edition_parent_unit'] for e in entries}),'distinct_printed_catalogue_labels':len({e['catalogue_caption_label'] for e in entries}),'physical_identities_certified':0,'independent_expert_reviews':0,'sign_readings_adjudicated':0,'count_boundary':'Two GO Wc 1 panels are one edition parent unit. Catalogue captions are historical edition reports, not certified current accessions or physical identity joins. HT prefix is section context, not printed in each panel heading.','comparison_sha256':digest(s.getvalue().encode())}
 return {'research/edition-catalogue-comparison.csv':s.getvalue(),'analysis/edition-catalogue-pilot-audit.json':json.dumps(audit,indent=2)+'\n'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--verify-assets',type=Path);args=p.parse_args();payload=json.loads((ROOT/INPUT).read_text())
 for path,s in build(payload,assets=args.verify_assets).items():
  if args.check:assert (ROOT/path).read_text()==s,'Catalogue replay drift'
  else:(ROOT/path).write_text(s)
 print('Edition catalogue pilot: 20 source entries / 19 edition parent units / 4 inspected pages; no certified physical identities')
if __name__=='__main__':main()
