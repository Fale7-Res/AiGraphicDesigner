"""Independent formula and scientific-contract tests; no dataset fitting."""
# START CHANGE AGD-COVERAGE-TEST | 2026-10-28T05:23:52Z | CREATED | Author: root
import unittest
import numpy as np
import research as r
class ResearchTests(unittest.TestCase):
    def test_balanced_background_objective(self):
        rng=np.random.default_rng(42);p=rng.random((30,3))*255;s=rng.random((30,3))*255
        ar=rng.random((30,1));ass=rng.random((30,1));bg=np.array([[255,255,255],[0,0,0],[40,80,120]])
        actual=np.mean([np.mean((p-s+(ass-ar)*b)**2) for b in bg])
        target=s+(ar-ass)*bg.mean(axis=0)
        constant=np.mean([(ass-ar)**2*(b-bg.mean(axis=0))**2 for b in bg])
        self.assertAlmostEqual(actual,float(np.mean((p-target)**2)+constant),places=9)
    def test_manifest_capacity_and_no_search(self):
        import json
        m=json.loads((r.ROOT/'inputs/manifest.json').read_text())
        self.assertEqual(len(m['cases']),9);self.assertEqual(m['architecture'],'NOT_APPROVED')
        self.assertEqual(sum(c['kind']=='real' for c in m['cases']),5)
        self.assertIn('No tracing/searches',m['protocol']['geometry'])
if __name__=='__main__':unittest.main()
# END CHANGE AGD-COVERAGE-TEST | 2026-10-28T05:23:52Z | CREATED | Author: root
