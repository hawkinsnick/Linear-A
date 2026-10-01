"""Membership audit only: do not open or score prospective candidate outcomes."""
import collections, json, pathlib
R=pathlib.Path(__file__).resolve().parents[1]
def audit(report):
    rows=report['rows']
    labels=[x['label'] for x in rows]
    if len(labels)!=report['cohort_labels'] or len(labels)!=len(set(labels)):
        raise ValueError('incomplete or duplicate frozen cohort membership')
    if report['candidate_outcomes_evaluated'] is not False:
        raise ValueError('membership audit cannot certify uninspected outcomes')
    counts=collections.Counter()
    for row in rows:
        old,new=row['v3_documents'],row['v4_documents']
        expected='PRESENT_IN_V3' if old else 'ABSENT_FROM_V3_PRESENT_IN_V4' if new else 'UNRESOLVED'
        if row['state']!=expected:raise ValueError('membership state inconsistent with evidence')
        counts[expected]+=1
    return {'scope':'Frozen cohort input membership only; no candidate outcome scoring.',
            'cohort_labels':len(rows),'membership_counts':dict(sorted(counts.items())),
            'historical_analytical_input_identity':report['historical_analytical_input_identity'],
            'entire_cohort_unseen_relative_to_v3':not bool(counts['PRESENT_IN_V3']),
            'prospective_scoring_allowed':False,'prospective_outcomes_evaluated':False,
            'conditional_statistical_repair':'Separate same-corpus descriptive analysis; does not establish original analytical input identity or prospective independence.',
            'next_proof':'Authenticate original analytical-input bytes and pre-analysis exposure history for every frozen label. Retain all 24 labels; do not silently remove the seven already present in v3.'}
if __name__=='__main__':
    print(json.dumps(audit(json.loads((R/'analysis/sigla-cohort-input-membership.json').read_text())),indent=2)+'\n',end='')
