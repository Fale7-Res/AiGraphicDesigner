#!/usr/bin/env python3
import sys
from pathlib import Path
import cv2
import numpy as np
import pymupdf

ROOT = Path(__file__).resolve().parents[4]
VERSION_01_DIR = ROOT / "versions" / "version-01"
sys.path.insert(0, str(VERSION_01_DIR))

from src.pipeline import SequentialPipeline

def main():
    img_path = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"
    img = cv2.imread(str(img_path))
    h, w = img.shape[:2]
    
    # 1. Pipeline without gradient
    p_flat = SequentialPipeline(error_tolerance_px=0.5, seed=42, enable_gradients=False)
    svg_flat, t_flat = p_flat.process_image(img_path, n_colors=16, min_contour_area=2.0)
    doc_flat = pymupdf.open(stream=svg_flat.encode(), filetype="svg")
    rend_flat = cv2.cvtColor(np.frombuffer(doc_flat[0].get_pixmap().samples, dtype=np.uint8).reshape((h, w, 3)), cv2.COLOR_RGB2BGR)
    mse_flat = np.mean((img.astype(float) - rend_flat.astype(float))**2)
    psnr_flat = 10 * np.log10(255**2 / mse_flat)
    print(f"Flat Pipeline (min_area=2.0): PSNR={psnr_flat:.2f} dB, MSE={mse_flat:.2f}, paths={t_flat['total_paths']}, nodes={t_flat['total_nodes']}")

    # 2. Pipeline with gradient
    p_grad = SequentialPipeline(error_tolerance_px=0.5, seed=42, enable_gradients=True)
    svg_grad, t_grad = p_grad.process_image(img_path, n_colors=16, min_contour_area=2.0)
    doc_grad = pymupdf.open(stream=svg_grad.encode(), filetype="svg")
    rend_grad = cv2.cvtColor(np.frombuffer(doc_grad[0].get_pixmap().samples, dtype=np.uint8).reshape((h, w, 3)), cv2.COLOR_RGB2BGR)
    mse_grad = np.mean((img.astype(float) - rend_grad.astype(float))**2)
    psnr_grad = 10 * np.log10(255**2 / mse_grad)
    print(f"Grad Pipeline (min_area=2.0): PSNR={psnr_grad:.2f} dB, MSE={mse_grad:.2f}, paths={t_grad['total_paths']}, nodes={t_grad['total_nodes']}")

    diff_map = np.abs(rend_grad.astype(float) - rend_flat.astype(float))
    print(f"Mean diff between flat and grad render: {np.mean(diff_map):.2f}, Max diff: {np.max(diff_map):.2f}")
    
    # Where does diff_map exceed 10?
    ys, xs = np.where(diff_map > 10)[:2]
    print(f"Number of pixels where flat != grad: {len(xs)}")
    if len(xs) > 0:
        # Check colors at those pixels in orig, flat, and grad
        sample_y, sample_x = ys[0], xs[0]
        print(f"Sample pixel at ({sample_x}, {sample_y}):")
        print(f"  Orig BGR: {img[sample_y, sample_x]}")
        print(f"  Flat BGR: {rend_flat[sample_y, sample_x]}")
        print(f"  Grad BGR: {rend_grad[sample_y, sample_x]}")

if __name__ == "__main__":
    main()
