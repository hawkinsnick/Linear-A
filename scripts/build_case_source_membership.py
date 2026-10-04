"""Classify reviewed case IDs against the complete pinned source-ID universe.

This is source membership accounting, not an edition/object identity assertion.
"""
import argparse,csv,hashlib,io,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def key(s):return re.sub(r'\s+','',s)
def build(root=ROOT):
 table=(root/'research/edition-concordance.csv').read_bytes();rows=list(csv.DictReader(io.StringIO(table.decode())))
 audit=json.loads((root/'analysis/edition-concordance-audit.json').read_text())
 assert hashlib.sha256(table).hexdigest()==audit['concordance_sha256'] and len(rows)==802
 by={key(r['source_record_id']):r for r in rows};assert len(by)==802
 cases=json.loads((root/'research/critical-pilot.json').read_text())['cases'];out=[]
 for c in cases:
  raw=c['legacy_document_id'];k=key(raw);exact=by.get(k);components=[]
  if c['legacy_kind']=='metrology':status='INTERPRETATION_NOT_DOCUMENT'
  elif exact:status='EXACT_SOURCE_ID'
  elif re.fullmatch(r'HTZd\d+\+\d+',k):
   numbers=k.removeprefix('HTZd').split('+');components=[by.get('HTZd'+n) for n in numbers]
   assert all(components);status='COMPOSITE_CASE_SEPARATE_SOURCE_RECORDS_NO_COMBINED_ID'
  else:status='NO_EXACT_ID_IN_PINNED_SNAPSHOT'
  targets=[exact] if exact else components
  out.append({'case_id':c['case_id'],'legacy_document_id':raw,'membership_status':status,'source_record_ids':[r['source_record_id'] for r in targets],'source_pointers':[r['source_pointer'] for r in targets],'physical_join_certified':False,'reading_adjudicated':False,'absence_scope':'Pinned derivative only; no claim of absence from editions or surviving corpus'})
 report={'format':'linear-a-case-source-membership-v1','source_sha256':audit['source_sha256'],'concordance_sha256':audit['concordance_sha256'],'scope':'15 legacy review cases against 802 pinned source IDs; no new primary-page inspection','cases':out,'source_derived_license':'CC BY-NC-SA 4.0','attribution':'Ester Salgarella and Simon Castellan, SigLA, via Ryan Pavlicek/pyaegean','boundary':'Composite component membership does not certify a join or permit concatenated readings. Missing source IDs are not missing inscriptions. Preserve legacy IDs and prior unresolved review decisions.'}
 return json.dumps(report,ensure_ascii=False,indent=2)+'\n'
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args();s=build();dest=ROOT/'analysis/case-source-membership.json'
 if a.check:assert dest.read_text()==s
 else:dest.write_text(s)
 print('Case/source membership replay verified; no join or reading adjudication')
