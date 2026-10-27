"""Regression checks against actual saved research evidence; never trace or render."""
# START CHANGE AGD-GEN-QA | 2026-10-27T14:33:48Z | CREATED | Author: package_generalization
import json,unittest
from PIL import Image
from package_evidence import ROOT,check_saved_evidence,saved_inventory

class SavedGeneralizationEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report=check_saved_evidence()
    def test_frozen_sources_and_140_successful_candidates(self):
        self.assertEqual(tuple(self.report[k] for k in ('case_count','independent_originals','candidates','failed_candidates')),(8,7,140,0))
    def test_no_reconstruction_improvement_or_reranked_winner(self):
        self.assertEqual(self.report['same_winner_cases'],8);self.assertFalse(self.report['reconstruction_improvement_demonstrated'])
    def test_selected_transparency_exact_at_test_dimensions(self):
        rows=[r for r in self.report['cases'] if r['has_alpha']];self.assertEqual(len(rows),3)
        for row in rows:self.assertEqual(row['alpha_max_error_0_255'],0)
    def test_saved_metrics_and_all_svg_png_artifacts(self):
        self.assertEqual(self.report['status'],'PASS');self.assertGreaterEqual(self.report['svgs_parsed_raster_free'],140);self.assertGreaterEqual(self.report['pngs_decoded'],140)
    def test_saved_evidence_byte_preservation(self):
        self.assertEqual(json.loads((ROOT/'reports/saved_artifact_inventory.json').read_text()),saved_inventory())
    def test_visual_sheets_decode_and_dashboard_has_all_cases(self):
        document=(ROOT/'reports/dashboard.html').read_text(encoding='utf-8')
        for row in self.report['cases']:self.assertIn(row['id'],document)
        sheets=list((ROOT/'reports/comparisons').glob('*.png'));self.assertGreaterEqual(len(sheets),16)
        for path in sheets:
            with Image.open(path) as im:im.load();self.assertGreater(im.width,0)

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-GEN-QA | 2026-10-27T14:33:48Z | CREATED | Author: package_generalization
