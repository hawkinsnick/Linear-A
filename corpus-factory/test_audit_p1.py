import importlib.util,json,subprocess,tempfile,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('p1',ROOT/'corpus-factory/audit_p1.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
class SnapshotTests(unittest.TestCase):
 def fixture(self,r):
  p=r/'corpus';p.mkdir();subprocess.run(['git','init','-q'],cwd=p,check=True);subprocess.run(['git','remote','add','origin','https://github.com/example/corpus.git'],cwd=p,check=True);subprocess.run(['git','-c','user.name=Fixture','-c','user.email=fixture@example.invalid','commit','--allow-empty','-qm','fixture'],cwd=p,check=True)
  for d in ['research','scripts','review','data']:(p/d).mkdir()
  (p/'scripts/build_collection_handoff.py').write_bytes((ROOT/'scripts/build_collection_handoff.py').read_bytes());(p/'data/records.json').write_text('[{"id":"A","uncertain":true}]');(p/'research/tasks.json').write_text('{}');(p/'research/collection-readiness-inputs.json').write_text(json.dumps({'repository':'example/corpus','record_sets':[{'name':'digital','path':'data/records.json','id_key':'id','unit':'source_entry'}],'source_files':['research/tasks.json'],'native_review_links':[]}));subprocess.run(['python','scripts/build_collection_handoff.py','--write'],cwd=p,check=True,capture_output=True);return p
 def test_units_missing_rights_and_absent_interop_remain_unknown(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);self.fixture(r);x=m.inspect(r,'example/corpus');self.assertEqual(x['record_views'][0]['unit'],'source_entry');self.assertEqual(x['rights_authority_paths'],[]);self.assertEqual(x['interoperability_paths'],[]);self.assertEqual(x['expert_acceptance'],'NOT_GRANTED_BY_THIS_AUDIT')
 def test_wrong_checkout_is_rejected(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);p=self.fixture(r);subprocess.run(['git','remote','set-url','origin','https://github.com/other/corpus.git'],cwd=p,check=True)
   with self.assertRaisesRegex(ValueError,'origin'):m.inspect(r,'example/corpus')
 def test_native_change_invalidates_snapshot(self):
  with tempfile.TemporaryDirectory() as d:
   r=Path(d);p=self.fixture(r);(p/'data/records.json').write_text('[{"id":"A","uncertain":false}]')
   with self.assertRaisesRegex(ValueError,'replay failed'):m.inspect(r,'example/corpus')
if __name__=='__main__':unittest.main()
