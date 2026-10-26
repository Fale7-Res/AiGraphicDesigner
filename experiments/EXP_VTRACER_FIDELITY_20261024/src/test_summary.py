# START CHANGE VTRACER-SUMMARY-TEST | 2026-10-24T23:43:25Z | CREATED | Author: vtracer_sources
"""Spatial diagnostic and incomplete-evidence regression checks."""
import sys,tempfile,unittest
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from summarize import local_errors,collect

class SummaryTests(unittest.TestCase):
    def test_fixed_tiles_detect_concentrated_error(self):
        source=np.zeros((16,16,3),np.uint8);pred=source.copy();pred[:4,:4]=100
        result=local_errors(source,pred,[(1.5,1.5)])
        self.assertEqual(result['tile_rmse_worst'],100)
        self.assertEqual(result['tile_rmse_median'],0)
        self.assertGreater(result['seed_center_rmse'],0)
        self.assertEqual(local_errors(source,source)['tile_rmse_worst'],0)
    def test_incomplete_evidence_does_not_write_summary(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary);(root/'inputs').mkdir();(root/'protocol.json').write_text('{}')
            with self.assertRaises(ValueError):collect(root,root/'out')
            self.assertFalse((root/'out').exists())

if __name__=='__main__':unittest.main()
# END CHANGE VTRACER-SUMMARY-TEST | 2026-10-24T23:43:25Z | CREATED | Author: vtracer_sources
