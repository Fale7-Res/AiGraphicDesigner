#!/usr/bin/env python3
"""Unit and regression tests for Version 02: Hierarchical Scene Graph & Vector Optimization."""
from pathlib import Path
import sys
import unittest

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:10:00Z | CREATED | Author: orchestrator-planner
HERE = Path(__file__).resolve().parent
VERSION_ROOT = HERE.parent
sys.path.insert(0, str(VERSION_ROOT))

from src.geometry.bezier import VectorPoint, OptimizedBezierSegment, fit_smooth_curve
from src.pipeline import HierarchicalSceneGraphPipeline, SemanticObjectGroup, SemanticPathElement


class TestVersion02Pipeline(unittest.TestCase):
    """Test suite validating Version 02 Scene Graph and clean SVG output."""

    def test_vector_point_distance(self) -> None:
        """Verify vector point distance metric."""
        p1 = VectorPoint(10.0, 20.0)
        p2 = VectorPoint(13.0, 24.0)
        self.assertAlmostEqual(p1.distance_to(p2), 5.0)

    def test_optimized_bezier_segment_handles(self) -> None:
        """Verify optimized Bézier segment handles formatting."""
        p0 = VectorPoint(0.0, 0.0)
        h_out = VectorPoint(5.0, 10.0)
        h_in = VectorPoint(15.0, 10.0)
        p3 = VectorPoint(20.0, 0.0)
        seg = OptimizedBezierSegment(anchor_start=p0, handle_out=h_out, handle_in=h_in, anchor_end=p3)
        cmd = seg.to_svg_cubic_command()
        self.assertIn("C 5.00 10.00, 15.00 10.00, 20.00 0.00", cmd)

    def test_fit_smooth_curve_node_budget(self) -> None:
        """Verify node count respects budget."""
        points = [VectorPoint(float(i), float(i % 10)) for i in range(100)]
        segs = fit_smooth_curve(points, max_nodes=20)
        self.assertLessEqual(len(segs), 25)

    def test_pipeline_semantic_group_with_clippath(self) -> None:
        """Verify semantic group SVG generation contains <clipPath> and base/shadow elements."""
        pipeline = HierarchicalSceneGraphPipeline(max_nodes_budget=36)
        base_pts = [(0.0, 0.0), (100.0, 0.0), (100.0, 100.0), (0.0, 100.0)]
        shadow_pts = [(50.0, 50.0), (100.0, 50.0), (100.0, 100.0), (50.0, 100.0)]
        group = pipeline.create_semantic_group(
            group_id="fries_pack",
            label="fries",
            base_points=base_pts,
            base_color_hex="#FFAA00",
            shadow_points=shadow_pts,
            shadow_color_hex="#994400",
            shadow_opacity=0.4,
        )
        svg_group = group.to_svg_group()
        self.assertIn('<g id="fries_pack"', svg_group)
        self.assertIn('<clipPath id="clip_fries_pack">', svg_group)
        self.assertIn('clip-path="url(#clip_fries_pack)"', svg_group)
        self.assertIn('opacity="0.40"', svg_group)

        full_svg = pipeline.export_scene_graph_svg([group])
        self.assertIn("<svg", full_svg)
        self.assertIn("version-02", full_svg)


if __name__ == "__main__":
    unittest.main()
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:10:00Z | CREATED
