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
 pages={p['route_id']:p for p in payload['pages']};assert len(pages)==payload['declared_coverage']['pages']
 entries=payload['entries'];assert len(entries)==len({e['source_record_id'] for e in entries})==payload['declared_coverage']['source_entries']
 for key,p in pages.items():
  r=routes[key];assert r['volume']==p['volume'] and p['viewer_page']==r['viewer_page'] and p['page_url']==r['page_url'] and p['image_sha256']==r['image_sha256'] and p['image_bytes']==r['image_bytes'] and p['images_redistributed'] is False
  assert [e['source_record_id'] for e in entries if e['route_id']==key]==r['source_record_ids']
  if assets:
   b=(assets/(key+'.jpg')).read_bytes();assert digest(b)==p['image_sha256'] and len(b)==p['image_bytes']
 for e in entries:
  assert e['physical_object_identity_certified'] is e['current_museum_accession_verified'] is e['reading_adjudicated'] is False
  assert e['classification']=='PRIMARY_EDITION_REPORTED' and e['source_license']=='CC BY-NC-SA 4.0' and e['source_attribution']
  assert e['locator_status'] in ['TARGET_HEADING_VISUALLY_CONFIRMED','SOURCE_ROUTE_TARGET_MISMATCH']
  if e['locator_status']=='SOURCE_ROUTE_TARGET_MISMATCH':
   assert e['edition_heading'] is e['edition_parent_unit'] is e['edition_panel_label'] is None and e['edition_counting_unit']=='UNRESOLVED_SOURCE_ROUTE'
   assert e['catalogue_caption_label'] is e['caption_dimensions'] is None
  if e['catalogue_caption_scope']=='NOT_COLLATED_IN_LOCATOR_ONLY_REVIEW':
   assert e['catalogue_caption_label'] is e['caption_dimensions'] is None and e['dimension_scope']=='NOT_COLLATED_IN_LOCATOR_ONLY_REVIEW'
  if e['locator_status']=='SOURCE_ROUTE_TARGET_MISMATCH':continue
  if e['source_record_id'].startswith('GO'):
   assert e['edition_parent_unit']=='GO Wc 1' and e['edition_panel_label'] in ['a','b'] and e['catalogue_caption_label']=='HM 83' and e['edition_counting_unit']=='LABELLED_PANEL_OF_ONE_EDITION_ENTRY'
  elif e['edition_panel_label']:
   assert e['edition_parent_unit']==e['source_record_id'][:-1] and e['edition_panel_label'] in ['a','b'] and e['edition_counting_unit']=='LABELLED_FACE_OF_EDITION_PARENT'
  elif e['source_record_id'].startswith('HT'):
   assert e['edition_panel_label'] is None and e['edition_parent_unit']==e['source_record_id']
 by={e['source_record_id']:e for e in entries}
 for relation in payload.get('caption_relations',[]):
  target=by[relation['target_source_record_id']];source=by[relation['caption_source_record_id']]
  assert target['edition_parent_unit']==source['edition_parent_unit'] and target['edition_panel_label']=='b' and source['edition_panel_label']=='a'
  assert target['catalogue_caption_label'] is None and source['catalogue_caption_label'] and relation['physical_join_certified'] is False
 for dossier in payload.get('fragment_dossiers',[]):
  assert dossier['edition_parent_unit'] in {e['edition_parent_unit'] for e in entries} and dossier['caption_route_id'] in pages
  assert dossier['certified_fragment_identities']==0 and dossier['dimension_aggregation_status']=='NO_SUM_OR_NORMALIZED_GLOBAL_SIZE'
  assert dossier['join_status']=='EDITION_PRESENTATION_ONLY_NOT_CERTIFIED_PHYSICAL_JOIN'
  assert 'normalized_global_dimensions' not in dossier and 'physical_object_id' not in dossier
  assert dossier['additional_separate_fragments_reported']==4 and len(dossier['caption_fragment_items'])==3
  assert [f['catalogue_label'] for f in dossier['caption_fragment_items']]==['HM 1668','HM 1669','HM —']
  assert all('physical_object_id' not in f and 'certified' not in f for f in dossier['caption_fragment_items'])
 for form in payload.get('object_form_reports',[]):
  assert form['source_record_id'] in by and form['route_id']==by[form['source_record_id']]['route_id']
  assert form['dimension_inference']=='DO_NOT_MEASURE_SCREEN_PIXELS_FROM_PRINTED_SCALE'
 for observation in payload.get('unresolved_caption_observations',[]):
  assert observation['source_record_id'] in by and observation['expert_decision'] is False
  assert by[observation['source_record_id']][observation['field']] is None
  assert observation.get('adopted_label') is None and observation.get('adopted_dimensions') is None
 for resolved in payload.get('resolved_caption_observations',[]):
  e=by[resolved['source_record_id']];page=pages[e['route_id']]
  assert resolved['route_id']==e['route_id'] and resolved['original_image_sha256']==page['image_sha256']
  assert resolved['physical_identity_certified'] is resolved['expert_decision'] is False
  assert resolved['resolution_scope']=='WHAT_THE_EDITION_CAPTION_PRINTS_ONLY'
  assert e[resolved['field']]==resolved['edition_caption_value'] and resolved['previous_unresolved_observation']['expert_decision'] is False
  assert resolved['previous_unresolved_observation']['source_record_id']==e['source_record_id']
 for exclusion in payload.get('inspection_exclusions',[]):
  assert exclusion['route_id'] in pages and exclusion['excluded_heading'] not in by
 for note in payload.get('source_critical_notes',[]):
  assert note['source_record_id'] in by and note['route_id']==by[note['source_record_id']]['route_id']
  assert 'physical_join_certified' not in note
 for discrepancy in payload.get('locator_discrepancies',[]):
  assert discrepancy['replacement_route_verified'] is False
  assert all(by[s]['locator_status']=='SOURCE_ROUTE_TARGET_MISMATCH' and by[s]['route_id']==discrepancy['route_id'] for s in discrepancy['source_record_ids'])
 for sid in ['HT 42+59','HT 62+73','HT 79+83']:
  if sid in by:assert '[+]' in by[sid]['edition_heading']
 for sid,expression in [('HT 42+59','6,20 × [4,80]+[5,30] × 0,90 cm'),('HT 49a','5,50 × [3,00]+[6,20] × 0,70 cm'),('HT 62+73','[5,10] × [7,00]+[3,30] × 0,80 cm'),('HT 79+83','[2,30]+[3,20] × [3,00]+[2,60] × 0,80 cm')]:
  assert by[sid]['caption_dimensions']==expression,'Fragment-size expression lost qualification or operator'
 assert by['HT 29']['catalogue_caption_label']=='Pigorini 81951; HM 9 (moulage)','Original/cast distinction lost'
 assert by['HT 42+59']['catalogue_caption_label']=='HM 46 [+] 42' and by['HT 62+73']['catalogue_caption_label']=='HM 54 [+] —'
 rows=[{**e,'gorila_volume':pages[e['route_id']]['volume'],'gorila_printed_page':pages[e['route_id']]['printed_page'],'gorila_viewer_page':pages[e['route_id']]['viewer_page'],'page_url':pages[e['route_id']]['page_url'],'image_sha256':pages[e['route_id']]['image_sha256']} for e in entries]
 s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)
 audit={'format':'linear-a-edition-catalogue-audit-v1','input_sha256':digest((json.dumps(payload,ensure_ascii=False,indent=2)+'\n').encode()),'consulted_primary_pages':len(pages),'source_entries':len(entries),'target_headings_confirmed':sum(e['locator_status']=='TARGET_HEADING_VISUALLY_CONFIRMED' for e in entries),'source_route_target_mismatches':sum(e['locator_status']=='SOURCE_ROUTE_TARGET_MISMATCH' for e in entries),'caption_review_pages':sum(p['inspection']!='AI_VISUAL_INSPECTION_PRINTED_PAGE_AND_HEADINGS_ONLY' for p in pages.values()),'locator_only_pages':sum(p['inspection']=='AI_VISUAL_INSPECTION_PRINTED_PAGE_AND_HEADINGS_ONLY' for p in pages.values()),'edition_parent_units':len({e['edition_parent_unit'] for e in entries if e['edition_parent_unit']}),'distinct_printed_catalogue_labels':len({e['catalogue_caption_label'] for e in entries if e['catalogue_caption_label']}),'caption_label_rows':sum(e['catalogue_caption_label'] is not None for e in entries),'dimension_expression_rows':sum(e['caption_dimensions'] is not None for e in entries),'shared_face_caption_relations':len(payload.get('caption_relations',[])),'unresolved_caption_fields':len(payload.get('unresolved_caption_observations',[])),'resolved_edition_caption_fields':len(payload.get('resolved_caption_observations',[])),'caption_scope':'Inventory labels and dimension fields/status on acquired pages; selected qualifiers, not full caption text or critical sign transcription','fragment_caption_items':sum(len(f['caption_fragment_items']) for f in payload.get('fragment_dossiers',[])),'additional_separate_fragments_reported':sum(f['additional_separate_fragments_reported'] for f in payload.get('fragment_dossiers',[])),'physical_identities_certified':0,'independent_expert_reviews':0,'sign_readings_adjudicated':0,'count_boundary':'Two GO Wc 1 panels are one edition parent unit. Catalogue captions are historical edition reports, not certified current accessions or physical identity joins. HT Wa prefix is section context; tablet HT headings are printed. Two mismatched source routes have no confirmed edition parent. Uncollated captions are not absent captions.','comparison_sha256':digest(s.getvalue().encode())}
 return {'research/edition-catalogue-comparison.csv':s.getvalue(),'analysis/edition-catalogue-pilot-audit.json':json.dumps(audit,indent=2)+'\n'}
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');p.add_argument('--verify-assets',type=Path);args=p.parse_args();payload=json.loads((ROOT/INPUT).read_text())
 for path,s in build(payload,assets=args.verify_assets).items():
  if args.check:assert (ROOT/path).read_text()==s,'Catalogue replay drift'
  else:(ROOT/path).write_text(s)
 print('Edition catalogue views verified; no physical identity certification')
if __name__=='__main__':main()
