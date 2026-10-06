#!/usr/bin/env python3
"""Descriptive queries over source-defined word groups; no linguistic promotion."""
import argparse,collections,json,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
from research_api import rows
def groups():
 return list(rows("source_words"))
def stats():
 g=groups();lengths=collections.Counter(len(r["occurrence_indices"]) for r in g);docs=collections.Counter(r["document_id"] for r in g)
 return {"groups":len(g),"group_length_frequency":dict(sorted(lengths.items())),"documents_with_groups":len(docs),"boundary":"SigLA source-defined groups are editorial units, not established linguistic words."}
def find(pattern):
 import re
 rx=re.compile(pattern,re.I);return [r for r in groups() if rx.search(r["word_id"]) or rx.search(r["document_id"])]
if __name__=="__main__":
 p=argparse.ArgumentParser();p.add_argument("--stats",action="store_true");p.add_argument("--pattern");a=p.parse_args();out=stats() if a.stats or not a.pattern else {"records":find(a.pattern),"boundary":"Pattern matches identifiers/source groups; no morphological interpretation."};print(json.dumps(out,ensure_ascii=False,indent=2))
