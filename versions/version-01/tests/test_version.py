#!/usr/bin/env python3
"""Unit and regression tests for Version 01: Sequential Pipeline Monolith."""
from pathlib import Path
import sys
import unittest

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:05:00Z | CREATED | Author: orchestrator-planner
HERE = Path(__file__).resolve().parent
VERSION_ROOT = HERE.parent
sys.path.insert(0, str(VERSION_ROOT))

from src.geometry.bezier import Point2D, BezierSegment, fit_schneider_bezier
from src.pipeline import SequentialPipeline, VectorLayer


class TestVersion01Pipeline(unittest.TestCase):
    """Test suite validating Version 01 geometry and pipeline functionality."""

    def test_point2d_euclidean_distance(self) -> None:
        """Verify 2D distance calculation."""
        p1 = Point2D(0.0, 0.0)
        p2 = Point2D(3.0, 4.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_bezier_segment_evaluation(self) -> None:
        """Verify cubic curve evaluation at t=0, t=0.5, t=1.0."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(0.0, 10.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(10.0, 0.0)
        seg = BezierSegment(p0, p1, p2, p3)
        self.assertEqual(seg.evaluate(0.0), p0)
        self.assertEqual(seg.evaluate(1.0), p3)
        mid = seg.evaluate(0.5)
        self.assertAlmostEqual(mid.x, 5.0)
        self.assertAlmostEqual(mid.y, 7.5)

    def test_fit_schneider_bezier_two_points(self) -> None:
        """Fitting two points returns exactly one cubic segment."""
        pts = [Point2D(0.0, 0.0), Point2D(100.0, 100.0)]
        segments = fit_schneider_bezier(pts)
        self.assertEqual(len(segments), 1)
        self.assertEqual(segments[0].p0, pts[0])
        self.assertEqual(segments[0].p3, pts[1])

    def test_pipeline_compile_clean_svg(self) -> None:
        """Verify pipeline produces valid SVG string with descriptor."""
        pipeline = SequentialPipeline(error_tolerance_px=1.5, max_nodes_per_path=36)
        contour = [(10.0, 10.0), (50.0, 10.0), (50.0, 50.0), (10.0, 50.0)]
        layer = pipeline.process_polygon_contour(contour, layer_id="layer_01", label="shield_base", fill_hex="#FF5733")
        svg = pipeline.compile_clean_svg([layer])
        self.assertIn("<svg", svg)
        self.assertIn("version-01", svg)
        self.assertIn('id="layer_01"', svg)
        self.assertIn('fill="#FF5733"', svg)

    def test_pipeline_default_gradient_disabled(self) -> None:
        """Verify pipeline defaults to enable_gradients=False to protect baseline fidelity."""
        pipeline = SequentialPipeline()
        self.assertFalse(pipeline.enable_gradients)
        self.assertEqual(pipeline.seed, 0)

    def test_bezier_segment_and_node_accounting(self) -> None:
        """Verify distinction between cubic segments (C), on-curve anchor nodes, and control handles."""
        p0 = Point2D(0.0, 0.0)
        p1 = Point2D(10.0, 0.0)
        p2 = Point2D(10.0, 10.0)
        p3 = Point2D(0.0, 10.0)
        seg1 = BezierSegment(p0, Point2D(3.0, 0.0), Point2D(7.0, 0.0), p1)
        seg2 = BezierSegment(p1, Point2D(10.0, 3.0), Point2D(10.0, 7.0), p2)
        seg3 = BezierSegment(p2, Point2D(7.0, 10.0), Point2D(3.0, 10.0), p3)
        seg4 = BezierSegment(p3, Point2D(0.0, 7.0), Point2D(0.0, 3.0), p0)
        subpath = [seg1, seg2, seg3, seg4]
        # In a closed loop of K cubic segments:
        k_segments = len(subpath)
        on_curve_anchors = k_segments
        off_curve_handles = k_segments * 2
        total_defining_points = on_curve_anchors + off_curve_handles
        self.assertEqual(k_segments, 4)
        self.assertEqual(on_curve_anchors, 4)
        self.assertEqual(off_curve_handles, 8)
        self.assertEqual(total_defining_points, 12)


if __name__ == "__main__":
    unittest.main()
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:05:00Z | CREATED
