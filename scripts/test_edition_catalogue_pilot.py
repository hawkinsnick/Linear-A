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
if __name__=='__main__':unittest.main()
