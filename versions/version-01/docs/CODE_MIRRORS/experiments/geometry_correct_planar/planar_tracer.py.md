# مرآة الكود التفصيلية للإصدار: `version-01/experiments/geometry_correct_planar/planar_tracer.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/experiments/geometry_correct_planar/planar_tracer.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `experiments/geometry_correct_planar/planar_tracer.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `382` (`Lines 1–382`)
- **بصمة الملف (`SHA-256`):** `6667701cab02e0540182c3932b2c93f2a876eb5263a48437028f66cb04a22be8`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PlanarPolygon` | `class` | `Lines 30–46` | `class PlanarPolygon:` | Represents a closed polygonal loop on the planar dual grid. |
| `PlanarPolygon.to_svg_subpath` | `method` | `Lines 37–46` | `def to_svg_subpath(self) -> str:` | Format as SVG path data M x y L x y ... Z. |
| `PlanarColorRegion` | `class` | `Lines 50–86` | `class PlanarColorRegion:` | Represents a complete color region composed of outer boundaries and nested holes. |
| `PlanarColorRegion.to_svg_element` | `method` | `Lines 58–86` | `def to_svg_element(self, use_bezier: bool = False) -> str:` | Render this color region as a single compound <path> with fill-rule='evenodd'. |
| `DualGridPlanarTracer` | `class` | `Lines 89–381` | `class DualGridPlanarTracer:` | Extracts exact shared-boundary planar tiling from a discrete label matrix. |
| `DualGridPlanarTracer.__init__` | `method` | `Lines 92–107` | `def __init__(self, labels_img: np.ndarray, centers_bgr: np.ndarray, bg_color_index: int | None = None) -> None:` | رمز برمجي موثق للإصدار. |
| `DualGridPlanarTracer.extract_directed_cell_edges` | `method` | `Lines 109–148` | `def extract_directed_cell_edges(self) -> dict[int, list[tuple[tuple[int, int], tuple[int, int]]]]:` | Extracts directed interface edges for each color on the grid [0, W] x [0, H]. |
| `DualGridPlanarTracer.assemble_closed_loops` | `method` | `Lines 151–200` | `def assemble_closed_loops(edges: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[list[tuple[float, float]]]:` | Assembles directed unit edges into closed simple polygonal loops without self-intersection. |
| `DualGridPlanarTracer.simplify_collinear_runs` | `method` | `Lines 203–232` | `def simplify_collinear_runs(loop: list[tuple[float, float]]) -> list[tuple[float, float]]:` | Removes redundant intermediate points along straight orthogonal lines. |
| `DualGridPlanarTracer.compute_signed_area` | `method` | `Lines 235–244` | `def compute_signed_area(pts: list[tuple[float, float]]) -> float:` | Computes polygon signed area using shoelace formula. |
| `DualGridPlanarTracer.trace_planar_regions` | `method` | `Lines 246–280` | `def trace_planar_regions(self, simplify_collinear: bool = True, min_area: float = 1.0) -> list[PlanarColorRegion]:` | Extracts all planar color regions as mutually exclusive compound polygons. |
| `DualGridPlanarTracer.build_exact_planar_svg` | `method` | `Lines 282–303` | `def build_exact_planar_svg(self, regions: list[PlanarColorRegion], include_bg: bool = True) -> str:` | Assembles exact planar regions into an SVG document with crispEdges and 0% bloat. |
| `DualGridPlanarTracer.fit_shared_arc_bezier` | `method` | `Lines 305–317` | `def fit_shared_arc_bezier(self, regions: list[PlanarColorRegion], epsilon_px: float = 0.5, max_nodes: int = 48) -> list[PlanarColorRegion]:` | Fits cubic Bézier curves to closed loops while strictly preserving corner junctions. |
| `DualGridPlanarTracer.build_smooth_planar_svg` | `method` | `Lines 319–381` | `def build_smooth_planar_svg(self, regions: list[PlanarColorRegion], stroke_width: float = 0.0, clip_to_silhouette: bool = True) -> str:` | Assembles smooth Bézier planar SVG with optional master silhouette clipping to guarantee 0% bloat. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PlanarPolygon` — `Lines 30–46`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `46` (`Lines 30–46`)
- **الوظيفة:** Represents a closed polygonal loop on the planar dual grid.
- **الكود الفعلي (`Lines 30–46`):**
```python
class PlanarPolygon:
    """Represents a closed polygonal loop on the planar dual grid."""
    color_index: int
    points: list[tuple[float, float]]
    is_hole: bool
    signed_area: float

    def to_svg_subpath(self) -> str:
        """Format as SVG path data M x y L x y ... Z."""
        if len(self.points) < 3:
            return ""
        p0 = self.points[0]
        cmds = [f"M {p0[0]:.2f} {p0[1]:.2f}"]
        for p in self.points[1:]:
            cmds.append(f"L {p[0]:.2f} {p[1]:.2f}")
        cmds.append("Z")
        return " ".join(cmds)
```

### `PlanarPolygon.to_svg_subpath` — `Lines 37–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `46` (`Lines 37–46`)
- **الوظيفة:** Format as SVG path data M x y L x y ... Z.
- **الكود الفعلي (`Lines 37–46`):**
```python
    def to_svg_subpath(self) -> str:
        """Format as SVG path data M x y L x y ... Z."""
        if len(self.points) < 3:
            return ""
        p0 = self.points[0]
        cmds = [f"M {p0[0]:.2f} {p0[1]:.2f}"]
        for p in self.points[1:]:
            cmds.append(f"L {p[0]:.2f} {p[1]:.2f}")
        cmds.append("Z")
        return " ".join(cmds)
```

### `PlanarColorRegion` — `Lines 50–86`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `86` (`Lines 50–86`)
- **الوظيفة:** Represents a complete color region composed of outer boundaries and nested holes.
- **الكود الفعلي (`Lines 50–86`):**
```python
class PlanarColorRegion:
    """Represents a complete color region composed of outer boundaries and nested holes."""
    color_index: int
    hex_color: str
    outer_loops: list[list[tuple[float, float]]] = field(default_factory=list)
    hole_loops: list[list[tuple[float, float]]] = field(default_factory=list)
    bezier_subpaths: list[list[BezierSegment]] = field(default_factory=list)

    def to_svg_element(self, use_bezier: bool = False) -> str:
        """Render this color region as a single compound <path> with fill-rule='evenodd'."""
        d_parts = []
        if use_bezier and self.bezier_subpaths:
            for sub in self.bezier_subpaths:
                if not sub:
                    continue
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))
        else:
            all_loops = self.outer_loops + self.hole_loops
            for loop in all_loops:
                if len(loop) < 3:
                    continue
                part = [f"M {loop[0][0]:.2f} {loop[0][1]:.2f}"]
                for pt in loop[1:]:
                    part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                part.append("Z")
                d_parts.append(" ".join(part))

        if not d_parts:
            return ""
        d_attr = " ".join(d_parts)
        rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
        return f'<path id="planar_c{self.color_index}" fill="{self.hex_color}"{rule} d="{d_attr}" />'
```

### `PlanarColorRegion.to_svg_element` — `Lines 58–86`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `86` (`Lines 58–86`)
- **الوظيفة:** Render this color region as a single compound <path> with fill-rule='evenodd'.
- **الكود الفعلي (`Lines 58–86`):**
```python
    def to_svg_element(self, use_bezier: bool = False) -> str:
        """Render this color region as a single compound <path> with fill-rule='evenodd'."""
        d_parts = []
        if use_bezier and self.bezier_subpaths:
            for sub in self.bezier_subpaths:
                if not sub:
                    continue
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))
        else:
            all_loops = self.outer_loops + self.hole_loops
            for loop in all_loops:
                if len(loop) < 3:
                    continue
                part = [f"M {loop[0][0]:.2f} {loop[0][1]:.2f}"]
                for pt in loop[1:]:
                    part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                part.append("Z")
                d_parts.append(" ".join(part))

        if not d_parts:
            return ""
        d_attr = " ".join(d_parts)
        rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
        return f'<path id="planar_c{self.color_index}" fill="{self.hex_color}"{rule} d="{d_attr}" />'
```

### `DualGridPlanarTracer` — `Lines 89–381`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `89` إلى السطر `381` (`Lines 89–381`)
- **الوظيفة:** Extracts exact shared-boundary planar tiling from a discrete label matrix.
- **الكود الفعلي (`Lines 89–381`):**
```python
class DualGridPlanarTracer:
    """Extracts exact shared-boundary planar tiling from a discrete label matrix."""

    def __init__(self, labels_img: np.ndarray, centers_bgr: np.ndarray, bg_color_index: int | None = None) -> None:
        self.labels = labels_img
        self.centers_bgr = centers_bgr
        self.H, self.W = labels_img.shape[:2]
        self.num_colors = len(centers_bgr)

        if bg_color_index is None:
            # Determine dominant background cluster by border occurrence or area
            border_pixels = np.concatenate([
                labels_img[0, :], labels_img[-1, :],
                labels_img[:, 0], labels_img[:, -1]
            ])
            counts = np.bincount(border_pixels, minlength=self.num_colors)
            self.bg_ci = int(np.argmax(counts))
        else:
            self.bg_ci = bg_color_index

    def extract_directed_cell_edges(self) -> dict[int, list[tuple[tuple[int, int], tuple[int, int]]]]:
        """Extracts directed interface edges for each color on the grid [0, W] x [0, H].
        
        A unit grid edge separates two pixel cells. Each edge is directed so that the
        region of that color is strictly on its LEFT in y-down screen coordinates.
        """
        pad = np.pad(self.labels, ((1, 1), (1, 1)), mode='constant', constant_values=-1)
        edges_by_color = defaultdict(list)

        # 1. Horizontal grid lines y in 0..H
        for y in range(self.H + 1):
            for x in range(self.W):
                c_above = pad[y, x + 1]      # cell at row y-1
                c_below = pad[y + 1, x + 1]  # cell at row y
                if c_above != c_below:
                    p_left = (x, y)
                    p_right = (x + 1, y)
                    # Walking RIGHT puts c_above on the LEFT
                    if c_above != -1:
                        edges_by_color[c_above].append((p_left, p_right))
                    # Walking LEFT puts c_below on the LEFT
                    if c_below != -1:
                        edges_by_color[c_below].append((p_right, p_left))

        # 2. Vertical grid lines x in 0..W
        for x in range(self.W + 1):
            for y in range(self.H):
                c_left = pad[y + 1, x]       # cell at col x-1
                c_right = pad[y + 1, x + 1]  # cell at col x
                if c_left != c_right:
                    p_top = (x, y)
                    p_bottom = (x, y + 1)
                    # Walking UP puts c_left on the LEFT
                    if c_left != -1:
                        edges_by_color[c_left].append((p_bottom, p_top))
                    # Walking DOWN puts c_right on the LEFT
                    if c_right != -1:
                        edges_by_color[c_right].append((p_top, p_bottom))

        return edges_by_color

    @staticmethod
    def assemble_closed_loops(edges: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[list[tuple[float, float]]]:
        """Assembles directed unit edges into closed simple polygonal loops without self-intersection."""
        if not edges:
            return []

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = set()
        loops = []

        for u, v in edges:
            if (u, v) in visited:
                continue

            loop = [u]
            curr_u, curr_v = u, v
            visited.add((curr_u, curr_v))

            while curr_v != u:
                loop.append(curr_v)
                cands = [nxt for nxt in adj[curr_v] if (curr_v, nxt) not in visited]
                if not cands:
                    break

                if len(cands) == 1:
                    nxt = cands[0]
                else:
                    # Resolve saddle points deterministically (prefer sharpest left turn to keep interior on left)
                    dx_in = curr_v[0] - curr_u[0]
                    dy_in = curr_v[1] - curr_u[1]

                    def turn_score(cand):
                        dx_out = cand[0] - curr_v[0]
                        dy_out = cand[1] - curr_v[1]
                        cross = dx_in * dy_out - dy_in * dx_out
                        dot = dx_in * dx_out + dy_in * dy_out
                        return np.arctan2(cross, dot)

                    cands.sort(key=turn_score)
                    nxt = cands[0]

                visited.add((curr_v, nxt))
                curr_u, curr_v = curr_v, nxt

            if curr_v == u and len(loop) >= 3:
                loops.append([(float(p[0]), float(p[1])) for p in loop])

        return loops

    @staticmethod
    def simplify_collinear_runs(loop: list[tuple[float, float]]) -> list[tuple[float, float]]:
        """Removes redundant intermediate points along straight orthogonal lines."""
        n = len(loop)
        if n < 3:
            return loop

        simplified = [loop[0]]
        for i in range(1, n):
            prev = simplified[-1]
            curr = loop[i]
            nxt = loop[(i + 1) % n]
            dx1 = curr[0] - prev[0]
            dy1 = curr[1] - prev[1]
            dx2 = nxt[0] - curr[0]
            dy2 = nxt[1] - curr[1]
            # Cross product == 0 and same direction
            if abs(dx1 * dy2 - dy1 * dx2) < 1e-5 and (dx1 * dx2 >= -1e-5 and dy1 * dy2 >= -1e-5):
                continue
            simplified.append(curr)

        # Check wrap-around
        if len(simplified) >= 3:
            dx1 = simplified[0][0] - simplified[-1][0]
            dy1 = simplified[0][1] - simplified[-1][1]
            dx2 = simplified[1][0] - simplified[0][0]
            dy2 = simplified[1][1] - simplified[0][1]
            if abs(dx1 * dy2 - dy1 * dx2) < 1e-5 and (dx1 * dx2 >= -1e-5 and dy1 * dy2 >= -1e-5):
                simplified = simplified[1:]

        return simplified

    @staticmethod
    def compute_signed_area(pts: list[tuple[float, float]]) -> float:
        """Computes polygon signed area using shoelace formula."""
        n = len(pts)
        if n < 3:
            return 0.0
        area2 = 0.0
        for i in range(n):
            j = (i + 1) % n
            area2 += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
        return area2 * 0.5

    def trace_planar_regions(self, simplify_collinear: bool = True, min_area: float = 1.0) -> list[PlanarColorRegion]:
        """Extracts all planar color regions as mutually exclusive compound polygons."""
        edges_by_color = self.extract_directed_cell_edges()
        regions: list[PlanarColorRegion] = []

        for ci in range(self.num_colors):
            b, g, r = self.centers_bgr[ci]
            hex_col = f"#{r:02x}{g:02x}{b:02x}"
            region = PlanarColorRegion(color_index=ci, hex_color=hex_col)

            raw_edges = edges_by_color.get(ci, [])
            if not raw_edges:
                regions.append(region)
                continue

            raw_loops = self.assemble_closed_loops(raw_edges)
            for loop in raw_loops:
                pts = self.simplify_collinear_runs(loop) if simplify_collinear else loop
                if len(pts) < 3:
                    continue
                s_area = self.compute_signed_area(pts)
                abs_area = abs(s_area)
                if abs_area < min_area:
                    continue

                # In y-down screen coordinates with interior on left:
                # Outer boundaries have negative signed area, holes have positive signed area
                if s_area < 0:
                    region.outer_loops.append(pts)
                else:
                    region.hole_loops.append(pts)

            regions.append(region)

        return regions

    def build_exact_planar_svg(self, regions: list[PlanarColorRegion], include_bg: bool = True) -> str:
        """Assembles exact planar regions into an SVG document with crispEdges and 0% bloat."""
        bg_b, bg_g, bg_r = self.centers_bgr[self.bg_ci]
        bg_hex = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"

        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}" shape-rendering="crispEdges">',
            f'  <desc>Geometry-Correct Planar Tiling (Exact Dual-Grid Shared Boundaries, Zero Bloat)</desc>',
        ]
        if include_bg:
            lines.append(f'  <rect width="{self.W}" height="{self.H}" fill="{bg_hex}" />')

        # Render foreground colors
        for reg in regions:
            if reg.color_index == self.bg_ci and include_bg:
                continue
            elem = reg.to_svg_element(use_bezier=False)
            if elem:
                lines.append(f"  {elem}")

        lines.append('</svg>')
        return "\n".join(lines)

    def fit_shared_arc_bezier(self, regions: list[PlanarColorRegion], epsilon_px: float = 0.5, max_nodes: int = 48) -> list[PlanarColorRegion]:
        """Fits cubic Bézier curves to closed loops while strictly preserving corner junctions."""
        for reg in regions:
            reg.bezier_subpaths = []
            all_loops = reg.outer_loops + reg.hole_loops
            for loop in all_loops:
                if len(loop) < 3:
                    continue
                pts = [Point2D(p[0], p[1]) for p in loop]
                segs = fit_schneider_bezier(pts, max_error_px=epsilon_px, max_nodes=max_nodes, closed=True)
                if segs:
                    reg.bezier_subpaths.append(segs)
        return regions

    def build_smooth_planar_svg(self, regions: list[PlanarColorRegion], stroke_width: float = 0.0, clip_to_silhouette: bool = True) -> str:
        """Assembles smooth Bézier planar SVG with optional master silhouette clipping to guarantee 0% bloat."""
        bg_b, bg_g, bg_r = self.centers_bgr[self.bg_ci]
        bg_hex = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"

        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}">',
            f'  <desc>Geometry-Correct Smooth Planar SVG (Silhouette-Clipped, Zero Bloat)</desc>',
        ]

        # Build master silhouette clip-path from exact foreground dual grid
        clip_def = ""
        if clip_to_silhouette:
            fg_d_parts = []
            for reg in regions:
                if reg.color_index == self.bg_ci:
                    continue
                for loop in reg.outer_loops:
                    if len(loop) < 3:
                        continue
                    part = [f"M {loop[0][0]:.2f} {loop[0][1]:.2f}"]
                    for pt in loop[1:]:
                        part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                    part.append("Z")
                    fg_d_parts.append(" ".join(part))
                for h_loop in reg.hole_loops:
                    if len(h_loop) < 3:
                        continue
                    part = [f"M {h_loop[0][0]:.2f} {h_loop[0][1]:.2f}"]
                    for pt in h_loop[1:]:
                        part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                    part.append("Z")
                    fg_d_parts.append(" ".join(part))

            if fg_d_parts:
                clip_d = " ".join(fg_d_parts)
                clip_def = (
                    "  <defs>\n"
                    f'    <clipPath id="master_silhouette_clip">\n'
                    f'      <path fill-rule="evenodd" d="{clip_d}" />\n'
                    "    </clipPath>\n"
                    "  </defs>"
                )
                lines.append(clip_def)

        lines.append(f'  <rect width="{self.W}" height="{self.H}" fill="{bg_hex}" />')

        group_open = '  <g clip-path="url(#master_silhouette_clip)">' if clip_to_silhouette and clip_def else '  <g id="planar_content">'
        lines.append(group_open)

        for reg in regions:
            if reg.color_index == self.bg_ci:
                continue
            elem = reg.to_svg_element(use_bezier=True)
            if elem:
                if stroke_width > 0.0:
                    # Apply internal stroke trapping safely inside the clipped group
                    elem = elem.replace('/>', f' stroke="{reg.hex_color}" stroke-width="{stroke_width:.1f}" stroke-linejoin="round" />')
                lines.append(f"    {elem}")

        lines.append('  </g>')
        lines.append('</svg>')
        return "\n".join(lines)
```

### `DualGridPlanarTracer.__init__` — `Lines 92–107`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `92` إلى السطر `107` (`Lines 92–107`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 92–107`):**
```python
    def __init__(self, labels_img: np.ndarray, centers_bgr: np.ndarray, bg_color_index: int | None = None) -> None:
        self.labels = labels_img
        self.centers_bgr = centers_bgr
        self.H, self.W = labels_img.shape[:2]
        self.num_colors = len(centers_bgr)

        if bg_color_index is None:
            # Determine dominant background cluster by border occurrence or area
            border_pixels = np.concatenate([
                labels_img[0, :], labels_img[-1, :],
                labels_img[:, 0], labels_img[:, -1]
            ])
            counts = np.bincount(border_pixels, minlength=self.num_colors)
            self.bg_ci = int(np.argmax(counts))
        else:
            self.bg_ci = bg_color_index
```

### `DualGridPlanarTracer.extract_directed_cell_edges` — `Lines 109–148`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `109` إلى السطر `148` (`Lines 109–148`)
- **الوظيفة:** Extracts directed interface edges for each color on the grid [0, W] x [0, H].
- **الكود الفعلي (`Lines 109–148`):**
```python
    def extract_directed_cell_edges(self) -> dict[int, list[tuple[tuple[int, int], tuple[int, int]]]]:
        """Extracts directed interface edges for each color on the grid [0, W] x [0, H].
        
        A unit grid edge separates two pixel cells. Each edge is directed so that the
        region of that color is strictly on its LEFT in y-down screen coordinates.
        """
        pad = np.pad(self.labels, ((1, 1), (1, 1)), mode='constant', constant_values=-1)
        edges_by_color = defaultdict(list)

        # 1. Horizontal grid lines y in 0..H
        for y in range(self.H + 1):
            for x in range(self.W):
                c_above = pad[y, x + 1]      # cell at row y-1
                c_below = pad[y + 1, x + 1]  # cell at row y
                if c_above != c_below:
                    p_left = (x, y)
                    p_right = (x + 1, y)
                    # Walking RIGHT puts c_above on the LEFT
                    if c_above != -1:
                        edges_by_color[c_above].append((p_left, p_right))
                    # Walking LEFT puts c_below on the LEFT
                    if c_below != -1:
                        edges_by_color[c_below].append((p_right, p_left))

        # 2. Vertical grid lines x in 0..W
        for x in range(self.W + 1):
            for y in range(self.H):
                c_left = pad[y + 1, x]       # cell at col x-1
                c_right = pad[y + 1, x + 1]  # cell at col x
                if c_left != c_right:
                    p_top = (x, y)
                    p_bottom = (x, y + 1)
                    # Walking UP puts c_left on the LEFT
                    if c_left != -1:
                        edges_by_color[c_left].append((p_bottom, p_top))
                    # Walking DOWN puts c_right on the LEFT
                    if c_right != -1:
                        edges_by_color[c_right].append((p_top, p_bottom))

        return edges_by_color
```

### `DualGridPlanarTracer.assemble_closed_loops` — `Lines 151–200`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `151` إلى السطر `200` (`Lines 151–200`)
- **الوظيفة:** Assembles directed unit edges into closed simple polygonal loops without self-intersection.
- **الكود الفعلي (`Lines 151–200`):**
```python
    def assemble_closed_loops(edges: list[tuple[tuple[int, int], tuple[int, int]]]) -> list[list[tuple[float, float]]]:
        """Assembles directed unit edges into closed simple polygonal loops without self-intersection."""
        if not edges:
            return []

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        visited = set()
        loops = []

        for u, v in edges:
            if (u, v) in visited:
                continue

            loop = [u]
            curr_u, curr_v = u, v
            visited.add((curr_u, curr_v))

            while curr_v != u:
                loop.append(curr_v)
                cands = [nxt for nxt in adj[curr_v] if (curr_v, nxt) not in visited]
                if not cands:
                    break

                if len(cands) == 1:
                    nxt = cands[0]
                else:
                    # Resolve saddle points deterministically (prefer sharpest left turn to keep interior on left)
                    dx_in = curr_v[0] - curr_u[0]
                    dy_in = curr_v[1] - curr_u[1]

                    def turn_score(cand):
                        dx_out = cand[0] - curr_v[0]
                        dy_out = cand[1] - curr_v[1]
                        cross = dx_in * dy_out - dy_in * dx_out
                        dot = dx_in * dx_out + dy_in * dy_out
                        return np.arctan2(cross, dot)

                    cands.sort(key=turn_score)
                    nxt = cands[0]

                visited.add((curr_v, nxt))
                curr_u, curr_v = curr_v, nxt

            if curr_v == u and len(loop) >= 3:
                loops.append([(float(p[0]), float(p[1])) for p in loop])

        return loops
```

### `DualGridPlanarTracer.simplify_collinear_runs` — `Lines 203–232`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `203` إلى السطر `232` (`Lines 203–232`)
- **الوظيفة:** Removes redundant intermediate points along straight orthogonal lines.
- **الكود الفعلي (`Lines 203–232`):**
```python
    def simplify_collinear_runs(loop: list[tuple[float, float]]) -> list[tuple[float, float]]:
        """Removes redundant intermediate points along straight orthogonal lines."""
        n = len(loop)
        if n < 3:
            return loop

        simplified = [loop[0]]
        for i in range(1, n):
            prev = simplified[-1]
            curr = loop[i]
            nxt = loop[(i + 1) % n]
            dx1 = curr[0] - prev[0]
            dy1 = curr[1] - prev[1]
            dx2 = nxt[0] - curr[0]
            dy2 = nxt[1] - curr[1]
            # Cross product == 0 and same direction
            if abs(dx1 * dy2 - dy1 * dx2) < 1e-5 and (dx1 * dx2 >= -1e-5 and dy1 * dy2 >= -1e-5):
                continue
            simplified.append(curr)

        # Check wrap-around
        if len(simplified) >= 3:
            dx1 = simplified[0][0] - simplified[-1][0]
            dy1 = simplified[0][1] - simplified[-1][1]
            dx2 = simplified[1][0] - simplified[0][0]
            dy2 = simplified[1][1] - simplified[0][1]
            if abs(dx1 * dy2 - dy1 * dx2) < 1e-5 and (dx1 * dx2 >= -1e-5 and dy1 * dy2 >= -1e-5):
                simplified = simplified[1:]

        return simplified
```

### `DualGridPlanarTracer.compute_signed_area` — `Lines 235–244`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `235` إلى السطر `244` (`Lines 235–244`)
- **الوظيفة:** Computes polygon signed area using shoelace formula.
- **الكود الفعلي (`Lines 235–244`):**
```python
    def compute_signed_area(pts: list[tuple[float, float]]) -> float:
        """Computes polygon signed area using shoelace formula."""
        n = len(pts)
        if n < 3:
            return 0.0
        area2 = 0.0
        for i in range(n):
            j = (i + 1) % n
            area2 += pts[i][0] * pts[j][1] - pts[j][0] * pts[i][1]
        return area2 * 0.5
```

### `DualGridPlanarTracer.trace_planar_regions` — `Lines 246–280`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `246` إلى السطر `280` (`Lines 246–280`)
- **الوظيفة:** Extracts all planar color regions as mutually exclusive compound polygons.
- **الكود الفعلي (`Lines 246–280`):**
```python
    def trace_planar_regions(self, simplify_collinear: bool = True, min_area: float = 1.0) -> list[PlanarColorRegion]:
        """Extracts all planar color regions as mutually exclusive compound polygons."""
        edges_by_color = self.extract_directed_cell_edges()
        regions: list[PlanarColorRegion] = []

        for ci in range(self.num_colors):
            b, g, r = self.centers_bgr[ci]
            hex_col = f"#{r:02x}{g:02x}{b:02x}"
            region = PlanarColorRegion(color_index=ci, hex_color=hex_col)

            raw_edges = edges_by_color.get(ci, [])
            if not raw_edges:
                regions.append(region)
                continue

            raw_loops = self.assemble_closed_loops(raw_edges)
            for loop in raw_loops:
                pts = self.simplify_collinear_runs(loop) if simplify_collinear else loop
                if len(pts) < 3:
                    continue
                s_area = self.compute_signed_area(pts)
                abs_area = abs(s_area)
                if abs_area < min_area:
                    continue

                # In y-down screen coordinates with interior on left:
                # Outer boundaries have negative signed area, holes have positive signed area
                if s_area < 0:
                    region.outer_loops.append(pts)
                else:
                    region.hole_loops.append(pts)

            regions.append(region)

        return regions
```

### `DualGridPlanarTracer.build_exact_planar_svg` — `Lines 282–303`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `282` إلى السطر `303` (`Lines 282–303`)
- **الوظيفة:** Assembles exact planar regions into an SVG document with crispEdges and 0% bloat.
- **الكود الفعلي (`Lines 282–303`):**
```python
    def build_exact_planar_svg(self, regions: list[PlanarColorRegion], include_bg: bool = True) -> str:
        """Assembles exact planar regions into an SVG document with crispEdges and 0% bloat."""
        bg_b, bg_g, bg_r = self.centers_bgr[self.bg_ci]
        bg_hex = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"

        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}" shape-rendering="crispEdges">',
            f'  <desc>Geometry-Correct Planar Tiling (Exact Dual-Grid Shared Boundaries, Zero Bloat)</desc>',
        ]
        if include_bg:
            lines.append(f'  <rect width="{self.W}" height="{self.H}" fill="{bg_hex}" />')

        # Render foreground colors
        for reg in regions:
            if reg.color_index == self.bg_ci and include_bg:
                continue
            elem = reg.to_svg_element(use_bezier=False)
            if elem:
                lines.append(f"  {elem}")

        lines.append('</svg>')
        return "\n".join(lines)
```

### `DualGridPlanarTracer.fit_shared_arc_bezier` — `Lines 305–317`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `305` إلى السطر `317` (`Lines 305–317`)
- **الوظيفة:** Fits cubic Bézier curves to closed loops while strictly preserving corner junctions.
- **الكود الفعلي (`Lines 305–317`):**
```python
    def fit_shared_arc_bezier(self, regions: list[PlanarColorRegion], epsilon_px: float = 0.5, max_nodes: int = 48) -> list[PlanarColorRegion]:
        """Fits cubic Bézier curves to closed loops while strictly preserving corner junctions."""
        for reg in regions:
            reg.bezier_subpaths = []
            all_loops = reg.outer_loops + reg.hole_loops
            for loop in all_loops:
                if len(loop) < 3:
                    continue
                pts = [Point2D(p[0], p[1]) for p in loop]
                segs = fit_schneider_bezier(pts, max_error_px=epsilon_px, max_nodes=max_nodes, closed=True)
                if segs:
                    reg.bezier_subpaths.append(segs)
        return regions
```

### `DualGridPlanarTracer.build_smooth_planar_svg` — `Lines 319–381`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `319` إلى السطر `381` (`Lines 319–381`)
- **الوظيفة:** Assembles smooth Bézier planar SVG with optional master silhouette clipping to guarantee 0% bloat.
- **الكود الفعلي (`Lines 319–381`):**
```python
    def build_smooth_planar_svg(self, regions: list[PlanarColorRegion], stroke_width: float = 0.0, clip_to_silhouette: bool = True) -> str:
        """Assembles smooth Bézier planar SVG with optional master silhouette clipping to guarantee 0% bloat."""
        bg_b, bg_g, bg_r = self.centers_bgr[self.bg_ci]
        bg_hex = f"#{bg_r:02x}{bg_g:02x}{bg_b:02x}"

        lines = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.W} {self.H}" width="{self.W}" height="{self.H}">',
            f'  <desc>Geometry-Correct Smooth Planar SVG (Silhouette-Clipped, Zero Bloat)</desc>',
        ]

        # Build master silhouette clip-path from exact foreground dual grid
        clip_def = ""
        if clip_to_silhouette:
            fg_d_parts = []
            for reg in regions:
                if reg.color_index == self.bg_ci:
                    continue
                for loop in reg.outer_loops:
                    if len(loop) < 3:
                        continue
                    part = [f"M {loop[0][0]:.2f} {loop[0][1]:.2f}"]
                    for pt in loop[1:]:
                        part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                    part.append("Z")
                    fg_d_parts.append(" ".join(part))
                for h_loop in reg.hole_loops:
                    if len(h_loop) < 3:
                        continue
                    part = [f"M {h_loop[0][0]:.2f} {h_loop[0][1]:.2f}"]
                    for pt in h_loop[1:]:
                        part.append(f"L {pt[0]:.2f} {pt[1]:.2f}")
                    part.append("Z")
                    fg_d_parts.append(" ".join(part))

            if fg_d_parts:
                clip_d = " ".join(fg_d_parts)
                clip_def = (
                    "  <defs>\n"
                    f'    <clipPath id="master_silhouette_clip">\n'
                    f'      <path fill-rule="evenodd" d="{clip_d}" />\n'
                    "    </clipPath>\n"
                    "  </defs>"
                )
                lines.append(clip_def)

        lines.append(f'  <rect width="{self.W}" height="{self.H}" fill="{bg_hex}" />')

        group_open = '  <g clip-path="url(#master_silhouette_clip)">' if clip_to_silhouette and clip_def else '  <g id="planar_content">'
        lines.append(group_open)

        for reg in regions:
            if reg.color_index == self.bg_ci:
                continue
            elem = reg.to_svg_element(use_bezier=True)
            if elem:
                if stroke_width > 0.0:
                    # Apply internal stroke trapping safely inside the clipped group
                    elem = elem.replace('/>', f' stroke="{reg.hex_color}" stroke-width="{stroke_width:.1f}" stroke-linejoin="round" />')
                lines.append(f"    {elem}")

        lines.append('  </g>')
        lines.append('</svg>')
        return "\n".join(lines)
```
