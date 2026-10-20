import sys, unittest, xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
V4=Path(__file__).resolve().parents[1];sys.path.insert(0,str(V4))
from src.challenger import Challenger,Config,estimate_target_regions
NS={'s':'http://www.w3.org/2000/svg'}
class ChallengerTests(unittest.TestCase):
 def test_svg_is_valid_vector_and_has_shared_geometry_clips(self):
  img=np.full((32,48,3),(239,238,232),dtype=np.uint8);img[7:26,10:36]=(190,20,30)
  svg,m=Challenger(Config(initial_segments=100,target_regions=35)).vectorize(img)
  root=ET.fromstring(svg)
  self.assertEqual(root.tag.rsplit('}',1)[-1],'svg')
  self.assertEqual(root.findall('.//s:image',NS),[])
  self.assertGreater(len(root.findall('.//s:path',NS)),0)
  self.assertGreaterEqual(len(root.findall('.//s:clipPath',NS)),2)
  self.assertGreater(m['gradient_count'],0)
 def test_no_pixel_run_overlay_or_raster_payload(self):
  img=np.tile(np.arange(48,dtype=np.uint8)[None,:,None],(32,1,3))
  svg,_=Challenger(Config(initial_segments=100,target_regions=35)).vectorize(img)
  self.assertNotIn('edge-band-residuals',svg)
  self.assertNotIn('<image',svg)
  self.assertNotIn('data:image',svg)
 def test_adaptive_budget_respects_texture_complexity_range(self):
  flat=np.full((64,64,3),128,dtype=np.uint8)
  rng=np.random.default_rng(7);texture=rng.integers(0,256,(64,64,3),dtype=np.uint8)
  flat_target,_=estimate_target_regions(flat);texture_target,_=estimate_target_regions(texture)
  self.assertTrue(220<=flat_target<=560)
  self.assertTrue(220<=texture_target<=560)
  self.assertGreaterEqual(texture_target,flat_target)
 def test_deterministic_vectorization(self):
  img=np.zeros((40,45,3),dtype=np.uint8);img[:]=(235,235,235);img[8:33,9:37]=(220,35,40)
  cfg=Config(initial_segments=100,target_regions=35)
  a,_=Challenger(cfg).vectorize(img);b,_=Challenger(cfg).vectorize(img)
  self.assertEqual(a,b)
if __name__=='__main__':unittest.main()
