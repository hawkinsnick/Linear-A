#!/usr/bin/env python3
"""Replay a licensed, pinned SigLA derivative into public source-only JSONL."""
import argparse,csv,hashlib,json
from pathlib import Path
from urllib.parse import urlsplit,parse_qsl,urlencode,urlunsplit
from build_pre_expert_audit import ROOT,PINS,build
PIN=PINS['Linear-A']
ATTR='Ester Salgarella and Simon Castellan, SigLA; derivative by Ryan Pavlicek/pyaegean'
FILES=['research/sigla-source-documents.jsonl','research/sigla-source-groups.jsonl','research/sigla-source-signs.jsonl']
AUDIT='analysis/public-sigla-layer-audit.json'
def digest(b):return hashlib.sha256(b).hexdigest()
def clean(url):
 if not isinstance(url,str) or not url or url=='missing':return None
 p=urlsplit(url)
 return urlunsplit((p.scheme,p.netloc,p.path,urlencode([(k,v) for k,v in parse_qsl(p.query,keep_blank_values=True) if k!='ce']),p.fragment))
def outputs(raw):
 assert digest(raw)==PIN,'Unverified source bytes'
 data=json.loads(raw);audit,local=build(data,'Linear-A',PIN)
 docs=[]
 for i,d in enumerate(data['documents']):
  fields={k:v for k,v in d.items() if k!='reference_url'}
  docs.append({'source_record_id':d['id'],'source_fields':fields,'public_reference_url':clean(d.get('reference_url')),'reference_url_status':'ABSENT' if not d.get('reference_url') else 'LITERAL_MISSING' if d['reference_url']=='missing' else 'SESSION_PARAMETER_REMOVED_PUBLIC_ROUTE','reference_url_pointer':f'/documents/{i}/reference_url','provenance':{'input_sha256':PIN,'json_pointer':f'/documents/{i}','license':'CC BY-NC-SA 4.0','attribution':ATTR},'classification':'SOURCE_REPORTED_NOT_INDEPENDENTLY_VERIFIED','physical_object_identity_certified':False})
 groups=local['source-words.json'];signs=local['sign-concordance.json']
 for row in groups+signs:row['provenance']['attribution']=ATTR
 result={p:''.join(json.dumps(r,ensure_ascii=False,separators=(',',':'))+'\n' for r in rows).encode() for p,rows in zip(FILES,[docs,groups,signs])}
 report={'format':'linear-a-public-sigla-layer-v1','input_sha256':PIN,'upstream_release':'https://github.com/ryanpavlicek/pyaegean/releases/download/sigla-corpus-v4/sigla-corpus.json','source_metadata':{k:data['_meta'].get(k) for k in ['license','attribution','cite','version','generated','source_sha256','note']},'counts':{k:audit[k] for k in ['documents','occurrences','source_word_groups','source_sign_entries','occurrences_without_sign_key','occurrences_with_sign_key_absent_from_sign_table']},'source_independence':audit['source_independence'],'scope':'All entries in one authenticated derivative; not a census of physical objects or independent edition reconciliation.','images_redistributed':False,'numeral_quantities':'NOT_PROVIDED_BY_SOURCE','raw_flags':'PRESERVED_UNDECODED','reference_url_policy':'Only volatile ce query parameters removed; original input hash and per-field pointer retained. Absent and literal missing remain distinct.','files':[{'path':p,'sha256':digest(b),'bytes':len(b),'records':len(b.splitlines())} for p,b in result.items()]}
 result[AUDIT]=(json.dumps(report,ensure_ascii=False,indent=2)+'\n').encode();return result

def validate_committed(root=ROOT):
 report=json.loads((root/AUDIT).read_text());assert report['input_sha256']==PIN
 ids=[];slots=0
 for entry in report['files']:
  b=(root/entry['path']).read_bytes();assert digest(b)==entry['sha256'],'public source file drift'
  rows=[json.loads(line) for line in b.splitlines()];assert len(rows)==entry['records']
  for row in rows:
   assert row['provenance']['license']=='CC BY-NC-SA 4.0' and row['provenance']['input_sha256']==PIN
   assert row['provenance']['attribution']==ATTR
  if entry['path']==FILES[0]:
   for i,row in enumerate(rows):
    assert row['provenance']['json_pointer']==f'/documents/{i}'
    assert row['source_record_id']==row['source_fields']['id']
    assert row['physical_object_identity_certified'] is False
    assert 'reference_url' not in row['source_fields']
    assert 'ce' not in dict(parse_qsl(urlsplit(row['public_reference_url'] or '').query))
    ids.append(row['source_record_id']);slots+=len(row['source_fields']['attestations'])
 assert len(ids)==len(set(ids))==802 and slots==5144
 return report

def main():
 p=argparse.ArgumentParser();p.add_argument('source',nargs='?',type=Path);p.add_argument('--check',action='store_true');args=p.parse_args()
 if args.source:
  for path,b in outputs(args.source.read_bytes()).items():
   if args.check:assert (ROOT/path).read_bytes()==b,'Replay drift: '+path
   else:(ROOT/path).write_bytes(b)
 validate_committed();print('Public SigLA layer verified: 802 entries / 5144 slots / 1401 groups / 376 sign entries')
if __name__=='__main__':main()
