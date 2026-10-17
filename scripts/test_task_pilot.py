import tempfile
import unittest
from pathlib import Path
import task_pilot as t


class PilotTests(unittest.TestCase):
    def test_exact_labels_and_source_boundaries(self):
        atts = [{'sign': 'KU', 'word': 1}, {'sign': 'RO', 'word': 2}]
        self.assertEqual(t.match_slots(atts, ['KU', 'RO']), [])
        atts[1]['word'] = 1
        self.assertEqual(t.match_slots(atts, ['KU', 'RO']), [0])
        self.assertEqual(t.match_slots(atts, ['ku', 'ro']), [])
        atts[0]['word'] = atts[1]['word'] = None
        self.assertEqual(t.match_slots(atts, ['KU', 'RO']), [])

    def test_damaged_labels_not_completed(self):
        self.assertEqual(t.match_slots([{'sign': '[KU]', 'word': 1}, {'sign': 'RO', 'word': 1}], ['KU', 'RO']), [])
        with self.assertRaises(ValueError): t.match_slots([], [])

    def test_real_replay_and_source_mutation(self):
        result = t.build()
        self.assertEqual(result['summary']['source_sequence_matches'], 7)
        self.assertIsNone(result['summary']['meanings_established'])
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            (root / 'research').mkdir()
            (root / 'research/task-pilot.json').write_bytes((t.ROOT / 'research/task-pilot.json').read_bytes())
            (root / 'research/sigla-source-documents.jsonl').write_text('{}')
            with self.assertRaisesRegex(ValueError, 'checksum'): t.build(root)


if __name__ == '__main__': unittest.main()
