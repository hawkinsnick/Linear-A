#!/usr/bin/env python3
"""Reproduce bounded academic-audit diagnostics; never admit readings or identities."""
import argparse
import collections
import csv
import hashlib
import importlib.util
import json
from pathlib import Path


def probe(checkouts):
    inputs = []
    def raw(repo, path):
        b = (checkouts / repo / path).read_bytes()
        inputs.append({'repository': 'hawkinsnick/' + repo, 'path': path,
                       'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b)})
        return b
    def load(repo, path):
        return json.loads(raw(repo, path))
    la = checkouts / 'Linear-A'
    implementation = raw('Linear-A', 'scripts/run_structural_sensitivity_v1.py')
    module_spec = importlib.util.spec_from_file_location('conditional_sensitivity', la / 'scripts/run_structural_sensitivity_v1.py')
    s = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(s)
    raw('Linear-A', 'data/source_words.csv')
    raw('Linear-A', 'data/candidate_registry_0.9.csv')
    words, candidates = s.load_inputs(la / 'data/source_words.csv', la / 'data/candidate_registry_0.9.csv')
    protocol = load('Linear-A', 'research/structural-sensitivity-repair-v1.json')
    if hashlib.sha256(implementation).hexdigest() != protocol['implementation_sha256']:
        raise ValueError('conditional sensitivity implementation changed')
    for path, field in [('data/source_words.csv', 'words_sha256'), ('data/candidate_registry_0.9.csv', 'candidates_sha256')]:
        if hashlib.sha256((la / path).read_bytes()).hexdigest() != protocol[field]:
            raise ValueError('historical diagnostic input changed: ' + path)
    types = collections.Counter(seq for doc, seq in words)
    prefixes = collections.Counter(doc.split(' ')[0] for doc, seq in words)
    all_docs = {doc for doc, seq in words}
    families = sorted({doc[:-1] for doc in all_docs if doc.endswith('a') and doc[:-1] + 'b' in all_docs})
    grouped = [(doc[:-1] if doc.endswith(('a', 'b')) and doc[:-1] in families else doc, seq) for doc, seq in words]
    original = load('Linear-A', 'analysis/structural-sensitivity-repair-v1-result.json')
    bootstrap = s.cluster_bootstrap(grouped, candidates, protocol)
    excluded = [seq for doc, seq in words if doc.split(' ')[0] != 'HT']
    contrasts = [{'candidate_id': c['candidate_id'],
                  'all': s.moments([seq for doc, seq in words], c['sign_id'], c['position']),
                  'without_HT_prefix': s.moments(excluded, c['sign_id'], c['position'])}
                 for c in candidates]
    x = raw('Milyan-Lycian-B', 'data/reference/ediana-milyan-source.json')
    y = raw('Lycian-and-Carian', 'data/raw/ediana/milyan-1-0.json')
    csg = load('Cypriot-syllabic-Greek', 'exports/corpus.json')['records']
    etec = load('Eteocypriot', 'exports/corpus.json')['records']
    a, b = {r['source_id'] for r in csg}, {r['source_id'] for r in etec}
    admissions = []
    for repo in ['Lydian', 'Sidetic', 'Pisidian']:
        rows = load(repo, 'analysis/record-admission.json')
        admissions.append({'repository': repo, 'records': len(rows),
                           'analytical_admissions': sum(row['analytical_admission'] for row in rows),
                           'lines': sum(len(row['lines']) for row in rows),
                           'edition_locator_states': dict(sorted(collections.Counter(row.get('edition_locator_status') for row in rows).items())),
                           'unflagged_but_unadjudicated_lines': sum(not line['syntactic_flags'] and line['epigraphic_certainty'] == 'NOT_ADJUDICATED' for row in rows for line in row['lines'])})
    cm = load('Cypro-Minoan', 'analysis/occurrence-coverage-v1.json')
    ch = load('Cretan-hieroglyphs', 'analysis/current-status.json')['committed_evidence_counts']
    legacy = load('Linear-A', 'analysis/legacy-case-attribution-audit.json')
    prospective = load('Linear-A', 'analysis/prospective-independence-audit-v1.json')
    disc = load('Phaistos-Disc', 'analysis/acceptance-2.0.json')
    return {'format': 'adversarial-academic-audit-probes-v1',
            'scope': 'Deterministic checks of repository assertions and post hoc sensitivity diagnostics; not external epigraphic review.',
            'inputs': inputs,
            'linear_a': {'serialized_word_rows': sum(1 for _ in csv.DictReader((la / 'data/source_words.csv').open())),
                         'nonempty_source_word_tokens': len(words), 'source_word_types': len(types),
                         'hapax_types': sum(n == 1 for n in types.values()),
                         'document_labels': len(all_docs), 'prefix_counts': dict(sorted(prefixes.items())),
                         'leave_HT_token_count': len(excluded), 'leave_HT_moments': contrasts,
                         'a_b_diagnostic': {'rule': 'Merge only exact source labels ending a/b when BOTH labels exist. This is an unverified sensitivity grouping, not a certified physical-object join.',
                                            'label_families': len(families), 'clusters': len({doc for doc, seq in grouped}),
                                            'replicates': protocol['bootstrap_replicates'], 'seed': protocol['cluster_seed'],
                                            'original_lower_z_above_1_96_count': sum(r['document_cluster_bootstrap']['p025_z'] > 1.96 for r in original['results']),
                                            'diagnostic_lower_z_above_1_96_count': sum(r['p025_z'] > 1.96 for r in bootstrap),
                                            'results': [{'candidate_id': c['candidate_id'], 'original': old['document_cluster_bootstrap'], 'diagnostic': new} for c, old, new in zip(candidates, original['results'], bootstrap)],
                                            'significance_claim_allowed': False},
                         'legacy_attribution': legacy, 'prospective_independence': prospective},
            'source_overlap': {'milyan_bytes_identical': x == y,
                               'milyan_shared_source_sha256': hashlib.sha256(x).hexdigest(),
                               'milyan_nonempty_source_rows': sum(bool(row.get('sentence')) for rows in json.loads(x).values() for row in rows),
                               'cypriot_full_index_source_ids': len(a), 'eteocypriot_source_ids': len(b),
                               'shared_cypriot_source_ids': len(a & b),
                               'all_eteocypriot_ids_in_full_index': b <= a},
            'reference_admissions': admissions,
            'cypro_minoan': {'rich_records': cm['rich_records'], 'covered_rich_records': cm['records_with_encoded_occurrences'],
                             'encoded_occurrences': cm['encoded_occurrences'],
                             'source_strata': [{'source_id': t['source_id'], 'source_role': t['source_role'], 'occurrences': t['occurrences']} for t in cm['source_strata']]},
            'cretan_hieroglyphic': ch,
            'phaistos_disc': {'final_release_allowed': disc['final_2_0_allowed'], 'occurrence_audit_counts': disc['occurrence_audit_counts'], 'review_evidence': disc['review_evidence']},
            'scholarly_acceptance_granted': False,
            'diagnostic_warning': 'All new sensitivity checks are post hoc, use the selected historical candidates and are not preregistered confirmation. The 1.96 summary is a historical diagnostic convention, not an inferential bootstrap test.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkouts', required=True, type=Path)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--compare', type=Path)
    args = parser.parse_args()
    result = probe(args.checkouts.resolve())
    if args.compare and json.loads(args.compare.read_text()) != result:
        raise ValueError('audit inputs or diagnostic results differ from the saved audit')
    if args.output:
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'status': 'PASS_BOUNDED_AUDIT_PROBES', 'input_artifacts': len(result['inputs']),
                      'scientific_acceptance': False, 'new_confirmatory_test': False}))


if __name__ == '__main__':
    main()
