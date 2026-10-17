#!/usr/bin/env python3
"""Round trips, provenance rejection, semantic boundaries and offline replay."""
import csv
import hashlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
import zipfile

import build_research_package as pkg
import build_source_context as context
import export_research_layer as ex
import research_api as api
import research_readiness as audit


class Readiness(unittest.TestCase):
    def test_context_fields_and_units(self):
        docs = {r['source_record_id']:r for r in api.rows('documents')}
        assertions = context.build()
        keys = {(c['document_id'],c['source_field']):c for c in assertions}
        for docid, d in docs.items():
            for field in ('typology','dimensions_cm'):
                value = d['source_fields'][field]
                if value not in (None, ''):
                    c = keys[docid,field]
                    self.assertEqual(c['asserted_value'], value)
                    self.assertEqual(c['source_locator'],d['provenance']['json_pointer']+'/'+field)
                    self.assertEqual(c['input_sha256'],d['provenance']['input_sha256'])
                    self.assertEqual(c['certainty'],'SOURCE_REPORTED')
                    if field == 'dimensions_cm': self.assertEqual(c['units'],'cm')

    def test_all_exports_round_trip(self):
        with tempfile.TemporaryDirectory() as td:
            for resource in ('documents','source_words','signs'):
                original = list(api.rows(resource))
                for fmt in ('json','csv','jsonld','epidoc'):
                    with self.subTest(resource=resource, format=fmt):
                        out = Path(td)/(resource+'.'+fmt)
                        m = ex.write_export(resource,fmt,out)
                        raw = out.read_bytes()
                        self.assertEqual(m['output']['sha256'],hashlib.sha256(raw).hexdigest())
                        self.assertEqual(m['source_snapshot']['sha256'],hashlib.sha256((api.ROOT/api.FILES[resource]).read_bytes()).hexdigest())
                        self.assertEqual(m['record_count'],len(original))
                        self.assertEqual(m['epistemic_status'],'SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED')
                        if fmt == 'json': restored = json.loads(raw)
                        elif fmt == 'csv': restored = [json.loads(r['record_json']) for r in csv.DictReader(io.StringIO(raw.decode()))]
                        elif fmt == 'jsonld':
                            graph = json.loads(raw)['@graph']
                            self.assertEqual(len({r['@id'] for r in graph}),len(original))
                            self.assertTrue(all(r['@id'].startswith('urn:linear-a:') for r in graph))
                            restored = [r['record'] for r in graph]
                        else: restored = [json.loads(n.text) for n in ET.fromstring(raw).findall('.//{http://www.tei-c.org/ns/1.0}note')]
                        self.assertEqual(restored,original)
                        ex.write_export(resource,fmt,out)
                        self.assertEqual(raw,out.read_bytes())

    def copy_source(self, root):
        for p in [*api.FILES.values(),'analysis/public-sigla-layer-audit.json']:
            source = api.ROOT/p
            if source.exists():
                (root/p).parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(source,root/p)

    def test_tampered_source_rejected_before_export(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.copy_source(root)
            p = root/api.FILES['documents']; p.write_bytes(p.read_bytes()+b'\n')
            with self.assertRaisesRegex(ValueError,'checksum'): audit.build(root)
            with patch.object(ex,'ROOT',root):
                with self.assertRaisesRegex(ValueError,'checksum'): ex.write_export('documents','json',root/'out.json')
            self.assertFalse((root/'out.json').exists())

    def test_semantic_promotions_and_orphan_rejected(self):
        mutations = [
            ('documents', lambda r:r.update(physical_object_identity_certified=True)),
            ('source_words', lambda r:r.update(definition='confirmed linguistic word')),
            ('signs', lambda r:r.update(linear_a_phonetic_value='da')),
            ('source_words', lambda r:r.update(document_id='INVENTED')),
        ]
        for resource, mutate in mutations:
            with self.subTest(resource=resource), tempfile.TemporaryDirectory() as td:
                root = Path(td); self.copy_source(root)
                p = root/api.FILES[resource]
                data = [json.loads(l) for l in p.read_text().splitlines()]
                mutate(data[0])
                p.write_text(''.join(json.dumps(r)+'\n' for r in data))
                a = root/'analysis/public-sigla-layer-audit.json'; d=json.loads(a.read_text())
                next(e for e in d['files'] if e['path']==api.FILES[resource])['sha256']=hashlib.sha256(p.read_bytes()).hexdigest()
                a.write_text(json.dumps(d))
                with self.assertRaises(ValueError): audit.build(root)

    def test_package_integrity_and_offline_replay(self):
        raw = pkg.package()
        self.assertEqual(raw,pkg.package())
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with zipfile.ZipFile(io.BytesIO(raw)) as z:
                manifest=json.loads(z.read('package-manifest.json'))
                self.assertFalse(manifest['expert_review_completed'])
                for e in manifest['files']:
                    self.assertEqual(e['sha256'],hashlib.sha256(z.read(e['path'])).hexdigest())
                z.extractall(root)
            subprocess.run([sys.executable,'scripts/build_research_package.py','replay.zip'],cwd=root,check=True,capture_output=True)
            self.assertEqual(raw,(root/'replay.zip').read_bytes())


if __name__ == '__main__': unittest.main()
