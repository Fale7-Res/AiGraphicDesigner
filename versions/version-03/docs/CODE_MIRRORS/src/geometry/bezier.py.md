# مرآة الكود التفصيلية للإصدار: `version-03/src/geometry/bezier.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-03/src/geometry/bezier.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-03`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/geometry/bezier.py`
- **الإصدار المعماري (`Architecture Version`):** `version-03`
- **إجمالي عدد الأسطر (`Total Lines`):** `59` (`Lines 1–59`)
- **بصمة الملف (`SHA-256`):** `43ff7a492e02813fed10fe2a8490b4bbfe97ebf173b2e8c00fb93a898a92a4fc`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-03`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-03` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `TypographicPoint` | `class` | `Lines 12–20` | `class TypographicPoint:` | Represents a contour point on a glyph or typographic path. |
| `TypographicPoint.distance_to` | `method` | `Lines 18–20` | `def distance_to(self, other: "TypographicPoint") -> float:` | Compute Euclidean distance to another point. |
| `CalligraphicBezierSegment` | `class` | `Lines 24–33` | `class CalligraphicBezierSegment:` | Cubic Bézier segment optimized for calligraphic curvature. |
| `CalligraphicBezierSegment.to_svg_cubic_path` | `method` | `Lines 31–33` | `def to_svg_cubic_path(self) -> str:` | Format as standard SVG C command. |
| `fit_typographic_bezier` | `function` | `Lines 36–58` | `def fit_typographic_bezier(points: list[TypographicPoint], error_tolerance_px: float = 1.0) -> list[CalligraphicBezierSegment]:` | Fit typographic contour points into cubic Bézier segments preserving corner sharpness. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `TypographicPoint` — `Lines 12–20`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `20` (`Lines 12–20`)
- **الوظيفة:** Represents a contour point on a glyph or typographic path.
- **الكود الفعلي (`Lines 12–20`):**
```python
class TypographicPoint:
    """Represents a contour point on a glyph or typographic path."""
    x: float
    y: float
    is_corner: bool = False

    def distance_to(self, other: "TypographicPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `TypographicPoint.distance_to` — `Lines 18–20`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `20` (`Lines 18–20`)
- **الوظيفة:** Compute Euclidean distance to another point.
- **الكود الفعلي (`Lines 18–20`):**
```python
    def distance_to(self, other: "TypographicPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `CalligraphicBezierSegment` — `Lines 24–33`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `33` (`Lines 24–33`)
- **الوظيفة:** Cubic Bézier segment optimized for calligraphic curvature.
- **الكود الفعلي (`Lines 24–33`):**
```python
class CalligraphicBezierSegment:
    """Cubic Bézier segment optimized for calligraphic curvature."""
    p0: TypographicPoint
    p1: TypographicPoint
    p2: TypographicPoint
    p3: TypographicPoint

    def to_svg_cubic_path(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"
```

### `CalligraphicBezierSegment.to_svg_cubic_path` — `Lines 31–33`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `33` (`Lines 31–33`)
- **الوظيفة:** Format as standard SVG C command.
- **الكود الفعلي (`Lines 31–33`):**
```python
    def to_svg_cubic_path(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"
```

### `fit_typographic_bezier` — `Lines 36–58`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `58` (`Lines 36–58`)
- **الوظيفة:** Fit typographic contour points into cubic Bézier segments preserving corner sharpness.
- **الكود الفعلي (`Lines 36–58`):**
```python
def fit_typographic_bezier(points: list[TypographicPoint], error_tolerance_px: float = 1.0) -> list[CalligraphicBezierSegment]:
    """Fit typographic contour points into cubic Bézier segments preserving corner sharpness."""
    if len(points) < 2:
        return []
    segments: list[CalligraphicBezierSegment] = []
    # Identify corner breakpoints or partition uniformly
    indices = [0]
    for idx in range(1, len(points) - 1):
        if points[idx].is_corner:
            indices.append(idx)
    indices.append(len(points) - 1)

    for i in range(len(indices) - 1):
        start_idx = indices[i]
        end_idx = indices[i + 1]
        p_start = points[start_idx]
        p_end = points[end_idx]
        dx = (p_end.x - p_start.x) / 3.0
        dy = (p_end.y - p_start.y) / 3.0
        p1 = TypographicPoint(x=p_start.x + dx, y=p_start.y + dy)
        p2 = TypographicPoint(x=p_end.x - dx, y=p_end.y - dy)
        segments.append(CalligraphicBezierSegment(p0=p_start, p1=p1, p2=p2, p3=p_end))
    return segments
```
