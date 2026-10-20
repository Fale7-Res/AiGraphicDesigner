# مرآة الكود التفصيلية للإصدار: `version-02/src/geometry/bezier.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-02/src/geometry/bezier.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-02`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/geometry/bezier.py`
- **الإصدار المعماري (`Architecture Version`):** `version-02`
- **إجمالي عدد الأسطر (`Total Lines`):** `72` (`Lines 1–72`)
- **بصمة الملف (`SHA-256`):** `8c5e89b1d82cfc800fb42eae8644c8c1218bbe2289cdce1722923c9fc11b3e80`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-02`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-02` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `VectorPoint` | `class` | `Lines 12–19` | `class VectorPoint:` | Represents a 2D position vector in canvas coordinate space. |
| `VectorPoint.distance_to` | `method` | `Lines 17–19` | `def distance_to(self, other: "VectorPoint") -> float:` | Compute Euclidean distance to another point. |
| `OptimizedBezierSegment` | `class` | `Lines 23–45` | `class OptimizedBezierSegment:` | Cubic Bézier segment with explicit in/out pen tool handles. |
| `OptimizedBezierSegment.evaluate_at` | `method` | `Lines 30–41` | `def evaluate_at(self, t: float) -> VectorPoint:` | Evaluate the cubic curve at parameter t in [0.0, 1.0]. |
| `OptimizedBezierSegment.to_svg_cubic_command` | `method` | `Lines 43–45` | `def to_svg_cubic_command(self) -> str:` | Format as standard SVG C command. |
| `fit_smooth_curve` | `function` | `Lines 48–71` | `def fit_smooth_curve(points: list[VectorPoint], max_nodes: int = 36) -> list[OptimizedBezierSegment]:` | Fit a series of points into smooth cubic Bézier segments enforcing maximum node budget. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `VectorPoint` — `Lines 12–19`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `19` (`Lines 12–19`)
- **الوظيفة:** Represents a 2D position vector in canvas coordinate space.
- **الكود الفعلي (`Lines 12–19`):**
```python
class VectorPoint:
    """Represents a 2D position vector in canvas coordinate space."""
    x: float
    y: float

    def distance_to(self, other: "VectorPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `VectorPoint.distance_to` — `Lines 17–19`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `19` (`Lines 17–19`)
- **الوظيفة:** Compute Euclidean distance to another point.
- **الكود الفعلي (`Lines 17–19`):**
```python
    def distance_to(self, other: "VectorPoint") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `OptimizedBezierSegment` — `Lines 23–45`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `45` (`Lines 23–45`)
- **الوظيفة:** Cubic Bézier segment with explicit in/out pen tool handles.
- **الكود الفعلي (`Lines 23–45`):**
```python
class OptimizedBezierSegment:
    """Cubic Bézier segment with explicit in/out pen tool handles."""
    anchor_start: VectorPoint
    handle_out: VectorPoint
    handle_in: VectorPoint
    anchor_end: VectorPoint

    def evaluate_at(self, t: float) -> VectorPoint:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.anchor_start.x +
             3.0 * u**2 * t * self.handle_out.x +
             3.0 * u * t**2 * self.handle_in.x +
             t**3 * self.anchor_end.x)
        y = (u**3 * self.anchor_start.y +
             3.0 * u**2 * t * self.handle_out.y +
             3.0 * u * t**2 * self.handle_in.y +
             t**3 * self.anchor_end.y)
        return VectorPoint(x=x, y=y)

    def to_svg_cubic_command(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.handle_out.x:.2f} {self.handle_out.y:.2f}, {self.handle_in.x:.2f} {self.handle_in.y:.2f}, {self.anchor_end.x:.2f} {self.anchor_end.y:.2f}"
```

### `OptimizedBezierSegment.evaluate_at` — `Lines 30–41`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `41` (`Lines 30–41`)
- **الوظيفة:** Evaluate the cubic curve at parameter t in [0.0, 1.0].
- **الكود الفعلي (`Lines 30–41`):**
```python
    def evaluate_at(self, t: float) -> VectorPoint:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.anchor_start.x +
             3.0 * u**2 * t * self.handle_out.x +
             3.0 * u * t**2 * self.handle_in.x +
             t**3 * self.anchor_end.x)
        y = (u**3 * self.anchor_start.y +
             3.0 * u**2 * t * self.handle_out.y +
             3.0 * u * t**2 * self.handle_in.y +
             t**3 * self.anchor_end.y)
        return VectorPoint(x=x, y=y)
```

### `OptimizedBezierSegment.to_svg_cubic_command` — `Lines 43–45`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `43` إلى السطر `45` (`Lines 43–45`)
- **الوظيفة:** Format as standard SVG C command.
- **الكود الفعلي (`Lines 43–45`):**
```python
    def to_svg_cubic_command(self) -> str:
        """Format as standard SVG C command."""
        return f"C {self.handle_out.x:.2f} {self.handle_out.y:.2f}, {self.handle_in.x:.2f} {self.handle_in.y:.2f}, {self.anchor_end.x:.2f} {self.anchor_end.y:.2f}"
```

### `fit_smooth_curve` — `Lines 48–71`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `71` (`Lines 48–71`)
- **الوظيفة:** Fit a series of points into smooth cubic Bézier segments enforcing maximum node budget.
- **الكود الفعلي (`Lines 48–71`):**
```python
def fit_smooth_curve(points: list[VectorPoint], max_nodes: int = 36) -> list[OptimizedBezierSegment]:
    """Fit a series of points into smooth cubic Bézier segments enforcing maximum node budget."""
    if len(points) < 2:
        return []
    segments: list[OptimizedBezierSegment] = []
    step = max(1, len(points) // max_nodes)
    subsampled = points[::step]
    if subsampled[-1] != points[-1]:
        subsampled.append(points[-1])

    for i in range(len(subsampled) - 1):
        p0 = subsampled[i]
        p3 = subsampled[i + 1]
        dx = (p3.x - p0.x) / 3.0
        dy = (p3.y - p0.y) / 3.0
        h_out = VectorPoint(x=p0.x + dx, y=p0.y + dy)
        h_in = VectorPoint(x=p3.x - dx, y=p3.y - dy)
        segments.append(OptimizedBezierSegment(
            anchor_start=p0,
            handle_out=h_out,
            handle_in=h_in,
            anchor_end=p3,
        ))
    return segments
```
