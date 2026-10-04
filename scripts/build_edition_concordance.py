"""Build bibliographic accounting for every authenticated SigLA source entry."""
import argparse,collections,csv,hashlib,io,json,re
from pathlib import Path
from urllib.parse import urlsplit,parse_qs,urlencode
ROOT=Path(__file__).resolve().parents[1]
PIN='9a5e4783146144fc5ac54c5dc2b372b39cc0e0ea40ca15207243f8c539f03dd8'
CSV='research/edition-concordance.csv';REPORT='analysis/edition-concordance-audit.json'
FIELDS=['source_record_id','source_pointer','sigla_status','gorila_status','gorila_volume','gorila_viewer_page','gorila_source_url','inspected_case_ids','inspected_locators_json','rp1980_status','rp1994_status','rila_s1_status','rila_s1_source_url','rila_s1_candidate_section_start','reference_gap','physical_object_identity_certified']
def digest(b):return hashlib.sha256(b).hexdigest()
def key(x):return re.sub(r'\s+','',x)
def gorila_locator(url):
 p=urlsplit(url);q=parse_qs(p.query)
 if p.scheme!='https' or p.netloc!='cefael.efa.gr':return None
 required={'site_id':['1'],'actionID':['page'],'serie_id':['EtCret'],'volume_number':['21']}
 if any(q.get(k)!=v for k,v in required.items()):raise ValueError('unexpected GORILA route parameters')
 vol=q.get('issue_number',[]);page=q.get('sp',[])
 if len(vol)!=1 or vol[0] not in {'1','2','3','4','5'} or len(page)!=1 or not page[0].isdigit() or int(page[0])<1:raise ValueError('invalid GORILA locator')
 clean={k:q[k][0] for k in ['site_id','actionID','serie_id','volume_number','issue_number','sp']}
 return vol[0],page[0],'https://cefael.efa.gr/detail.php?'+urlencode(clean)
def build(raw,root=ROOT):
 root=Path(root)
 if digest(raw)!=PIN:raise ValueError('source checksum mismatch')
 source=json.loads(raw);docs=source['documents'];ids=[d['id'] for d in docs]
 if len(ids)!=802 or len(set(ids))!=802 or source['_meta']['license']!='CC BY-NC-SA 4.0':raise ValueError('source identity or rights mismatch')
 route_path='research/edition-route-evidence.json';primary_path='analysis/pre-expert-primary-collation.json'
 routes=json.loads((root/route_path).read_text());primary=json.loads((root/primary_path).read_text())
 if any(routes['editions'][v]['entry_content_inspected'] for v in ['RP1980','RP1994','RILA-S1']):raise ValueError('edition inspection promotion requires new evidence and implementation')
 lookup=collections.defaultdict(list)
 for c in primary['cases']:
  if c.get('expert_validated') or c.get('physical_reading_adjudicated'):raise ValueError('existing primary audit promoted')
  if any(e.get('edition')=='Godart & Olivier, GORILA' for e in c.get('evidence',[])):lookup[key(c['document_id'])].append(c)
 rows=[]
 for i,d in enumerate(docs):
  url=d.get('reference_url') or '';loc=gorila_locator(url);cases=lookup.get(key(d['id']),[])
  if not loc and url and url!='missing' and urlsplit(url).netloc!='editions.efa.gr':raise ValueError('unclassified source URL')
  inspected=[]
  for c in cases:
   for e in c['evidence']:
    if e.get('edition')=='Godart & Olivier, GORILA':
     if e.get('inspection')!='AI_VISUAL_PAGE_INSPECTION_NOT_EXPERT_AUTOPSY' or not re.fullmatch('[0-9a-f]{64}',e.get('locally_inspected_page_sha256','')):raise ValueError('unbound primary inspection')
     record={k:e[k] for k in ['volume','printed_page','viewer_page','url','locally_inspected_page_sha256']}
     if record not in inspected:inspected.append(record)
  later=urlsplit(url).netloc=='editions.efa.gr' and parse_qs(urlsplit(url).query)=={'r':['publication'],'id':['1050']}
  if urlsplit(url).netloc=='editions.efa.gr' and not later:raise ValueError('unclassified later-edition route')
  section=routes['editions']['RILA-S1']['tablet_section_start_pages'].get(d['id'].split()[0]) if later and d['typology']=='Tablet' else None
  rows.append(dict(zip(FIELDS,[d['id'],f'/documents/{i}','ATTRIBUTED_EXACT_SOURCE_RECORD',('PRIMARY_CASE_PAGES_INSPECTED' if cases else 'SOURCE_REPORTED_PAGE_LOCATOR') if loc else ('SOURCE_POINTS_TO_LATER_EDITION' if later else 'UNRESOLVED_NO_USABLE_REFERENCE'),loc[0] if loc else '',loc[1] if loc else '',loc[2] if loc else '', '|'.join(c['case_id'] for c in cases),json.dumps(inspected,ensure_ascii=False,separators=(',',':')),'UNRESOLVED_EDITION_CONTENT_NOT_ACQUIRED','UNRESOLVED_EDITION_CONTENT_NOT_ACQUIRED','SOURCE_REPORTED_PUBLICATION_SECTION_CANDIDATE' if later else 'UNRESOLVED_NOT_RECONCILED',routes['editions']['RILA-S1']['publisher_url'] if later else '',section or '',('LITERAL_MISSING' if url=='missing' else 'ABSENT' if not url else ''),'false'])))
 out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=FIELDS,lineterminator='\n');w.writeheader();w.writerows(rows);table=out.getvalue().encode()
 counts=lambda f:dict(sorted(collections.Counter(r[f] for r in rows).items()))
 bound_cases={c for r in rows for c in r['inspected_case_ids'].split('|') if c};unbound=[c['case_id'] for cs in lookup.values() for c in cs if c['case_id'] not in bound_cases]
 report={'format':'linear-a-edition-concordance-audit-v1','scope':'All 802 entries in the exact authenticated snapshot; not all surviving inscriptions, objects or independent witnesses.','source_sha256':PIN,'source_id_universe_sha256':digest(json.dumps(ids,ensure_ascii=False,separators=(',',':')).encode()),'input_hashes':{p:digest((root/p).read_bytes()) for p in [route_path,primary_path]},'concordance_sha256':digest(table),'row_count':len(rows),'unique_source_ids':len(set(ids)),'sigla_status_counts':counts('sigla_status'),'gorila_status_counts':counts('gorila_status'),'gorila_volume_counts':dict(sorted(collections.Counter(r['gorila_volume'] for r in rows if r['gorila_volume']).items())),'rp1980_status_counts':counts('rp1980_status'),'rp1994_status_counts':counts('rp1994_status'),'rila_s1_status_counts':counts('rila_s1_status'),'reference_gap_counts':counts('reference_gap'),'primary_case_entries_bound_to_source_records':len(bound_cases),'primary_inspected_source_records':sum(bool(r['inspected_case_ids']) for r in rows),'primary_case_ids_without_exact_source_id_join':unbound,'inspected_pages_are_independent_verification':False,'certified_physical_object_count':None,'canonical_readings_added':0,'prospective_outcomes_inspected':False,'completion':'STEP_1_CURRENT_RECORD_ACCOUNTING_COMPLETE_EDITION_RESOLUTION_PARTIAL','boundary':'Whitespace-only joins preserve suffixes, faces, plus signs and fragment labels. Viewer indices are not printed page numbers. Publication/section links are not exact inscription matches. Unresolved does not mean absent from an edition. Raison–Pope and later entry readings remain uncollated.','rights':{'source_derived_identifier_locator_table':'CC BY-NC-SA 4.0; Ester Salgarella and Simon Castellan, SigLA, via Ryan Pavlicek/pyaegean authenticated derivative','original_audit_tooling':'Repository software terms','edition_images_and_transcriptions_redistributed':False}}
 return table,(json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode()
def validate_committed(root=ROOT):
 root=Path(root);report=json.loads((root/REPORT).read_text());raw=(root/CSV).read_bytes();rows=list(csv.DictReader(io.StringIO(raw.decode())))
 if digest(raw)!=report['concordance_sha256'] or len(rows)!=802 or len({r['source_record_id'] for r in rows})!=802:raise ValueError('concordance integrity/coverage drift')
 if digest(json.dumps([r['source_record_id'] for r in rows],ensure_ascii=False,separators=(',',':')).encode())!=report['source_id_universe_sha256']:raise ValueError('identity universe drift')
 for p,h in report['input_hashes'].items():
  if digest((root/p).read_bytes())!=h:raise ValueError('source evidence drift')
 primary=json.loads((root/'analysis/pre-expert-primary-collation.json').read_text())
 primary_cases={c['case_id']:c for c in primary['cases']}
 for column in ['sigla_status','gorila_status','rp1980_status','rp1994_status','rila_s1_status','reference_gap']:
  if dict(sorted(collections.Counter(r[column] for r in rows).items()))!=report[column+'_counts']:raise ValueError('status accounting drift')
 for i,r in enumerate(rows):
  if r['source_pointer']!=f'/documents/{i}' or r['physical_object_identity_certified']!='false':raise ValueError('source identity or object promotion')
  if r['rp1980_status']!='UNRESOLVED_EDITION_CONTENT_NOT_ACQUIRED' or r['rp1994_status']!='UNRESOLVED_EDITION_CONTENT_NOT_ACQUIRED':raise ValueError('Raison–Pope match promotion')
  cases=[primary_cases[c] for c in r['inspected_case_ids'].split('|') if c]
  if any(key(c['document_id'])!=key(r['source_record_id']) for c in cases):raise ValueError('primary case identity misjoin')
  if bool(cases)!=(r['gorila_status']=='PRIMARY_CASE_PAGES_INSPECTED'):raise ValueError('primary inspection status promotion')
  expected=[]
  for c in cases:
   for e in c['evidence']:
    if e.get('edition')=='Godart & Olivier, GORILA':
     entry={k:e[k] for k in ['volume','printed_page','viewer_page','url','locally_inspected_page_sha256']}
     if entry not in expected:expected.append(entry)
  if json.loads(r['inspected_locators_json'])!=expected:raise ValueError('inspected locator evidence drift')
  if r['gorila_source_url']:
   loc=gorila_locator(r['gorila_source_url'])
   if loc is None or loc[:2]!=(r['gorila_volume'],r['gorila_viewer_page']):raise ValueError('GORILA locator drift')
 if report['source_sha256']!=PIN or report['certified_physical_object_count'] is not None or report['canonical_readings_added'] or report['prospective_outcomes_inspected']:raise ValueError('unsupported claims')
 return len(rows)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('source',type=Path,nargs='?');p.add_argument('--check',action='store_true');a=p.parse_args()
 if a.source:
  outputs=build(a.source.read_bytes())
  for path,b in zip([CSV,REPORT],outputs):
   if a.check:
    if (ROOT/path).read_bytes()!=b:raise SystemExit('Stale edition concordance: '+path)
   else:(ROOT/path).write_bytes(b)
 elif not a.check:p.error('Supply authenticated source or use --check for offline integrity')
 print('Edition concordance integrity PASS:',validate_committed(),'source entries; independent reading approval remains open')
