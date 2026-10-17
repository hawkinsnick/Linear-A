import copy,json,shutil,tempfile,unittest
from pathlib import Path
import validate_northwestern_program as v

class Program(unittest.TestCase):
    def test_real_receipts(self):self.assertEqual(v.validate()['requirements'],7)
    def test_completion_membership_and_failed_validation_rejected(self):
        paths=['combined-ai-skill/registry/corpus-projects.json']+['corpus-factory/'+p for p in ['northwestern-work-program.json','research-delivery-fleet.json','northwestern-exercises.json','northwestern-validation.json']]
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            for p in paths:
                (root/p).parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(v.ROOT/p,root/p)
            for case in ('closure','requirement','member','native-failure'):
                path='corpus-factory/'+('northwestern-work-program.json' if case in ('closure','requirement') else 'research-delivery-fleet.json' if case=='member' else 'northwestern-validation.json')
                target=root/path;original=target.read_bytes();d=json.loads(original)
                if case=='closure':d['all_scholarly_p0_p1_closed']=True
                elif case=='requirement':d['requirements'].pop()
                elif case=='member':d['members'].pop()
                else:d['native_commands'][0]['checks'][0]['exit']=1
                target.write_text(json.dumps(d))
                with self.assertRaises(ValueError):v.validate(root)
                target.write_bytes(original)

if __name__=='__main__':unittest.main()
