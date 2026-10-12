from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
class PublicationWorkflowTests(unittest.TestCase):
 def test_guarded_native_and_master_publishers(self):
  native=(ROOT/'.github/workflows/sync-ai-skill.yml').read_text()
  master=(ROOT/'.github/workflows/combined-ai-starter.yml').read_text()
  for text in [native,master]:
   self.assertNotIn('git pull --rebase',text)
   self.assertNotIn('git push --force',text)
  self.assertIn('python ai-skill/scripts/publish_sync.py',native)
  self.assertIn('python combined-ai-skill/scripts/publish_starter.py',master)
  self.assertIn("test_starter*.py",master)
