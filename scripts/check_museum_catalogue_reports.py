"""Check report-to-edition links without promoting candidate physical identities."""
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def check():
 d=json.loads((ROOT/'research/museum-catalogue-reports.json').read_text());e=json.loads((ROOT/'research/edition-catalogue-pilot.json').read_text());by={x['source_record_id']:x for x in e['entries']};sources={s['source_id']:s for s in d['sources']}
 assert len(sources)==3 and d['physical_identities_certified']==d['independent_confirmations_certified']==0 and d['images_or_models_redistributed'] is False
 for row in d['comparisons']:
  target=by[row['edition_source_record_id']];assert row['edition_parent_unit']==target['edition_parent_unit'] and row['edition_caption']==target['catalogue_caption_label']
  assert all(s in sources for s in row['catalogue_source_ids'])
  assert row['physical_object_identity_certified'] is row['modern_accession_crosswalk_certified'] is row['reading_adjudicated'] is False and row['source_independence']=='NOT_ESTABLISHED'
 assert sources['MUCIV-81951']['reported_inscription_id'] is None
 assert sources['INSCRIBE-HT114']['reported_inscription_id']=='HT 114' and sources['INSCRIBE-HT114']['reported_inventory']=='83735'
 assert all(s['source_body_sha256'] is None and s['rights'] and s['attribution'] and s['url'].startswith('https://') for s in sources.values())
 print('Catalogue report links verified; no certified identities, independence or image/model reuse')
if __name__=='__main__':check()
