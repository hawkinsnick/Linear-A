import copy,importlib.util,unittest
from pathlib import Path
from unittest.mock import patch
spec=importlib.util.spec_from_file_location('coverage',Path(__file__).with_name('coverage_denominators.py'));m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
class CoverageBoundaries(unittest.TestCase):
 def test_valid(self):m.validate()
 def reject(self,mutate):
  genuine=m.load;bad=copy.deepcopy(genuine('corpus-factory/coverage-denominators.json'));mutate(bad)
  with patch.object(m,'load',side_effect=lambda p:bad if p=='corpus-factory/coverage-denominators.json' else genuine(p)):
   with self.assertRaises(ValueError):m.validate()
 def test_fabricated_physical_population(self):self.reject(lambda x:x.update(aggregate_physical_population=12000))
 def test_fabricated_collection_reconciliation(self):self.reject(lambda x:x.update(collection_primary_reconciliation_complete=True))
 def test_historical_promoted_to_current(self):self.reject(lambda x:x['members'][0].update(freshness='FRESH_BOUNDED_SOURCE_CHECKPOINT'))
 def test_mixed_view_unit(self):self.reject(lambda x:x['members'][0]['views'][0].update(unit='physical_inscription'))
if __name__=='__main__':unittest.main()
