"""Abstract Track A controls; no research benchmark/GT input."""
# START CHANGE AGD-THIN-TRACK-A-TESTS | 2026-10-29T11:31:15Z | EDITED | Author: package_generalization
import unittest
import numpy as np
from track_a import discover,DEFAULT_CONFIG

def line_control(supported=True):
    rgb=np.full((21,41,3),255,np.uint8);labels=np.ones((21,41),np.uint32)
    rgb[10,5:35]=[24,30,40];labels[10,5:15]=2;labels[10,17:35]=3
    if not supported:rgb[10,15:17]=255
    return rgb,labels

class TrackATests(unittest.TestCase):
    def test_supported_missing_label_connector(self):
        rgb,labels=line_control();out,audit,evidence=discover(rgb,labels)
        self.assertEqual(audit['accepted_bridges'],1);self.assertEqual(audit['connector_pixels'],2)
        self.assertEqual(out[10,5],out[10,34]);self.assertEqual(audit['output_regions'],2)
        self.assertEqual(int(evidence['connector_mask'].sum()),2)
    def test_blank_gap_rejected_no_global_fallback(self):
        rgb,labels=line_control(False);out,audit,_=discover(rgb,labels)
        np.testing.assert_array_equal(out,labels);self.assertEqual(audit['accepted_bridges'],0)
        self.assertEqual(audit['status'],'UNCHANGED_NO_CONFIDENT_PROPOSAL')
    def test_determinism_and_input_immutability(self):
        rgb,labels=line_control();original=labels.copy();r1,a1,e1=discover(rgb,labels);r2,a2,e2=discover(rgb,labels)
        np.testing.assert_array_equal(labels,original);np.testing.assert_array_equal(r1,r2)
        self.assertEqual(a1['bridges'],a2['bridges']);np.testing.assert_array_equal(e1['connector_mask'],e2['connector_mask'])
    def test_parallel_offset_features_not_joined(self):
        rgb=np.full((24,40,3),255,np.uint8);labels=np.ones((24,40),np.uint32)
        rgb[8,4:15]=20;labels[8,4:15]=2;rgb[12,17:30]=20;labels[12,17:30]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
    def test_adjacent_tonal_regions_not_globally_merged(self):
        rgb=np.full((21,41,3),255,np.uint8);labels=np.ones((21,41),np.uint32)
        rgb[10,5:35]=20;labels[10,5:20]=2;labels[10,20:35]=3
        out,audit,_=discover(rgb,labels);self.assertEqual(audit['accepted_bridges'],0);np.testing.assert_array_equal(out,labels)
    def test_pair_budget_and_convex_mixture(self):
        rgb,labels=line_control();out,audit,_=discover(rgb,labels,{'max_endpoint_pairs':0})
        self.assertEqual(audit['endpoint_pairs_tested'],0);self.assertGreater(audit['endpoint_pairs_truncated'],0)
        np.testing.assert_array_equal(out,labels)
        _,audit,_=discover(rgb,labels)
        for bridge in audit['bridges']:
            self.assertGreaterEqual(bridge['min_mixture_fraction'],0);self.assertLessEqual(bridge['mean_mixture_fraction'],1)

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-THIN-TRACK-A-TESTS | 2026-10-29T11:31:15Z | EDITED | Author: package_generalization
