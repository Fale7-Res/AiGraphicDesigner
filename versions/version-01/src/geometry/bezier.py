#!/usr/bin/env python3
"""Schneider Bézier curve fitting and cubic segment representation for Version 01.

Implements a robust curve fitting algorithm with corner preservation, bounded control
handle lengths, and adaptive point reduction for faithful image tracing.
"""
from dataclasses import dataclass
import math
import cv2
import numpy as np

# START CHANGE TASK-V01-FIDELITY-01 | 2026-10-17T17:10:00Z | EDITED | Author: orchestrator-planner
@dataclass(frozen=True)
class Point2D:
    """Represents a 2D coordinate point."""
    x: float
    y: float

    def distance_to(self, other: "Point2D") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)


@dataclass
class BezierSegment:
    """Cubic Bézier curve segment defined by start, two control points, and end."""
    p0: Point2D
    p1: Point2D
    p2: Point2D
    p3: Point2D

    def evaluate(self, t: float) -> Point2D:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.p0.x +
             3.0 * u**2 * t * self.p1.x +
             3.0 * u * t**2 * self.p2.x +
             t**3 * self.p3.x)
        y = (u**3 * self.p0.y +
             3.0 * u**2 * t * self.p1.y +
             3.0 * u * t**2 * self.p2.y +
             t**3 * self.p3.y)
        return Point2D(x=x, y=y)

    def to_svg_path_data(self) -> str:
        """Format cubic Bézier segment as SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"


def fit_schneider_bezier(
    points: list[Point2D],
    max_error_px: float = 1.5,
    max_nodes: int = 48,
    closed: bool = False
) -> list[BezierSegment]:
    """Fit a series of digitized points with cubic Bézier segments preserving sharp corners and fidelity."""
    if len(points) < 2:
        return []
    if len(points) == 2:
        p0, p3 = points[0], points[1]
        p1 = Point2D(x=p0.x + (p3.x - p0.x) / 3.0, y=p0.y + (p3.y - p0.y) / 3.0)
        p2 = Point2D(x=p0.x + 2.0 * (p3.x - p0.x) / 3.0, y=p0.y + 2.0 * (p3.y - p0.y) / 3.0)
        return [BezierSegment(p0=p0, p1=p1, p2=p2, p3=p3)]

    pts = list(points)
    # Adaptive corner-preserving simplification if points exceed max_nodes
    if len(pts) > max_nodes and max_nodes >= 6:
        np_pts = np.array([[p.x, p.y] for p in pts], dtype=np.float32).reshape((-1, 1, 2))
        eps = max(0.4, max_error_px * 0.3)
        while len(pts) > max_nodes and eps <= 2.5:
            approx = cv2.approxPolyDP(np_pts, epsilon=eps, closed=closed)
            pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in approx]
            eps += 0.2
        if not closed and points[-1] not in pts:
            pts.append(points[-1])

    n = len(pts)
    if n < 2:
        return []
    if n == 2:
        p0, p3 = pts[0], pts[1]
        p1 = Point2D(x=p0.x + (p3.x - p0.x) / 3.0, y=p0.y + (p3.y - p0.y) / 3.0)
        p2 = Point2D(x=p0.x + 2.0 * (p3.x - p0.x) / 3.0, y=p0.y + 2.0 * (p3.y - p0.y) / 3.0)
        return [BezierSegment(p0=p0, p1=p1, p2=p2, p3=p3)]

    segments: list[BezierSegment] = []
    num_segments = n if closed else n - 1

    for i in range(num_segments):
        p_prev = pts[(i - 1) % n] if closed else pts[max(0, i - 1)]
        p1 = pts[i]
        p2 = pts[(i + 1) % n] if closed else pts[min(n - 1, i + 1)]
        p_next = pts[(i + 2) % n] if closed else pts[min(n - 1, i + 2)]

        chord_dx = p2.x - p1.x
        chord_dy = p2.y - p1.y
        chord_len = math.hypot(chord_dx, chord_dy)
        if chord_len < 1e-4:
            continue

        v_in = (p1.x - p_prev.x, p1.y - p_prev.y)
        len_in = math.hypot(*v_in)
        v_out = (p_next.x - p2.x, p_next.y - p2.y)
        len_out = math.hypot(*v_out)

        # Cusp detection at p1
        is_corner_p1 = False
        if len_in > 1e-4:
            cos_p1 = (v_in[0] * chord_dx + v_in[1] * chord_dy) / (len_in * chord_len)
            if cos_p1 < -0.35:  # Angle < ~110 degrees is a corner cusp
                is_corner_p1 = True

        # Cusp detection at p2
        is_corner_p2 = False
        if len_out > 1e-4:
            cos_p2 = (chord_dx * v_out[0] + chord_dy * v_out[1]) / (chord_len * len_out)
            if cos_p2 < -0.35:
                is_corner_p2 = True

        if is_corner_p1:
            t1 = (chord_dx / chord_len, chord_dy / chord_len)
        else:
            t1_un = (p2.x - p_prev.x, p2.y - p_prev.y)
            t1_len = math.hypot(*t1_un)
            t1 = (t1_un[0] / t1_len, t1_un[1] / t1_len) if t1_len > 1e-4 else (chord_dx / chord_len, chord_dy / chord_len)

        if is_corner_p2:
            t2 = (chord_dx / chord_len, chord_dy / chord_len)
        else:
            t2_un = (p_next.x - p1.x, p_next.y - p1.y)
            t2_len = math.hypot(*t2_un)
            t2 = (t2_un[0] / t2_len, t2_un[1] / t2_len) if t2_len > 1e-4 else (chord_dx / chord_len, chord_dy / chord_len)

        # Handle lengths strictly bounded by 1/3 of chord length to eliminate loops and overshoots
        h1 = chord_len / 3.0
        h2 = chord_len / 3.0

        b1 = Point2D(p1.x + h1 * t1[0], p1.y + h1 * t1[1])
        b2 = Point2D(p2.x - h2 * t2[0], p2.y - h2 * t2[1])
        segments.append(BezierSegment(p0=p1, p1=b1, p2=b2, p3=p2))

    return segments
# END CHANGE TASK-V01-FIDELITY-01 | 2026-10-17T17:10:00Z | EDITED

