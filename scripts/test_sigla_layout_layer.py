import copy
import unittest
from build_sigla_layout_layer import construct, Block


class LayoutTests(unittest.TestCase):
    def fixture(self):
        name = 'SYNTHETIC'
        meta = Block(0, [None]*12)
        meta.fields[1] = name
        att = Block(0, [0, 1, 1, 0, 0, 0, 0, Block(0, [2, 3, 4, 5])])
        doc = Block(0, [meta, 'synthetic/image', 0, Block(0, [20, 20]), Block(0, [att])])
        node = Block(0, [0, name, Block(0, [doc]), 0, 1])
        db = {'data': Block(0, [node])}
        rows = [{'source_record_id': name, 'source_fields': {'attestations': [{}]},
                 'provenance': {'input_sha256': '9a5e4783146144fc5ac54c5dc2b372b39cc0e0ea40ca15207243f8c539f03dd8'}}]
        return db, rows, att, doc

    def test_unreadable_constructor_and_no_admission(self):
        import json
        db, rows, _, _ = self.fixture()
        result = construct(db, rows, b'synthetic')
        layer = json.loads(result['research/sigla-source-layout.json'])
        doc = layer['documents'][0]
        self.assertEqual(doc['rectangles'][0]['reading_state_raw'], 1)
        self.assertFalse(doc['rectangles'][0]['reading_payload_present'])
        self.assertFalse(doc['new_reading_admission'])
        self.assertEqual(doc['rectangles'][0]['rectangle_xywh'], [2, 3, 4, 5])

    def test_out_of_plane_is_not_clipped(self):
        db, rows, att, _ = self.fixture()
        att.fields[7].fields[0] = 30
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')

    def test_slot_coverage_loss(self):
        db, rows, _, _ = self.fixture()
        rows[0]['source_fields']['attestations'].append({})
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')

    def test_identity_and_boolean_coordinate_drift(self):
        db, rows, att, doc = self.fixture()
        doc.fields[0].fields[1] = 'OTHER'
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')
        doc.fields[0].fields[1] = 'SYNTHETIC'
        att.fields[7].fields[0] = True
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')

    def test_duplicate_and_unbound_frozen_ids(self):
        db, rows, _, _ = self.fixture()
        with self.assertRaises(ValueError):
            construct(db, rows + copy.deepcopy(rows), b'synthetic')
        rows[0]['provenance']['input_sha256'] = 'wrong'
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')

    def test_missing_coordinate_plane(self):
        db, rows, _, doc = self.fixture()
        doc.fields[3].fields[0] = 0
        with self.assertRaises(ValueError):
            construct(db, rows, b'synthetic')


if __name__ == '__main__':
    unittest.main()
