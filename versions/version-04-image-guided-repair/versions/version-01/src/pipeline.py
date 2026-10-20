#!/usr/bin/env python3
"""Sequential Pipeline Monolith implementation for Version 01.

Provides the end-to-end processing pipeline orchestrating edge-preserving color quantization,
compound-contour extraction with hole preservation, gradient-aware vectorization, topological
layer ordering, and Bézier vectorization for high fidelity and visual elegance.
"""
from dataclasses import dataclass, field
import math
from pathlib import Path
import sys
import time
import cv2
import numpy as np

# START CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:20:00Z | EDITED | Author: orchestrator-planner
from .geometry.bezier import Point2D, BezierSegment, fit_schneider_bezier


@dataclass
class VectorLayer:
    """Represents a single vector layer in the output design, supporting compound subpaths, holes, and gradients."""
    layer_id: str
    semantic_label: str
    z_index: int
    fill_color_hex: str
    segments: list[BezierSegment] = field(default_factory=list)
    subpaths: list[list[BezierSegment]] = field(default_factory=list)
    stroke_width: float = 0.75
    gradient_id: str | None = None
    gradient_def: str | None = None

    def to_svg_element(self) -> str:
        """Render this layer as an SVG path element with compound path (fill-rule='evenodd') and gradient support."""
        fill_attr = f'url(#{self.gradient_id})' if self.gradient_id else self.fill_color_hex
        stroke_attr = f' stroke="{self.fill_color_hex}" stroke-width="{self.stroke_width:.2f}" stroke-linejoin="round"' if self.stroke_width > 0 else ''
        
        if self.subpaths:
            d_parts = []
            for sub in self.subpaths:
                if not sub:
                    continue
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))
            if not d_parts:
                return ""
            d_attr = " ".join(d_parts)
            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            return f'<path id="{self.layer_id}" data-label="{self.semantic_label}" fill="{fill_attr}"{rule}{stroke_attr} d="{d_attr}" />'

        if not self.segments:
            return ""
        start = self.segments[0].p0
        path_data = [f"M {start.x:.2f} {start.y:.2f}"]
        for seg in self.segments:
            path_data.append(seg.to_svg_path_data())
        path_data.append("Z")
        d_attr = " ".join(path_data)
        return f'<path id="{self.layer_id}" data-label="{self.semantic_label}" fill="{fill_attr}"{stroke_attr} d="{d_attr}" />'


class SequentialPipeline:
    """Version 01 sequential monolith pipeline with gradient-aware, topologically ordered image tracing."""

    def __init__(
        self,
        error_tolerance_px: float = 0.8,
        max_nodes_per_path: int = 48,
        seed: int = 0,
        enable_gradients: bool = False,
    ) -> None:
        self.error_tolerance_px = error_tolerance_px
        self.max_nodes_per_path = max_nodes_per_path
        self.seed = seed
        self.enable_gradients = enable_gradients

    def process_polygon_contour(self, contour_points: list[tuple[float, float]], layer_id: str, label: str, fill_hex: str) -> VectorLayer:
        """Convert a 2D contour polygon into a fitted Bézier vector layer."""
        pts = [Point2D(x=p[0], y=p[1]) for p in contour_points]
        fitted_segments = fit_schneider_bezier(
            points=pts,
            max_error_px=self.error_tolerance_px,
            max_nodes=self.max_nodes_per_path,
            closed=True,
        )
        return VectorLayer(
            layer_id=layer_id,
            semantic_label=label,
            z_index=0,
            fill_color_hex=fill_hex,
            segments=fitted_segments,
            stroke_width=0.0,
        )

    def compile_clean_svg(
        self,
        layers: list[VectorLayer],
        width: int = 2048,
        height: int = 2048,
        bg_hex: str | None = None,
        defs: list[str] | None = None,
    ) -> str:
        """Assemble vector layers into a clean SVG document with optional background rect and gradient defs."""
        sorted_layers = sorted(layers, key=lambda l: l.z_index)
        
        all_defs = list(defs) if defs else []
        for l in sorted_layers:
            if l.gradient_def and l.gradient_def not in all_defs:
                all_defs.append(l.gradient_def)
                
        defs_str = ""
        if all_defs:
            defs_content = "\n    ".join(all_defs)
            defs_str = f"  <defs>\n    {defs_content}\n  </defs>\n"
            
        elements = []
        if bg_hex:
            elements.append(f'<rect width="{width}" height="{height}" fill="{bg_hex}" />')
        for l in sorted_layers:
            elem = l.to_svg_element()
            if elem:
                elements.append(elem)
        body = "\n  ".join(elements)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
            f'  <desc>Generated by AI Graphic Designer version-01</desc>\n'
            f'{defs_str}'
            f'  {body}\n'
            f'</svg>'
        )

    def estimate_linear_gradient(
        self,
        img_bgr: np.ndarray,
        outer_cnt: np.ndarray,
        hole_cnts: list[np.ndarray],
        layer_id: str,
    ) -> tuple[str | None, str | None]:
        """Estimate 2D linear gradient regression for a contour component if color variance is significant."""
        h, w = img_bgr.shape[:2]
        c_mask = np.zeros((h, w), dtype=np.uint8)
        cv2.drawContours(c_mask, [outer_cnt], -1, 255, -1)
        for h_cnt in hole_cnts:
            cv2.drawContours(c_mask, [h_cnt], -1, 0, -1)
            
        ys, xs = np.where(c_mask > 0)
        if len(xs) < 60:
            return None, None
            
        bgr_vals = img_bgr[ys, xs].astype(np.float64)
        mean_col = np.mean(bgr_vals, axis=0)
        std_col = np.std(bgr_vals, axis=0)
        total_std = np.sqrt(np.mean(std_col**2))
        
        if total_std < 10.0:
            return None, None
            
        x_c = xs - np.mean(xs)
        y_c = ys - np.mean(ys)
        X = np.column_stack([x_c, y_c])
        XtX = X.T @ X + np.eye(2) * 1e-4
        XtY = X.T @ (bgr_vals - mean_col)
        slopes = np.linalg.solve(XtX, XtY)
        
        pred = mean_col + X @ slopes
        ss_tot = np.sum((bgr_vals - mean_col)**2)
        ss_res = np.sum((bgr_vals - pred)**2)
        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 1e-5 else 0.0
        
        if r2 < 0.60:
            return None, None
            
        U, _, _ = np.linalg.svd(slopes)
        ux, uy = float(U[0, 0]), float(U[1, 0])
        
        t = x_c * ux + y_c * uy
        t_min, t_max = float(np.percentile(t, 5)), float(np.percentile(t, 95))
        if t_max - t_min < 8.0:
            return None, None
            
        x1 = float(np.mean(xs) + t_min * ux)
        y1 = float(np.mean(ys) + t_min * uy)
        x2 = float(np.mean(xs) + t_max * ux)
        y2 = float(np.mean(ys) + t_max * uy)
        
        c_start = np.clip(mean_col + t_min * (slopes[0, :] * ux + slopes[1, :] * uy), 0, 255)
        c_end = np.clip(mean_col + t_max * (slopes[0, :] * ux + slopes[1, :] * uy), 0, 255)
        
        hex_start = f"#{int(round(c_start[2])):02x}{int(round(c_start[1])):02x}{int(round(c_start[0])):02x}"
        hex_end = f"#{int(round(c_end[2])):02x}{int(round(c_end[1])):02x}{int(round(c_end[0])):02x}"
        
        gid = f"grad_{layer_id}"
        grad_def = (
            f'<linearGradient id="{gid}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" gradientUnits="userSpaceOnUse">\n'
            f'      <stop offset="0%" stop-color="{hex_start}" />\n'
            f'      <stop offset="100%" stop-color="{hex_end}" />\n'
            f'    </linearGradient>'
        )
        return gid, grad_def

    def process_image(
        self,
        image_path: Path | str,
        n_colors: int = 16,
        min_contour_area: float | None = None,
    ) -> tuple[str, dict]:
        """Process a raster image through CIELAB quantization and compound Bézier fitting to produce high-fidelity SVG."""
        t_start = time.perf_counter()
        img_bgr = cv2.imread(str(image_path))
        if img_bgr is None:
            raise FileNotFoundError(f"Image not found or unreadable: {image_path}")

        # Deterministic RNG seeding for 100% byte-identical reproducibility
        cv2.setRNGSeed(self.seed)
        np.random.seed(self.seed)

        h, w = img_bgr.shape[:2]

        # 1. Edge-preserving bilateral filter to suppress raster noise while keeping sharp edges
        smooth_bgr = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=25, sigmaSpace=10)
        img_lab = cv2.cvtColor(smooth_bgr, cv2.COLOR_BGR2LAB)

        # 2. Adaptive CIELAB K-Means clustering with deterministic seed
        k = max(4, min(n_colors, 32))
        pixels = np.float32(img_lab.reshape(-1, 3))
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
        _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 1, cv2.KMEANS_PP_CENTERS)
        labels_img = labels.reshape((h, w)).astype(np.uint8)

        centers_lab = np.uint8(centers.reshape((1, k, 3)))
        centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((k, 3))

        cluster_areas = [(int(np.sum(labels_img == ci)), ci) for ci in range(k)]
        cluster_areas.sort(key=lambda x: x[0], reverse=True)

        # Dominant background color (largest area cluster)
        bg_ci = cluster_areas[0][1]
        bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"

        # Adaptive minimum contour area selection if not explicitly provided
        if min_contour_area is None:
            edges = cv2.Canny(smooth_bgr, 50, 150)
            edge_ratio = float(np.count_nonzero(edges)) / float(h * w)
            min_area = 18.0 if edge_ratio > 0.08 else 8.0
        else:
            min_area = float(min_contour_area)

        layers: list[VectorLayer] = []
        total_nodes = 0
        total_paths = 0

        # 3. Contour extraction with full two-level hierarchy (RETR_CCOMP) to preserve internal holes
        for z_rank, (_, ci) in enumerate(cluster_areas):
            b, g, r = int(centers_bgr[ci][0]), int(centers_bgr[ci][1]), int(centers_bgr[ci][2])
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            mask = (labels_img == ci).astype(np.uint8) * 255

            contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
            if hierarchy is None or len(contours) == 0:
                continue

            hierarchy_arr = hierarchy[0]
            for i, h_node in enumerate(hierarchy_arr):
                if h_node[3] != -1:
                    continue

                outer_cnt = contours[i]
                if len(outer_cnt) < 3 or cv2.contourArea(outer_cnt) < min_area:
                    continue

                outer_approx = cv2.approxPolyDP(outer_cnt, epsilon=self.error_tolerance_px, closed=True)
                if len(outer_approx) < 3:
                    continue

                outer_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in outer_approx]
                outer_segs = fit_schneider_bezier(
                    points=outer_pts,
                    max_error_px=self.error_tolerance_px,
                    max_nodes=self.max_nodes_per_path,
                    closed=True,
                )
                if not outer_segs:
                    continue

                subpaths = [outer_segs]
                total_nodes += len(outer_segs)

                hole_cnts = []
                ch_idx = h_node[2]
                while ch_idx != -1:
                    hole_cnt = contours[ch_idx]
                    if len(hole_cnt) >= 3 and cv2.contourArea(hole_cnt) >= min_area:
                        hole_approx = cv2.approxPolyDP(hole_cnt, epsilon=self.error_tolerance_px, closed=True)
                        if len(hole_approx) >= 3:
                            hole_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in hole_approx]
                            hole_segs = fit_schneider_bezier(
                                points=hole_pts,
                                max_error_px=self.error_tolerance_px,
                                max_nodes=self.max_nodes_per_path,
                                closed=True,
                            )
                            if hole_segs:
                                subpaths.append(hole_segs)
                                hole_cnts.append(hole_cnt)
                                total_nodes += len(hole_segs)
                    ch_idx = hierarchy_arr[ch_idx][0]

                gid, gdef = None, None
                if self.enable_gradients and ci != bg_ci:
                    gid, gdef = self.estimate_linear_gradient(
                        img_bgr=img_bgr,
                        outer_cnt=outer_cnt,
                        hole_cnts=hole_cnts,
                        layer_id=f"c{ci}_{i}",
                    )

                layer = VectorLayer(
                    layer_id=f"layer_c{ci}_{i}",
                    semantic_label=f"cluster_{ci}_part_{i}",
                    z_index=z_rank,
                    fill_color_hex=hex_color,
                    subpaths=subpaths,
                    stroke_width=0.75,
                    gradient_id=gid,
                    gradient_def=gdef,
                )
                layers.append(layer)
                total_paths += 1

        compiled_svg = self.compile_clean_svg(layers, width=w, height=h, bg_hex=bg_hex)
        elapsed_ms = (time.perf_counter() - t_start) * 1000.0

        telemetry = {
            "image_path": str(image_path),
            "dimensions": [w, h],
            "clusters_count": k,
            "total_layers": len(layers),
            "total_paths": total_paths,
            "total_nodes": total_nodes,
            "elapsed_ms": round(elapsed_ms, 2),
            "svg_size_bytes": len(compiled_svg.encode("utf-8")),
        }
        return compiled_svg, telemetry
# END CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:20:00Z | EDITED
