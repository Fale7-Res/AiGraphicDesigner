"""Passive checks for frozen known-vector controls; no tracing or fitting."""
# START CHANGE AGD-CA-FIXTURE-QA | 2026-10-28T05:13:01Z | CREATED | Author: package_generalization
import hashlib,json,tempfile,unittest,xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image
import fixtures

class AnalyticFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest=json.loads((fixtures.ROOT/'inputs/analytic/manifest.json').read_text())
    def test_two_small_frozen_controls_and_reference_reuse(self):
        self.assertEqual(self.manifest['status'],'FROZEN_BEFORE_FITTING')
        self.assertEqual(len(self.manifest['cases']),2);self.assertEqual(len(self.manifest['existing_control_references']),2)
        for ref in self.manifest['existing_control_references']:
            self.assertEqual(hashlib.sha256(Path(ref['truth_svg']).read_bytes()).hexdigest(),ref['truth_sha256'])
            self.assertEqual(hashlib.sha256(Path(ref['source_png']).read_bytes()).hexdigest(),ref['source_sha256'])
        for case in self.manifest['cases']:
            self.assertLessEqual(case['paint_paths'],8);self.assertLessEqual(max(case['dimensions']),160)
            self.assertEqual(case['license'],'CC0-1.0')
    def test_frozen_hashes_and_real_png_decoding(self):
        for case in self.manifest['cases']:
            folder=fixtures.ROOT/Path(case['truth_svg']).parent
            for name,record in case['files'].items():
                self.assertEqual(hashlib.sha256((folder/name).read_bytes()).hexdigest(),record['sha256'])
            with Image.open(fixtures.ROOT/case['source_png']) as im:
                im.load();self.assertEqual(list(im.size),case['dimensions'])
    def test_no_raster_or_dense_grid_and_same_initial_geometry(self):
        for case in self.manifest['cases']:
            a=ET.parse(fixtures.ROOT/case['truth_svg']).getroot();b=ET.parse(fixtures.ROOT/case['initial_svg']).getroot()
            for node in a.iter():self.assertNotIn(node.tag.rsplit('}',1)[-1],('image','filter','script','foreignObject'))
            paths=[p for p in a.iter(f'{{{fixtures.SVG}}}path') if p.get('id')]
            self.assertEqual(len(paths),case['paint_paths'])
            self.assertEqual([(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in paths],[(p.get('id'),p.get('d'),p.get('opacity'),p.get('fill-rule')) for p in b.iter(f'{{{fixtures.SVG}}}path') if p.get('id')])
    def test_gradient_stop_family_and_subpixel_features(self):
        for case in self.manifest['cases']:
            for gradient in case['truth_gradients']:
                stops=gradient['stops'];self.assertLessEqual(len(stops),4)
                np.testing.assert_allclose([float(s['offset']) for s in stops],np.linspace(0,1,len(stops)),atol=1e-10)
            self.assertTrue(all(0<r['nominal_perpendicular_width_px']<1 for r in case['thin_regions']))
    def test_soft_alpha_is_actual_vector_mask_and_visible_in_render(self):
        case=self.manifest['cases'][1];root=ET.parse(fixtures.ROOT/case['truth_svg']).getroot()
        self.assertEqual(len(list(root.iter(f'{{{fixtures.SVG}}}mask'))),1)
        alpha=np.asarray(Image.open(fixtures.ROOT/case['source_png']).convert('RGBA'))[:,:,3]
        self.assertGreater(int(((alpha>0)&(alpha<255)).sum()),1000);self.assertGreater(int((alpha==0).sum()),0)
    def test_nonempty_freeze_target_refused(self):
        previous=fixtures.ROOT
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);(root/'inputs/analytic').mkdir(parents=True);(root/'inputs/analytic/keep.txt').write_text('keep')
            fixtures.ROOT=root
            try:
                with self.assertRaises(FileExistsError):fixtures.freeze_fixtures()
            finally:fixtures.ROOT=previous

if __name__=='__main__':unittest.main(verbosity=2)
# END CHANGE AGD-CA-FIXTURE-QA | 2026-10-28T05:13:01Z | CREATED | Author: package_generalization
