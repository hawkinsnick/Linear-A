#!/usr/bin/env python3
import copy,json,tempfile,unittest
from pathlib import Path
import build_public_sigla_layer as public
import build_gorila_route_audit as routes
class Layers(unittest.TestCase):
 def test_public_integrity(self):public.validate_committed()
 def test_routes(self):self.assertEqual(routes.build()['acquired_page_routes'],135)
 def test_unpinned_source(self):
  with self.assertRaises(AssertionError):public.outputs(b'{}')
 def test_session_removed(self):
  self.assertEqual(public.clean('https://cefael.efa.gr/detail.php?ce=SECRET&sp=67'),'https://cefael.efa.gr/detail.php?sp=67')
  self.assertIsNone(public.clean('missing'));self.assertIsNone(public.clean(None))
 def mutation(self,which,edit):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d)
   for p in ['research/edition-concordance.csv','analysis/edition-concordance-audit.json','research/edition-route-evidence.json','analysis/pre-expert-primary-collation.json','analysis/pre-expert-source-audit.json','data/unresolved_cases.csv',routes.PATH]:
    (root/p).parent.mkdir(parents=True,exist_ok=True);(root/p).write_bytes((routes.ROOT/p).read_bytes())
   payload=json.loads((root/routes.PATH).read_text());edit(payload);(root/routes.PATH).write_text(json.dumps(payload))
   with self.assertRaises((AssertionError,KeyError)):routes.build(root)
 def test_acquisition_not_reading(self):self.mutation('reading',lambda p:p['routes'][0].update(primary_reading_inspected=True))
 def test_shared_page_membership(self):self.mutation('ids',lambda p:p['routes'][0].update(source_record_ids=['INVENTED']))
 def test_no_certified_identity(self):self.mutation('object',lambda p:p['routes'][0].update(physical_object_identity_certified=True))
 def test_missing_page_rejected(self):self.mutation('missing',lambda p:p['routes'].pop())
if __name__=='__main__':unittest.main()
