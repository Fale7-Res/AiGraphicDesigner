# START CHANGE VTRACER-TEST | 2026-10-24T09:56:47Z | CREATED | Author: vtracer_engine
"""Tests for benchmark normalization, bounded search and native worker."""
import json,tempfile,unittest
from pathlib import Path
import numpy as np
from PIL import Image
from search import OWNER,pilot_configs,refined_configs,prepare_input,fidelity_score,run_trial

class SearchTests(unittest.TestCase):
    def test_exact_owner_mapping_and_budget(self):
        pilots=pilot_configs();self.assertEqual(pilots[0],OWNER)
        self.assertEqual(OWNER['layer_difference'],0);self.assertEqual(OWNER['simplify'],1.5)
        self.assertEqual(len(pilots),13);self.assertEqual(len(refined_configs(OWNER)),4)
        self.assertEqual({p['clustering'] for p in pilots},{'color-cluster','watershed','bw'})
        self.assertEqual({p['hierarchical'] for p in pilots},{'cutout','stacked'})
    def test_alpha_normalization_and_original_immutable(self):
        with tempfile.TemporaryDirectory() as folder:
            src=Path(folder)/'source.png';out=Path(folder)/'normalized.png'
            a=np.array([[[200,0,0,0],[0,0,0,255],[255,0,0,128]]],dtype=np.uint8);Image.fromarray(a,'RGBA').save(src);original=src.read_bytes()
            info=prepare_input(src,out);actual=np.array(Image.open(out))
            np.testing.assert_array_equal(actual[0],[[255,255,255],[0,0,0],[255,127,127]])
            self.assertEqual(src.read_bytes(),original);self.assertEqual(info['alpha_extrema'],[0,255])
    def test_multimetric_score_and_empty_edges(self):
        m={'ssim':1.,'psnr_db':None,'identical':True,'edge_f1_1_5px':None,'delta_e76_mean':0.,'highpass_rmse_sigma1':0.}
        self.assertAlmostEqual(fidelity_score(m),1.)
        for k,v in [('ssim',.5),('delta_e76_mean',10),('highpass_rmse_sigma1',10),('edge_f1_1_5px',.5)]:self.assertLess(fidelity_score(m|{k:v}),1.)
    def test_native_pixel_worker(self):
        with tempfile.TemporaryDirectory() as folder:
            folder=Path(folder);a=np.zeros((16,16,3),dtype=np.uint8);a[:8]=[255,0,0];a[8:]=[0,120,255];source=folder/'s.png';Image.fromarray(a).save(source)
            r=run_trial(source,folder/'trial',OWNER|{'mode':'pixel','simplify':None})
            self.assertEqual(r['status'],'ok',r);self.assertTrue(r['structure']['raster_free']);self.assertGreater(r['metrics']['ssim'],.95)
            self.assertEqual(r['vtracer_version'],'1.0.0a4')

if __name__=='__main__':unittest.main()

# END CHANGE VTRACER-TEST | 2026-10-24T09:56:47Z | CREATED | Author: vtracer_engine
