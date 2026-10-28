"""Coverage diagnostics and reversible stroke invariants; no new searches."""
# START CHANGE AGD-COVERAGE-QA | 2026-10-27T20:38:55Z | EDITED | Author: package_generalization
import json,tempfile,unittest,xml.etree.ElementTree as ET
import coverage as coverage_module
from pathlib import Path
from coverage import ROOT,SVG,correct_coverage,rgb_paths

class CoverageTests(unittest.TestCase):
    def test_exact_partition_aa_seam_differs_from_known_union(self):
        results=json.loads((ROOT/'results/coverage/controls/results.json').read_text())
        for name in ('diagonal','curved'):
            row=results[name]['coverage']
            self.assertGreater(row['separate_1x']['interior_alpha_deficit_pixels'],0)
            self.assertEqual(row['compound_1x']['interior_alpha_deficit_pixels'],0)
            self.assertGreaterEqual(row['separate_1x']['coverage_deficit_source_pixel_equivalents'],row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'])
    def test_real_gap_negative_not_declared_repaired(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['genuine_gap']['coverage']
        self.assertGreater(row['compound_1x']['coverage_deficit_source_pixel_equivalents'],0)
        self.assertGreater(row['stroke025_1x']['coverage_deficit_source_pixel_equivalents'],0)
    def test_exterior_stroke_changes_known_silhouette(self):
        row=json.loads((ROOT/'results/coverage/controls/results.json').read_text())['exterior']['coverage']['4x']
        self.assertGreater(row['coverage_excess_source_pixel_equivalents'],0)
    def test_mask_and_path_geometry_untouched_gradient_paint_reused(self):
        source=f'<svg xmlns="{SVG}" width="8" height="8"><defs><mask id="m"><path fill="white" d="M0 0H8V8H0Z"/></mask><linearGradient id="g"/></defs><g mask="url(#m)"><path fill="url(#g)" d="M1 1H7V7H1Z"/></g></svg>'
        with tempfile.TemporaryDirectory() as tmp:
            a=Path(tmp)/'a.svg';b=Path(tmp)/'b.svg';a.write_text(source)
            before=ET.parse(a).getroot();correct_coverage(a,b);after=ET.parse(b).getroot()
            self.assertEqual(ET.tostring(next(before.iter(f'{{{SVG}}}mask'))),ET.tostring(next(after.iter(f'{{{SVG}}}mask'))))
            self.assertEqual([p.get('d') for p in rgb_paths(before)],[p.get('d') for p in rgb_paths(after)])
            self.assertEqual(rgb_paths(after)[0].get('stroke'),'url(#g)')
            self.assertEqual(a.read_text(),source)
    def test_out_of_scope_stroke_width_refused(self):
        with self.assertRaises(ValueError):correct_coverage('missing.svg','unused.svg',width=2)
    def test_nonempty_run_targets_refused(self):
        previous=coverage_module.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'results/coverage/controls').mkdir(parents=True)
            (root/'results/coverage/controls/preserved.txt').write_text('keep')
            coverage_module.ROOT=root
            try:
                with self.assertRaises(FileExistsError):coverage_module.run_exact_controls()
                (root/'results/coverage/A01_shield').mkdir()
                (root/'results/coverage/A01_shield/preserved.txt').write_text('keep')
                with self.assertRaises(FileExistsError):coverage_module.run_real_cases()
                self.assertEqual((root/'results/coverage/A01_shield/preserved.txt').read_text(),'keep')
            finally:coverage_module.ROOT=previous

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-COVERAGE-QA | 2026-10-27T20:38:55Z | EDITED | Author: package_generalization
