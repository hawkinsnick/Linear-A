#!/usr/bin/env python3
"""Replay a bounded critical dossier, preserving every source and review boundary."""
import argparse, collections, csv, hashlib, io, json, re
from pathlib import Path
from build_edition_concordance import PIN, gorila_locator, key
ROOT=Path(__file__).resolve().parents[1]
INPUT='research/critical-pilot.json'
OUTPUTS=['analysis/critical-pilot-audit.json','research/critical-disagreement-comparison.csv','reviews/critical-pilot-review.tsv','docs/CRITICAL-PILOT.md','research/critical-pilot-sigla-witness.json','research/critical-pilot-sigla-slots.csv']
def digest(b): return hashlib.sha256(b).hexdigest()
def dump(x): return json.dumps(x,ensure_ascii=False,indent=2)+'\n'
def compact(x): return json.dumps(x,ensure_ascii=False,separators=(',',':'))
def require(ok,message):
 if not ok: raise ValueError(message)
def table(rows,fields,delimiter=','):
 out=io.StringIO(newline='');writer=csv.DictWriter(out,fieldnames=fields,delimiter=delimiter,lineterminator='\n');writer.writeheader();writer.writerows(rows);return out.getvalue()
def verify_acquired_assets(p,directory):
 directory=Path(directory).resolve();assets=[]
 for q in p['pages']:assets.append((q['name']+'.jpg',q['image_sha256'],q['bytes']))
 for s in p['scholarly_sources']:
  for q in s['reprint_evidence']:assets.append((q['acquired_filename'],q['sha256'],q['bytes']))
 for filename,expected,size in assets:
  path=(directory/filename).resolve()
  require(path.is_relative_to(directory) and path.is_file(),'missing or unsafe acquired asset: '+filename)
  data=path.read_bytes();require(digest(data)==expected and len(data)==size,'acquired asset digest/length drift: '+filename)
 return len(assets)
def validate(p,root=ROOT,raw=None):
 root=Path(root)
 require(p['source_sha256']==PIN and p['source_derived_metadata_license']=='CC BY-NC-SA 4.0','source pin or rights drift')
 require(p['raison_pope_status']=='UNRESOLVED_EDITION_CONTENT_NOT_ACQUIRED','unsupported Raison–Pope promotion')
 require(p['expert_validation_added'] is False and p['physical_readings_adjudicated']==p['independently_verified_object_count']==p['canonical_readings_added']==0 and p['prospective_outcomes_inspected'] is False,'unsupported scientific promotion')
 concordance=list(csv.DictReader(io.StringIO((root/'research/edition-concordance.csv').read_text()))); by={r['source_record_id']:r for r in concordance}
 ids=p['declared_source_ids'];entries=p['entries']
 require(len(ids)==10 and len(set(ids))==10 and [e['source_record_id'] for e in entries]==ids,'declared pilot identity or coverage drift')
 pages={q['page_id']:q for q in p['pages']};require(len(pages)==len(p['pages']),'duplicate page identity')
 for q in pages.values():
  loc=gorila_locator(q['url']);require(loc is not None and loc[:2]==(str(q['volume']),str(q['viewer_page'])),'page route mismatch')
  require(q['inspection']=='AI_VISUAL_PAGE_INSPECTION_NOT_EXPERT_AUTOPSY' and q['image_redistributed'] is False and q['lineage']=='GORILA_EDITION','page authority/rights promotion')
  require(all(re.fullmatch('[0-9a-f]{64}',q[h]) for h in ['image_sha256','html_sha256']),'invalid acquisition digest')
  if q['finding']=='NO_TARGET_ENTRY_BLANK_PAGE': require(not q['document_ids'] and q['printed_page'] is None,'blank page promoted to inscription')
  else: require(q['finding']=='IDENTIFIED_ENTRY_PRESENT' and q['document_ids'] and set(q['document_ids'])<=set(ids) and isinstance(q['printed_page'],int) and q['printed_page']>0,'invalid inspected entry binding')
 scholars={s['source_id']:s for s in p['scholarly_sources']}
 for s in scholars.values():
  require(s['consultation']=='PUBLIC_SCHOLARLY_REPRINT_HTML_AND_FIGURE15' and s['figure_pixels_inspected'] is True and s['reprint_html_acquired'] is True and s['original_pdf_acquired'] is False and s['file_acquired'] is False and s['text_redistributed'] is False,'reprint source promoted to original PDF inspection')
  evidence=s['reprint_evidence'];require(len({v['evidence_id'] for v in evidence})==len(evidence),'duplicate reprint evidence')
  require(any(v['evidence_id']=='FLOUDA-FIGURE15' and v['target_entry_present'] is True for v in evidence),'missing inspected cup figure')
  for v in evidence:require(re.fullmatch('[0-9a-f]{64}',v['sha256']) and v['redistributed'] is False and v['bytes']>0 and v['url'].startswith('https://socialsci.libretexts.org/'),'unqualified reprint acquisition')
 assertion_ids=[]
 allowed={'inventory_label','dimension_caption','damage_caption','damage_presentation','surface_presentation','vessel_caption','numbered_rows','editorial_quantities','vacat_rows','layout_presentation','rim_diameter_cm','find_context','reading_layout','punctuation'}
 for e in entries:
  id=e['source_record_id'];require(id in by and e['source_pointer']==by[id]['source_pointer'],'source record/pointer mismatch')
  require(e['object_identity_certified'] is False and e['expert_validated'] is False and e['reading_adjudicated'] is False and e['join_status']=='UNASSESSED' and e['restoration_status']=='NO_NEW_RESTORATION_ENTERED','unsupported object, reading or restoration promotion')
  require(set(e['source_context'])=={'site','typology','period','dimensions_cm'},'source context schema drift')
  attestations=e['source_attestations']
  require(len(attestations)==e['source_attestation_count'],'selected witness slot coverage drift')
  for a in attestations:
   require(set(a)=={'sign','kind','word','series','number','raw_flags'} and isinstance(a['sign'],str) and isinstance(a['series'],str) and isinstance(a['raw_flags'],list) and all(isinstance(v,int) for v in a['raw_flags']),'source witness field loss or invented quantity')
  diag=e['source_encoding_diagnostics']
  require(diag['account_quantity_field']==diag['line_and_glyph_coordinates']=='NOT_SUPPLIED' and diag['raw_flags']=='PRESERVED_UPSTREAM_UNDECODED_NOT_INTERPRETED_AS_DAMAGE_OR_LINE_NUMBERS','source absence or raw flag promotion')
  require(all(isinstance(diag[k],int) and 0<=diag[k]<=e['source_attestation_count'] for k in ['editorial_groups','blank_slots','fraction_slots']),'invalid source encoding diagnostics')
  expected=[q['page_id'] for q in p['pages'] if id in q['document_ids']];require(e['gorila_page_ids']==expected and expected,'entry page coverage mismatch')
  for a in e['assertions']:
   assertion_ids.append(a['assertion_id']);require(a['field'] in allowed and a['locator_detail'] and a['limitation'],'unqualified assertion')
   if a['source_id'] in pages:
    q=pages[a['source_id']];require(id in q['document_ids'] and a['level']=='PRIMARY_EDITION_REPORTED','assertion/page misjoin')
   else:
    require(a['source_id'] in scholars and a['level']=='ATTRIBUTED_SCHOLARLY_REPORT_PUBLIC_REPRINT','unbound scholarly assertion')
    evidence={v['evidence_id']:v for v in scholars[a['source_id']]['reprint_evidence']}
    require(a.get('supplementary_evidence_ids') and all(i in evidence and evidence[i]['target_entry_present'] is True for i in a['supplementary_evidence_ids']),'wrong figure or unbound scholarly assertion')
   if a['field']=='editorial_quantities':
    require(a['level']=='PRIMARY_EDITION_REPORTED' and all(set(x)=={'edition_group','quantity'} and isinstance(x['quantity'],int) and x['quantity']>=0 and x['edition_group'] for x in a['value']),'quantity must remain printed edition assertion')
 require(len(assertion_ids)==len(set(assertion_ids)),'duplicate assertion identity')
 legacy_bytes=(root/'data/unresolved_cases.csv').read_bytes();require(digest(legacy_bytes)==p['legacy_queue_sha256'],'legacy alternatives input drift')
 legacy=list(csv.DictReader(io.StringIO(legacy_bytes.decode())));require(len(p['cases'])==len(legacy)==15,'case coverage drift')
 for c,old in zip(p['cases'],legacy):
  require((c['case_id'],c['legacy_document_id'],c['legacy_kind'],c['legacy_alternatives'])==(old['case_id'],old['document_id'],old['kind'],old['dispute']),'legacy comparison changed')
  matches=[id for id in ids if key(id)==key(old['document_id'])];expected=matches[0] if matches else None
  require(c['source_record_id']==expected,'case identity misjoin; suffixes and fragments preserved')
  status='EXACT_PILOT_SOURCE_ID' if expected else ('INTERPRETATION_ONLY_NOT_A_DOCUMENT' if c['case_id']=='U015' else 'NO_EXACT_PILOT_SOURCE_ID')
  require(c['source_join_status']==status and c['quantity_field_status']=='NOT_SUPPLIED_BY_AUTHENTICATED_SIGLA_EXPORT','quantity/source identity promotion')
  require(c['review_decision']=='UNREVIEWED' and c['expert_validated'] is False,'blank review promoted')
  for x in c['authenticated_source_excerpts']:
   prefix=by[expected]['source_pointer']+'/attestations/' if expected else 'NO_MATCH/'
   require(x['source_pointer'].startswith(prefix) and x['source_pointer'][len(prefix):].isdigit(),'attestation pointer misjoin')
   require(set(x['fields'])=={'sign','kind','series','number','word'},'sign-series field misrepresented as quantity')
   selected=next(e for e in entries if e['source_record_id']==expected)['source_attestations']
   index=int(x['source_pointer'].split('/')[-1]);require(index<len(selected) and x['fields']=={k:selected[index][k] for k in x['fields']},'comparison excerpt differs from full selected witness')
 if raw is not None:
  require(digest(raw)==PIN,'source checksum mismatch'); source=json.loads(raw)
  for e in entries:
   i=int(e['source_pointer'].split('/')[-1]);d=source['documents'][i]
   require(d['id']==e['source_record_id'] and e['source_context']=={k:d[k] for k in e['source_context']} and e['source_attestation_count']==len(d['attestations']),'authenticated context replay drift')
   require(e['source_attestations']==d['attestations'],'full selected witness differs from authenticated source')
   a=d['attestations'];diag=e['source_encoding_diagnostics']
   require(diag['editorial_groups']==len({z['word'] for z in a if z['word'] is not None}) and diag['blank_slots']==sum(z['kind']=='blank' for z in a) and diag['fraction_slots']==sum(z['kind']=='fraction' for z in a),'source encoding diagnostic replay drift')
  for c in p['cases']:
   for x in c['authenticated_source_excerpts']:
    _,_,i,_,j=x['source_pointer'].split('/'); a=source['documents'][int(i)]['attestations'][int(j)]
    require(x['fields']=={k:a[k] for k in x['fields']},'authenticated excerpt replay drift')
 return p

def calculate(root=ROOT,raw=None):
 root=Path(root);p=validate(json.loads((root/INPUT).read_text()),root,raw);pages={q['page_id']:q for q in p['pages']};entries={e['source_record_id']:e for e in p['entries']}
 witness_entries=[];slots=[]
 for e in entries.values():
  witnesses=[]
  for i,a in enumerate(e['source_attestations']):
   pointer=e['source_pointer']+'/attestations/'+str(i);identifier='SIGLA-V4:'+pointer
   witnesses.append({'attestation_id':identifier,'source_pointer':pointer,'source_fields':a})
   slots.append({'attestation_id':identifier,'source_record_id':e['source_record_id'],'source_pointer':pointer,'source_slot_index':i,'source_sign_label':a['sign'],'source_kind':a['kind'],'source_series':a['series'],'source_sign_number_json':compact(a['number']),'source_editorial_group_json':compact(a['word']),'source_raw_flags_json':compact(a['raw_flags']),'source_line_alignment':'UNKNOWN','physical_glyph_coordinates':'UNKNOWN','raw_flags_interpretation':'UNDECODED','physical_reading_adjudicated':'false','record_license':p['source_derived_metadata_license'],'source_attribution':p['source_attribution'],'source_snapshot_sha256':PIN,'source_release_url':p['source_url']})
  witness_entries.append({'source_record_id':e['source_record_id'],'source_pointer':e['source_pointer'],'source_context':e['source_context'],'record_license':p['source_derived_metadata_license'],'attestations':witnesses,'edition_line_alignment':None,'physical_glyph_coordinates':None,'raw_flags_interpretation':'UNDECODED','expert_validated':False,'object_identity_certified':False})
 witness=dump({'format':'linear-a-selected-sigla-witness-v1','source_sha256':PIN,'source_attribution':p['source_attribution'],'source_url':p['source_url'],'record_license':p['source_derived_metadata_license'],'source_entries':len(witness_entries),'source_attestation_slots':len(slots),'entries':witness_entries,'boundary':'Complete source encodings for the ten selected entries only. Source labels, editorial groups, blank slots, fractions, raw flags and competing encodings are preserved. Sign-series numbers are not quantities. No verified phonetic value, linguistic word, primary-edition equivalence, physical reading or source independence is inferred.'})
 slot_table=table(slots,list(slots[0]))
 def cite(a):
  if a['source_id'] in pages:
   q=pages[a['source_id']];return f"GORILA {q['volume']}, printed p. {q['printed_page']}, viewer {q['viewer_page']}: {a['locator_detail']} ({q['url']})"
  return f"Flouda 2013, DOI 10.5334/bai.h: {a['locator_detail']}; public reprint evidence " + "; ".join(v["url"] for v in p["scholarly_sources"][0]["reprint_evidence"] if v["evidence_id"] in a["supplementary_evidence_ids"])
 comparisons=[];review=[]
 for c in p['cases']:
  e=entries.get(c['source_record_id']);quantities=[a for a in e['assertions'] if a['field']=='editorial_quantities'] if e and c['case_id']=='U001' else []
  excerpts=c['authenticated_source_excerpts']
  commentary='Legacy strings have no individually verified witness locator; source excerpts are exact encodings, not a palaeographic verdict.'
  if c['case_id']=='U001':commentary='GORILA prints 38, 10 and 5 in the HT 17 panel. Legacy quantity 37 remains untraced: this SigLA export supplies no account quantities. Its sign number 37 denotes TI, not a numeral quantity. This does not prove the origin of the legacy error or adjudicate the object.'
  if c['case_id']=='U011':commentary='SigLA supplies four source editorial groups. Flouda p. 162 reports punctuation around the second sign group. Neither establishes the legacy exact split before IZU; source blank and label *79 are preserved without equating them to a restored sign or linguistic boundary.'
  if not e:commentary='No exact pilot source-ID match; no whitespace-only join licenses a renamed, combined or alternate identifier. Earlier inspected pages remain available in the historical primary audit. Fraction K is a scholarly/model question.'
  comparisons.append({'case_id':c['case_id'],'legacy_document_id':c['legacy_document_id'],'source_record_id':c['source_record_id'] or '', 'kind':c['legacy_kind'],'legacy_alternatives':c['legacy_alternatives'],'legacy_status':'PROJECT_QUEUE_STRINGS_WITNESS_LOCATORS_UNTRACED','source_join_status':c['source_join_status'],'authenticated_source_excerpts_json':compact(excerpts),'edition_quantity_assertions_json':compact(quantities),'primary_page_ids':'|'.join(e['gorila_page_ids']) if e else '', 'disposition':c['disposition'],'review_note':commentary,'expert_validated':'false','physical_reading_adjudicated':'false','source_metadata_license':p['source_derived_metadata_license']})
  review.append({'review_id':c['case_id'],'review_type':'disagreement','source_record_id':c['source_record_id'] or '', 'evidence_path':'research/critical-disagreement-comparison.csv','evidence_locator':c['case_id'],'question':'Trace each alternative to an attributed witness and locator; assess graphical ambiguity without silently selecting a canonical reading.','decision':'UNREVIEWED','reviewer':'','review_date':'','decision_evidence':'','independent_review':'false'})
 for e in entries.values():
  review.append({'review_id':'ENTRY-'+key(e['source_record_id']),'review_type':'context_and_layout','source_record_id':e['source_record_id'],'evidence_path':INPUT,'evidence_locator':e['source_pointer'],'question':'Verify caption, layout, missingness and quantities against linked edition pages. Check modern inventory and fragment/face relations separately.','decision':'UNREVIEWED','reviewer':'','review_date':'','decision_evidence':'','independent_review':'false'})
 comparison=table(comparisons,list(comparisons[0]));sheet=table(review,list(review[0]),'\t')
 lines=['# Linear A critical pilot and review handoff','',p['scope'],'',p['selection_reason'],'','## Reproduce','', '```sh','python scripts/build_critical_pilot.py /path/to/sigla-corpus.json --check','python scripts/build_critical_pilot.py --check','python scripts/build_critical_pilot.py --check --verify-assets /path/to/lawfully-acquired-assets','python scripts/test_critical_pilot.py','```','','The first command verifies the pinned source bytes, every selected context field and every excerpt pointer. The second replays committed views without acquiring source files. Page hashes identify the consulted images; automated replay cannot certify their epigraphic content.','', '## Boundaries and review queue','','Ten source entries span five source-reported sites and three source-reported forms. Entries, surfaces, photographs, editorial groups and physical objects are separate units. No full critical transcription, object-level join or independent expert approval is claimed. Unknown context, join and restoration fields remain explicit.','', 'Raison–Pope remains entry-level unresolved. The earlier Step 1 concordance reports its original eight exact inspected source entries; this separate pilot adds ARKH 2 and KN Zb 40 and new field-level assertions. Historical counts are not overwritten.','', 'Use [the blank 25-item review sheet](../reviews/critical-pilot-review.tsv) and [the attributed comparison CSV](../research/critical-disagreement-comparison.csv). Every decision is UNREVIEWED. Record a subsequent decision as a separate attributed assertion with reviewer, date, locator, scope and source dependence; do not overwrite these witness assertions.','', '## Source-bound entry dossiers','']
 for e in entries.values():
  c=e['source_context'];lines.extend([f"### {e['source_record_id']}",'',f"Authenticated SigLA pointer `{e['source_pointer']}`; source-reported site **{c['site']}**, form **{c['typology']}**, period **{c['period']}**; dimensions (source order) `{compact(c['dimensions_cm'])}`; {e['source_attestation_count']} source attestations. These are source encodings, not independently counted physical signs.",'',f"Find context: {e['archaeological_find_context_status']}. Joins: {e['join_status']}. Restorations: {e['restoration_status']}. Modern inventory identity unverified.",'','| Field | Attributed assertion | Exact locator and boundary |','|---|---|---|'])
  for a in e['assertions']:
   val=compact(a['value']) if not isinstance(a['value'],str) else a['value'];lines.append('| '+ ' | '.join(x.replace('|','\\|').replace('\n',' ') for x in [a['field'],val,cite(a)+'; '+a['level']+'; '+a['limitation']])+' |')
  lines.extend(['', 'Source encoding diagnostics: `'+compact(e['source_encoding_diagnostics'])+'`. Source word indices are editorial group IDs, not established linguistic words; blank slots and raw flags are not an expert damage assessment.', ''])
 lines.extend(['## Fifteen unresolved comparisons','','Legacy alternatives are preserved project queue strings. They do not become verified Raison–Pope, GORILA or SigLA witness readings merely by appearing here. Exact authenticated excerpts and inspected edition facts are separate columns in the CSV.','','| Case | Project alternatives | Current source-bound assessment |','|---|---|---|'])
 for c in comparisons:lines.append('| '+ ' | '.join(x.replace('|','\\|') for x in [c['case_id']+' / '+c['legacy_document_id'],c['legacy_alternatives'],c['review_note']])+' |')
 lines.extend(['','## Acquisition barriers and negative evidence','','GORILA IV viewer page 126 is blank, has no printed page number and is not a continuation of KN Zb 40. It has no entry binding or field assertions. Multiple representations of an inscription in GORILA share the same edition lineage.','','Flouda 2013, pp. 160 and 162: initially consulted indexed publication text was supplemented by direct public LibreTexts reprint HTML and Figure 15 inspection. Panel a is KN Zc 6; panel b is KN Zc 7 and excluded. The separately inspected Figure 16a ring image is excluded from cup assertions. Publisher, institutional PDF and OAPEN direct routes returned HTTP 403; the web PDF parser also rejected its 15,064,351-byte size. The original PDF remains unacquired; no access control was bypassed. Flouda cites GORILA and is not presumed an independent object witness. Exact reprint URLs and acquired-byte hashes are in the source record.','','## Remaining scholarly work','']+[str(i)+'. '+q for i,q in enumerate(p['next_review_requirements'],1)]+['','## Rights and attribution','',p['source_attribution']+'. '+p['rights'],''])
 lines.extend(['## Downloadable source witness','','[Selected SigLA witness JSON](../research/critical-pilot-sigla-witness.json) and [the 168-slot source CSV](../research/critical-pilot-sigla-slots.csv) retain every attestation field for the ten selected source entries, including empty labels, raw flags, fractions and source editorial groups. Stable attestation IDs are snapshot-qualified exact JSON pointers. Edition line alignment and physical glyph coordinates remain unknown. This is a complete selected-source encoding export, not a full multi-edition critical transcription or an expert reading.','','Both exports retain SigLA CC BY-NC-SA 4.0 and attribution to Ester Salgarella and Simon Castellan via Ryan Pavlicek/pyaegean. The remainder of the 802-entry source snapshot is not bundled by this pilot.',''])
 guide='\n'.join(lines)
 assertions=[a for e in entries.values() for a in e['assertions']];q=[a for a in assertions if a['field']=='editorial_quantities']
 report={'format':'linear-a-critical-pilot-audit-v1','scope':p['scope'],'source_sha256':PIN,'input_hashes':{x:digest((root/x).read_bytes()) for x in [INPUT,'data/unresolved_cases.csv','research/edition-concordance.csv']},'pilot_source_entries':len(entries),'source_reported_sites':dict(collections.Counter(e['source_context']['site'] for e in entries.values())),'source_reported_forms':dict(collections.Counter(e['source_context']['typology'] for e in entries.values())),'inspected_page_images':len(pages),'identified_target_page_images':sum(bool(q['document_ids']) for q in pages.values()),'blank_adjacent_page_negative_checks':sum(q['finding']=='NO_TARGET_ENTRY_BLANK_PAGE' for q in pages.values()),'supplementary_reprint_acquisitions':4,'supplementary_target_figures_inspected':1,'supplementary_non_target_figure_negative_checks':1,'field_assertions':len(assertions),'assertion_levels':dict(collections.Counter(a['level'] for a in assertions)),'entries_with_primary_edition_quantities':len(q),'printed_edition_quantity_assertions':sum(len(a['value']) for a in q),'comparison_cases':len(comparisons),'case_source_join_status':dict(collections.Counter(c['source_join_status'] for c in comparisons)),'unreviewed_review_items':len(review),'expert_reviews':0,'canonical_readings_added':0,'certified_physical_objects':None,'independent_object_confirmation':False,'raison_pope_status':p['raison_pope_status'],'prospective_outcomes_inspected':False,'generated_hashes':{OUTPUTS[1]:digest(comparison.encode()),OUTPUTS[2]:digest(sheet.encode()),OUTPUTS[3]:digest(guide.encode())},'boundary':'A bounded, source-traced metadata and disagreement pilot. Reproducibility verifies identity/encoding/view integrity, not physical epigraphy, source independence, full critical transcription or scholarly parity.'}
 report.update(public_source_witness_entries=len(witness_entries),public_source_witness_slots=len(slots),source_slot_kinds=dict(collections.Counter(s['source_kind'] for s in slots)),source_editorial_groups=sum(e['source_encoding_diagnostics']['editorial_groups'] for e in entries.values()))
 report['generated_hashes'].update({OUTPUTS[4]:digest(witness.encode()),OUTPUTS[5]:digest(slot_table.encode())})
 return dict(zip(OUTPUTS,[dump(report),comparison,sheet,guide,witness,slot_table]))
def main():
 parser=argparse.ArgumentParser();parser.add_argument('source',nargs='?');parser.add_argument('--check',action='store_true');parser.add_argument('--verify-assets',type=Path);args=parser.parse_args();raw=Path(args.source).read_bytes() if args.source else None
 out=calculate(raw=raw)
 if args.verify_assets: print('Verified '+str(verify_acquired_assets(json.loads((ROOT/INPUT).read_text()),args.verify_assets))+' acquired asset digests; hashes do not certify epigraphic interpretation')
 for path,value in out.items():
  p=ROOT/path
  if args.check:require(p.is_file() and p.read_bytes()==value.encode(), 'generated pilot view drift: '+path)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(value,encoding='utf-8')
 print('Critical pilot views '+('replayed' if args.check else 'written')+(' with authenticated source verification' if raw is not None else '; epigraphic content not automatically verified'))
if __name__=='__main__':main()
