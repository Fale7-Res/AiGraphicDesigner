# START CHANGE AGD-COVERAGE-FITTER-TEST | 2026-10-28T05:16:21Z | EDITED | Author: /root/appearance_fit
"""Actual-render composition controls for coverage-aware fitting."""
import json
import os
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image
from coverage_fitter import SVG, _render, _shape_signature, build_maps, fit_case


@unittest.skipUnless(os.environ.get("AGD_RENDERER_EXE") and os.environ.get("AGD_INHERITED_FITTER"), "Renderer and historical fitter required")
class FitterTests(unittest.TestCase):
    def _fixture(self, folder, alpha=False):
        defs='<defs><linearGradient id="fixedAlpha" x1="0" y1="0" x2="64" y2="0" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#fff" stop-opacity=".15"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient><mask id="fixedMask" style="mask-type:alpha" mask-type="alpha" maskUnits="userSpaceOnUse" x="0" y="0" width="64" height="48"><path fill="url(#fixedAlpha)" d="M0 0H64V48H0Z"/></mask></defs>' if alpha else ''
        group=' mask="url(#fixedMask)"' if alpha else ''
        paths='<path fill="#143c50" d="M0 0H64V48H0Z"/><path opacity=".5" fill="#d25a1e" d="M12 7H58V39H12Z"/><path fill="#1eb4c8" d="M30.2 3H30.8V46H30.2Z"/>'
        truth=f'<svg xmlns="{SVG}" width="64" height="48">{defs}<g{group}>{paths}</g></svg>'
        source=folder/'source.svg';source.write_text(truth)
        _render(ET.fromstring(truth),folder/'render_input.svg',folder/'source.png')
        root=ET.fromstring(truth)
        # Change only visible paint, preserving the soft alpha dependency.
        visible=root.find(f'{{{SVG}}}g')
        for path in visible:path.set('fill','#777777')
        baseline=folder/'baseline.svg';ET.ElementTree(root).write(baseline,encoding='utf-8')
        return source,baseline

    def test_source_over_coefficients_recover_thin_support(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);_,baseline=self._fixture(folder)
            metadata=build_maps(baseline,folder/'maps')
            self.assertLess(metadata['closure_max'],.02)
            self.assertLess(metadata['random_forward_rmse_bytes'],1.5)
            with np.load(folder/'maps/maps.npz') as values:
                w=values['weights'].reshape(3,48,64)
                self.assertGreater(w[2].sum(),0)
                self.assertLess(w[2].max(),1)
                self.assertAlmostEqual(float(w[1,15,20]),.5,delta=.01)
                self.assertAlmostEqual(float(w[0,15,20]),.5,delta=.01)
            self.assertEqual(build_maps(baseline,folder/'maps')['maps_npz_sha256'],metadata['maps_npz_sha256'])
            with (folder/'maps/maps.npz').open('ab') as stream:stream.write(b'corruption')
            with self.assertRaisesRegex(ValueError,'cache drift'):build_maps(baseline,folder/'maps')

    def test_joint_fit_preserves_soft_alpha_gradient_and_improves_render(self):
        with tempfile.TemporaryDirectory() as directory:
            folder=Path(directory);source,baseline=self._fixture(folder,alpha=True)
            build_maps(baseline,folder/'maps')
            fit_case(folder/'source.png',baseline,baseline,folder/'maps',folder/'flat.svg',folder/'gradient.svg',folder/'fit.json',max_seconds=20)
            original=ET.parse(baseline).getroot()
            for name in ('flat','gradient'):
                root=ET.parse(folder/f'{name}.svg').getroot()
                self.assertEqual(_shape_signature(root),_shape_signature(original))
                dependency=root.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')
                self.assertIsNotNone(dependency)
                self.assertEqual(ET.tostring(dependency),ET.tostring(original.find(f'.//{{{SVG}}}linearGradient[@id="fixedAlpha"]')))
            truth=np.asarray(Image.open(folder/'source.png').convert('RGBA'),dtype=float)
            target=truth[:,:,:3]*(truth[:,:,3:4]/255.)
            initial=_render(original,folder/'initial_probe.svg',folder/'initial.png')
            fitted=_render(ET.parse(folder/'flat.svg').getroot(),folder/'final_probe.svg',folder/'final.png')
            self.assertLess(float(np.mean((fitted-target)**2)),float(np.mean((initial-target)**2))*.05)
            np.testing.assert_equal(np.asarray(Image.open(folder/'initial.png'))[:,:,3],np.asarray(Image.open(folder/'final.png'))[:,:,3])
            diagnostic=json.loads((folder/'fit.json').read_text())
            self.assertIn('untouched_test_mse',diagnostic['flat_surrogate'])
            self.assertIn('Atotal-As',diagnostic['objective'])


if __name__=='__main__':unittest.main()
# END CHANGE AGD-COVERAGE-FITTER-TEST | 2026-10-28T05:16:21Z | EDITED
