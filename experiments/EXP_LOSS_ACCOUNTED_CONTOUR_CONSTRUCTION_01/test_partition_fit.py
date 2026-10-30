# START CHANGE AGD-LOSS-CONTOUR-TEST | 2026-10-30T08:41:02Z | CREATED | Author: contour_partition
import unittest
import math
import time
import numpy as np
from partition_fit import construct, signed_area, flattened


class PartitionFitTests(unittest.TestCase):
    def assert_accounted(self,p,result):
        self.assertAlmostEqual(result['accepted_length_px']+result['rejected_length_px'],np.linalg.norm(np.diff(p,axis=0),axis=1).sum(),places=8)
        edges=[]
        for row in result['ledger']:edges.extend(range(row['lo'],row['hi']))
        self.assertEqual(edges,list(range(len(p)-1)))

    def test_circle_periodic_closed(self):
        t=np.linspace(0,2*np.pi,181);p=np.column_stack([20*np.cos(t),20*np.sin(t)]);p[-1]=p[0]
        q=construct(p,'Q');self.assert_accounted(p,q)
        self.assertTrue(q['closed_retained']);self.assertEqual(len(q['chains']),1)
        c=np.array(q['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],c[-1,3]))
        self.assertGreater(signed_area(flattened(c))*signed_area(p),0)
        for left,right in zip(c,np.concatenate([c[1:],c[:1]])):
            a=left[3]-left[2];b=right[1]-right[0]
            if np.linalg.norm(a)*np.linalg.norm(b)>1e-9:self.assertLess(abs(np.cross(a,b))/(np.linalg.norm(a)*np.linalg.norm(b)),1e-6)

    def test_square_sharp_corners(self):
        p=np.array([[0.,0.],[20,0],[20,20],[0,20],[0,0]])
        q=construct(p,'Q');self.assert_accounted(p,q);self.assertTrue(q['closed_retained'])
        c=np.array(q['chains'][0]['curves']);self.assertEqual(len(c),4)
        for v in p[:-1]:self.assertTrue(any(np.array_equal(v,a) for a in c[:,0]))

    def test_long_contour_no_lost_edges(self):
        x=np.linspace(0,300,601);p=np.column_stack([x,3*np.sin(x/35)])
        q=construct(p,'P');self.assert_accounted(p,q)
        self.assertEqual(q['rejected_length_px'],0)
        self.assertGreater(len(q['ledger']),8);self.assertEqual(len(q['chains']),1)
        self.assertTrue(all(r['length_px']<=32.000001 for r in q['ledger']))

    def test_open_junction_endpoints_and_same_conditions(self):
        p=np.array([[3.,4.],[6,4],[8,7],[11,10],[16,10]])
        a=construct(p,'P');b=construct(p,'Q');self.assertEqual(a['chains'],b['chains'])
        c=np.array(a['chains'][0]['curves']);self.assertTrue(np.array_equal(c[0,0],p[0]));self.assertTrue(np.array_equal(c[-1,-1],p[-1]))

    def test_nested_loop_winding(self):
        for radius,orientation in [(20,1),(8,-1)]:
            t=np.linspace(0,orientation*2*np.pi,121);p=np.column_stack([radius*np.cos(t),radius*np.sin(t)]);p[-1]=p[0]
            q=construct(p,'Q');self.assertTrue(q['closed_retained']);self.assertEqual(np.sign(signed_area(flattened(np.array(q['chains'][0]['curves'])))),orientation)

    def test_budget_rejection_is_explicit(self):
        x=np.linspace(0,200,401);p=np.column_stack([x,np.sin(x/25)])
        q=construct(p,'P',maximum_trace_cubics=1);self.assert_accounted(p,q)
        self.assertGreater(q['rejected_length_px'],0)
        self.assertTrue(any(r['reason']=='original_trace_cubic_budget' for r in q['ledger']))

    def test_deadline_ledger(self):
        p=np.column_stack([np.arange(101),np.zeros(101)])
        q=construct(p,'Q',deadline=time.monotonic()-1);self.assert_accounted(p,q)
        self.assertEqual(q['accepted_length_px'],0);self.assertTrue(all(r['reason']=='arm_wall_budget' for r in q['ledger']))

    def test_short_trace_and_duplicate_explicit(self):
        for p,reason in [(np.array([[0.,0.],[1,0]]),'short_chain'),(np.array([[0.,0.],[0,0],[9,0]]),'duplicate_adjacent_points')]:
            q=construct(p);self.assert_accounted(p,q);self.assertEqual(q['reason'],reason)

    def test_two_source_junction_traces_keep_same_endpoint(self):
        paths=[np.array([[0.,0.],[3,0],[8,0]]),np.array([[0.,0.],[0,3],[0,8]])]
        curves=[construct(p)['chains'][0]['curves'] for p in paths]
        self.assertEqual(curves[0][0][0],curves[1][0][0])


if __name__=='__main__':unittest.main()
# END CHANGE AGD-LOSS-CONTOUR-TEST | 2026-10-30T08:41:02Z | CREATED | Author: contour_partition
