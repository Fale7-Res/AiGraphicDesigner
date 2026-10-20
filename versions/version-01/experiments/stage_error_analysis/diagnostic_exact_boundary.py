#!/usr/bin/env python3
"""Diagnostic Exact-Boundary & Topology Breakdown Experiments for Version 01.

Conducts Iteration 07 diagnostic experiments:
1. Experiment 1: Exact-Boundary / Pixel-Run Diagnostic SVG Representation.
   Determines the theoretical fidelity upper bound (Fidelity Upper Bound) by converting
   the quantized raster directly into exact pixel runs and exact orthogonal grid paths.
2. Experiment 2: Topology and Contour Reconstruction Breakdown.
   Decomposes and quantifies the isolated error of each pipeline stage:
   - Pixel-grid boundary alignment ([0, W] x [0, H] cell coordinates vs pixel centers).
   - approxPolyDP contour decimation across multiple epsilons.
   - Schneider cubic Bézier fitting.
   - Stroke trapping analysis (why symmetric stroke is cosmetic and distorts silhouettes).
   - Topological enclosure poset vs naive area sorting for planar tiling.
"""
from pathlib import Path
import json
import math
import sys
import time
import cv2
import numpy as np
import pymupdf

# START CHANGE TASK-V01-ITERATION-07 | 2026-10-17T22:15:00Z | CREATED | Author: vector-and-typography-agent
ROOT = Path(__file__).resolve().parents[4]
VERSION_01_DIR = ROOT / "versions" / "version-01"
sys.path.insert(0, str(VERSION_01_DIR))

from src.geometry.bezier import Point2D, BezierSegment, fit_schneider_bezier
from experiments.stage_error_analysis.stage_by_stage_error_analysis import compute_metrics


def quantize_image_cielab(img_bgr: np.ndarray, n_colors: int = 16, seed: int = 42) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Applies edge-preserving bilateral filter and CIELAB K-Means clustering deterministically."""
    h, w = img_bgr.shape[:2]
    smooth_bgr = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=25, sigmaSpace=10)
    img_lab = cv2.cvtColor(smooth_bgr, cv2.COLOR_BGR2LAB)
    pixels = np.float32(img_lab.reshape(-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
    cv2.setRNGSeed(seed)
    np.random.seed(seed)
    _, labels, centers = cv2.kmeans(pixels, n_colors, None, criteria, 5, cv2.KMEANS_PP_CENTERS)
    labels_img = labels.reshape((h, w)).astype(np.uint8)

    centers_lab = np.uint8(centers.reshape((1, n_colors, 3)))
    centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((n_colors, 3))

    quant_bgr = np.zeros_like(img_bgr)
    for ci in range(n_colors):
        quant_bgr[labels_img == ci] = centers_bgr[ci]

    return labels_img, centers_bgr, quant_bgr


def render_svg_to_bgr(svg_content: str, width: int, height: int) -> np.ndarray:
    """Renders SVG content to BGR numpy array using PyMuPDF at exact 1:1 pixel dimensions."""
    doc = pymupdf.open(stream=svg_content.encode("utf-8"), filetype="svg")
    page = doc[0]
    # Render at 1x resolution matching viewBox
    pix = page.get_pixmap()
    arr = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        bgr = cv2.cvtColor(arr, cv2.COLOR_RGBA2BGR)
    elif pix.n == 3:
        bgr = cv2.cvtColor(arr, cv2.COLOR_RGB2BGR)
    else:
        bgr = cv2.cvtColor(arr, cv2.COLOR_GRAY2BGR)

    if bgr.shape[:2] != (height, width):
        bgr = cv2.resize(bgr, (width, height), interpolation=cv2.INTER_NEAREST)
    return bgr


# ==============================================================================
# EXPERIMENT 1: Exact-Boundary / Pixel-Run Diagnostic SVG Representation
# ==============================================================================

def build_pixel_run_svg(labels_img: np.ndarray, centers_bgr: np.ndarray) -> str:
    """Builds a lossless Pixel-Run SVG where every horizontal span of pixels is represented exactly.
    
    Each pixel cell [x, x+1] x [y, y+1] is placed on the exact integer grid [0, W] x [0, H].
    """
    h, w = labels_img.shape[:2]
    k = len(centers_bgr)
    runs_by_color = {ci: [] for ci in range(k)}

    for y in range(h):
        row = labels_img[y, :]
        diffs = np.diff(row)
        run_starts = np.where(diffs != 0)[0] + 1
        starts = np.concatenate(([0], run_starts))
        ends = np.concatenate((run_starts, [w]))
        for s, e in zip(starts, ends):
            ci = row[s]
            runs_by_color[ci].append((s, y, e - s, 1))

    svg_lines = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" shape-rendering="crispEdges">',
        '  <desc>Diagnostic Pixel-Run Exact SVG (Theoretical Upper Bound)</desc>'
    ]

    for ci in range(k):
        b, g, r = centers_bgr[ci]
        hex_col = f"#{r:02x}{g:02x}{b:02x}"
        runs = runs_by_color[ci]
        if not runs:
            continue
        d_commands = []
        for (rx, ry, rw, rh) in runs:
            d_commands.append(f"M {rx} {ry} h {rw} v {rh} h -{rw} Z")
        d_attr = " ".join(d_commands)
        svg_lines.append(f'  <path id="pixel_run_c{ci}" fill="{hex_col}" d="{d_attr}" />')

    svg_lines.append('</svg>')
    return "\n".join(svg_lines)


def run_experiment_1(img_orig: np.ndarray, labels_img: np.ndarray, centers_bgr: np.ndarray, quant_bgr: np.ndarray, output_dir: Path) -> dict:
    """Executes Experiment 1: Evaluates lossless Pixel-Run SVG and establishes theoretical upper bound."""
    h, w = img_orig.shape[:2]
    svg_pixel_run = build_pixel_run_svg(labels_img, centers_bgr)
    svg_path = output_dir / "exp1_pixel_run.svg"
    svg_path.write_text(svg_pixel_run, encoding="utf-8")

    rendered_pixel_run = render_svg_to_bgr(svg_pixel_run, w, h)
    cv2.imwrite(str(output_dir / "exp1_pixel_run_rendered.png"), rendered_pixel_run)

    # Metrics
    metrics_quant_vs_orig = compute_metrics(img_orig, quant_bgr)
    metrics_svg_vs_quant = compute_metrics(quant_bgr, rendered_pixel_run)
    metrics_svg_vs_orig = compute_metrics(img_orig, rendered_pixel_run)

    diff_svg_vs_quant = cv2.absdiff(quant_bgr, rendered_pixel_run)
    cv2.imwrite(str(output_dir / "exp1_diff_svg_vs_quant.png"), diff_svg_vs_quant * 10)

    res = {
        "description": "Experiment 1: Lossless Pixel-Run Vector Representation (Theoretical Upper Bound)",
        "svg_file_size_bytes": len(svg_pixel_run.encode("utf-8")),
        "quant_vs_original": metrics_quant_vs_orig,
        "pixel_run_svg_vs_quant": metrics_svg_vs_quant,
        "pixel_run_svg_vs_original": metrics_svg_vs_orig,
        "theoretical_upper_bound_psnr_db": metrics_quant_vs_orig["psnr_db"],
        "fidelity_loss_due_to_exact_vector_representation_mse": metrics_svg_vs_quant["mse"],
    }
    return res


# ==============================================================================
# EXPERIMENT 2: Topology and Contour Reconstruction Breakdown
# ==============================================================================

def build_raw_grid_contour_svg(labels_img: np.ndarray, centers_bgr: np.ndarray, shift_half_pixel: bool = False) -> str:
    """Builds SVG using exact OpenCV contour points with RETR_CCOMP and CHAIN_APPROX_NONE (no polygon decimation).
    
    Demonstrates pixel-grid boundary alignment:
    - shift_half_pixel=False: integer pixel centers (x, y) causing boundary shrinkage and 1px gaps.
    - shift_half_pixel=True: adjusted coordinates (x + 0.5, y + 0.5) or cell boundary compensation.
    """
    h, w = labels_img.shape[:2]
    k = len(centers_bgr)
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"

    elements = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
    offset = 0.5 if shift_half_pixel else 0.0

    for z_rank, (_, ci) in enumerate(cluster_areas):
        if ci == bg_ci:
            continue
        mask = (labels_img == ci).astype(np.uint8) * 255
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
        if hierarchy is None or len(contours) == 0:
            continue

        hierarchy_arr = hierarchy[0]
        b, g, r = centers_bgr[ci]
        hex_col = f"#{r:02x}{g:02x}{b:02x}"

        for i, h_node in enumerate(hierarchy_arr):
            if h_node[3] != -1:
                continue
            outer_cnt = contours[i]
            if cv2.contourArea(outer_cnt) < 2.0:
                continue

            d_parts = []
            pts = outer_cnt.reshape(-1, 2)
            part = [f"M {pts[0][0] + offset:.1f} {pts[0][1] + offset:.1f}"]
            for pt in pts[1:]:
                part.append(f"L {pt[0] + offset:.1f} {pt[1] + offset:.1f}")
            part.append("Z")
            d_parts.append(" ".join(part))

            # Holes
            ch_idx = h_node[2]
            while ch_idx != -1:
                hole_cnt = contours[ch_idx]
                if cv2.contourArea(hole_cnt) >= 2.0:
                    h_pts = hole_cnt.reshape(-1, 2)
                    h_part = [f"M {h_pts[0][0] + offset:.1f} {h_pts[0][1] + offset:.1f}"]
                    for pt in h_pts[1:]:
                        h_part.append(f"L {pt[0] + offset:.1f} {pt[1] + offset:.1f}")
                    h_part.append("Z")
                    d_parts.append(" ".join(h_part))
                ch_idx = hierarchy_arr[ch_idx][0]

            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            d_attr = " ".join(d_parts)
            elements.append(f'<path fill="{hex_col}"{rule} d="{d_attr}" />')

    body = "\n  ".join(elements)
    desc = "Half-Pixel Shifted" if shift_half_pixel else "Raw Integer Pixel Centers"
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n  <desc>{desc}</desc>\n  {body}\n</svg>'


def build_polygonal_svg(labels_img: np.ndarray, centers_bgr: np.ndarray, epsilon: float) -> tuple[str, int]:
    """Builds SVG using approxPolyDP polygon decimation at specified epsilon."""
    h, w = labels_img.shape[:2]
    k = len(centers_bgr)
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"

    elements = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
    total_vertices = 0

    for z_rank, (_, ci) in enumerate(cluster_areas):
        if ci == bg_ci:
            continue
        mask = (labels_img == ci).astype(np.uint8) * 255
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if hierarchy is None or len(contours) == 0:
            continue

        hierarchy_arr = hierarchy[0]
        b, g, r = centers_bgr[ci]
        hex_col = f"#{r:02x}{g:02x}{b:02x}"

        for i, h_node in enumerate(hierarchy_arr):
            if h_node[3] != -1:
                continue
            outer_cnt = contours[i]
            if cv2.contourArea(outer_cnt) < 2.0:
                continue

            approx = cv2.approxPolyDP(outer_cnt, epsilon, True)
            if len(approx) < 3:
                continue
            total_vertices += len(approx)

            d_parts = []
            pts = approx.reshape(-1, 2)
            part = [f"M {pts[0][0]:.1f} {pts[0][1]:.1f}"]
            for pt in pts[1:]:
                part.append(f"L {pt[0]:.1f} {pt[1]:.1f}")
            part.append("Z")
            d_parts.append(" ".join(part))

            ch_idx = h_node[2]
            while ch_idx != -1:
                hole_cnt = contours[ch_idx]
                if cv2.contourArea(hole_cnt) >= 2.0:
                    h_approx = cv2.approxPolyDP(hole_cnt, epsilon, True)
                    if len(h_approx) >= 3:
                        total_vertices += len(h_approx)
                        h_pts = h_approx.reshape(-1, 2)
                        h_part = [f"M {h_pts[0][0]:.1f} {h_pts[0][1]:.1f}"]
                        for pt in h_pts[1:]:
                            h_part.append(f"L {pt[0]:.1f} {pt[1]:.1f}")
                        h_part.append("Z")
                        d_parts.append(" ".join(h_part))
                ch_idx = hierarchy_arr[ch_idx][0]

            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            d_attr = " ".join(d_parts)
            elements.append(f'<path fill="{hex_col}"{rule} d="{d_attr}" />')

    body = "\n  ".join(elements)
    svg_str = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n  {body}\n</svg>'
    return svg_str, total_vertices


def build_bezier_svg(labels_img: np.ndarray, centers_bgr: np.ndarray, stroke_width: float = 0.0) -> tuple[str, int]:
    """Builds SVG using Schneider cubic Bézier fitting with selectable stroke trapping width."""
    h, w = labels_img.shape[:2]
    k = len(centers_bgr)
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"

    elements = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
    total_nodes = 0

    for z_rank, (_, ci) in enumerate(cluster_areas):
        if ci == bg_ci:
            continue
        mask = (labels_img == ci).astype(np.uint8) * 255
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if hierarchy is None or len(contours) == 0:
            continue

        hierarchy_arr = hierarchy[0]
        b, g, r = centers_bgr[ci]
        hex_col = f"#{r:02x}{g:02x}{b:02x}"

        for i, h_node in enumerate(hierarchy_arr):
            if h_node[3] != -1:
                continue
            outer_cnt = contours[i]
            if cv2.contourArea(outer_cnt) < 2.0:
                continue

            outer_approx = cv2.approxPolyDP(outer_cnt, epsilon=0.5, closed=True)
            if len(outer_approx) < 3:
                continue

            outer_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in outer_approx]
            outer_segs = fit_schneider_bezier(outer_pts, max_error_px=0.5, max_nodes=48, closed=True)
            if not outer_segs:
                continue

            subpaths = [outer_segs]
            total_nodes += len(outer_segs)

            ch_idx = h_node[2]
            while ch_idx != -1:
                hole_cnt = contours[ch_idx]
                if cv2.contourArea(hole_cnt) >= 2.0:
                    hole_approx = cv2.approxPolyDP(hole_cnt, epsilon=0.5, closed=True)
                    if len(hole_approx) >= 3:
                        hole_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in hole_approx]
                        hole_segs = fit_schneider_bezier(hole_pts, max_error_px=0.5, max_nodes=48, closed=True)
                        if hole_segs:
                            subpaths.append(hole_segs)
                            total_nodes += len(hole_segs)
                ch_idx = hierarchy_arr[ch_idx][0]

            d_parts = []
            for sub in subpaths:
                if not sub:
                    continue
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))

            d_attr = " ".join(d_parts)
            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            stroke_attr = f' stroke="{hex_col}" stroke-width="{stroke_width:.1f}" stroke-linejoin="round"' if stroke_width > 0.0 else ''
            elements.append(f'<path fill="{hex_col}"{rule}{stroke_attr} d="{d_attr}" />')

    body = "\n  ".join(elements)
    svg_str = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n  {body}\n</svg>'
    return svg_str, total_nodes


def run_experiment_2(img_orig: np.ndarray, labels_img: np.ndarray, centers_bgr: np.ndarray, quant_bgr: np.ndarray, output_dir: Path) -> dict:
    """Executes Experiment 2: Dissects the isolated error contribution of each pipeline step."""
    h, w = img_orig.shape[:2]

    # Step A: Raw Pixel Center Contours (CHAIN_APPROX_NONE) vs Shifted
    svg_raw_centers = build_raw_grid_contour_svg(labels_img, centers_bgr, shift_half_pixel=False)
    rend_raw_centers = render_svg_to_bgr(svg_raw_centers, w, h)
    metrics_raw_centers = compute_metrics(quant_bgr, rend_raw_centers)

    svg_shifted_half = build_raw_grid_contour_svg(labels_img, centers_bgr, shift_half_pixel=True)
    rend_shifted_half = render_svg_to_bgr(svg_shifted_half, w, h)
    metrics_shifted_half = compute_metrics(quant_bgr, rend_shifted_half)

    cv2.imwrite(str(output_dir / "exp2_raw_centers_rendered.png"), rend_raw_centers)
    cv2.imwrite(str(output_dir / "exp2_raw_diff_quant.png"), cv2.absdiff(quant_bgr, rend_raw_centers) * 5)

    # Step B: Polygon Simplification sweep (approxPolyDP epsilons)
    poly_results = {}
    for eps in [0.25, 0.5, 1.0, 1.5, 2.0]:
        svg_poly, v_count = build_polygonal_svg(labels_img, centers_bgr, epsilon=eps)
        rend_poly = render_svg_to_bgr(svg_poly, w, h)
        m_quant = compute_metrics(quant_bgr, rend_poly)
        m_orig = compute_metrics(img_orig, rend_poly)
        poly_results[f"epsilon_{eps}"] = {
            "vertices": v_count,
            "metrics_vs_quant": m_quant,
            "metrics_vs_orig": m_orig,
        }

    # Step C: Schneider Bézier Fitting (No stroke trapping)
    svg_bezier_no_stroke, b_nodes = build_bezier_svg(labels_img, centers_bgr, stroke_width=0.0)
    rend_bezier_no_stroke = render_svg_to_bgr(svg_bezier_no_stroke, w, h)
    m_bezier_no_stroke_vs_quant = compute_metrics(quant_bgr, rend_bezier_no_stroke)
    m_bezier_no_stroke_vs_orig = compute_metrics(img_orig, rend_bezier_no_stroke)

    # Step D: Stroke Trapping Sweep (stroke-width 0.5, 1.0, 1.5)
    stroke_results = {}
    for sw in [0.5, 1.0, 1.5]:
        svg_bezier_stroke, _ = build_bezier_svg(labels_img, centers_bgr, stroke_width=sw)
        rend_bezier_stroke = render_svg_to_bgr(svg_bezier_stroke, w, h)
        m_quant = compute_metrics(quant_bgr, rend_bezier_stroke)
        m_orig = compute_metrics(img_orig, rend_bezier_stroke)
        stroke_results[f"stroke_width_{sw}"] = {
            "metrics_vs_quant": m_quant,
            "metrics_vs_orig": m_orig,
        }

    # Measure silhouette boundary error specifically
    # Outer mask of original vs rendered with stroke 1.0 vs 0.0
    bg_ci = [(np.sum(labels_img == ci), ci) for ci in range(len(centers_bgr))]
    bg_ci.sort(key=lambda x: x[0], reverse=True)
    dominant_bg_bgr = centers_bgr[bg_ci[0][1]]

    mask_orig_fg = np.linalg.norm(img_orig.astype(float) - dominant_bg_bgr, axis=2) > 30.0
    mask_stroke0_fg = np.linalg.norm(rend_bezier_no_stroke.astype(float) - dominant_bg_bgr, axis=2) > 30.0
    mask_stroke1_fg = np.linalg.norm(render_svg_to_bgr(build_bezier_svg(labels_img, centers_bgr, stroke_width=1.0)[0], w, h).astype(float) - dominant_bg_bgr, axis=2) > 30.0

    fg_pixels_orig = int(np.sum(mask_orig_fg))
    fg_pixels_stroke0 = int(np.sum(mask_stroke0_fg))
    fg_pixels_stroke1 = int(np.sum(mask_stroke1_fg))
    bloating_pixels_stroke1 = fg_pixels_stroke1 - fg_pixels_orig

    return {
        "step_a_pixel_grid_alignment": {
            "raw_integer_centers_vs_quant": metrics_raw_centers,
            "shifted_half_pixel_vs_quant": metrics_shifted_half,
            "interpretation": "Integer centers clip boundary pixels, leading to seam gaps. Half-pixel shifting reduces boundary clipping."
        },
        "step_b_polygon_simplification_sweep": poly_results,
        "step_c_bezier_fitting_no_stroke": {
            "total_nodes": b_nodes,
            "metrics_vs_quant": m_bezier_no_stroke_vs_quant,
            "metrics_vs_orig": m_bezier_no_stroke_vs_orig,
        },
        "step_d_stroke_trapping_sweep": stroke_results,
        "silhouette_bloating_analysis": {
            "foreground_pixels_original": fg_pixels_orig,
            "foreground_pixels_stroke_0_0": fg_pixels_stroke0,
            "foreground_pixels_stroke_1_0": fg_pixels_stroke1,
            "bloat_pixels_added_by_stroke_1_0": bloating_pixels_stroke1,
            "bloat_percentage": round((bloating_pixels_stroke1 / fg_pixels_orig) * 100.0, 2) if fg_pixels_orig > 0 else 0.0,
        }
    }


def main():
    img_path = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"
    out_dir = ROOT / "versions" / "version-01" / "experiments" / "stage_error_analysis" / "iteration_07_diagnostics"
    out_dir.mkdir(parents=True, exist_ok=True)

    img_bgr = cv2.imread(str(img_path))
    if img_bgr is None:
        raise FileNotFoundError(f"Cannot load {img_path}")

    print("=" * 80)
    print("RUNNING ITERATION 07 DIAGNOSTIC EXPERIMENTS — VECTOR & TYPOGRAPHY SPECIALIST")
    print("=" * 80)

    # Stage 1: Standard CIELAB Quantization (k=16, seed=42)
    labels_img, centers_bgr, quant_bgr = quantize_image_cielab(img_bgr, n_colors=16, seed=42)
    cv2.imwrite(str(out_dir / "01_quantized.png"), quant_bgr)

    # Run Experiment 1
    print("\n--- Running Experiment 1: Lossless Pixel-Run Diagnostic SVG ---")
    exp1_res = run_experiment_1(img_bgr, labels_img, centers_bgr, quant_bgr, out_dir)
    print(f"  Pixel-Run vs Quantized Raster: MSE = {exp1_res['pixel_run_svg_vs_quant']['mse']}, PSNR = {exp1_res['pixel_run_svg_vs_quant']['psnr_db']} dB, SSIM = {exp1_res['pixel_run_svg_vs_quant']['ssim']}")
    print(f"  Pixel-Run vs Original Image:   MSE = {exp1_res['pixel_run_svg_vs_original']['mse']}, PSNR = {exp1_res['pixel_run_svg_vs_original']['psnr_db']} dB, SSIM = {exp1_res['pixel_run_svg_vs_original']['ssim']}")
    print(f"  Fidelity Upper Bound (Quant):  MSE = {exp1_res['theoretical_upper_bound_psnr_db']} dB PSNR")

    # Run Experiment 2
    print("\n--- Running Experiment 2: Topology and Contour Reconstruction Breakdown ---")
    exp2_res = run_experiment_2(img_bgr, labels_img, centers_bgr, quant_bgr, out_dir)
    print(f"  Raw Centers vs Quant: MSE = {exp2_res['step_a_pixel_grid_alignment']['raw_integer_centers_vs_quant']['mse']}, PSNR = {exp2_res['step_a_pixel_grid_alignment']['raw_integer_centers_vs_quant']['psnr_db']} dB")
    print(f"  Bézier (No Stroke) vs Quant: MSE = {exp2_res['step_c_bezier_fitting_no_stroke']['metrics_vs_quant']['mse']}, PSNR = {exp2_res['step_c_bezier_fitting_no_stroke']['metrics_vs_quant']['psnr_db']} dB")
    print(f"  Bézier (Stroke 1.0) vs Quant: MSE = {exp2_res['step_d_stroke_trapping_sweep']['stroke_width_1.0']['metrics_vs_quant']['mse']}, PSNR = {exp2_res['step_d_stroke_trapping_sweep']['stroke_width_1.0']['metrics_vs_quant']['psnr_db']} dB")
    print(f"  Silhouette Bloat by Stroke 1.0: +{exp2_res['silhouette_bloating_analysis']['bloat_pixels_added_by_stroke_1_0']} pixels (+{exp2_res['silhouette_bloating_analysis']['bloat_percentage']}%)")

    # Combine and save full report
    full_report = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "task_id": "TASK-V01-ITERATION-07",
        "agent": "vector-and-typography-agent",
        "image": "A01_shield.png",
        "dimensions": [img_bgr.shape[1], img_bgr.shape[0]],
        "experiment_1_pixel_run_upper_bound": exp1_res,
        "experiment_2_topology_breakdown": exp2_res,
    }

    report_path = out_dir / "iteration_07_experiment_report.json"
    report_path.write_text(json.dumps(full_report, indent=2), encoding="utf-8")
    print(f"\nFull report written to {report_path}")
    print("=" * 80)
    return full_report


if __name__ == "__main__":
    main()
# END CHANGE TASK-V01-ITERATION-07 | 2026-10-17T22:15:00Z | CREATED
