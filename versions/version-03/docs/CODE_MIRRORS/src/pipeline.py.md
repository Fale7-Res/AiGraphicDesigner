# مرآة الكود التفصيلية للإصدار: `version-03/src/pipeline.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-03/src/pipeline.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-03`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/pipeline.py`
- **الإصدار المعماري (`Architecture Version`):** `version-03`
- **إجمالي عدد الأسطر (`Total Lines`):** `91` (`Lines 1–91`)
- **بصمة الملف (`SHA-256`):** `9ac0090a52d2d35971cb45dffbe08ce39f86de5383e12f59ae08f426458f706f`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-03`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-03` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `DualPathTypographyLayer` | `class` | `Lines 17–46` | `class DualPathTypographyLayer:` | Represents a typographic layer with dual-path visual and editable representations. |
| `DualPathTypographyLayer.render_exact_outline_svg` | `method` | `Lines 27–36` | `def render_exact_outline_svg(self) -> str:` | Render Path 1: exact Bézier outlines. |
| `DualPathTypographyLayer.render_editable_text_svg` | `method` | `Lines 38–46` | `def render_editable_text_svg(self, x: float = 100.0, y: float = 100.0) -> str:` | Render Path 2: editable text SVG element. |
| `DualPathTypographyPipeline` | `class` | `Lines 49–90` | `class DualPathTypographyPipeline:` | Version 03 pipeline combining latent attention decomposition and dual-path typography. |
| `DualPathTypographyPipeline.__init__` | `method` | `Lines 52–53` | `def __init__(self, default_font_fallback: str = "Cairo") -> None:` | رمز برمجي موثق للإصدار. |
| `DualPathTypographyPipeline.create_typography_layer` | `method` | `Lines 55–74` | `def create_typography_layer(` | Construct a dual-path typography layer. |
| `DualPathTypographyPipeline.export_dual_path_svg` | `method` | `Lines 76–90` | `def export_dual_path_svg(self, layers: list[DualPathTypographyLayer], width: int = 2048, height: int = 2048) -> str:` | Compile SVG document containing both vector outline and editable text layers. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `DualPathTypographyLayer` — `Lines 17–46`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `46` (`Lines 17–46`)
- **الوظيفة:** Represents a typographic layer with dual-path visual and editable representations.
- **الكود الفعلي (`Lines 17–46`):**
```python
class DualPathTypographyLayer:
    """Represents a typographic layer with dual-path visual and editable representations."""
    layer_id: str
    text_content: str
    matched_font_family: str
    font_weight: str
    font_size_pt: float
    fill_color_hex: str
    outline_segments: list[CalligraphicBezierSegment] = field(default_factory=list)

    def render_exact_outline_svg(self) -> str:
        """Render Path 1: exact Bézier outlines."""
        if not self.outline_segments:
            return ""
        start = self.outline_segments[0].p0
        d_parts = [f"M {start.x:.2f} {start.y:.2f}"]
        for seg in self.outline_segments:
            d_parts.append(seg.to_svg_cubic_path())
        d_parts.append("Z")
        return f'<path id="{self.layer_id}_outline" fill="{self.fill_color_hex}" d="{" ".join(d_parts)}" />'

    def render_editable_text_svg(self, x: float = 100.0, y: float = 100.0) -> str:
        """Render Path 2: editable text SVG element."""
        return (
            f'<text id="{self.layer_id}_editable" x="{x:.2f}" y="{y:.2f}" '
            f'font-family="{self.matched_font_family}, sans-serif" font-weight="{self.font_weight}" '
            f'font-size="{self.font_size_pt}pt" fill="{self.fill_color_hex}" direction="rtl">'
            f'{self.text_content}'
            f'</text>'
        )
```

### `DualPathTypographyLayer.render_exact_outline_svg` — `Lines 27–36`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `36` (`Lines 27–36`)
- **الوظيفة:** Render Path 1: exact Bézier outlines.
- **الكود الفعلي (`Lines 27–36`):**
```python
    def render_exact_outline_svg(self) -> str:
        """Render Path 1: exact Bézier outlines."""
        if not self.outline_segments:
            return ""
        start = self.outline_segments[0].p0
        d_parts = [f"M {start.x:.2f} {start.y:.2f}"]
        for seg in self.outline_segments:
            d_parts.append(seg.to_svg_cubic_path())
        d_parts.append("Z")
        return f'<path id="{self.layer_id}_outline" fill="{self.fill_color_hex}" d="{" ".join(d_parts)}" />'
```

### `DualPathTypographyLayer.render_editable_text_svg` — `Lines 38–46`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `38` إلى السطر `46` (`Lines 38–46`)
- **الوظيفة:** Render Path 2: editable text SVG element.
- **الكود الفعلي (`Lines 38–46`):**
```python
    def render_editable_text_svg(self, x: float = 100.0, y: float = 100.0) -> str:
        """Render Path 2: editable text SVG element."""
        return (
            f'<text id="{self.layer_id}_editable" x="{x:.2f}" y="{y:.2f}" '
            f'font-family="{self.matched_font_family}, sans-serif" font-weight="{self.font_weight}" '
            f'font-size="{self.font_size_pt}pt" fill="{self.fill_color_hex}" direction="rtl">'
            f'{self.text_content}'
            f'</text>'
        )
```

### `DualPathTypographyPipeline` — `Lines 49–90`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `90` (`Lines 49–90`)
- **الوظيفة:** Version 03 pipeline combining latent attention decomposition and dual-path typography.
- **الكود الفعلي (`Lines 49–90`):**
```python
class DualPathTypographyPipeline:
    """Version 03 pipeline combining latent attention decomposition and dual-path typography."""

    def __init__(self, default_font_fallback: str = "Cairo") -> None:
        self.default_font_fallback = default_font_fallback

    def create_typography_layer(
        self,
        layer_id: str,
        text: str,
        font_family: str,
        contour_points: list[tuple[float, float]],
        fill_hex: str = "#1A1A1A",
    ) -> DualPathTypographyLayer:
        """Construct a dual-path typography layer."""
        pts = [TypographicPoint(x=p[0], y=p[1]) for p in contour_points]
        fitted_segs = fit_typographic_bezier(pts)
        return DualPathTypographyLayer(
            layer_id=layer_id,
            text_content=text,
            matched_font_family=font_family or self.default_font_fallback,
            font_weight="bold",
            font_size_pt=36.0,
            fill_color_hex=fill_hex,
            outline_segments=fitted_segs,
        )

    def export_dual_path_svg(self, layers: list[DualPathTypographyLayer], width: int = 2048, height: int = 2048) -> str:
        """Compile SVG document containing both vector outline and editable text layers."""
        outlines = "\n    ".join(l.render_exact_outline_svg() for l in layers)
        editable = "\n    ".join(l.render_editable_text_svg() for l in layers)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
            f'  <desc>Generated by AI Graphic Designer version-03 (Dual-Path Typography)</desc>\n'
            f'  <g id="visual_outlines_layer">\n'
            f'    {outlines}\n'
            f'  </g>\n'
            f'  <g id="editable_text_layer" opacity="0.0">\n'
            f'    {editable}\n'
            f'  </g>\n'
            f'</svg>'
        )
```

### `DualPathTypographyPipeline.__init__` — `Lines 52–53`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `52` إلى السطر `53` (`Lines 52–53`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 52–53`):**
```python
    def __init__(self, default_font_fallback: str = "Cairo") -> None:
        self.default_font_fallback = default_font_fallback
```

### `DualPathTypographyPipeline.create_typography_layer` — `Lines 55–74`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `55` إلى السطر `74` (`Lines 55–74`)
- **الوظيفة:** Construct a dual-path typography layer.
- **الكود الفعلي (`Lines 55–74`):**
```python
    def create_typography_layer(
        self,
        layer_id: str,
        text: str,
        font_family: str,
        contour_points: list[tuple[float, float]],
        fill_hex: str = "#1A1A1A",
    ) -> DualPathTypographyLayer:
        """Construct a dual-path typography layer."""
        pts = [TypographicPoint(x=p[0], y=p[1]) for p in contour_points]
        fitted_segs = fit_typographic_bezier(pts)
        return DualPathTypographyLayer(
            layer_id=layer_id,
            text_content=text,
            matched_font_family=font_family or self.default_font_fallback,
            font_weight="bold",
            font_size_pt=36.0,
            fill_color_hex=fill_hex,
            outline_segments=fitted_segs,
        )
```

### `DualPathTypographyPipeline.export_dual_path_svg` — `Lines 76–90`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `76` إلى السطر `90` (`Lines 76–90`)
- **الوظيفة:** Compile SVG document containing both vector outline and editable text layers.
- **الكود الفعلي (`Lines 76–90`):**
```python
    def export_dual_path_svg(self, layers: list[DualPathTypographyLayer], width: int = 2048, height: int = 2048) -> str:
        """Compile SVG document containing both vector outline and editable text layers."""
        outlines = "\n    ".join(l.render_exact_outline_svg() for l in layers)
        editable = "\n    ".join(l.render_editable_text_svg() for l in layers)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
            f'  <desc>Generated by AI Graphic Designer version-03 (Dual-Path Typography)</desc>\n'
            f'  <g id="visual_outlines_layer">\n'
            f'    {outlines}\n'
            f'  </g>\n'
            f'  <g id="editable_text_layer" opacity="0.0">\n'
            f'    {editable}\n'
            f'  </g>\n'
            f'</svg>'
        )
```
