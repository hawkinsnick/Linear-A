"""Query a local combined research package without pooling native populations."""
import argparse
import json
from pathlib import Path
from build_mega_corpus import verify_package


def query(package, repository=None, view=None, text=None, key=None, limit=20):
    if not 1 <= limit <= 1000:
        raise ValueError('limit must be between 1 and 1000')
    verify_package(package)
    result, matched = [], 0
    with (Path(package) / 'records.jsonl').open() as stream:
        for line in stream:
            row = json.loads(line)
            if repository and row['repository'] != repository:
                continue
            if view and row['view'] != view:
                continue
            if key and row['record_key'] != key:
                continue
            if text and text.casefold() not in json.dumps(row['source_record'], ensure_ascii=False).casefold():
                continue
            matched += 1
            if len(result) < limit:
                result.append(row)
    return {'matched_view_rows': matched, 'returned_rows': len(result), 'records': result,
            'physical_object_count': None, 'independent_witness_count': None,
            'scientific_approval_granted': False,
            'boundary': 'Read each result with its component context and native AI skill; source assertions and overlapping views retain their own units.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('package', type=Path)
    parser.add_argument('--repository')
    parser.add_argument('--view')
    parser.add_argument('--text')
    parser.add_argument('--key')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()
    print(json.dumps(query(args.package, args.repository, args.view, args.text, args.key, args.limit), ensure_ascii=False, indent=2))
