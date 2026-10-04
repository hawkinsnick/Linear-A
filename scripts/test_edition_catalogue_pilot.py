import copy,json,unittest
from build_edition_catalogue_pilot import ROOT,INPUT,build
class Catalogue(unittest.TestCase):
 def setUp(self):self.p=json.loads((ROOT/INPUT).read_text())
 def test_replay(self):
  for path,s in build(self.p).items():self.assertEqual((ROOT/path).read_text(),s)
 def test_faces_not_two_parents(self):
  self.p['entries'][1]['edition_parent_unit']='GO Wc 1b'
  with self.assertRaises(AssertionError):build(self.p)
 def test_no_modern_accession_certification(self):
  self.p['entries'][3]['current_museum_accession_verified']=True
  with self.assertRaises(AssertionError):build(self.p)
 def test_no_physical_identity_promotion(self):
  self.p['entries'][0]['physical_object_identity_certified']=True
  with self.assertRaises(AssertionError):build(self.p)
 def test_wrong_page_image(self):
  self.p['pages'][0]['image_sha256']='0'*64
  with self.assertRaises(AssertionError):build(self.p)
 def test_missing_panel(self):
  self.p['entries'].pop()
  with self.assertRaises(AssertionError):build(self.p)
 def test_locator_only_cannot_gain_caption(self):
  e=next(e for e in self.p['entries'] if e['source_record_id']=='HT 90');e.update(catalogue_caption_scope='NOT_COLLATED_IN_LOCATOR_ONLY_REVIEW',dimension_scope='NOT_COLLATED_IN_LOCATOR_ONLY_REVIEW',caption_dimensions=None,catalogue_caption_label='HM invented')
  with self.assertRaises(AssertionError):build(self.p)
 def test_mismatch_cannot_gain_parent(self):
  next(e for e in self.p['entries'] if e['source_record_id']=='HT 53a')['edition_parent_unit']='HT 53'
  with self.assertRaises(AssertionError):build(self.p)
 def test_bracketed_join_cannot_be_flattened(self):
  next(e for e in self.p['entries'] if e['source_record_id']=='HT 42+59')['edition_heading']='HT 42+59'
  with self.assertRaises(AssertionError):build(self.p)
 def test_fragment_sizes_cannot_be_aggregated(self):
  self.p['fragment_dossiers'][0]['normalized_global_dimensions']='invented'
  with self.assertRaises(AssertionError):build(self.p)
 def test_candidate_cannot_be_adopted(self):
  self.p['unresolved_caption_observations'][0]['adopted_label']='candidate'
  with self.assertRaises(AssertionError):build(self.p)
 def test_caption_relation_cannot_certify_join(self):
  self.p['caption_relations'][0]['physical_join_certified']=True
  with self.assertRaises(AssertionError):build(self.p)
 def test_cast_qualifier_cannot_disappear(self):
  next(e for e in self.p['entries'] if e['source_record_id']=='HT 29')['catalogue_caption_label']='Pigorini 81951; HM 9'
  with self.assertRaises(AssertionError):build(self.p)
 def test_fragment_expression_cannot_be_summed(self):
  next(e for e in self.p['entries'] if e['source_record_id']=='HT 42+59')['caption_dimensions']='6,20 × 10,10 × 0,90 cm'
  with self.assertRaises(AssertionError):build(self.p)
 def test_mismatched_route_cannot_gain_caption(self):
  next(e for e in self.p['entries'] if e['source_record_id']=='HT 53a')['catalogue_caption_label']='HM —'
  with self.assertRaises(AssertionError):build(self.p)
if __name__=='__main__':unittest.main()
