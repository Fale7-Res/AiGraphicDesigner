"""Run fair Version 01 vs Version 04 native-size SVG evaluation."""
from __future__ import annotations
import argparse
import csv
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import threading
import time
import xml.etree.ElementTree as ET

import cv2
import numpy as np
import psutil
from PIL import Image, ImageDraw, ImageFont
from skimage.metrics import structural_similarity

HERE = Path(__file__).resolve()
VERSION_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
sys.path.insert(0, str(VERSION_DIR))
from src.challenger import AdaptiveVectorSurface, Config, rasterize_svg  # noqa: E402

SRC_DIR = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12"
V01_SVG_DIR = ROOT / "versions/version-01/experiments/preliminary_visual_tests/outputs"
V01_RECORDED_JSON = ROOT / "versions/version-01/experiments/fidelity_diagnostics/all_12_rerun_metrics.json"
OUT = VERSION_DIR / "experiments"

class PeakRssSampler:
    def __init__(self, interval=0.005):
        self.process = psutil.Process(os.getpid())
        self.interval = interval
        self.peak = 0
        self.stop_flag = False
        self.thread = threading.Thread(target=self._run, daemon=True)
    def _run(self):
        while not self.stop_flag:
            try:
                self.peak = max(self.peak, self.process.memory_info().rss)
            except psutil.Error:
                pass
            time.sleep(self.interval)
    def __enter__(self):
        self.peak = self.process.memory_info().rss
        self.thread.start()
        return self
    def __exit__(self, *args):
        self.stop_flag = True
        self.thread.join(timeout=1)
        try: self.peak = max(self.peak, self.process.memory_info().rss)
        except psutil.Error: pass
    @property
    def mb(self): return self.peak / (1024 * 1024)


def load_rgb(path: Path) -> np.ndarray:
    return np.asarray(Image.open(path).convert("RGB"), dtype=np.uint8)


def svg_structure(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    root = ET.fromstring(text)
    tags = [el.tag.rsplit("}", 1)[-1] for el in root.iter()]
    paths = [el for el in root.iter() if el.tag.rsplit("}", 1)[-1] == "path"]
    rects = sum(t == "rect" for t in tags)
    path_cmd_counts = {"M": 0, "L": 0, "C": 0, "Q": 0, "A": 0, "other": 0}
    anchors_controls = 0
    for el in paths:
        d = el.attrib.get("d", "")
        for m in re.finditer(r"([MmLlHhVvCcSsQqTtAaZz])", d):
            cmd = m.group(1).upper()
            if cmd == "M": anchors_controls += 1; path_cmd_counts["M"] += 1
            elif cmd == "L": anchors_controls += 1; path_cmd_counts["L"] += 1
            elif cmd == "C": anchors_controls += 3; path_cmd_counts["C"] += 1
            elif cmd == "Q": anchors_controls += 2; path_cmd_counts["Q"] += 1
            elif cmd == "A": anchors_controls += 1; path_cmd_counts["A"] += 1
            elif cmd in ("H", "V"): anchors_controls += 1; path_cmd_counts["L"] += 1
            elif cmd in ("S", "T"): anchors_controls += 2 if cmd == "S" else 1; path_cmd_counts["other"] += 1
    return {
        "svg_bytes": path.stat().st_size,
        "path_count": len(paths),
        "rectangle_count": rects,
        "estimated_path_anchors_and_controls": anchors_controls,
        "path_commands": path_cmd_counts,
        "embedded_raster_images": sum(t == "image" for t in tags),
        "linear_gradients": sum(t == "linearGradient" for t in tags),
        "xml_well_formed": True,
    }


def _edge_metrics(ref: np.ndarray, pred: np.ndarray) -> dict:
    ref_g = cv2.cvtColor(ref, cv2.COLOR_RGB2GRAY)
    pred_g = cv2.cvtColor(pred, cv2.COLOR_RGB2GRAY)
    ref_edge = cv2.Canny(ref_g, 80, 160) > 0
    pred_edge = cv2.Canny(pred_g, 80, 160) > 0
    kernel = np.ones((3, 3), np.uint8)
    ref_dil = cv2.dilate(ref_edge.astype(np.uint8), kernel) > 0
    pred_dil = cv2.dilate(pred_edge.astype(np.uint8), kernel) > 0
    precision = float((pred_edge & ref_dil).sum() / max(1, pred_edge.sum()))
    recall = float((ref_edge & pred_dil).sum() / max(1, ref_edge.sum()))
    f1 = 2 * precision * recall / max(1e-12, precision + recall)

    # Tiny-contour diagnostic: edge pixels belonging to <=50-pixel connected
    # components in the reference edge map. This is a proxy, not semantic GT.
    nlab, labels, stats, _ = cv2.connectedComponentsWithStats(ref_edge.astype(np.uint8), 8)
    tiny = np.zeros_like(ref_edge)
    for i in range(1, nlab):
        if stats[i, cv2.CC_STAT_AREA] <= 50:
            tiny |= labels == i
    tiny_den = int(tiny.sum())
    tiny_recall = float((tiny & pred_dil).sum() / max(1, tiny_den)) if tiny_den else float("nan")

    # Foreground proxy relative to the reference image's border median color.
    border = np.concatenate([ref[0], ref[-1], ref[:, 0], ref[:, -1]], axis=0).astype(np.float32)
    bg = np.median(border, axis=0)
    ref_mask = np.linalg.norm(ref.astype(np.float32) - bg, axis=2) > 20.0
    pred_mask = np.linalg.norm(pred.astype(np.float32) - bg, axis=2) > 20.0
    iou = float((ref_mask & pred_mask).sum() / max(1, (ref_mask | pred_mask).sum()))
    return {"edge_precision_1px": precision, "edge_recall_1px": recall,
            "edge_f1_1px": f1, "small_edge_component_recall_proxy": tiny_recall,
            "border_background_foreground_iou_proxy": iou}


def compare(ref: np.ndarray, rendered: np.ndarray) -> dict:
    if ref.shape != rendered.shape:
        raise ValueError(f"Image dimension mismatch: {ref.shape} vs {rendered.shape}")
    diff = ref.astype(np.float64) - rendered.astype(np.float64)
    mse = float(np.mean(diff * diff))
    psnr = float(10 * np.log10((255.0 * 255.0) / mse)) if mse > 0 else 99.0
    ssim = float(structural_similarity(ref, rendered, channel_axis=2, data_range=255))
    out = {"mse": mse, "psnr_db": psnr, "ssim": ssim}
    out.update(_edge_metrics(ref, rendered))
    return out


def render_font(size=18):
    try: return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError: return ImageFont.load_default()


def make_comparison(stem: str, source_path: Path, v01_path: Path, v04_path: Path, target: Path):
    imgs = [Image.open(source_path).convert("RGB"), Image.open(v01_path).convert("RGB"), Image.open(v04_path).convert("RGB")]
    labels = ["ORIGINAL", "VERSION 01 / ANTIGRAVITY", "VERSION 04 / CLAUDE CHALLENGER"]
    scale = max(1, min(3, 900 // max(i.width for i in imgs)))
    panel_h = max(i.height for i in imgs) * scale + 34
    panel_w = sum(i.width * scale + 24 for i in imgs)
    canvas = Image.new("RGB", (panel_w, panel_h + 8), (247, 247, 247))
    draw = ImageDraw.Draw(canvas)
    x = 8
    for img, label in zip(imgs, labels):
        draw.text((x, 4), label, fill=(20, 20, 20), font=render_font(14))
        thumb = img.resize((img.width * scale, img.height * scale), Image.Resampling.LANCZOS)
        canvas.paste(thumb, (x, 28))
        x += img.width * scale + 24
    canvas.save(target)


def make_contact_sheet(records: list[dict], target: Path):
    """Contact sheet with non-overlapping image IDs and panel labels."""
    thumbs = []
    font = render_font(14)
    for rec in records:
        paths = [Path(rec["source_path"]), Path(rec["v01_render_path"]), Path(rec["v04_render_path"])]
        ims = [Image.open(p).convert("RGB") for p in paths]
        panel_w, panel_h = 240, 190
        row = Image.new("RGB", (panel_w * 3, panel_h + 34), "white")
        draw = ImageDraw.Draw(row)
        draw.text((4, 2), rec["image_id"], fill="black", font=font)
        for i, (im, lbl) in enumerate(zip(ims, ["Original", "Antigravity V01", "Claude V04"])):
            x = i * panel_w
            draw.text((x + 4, 18), lbl, fill=(30, 30, 30), font=font)
            im.thumbnail((panel_w - 8, panel_h - 8), Image.Resampling.LANCZOS)
            row.paste(im, (x + (panel_w - im.width) // 2, 44 + (panel_h - im.height) // 2))
        thumbs.append(row)
    col_n = 2
    row_n = (len(thumbs) + col_n - 1) // col_n
    sheet = Image.new("RGB", (col_n * thumbs[0].width, row_n * thumbs[0].height), (240, 240, 240))
    for i, im in enumerate(thumbs):
        sheet.paste(im, ((i % col_n) * im.width, (i // col_n) * im.height))
    target.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(target)

def main():
    """Reproducible entry point for A01 budget sweep and final 12-image run."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--budget", type=int, default=9000, help="adaptive surface leaf-cell budget")
    parser.add_argument("--inkscape", default="inkscape", help="Inkscape executable or full path")
    parser.add_argument("--skip-v01-render", action="store_true", help="reuse prior fresh V01 PNG renders if present")
    parser.add_argument("--a01-sweep", action="store_true", help="measure surface-only A01 budgets before final hybrid run")
    args = parser.parse_args()
    if shutil.which(args.inkscape) is None and not Path(args.inkscape).exists():
        raise SystemExit(f"Inkscape executable not found: {args.inkscape}")
    for sub in ["outputs", "rendered/v01", "rendered/v04", "comparisons", "metrics", "logs"]:
        (OUT / sub).mkdir(parents=True, exist_ok=True)
    inputs = sorted(p for p in SRC_DIR.glob("A*.png") if re.match(r"A\d\d_", p.name))
    if len(inputs) != 12:
        raise RuntimeError(f"Expected 12 benchmark images; found {len(inputs)}")
    if args.a01_sweep:
        a01 = next(p for p in inputs if p.name.startswith("A01_"))
        source = load_rgb(a01)
        sweep_rows = []
        for budget in sorted(set([1000, 2500, 5000, args.budget])):
            svg, stats = AdaptiveVectorSurface(Config(max_cells=budget)).vectorize(source)
            svg_path = OUT / "outputs" / f"A01_surface_only_budget_{budget}.svg"
            png_path = OUT / "rendered" / "v04" / f"A01_surface_only_budget_{budget}.png"
            svg_path.write_text(svg, encoding="utf-8")
            render_ms = rasterize_svg(svg_path, png_path, source.shape[1], source.shape[0], args.inkscape)
            sweep_rows.append({"budget": budget, **stats, "render_ms": round(render_ms, 3), **compare(source, load_rgb(png_path))})
        (OUT / "metrics" / "a01_surface_only_budget_sweep.json").write_text(json.dumps(sweep_rows, indent=2), encoding="utf-8")
        with (OUT / "metrics" / "a01_surface_only_budget_sweep.csv").open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(sweep_rows[0].keys())); writer.writeheader(); writer.writerows(sweep_rows)
        print(f"A01 pre-residual surface-only sweep saved ({len(sweep_rows)} budgets).", flush=True)
    command = [sys.executable, str(HERE.parent / "finalize_metrics.py"), "--budget", str(args.budget), "--inkscape", args.inkscape]
    if args.skip_v01_render: command.append("--skip-v01-render")
    subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
