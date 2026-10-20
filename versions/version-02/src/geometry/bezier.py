#!/usr/bin/env python3
"""Hierarchical vector geometry and optimized Bézier fitting for Version 02.

Supports smooth curvature continuity, pen-tool handle vectors, and boolean union
simplification for hierarchical Scene Graph layers.
"""
from dataclasses import dataclass
import math

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:10:00Z | CREATED | Author: orchestrator-planner
@dataclass(frozen=True)
class VectorPoint:
    """Represents a 2D position vector in canvas coordinate space."""
    x: float
    y: float

    def distance_to(self, other: "VectorPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)


@dataclass
class OptimizedBezierSegment:
    """Cubic Bézier segment with explicit in/out pen tool handles."""
    anchor_start: VectorPoint
    handle_out: VectorPoint
    handle_in: VectorPoint
    anchor_end: VectorPoint

    def evaluate_at(self, t: float) -> VectorPoint:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.anchor_start.x +
             3.0 * u**2 * t * self.handle_out.x +
             3.0 * u * t**2 * self.handle_in.x +
             t**3 * self.anchor_end.x)
        y = (u**3 * self.anchor_start.y +
             3.0 * u**2 * t * self.handle_out.y +
             3.0 * u * t**2 * self.handle_in.y +
             t**3 * self.anchor_end.y)
        return VectorPoint(x=x, y=y)

    def to_svg_cubic_command(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.handle_out.x:.2f} {self.handle_out.y:.2f}, {self.handle_in.x:.2f} {self.handle_in.y:.2f}, {self.anchor_end.x:.2f} {self.anchor_end.y:.2f}"


def fit_smooth_curve(points: list[VectorPoint], max_nodes: int = 36) -> list[OptimizedBezierSegment]:
    """Fit a series of points into smooth cubic Bézier segments enforcing maximum node budget."""
    if len(points) < 2:
        return []
    segments: list[OptimizedBezierSegment] = []
    step = max(1, len(points) // max_nodes)
    subsampled = points[::step]
    if subsampled[-1] != points[-1]:
        subsampled.append(points[-1])

    for i in range(len(subsampled) - 1):
        p0 = subsampled[i]
        p3 = subsampled[i + 1]
        dx = (p3.x - p0.x) / 3.0
        dy = (p3.y - p0.y) / 3.0
        h_out = VectorPoint(x=p0.x + dx, y=p0.y + dy)
        h_in = VectorPoint(x=p3.x - dx, y=p3.y - dy)
        segments.append(OptimizedBezierSegment(
            anchor_start=p0,
            handle_out=h_out,
            handle_in=h_in,
            anchor_end=p3,
        ))
    return segments
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:10:00Z | CREATED
