# START CHANGE AGD-RAWFACE-TEST-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root
import unittest,copy,collections
import numpy as np
from face_cycles import split_closed_walk

class FaceWalkTests(unittest.TestCase):
    def test_pinched_triangles_preserve_every_directed_reference(self):
        raw={0:np.array([[0,0],[2,0],[1,1],[0,0]]),1:np.array([[0,0],[-2,0],[-1,-1],[0,0]])}
        refs=[{'chain':0,'forward':True},{'chain':1,'forward':True}];saved=copy.deepcopy(refs)
        pieces,n=split_closed_walk(refs,raw)
        self.assertEqual(n,1);self.assertEqual(len(pieces),2);self.assertEqual(refs,saved)
        self.assertEqual(collections.Counter((x['chain'],x['forward']) for p in pieces for x in p),collections.Counter((x['chain'],x['forward']) for x in refs))
    def test_no_silent_open_walk_fix(self):
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True}],{0:np.array([[0,0],[1,0]])})
    def test_reversed_references_and_hole_winding_not_reoriented(self):
        raw={0:np.array([[0,0],[1,0],[0,1],[0,0]])};refs=[{'chain':0,'forward':False}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs]);self.assertEqual(n,0)
    def test_degenerate_cycle_is_retained_not_pruned(self):
        raw={0:np.array([[0,0],[1,0],[0,0]])};refs=[{'chain':0,'forward':True}]
        pieces,n=split_closed_walk(refs,raw);self.assertEqual(pieces,[refs])
    def test_budget_is_fail_closed(self):
        raw={0:np.array([[0,0],[1,0],[0,0]]),1:np.array([[0,0],[0,1],[0,0]])}
        with self.assertRaises(ValueError):split_closed_walk([{'chain':0,'forward':True},{'chain':1,'forward':True}],raw,max_splits=0)

if __name__=='__main__':unittest.main()

# END CHANGE AGD-RAWFACE-TEST-FACE-CYCLES | 2026-10-29T12:20:15Z | CREATED | Author: root
