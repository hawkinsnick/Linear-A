#!/usr/bin/env python3
"""Symbolic/model-specific accounting checks. Never assigns unstated sign values."""
import argparse,json,pathlib
from fractions import Fraction
def val(x,model):
 if isinstance(x,(int,float)): return Fraction(str(x))
 if isinstance(x,str) and x in model: return Fraction(str(model[x]))
 return None
def check(record,model):
 items=[];total=Fraction(0);indeterminate=[]
 for item in record.get("items",[]):
  v=val(item.get("quantity"),model)
  if v is None: indeterminate.append(item.get("quantity"));continue
  total+=v;items.append({"quantity":item.get("quantity"),"value":str(v)})
 stated=val(record.get("stated_total"),model)
 return {"model_id":model.get("_id","anonymous"),"computed_total":str(total) if not indeterminate else None,"stated_total":str(stated) if stated is not None else None,"balanced":(total==stated) if stated is not None and not indeterminate else None,"indeterminate_symbols":indeterminate,"boundary":"Arithmetic consistency does not validate the metrological model or decipherment."}
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("record",type=pathlib.Path);p.add_argument("model",type=pathlib.Path);a=p.parse_args();print(json.dumps(check(json.loads(a.record.read_text()),json.loads(a.model.read_text())),indent=2))
