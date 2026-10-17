#!/usr/bin/env python3
"""Deterministic, checksummed, offline-replayable public-source research package."""
import argparse
import hashlib
import io
import json
from pathlib import Path
import tempfile
import zipfile

import export_research_layer as exports
from research_readiness import build, REPORT

ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    'research/sigla-source-documents.jsonl', 'research/sigla-source-groups.jsonl',
    'research/sigla-source-signs.jsonl', 'analysis/public-sigla-layer-audit.json',
    'scripts/research_api.py', 'scripts/build_source_context.py',
    'scripts/export_research_layer.py', 'scripts/research_readiness.py',
    'scripts/build_research_package.py', 'docs/NORTHWESTERN-RESEARCH-READINESS.md',
    'DATA-LICENSE-MATRIX.md', 'THIRD-PARTY-NOTICES.md', 'NOTICE',
    'LICENSE', 'LICENSE-CODE', 'LICENSE-CONTENT.md', 'LICENSING.md', 'SOURCE-POLICY.md'
]


def package():
    report = build()
    payload = {p:(ROOT/p).read_bytes() for p in SOURCES}
    payload[REPORT] = (json.dumps(report, ensure_ascii=False, indent=2)+'\n').encode()
    with tempfile.TemporaryDirectory() as td:
        for resource in ('documents', 'source_words', 'signs'):
            for fmt in ('json', 'csv', 'jsonld', 'epidoc'):
                name = resource+'.'+fmt
                out = Path(td)/name
                exports.write_export(resource, fmt, out)
                payload['exports/'+name] = out.read_bytes()
                payload['exports/'+name+'.manifest.json'] = out.with_suffix(out.suffix+'.manifest.json').read_bytes()
    manifest = {'format':'linear-a-research-package-v1',
                'scope':report['scope'], 'expert_review_completed':False,
                'replay':'python scripts/build_research_package.py replay.zip',
                'files':[{'path':p, 'sha256':hashlib.sha256(raw).hexdigest(), 'bytes':len(raw)}
                         for p,raw in sorted(payload.items())]}
    payload['package-manifest.json'] = (json.dumps(manifest, indent=2)+'\n').encode()
    buf = io.BytesIO()
    # Fixed timestamps, permissions and order; ZIP_STORED avoids zlib-version drift.
    with zipfile.ZipFile(buf, 'w', compression=zipfile.ZIP_STORED) as z:
        for path, raw in sorted(payload.items()):
            info = zipfile.ZipInfo(path, date_time=(1980,1,1,0,0,0))
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            z.writestr(info, raw)
    return buf.getvalue()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('output', type=Path)
    args = p.parse_args()
    raw = package()
    args.output.write_bytes(raw)
    args.output.with_suffix(args.output.suffix+'.sha256').write_text(
        hashlib.sha256(raw).hexdigest()+'  '+args.output.name+'\n', encoding='utf-8')
    print('Built public-source research package:', args.output.name)


if __name__ == '__main__':
    main()
