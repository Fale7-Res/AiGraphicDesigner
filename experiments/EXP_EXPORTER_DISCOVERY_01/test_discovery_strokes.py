# START CHANGE AGD-SOURCE-STROKES-TEST | 2026-10-29T21:58:16Z | CREATED | Author: discovery_strokes
"""Synthetic behavior checks; never benchmark construction or truth tuning."""
import unittest
import numpy as np
import discovery_strokes as ds


class SourceStrokeTests(unittest.TestCase):
    def test_uniform_has_no_candidates(self):
        audit, arrays = ds.discover(np.full((32, 48, 3), 255, np.uint8))
        self.assertEqual(audit['accepted'], [])
        self.assertEqual(int(arrays['source_skeleton'].sum()), 0)

    def test_single_boundary_not_stroke(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[:, :24] = 0
        audit, _ = ds.discover(rgb)
        self.assertEqual(audit['accepted'], [])

    def test_absent_label_thin_stroke_proposal(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = 0
        original = rgb.copy()
        audit, _ = ds.discover(rgb)
        self.assertTrue(audit['accepted'])
        self.assertTrue(np.array_equal(original, rgb))
        self.assertTrue(all(x['width_px'] <= 6 for x in audit['accepted']))
        self.assertFalse(audit['integrated_into_shared_graph'])
        self.assertNotIn('<image', ds.svg(audit, 48, 32))

    def test_deterministic_geometry(self):
        rgb = np.full((32, 48, 3), 255, np.uint8); rgb[15:17, 7:40] = (180, 0, 0)
        first, _ = ds.discover(rgb); second, _ = ds.discover(rgb)
        self.assertEqual(first['accepted'], second['accepted'])

    def test_junction_trace_edges_once(self):
        sk = np.zeros((9, 9), bool); sk[4, 1:8] = True; sk[1:5, 4] = True
        chains, adjacency = ds._trace(sk)
        observed = sum(len(chain)-1 for chain in chains)
        expected = sum(len(near) for near in adjacency.values())//2
        self.assertEqual(observed, expected)
        self.assertEqual(len(chains), 3)

    def test_corner_fit_keeps_vertex(self):
        points = np.array([[2., 2.], [3, 2], [4, 2], [5, 2], [5, 3], [5, 4], [5, 5]])
        curves, meta = ds._fit(points)
        self.assertIsNotNone(curves)
        self.assertEqual(meta['intentional_corner_count'], 1)
        self.assertTrue(np.array_equal(curves[0, 3], [5, 2]))

    def test_loop_trace_closes_once(self):
        sk = np.zeros((9, 9), bool)
        sk[2, 2:7] = True; sk[6, 2:7] = True
        sk[2:7, 2] = True; sk[2:7, 6] = True
        chains, _ = ds._trace(sk)
        self.assertEqual(len(chains), 1)
        self.assertTrue(np.array_equal(chains[0][0], chains[0][-1]))
        self.assertEqual(len(chains[0])-1, 16)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            ds.discover(np.zeros((10, 10), np.uint8))


if __name__ == '__main__':
    unittest.main()
# END CHANGE AGD-SOURCE-STROKES-TEST | 2026-10-29T21:58:16Z | CREATED | Author: discovery_strokes
