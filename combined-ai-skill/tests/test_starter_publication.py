import importlib.util,json,subprocess,tempfile,unittest,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from publish_starter import publish,git
class Publisher:
 git=staticmethod(git)
 @staticmethod
 def publish(root,expected,before_push=None):
  def builder(root):return {'combined-ai-skill/downloads/starter.txt':b'validated instructions\n'},b'', 'test'
  return publish(root,expected,before_push,builder)
m=Publisher()
class PublicationTests(unittest.TestCase):
 def setUp(self):
  self.t=tempfile.TemporaryDirectory();self.base=Path(self.t.name);self.remote=self.base/'remote.git';self.work=self.base/'work';self.other=self.base/'other'
  self.sh(['git','init','--bare','--initial-branch=main',str(self.remote)])
  self.sh(['git','clone',str(self.remote),str(self.work)])
  self.configure(self.work);p=self.work/'ai-skill/scripts';p.mkdir(parents=True);(p/'validate_bundle.py').write_text('pass\n');(self.work/'.gitignore').write_text('__pycache__/\n');(self.work/'canonical.txt').write_text('source\n');self.sh(['git','add','.'],self.work);self.sh(['git','commit','-m','source'],self.work);self.sh(['git','push','origin','main'],self.work);self.source=m.git(self.work,'rev-parse','HEAD')
  self.sh(['git','clone',str(self.remote),str(self.other)]);self.configure(self.other)
  p=self.work/'combined-ai-skill/downloads';p.mkdir(parents=True);(p/'starter.txt').write_bytes(b'validated instructions\n')
 def tearDown(self):self.t.cleanup()
 def sh(self,args,cwd=None):return subprocess.run(args,cwd=cwd,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 def configure(self,r):self.sh(['git','config','user.email','test@example.invalid'],r);self.sh(['git','config','user.name','Test'],r)
 def advance(self):
  (self.other/'canonical.txt').write_text('new source\n');self.sh(['git','add','.'],self.other);self.sh(['git','commit','-m','concurrent source'],self.other);self.sh(['git','push','origin','main'],self.other)
 def test_publish_exact_parent(self):
  d=m.publish(self.work,self.source);self.assertTrue(d['published']);self.assertEqual(m.git(self.work,'rev-parse','HEAD^'),self.source)
 def test_advanced_source_skips_without_rebase(self):
  self.advance();d=m.publish(self.work,self.source);self.assertFalse(d['published']);self.assertEqual(m.git(self.work,'rev-parse','HEAD'),self.source)
 def test_race_after_guard_cannot_push(self):
  with self.assertRaises(subprocess.CalledProcessError):m.publish(self.work,self.source,self.advance)
  self.assertEqual(subprocess.check_output(['git','--git-dir',str(self.remote),'rev-parse','main'],text=True).strip(),m.git(self.other,'rev-parse','HEAD'))
  self.assertEqual(m.git(self.other,'show','HEAD:canonical.txt'),'new source')
 def test_unrelated_changes_rejected(self):
  (self.work/'canonical.txt').write_text('tampered\n')
  with self.assertRaises(ValueError):m.publish(self.work,self.source)
 def test_stale_output_cannot_publish(self):
  (self.work/'combined-ai-skill/downloads/starter.txt').write_text('stale')
  with self.assertRaises(ValueError):m.publish(self.work,self.source)
 def test_unrelated_staged_change_cannot_publish(self):
  (self.work/'other.txt').write_text('unrelated')
  self.sh(['git','add','other.txt'],self.work)
  with self.assertRaises(ValueError):m.publish(self.work,self.source)
if __name__=='__main__':unittest.main()
