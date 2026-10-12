"""Loss, source-boundary and hostile package checks using labelled synthetic rows."""
import hashlib
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from build_mega_corpus import collect, digest, encode, safe_path, verify_package, write_package
from query_mega_corpus import query


class MegaCorpusTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.root = self.base / 'checkouts/Synthetic-Corpus'
        self.root.mkdir(parents=True)
        subprocess.run(['git', 'init', '-q', str(self.root)], check=True)
        self.git('remote', 'add', 'origin', 'https://github.com/synthetic/Synthetic-Corpus.git')
        self.git('config', 'user.name', 'Synthetic')
        self.git('config', 'user.email', 'synthetic@example.invalid')
        self.record = {'id': 'SYNTHETIC-1', 'literal': 'SYNTHETIC ?', 'alternatives': ['SYNTHETIC-A', 'SYNTHETIC-B'], 'accepted': False}
        self.put('data/records.json', [self.record])
        config = {'repository': 'synthetic/Synthetic-Corpus', 'record_sets': [{'name': 'source', 'path': 'data/records.json', 'id_key': 'id', 'unit': 'synthetic_fixture'}]}
        self.put('research/collection-readiness-inputs.json', config)
        self.put('research/collection-work-ledger.json', {'config_sha256': digest((self.root / 'research/collection-readiness-inputs.json').read_bytes()),
             'input_sha256': {'data/records.json': digest((self.root / 'data/records.json').read_bytes())}, 'scientific_approval_granted': False})
        self.put('research/reference-reconciliation-v2.json', {'apparatus': ['SYNTHETIC-UNCERTAINTY']})
        self.git('add', '.')
        self.git('commit', '-q', '-m', 'synthetic fixture')
        self.registry = {'members': [{'repository': 'synthetic/Synthetic-Corpus'}]}
        self.output = self.base / 'package'

    def git(self, *args):
        subprocess.run(['git', *args], cwd=self.root, check=True, capture_output=True)

    def put(self, relative, data):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(encode(data))

    def build(self):
        return write_package(self.base / 'checkouts', self.output, registry=self.registry)

    def test_lossless_payload_and_qualified_query(self):
        self.build()
        result = query(self.output, text='SYNTHETIC', limit=1)
        self.assertEqual(result['records'][0]['source_record'], self.record)
        self.assertIsNone(result['physical_object_count'])
        self.assertFalse(result['scientific_approval_granted'])
        manifest = (self.output / 'manifest.json').read_bytes()
        self.assertTrue(verify_package(self.output, digest(manifest))['external_receipt_checked'])

    def test_payload_tamper_rejected(self):
        self.build()
        with (self.output / 'records.jsonl').open('a') as stream:
            stream.write('{}\n')
        with self.assertRaisesRegex(ValueError, 'payload digest'):
            verify_package(self.output)

    def test_apparatus_loss_rejected(self):
        self.build()
        (self.output / 'members/Synthetic-Corpus/research/reference-reconciliation-v2.json').write_text('{}')
        with self.assertRaisesRegex(ValueError, 'context changed'):
            verify_package(self.output)

    def test_source_drift_rejected(self):
        self.put('data/records.json', [])
        with self.assertRaisesRegex(ValueError, 'stale native evidence'):
            self.build()

    def test_unsafe_and_sealed_paths_rejected(self):
        for path in ['../private.json', '/private.json', 'research/predictions.json', 'data/gold.json', 'research/gorila-extraction.json']:
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_path(self.root, path)

    def test_excluded_or_duplicate_members_rejected(self):
        for repos in [['hawkinsnick/LightroomIsSlow'], ['hawkinsnick/Egyptian-Hieroglyphic-Corpus'], ['synthetic/Synthetic-Corpus'] * 2]:
            with self.assertRaises(ValueError):
                collect(self.base / 'checkouts', {'members': [{'repository': repo} for repo in repos]})

    def test_no_overwrite_or_repository_output(self):
        self.build()
        with self.assertRaises(FileExistsError):
            self.build()
        with self.assertRaisesRegex(ValueError, 'outside corpus'):
            write_package(self.base / 'checkouts', self.root / 'output', registry=self.registry)

    def test_missing_manifest_receipt_and_false_acceptance_rejected(self):
        self.build()
        with self.assertRaisesRegex(ValueError, 'receipt mismatch'):
            verify_package(self.output, '0' * 64)
        manifest = json.loads((self.output / 'manifest.json').read_bytes())
        manifest['scientific_approval_granted'] = True
        (self.output / 'manifest.json').write_bytes(encode(manifest))
        with self.assertRaisesRegex(ValueError, 'approval'):
            verify_package(self.output)

    def configure_local_layers(self):
        self.put('data/occurrences.json', [{'id': 'SYNTHETIC-SLOT', 'uncertain': True}])
        audit = {'documents': 1, 'local_export_manifest': [
            {'file': name, 'sha256': digest((self.root / 'data' / name).read_bytes())}
            for name in ['records.json', 'occurrences.json']]}
        self.put('analysis/source-audit.json', audit)
        config_path = self.root / 'research/collection-readiness-inputs.json'
        config = json.loads(config_path.read_bytes())
        config['record_sets'][0].update(local_only=True, count_path='analysis/source-audit.json', count_pointer='/documents')
        self.put('research/collection-readiness-inputs.json', config)
        ledger_path = self.root / 'research/collection-work-ledger.json'
        ledger = json.loads(ledger_path.read_bytes())
        ledger['config_sha256'] = digest(config_path.read_bytes())
        ledger['input_sha256']['analysis/source-audit.json'] = digest((self.root / 'analysis/source-audit.json').read_bytes())
        self.put('research/collection-work-ledger.json', ledger)

    def test_authenticated_occurrence_layers_travel_with_private_records(self):
        self.configure_local_layers()
        report = write_package(self.base / 'checkouts', self.output, include_local=True, registry=self.registry)
        self.assertEqual(report['record_view_rows'], 1)
        payload = self.output / 'members/Synthetic-Corpus/data/occurrences.json'
        self.assertEqual(payload.read_bytes(), (self.root / 'data/occurrences.json').read_bytes())
        verify_package(self.output)

    def test_auxiliary_layer_drift_is_rejected(self):
        self.configure_local_layers()
        self.put('data/occurrences.json', [])
        with self.assertRaisesRegex(ValueError, 'auxiliary layer digest'):
            write_package(self.base / 'checkouts', self.output, include_local=True, registry=self.registry)


if __name__ == '__main__':
    unittest.main()
