# START CHANGE AGD-UNIVERSAL-COHERENCE-TEST | 2026-10-31T11:07:29Z | EDITED | Author: coherence_control
"""Generic fixtures only; no benchmark/case/reference input is read."""
from pathlib import Path
import sys
import unittest
import copy
import numpy as np
R=Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner')
sys.path[:0]=[str(R/'experiments/EXP_LOSS_ACCOUNTED_CONTOUR_CONSTRUCTION_01'),str(R/'experiments/EXP_ML_CLASSICAL_HYBRID_GEOMETRY_01'),str(Path.cwd()/'work/geometry-deps')]
from partition_fit import fit_trace
from coherence_refine import refine,polyline,curve_quality
from shapely.geometry import Polygon


def bundle(points,tid=0):
    p=np.asarray(points,float);fit=fit_trace(p,periodic=False)
    assert fit['chains'],fit
    return [dict(c,trace_id=tid) for c in fit['chains']],dict(trace_id=tid,source_points_xy=p.tolist())


class CoherenceTests(unittest.TestCase):
    def assert_anchors(self,before,after):
        for a,b in zip(before,after):
            ca=np.asarray(a['curves']);cb=np.asarray(b['curves'])
            self.assertTrue(np.array_equal(ca[0,0],cb[0,0]));self.assertTrue(np.array_equal(ca[-1,-1],cb[-1,-1]))
            self.assertEqual(a['closed'],b['closed']);self.assertEqual(a['partition_ids'],b['partition_ids'])
    def test_circle(self):
        t=np.linspace(0,2*np.pi,97);p=np.c_[30+15*np.cos(t),30+15*np.sin(t)];p[-1]=p[0]
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertTrue(np.array_equal(np.asarray(b[0]['curves'])[0,0],np.asarray(b[0]['curves'])[-1,-1]))
        for row in audit['chains']:
            for part in row.get('partitions',[]):self.assertLessEqual(part['deviation']['numerical_upper_envelope_px'],.6)
    def test_jaggy_staircase(self):
        p=[[0.,0.]]
        for k in range(20):p.extend([[k+1.,k+0.],[k+1.,k+1.]])
        a,s=bundle(p);b,audit=refine(a,[s]);self.assert_anchors(a,b)
        self.assertLessEqual(sum(len(x['curves']) for x in b),sum(len(x['curves']) for x in a))
        self.assertEqual(len(audit['chains']),len(a))
    def test_thin_L_corner(self):
        p=np.r_[np.c_[np.arange(0,11),np.zeros(11)],np.c_[np.full(10,10),np.arange(1,11)]]
        a,s=bundle(p);b,_=refine(a,[s]);self.assert_anchors(a,b)
        vertices=np.concatenate([np.asarray(x['curves'])[:,0] for x in b]+[np.asarray(b[-1]['curves'])[-1,-1:]])
        self.assertTrue(np.any(np.all(vertices==[10,0],axis=1)))
    def test_shared_junction(self):
        a,s=bundle([[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0]])
        c,t=bundle([[8,0],[8,1],[8,2],[8,3],[8,4],[8,5],[8,6],[8,7]],1)
        before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(np.array_equal(np.asarray(after[0]['curves'])[-1,-1],np.asarray(after[1]['curves'])[0,0]))
    def test_closed_hole_nesting(self):
        theta=np.linspace(0,2*np.pi,65)
        outer=np.c_[30+20*np.cos(theta),30+20*np.sin(theta)];outer[-1]=outer[0]
        inner=np.c_[30+7*np.cos(-theta),30+7*np.sin(-theta)];inner[-1]=inner[0]
        a,s=bundle(outer);c,t=bundle(inner,1);before=a+c;after,_=refine(before,[s,t]);self.assert_anchors(before,after)
        self.assertTrue(Polygon(polyline(after[0]['curves'])).contains(Polygon(polyline(after[1]['curves']))))
    def test_missing_provenance_explicit_rollback(self):
        a,s=bundle([[k,0] for k in range(10)]);a[0].pop('partition_ids');before=copy.deepcopy(a)
        b,audit=refine(a,[s]);self.assertEqual(b,before);self.assertEqual(audit['chains'][0]['reason'],'missing_partition_provenance')
    def test_quality_is_separate(self):
        a,s=bundle([[k,0] for k in range(10)]);q=curve_quality(a[0]['curves'])
        self.assertIn('sampled_curvature_p95',q);self.assertIn('length_fraction_cubic_span_le2px',q)


if __name__=='__main__':unittest.main()
# END CHANGE AGD-UNIVERSAL-COHERENCE-TEST | 2026-10-31T11:07:29Z | EDITED | Author: coherence_control
