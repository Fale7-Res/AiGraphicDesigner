"""Small invariants for the isolated V04 experimental engine."""
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

import numpy as np

VERSION_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(VERSION_DIR))
from src.challenger import AdaptiveVectorSurface, Config, add_edge_residual_layer  # noqa: E402

SVG_NS = {'svg': 'http://www.w3.org/2000/svg'}


class ChallengerTests(unittest.TestCase):
    def test_surface_output_stays_within_leaf_budget_and_contains_no_raster(self):
        rgb = np.zeros((32, 48, 3), dtype=np.uint8)
        rgb[:] = (238, 240, 242)
        rgb[5:26, 9:37] = (20, 60, 90)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=180)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(root.tag.rsplit('}', 1)[-1], 'svg')
        self.assertLessEqual(meta['leaf_cells'], 180)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), meta['rectangles'])
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])

    def test_constant_image_is_valid_svg_and_has_no_gradient_need(self):
        rgb = np.full((24, 24, 3), (128, 128, 128), dtype=np.uint8)
        svg, meta = AdaptiveVectorSurface(Config(max_cells=40)).vectorize(rgb)
        root = ET.fromstring(svg)
        self.assertEqual(len(root.findall('.//svg:rect', SVG_NS)), 1)
        self.assertEqual(meta['linear_gradients'], 0)
        self.assertIn('#808080', svg.lower())

    def test_edge_residual_is_explicit_vector_hybrid(self):
        rgb = np.zeros((30, 30, 3), dtype=np.uint8)
        rgb[:] = (245, 245, 245)
        rgb[8:22, 7:23] = (200, 20, 30)
        base, _ = AdaptiveVectorSurface(Config(max_cells=120)).vectorize(rgb)
        hybrid, edge = add_edge_residual_layer(base, rgb, dilation=1, color_bits=5)
        root = ET.fromstring(hybrid)
        self.assertIn('Hybrid vector-only representation', hybrid)
        self.assertIn('edge-band-residuals', hybrid)
        self.assertGreater(edge['edge_residual_pixels'], 0)
        self.assertEqual(edge['embedded_raster_images'], 0)
        self.assertEqual(root.findall('.//svg:image', SVG_NS), [])
        self.assertGreater(len(root.findall('.//svg:path', SVG_NS)), 0)

    def test_edge_residual_is_deterministic(self):
        yy, xx = np.indices((25, 31))
        rgb = np.stack([xx * 7 % 256, yy * 9 % 256, (xx + yy) * 5 % 256], axis=2).astype(np.uint8)
        base1, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        base2, _ = AdaptiveVectorSurface(Config(max_cells=90)).vectorize(rgb)
        out1, meta1 = add_edge_residual_layer(base1, rgb)
        out2, meta2 = add_edge_residual_layer(base2, rgb)
        self.assertEqual(out1, out2)
        self.assertEqual(meta1, meta2)


if __name__ == '__main__':
    unittest.main()
