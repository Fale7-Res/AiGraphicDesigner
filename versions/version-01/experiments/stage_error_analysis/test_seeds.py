#!/usr/bin/env python3
import sys
from pathlib import Path
import cv2
import numpy as np
import pymupdf
import math

ROOT = Path(__file__).resolve().parents[4]
VERSION_01_DIR = ROOT / "versions" / "version-01"
sys.path.insert(0, str(VERSION_01_DIR))

from src.geometry.bezier import Point2D, fit_schneider_bezier

def test_each_gradient():
    img_path = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"
    img_bgr = cv2.imread(str(img_path))
    h, w = img_bgr.shape[:2]
    
    cv2.setRNGSeed(0)
    np.random.seed(0)
    
    smooth_bgr = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=25, sigmaSpace=10)
    img_lab = cv2.cvtColor(smooth_bgr, cv2.COLOR_BGR2LAB)
    
    k = 16
    pixels = np.float32(img_lab.reshape(-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 5, cv2.KMEANS_PP_CENTERS)
    labels_img = labels.reshape((h, w)).astype(np.uint8)
    
    centers_lab = np.uint8(centers.reshape((1, k, 3)))
    centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((k, 3))
    
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"
    
    # Pre-extract all path data
    path_data = []
    
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
            area = cv2.contourArea(outer_cnt)
            if area < 2.0:
                continue
            outer_approx = cv2.approxPolyDP(outer_cnt, epsilon=0.5, closed=True)
            if len(outer_approx) < 3:
                continue
            outer_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in outer_approx]
            outer_segs = fit_schneider_bezier(outer_pts, max_error_px=0.5, max_nodes=48, closed=True)
            if not outer_segs:
                continue
            subpaths = [outer_segs]
            
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
                ch_idx = hierarchy_arr[ch_idx][0]
                
            d_parts = []
            for sub in subpaths:
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))
            d_attr = " ".join(d_parts)
            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            
            # Check gradient
            grad_info = None
            if area >= 100.0:
                c_mask = np.zeros((h, w), dtype=np.uint8)
                cv2.drawContours(c_mask, [outer_cnt], -1, 255, -1)
                ch_idx = h_node[2]
                while ch_idx != -1:
                    cv2.drawContours(c_mask, [contours[ch_idx]], -1, 0, -1)
                    ch_idx = hierarchy_arr[ch_idx][0]
                ys, xs = np.where(c_mask > 0)
                if len(xs) >= 80:
                    bgr_vals = img_bgr[ys, xs].astype(np.float64)
                    mean_col = np.mean(bgr_vals, axis=0)
                    std_col = np.std(bgr_vals, axis=0)
                    total_std = np.sqrt(np.mean(std_col**2))
                    if total_std >= 10.0:
                        xc = xs - np.mean(xs)
                        yc = ys - np.mean(ys)
                        X = np.column_stack([xc, yc])
                        XtX = X.T @ X + np.eye(2) * 1e-4
                        XtY = X.T @ (bgr_vals - mean_col)
                        slopes = np.linalg.solve(XtX, XtY)
                        pred = mean_col + X @ slopes
                        ss_tot = np.sum((bgr_vals - mean_col)**2)
                        ss_res = np.sum((bgr_vals - pred)**2)
                        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 1e-5 else 0.0
                        if r2 >= 0.50:
                            U, S, Vt = np.linalg.svd(slopes)
                            ux, uy = float(U[0, 0]), float(U[1, 0])
                            t = xc * ux + yc * uy
                            t_min, t_max = float(np.percentile(t, 5)), float(np.percentile(t, 95))
                            if t_max - t_min >= 10.0:
                                x1 = float(np.mean(xs) + t_min * ux)
                                y1 = float(np.mean(ys) + t_min * uy)
                                x2 = float(np.mean(xs) + t_max * ux)
                                y2 = float(np.mean(ys) + t_max * uy)
                                c_start = np.clip(mean_col + t_min * (slopes[0, :] * ux + slopes[1, :] * uy), 0, 255)
                                c_end = np.clip(mean_col + t_max * (slopes[0, :] * ux + slopes[1, :] * uy), 0, 255)
                                hex_start = f"#{int(round(c_start[2])):02x}{int(round(c_start[1])):02x}{int(round(c_start[0])):02x}"
                                hex_end = f"#{int(round(c_end[2])):02x}{int(round(c_end[1])):02x}{int(round(c_end[0])):02x}"
                                gid = f"grad_c{ci}_{i}"
                                grad_def = (
                                    f'<linearGradient id="{gid}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" gradientUnits="userSpaceOnUse">\n'
                                    f'      <stop offset="0%" stop-color="{hex_start}" />\n'
                                    f'      <stop offset="100%" stop-color="{hex_end}" />\n'
                                    f'    </linearGradient>'
                                )
                                grad_info = (gid, grad_def, hex_start, hex_end, r2, total_std, area)
                                
            path_data.append({
                "layer_id": f"layer_c{ci}_{i}",
                "hex_color": hex_color,
                "rule": rule,
                "d_attr": d_attr,
                "grad_info": grad_info,
            })
            
    # Baseline render
    def render_svg(active_grad_idx=-1):
        defs = []
        body = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
        for idx, p in enumerate(path_data):
            fill = p["hex_color"]
            if idx == active_grad_idx and p["grad_info"] is not None:
                defs.append(p["grad_info"][1])
                fill = f'url(#{p["grad_info"][0]})'
            body.append(f'<path id="{p["layer_id"]}" fill="{fill}"{p["rule"]} stroke="{p["hex_color"]}" stroke-width="1.0" stroke-linejoin="round" d="{p["d_attr"]}" />')
        defs_str = "  <defs>\n    " + "\n    ".join(defs) + "\n  </defs>\n" if defs else ""
        svg_str = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n{defs_str}  ' + "\n  ".join(body) + "\n</svg>"
        doc = pymupdf.open(stream=svg_str.encode("utf-8"), filetype="svg")
        pix = doc[0].get_pixmap()
        rend = cv2.cvtColor(np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, 3)), cv2.COLOR_RGB2BGR)
        mse = float(np.mean((img_bgr.astype(float) - rend.astype(float))**2))
        return mse
        
    base_mse = render_svg(-1)
    print(f"Base MSE: {base_mse:.2f}")
    
    grad_indices = [idx for idx, p in enumerate(path_data) if p["grad_info"] is not None]
    print(f"Testing {len(grad_indices)} candidate gradients individually:")
    for idx in grad_indices:
        p = path_data[idx]
        gid, _, hs, he, r2, std, area = p["grad_info"]
        m = render_svg(idx)
        print(f"  {p['layer_id']} (col={p['hex_color']}, area={area:.0f}, R2={r2:.2f}, {hs}->{he}): MSE={m:.2f} (Delta={m - base_mse:+.2f})")

if __name__ == "__main__":
    test_each_gradient()
