"""Validate the bounded source-attribution audit; never adjudicate a reading."""
import argparse
import copy
import csv
import hashlib
import io
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
INPUT='research/legacy-case-attribution.json'
REPORT='analysis/legacy-case-attribution-audit.json'
GUIDE='docs/LEGACY-CASE-ATTRIBUTION.md'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pointer(value,path):
    if not path.startswith('/'):
        raise ValueError('evidence pointer must be absolute JSON pointer')
    for token in path[1:].split('/'):
        token=token.replace('~1','/').replace('~0','~')
        value=value[int(token)] if isinstance(value,list) else value[token]
    return value


def load(root=ROOT):
    return json.loads((Path(root)/INPUT).read_bytes())


def validate(audit,root=ROOT):
    root=Path(root).resolve()
    if audit['format']!='linear-a-legacy-attribution-v1':raise ValueError('audit format drift')
    artifacts={}
    for item in audit['inputs']:
        path=(root/item['path']).resolve()
        if not path.is_relative_to(root) or not path.is_file():raise ValueError('unsafe audit input')
        raw=path.read_bytes()
        if digest(raw)!=item['sha256']:raise ValueError('audit input pin mismatch: '+item['path'])
        if item['path'] in artifacts:raise ValueError('duplicate input')
        artifacts[item['path']]=raw
    required={'data/unresolved_cases.csv','data/rc2_case_register.csv','data/unresolved_cases_rc2.csv','data/visual_evidence_register.csv','data/branch_catalog.csv','research/critical-pilot.json','SOURCE-POLICY.md','research/legacy-case-source-searches.json'}
    if set(artifacts)!=required:raise ValueError('audit input coverage drift')
    search=json.loads(artifacts['research/legacy-case-source-searches.json'])
    pilot=json.loads(artifacts['research/critical-pilot.json'])
    joined={c['case_id']:c for c in pilot['cases'] if c['source_record_id']}
    if {q['case_id'] for q in search['case_queries']}!=set(joined):raise ValueError('source search scope drift')
    cases=audit['cases']
    if len(cases)!=10 or len({c['case_id'] for c in cases})!=10 or {c['case_id'] for c in cases}!=set(joined):raise ValueError('joined case coverage drift')
    ingress=audit['project_ingress']
    if ingress['archive_csv_sha256']!=digest(artifacts['data/unresolved_cases.csv']):raise ValueError('archived queue bytes differ')
    for k in ['earliest_observed_git_commit','normalized_root_commit']:
        if not re.fullmatch('[0-9a-f]{40}',ingress[k]):raise ValueError('invalid historical commit')
    sources={s['source_id']:s for s in audit['sources']}
    if len(sources)!=len(audit['sources']):raise ValueError('duplicate scholarly source')
    for source in sources.values():
        if not source['citation'] or not source['locator'] or not source['consultation']:raise ValueError('unqualified source')
        receipt=source['receipt']
        if not re.fullmatch('[0-9a-f]{64}',receipt['sha256']) or receipt['bytes']<=0 or not receipt['url'].startswith('https://'):raise ValueError('invalid acquisition receipt')
        if source['full_source_redistributed'] is not False or source['independence_established'] is not False:raise ValueError('source rights/independence promotion')
    for c in cases:
        legacy=joined[c['case_id']]
        for key in ['source_record_id','legacy_document_id','legacy_alternatives']:
            if c[key]!=legacy[key]:raise ValueError('case identity/literal drift')
        if not c['finding'] or not c['remaining_evidence_gap']:raise ValueError('missing specific evidence gap')
        if c['pass_status']!='BOUNDED_ATTRIBUTION_PASS_COMPLETE_SCHOLARLY_CASE_OPEN':raise ValueError('scholarly closure promotion')
        for key in ['same_locus_competing_pair_established','independent_witnesses_established','canonical_reading_changed','expert_review_granted']:
            if c[key] is not False:raise ValueError('unsupported scholarly promotion')
        alternatives=[s.strip() for s in c['legacy_alternatives'].split(' vs ')]
        if [a['literal'] for a in c['alternatives']]!=alternatives:raise ValueError('alternative literal changed')
        if any(a['complete_author_source_locus_attribution'] is not False or not a['attribution_status'] for a in c['alternatives']):raise ValueError('unsupported complete alternative attribution')
        entry=next(i for i,e in enumerate(pilot['entries']) if e['source_record_id']==c['source_record_id'])
        for e in c['source_evidence']:
            if e['path']!='research/critical-pilot.json' or not e['pointer'].startswith('/entries/'+str(entry)+'/source_attestations/'):
                raise ValueError('evidence/entry misjoin')
            fields=pointer(pilot,e['pointer'])
            if set(fields)!={'sign','kind','word','series','number','raw_flags'}:raise ValueError('not an admitted source attestation')
        for context in c['published_contexts']:
            if context['source_id'] not in sources or not context['locator'] or not context['finding']:raise ValueError('unbound scholarly context')
    # Specific guards for the exact prior failure modes, not an epigraphic truth test.
    by={c['case_id']:c for c in cases}
    locs=[pointer(pilot,e['pointer']) for e in by['U008']['source_evidence']]
    if [e['number'] for e in locs]!=[567,510] or len({e['pointer'] for e in by['U008']['source_evidence']})!=2:raise ValueError('KH8 distinct-locus evidence drift')
    if by['U001']['alternatives'][0]['attribution_status']!='UNTRACED_ACCOUNT_QUANTITY':raise ValueError('sign number promoted to account quantity')
    if audit['canonical_readings_added']!=0 or audit['source_collated_competing_pairs_added']!=0 or audit['expert_reviews_added']!=0:raise ValueError('unsupported aggregate scholarly promotion')
    return True


def summary(root=ROOT):
    audit=load(root);validate(audit,root)
    return {'format':'linear-a-legacy-attribution-audit-v1','input_path':INPUT,'input_sha256':digest((Path(root)/INPUT).read_bytes()),
            'joined_cases_examined':len(audit['cases']),'alternatives_preserved':sum(len(c['alternatives']) for c in audit['cases']),
            'cases_with_specific_remaining_gaps':sum(bool(c['remaining_evidence_gap']) for c in audit['cases']),
            'qualified_published_contexts':sum(len(c['published_contexts']) for c in audit['cases']),
            'same_locus_competing_pairs_established':0,'canonical_readings_added':0,'expert_reviews_added':0,
            'boundary':'Bounded attribution pass complete; all scholarly cases remain open. New publication context is not new physical evidence or an independently collated alternative pair.'}


def case(case_id,root=ROOT):
    audit=load(root);validate(audit,root)
    found=next((c for c in audit['cases'] if c['case_id']==case_id),None)
    if found is None:raise ValueError('case outside joined attribution scope: '+case_id)
    return copy.deepcopy(found)


def guide(root=ROOT):
    audit=load(root);validate(audit,root)
    lines=['# Linear A: joined legacy-case attribution pass','',audit['scope'],'',
           'All ten cases now have an explicit attribution disposition and remaining evidence gap. None has two attributed readings aligned to the same locus. The old queue and historical registers remain unchanged; this audit qualifies their unsupported claims rather than silently rewriting history.','',
           '## Findings','',
           '- HT17: the authenticated SigLA export has no account-quantity field. A sign identifier numbered37 is not the account quantity37. The old attribution of37 to that export is unsupported; its actual origin remains untraced.',
           '- KH8: A567 and A510 occur at different source slots. The RC2 and original queue do not identify one aligned locus. Do not treat these identifiers as interchangeable alternatives.',
           '- MA10b: the identified Consani2002 passage supports a related vessel-sign discussion, not the full legacy pair. The early register gives no precise Consani publication or locator.',
           '- KNZc6: Flouda’s punctuation report is attributable. Its correspondence to the queued before-IZU break, linguistic function and independent physical adjudication remain unestablished. An old project status saying a physical feature was resolved does not establish these claims.','',
           '## Case-by-case ledger','',
           '| Case | Source record | Disposition | Remaining evidence needed |','|---|---|---|---|']
    for c in audit['cases']:
        lines.append('| '+c['case_id']+' | '+c['source_record_id']+' | '+c['attribution_disposition']+' | '+c['remaining_evidence_gap'].replace('|','\\|')+' |')
    lines+=['','## Identified scholarly context','']
    for source in audit['sources']:
        lines+=['- **'+source['source_id']+'**: '+source['citation']+' '+source['locator']+' Consultation: '+source['consultation']+'. [Source]('+source['receipt']['url']+').']
    lines+=['','These are three qualified publication contexts across three cases: one general sign-class discussion, one related vessel-sign discussion and one punctuation report. They are not three recovered alternative pairs. Accepted DOCX paragraph numbers do not establish final journal pagination. The original PDFs/HTML/DOCX and images are not redistributed.','',
            '## Project history','',
            'The earliest observed Git archive `'+audit['project_ingress']['earliest_observed_git_commit']+'` contains `'+audit['project_ingress']['archive_path']+'`. Its queue bytes match the normalized current CSV. All15 rows entered together without per-reading scholar/publication/locator columns. This identifies project ingress, not the source or authorship before upload. GitHub account authorship is not scholarly attribution.','',
            '## Query and verification','',
            '```sh','python scripts/legacy_case_attribution.py --summary','python scripts/legacy_case_attribution.py --case U008','python scripts/legacy_case_attribution.py --check','python scripts/test_legacy_case_attribution.py','```','',
            '`query_critical_evidence.py --record` returns this attribution overlay beside the unchanged historical cases. The corpus-native evidence profile also exposes an `attribution-audit` collection. Consult this audit before interpreting the old RC2, visual-evidence and branch labels as sourced scholarly disputes.','',
            '## Boundaries and next evidence','',audit['rights_boundary'],'',
            'The historic GORILA quantity assertion is referenced only as existing audit history. No new GORILA-derived transcription or restricted downstream payload was acquired or reconstructed. A failed URL or unsuccessful search is not a finding that a publication or reading does not exist. The finite attribution pass is complete; scholarly resolution, occurrence alignment and expert review are not.','']
    return '\n'.join(lines)


def verify_external_assets(directory,root=ROOT):
    directory=Path(directory).resolve()
    audit=load(root);validate(audit,root)
    for source in audit['sources']:
        p=(directory/source['local_filename']).resolve()
        if not p.is_relative_to(directory) or not p.is_file():raise ValueError('missing/unsafe external source asset')
        raw=p.read_bytes();receipt=source['receipt']
        if digest(raw)!=receipt['sha256'] or len(raw)!=receipt['bytes']:raise ValueError('external source bytes changed: '+source['source_id'])
    return len(audit['sources'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    mode=parser.add_mutually_exclusive_group(required=True)
    parser.add_argument('--source-dir',type=Path,help='Optional private source directory; validates acquired bytes without redistributing them')
    mode.add_argument('--case');mode.add_argument('--summary',action='store_true');mode.add_argument('--check',action='store_true');mode.add_argument('--write',action='store_true')
    args=parser.parse_args()
    try:
        result=summary()
        if args.source_dir:verify_external_assets(args.source_dir)
        if args.case:result=case(args.case)
        elif args.write:
            (ROOT/REPORT).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
            (ROOT/GUIDE).write_text(guide())
        elif args.check:
            if json.loads((ROOT/REPORT).read_text())!=result or (ROOT/GUIDE).read_text()!=guide():raise ValueError('attribution output replay drift')
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,IndexError,OSError) as error:parser.exit(2,str(error)+'\n')


if __name__=='__main__':main()
