"""Excerpt validation must never silently weaken the default full-film gate."""
import sys,json,tempfile,hashlib,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]))
from production_standard import validate_standard
from finishing_contract import validate_finishing
class ScopeTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);self.r=Path(self.tmp.name)
  self.c={'id':'new','production_standard':'sun-disappeared-v1','width':1080,'height':1920,'fps':30,'scene_fps':12,'brand_ending':'london-bridge-v1','motion_review_targets':'motion.json','visual_style':'image-led','capture_scope':'isolated-preflight','finishing':{'enabled':True,'implementation':'render.cjs','contract':'contract.md','runtime_proof':'proof.json','studio':'render.cjs'}}
  (self.r/'motion.json').write_text(json.dumps({'duration':3,'events':[{'t':t,'operation':'reveal','understanding':'relationship'}for t in [0,1.5,2.5]]}))
  (self.r/'contract.md').write_text('contract');(self.r/'render.cjs').write_text('renderer')
  self.proof={'native':[1080,1920],'deterministic':True,'cases':[{'t':t,'meanRedDifference':3,'opaqueCaptionDifference':0}for t in [.5,1,2]],'temporal_grain':{'changed_mean_abs':.7},'studio_sha256':hashlib.sha256(b'renderer').hexdigest()}
  (self.r/'proof.json').write_text(json.dumps(self.proof))
 def test_explicit_excerpt_checks_actual_tail(self):
  self.assertFalse(validate_standard(self.c,self.r,3,scope='isolated-preflight')['ending_included'])
  self.assertFalse(validate_finishing(self.c,self.r,'release',expected_size=[1080,1920],scope='isolated-preflight')['ending_included'])
 def test_default_full_film_requires_ending(self):
  with self.assertRaises(ValueError):validate_standard(self.c,self.r,3)
  with self.assertRaises(ValueError):validate_finishing(self.c,self.r,'release',expected_size=[1080,1920])
 def test_undeclared_excerpt_rejected(self):
  self.c.pop('capture_scope')
  with self.assertRaises(ValueError):validate_standard(self.c,self.r,3,scope='isolated-preflight')
  with self.assertRaises(ValueError):validate_finishing(self.c,self.r,'release',expected_size=[1080,1920],scope='isolated-preflight')
 def test_excerpt_still_rejects_stale_renderer(self):
  (self.r/'render.cjs').write_text('changed')
  with self.assertRaises(ValueError):validate_finishing(self.c,self.r,'release',expected_size=[1080,1920],scope='isolated-preflight')
if __name__=='__main__':unittest.main()
