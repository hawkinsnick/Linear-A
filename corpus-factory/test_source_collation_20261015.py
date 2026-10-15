import json
from pathlib import Path
import tempfile
import unittest
from validate_source_collation_20261015 import ROOT, validate


class SelectedCollationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.path = 'corpus-factory/source-collation-2026-10-15.json'
        self.data = json.loads((ROOT/self.path).read_text())
        for path in [self.path,'combined-ai-skill/registry/corpus-projects.json']+[m['snapshot_path'] for m in self.data['members']]:
            p = self.root/path
            p.parent.mkdir(parents=True,exist_ok=True)
            p.write_bytes((ROOT/path).read_bytes())

    def save(self):
        (self.root/self.path).write_text(json.dumps(self.data))

    def test_current(self):
        self.assertEqual(validate()['selected_comparison_tasks'],17)

    def test_no_omitted_member(self):
        self.data['members'].pop()
        self.save()
        with self.assertRaisesRegex(ValueError,'member mismatch'):
            validate(self.root)

    def test_stale_snapshot(self):
        p = self.root/self.data['members'][0]['snapshot_path']
        p.write_text(p.read_text()+'\n')
        with self.assertRaisesRegex(ValueError,'stale'):
            validate(self.root)

    def test_no_acceptance_from_review(self):
        self.data['accepted_readings_added'] = 17
        self.save()
        with self.assertRaisesRegex(ValueError,'promotion'):
            validate(self.root)

    def test_tasks_and_inspections_are_distinct(self):
        self.data['rendered_page_inspections'] = self.data['selected_comparison_tasks']
        self.save()
        with self.assertRaisesRegex(ValueError,'accounting'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
