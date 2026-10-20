#!/usr/bin/env python3
"""Synthetic Illumination and Appearance Benchmark for Version 01.

Work Package 1 (TASK-V01-FINAL-GEOMETRY-INVESTIGATION):
Isolates appearance/illumination reconstruction from semantic boundary extraction using
100% known ground-truth geometry (256x256 test cards).
Evaluates Method A (K-Means solid fragments), Method B (True SVG gradients), and
Method C (Layered base + highlight/shadow vector decomposition).
"""
import math
import json
from pathlib import Path
import cv2
import numpy as np
import pymupdf
from skimage.metrics import structural_similarity as ssim

OUT_DIR = Path(__file__).resolve().parent

# START CHANGE TASK-V01-FINAL-GEOMETRY-INVESTIGATION | 2026-10-17T20:05:00Z | EDITED | Author: performance-optimization-specialist
def compute_illumination_metrics(ref: np.ndarray, test: np.ndarray) -> dict:
    diff = ref.astype(np.float64) - test.astype(np.float64)
    mse = float(np.mean(diff ** 2))
    rmse = float(np.sqrt(mse))
    psnr = float(99.99 if mse < 1e-10 else 10.0 * np.log10((255.0 ** 2) / mse))
    ssim_val = float(ssim(ref, test, channel_axis=2, data_range=255.0))
    return {
        "mse": round(mse, 2),
        "rmse": round(rmse, 2),
        "psnr": round(psnr, 2),
        "ssim": round(ssim_val, 4)
    }
# END CHANGE TASK-V01-FINAL-GEOMETRY-INVESTIGATION | 2026-10-17T20:05:00Z | EDITED

# -------------------------------------------------------------
# 1. GROUND TRUTH GENERATION (256x256)
# Center (128, 128), Radius R = 80
# -------------------------------------------------------------
W, H = 256, 256
CX, CY, R = 128.0, 128.0, 80.0

def make_ground_truth_images():
    Y, X = np.ogrid[:H, :W]
    dist_sq = (X - CX)**2 + (Y - CY)**2
    dist = np.sqrt(dist_sq)
    
    # Smooth 1px anti-aliased edge mask for raster rendering
    edge_width = 1.0
    fg_mask = np.clip(0.5 - (dist - R) / edge_width, 0.0, 1.0)
    
    # --- S01: Flat Red ---
    bg_s01 = np.full((H, W, 3), 240, dtype=np.uint8) # BGR
    fg_s01 = np.zeros((H, W, 3), dtype=np.uint8)
    fg_s01[:] = [32, 32, 230] # BGR for #e62020
    s01 = (bg_s01 * (1.0 - fg_mask[:, :, None]) + fg_s01 * fg_mask[:, :, None]).astype(np.uint8)
    cv2.imwrite(str(OUT_DIR / "S01_flat_red.png"), s01)

    # --- S02: Smooth Red Sphere (Phong 3D Shading) ---
    s02_float = np.full((H, W, 3), 240.0, dtype=np.float64)
    inside = dist <= R
    Z = np.zeros((H, W), dtype=np.float64)
    Z[inside] = np.sqrt(np.maximum(0.0, R**2 - dist_sq[inside]))
    
    # Light direction: (-0.45, -0.55, 0.70)
    lx, ly, lz = -0.45, -0.55, 0.70
    l_len = math.hypot(lx, ly, lz)
    lx, ly, lz = lx/l_len, ly/l_len, lz/l_len
    
    Nx = (X - CX) / R
    Ny = (Y - CY) / R
    Nz = Z / R
    
    NdotL = np.maximum(0.0, Nx * lx + Ny * ly + Nz * lz)
    
    hx, hy, hz = lx, ly, lz + 1.0
    h_len = math.hypot(hx, hy, hz)
    hx, hy, hz = hx/h_len, hy/h_len, hz/h_len
    NdotH = np.maximum(0.0, Nx * hx + Ny * hy + Nz * hz)
    spec = (NdotH ** 24) * 0.85
    
    ambient = 0.20
    intensity = np.clip(ambient + 0.80 * NdotL, 0.0, 1.0)
    
    sphere_b = np.clip(25.0 * intensity + 255.0 * spec, 0, 255)
    sphere_g = np.clip(20.0 * intensity + 255.0 * spec, 0, 255)
    sphere_r = np.clip(210.0 * intensity + 255.0 * spec, 0, 255)
    sphere_bgr = np.stack([sphere_b, sphere_g, sphere_r], axis=2)
    
    s02 = (s02_float * (1.0 - fg_mask[:, :, None]) + sphere_bgr * fg_mask[:, :, None]).astype(np.uint8)
    cv2.imwrite(str(OUT_DIR / "S02_smooth_red_sphere.png"), s02)

    # --- S03: Metallic Gold with Specular Sheen (Angle 135 deg) ---
    s03_float = np.full((H, W, 3), 240.0, dtype=np.float64)
    u_diag = ((X - CX) * (-0.7071) + (Y - CY) * (-0.7071)) / R # in [-1, 1]
    t = (u_diag + 1.0) / 2.0 # [0, 1]
    t = np.clip(t, 0.0, 1.0)
    
    b_chan = 24.0 + 80.0 * np.sin(t * np.pi) + 140.0 * np.exp(-((t - 0.65)**2) / 0.015)
    g_chan = 64.0 + 130.0 * np.sin(t * np.pi) + 80.0 * np.exp(-((t - 0.65)**2) / 0.015)
    r_chan = 92.0 + 135.0 * np.sin(t * np.pi) + 30.0 * np.exp(-((t - 0.65)**2) / 0.015)
    gold_bgr = np.stack([np.clip(b_chan, 0, 255), np.clip(g_chan, 0, 255), np.clip(r_chan, 0, 255)], axis=2)
    
    s03 = (s03_float * (1.0 - fg_mask[:, :, None]) + gold_bgr * fg_mask[:, :, None]).astype(np.uint8)
    cv2.imwrite(str(OUT_DIR / "S03_metallic_gold.png"), s03)

    # --- S04: Transparency over High-Contrast Checkerboard ---
    grid_size = 16
    check = ((X // grid_size) + (Y // grid_size)) % 2
    # In raster: check==0 is White (255, 255, 255), check==1 is Gray (96, 96, 96)
    bg_s04 = np.where(check[:, :, None] == 0, [255, 255, 255], [96, 96, 96]).astype(np.float64) # BGR
    
    alpha_disk = np.clip(0.70 - 0.35 * (dist / R), 0.35, 0.70)
    glass_bgr = np.full((H, W, 3), [220.0, 180.0, 20.0], dtype=np.float64) # Cyan tint
    rim = np.exp(-((dist - (R - 2.0))**2) / 4.0) * 0.40
    glass_bgr = glass_bgr * (1.0 - rim[:, :, None]) + np.array([255.0, 255.0, 255.0]) * rim[:, :, None]
    
    comp_glass = bg_s04 * (1.0 - alpha_disk[:, :, None]) + glass_bgr * alpha_disk[:, :, None]
    s04 = (bg_s04 * (1.0 - fg_mask[:, :, None]) + comp_glass * fg_mask[:, :, None]).astype(np.uint8)
    cv2.imwrite(str(OUT_DIR / "S04_transparency.png"), s04)
    print("Ground truth images generated.")

# -------------------------------------------------------------
# 2. REPRESENTATION METHODS A, B, C IMPLEMENTATION
# -------------------------------------------------------------

def run_method_a_kmeans_pipeline(img_bgr: np.ndarray, bg_hex: str = "#f0f0f0") -> str:
    """Method A: Classical K-Means (K=16) color quantization into flat-shaded vector fragments (Current Version 01)."""
    h, w = img_bgr.shape[:2]
    smooth = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=25, sigmaSpace=10)
    lab = cv2.cvtColor(smooth, cv2.COLOR_BGR2LAB)
    pixels = np.float32(lab.reshape(-1, 3))
    
    cv2.setRNGSeed(42)
    np.random.seed(42)
    k = 16
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 1, cv2.KMEANS_PP_CENTERS)
    
    labels_img = labels.reshape((h, w)).astype(np.uint8)
    centers_lab = np.uint8(centers.reshape((1, k, 3)))
    centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((k, 3))
    
    cluster_areas = [(int(np.sum(labels_img == ci)), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    
    elements = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
    for z_rank, (_, ci) in enumerate(cluster_areas):
        if ci == bg_ci:
            continue
        b, g, r = int(centers_bgr[ci][0]), int(centers_bgr[ci][1]), int(centers_bgr[ci][2])
        hex_col = f"#{r:02x}{g:02x}{b:02x}"
        mask = (labels_img == ci).astype(np.uint8) * 255
        
        cnts, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if hier is None or len(cnts) == 0:
            continue
        h_arr = hier[0]
        for i, h_node in enumerate(h_arr):
            if h_node[3] != -1:
                continue
            outer = cnts[i]
            if len(outer) < 3 or cv2.contourArea(outer) < 2.0:
                continue
            approx = cv2.approxPolyDP(outer, epsilon=0.6, closed=True)
            if len(approx) < 3:
                continue
            
            d_parts = ["M " + " L ".join(f"{p[0][0]:.2f} {p[0][1]:.2f}" for p in approx) + " Z"]
            ch = h_node[2]
            while ch != -1:
                hole = cnts[ch]
                if len(hole) >= 3 and cv2.contourArea(hole) >= 2.0:
                    h_approx = cv2.approxPolyDP(hole, epsilon=0.6, closed=True)
                    if len(h_approx) >= 3:
                        d_parts.append("M " + " L ".join(f"{p[0][0]:.2f} {p[0][1]:.2f}" for p in h_approx) + " Z")
                ch = h_arr[ch][0]
                
            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            stroke_attr = f' stroke="{hex_col}" stroke-width="0.75" stroke-linejoin="round"'
            elements.append(f'<path fill="{hex_col}"{rule}{stroke_attr} d="{" ".join(d_parts)}" />')
            
    body = "\n  ".join(elements)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
        f'  <desc>Method A: K-Means Solid Fragments</desc>\n'
        f'  {body}\n'
        f'</svg>'
    )

def build_svg_checkerboard_rects(w: int, h: int, grid: int = 16) -> str:
    """Build exact checkerboard using pure SVG rect elements rendered 100% by PyMuPDF."""
    rects = [f'<rect width="{w}" height="{h}" fill="#ffffff" />']
    for gy in range(0, h, grid):
        for gx in range(0, w, grid):
            if ((gx // grid) + (gy // grid)) % 2 == 1:
                rects.append(f'<rect x="{gx}" y="{gy}" width="{grid}" height="{grid}" fill="#606060" />')
    return "\n    ".join(rects)

def make_method_b_svg(asset_id: str) -> str:
    """Method B: Unified Ground-Truth Boundary filled with true SVG Linear or Radial Gradient."""
    w, h = W, H
    cx, cy, r = CX, CY, R
    
    if asset_id == "S01":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="#e62020" />\n'
            f'</svg>'
        )
    elif asset_id == "S02":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <defs>\n'
            f'    <radialGradient id="sphereGrad" cx="50%" cy="50%" r="50%" fx="37.5%" fy="35%">\n'
            f'      <stop offset="0%" stop-color="#ffebf0" />\n'
            f'      <stop offset="10%" stop-color="#ffced3" />\n'
            f'      <stop offset="25%" stop-color="#ff7478" />\n'
            f'      <stop offset="48%" stop-color="#9e181c" />\n'
            f'      <stop offset="70%" stop-color="#6b0a0c" />\n'
            f'      <stop offset="90%" stop-color="#370506" />\n'
            f'      <stop offset="100%" stop-color="#2a0405" />\n'
            f'    </radialGradient>\n'
            f'  </defs>\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#sphereGrad)" />\n'
            f'</svg>'
        )
    elif asset_id == "S03":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <defs>\n'
            f'    <linearGradient id="goldGrad" x1="184.6" y1="184.6" x2="71.4" y2="71.4" gradientUnits="userSpaceOnUse">\n'
            f'      <stop offset="0%" stop-color="#5c4018" />\n'
            f'      <stop offset="15%" stop-color="#997b3c" />\n'
            f'      <stop offset="35%" stop-color="#d4b460" />\n'
            f'      <stop offset="50%" stop-color="#ead487" />\n'
            f'      <stop offset="60%" stop-color="#f6ffdb" />\n'
            f'      <stop offset="65%" stop-color="#f2ffeb" />\n'
            f'      <stop offset="70%" stop-color="#e3edcf" />\n'
            f'      <stop offset="85%" stop-color="#9b8146" />\n'
            f'      <stop offset="100%" stop-color="#5c4018" />\n'
            f'    </linearGradient>\n'
            f'  </defs>\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#goldGrad)" />\n'
            f'</svg>'
        )
    elif asset_id == "S04":
        cb = build_svg_checkerboard_rects(w, h, 16)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <defs>\n'
            f'    <radialGradient id="glassGrad" cx="50%" cy="50%" r="50%">\n'
            f'      <stop offset="0%" stop-color="#14b4dc" stop-opacity="0.70" />\n'
            f'      <stop offset="65%" stop-color="#14b4dc" stop-opacity="0.48" />\n'
            f'      <stop offset="92%" stop-color="#ffffff" stop-opacity="0.65" />\n'
            f'      <stop offset="100%" stop-color="#14b4dc" stop-opacity="0.35" />\n'
            f'    </radialGradient>\n'
            f'  </defs>\n'
            f'  <g id="Checkerboard">\n    {cb}\n  </g>\n'
            f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#glassGrad)" />\n'
            f'</svg>'
        )
    raise ValueError(f"Unknown asset_id {asset_id}")

def make_method_c_svg(asset_id: str) -> str:
    """Method C: Layered Base Shape + Independent Vector Layers for Highlight, Midtone, and Shadow."""
    w, h = W, H
    cx, cy, r = CX, CY, R
    
    if asset_id == "S01":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <g id="FlatRedCircle">\n'
            f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#e62020" />\n'
            f'  </g>\n'
            f'</svg>'
        )
    elif asset_id == "S02":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <defs>\n'
            f'    <clipPath id="circleClip">\n'
            f'      <circle cx="{cx}" cy="{cy}" r="{r}" />\n'
            f'    </clipPath>\n'
            f'  </defs>\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <g id="SphereGroup" clip-path="url(#circleClip)">\n'
            f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#9e181c" />\n'
            f'    <circle cx="155" cy="155" r="75" fill="#2a0405" opacity="0.75" />\n'
            f'    <ellipse cx="115" cy="110" rx="55" ry="50" fill="#e63236" opacity="0.80" />\n'
            f'    <ellipse cx="108" cy="104" rx="28" ry="24" fill="#ffced3" opacity="0.85" />\n'
            f'    <ellipse cx="108" cy="104" rx="12" ry="10" fill="#ffffff" opacity="0.95" />\n'
            f'  </g>\n'
            f'</svg>'
        )
    elif asset_id == "S03":
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <defs>\n'
            f'    <clipPath id="goldClip">\n'
            f'      <circle cx="{cx}" cy="{cy}" r="{r}" />\n'
            f'    </clipPath>\n'
            f'  </defs>\n'
            f'  <rect width="{w}" height="{h}" fill="#f0f0f0" />\n'
            f'  <g id="MetallicGoldGroup" clip-path="url(#goldClip)">\n'
            f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#5c4018" />\n'
            f'    <rect x="25" y="25" width="190" height="190" transform="rotate(-45 128 128)" fill="#d4b460" />\n'
            f'    <rect x="70" y="80" width="115" height="42" transform="rotate(-45 128 128)" fill="#ead487" opacity="0.85" />\n'
            f'    <rect x="88" y="94" width="80" height="16" transform="rotate(-45 128 128)" fill="#f2ffeb" opacity="0.92" />\n'
            f'    <ellipse cx="165" cy="165" rx="50" ry="32" fill="#5c4018" opacity="0.70" />\n'
            f'  </g>\n'
            f'</svg>'
        )
    elif asset_id == "S04":
        cb = build_svg_checkerboard_rects(w, h, 16)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
            f'  <g id="Checkerboard">\n    {cb}\n  </g>\n'
            f'  <g id="GlassGroup">\n'
            f'    <circle cx="{cx}" cy="{cy}" r="{r}" fill="#14b4dc" fill-opacity="0.48" />\n'
            f'    <circle cx="{cx}" cy="{cy}" r="45" fill="#14b4dc" fill-opacity="0.22" />\n'
            f'    <circle cx="{cx}" cy="{cy}" r="78.5" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-opacity="0.65" />\n'
            f'  </g>\n'
            f'</svg>'
        )
    raise ValueError(f"Unknown asset_id {asset_id}")

# START CHANGE TASK-V01-FINAL-GEOMETRY-INVESTIGATION | 2026-10-17T20:06:00Z | EDITED | Author: performance-optimization-specialist
def render_illumination_svg_to_bgr(svg_str: str) -> np.ndarray:
    doc = pymupdf.open(stream=svg_str.encode('utf-8'), filetype='svg')
    pix = doc[0].get_pixmap()
    rgb = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
    if pix.n == 4:
        return cv2.cvtColor(rgb, cv2.COLOR_RGBA2BGR)
    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
# END CHANGE TASK-V01-FINAL-GEOMETRY-INVESTIGATION | 2026-10-17T20:06:00Z | EDITED

# -------------------------------------------------------------
# 3. BENCHMARK EXECUTION & TELEMETRY
# -------------------------------------------------------------

def run_benchmark():
    make_ground_truth_images()
    
    assets = [
        ("S01", "S01_flat_red.png", "#f0f0f0"),
        ("S02", "S02_smooth_red_sphere.png", "#f0f0f0"),
        ("S03", "S03_metallic_gold.png", "#f0f0f0"),
        ("S04", "S04_transparency.png", None),
    ]
    
    results = []
    
    for aid, fname, bg_col in assets:
        gt_img = cv2.imread(str(OUT_DIR / fname))
        
        # Method A
        svg_a = run_method_a_kmeans_pipeline(gt_img, bg_hex=bg_col if bg_col else "#ffffff")
        (OUT_DIR / f"{aid}_method_A.svg").write_text(svg_a, encoding="utf-8")
        rend_a = render_illumination_svg_to_bgr(svg_a)
        cv2.imwrite(str(OUT_DIR / f"{aid}_method_A_rendered.png"), rend_a)
        m_a = compute_illumination_metrics(gt_img, rend_a)
        
        # Method B
        svg_b = make_method_b_svg(aid)
        (OUT_DIR / f"{aid}_method_B.svg").write_text(svg_b, encoding="utf-8")
        rend_b = render_illumination_svg_to_bgr(svg_b)
        cv2.imwrite(str(OUT_DIR / f"{aid}_method_B_rendered.png"), rend_b)
        m_b = compute_illumination_metrics(gt_img, rend_b)
        
        # Method C
        svg_c = make_method_c_svg(aid)
        (OUT_DIR / f"{aid}_method_C.svg").write_text(svg_c, encoding="utf-8")
        rend_c = render_illumination_svg_to_bgr(svg_c)
        cv2.imwrite(str(OUT_DIR / f"{aid}_method_C_rendered.png"), rend_c)
        m_c = compute_illumination_metrics(gt_img, rend_c)
        
        import re
        cnt_a = len(re.findall(r'<path\b', svg_a))
        cnt_b = len(re.findall(r'<(path|circle)\b', svg_b))
        cnt_c = len(re.findall(r'<(path|circle|rect|ellipse)\b', svg_c))
        
        entry = {
            "asset_id": aid,
            "filename": fname,
            "method_A_kmeans_solid_fragments": {
                "paths": cnt_a,
                "svg_bytes": len(svg_a.encode('utf-8')),
                "metrics": m_a
            },
            "method_B_true_svg_gradient": {
                "paths": cnt_b,
                "svg_bytes": len(svg_b.encode('utf-8')),
                "metrics": m_b
            },
            "method_C_layered_base_plus_light_shadow": {
                "paths": cnt_c,
                "svg_bytes": len(svg_c.encode('utf-8')),
                "metrics": m_c
            }
        }
        results.append(entry)
        
    res_path = OUT_DIR / "synthetic_benchmark_results.json"
    with open(res_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
        
    print("Benchmark complete. Results saved to:", res_path)
    return results

if __name__ == "__main__":
    res = run_benchmark()
    print(json.dumps(res, indent=2))
