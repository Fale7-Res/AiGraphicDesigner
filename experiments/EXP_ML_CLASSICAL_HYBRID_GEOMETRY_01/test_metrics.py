# START CHANGE AGD-ML-METRIC-TESTS | 2026-10-30T08:20:30Z | CREATED | Author: root
"""Independent small analytic controls for evaluator coordinates/empty cases."""
import unittest
import numpy as np
from evaluate_results import support_stats,xy,samples_from_items
from construct_geometry import chain_graph
from svg_exporter import svg_graph
from xml.etree import ElementTree as ET

class MetricTests(unittest.TestCase):
    def test_exact_and_displaced_support(self):
        q=np.array([[0.,0.],[10.,0.]])
        self.assertEqual(support_stats(q,q,1.25)['recall'],1.)
        self.assertEqual(support_stats(q,q+np.array([0.,2.]),1.25)['recall'],0.)

    def test_empty_support_is_failure(self):
        self.assertEqual(support_stats(np.array([[1.,1.]]),np.empty((0,2)),1.25)['recall'],0.)
        lines,points=samples_from_items([])
        self.assertEqual(lines,[]);self.assertEqual(points.shape,(0,2))

    def test_pixel_centers_are_explicit(self):
        m=np.zeros((3,4),bool);m[1,2]=True
        np.testing.assert_array_equal(xy(m),[[2.5,1.5]])

    def test_open_curve_has_no_implicit_closure(self):
        item={'curves':[[[1.,1.],[2.,1.],[3.,2.],[4.,2.]]]}
        root=ET.fromstring(svg_graph(chain_graph([item],10,10)))
        path=list(root)[0]
        self.assertNotIn('Z',path.attrib['d']);self.assertEqual(path.attrib['stroke-width'],'0.35')

if __name__=='__main__':unittest.main()
# END CHANGE AGD-ML-METRIC-TESTS | 2026-10-30T08:20:30Z | CREATED | Author: root
