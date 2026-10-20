"""Deterministic synthetic known-geometry test performed before the photo benchmarks."""
from pathlib import Path
import json
import sys
import time
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HERE = Path(__file__).resolve()
VERSION_DIR = HERE.parents[1]
ROOT = HERE.parents[3]
sys.path.insert(0, str(VERSION_DIR))
from src.challenger import AdaptiveVectorSurface, Config, add_edge_residual_layer, rasterize_svg  # noqa: E402
from src.run_benchmark import compare  # noqa: E402

OUT = VERSION_DIR / "experiments" / "synthetic"


def make_synthetic(width=320, height=240, scale=3):
    w, h = width * scale, height * scale
    y = np.linspace(0.0, 1.0, h, dtype=np.float32)[:, None]
    x = np.linspace(0.0, 1.0, w, dtype=np.float32)[None, :]
    arr = np.zeros((h, w, 3), dtype=np.uint8)
    for c, (a, b) in enumerate([(238, 248), (241, 246), (246, 252)]):
        arr[:, :, c] = np.clip(a * (1 - y) + b * y + 2 * np.sin(x * np.pi), 0, 255).astype(np.uint8)
    im = Image.fromarray(arr, "RGB")

    # Soft cast shadow on its own raster layer, composited into the ground truth.
    shadow = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    shd = ImageDraw.Draw(shadow)
    shd.ellipse((68*scale, 182*scale, 258*scale, 225*scale), fill=(20, 19, 31, 95))
    shadow = shadow.filter(ImageFilter.GaussianBlur(7*scale))
    im = Image.alpha_composite(im.convert("RGBA"), shadow).convert("RGB")

    # Rounded blue plaque with a true vector-like flat fill.
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((42*scale, 25*scale, 278*scale, 207*scale), radius=24*scale,
                        fill=(24, 54, 86), outline=(13, 29, 47), width=3*scale)

    # Metallic shield gradient painted through a known polygon mask.
    shield_pts = [(160, 45), (221, 66), (214, 135), (160, 173), (106, 135), (99, 66)]
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    md.polygon([(px*scale, py*scale) for px, py in shield_pts], fill=255)
    gy = np.linspace(0, 1, h)[:, None]
    ramp = np.array([[[138, 75, 9], [255, 225, 125], [171, 100, 23]]], dtype=np.float32)
    band = np.zeros((h, w, 3), dtype=np.uint8)
    for c in range(3):
        vals = np.interp(gy[:, 0], [0, 0.45, 1], ramp[0, :, c])
        band[:, :, c] = vals[:, None].astype(np.uint8)
    band_im = Image.fromarray(band, "RGB")
    im.paste(band_im, (0, 0), mask)
    d = ImageDraw.Draw(im)
    d.line([(px*scale, py*scale) for px, py in shield_pts + [shield_pts[0]]], fill=(255, 238, 176), width=2*scale, joint="curve")

    # Red inset (known nested region) and small bright highlight wedge.
    inner = [(160, 57), (209, 74), (202, 128), (160, 158), (118, 128), (111, 74)]
    d.polygon([(px*scale, py*scale) for px, py in inner], fill=(158, 22, 35))
    highlight = [(125, 77), (158, 64), (153, 112), (126, 125)]
    d.polygon([(px*scale, py*scale) for px, py in highlight], fill=(207, 66, 61))

    # Beveled gold circle and a small blue hole: overlapping, meaningful shapes.
    d.ellipse((145*scale, 98*scale, 176*scale, 129*scale), fill=(251, 199, 73), outline=(255, 239, 177), width=2*scale)
    d.ellipse((153*scale, 106*scale, 168*scale, 121*scale), fill=(24, 54, 86))
    d.arc((148*scale, 99*scale, 174*scale, 125*scale), start=205, end=315, fill=(255, 249, 220), width=2*scale)

    # Tiny separated marks test detail retention.
    d.ellipse((73*scale, 43*scale, 80*scale, 50*scale), fill=(245, 186, 59))
    d.ellipse((242*scale, 176*scale, 250*scale, 184*scale), fill=(238, 103, 55))
    return im.resize((width, height), Image.Resampling.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    source = make_synthetic()
    src_path = OUT / "S00_known_geometry_source.png"
    source.save(src_path)
    budget = 9000
    model = AdaptiveVectorSurface(Config(max_cells=budget))
    start = time.perf_counter()
    svg, stats = model.vectorize(src_path)
    svg_path = OUT / "S00_known_geometry_v04.svg"
    png_path = OUT / "S00_known_geometry_v04_rendered.png"
    svg_path.write_text(svg, encoding="utf-8")
    render_ms = rasterize_svg(svg_path, png_path, source.width, source.height)
    metrics = compare(np.asarray(source.convert("RGB")), np.asarray(Image.open(png_path).convert("RGB")))
    result = {"experiment": "S00_known_nested_geometry_gradient_shadow_and_highlights", "source_size": list(source.size),
              "budget": budget, **stats, "render_ms": round(render_ms, 3), **metrics,
              "known_geometry": ["rounded plaque", "nested shield polygons", "gold border", "red inset", "highlight patch", "ring with hole", "blurred shadow", "two small marks"],
              "limitations": ["test is synthetic and not evidence of semantic layer recovery", "input shadow was pre-composited to RGB", "tessellation is not object-aware"]}
    (OUT / "S00_known_geometry_metrics.json").write_text(json.dumps(result, indent=2), encoding="utf-8")

    # Second iteration: keep the pure surface output above as an experiment record,
    # and emit a separately named hybrid output with the source-derived edge residual.
    overlay_start = time.perf_counter()
    hybrid_svg, edge_meta = add_edge_residual_layer(svg, np.asarray(source.convert("RGB")), dilation=1, color_bits=5)
    overlay_ms = (time.perf_counter() - overlay_start) * 1000.0
    hybrid_svg_path = OUT / "S00_known_geometry_v04_hybrid.svg"
    hybrid_png_path = OUT / "S00_known_geometry_v04_hybrid_rendered.png"
    hybrid_svg_path.write_text(hybrid_svg, encoding="utf-8")
    hybrid_render_ms = rasterize_svg(hybrid_svg_path, hybrid_png_path, source.width, source.height)
    hybrid_metrics = compare(np.asarray(source.convert("RGB")), np.asarray(Image.open(hybrid_png_path).convert("RGB")))
    hybrid_result = {"experiment":"S00_known_geometry_hybrid_edge_residual_iteration", "source_size":list(source.size),
                     **edge_meta, "svg_bytes":hybrid_svg_path.stat().st_size, "generation_plus_overlay_ms":round(float(stats['generation_ms'])+overlay_ms,3),
                     "render_ms":round(hybrid_render_ms,3), **hybrid_metrics,
                     "note":"Source-derived edge residual is intentionally a hybrid vector-only correction, not semantic recovery."}
    (OUT / "S00_known_geometry_hybrid_metrics.json").write_text(json.dumps(hybrid_result,indent=2),encoding="utf-8")
    print(json.dumps({"surface_only":result,"hybrid_edge_residual":hybrid_result},indent=2))

if __name__ == "__main__": main()
