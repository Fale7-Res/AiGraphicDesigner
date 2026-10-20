#!/usr/bin/env python3
"""Stage-by-stage visual error decomposition for Version 01.

Decomposes and quantifies visual error introduced at each discrete processing stage:
1. Stage 1: Color Quantization (CIELAB K-Means)
2. Stage 2: Polygon Approximation (approxPolyDP)
3. Stage 3: Bézier Curve Fitting (Cubic Bézier segments)
4. Stage 4: Compositing & Rendering (Stroke trapping + Background + SVG rendering)
"""
from pathlib import Path
import json
import math
import sys
import cv2
import numpy as np

# Add repository root and version-01 directory to path
ROOT = Path(__file__).resolve().parents[4]
VERSION_01_DIR = ROOT / "versions" / "version-01"
sys.path.insert(0, str(VERSION_01_DIR))
sys.path.insert(0, str(ROOT))

from src.geometry.bezier import Point2D, fit_schneider_bezier
from src.pipeline import SequentialPipeline, VectorLayer


def compute_metrics(img_ref: np.ndarray, img_test: np.ndarray) -> dict[str, float]:
    """Compute MSE, RMSE, PSNR, and SSIM between reference and test RGB/BGR images."""
    if img_ref.shape != img_test.shape:
        img_test = cv2.resize(img_test, (img_ref.shape[1], img_ref.shape[0]))

    diff = img_ref.astype(np.float64) - img_test.astype(np.float64)
    mse = float(np.mean(diff ** 2))
    rmse = float(math.sqrt(mse))
    psnr = float(10.0 * math.log10((255.0 ** 2) / mse)) if mse > 1e-10 else 99.0

    # Simplified fast SSIM on luminance channel
    gray_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2GRAY).astype(np.float64)
    gray_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2GRAY).astype(np.float64)

    mu_x = cv2.GaussianBlur(gray_ref, (11, 11), 1.5)
    mu_y = cv2.GaussianBlur(gray_test, (11, 11), 1.5)
    mu_x_sq = mu_x ** 2
    mu_y_sq = mu_y ** 2
    mu_xy = mu_x * mu_y

    sigma_x_sq = cv2.GaussianBlur(gray_ref ** 2, (11, 11), 1.5) - mu_x_sq
    sigma_y_sq = cv2.GaussianBlur(gray_test ** 2, (11, 11), 1.5) - mu_y_sq
    sigma_xy = cv2.GaussianBlur(gray_ref * gray_test, (11, 11), 1.5) - mu_xy

    c1 = (0.01 * 255.0) ** 2
    c2 = (0.03 * 255.0) ** 2

    ssim_map = ((2.0 * mu_xy + c1) * (2.0 * sigma_xy + c2)) / ((mu_x_sq + mu_y_sq + c1) * (sigma_x_sq + sigma_y_sq + c2))
    ssim = float(np.mean(ssim_map))

    return {
        "mse": round(mse, 2),
        "rmse": round(rmse, 2),
        "psnr_db": round(psnr, 2),
        "ssim": round(ssim, 4),
    }


def analyze_image(image_path: Path, output_dir: Path, n_colors: int = 24, seed: int = 42):
    """Run stage-by-stage analysis on a single image and save artifacts."""
    output_dir.mkdir(parents=True, exist_ok=True)
    img_orig = cv2.imread(str(image_path))
    if img_orig is None:
        raise FileNotFoundError(f"Cannot read: {image_path}")

    h, w = img_orig.shape[:2]
    cv2.imwrite(str(output_dir / "00_original.png"), img_orig)

    # -------------------------------------------------------------
    # STAGE 1: Color Quantization in CIELAB
    # -------------------------------------------------------------
    smooth_bgr = cv2.bilateralFilter(img_orig, d=5, sigmaColor=25, sigmaSpace=10)
    img_lab = cv2.cvtColor(smooth_bgr, cv2.COLOR_BGR2LAB)
    pixels = np.float32(img_lab.reshape(-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
    cv2.setRNGSeed(seed)
    _, labels, centers = cv2.kmeans(pixels, n_colors, None, criteria, 5, cv2.KMEANS_PP_CENTERS)
    labels_img = labels.reshape((h, w)).astype(np.uint8)

    centers_lab = np.uint8(centers.reshape((1, n_colors, 3)))
    centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((n_colors, 3))

    quant_bgr = np.zeros_like(img_orig)
    for ci in range(n_colors):
        quant_bgr[labels_img == ci] = centers_bgr[ci]

    cv2.imwrite(str(output_dir / "01_quantized.png"), quant_bgr)
    metrics_s1 = compute_metrics(img_orig, quant_bgr)

    # Absolute diff visualization Stage 1
    diff_s1 = cv2.absdiff(img_orig, quant_bgr)
    cv2.imwrite(str(output_dir / "01_diff_quant.png"), diff_s1 * 3)

    # -------------------------------------------------------------
    # STAGE 2: Polygon Approximation
    # -------------------------------------------------------------
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(n_colors)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]

    poly_raster = np.zeros_like(img_orig)
    poly_raster[:] = centers_bgr[bg_ci]

    all_polys_by_layer = []
    total_poly_vertices = 0

    for z_rank, (_, ci) in enumerate(cluster_areas):
        mask = np.uint8(labels_img == ci) * 255
        if np.sum(mask) == 0:
            continue
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if hierarchy is None or len(contours) == 0:
            continue

        hierarchy_arr = hierarchy[0]
        layer_polys = []

        for i, h_node in enumerate(hierarchy_arr):
            # Outer contours only
            if h_node[3] != -1:
                continue
            cnt = contours[i]
            if cv2.contourArea(cnt) < 1.0:
                continue

            epsilon = max(0.5, 0.003 * cv2.arcLength(cnt, True))
            poly_outer = cv2.approxPolyDP(cnt, epsilon, True)
            total_poly_vertices += len(poly_outer)

            holes = []
            ch_idx = h_node[2]
            while ch_idx != -1:
                hole_cnt = contours[ch_idx]
                if cv2.contourArea(hole_cnt) >= 1.0:
                    hole_eps = max(0.5, 0.003 * cv2.arcLength(hole_cnt, True))
                    poly_hole = cv2.approxPolyDP(hole_cnt, hole_eps, True)
                    holes.append(poly_hole)
                    total_poly_vertices += len(poly_hole)
                ch_idx = hierarchy_arr[ch_idx][0]

            layer_polys.append((poly_outer, holes, centers_bgr[ci]))

            # Render onto poly_raster using evenodd / stencil logic
            cv2.drawContours(poly_raster, [poly_outer], -1, tuple(int(c) for c in centers_bgr[ci]), thickness=cv2.FILLED)
            for h_poly in holes:
                # Fill hole with background or underlying color
                cv2.drawContours(poly_raster, [h_poly], -1, tuple(int(c) for c in centers_bgr[bg_ci]), thickness=cv2.FILLED)

        all_polys_by_layer.append(layer_polys)

    cv2.imwrite(str(output_dir / "02_polygon_raster.png"), poly_raster)
    metrics_s2_vs_quant = compute_metrics(quant_bgr, poly_raster)
    metrics_s2_vs_orig = compute_metrics(img_orig, poly_raster)

    diff_s2 = cv2.absdiff(img_orig, poly_raster)
    cv2.imwrite(str(output_dir / "02_diff_poly.png"), diff_s2 * 3)

    # -------------------------------------------------------------
    # STAGE 3 & 4: Bézier Curve Fitting and Full SVG Pipeline
    # -------------------------------------------------------------
    pipeline = SequentialPipeline()
    svg_output, telemetry = pipeline.process_image(image_path, n_colors=n_colors)

    svg_file = output_dir / "03_bezier_rendered.svg"
    svg_file.write_text(svg_output, encoding="utf-8")

    # Render SVG via PyMuPDF
    rendered_png = output_dir / "04_rendered_svg.png"
    try:
        import pymupdf
        doc = pymupdf.open(stream=svg_output.encode("utf-8"), filetype="svg")
        pix = doc[0].get_pixmap()
        pix.save(str(rendered_png))
        img_svg = cv2.imread(str(rendered_png))
    except Exception as e:
        print(f"Warning: pymupdf rendering error: {e}")
        img_svg = poly_raster

    metrics_s4_vs_orig = compute_metrics(img_orig, img_svg)
    metrics_s4_vs_quant = compute_metrics(quant_bgr, img_svg)
    metrics_s4_vs_poly = compute_metrics(poly_raster, img_svg)

    diff_s4 = cv2.absdiff(img_orig, img_svg)
    cv2.imwrite(str(output_dir / "04_diff_svg.png"), diff_s4 * 3)

    # Stage-by-Stage Error Attribution
    total_error_mse = metrics_s4_vs_orig["mse"]
    quant_error_mse = metrics_s1["mse"]
    poly_delta_mse = max(0.0, metrics_s2_vs_orig["mse"] - quant_error_mse)
    svg_delta_mse = max(0.0, total_error_mse - metrics_s2_vs_orig["mse"])

    report = {
        "image": image_path.name,
        "dimensions": [w, h],
        "n_colors": n_colors,
        "stages": {
            "stage_1_quantization": {
                "description": "CIELAB K-Means Color Clustering",
                "metrics_vs_original": metrics_s1,
                "mse_share_pct": round((quant_error_mse / total_error_mse) * 100.0, 1) if total_error_mse > 0 else 0,
            },
            "stage_2_polygon": {
                "description": "approxPolyDP Contour Simplification",
                "total_vertices": total_poly_vertices,
                "metrics_vs_quantized": metrics_s2_vs_quant,
                "metrics_vs_original": metrics_s2_vs_orig,
                "mse_share_pct": round((poly_delta_mse / total_error_mse) * 100.0, 1) if total_error_mse > 0 else 0,
            },
            "stage_3_and_4_svg_rendering": {
                "description": "Safe Cubic Bézier + Stroke Trapping + SVG Compositing",
                "telemetry": telemetry,
                "metrics_vs_polygon": metrics_s4_vs_poly,
                "metrics_vs_quantized": metrics_s4_vs_quant,
                "metrics_vs_original": metrics_s4_vs_orig,
                "mse_share_pct": round((svg_delta_mse / total_error_mse) * 100.0, 1) if total_error_mse > 0 else 0,
            }
        },
        "summary": {
            "total_mse": total_error_mse,
            "quantization_mse": quant_error_mse,
            "polygon_incremental_mse": round(poly_delta_mse, 2),
            "curve_and_render_incremental_mse": round(svg_delta_mse, 2),
            "final_psnr_db": metrics_s4_vs_orig["psnr_db"],
            "final_ssim": metrics_s4_vs_orig["ssim"],
        }
    }

    report_path = output_dir / "stage_error_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Analysis complete for {image_path.name}:")
    print(json.dumps(report["summary"], indent=2))
    return report


if __name__ == "__main__":
    test_img = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"
    out_dir = ROOT / "versions" / "version-01" / "experiments" / "stage_error_analysis" / "A01_shield"
    analyze_image(test_img, out_dir, n_colors=24, seed=42)
