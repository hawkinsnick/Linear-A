#!/usr/bin/env python3
"""Acquire publicly linked GORILA JPEGs with bounded load; never infer readings."""
import argparse,concurrent.futures,csv,hashlib,html,io,json,re,threading,time,urllib.request
from pathlib import Path
from urllib.parse import urlsplit,urljoin
from build_edition_concordance import ROOT,validate_committed

def digest(data):return hashlib.sha256(data).hexdigest()
def groups(root=ROOT):
 validate_committed(root);result={}
 for row in csv.DictReader(io.StringIO((Path(root)/'research/edition-concordance.csv').read_text())):
  if row['gorila_source_url']:result.setdefault(row['gorila_source_url'],[]).append(row)
 return result

def atomic(path,value):
 temporary=path.with_suffix('.tmp');temporary.write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n');temporary.replace(path)

def cached(row,items,directory):
 if row.get('status')!='ACQUIRED_LINKED_EDITION_IMAGE_NOT_TEXT_VERIFICATION' or row.get('source_record_ids')!=[r['source_record_id'] for r in items] or row.get('page_url')!=items[0]['gorila_source_url']:return False
 for suffix,key,size in [('html','html_sha256','html_bytes'),('jpg','image_sha256','image_bytes')]:
  p=directory/(row['route_id']+'.'+suffix)
  if not p.is_file():return False
  b=p.read_bytes()
  if digest(b)!=row[key] or len(b)!=row[size]:return False
 return True

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--asset-dir',type=Path,default=ROOT/'data/private/gorila-route-assets');parser.add_argument('--output',type=Path,default=ROOT/'research/gorila-route-acquisition.json');parser.add_argument('--workers',type=int,default=4);parser.add_argument('--request-interval',type=float,default=1.0);args=parser.parse_args()
 if not 1<=args.workers<=4 or args.request_interval<1:parser.error('Use 1–4 workers and at most one request start per second.')
 from PIL import Image
 directory=args.asset_dir.resolve();directory.mkdir(parents=True,exist_ok=True);progress=directory/'acquisition-progress.json';prior={r['page_url']:r for r in json.loads(progress.read_text())} if progress.exists() else {}
 targets=groups();lock=threading.Lock();last=[0.0]
 def request(url):
  with lock:
   delay=max(0,args.request_interval-(time.monotonic()-last[0]))
   if delay:time.sleep(delay)
   last[0]=time.monotonic()
  with urllib.request.urlopen(url,timeout=25) as response:return response.read(),response.headers.get('content-type','')
 def acquire(pair):
  url,items=pair
  if url in prior and cached(prior[url],items,directory):return prior[url]
  first=items[0];name='v'+first['gorila_volume']+'-viewer-'+first['gorila_viewer_page'];row={'route_id':name,'edition':'Godart & Olivier, GORILA','volume':int(first['gorila_volume']),'viewer_page':int(first['gorila_viewer_page']),'page_url':url,'source_record_ids':[r['source_record_id'] for r in items],'primary_reading_inspected':False,'printed_page_verified':None,'physical_object_identity_certified':False,'consulted':time.strftime('%Y-%m-%d',time.gmtime()),'source_images_redistributed':False}
  try:
   b,ct=request(url);paths=[html.unescape(x) for x in re.findall(r'<img[^>]+src="([^"]+)',b.decode('latin1')) if '/apps/library/services/images/' in x]
   if not paths:raise ValueError('NO_LINKED_EDITION_IMAGE')
   imageurl=urljoin('https://cefael.efa.gr',paths[0]);parsed=urlsplit(imageurl)
   if parsed.scheme!='https' or parsed.netloc!='cefael.efa.gr' or not parsed.path.startswith('/apps/library/services/images/'):raise ValueError('UNEXPECTED_IMAGE_HOST_OR_PATH')
   data,ict=request(imageurl)
   if not data.startswith(b'\xff\xd8'):raise ValueError('LINKED_RESPONSE_NOT_JPEG')
   with Image.open(io.BytesIO(data)) as image:
    if image.format!='JPEG':raise ValueError('WRONG_IMAGE_FORMAT')
    size=image.size;image.verify()
   (directory/(name+'.html')).write_bytes(b);(directory/(name+'.jpg')).write_bytes(data)
   row.update(status='ACQUIRED_LINKED_EDITION_IMAGE_NOT_TEXT_VERIFICATION',image_url=imageurl,html_sha256=digest(b),image_sha256=digest(data),html_bytes=len(b),image_bytes=len(data),image_pixels=list(size),html_content_type=ct,image_content_type=ict)
  except Exception as error:row.update(status='SOURCE_ROUTE_BLOCKED',barrier=type(error).__name__+': '+str(error))
  return row
 rows=[]
 with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
  for row in executor.map(acquire,targets.items()):
   rows.append(row);atomic(progress,rows)
   if len(rows)%20==0 or row['status']=='SOURCE_ROUTE_BLOCKED':print(json.dumps({'finished':len(rows),'total':len(targets),'acquired':sum(r['status'].startswith('ACQUIRED') for r in rows),'last_route':row['route_id'],'last_status':row['status']}),flush=True)
 payload={'format':'linear-a-gorila-route-acquisition-v1','concordance_sha256':digest((ROOT/'research/edition-concordance.csv').read_bytes()),'scope':'755 attributed source-entry page references, grouped into 367 distinct route URLs. Linked JPEG availability only; no automatic printed-page, target-entry, reading or object certification.','record_metadata_license':'CC BY-NC-SA 4.0 on SigLA-derived IDs and routes; source images not redistributed.','source_attribution':'Ester Salgarella and Simon Castellan, SigLA, via Ryan Pavlicek/pyaegean; edition images hosted by EFA/CEFAEL, Godart and Olivier, GORILA.','acquisition_policy':{'max_workers':args.workers,'minimum_request_start_interval_seconds':args.request_interval,'image_copies_committed':False,'readings_added':0},'routes':rows}
 args.output.parent.mkdir(parents=True,exist_ok=True);atomic(args.output,payload);print('COMPLETE '+str(len(rows)),flush=True)
if __name__=='__main__':main()
