"""Hostile checks for source identity, edition locators and inspection boundaries."""
import csv,hashlib,io,json,tempfile,unittest
from pathlib import Path
import build_edition_concordance as m
class ConcordanceTests(unittest.TestCase):
 def fixture(self,folder):
  root=Path(folder)
  for name in [m.CSV,m.REPORT,'research/edition-route-evidence.json','analysis/pre-expert-primary-collation.json']:
   p=root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((m.ROOT/name).read_bytes())
  return root
 def mutate(self,root,operation):
  path=root/m.CSV;rows=list(csv.DictReader(io.StringIO(path.read_text())));operation(rows)
  out=io.StringIO();w=csv.DictWriter(out,fieldnames=m.FIELDS,lineterminator='\n');w.writeheader();w.writerows(rows);path.write_text(out.getvalue())
  p=root/m.REPORT;x=json.loads(p.read_text());x['concordance_sha256']=m.digest(path.read_bytes());p.write_text(json.dumps(x))
 def test_committed_coverage(self):self.assertEqual(m.validate_committed(),802)
 def test_bad_source_bytes_rejected(self):
  with self.assertRaisesRegex(ValueError,'checksum'):m.build(b'{}')
 def test_dropped_duplicate_and_renamed_source_ids_rejected(self):
  for op in [lambda r:r.pop(),lambda r:r.__setitem__(1,r[0].copy()),lambda r:r[0].update(source_record_id='ARKH 1')]:
   with tempfile.TemporaryDirectory() as d:
    root=self.fixture(d);self.mutate(root,op)
    with self.assertRaises(ValueError):m.validate_committed(root)
 def test_unsupported_match_and_object_promotions_rejected(self):
  for field,value in [('physical_object_identity_certified','true'),('rp1994_status','VERIFIED'),('rp1980_status','CANDIDATE_MATCH')]:
   with tempfile.TemporaryDirectory() as d:
    root=self.fixture(d);self.mutate(root,lambda r:r[0].update({field:value}))
    with self.assertRaises(ValueError):m.validate_committed(root)
 def test_locator_page_drift_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=self.fixture(d);self.mutate(root,lambda r:r[0].update(gorila_viewer_page='999'))
   with self.assertRaises(ValueError):m.validate_committed(root)
 def test_primary_page_case_misjoin_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=self.fixture(d);self.mutate(root,lambda r:r[0].update(inspected_case_ids='U001'))
   with self.assertRaisesRegex(ValueError,'misjoin'):m.validate_committed(root)
 def test_changed_evidence_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   root=self.fixture(d);p=root/'research/edition-route-evidence.json';p.write_text(p.read_text()+' ')
   with self.assertRaisesRegex(ValueError,'evidence drift'):m.validate_committed(root)
 def test_session_removed_without_page_conversion(self):
  u='https://cefael.efa.gr/detail.php?site_id=1&actionID=page&serie_id=EtCret&volume_number=21&issue_number=3&ce=temporary&sp=26'
  v,p,url=m.gorila_locator(u);self.assertEqual((v,p),('3','26'));self.assertNotIn('ce=',url)
 def test_faces_retained_and_primary_cases_not_objects(self):
  rows=list(csv.DictReader(io.StringIO((m.ROOT/m.CSV).read_text())));ids={r['source_record_id'] for r in rows}
  self.assertTrue({'ARKH 1a','ARKH 1b'}<=ids)
  report=json.loads((m.ROOT/m.REPORT).read_text());self.assertEqual(report['primary_inspected_source_records'],8);self.assertEqual(report['primary_case_entries_bound_to_source_records'],10)
  self.assertEqual(report['primary_case_ids_without_exact_source_id_join'],['U010','U012','U013'])
if __name__=='__main__':unittest.main()
