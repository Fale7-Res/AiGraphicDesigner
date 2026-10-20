#!/usr/bin/env python3
"""Unit and regression tests for Version 03: Diffusion Latent Decomposition & Dual-Path Typography."""
from pathlib import Path
import sys
import unittest

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:15:00Z | CREATED | Author: orchestrator-planner
HERE = Path(__file__).resolve().parent
VERSION_ROOT = HERE.parent
sys.path.insert(0, str(VERSION_ROOT))

from src.geometry.bezier import TypographicPoint, CalligraphicBezierSegment, fit_typographic_bezier
from src.pipeline import DualPathTypographyPipeline, DualPathTypographyLayer


class TestVersion03Pipeline(unittest.TestCase):
    """Test suite validating Version 03 typography and dual-path output."""

    def test_typographic_point_corner_flag(self) -> None:
        """Verify typographic point corner flag preservation."""
        p = TypographicPoint(10.0, 20.0, is_corner=True)
        self.assertTrue(p.is_corner)
        p2 = TypographicPoint(13.0, 24.0)
        self.assertAlmostEqual(p.distance_to(p2), 5.0)

    def test_calligraphic_bezier_segment_output(self) -> None:
        """Verify calligraphic segment SVG output."""
        p0 = TypographicPoint(0.0, 0.0)
        p1 = TypographicPoint(10.0, 5.0)
        p2 = TypographicPoint(20.0, 5.0)
        p3 = TypographicPoint(30.0, 0.0)
        seg = CalligraphicBezierSegment(p0, p1, p2, p3)
        self.assertIn("C 10.00 5.00, 20.00 5.00, 30.00 0.00", seg.to_svg_cubic_path())

    def test_fit_typographic_bezier_with_corners(self) -> None:
        """Verify corner breakpoints split segments cleanly."""
        points = [
            TypographicPoint(0.0, 0.0),
            TypographicPoint(50.0, 0.0, is_corner=True),
            TypographicPoint(100.0, 50.0),
        ]
        segments = fit_typographic_bezier(points)
        self.assertEqual(len(segments), 2)
        self.assertEqual(segments[0].p0, points[0])
        self.assertEqual(segments[1].p3, points[2])

    def test_dual_path_pipeline_export(self) -> None:
        """Verify dual path SVG contains both outline and editable text nodes."""
        pipeline = DualPathTypographyPipeline(default_font_fallback="Amiri")
        contour = [(0.0, 0.0), (20.0, 0.0), (40.0, 20.0), (0.0, 20.0)]
        layer = pipeline.create_typography_layer(
            layer_id="logo_text",
            text="تصميم ذكي",
            font_family="Amiri",
            contour_points=contour,
            fill_hex="#222222",
        )
        svg = pipeline.export_dual_path_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-03", svg)
        self.assertIn('id="visual_outlines_layer"', svg)
        self.assertIn('id="editable_text_layer"', svg)
        self.assertIn('direction="rtl"', svg)
        self.assertIn("تصميم ذكي", svg)


if __name__ == "__main__":
    unittest.main()
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:15:00Z | CREATED
