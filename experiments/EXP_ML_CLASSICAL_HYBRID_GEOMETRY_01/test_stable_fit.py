# START CHANGE AGD-ML-FIT-CONTROL-TEST | 2026-10-30T07:59:01Z | CREATED | Author: fitting_stability
import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'geometry-deps'))
import numpy as np
from stable_fit import fit,construct,measure

class StableFitTests(unittest.TestCase):
    def test_unequal_chord_cannot_create_long_short_handle(self):
        curves,_=construct(np.array([[0,0],[10,0],[11,1],[30,2]],float))
        lengths=np.linalg.norm(curves[:,3]-curves[:,0],axis=1)
        self.assertTrue(np.all(np.linalg.norm(curves[:,1]-curves[:,0],axis=1)<=lengths/3+1e-12))
        self.assertTrue(np.all(np.linalg.norm(curves[:,3]-curves[:,2],axis=1)<=lengths/3+1e-12))
    def test_sharp_corner_preserved(self):
        raw=np.array([[0,0],[2,0],[2,2]],float)
        curves,meta=fit(raw)
        self.assertIsNotNone(curves);self.assertEqual(meta['intentional_corner_count'],1)
        np.testing.assert_equal(curves[0,3],curves[1,0])
        self.assertLess(meta['numerical_upper_envelope_px'],.01)
    def test_no_budget_fallback(self):
        points=np.array([[i,i%2] for i in range(20)],float)
        curves,meta=fit(points,maximum_segments=2)
        self.assertIsNone(curves);self.assertEqual(meta['reason'],'cubic_budget')
    def test_nonfinite_rejected(self):
        self.assertIsNone(fit(np.array([[0,0],[np.nan,1]]))[0])
    def test_segment_distance_not_vertex_distance(self):
        raw=np.array([[0,0],[100,0]],float);curves,_=construct(raw)
        self.assertLess(measure(raw,curves)['curve_to_raw_max_px'],1e-10)

if __name__=='__main__':unittest.main()
# END CHANGE AGD-ML-FIT-CONTROL-TEST | 2026-10-30T07:59:01Z | CREATED | Author: fitting_stability
