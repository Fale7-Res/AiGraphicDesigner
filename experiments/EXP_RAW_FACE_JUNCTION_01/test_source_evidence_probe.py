# START CHANGE AGD-RAWFACE-TEST-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root
"""Small implementation tests; do not substitute for independent geometry QA."""
import unittest
import numpy as np
from source_evidence_probe import extract, _near


class EvidenceTests(unittest.TestCase):
    def test_constant_has_no_edges_or_ridges(self):
        arrays, meta = extract(np.full((24, 30, 3), 127, np.uint8))
        self.assertEqual(meta['persistent_edge_pixels'], 0)
        self.assertEqual(meta['ridge_maxima'], {'dark': 0.0, 'light': 0.0})
        self.assertFalse(arrays['persistent_edges'].any())

    def test_empty_support_does_not_create_corner_evidence(self):
        self.assertFalse(_near(np.zeros((5, 5), bool), 1.0).any())

    def test_deterministic_nonmutating_source_only(self):
        source = np.full((32, 32, 3), 240, np.uint8)
        source[5:27, 12:15] = [10, 10, 10]
        snapshot = source.copy()
        first, metadata = extract(source)
        second, _ = extract(source)
        np.testing.assert_array_equal(source, snapshot)
        for key in first:
            np.testing.assert_array_equal(first[key], second[key])
            self.assertEqual(first[key].shape, source.shape[:2])
            self.assertTrue(np.isfinite(first[key]).all())
        self.assertGreater(metadata['persistent_edge_pixels'], 0)
        self.assertGreater(metadata['ridge_maxima']['dark'], 0)
        self.assertFalse(metadata['config']['output_is_reconstructed_geometry'])

    def test_rejects_ambiguous_float_or_rgba_input(self):
        for source in [np.zeros((4, 4, 3)), np.zeros((4, 4, 4), np.uint8)]:
            with self.assertRaises(ValueError):
                extract(source)


if __name__ == '__main__':
    unittest.main()

# END CHANGE AGD-RAWFACE-TEST-SOURCE-EVIDENCE-PROBE | 2026-10-29T12:20:15Z | CREATED | Author: root
