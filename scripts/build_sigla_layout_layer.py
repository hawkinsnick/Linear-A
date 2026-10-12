"""Retain source rectangles from pinned, licensed SigLA data; no new readings."""
import argparse
import hashlib
import json
from pathlib import Path
from sigla_marshal import Block, load_database

ROOT = Path(__file__).resolve().parents[1]
PIN = 'cc624f148fd84c94fd2910b0adf92ecace25f52f9175664122bdf8384a8f1b9d'
OUTPUT = 'research/sigla-source-layout.json'
AUDIT = 'analysis/sigla-layout-audit.json'
FROZEN = 'research/sigla-source-documents.jsonl'
ATTRIBUTION = 'Ester Salgarella and Simon Castellan, SigLA: The Signs of Linear A'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + '\n').encode()


def block(value, length, label):
    if not isinstance(value, Block) or value.tag != 0 or len(value.fields) != length:
        raise ValueError('source schema drift: ' + label)
    return value.fields


def map_rows(node):
    if node == 0:
        return
    left, key, value, right, height = block(node, 5, 'document map')
    if not isinstance(height, int) or isinstance(height, bool):
        raise ValueError('invalid map height')
    yield from map_rows(left)
    yield key, value
    yield from map_rows(right)


def integers(value, length, label):
    values = block(value, length, label)
    if any(not isinstance(x, int) or isinstance(x, bool) for x in values):
        raise ValueError('noninteger source coordinates')
    return list(values)


def construct(database, frozen_rows, frozen_raw):
    data = block(database['data'], 1, 'database envelope')[0]
    frozen = {}
    for ix, row in enumerate(frozen_rows):
        rid = row['source_record_id']
        if rid in frozen or row['provenance']['input_sha256'] != '9a5e4783146144fc5ac54c5dc2b372b39cc0e0ea40ca15207243f8c539f03dd8':
            raise ValueError('unbound or duplicate frozen source')
        frozen[rid] = (ix, row)
    docs, seen, total = [], set(), 0
    for name, wrapper in map_rows(data):
        if not isinstance(name, str) or name in seen or name not in frozen:
            raise ValueError('orphan or duplicate source document')
        seen.add(name)
        inner = block(wrapper, 1, 'document wrapper')[0]
        meta, path, sequences, image_size, attestations = block(inner, 5, 'document')
        metadata = block(meta, 12, 'document metadata')
        if metadata[1] != name or not isinstance(path, str):
            raise ValueError('source document identity disagreement')
        size = integers(image_size, 2, 'image size')
        if min(size) <= 0:
            raise ValueError('missing coordinate plane')
        if not isinstance(attestations, Block) or attestations.tag != 0:
            raise ValueError('attestation array schema drift')
        ix, old = frozen[name]
        old_atts = old['source_fields']['attestations']
        if len(attestations.fields) != len(old_atts):
            raise ValueError('frozen/direct slot count drift')
        boxes = []
        for slot, att in enumerate(attestations.fields):
            fields = block(att, 8, 'attestation')
            number = fields[2]
            if not isinstance(number, int) or isinstance(number, bool):
                raise ValueError('invalid source number')
            rect = integers(fields[7], 4, 'source rectangle')
            x, y, w, h = rect
            if min(rect) < 0 or x+w > size[0] or y+h > size[1]:
                raise ValueError('source rectangle outside its plane; inspect rather than clip')
            reading = fields[1]
            if isinstance(reading, int):
                if reading not in (0, 1):
                    raise ValueError('unknown reading constructor')
                flag = None
            else:
                flag = block(reading, 2, 'reading envelope')[1]
            if flag is not None and (not isinstance(flag, int) or isinstance(flag, bool)):
                raise ValueError('reading flag schema drift')
            if fields[4] not in (0, 1) or fields[6] not in (0, 1):
                raise ValueError('boolean source flag drift')
            boxes.append({'source_array_index': slot, 'source_number_raw': number,
                          'rectangle_xywh': rect, 'reading_payload_present': isinstance(reading, Block),
                          'reading_state_raw': reading if isinstance(reading, int) else None,
                          'reading_flag_raw': flag, 'erasure_raw': fields[4],
                          'ghost_raw': fields[6],
                          'frozen_attestation_pointer': f'/documents/{ix}/attestations/{slot}'})
        total += len(boxes)
        docs.append({'id': name, 'source_image_path': path, 'source_image_size': size,
                     'rectangles': boxes,
                     'provenance': {'source_url': 'https://sigla.phis.me/database.js',
                        'source_sha256': PIN, 'source_map_key': name,
                        'license': 'CC BY-NC-SA 4.0', 'attribution': ATTRIBUTION},
                     'unit': 'SOURCE_DOCUMENT_LAYOUT',
                     'physical_object_identity_certified': False,
                     'coordinate_space': 'SOURCE_IMAGE_PLANE; NOT_PHYSICAL_METROLOGY',
                     'new_reading_admission': False})
    if seen != set(frozen):
        raise ValueError('source document coverage loss')
    layer = {'schema_version': '1.0', 'documents': docs,
             'boundary': 'SigLA source rectangles and uninterpreted flags only. No image redistributed, no new reading accepted, no ancient physical measurement or independent witness established. Slot pointers follow source array order; source record numbers are not canonical sign numbers.'}
    raw = encode(layer)
    audit = {'schema_version': '1.0', 'source_sha256': PIN,
             'frozen_source_layer_sha256': digest(frozen_raw),
             'documents': len(docs), 'source_rectangles': total,
             'layout_sha256': digest(raw), 'images_redistributed': False,
             'new_readings_admitted': 0, 'physical_identity_certified': False,
             'interpretation_authority': 'SigLA published application: Core_Rect xywh, document image_size and attestation position serializers; see research/sigla-layout-source-inspection.json',
             'frozen_slot_mapping': 'Same upstream database SHA and document/array structure; independent exporter replay has one preserved reading-classification difference, not a source-byte change.'}
    return {OUTPUT: raw, AUDIT: encode(audit)}


def build(source):
    raw = Path(source).read_bytes()
    if digest(raw) != PIN:
        raise ValueError('source digest drift; inspect before changing pin')
    frozen_raw = (ROOT/FROZEN).read_bytes()
    return construct(load_database(source), [json.loads(x) for x in frozen_raw.splitlines()], frozen_raw)


def validate():
    layer_raw = (ROOT/OUTPUT).read_bytes()
    layer = json.loads(layer_raw)
    audit = json.loads((ROOT/AUDIT).read_bytes())
    if digest(layer_raw) != audit['layout_sha256'] or audit['source_sha256'] != PIN:
        raise ValueError('layout receipt drift')
    if digest((ROOT/FROZEN).read_bytes()) != audit['frozen_source_layer_sha256']:
        raise ValueError('frozen source layer drift')
    docs = layer['documents']
    if len(docs) != audit['documents'] or len({d['id'] for d in docs}) != len(docs):
        raise ValueError('layout document coverage drift')
    if sum(len(d['rectangles']) for d in docs) != audit['source_rectangles']:
        raise ValueError('source rectangle loss')
    for d in docs:
        if d['new_reading_admission'] is not False or d['physical_object_identity_certified'] is not False or d['provenance']['license'] != 'CC BY-NC-SA 4.0':
            raise ValueError('unsupported admission or rights change')
    return audit


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('source', nargs='?', type=Path)
    p.add_argument('--write', action='store_true')
    a = p.parse_args()
    if a.source:
        for name, raw in build(a.source).items():
            if a.write:
                (ROOT/name).write_bytes(raw)
            elif (ROOT/name).read_bytes() != raw:
                raise ValueError('source layout replay drift: ' + name)
    elif a.write:
        p.error('--write requires pinned source bytes')
    print(json.dumps(validate(), indent=2))
