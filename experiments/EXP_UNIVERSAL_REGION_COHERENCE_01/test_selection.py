# START CHANGE AGD-UNIVERSAL-SELECTION-TEST | 2026-10-31T11:07:29Z | EDITED | Author: root
import unittest
import numpy as np
from universal_run import selection_rank
class SelectionTests(unittest.TestCase):
 def test_deterministic_and_no_mutation(self):
  rgb=np.full((24,24,3),255,dtype='uint8');rgb[5:18,10:12]=0
  traces=[dict(trace_id=9,length_px=12,source_points_xy=[[10,5],[10,17]]),dict(trace_id=2,length_px=20,source_points_xy=[[1,1],[21,1]])]
  a,rows=selection_rank(traces,rgb);b,_=selection_rank(traces,rgb)
  self.assertEqual(a,b);self.assertEqual(len(rows),2);self.assertEqual(traces[0]['trace_id'],9);self.assertEqual(a[0]['trace_id'],9)
 def test_closure_is_source_only(self):
  p=[[2,2],[12,2],[12,12],[2,12],[2,2]];t=dict(trace_id=0,length_px=40,source_points_xy=p)
  _,rows=selection_rank([t],np.zeros((16,16,3),dtype='uint8'));self.assertTrue(rows[0]['closed']);self.assertEqual(t['source_points_xy'],p)
if __name__=='__main__':unittest.main()
# END CHANGE AGD-UNIVERSAL-SELECTION-TEST | 2026-10-31T11:07:29Z | EDITED | Author: root
