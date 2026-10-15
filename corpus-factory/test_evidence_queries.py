import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
import validate_evidence_queries as q

class RolloutTests(unittest.TestCase):
    def test_real_rollout(self):
        self.assertEqual(q.validate()['members'],18)

    def test_missing_member_and_false_acceptance_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            paths=['combined-ai-skill/registry/corpus-projects.json','corpus-factory/evidence-query-rollout.json','scripts/evidence_query.py']
            paths += [str(p.relative_to(q.ROOT)) for p in (q.ROOT/'corpus-factory/evidence-query-snapshots').glob('*.json')]
            for path in paths:
                target=root/path;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(q.ROOT/path,target)
            p=root/'corpus-factory/evidence-query-rollout.json';original=json.loads(p.read_text())
            for change in ['missing','acceptance','pooled']:
                value=copy.deepcopy(original)
                if change=='missing':value['members'].pop()
                elif change=='acceptance':value['expert_acceptance_added']=True
                else:value['unique_inscription_total']=9999
                p.write_text(json.dumps(value))
                with self.assertRaises(ValueError):q.validate(root)

if __name__=='__main__':unittest.main()
