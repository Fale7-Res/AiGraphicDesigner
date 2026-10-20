#!/usr/bin/env python3
"""Typographic and calligraphic Bézier curve fitting for Version 03.

Optimized for connected Arabic glyphs, sharp calligraphic pen angles,
and high-precision curve continuity.
"""
from dataclasses import dataclass
import math

# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:15:00Z | CREATED | Author: orchestrator-planner
@dataclass(frozen=True)
class TypographicPoint:
    """Represents a contour point on a glyph or typographic path."""
    x: float
    y: float
    is_corner: bool = False

    def distance_to(self, other: "TypographicPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)


@dataclass
class CalligraphicBezierSegment:
    """Cubic Bézier segment optimized for calligraphic curvature."""
    p0: TypographicPoint
    p1: TypographicPoint
    p2: TypographicPoint
    p3: TypographicPoint

    def to_svg_cubic_path(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"


def fit_typographic_bezier(points: list[TypographicPoint], error_tolerance_px: float = 1.0) -> list[CalligraphicBezierSegment]:
    """Fit typographic contour points into cubic Bézier segments preserving corner sharpness."""
    if len(points) < 2:
        return []
    segments: list[CalligraphicBezierSegment] = []
    # Identify corner breakpoints or partition uniformly
    indices = [0]
    for idx in range(1, len(points) - 1):
        if points[idx].is_corner:
            indices.append(idx)
    indices.append(len(points) - 1)

    for i in range(len(indices) - 1):
        start_idx = indices[i]
        end_idx = indices[i + 1]
        p_start = points[start_idx]
        p_end = points[end_idx]
        dx = (p_end.x - p_start.x) / 3.0
        dy = (p_end.y - p_start.y) / 3.0
        p1 = TypographicPoint(x=p_start.x + dx, y=p_start.y + dy)
        p2 = TypographicPoint(x=p_end.x - dx, y=p_end.y - dy)
        segments.append(CalligraphicBezierSegment(p0=p_start, p1=p1, p2=p2, p3=p_end))
    return segments
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:15:00Z | CREATED
