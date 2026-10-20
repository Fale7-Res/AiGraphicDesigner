"""Independent vector-surface tessellation engine for version-04.

It partitions a raster into adaptive, non-overlapping rectangular cells and gives
each leaf a flat SVG fill or a locally fitted SVG linear gradient. It does not
 embed the source raster and does not import or reuse Version 01 code.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import heapq
import itertools
import time
import xml.etree.ElementTree as ET

import cv2
import numpy as np
from PIL import Image


@dataclass
class Config:
    max_cells: int = 9000
    min_gradient_side: int = 8
    min_gradient_gain: float = 0.16
    min_gradient_sse_gain_per_pixel: float = 3.0
    edge_priority_weight: float = 1.5
    comment: str = "V04 adaptive vector-surface tessellation; non-semantic cell representation"


@dataclass
class Leaf:
    x0: int
    y0: int
    x1: int
    y1: int
    flat_sse: float
    rep_sse: float
    mean_rgb: np.ndarray
    gradient: tuple[float, ...] | None = None
    edge_strength: float = 0.0
    children: list["Leaf"] = field(default_factory=list)
    split_gain: float = 0.0
    serial: int = 0

    @property
    def width(self) -> int:
        return self.x1 - self.x0

    @property
    def height(self) -> int:
        return self.y1 - self.y0


class IntegralStats:
    """Rectangle color moments, enabling O(1) local regression statistics."""

    def __init__(self, rgb: np.ndarray):
        image = rgb.astype(np.float64, copy=False)
        h, w, _ = image.shape
        yy = (np.arange(h, dtype=np.float64) + 0.5)[:, None]
        xx = (np.arange(w, dtype=np.float64) + 0.5)[None, :]
        self.sum_rgb = []
        self.sum_sq = []
        self.sum_x = []
        self.sum_y = []
        self.edge_integral = None
        gray = cv2.cvtColor(np.asarray(np.clip(image, 0, 255), dtype=np.uint8), cv2.COLOR_RGB2GRAY)
        gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
        gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
        edge_strength = np.clip(cv2.magnitude(gx, gy) / (4.0 * 255.0), 0.0, 1.0).astype(np.float64)
        self.edge_integral = cv2.integral(np.ascontiguousarray(edge_strength), sdepth=cv2.CV_64F)
        for c in range(3):
            plane = np.ascontiguousarray(image[:, :, c])
            self.sum_rgb.append(cv2.integral(plane, sdepth=cv2.CV_64F))
            self.sum_sq.append(cv2.integral(np.ascontiguousarray(plane * plane), sdepth=cv2.CV_64F))
            self.sum_x.append(cv2.integral(np.ascontiguousarray(plane * xx), sdepth=cv2.CV_64F))
            self.sum_y.append(cv2.integral(np.ascontiguousarray(plane * yy), sdepth=cv2.CV_64F))

    @staticmethod
    def rect(integral: np.ndarray, x0: int, y0: int, x1: int, y1: int) -> float:
        return float(integral[y1, x1] - integral[y0, x1] - integral[y1, x0] + integral[y0, x0])

    def vector(self, bundle: list[np.ndarray], x0: int, y0: int, x1: int, y1: int) -> np.ndarray:
        return np.array([self.rect(bundle[c], x0, y0, x1, y1) for c in range(3)], dtype=np.float64)

    def edge_mean(self, x0: int, y0: int, x1: int, y1: int) -> float:
        count = max(1, (x1 - x0) * (y1 - y0))
        return self.rect(self.edge_integral, x0, y0, x1, y1) / count

    def statistics(self, x0: int, y0: int, x1: int, y1: int):
        n = max(1, (x1 - x0) * (y1 - y0))
        sums = self.vector(self.sum_rgb, x0, y0, x1, y1)
        squares = self.vector(self.sum_sq, x0, y0, x1, y1)
        sum_x = self.vector(self.sum_x, x0, y0, x1, y1)
        sum_y = self.vector(self.sum_y, x0, y0, x1, y1)
        mean = sums / n
        flat_sse = max(0.0, float(np.sum(squares - sums * sums / n)))

        width, height = x1 - x0, y1 - y0
        var_x = (width * width - 1.0) / 12.0
        var_y = (height * height - 1.0) / 12.0
        cx = (x0 + x1) / 2.0
        cy = (y0 + y1) / 2.0
        dx_sum = sum_x - cx * sums
        dy_sum = sum_y - cy * sums
        dx_var = n * var_x
        dy_var = n * var_y
        ax = dx_sum / dx_var if dx_var > 1e-12 else np.zeros(3, dtype=np.float64)
        ay = dy_sum / dy_var if dy_var > 1e-12 else np.zeros(3, dtype=np.float64)
        plane_sse = flat_sse
        if dx_var > 1e-12:
            plane_sse -= float(np.sum(dx_sum * dx_sum / dx_var))
        if dy_var > 1e-12:
            plane_sse -= float(np.sum(dy_sum * dy_sum / dy_var))
        plane_sse = max(0.0, plane_sse)

        # Fit the best rank-1 spatial color gradient: one SVG linear-gradient
        # direction with a per-channel color vector. Any orthogonal gradient
        # component is counted as residual error.
        sx = np.sqrt(max(var_x, 0.0))
        sy = np.sqrt(max(var_y, 0.0))
        weighted = np.vstack([sx * ax, sy * ay])
        try:
            u, singular, vt = np.linalg.svd(weighted, full_matrices=False)
        except np.linalg.LinAlgError:
            u = np.zeros((2, 2)); singular = np.zeros(2); vt = np.zeros((2, 3))
        second = float(singular[1]) if len(singular) > 1 else 0.0
        gradient_sse = max(0.0, plane_sse + n * second * second)
        qx = float(u[0, 0] / sx) if sx > 1e-12 else 0.0
        qy = float(u[1, 0] / sy) if sy > 1e-12 else 0.0
        color_slope = singular[0] * vt[0] if len(singular) else np.zeros(3)
        gradient_gain = (flat_sse - gradient_sse) / max(flat_sse, 1e-9)
        gain_per_pixel = (flat_sse - gradient_sse) / n

        gradient = None
        if width >= self._min_gradient_side and height >= self._min_gradient_side:
            if gradient_gain >= self._min_gradient_gain and gain_per_pixel >= self._min_gradient_sse_gain_per_pixel:
                # Store the local SVG-space endpoints and RGB stop colors. The
                # endpoints are extreme corners along the fitted projection.
                corners = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
                proj = [qx * (x - cx) + qy * (y - cy) for x, y in corners]
                i0, i1 = int(np.argmin(proj)), int(np.argmax(proj))
                (gx0, gy0), (gx1, gy1) = corners[i0], corners[i1]
                col0 = np.clip(mean + color_slope * proj[i0], 0, 255)
                col1 = np.clip(mean + color_slope * proj[i1], 0, 255)
                # Keep stop channels separate to avoid any packed-color rounding.
                gradient = (float(gx0), float(gy0), float(gx1), float(gy1),
                            *[float(np.clip(round(c), 0, 255)) for c in col0],
                            *[float(np.clip(round(c), 0, 255)) for c in col1])
        if gradient is not None and gradient_sse < flat_sse:
            return mean, flat_sse, gradient_sse, gradient
        return mean, flat_sse, flat_sse, None


class AdaptiveVectorSurface:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()
        self._stats: IntegralStats | None = None
        self._id_iter = itertools.count()

    @staticmethod
    def _hex(rgb: tuple[int, int, int]) -> str:
        return "#%02x%02x%02x" % tuple(int(np.clip(round(c), 0, 255)) for c in rgb)

    def _node(self, x0: int, y0: int, x1: int, y1: int) -> Leaf:
        assert self._stats is not None
        mean, flat_sse, rep_sse, grad = self._stats.statistics(x0, y0, x1, y1)
        edge_mean = self._stats.edge_mean(x0, y0, x1, y1)
        return Leaf(x0, y0, x1, y1, flat_sse, rep_sse, mean, grad, edge_strength=edge_mean, serial=next(self._id_iter))

    def _split(self, node: Leaf) -> list[Leaf]:
        x0, y0, x1, y1 = node.x0, node.y0, node.x1, node.y1
        if node.width <= 1 and node.height <= 1:
            return []
        xs = [x0, (x0 + x1) // 2, x1] if node.width > 1 else [x0, x1]
        ys = [y0, (y0 + y1) // 2, y1] if node.height > 1 else [y0, y1]
        result = []
        for yi in range(len(ys) - 1):
            for xi in range(len(xs) - 1):
                xa, xb = xs[xi], xs[xi + 1]
                ya, yb = ys[yi], ys[yi + 1]
                if xb > xa and yb > ya:
                    result.append(self._node(xa, ya, xb, yb))
        return result

    def vectorize(self, image: str | Path | np.ndarray) -> tuple[str, dict]:
        start = time.perf_counter()
        if isinstance(image, (str, Path)):
            rgb = np.asarray(Image.open(image).convert("RGB"), dtype=np.uint8)
            source_label = str(image)
        else:
            rgb = np.asarray(image, dtype=np.uint8)
            if rgb.ndim != 3 or rgb.shape[2] != 3:
                raise ValueError("image array must have shape (height, width, 3) in RGB order")
            source_label = "<array>"
        h, w = rgb.shape[:2]
        if h < 1 or w < 1:
            raise ValueError("image cannot be empty")
        if self.config.max_cells < 1:
            raise ValueError("max_cells must be positive")

        # Make the per-node gradient decision configurable but keep it internal
        # to the local-statistics evaluator (no global color palette/contours).
        self._stats = IntegralStats(rgb)
        self._stats._min_gradient_side = self.config.min_gradient_side
        self._stats._min_gradient_gain = self.config.min_gradient_gain
        self._stats._min_gradient_sse_gain_per_pixel = self.config.min_gradient_sse_gain_per_pixel
        self._id_iter = itertools.count()
        root = self._node(0, 0, w, h)
        leaves: dict[int, Leaf] = {root.serial: root}
        queue: list[tuple[float, int, Leaf, list[Leaf]]] = []

        def enqueue(node: Leaf):
            kids = self._split(node)
            if not kids:
                return
            gain = max(0.0, node.rep_sse - sum(ch.rep_sse for ch in kids))
            node.children = kids
            node.split_gain = gain
            # A split adds (len(kids)-1) primitives, so rank by SSE reduction
            # per additional leaf. Serial is deterministic tie-breaking.
            score = gain / max(1, len(kids) - 1) * (1.0 + self.config.edge_priority_weight * node.edge_strength)
            heapq.heappush(queue, (-score, node.serial, node, kids))

        enqueue(root)
        cell_count = 1
        while queue:
            if cell_count >= self.config.max_cells:
                break
            neg_score, _serial, node, kids = heapq.heappop(queue)
            if node.serial not in leaves or not node.children:
                continue
            extra = len(kids) - 1
            if cell_count + extra > self.config.max_cells:
                # Keep the candidate aside for later? Since this adds more
                # leaves than the remaining budget, smaller candidates might
                # still fit. Skip it without splitting.
                continue
            if -neg_score <= 1e-10:
                break
            del leaves[node.serial]
            node.children = []
            for child in kids:
                leaves[child.serial] = child
                enqueue(child)
            cell_count += extra

        ordered = sorted(leaves.values(), key=lambda n: (n.y0, n.x0, n.y1, n.x1))
        svg_parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" version="1.1">',
            f'<title>{self.config.comment}</title>',
            '<desc>Pure SVG rectangle tessellation with optional per-cell linear gradients; source raster is not embedded.</desc>',
            '<defs>'
        ]
        gradient_defs: list[str] = []
        shapes: list[str] = []
        gradient_count = 0
        for node in ordered:
            x, y, ww, hh = node.x0, node.y0, node.width, node.height
            if node.gradient is not None:
                gx0, gy0, gx1, gy1, r0, g0, b0, r1, g1, b1 = node.gradient
                rgb0 = (int(r0), int(g0), int(b0))
                rgb1 = (int(r1), int(g1), int(b1))
                gid = f"g{gradient_count}"
                gradient_count += 1
                gradient_defs.append(
                    f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{gx0:.4f}" y1="{gy0:.4f}" x2="{gx1:.4f}" y2="{gy1:.4f}" spreadMethod="pad">'
                    f'<stop offset="0" stop-color="{self._hex(rgb0)}"/><stop offset="1" stop-color="{self._hex(rgb1)}"/></linearGradient>'
                )
                fill = f'url(#{gid})'
            else:
                fill = self._hex(tuple(node.mean_rgb.tolist()))
            shapes.append(f'<rect x="{x}" y="{y}" width="{ww}" height="{hh}" fill="{fill}"/>')
        svg_parts.extend(gradient_defs)
        svg_parts.append('</defs><g id="surface-tessellation" shape-rendering="crispEdges">')
        svg_parts.extend(shapes)
        svg_parts.append('</g></svg>')
        svg = ''.join(svg_parts)

        # This is a structural self-check, not a rendering compatibility claim.
        root_xml = ET.fromstring(svg)
        ns = {"svg": "http://www.w3.org/2000/svg"}
        rect_count = len(root_xml.findall(".//svg:rect", ns))
        path_count = len(root_xml.findall(".//svg:path", ns))
        embedded_images = len(root_xml.findall(".//svg:image", ns))
        elapsed_ms = (time.perf_counter() - start) * 1000.0
        metrics = {
            "source": source_label,
            "width": w,
            "height": h,
            "leaf_cells": len(ordered),
            "rectangles": rect_count,
            "linear_gradients": gradient_count,
            "path_count": path_count,
            "path_anchor_and_control_points": 0,
            "implicit_rectangle_corners": rect_count * 4,
            "embedded_raster_images": embedded_images,
            "svg_bytes": len(svg.encode("utf-8")),
            "generation_ms": round(elapsed_ms, 3),
            "representation": "pure vector surface tessellation; non-semantic cell objects",
            "requested_cell_budget": self.config.max_cells,
        }
        return svg, metrics


def rasterize_svg(svg_path: str | Path, png_path: str | Path, width: int, height: int,
                  inkscape: str = "inkscape") -> float:
    """Rasterize with local Inkscape CLI; returns render wall time in milliseconds."""
    import subprocess
    start = time.perf_counter()
    command = [inkscape, str(svg_path), "--export-type=png", f"--export-filename={png_path}",
               f"--export-width={width}", f"--export-height={height}"]
    try:
        done = subprocess.run(command, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"Inkscape exceeded 90 seconds rendering {svg_path}; this is a rendering-complexity failure, not a metric result.") from exc
    if done.returncode != 0:
        raise RuntimeError(f"Inkscape render failed for {svg_path}: {done.stderr[-1200:]}")
    rendered = Image.open(png_path)
    if rendered.size != (width, height):
        raise RuntimeError(f"unexpected render size {rendered.size}; expected {(width, height)}")
    return (time.perf_counter() - start) * 1000.0


def add_edge_residual_layer(svg: str, image: str | Path | np.ndarray, dilation: int = 1,
                            canny_low: int = 80, canny_high: int = 160,
                            color_bits: int = 5) -> tuple[str, dict]:
    """Add an edge-band appearance correction as SVG vector subregions.

    Only a 3x3-dilated Canny band is emitted by default. Each selected source
    pixel becomes a pixel-aligned, 1-row rectangular SVG subpath. To lower XML
    and DOM overhead, adjacent edge pixels with the same quantized source color
    are merged into horizontal runs, then same-color runs are grouped into one
    SVG path. The default residual colors have 5 bits/channel; set ``color_bits=8``
    for exact 24-bit source colors. This hybrid vector representation is not a
    clean semantic layer reconstruction and never embeds a raster image.
    """
    if isinstance(image, (str, Path)):
        rgb = np.asarray(Image.open(image).convert("RGB"), dtype=np.uint8)
    else:
        rgb = np.asarray(image, dtype=np.uint8)
    if rgb.ndim != 3 or rgb.shape[2] != 3:
        raise ValueError("image array must have shape (height, width, 3) in RGB order")
    if dilation < 0 or dilation > 4:
        raise ValueError("dilation must be between 0 and 4")
    if color_bits < 4 or color_bits > 8:
        raise ValueError("color_bits must be between 4 and 8")
    h, w = rgb.shape[:2]
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    edge_mask = (cv2.Canny(gray, canny_low, canny_high) > 0).astype(np.uint8)
    if dilation:
        edge_mask = cv2.dilate(edge_mask, np.ones((3, 3), np.uint8), iterations=dilation)

    # Per-channel uniform scalar quantization, confined to the residual band.
    levels = (1 << color_bits) - 1
    step = 255.0 / levels
    quantized = np.clip(np.rint(rgb.astype(np.float32) / step) * step, 0, 255).astype(np.uint8)
    by_color: dict[tuple[int, int, int], list[str]] = {}
    run_count = 0
    pixel_count = int(edge_mask.sum())
    for y in range(h):
        x = 0
        while x < w:
            if edge_mask[y, x] == 0:
                x += 1
                continue
            color = tuple(int(v) for v in quantized[y, x])
            x1 = x + 1
            while x1 < w and edge_mask[y, x1] and tuple(int(v) for v in quantized[y, x1]) == color:
                x1 += 1
            run_width = x1 - x
            by_color.setdefault(color, []).append(f"M{x},{y}h{run_width}v1h-{run_width}z")
            run_count += 1
            x = x1

    chunks = ['<g id="edge-band-residuals" shape-rendering="crispEdges">']
    for idx, color in enumerate(sorted(by_color)):
        d = " ".join(by_color[color])
        fill = "#%02x%02x%02x" % color
        chunks.append(f'<path id="edge-color-{idx}" fill="{fill}" d="{d}"/>')
    chunks.append('</g>')
    content = ''.join(chunks)
    updated = svg.replace(
        'Pure SVG rectangle tessellation with optional per-cell linear gradients; source raster is not embedded.',
        'Hybrid vector-only representation: adaptive surface cells plus RGB-quantized source-derived SVG subpaths along a dilated high-confidence source-edge band; no raster image is embedded.'
    )
    if '</svg>' not in updated:
        raise ValueError("input SVG is missing its closing </svg> tag")
    updated = updated.rsplit('</svg>', 1)[0] + content + '</svg>'
    meta = {
        "edge_residual_method": "Canny(80,160), dilated 3x3 neighborhood, horizontal same-color runs; vector-only, source-derived color correction",
        "edge_residual_dilation_iterations": dilation,
        "edge_residual_color_bits_per_channel": color_bits,
        "edge_residual_pixels": pixel_count,
        "edge_residual_horizontal_runs": run_count,
        "edge_residual_color_paths": len(by_color),
        "edge_residual_implicit_corners": run_count * 4,
        "embedded_raster_images": 0,
        "representation": "hybrid vector surface tessellation plus quantized edge-band residual; non-semantic objects",
    }
    return updated, meta
