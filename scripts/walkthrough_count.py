"""Count the public source view without pooling objects or interpreting blanks."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'research/sigla-source-documents.jsonl'
raw = path.read_bytes()
rows = [json.loads(line) for line in raw.decode('utf-8').splitlines() if line.strip()]
selected = [r for r in rows if r['source_record_id'] == 'ARKH 1a']
if len(selected) != 1:
    raise SystemExit('Expected exactly one ARKH 1a source entry; inspect this snapshot.')
slots = selected[0]['source_fields']['attestations']
print(json.dumps({
    'source_path': path.relative_to(ROOT).as_posix(),
    'source_sha256': hashlib.sha256(raw).hexdigest(),
    'source_document_entries': len(rows),
    'attestation_slots': sum(len(r['source_fields']['attestations']) for r in rows),
    'selected_id': 'ARKH 1a',
    'selected_slots': len(slots),
    'selected_blank_kind_slots': sum(s['kind'] == 'blank' for s in slots),
    'selected_nonempty_sign_labels': sum(bool(s['sign']) for s in slots),
    'scope': 'All nonempty JSONL rows; all attestation slots retained, including blanks. '
             'Source entries are not certified unique objects; sign labels are not translations.'
}, indent=2))
