# START CHANGE EXP-GEOMETRY-APPEARANCE-01 | 2026-10-27T14:43:00Z | CREATED | Author: /root/appearance_fit
"""Dedicated controls for fixed-geometry appearance fitting, not natural-image claims."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import time
import unittest
import xml.etree.ElementTree as ET

import numpy as np
from PIL import Image

from fit_appearance import SVG, _basis, _fit_region, _matrix, _paths, fit_svg


class AppearanceTests(unittest.TestCase):
    def test_alpha_squared_weighted_flat(self):
        xy = np.array([[0., 0.], [1., 0.], [2., 0.], [3., 0.]])
        rgb = np.array([[0., 0., 0.], [255., 255., 255.], [51., 51., 51.], [51., 51., 51.]])
        flat, selected, diagnostic = _fit_region(xy, rgb, np.array([0, 1]), np.array([2]), np.array([3]), time.monotonic() + 10, np.array([1., .25, 1., 1.]))
        np.testing.assert_allclose(flat["colors"], [[51., 51., 51.]])
        self.assertEqual(selected["kind"], "flat")
        self.assertAlmostEqual(diagnostic["selected_test_mse"], 0.)

    def test_basis_partition_and_clamp(self):
        b = _basis(np.array([-2., 0, .2, .7, 1, 2]), 4)
        np.testing.assert_allclose(b.sum(axis=1), 1)
        self.assertTrue(np.all(b >= 0))
        np.testing.assert_allclose(b[0], [1, 0, 0, 0])
        np.testing.assert_allclose(b[-1], [0, 0, 0, 1])

    def test_affine_transform_order(self):
        matrix = _matrix("translate(10 5) scale(2,3)")
        np.testing.assert_allclose(matrix @ [1, 2, 1], [12, 11, 1])
        with self.assertRaises(ValueError):
            _matrix("nonsense(1)")

    @unittest.skipUnless(os.environ.get("AGD_RENDERER_EXE"), "Actual resvg executable required")
    def test_linear_render_geometry_and_translation(self):
        self._control("linear")

    @unittest.skipUnless(os.environ.get("AGD_RENDERER_EXE"), "Actual resvg executable required")
    def test_radial_render_and_holdout(self):
        self._control("radial")

    def _control(self, kind):
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            baseline = folder / "baseline.svg"
            geometry = '<g transform="translate(8,6)"><path transform="translate(2,3)" d="M -10 -9 L 54 -9 L 54 55 L -10 55 Z" fill="#777777"/></g>'
            baseline.write_text(f'<svg xmlns="{SVG}" width="64" height="64">{geometry}</svg>', encoding="utf-8")
            if kind == "linear":
                gradient = '<linearGradient id="ref" gradientUnits="userSpaceOnUse" x1="-10" y1="0" x2="54" y2="0"><stop offset="0" stop-color="#14283c"/><stop offset="1" stop-color="#dcaa78"/></linearGradient>'
            else:
                gradient = '<radialGradient id="ref" gradientUnits="userSpaceOnUse" cx="22" cy="23" r="45"><stop offset="0" stop-color="#f0dfc0"/><stop offset="1" stop-color="#203040"/></radialGradient>'
            source = folder / "source.svg"
            source.write_text(f'<svg xmlns="{SVG}" width="64" height="64"><defs>{gradient}</defs>{geometry.replace(chr(35)+"777777", "url(#ref)")}</svg>', encoding="utf-8")
            png = folder / "source.png"
            subprocess.run([os.environ["AGD_RENDERER_EXE"], str(source), str(png)], check=True, capture_output=True)
            c, d, info = folder / "c.svg", folder / "d.svg", folder / "diagnostic.json"
            result = fit_svg(png, baseline, c, d, info, deadline_seconds=30)
            cpaths, dpaths = _paths(ET.parse(c).getroot()), _paths(ET.parse(d).getroot())
            self.assertEqual(len(cpaths), len(dpaths))
            for (cp, cm), (dp, dm) in zip(cpaths, dpaths):
                self.assertEqual({k: v for k, v in cp.attrib.items() if k != "fill"}, {k: v for k, v in dp.attrib.items() if k != "fill"})
                np.testing.assert_equal(cm, dm)
            stops = ET.parse(d).getroot().findall(f".//{{{SVG}}}stop")
            self.assertTrue(2 <= len(stops) <= 4)
            region = result["regions"][0]
            self.assertGreater(region["test_count"], 0)
            self.assertLess(region["selected_test_mse"], region["flat_test_mse"] * .1)
            self.assertLessEqual(region["optimizer_evaluations"], 100)
            for svg in (c, d):
                subprocess.run([os.environ["AGD_RENDERER_EXE"], str(svg), str(svg.with_suffix(".png"))], check=True, capture_output=True)
            reference = np.asarray(Image.open(png).convert("RGB"), dtype=float)
            crender = np.asarray(Image.open(c.with_suffix(".png")).convert("RGB"), dtype=float)
            drender = np.asarray(Image.open(d.with_suffix(".png")).convert("RGB"), dtype=float)
            self.assertLess(np.mean((drender-reference)**2), np.mean((crender-reference)**2) * .1)
            self.assertEqual(json.loads(info.read_text())["path_count"], 1)


if __name__ == "__main__":
    unittest.main()
# END CHANGE EXP-GEOMETRY-APPEARANCE-01 | 2026-10-27T14:43:00Z | CREATED
