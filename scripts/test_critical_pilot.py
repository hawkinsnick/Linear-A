"""Corruption tests for source identity, absent quantities and review authority."""
import copy,csv,io,json,tempfile,unittest
from pathlib import Path
import build_critical_pilot as m
class PilotTests(unittest.TestCase):
 def setUp(self):self.p=json.loads((m.ROOT/m.INPUT).read_text())
 def reject(self,operation,pattern):
  p=copy.deepcopy(self.p);operation(p)
  with self.assertRaisesRegex(ValueError,pattern):m.validate(p)
 def test_damaged_and_symbolic_amounts_have_no_complete_numeric_value(self):
  base={'integer_component':30,'symbolic_component_status':'ABSENT','terminal_status':'NO_MARKED_LOSS'}
  self.assertEqual(m.complete_printed_integer(base),30)
  for state in ['OPEN_BRACKET','UNCERTAIN_BRACKETED_CONTINUATION','EDITION_COMMENTARY_QUESTIONS_COMPLETENESS']:
   self.assertIsNone(m.complete_printed_integer(dict(base,terminal_status=state)))
  self.assertIsNone(m.complete_printed_integer(dict(base,symbolic_component_status='PRESENT_UNTRANSCRIBED')))
 def test_fractional_or_restored_normalization_cannot_be_imported(self):
  self.reject(lambda p:next(a for e in p['entries'] for a in e['assertions'] if a['field']=='editorial_quantity_components')['value'][0].update(normalized_quantity=0.5),'schema drift')
 def test_bracketed_dimensions_and_fragment_expressions_remain_distinct(self):
  parts=m.dimension_components('5,50 × [3,00]+[6,20] × 0,70 cm')
  self.assertIsNone(parts[1]['scalar']);self.assertTrue(parts[1]['fragment_expression']);self.assertEqual(parts[1]['literal'],'[3,00]+[6,20]')
  parts=m.dimension_components('[8,50] × 2,50 × 2,80 cm');self.assertTrue(parts[0]['bracketed'])
  with self.assertRaises(ValueError):m.dimension_components('8,50] × 2,50 × 2,80 cm')
 def test_face_relationship_cannot_become_object_certification(self):
  self.reject(lambda p:next(a for e in p['entries'] for a in e['assertions'] if a['field']=='edition_counting_unit')['value'].update(physical_identity_certified=True),'face relation')
 def test_neighboring_panels_are_excluded_and_source_witness_is_unchanged(self):
  out=m.calculate();rows=list(csv.DictReader(io.StringIO(out[m.OUTPUTS[6]])))
  self.assertFalse(any(r['source_record_id'] in ['KH 75','KH 76','HT 18'] for r in rows))
  self.assertEqual({r['source_record_id'] for r in rows},{'HT 15','HT 17','HT 34','HT 49a','KH 8','ARKH 2'})
  self.assertTrue(all(r['complete_physical_amount_certified']=='false' for r in rows))
  meta=list(csv.DictReader(io.StringIO(out[m.OUTPUTS[7]])));ht=next(r for r in meta if r['source_record_id']=='HT 49a')
  self.assertEqual(ht['dimension_comparison_status'],'SOURCE_SCALAR_VS_EDITION_FRAGMENT_EXPRESSION_UNRESOLVED')
 def test_committed_views_replay(self):
  for path,value in m.calculate().items():self.assertEqual((m.ROOT/path).read_bytes(),value.encode())
 def test_acquired_asset_wrong_bytes_and_path_escape_rejected(self):
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory);(root/'image.jpg').write_bytes(b'fixture')
   p={'pages':[{'name':'image','image_sha256':m.digest(b'fixture'),'bytes':7}],'scholarly_sources':[]}
   self.assertEqual(m.verify_acquired_assets(p,root),1)
   (root/'image.jpg').write_bytes(b'corrupt')
   with self.assertRaisesRegex(ValueError,'digest/length'):m.verify_acquired_assets(p,root)
   p['pages'][0]['name']='../escape'
   with self.assertRaisesRegex(ValueError,'unsafe'):m.verify_acquired_assets(p,root)
 def test_source_bytes_fail_closed(self):
  with self.assertRaisesRegex(ValueError,'checksum'):m.validate(self.p,raw=b'{}')
 def test_fragment_or_suffix_not_fuzzy_joined(self):
  self.reject(lambda p:p['cases'][9].update(source_record_id='HT 49a'),'misjoin')
  self.reject(lambda p:p['entries'][3].update(source_record_id='HT 49b'),'identity')
 def test_blank_page_cannot_become_target(self):
  self.reject(lambda p:next(q for q in p['pages'] if q['finding']=='NO_TARGET_ENTRY_BLANK_PAGE').update(document_ids=['KN Zb 40']),'blank page')
 def test_page_or_assertion_cannot_move_to_another_document(self):
  self.reject(lambda p:p['pages'][0].update(viewer_page=31),'route mismatch')
  self.reject(lambda p:p['entries'][0]['assertions'][0].update(source_id='HT17-photo'),'misjoin')
 def test_no_source_quantity_or_expert_promotion(self):
  self.reject(lambda p:p['cases'][0].update(quantity_field_status='SIGLA_QUANTITY_37'),'quantity')
  self.reject(lambda p:p['entries'][0].update(object_identity_certified=True),'promotion')
  self.reject(lambda p:p['cases'][0].update(review_decision='APPROVED'),'review promoted')
  self.reject(lambda p:p.update(raison_pope_status='MATCHED'),'Raison')
 def test_sign_number_cannot_be_relabelled_quantity(self):
  self.reject(lambda p:p['cases'][2]['authenticated_source_excerpts'][0]['fields'].update(quantity=37),'misrepresented')
 def test_reprint_is_not_original_pdf_or_wrong_object(self):
  self.reject(lambda p:p['scholarly_sources'][0].update(original_pdf_acquired=True),'original PDF')
  self.reject(lambda p:next(a for e in p['entries'] for a in e['assertions'] if a['source_id']=='FLOUDA2013').update(supplementary_evidence_ids=['FLOUDA-FIGURE16A-NEGATIVE']),'wrong figure')
 def test_editorial_groups_and_unknowns_not_linguistic_words(self):
  self.reject(lambda p:p['entries'][0]['assertions'][0].update(field='translated_word'),'unqualified')
  self.reject(lambda p:p['entries'][3].update(join_status='CONFIRMED'),'promotion')
 def test_raw_flags_cannot_be_promoted_to_damage(self):
  self.reject(lambda p:p['entries'][0]['source_encoding_diagnostics'].update(raw_flags='DAMAGE_DECODED'),'raw flag')
 def test_alternatives_and_legacy_input_preserved(self):
  self.reject(lambda p:p['cases'][0].update(legacy_alternatives='38'),'legacy comparison')
  with tempfile.TemporaryDirectory() as directory:
   root=Path(directory)
   for path in ['research/edition-concordance.csv','data/unresolved_cases.csv']:
    target=root/path;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes((m.ROOT/path).read_bytes())
   with (root/'data/unresolved_cases.csv').open('a') as f:f.write('\n')
   with self.assertRaisesRegex(ValueError,'input drift'):m.validate(self.p,root)
 def test_complete_witness_and_comparison_cannot_diverge(self):
  self.reject(lambda p:p['entries'][0]['source_attestations'].pop(),'slot coverage')
  self.reject(lambda p:p['cases'][2]['authenticated_source_excerpts'][0]['fields'].update(sign='invented'),'differs from full selected witness')
  self.reject(lambda p:p['entries'][0]['source_attestations'][0].update(quantity=37),'invented quantity')
 def test_standalone_export_preserves_blanks_uncertainty_and_rights(self):
  out=m.calculate();w=json.loads(out[m.OUTPUTS[4]]);slots=list(csv.DictReader(io.StringIO(out[m.OUTPUTS[5]])))
  self.assertEqual(w['source_attestation_slots'],168);self.assertEqual(len(slots),168)
  self.assertEqual(len({s['attestation_id'] for s in slots}),168)
  self.assertTrue(all(s['record_license']=='CC BY-NC-SA 4.0' and 'Salgarella' in s['source_attribution'] and s['source_line_alignment']=='UNKNOWN' and s['raw_flags_interpretation']=='UNDECODED' for s in slots))
  source=[a for e in self.p['entries'] for a in e['source_attestations']]
  exported=[a['source_fields'] for e in w['entries'] for a in e['attestations']]
  self.assertEqual(source,exported)
  self.assertTrue(any(a['kind']=='blank' and a['sign']=='' for a in exported))
  self.assertTrue(any('?' in a['sign'] for a in exported))
 def test_quantity_not_found_in_number_field_and_all_reviews_blank(self):
  out=m.calculate();rows=list(csv.DictReader(io.StringIO(out[m.OUTPUTS[1]])));ht=next(c for c in rows if c['case_id']=='U001')
  self.assertEqual(json.loads(ht['authenticated_source_excerpts_json']),[])
  self.assertEqual(json.loads(ht['edition_quantity_assertions_json'])[0]['value'][0]['quantity'],38)
  review=list(csv.DictReader(io.StringIO(out[m.OUTPUTS[2]]),delimiter='\t'))
  self.assertEqual(len(review),25);self.assertTrue(all(r['decision']=='UNREVIEWED' and not r['reviewer'] and r['independent_review']=='false' for r in review))
if __name__=='__main__':unittest.main()
