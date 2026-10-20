# مرآة الكود التفصيلية للإصدار: `version-01/src/geometry/bezier.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/src/geometry/bezier.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/geometry/bezier.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `144` (`Lines 1–144`)
- **بصمة الملف (`SHA-256`):** `0227ff347e0cb9e5f41ba3756d369502481e2f43720d94f1ad14136426131511`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `Point2D` | `class` | `Lines 14–21` | `class Point2D:` | Represents a 2D coordinate point. |
| `Point2D.distance_to` | `method` | `Lines 19–21` | `def distance_to(self, other: "Point2D") -> float:` | Compute Euclidean distance to another point. |
| `BezierSegment` | `class` | `Lines 25–47` | `class BezierSegment:` | Cubic Bézier curve segment defined by start, two control points, and end. |
| `BezierSegment.evaluate` | `method` | `Lines 32–43` | `def evaluate(self, t: float) -> Point2D:` | Evaluate the cubic curve at parameter t in [0.0, 1.0]. |
| `BezierSegment.to_svg_path_data` | `method` | `Lines 45–47` | `def to_svg_path_data(self) -> str:` | Format cubic Bézier segment as SVG C command. |
| `fit_schneider_bezier` | `function` | `Lines 50–142` | `def fit_schneider_bezier(` | Fit a series of digitized points with cubic Bézier segments preserving sharp corners and fidelity. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `Point2D` — `Lines 14–21`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `21` (`Lines 14–21`)
- **الوظيفة:** Represents a 2D coordinate point.
- **الكود الفعلي (`Lines 14–21`):**
```python
class Point2D:
    """Represents a 2D coordinate point."""
    x: float
    y: float

    def distance_to(self, other: "Point2D") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `Point2D.distance_to` — `Lines 19–21`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `21` (`Lines 19–21`)
- **الوظيفة:** Compute Euclidean distance to another point.
- **الكود الفعلي (`Lines 19–21`):**
```python
    def distance_to(self, other: "Point2D") -> float:
        """Compute Euclidean distance to another point."""
        return math.hypot(self.x - other.x, self.y - other.y)
```

### `BezierSegment` — `Lines 25–47`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `47` (`Lines 25–47`)
- **الوظيفة:** Cubic Bézier curve segment defined by start, two control points, and end.
- **الكود الفعلي (`Lines 25–47`):**
```python
class BezierSegment:
    """Cubic Bézier curve segment defined by start, two control points, and end."""
    p0: Point2D
    p1: Point2D
    p2: Point2D
    p3: Point2D

    def evaluate(self, t: float) -> Point2D:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.p0.x +
             3.0 * u**2 * t * self.p1.x +
             3.0 * u * t**2 * self.p2.x +
             t**3 * self.p3.x)
        y = (u**3 * self.p0.y +
             3.0 * u**2 * t * self.p1.y +
             3.0 * u * t**2 * self.p2.y +
             t**3 * self.p3.y)
        return Point2D(x=x, y=y)

    def to_svg_path_data(self) -> str:
        """Format cubic Bézier segment as SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"
```

### `BezierSegment.evaluate` — `Lines 32–43`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `32` إلى السطر `43` (`Lines 32–43`)
- **الوظيفة:** Evaluate the cubic curve at parameter t in [0.0, 1.0].
- **الكود الفعلي (`Lines 32–43`):**
```python
    def evaluate(self, t: float) -> Point2D:
        """Evaluate the cubic curve at parameter t in [0.0, 1.0]."""
        u = 1.0 - t
        x = (u**3 * self.p0.x +
             3.0 * u**2 * t * self.p1.x +
             3.0 * u * t**2 * self.p2.x +
             t**3 * self.p3.x)
        y = (u**3 * self.p0.y +
             3.0 * u**2 * t * self.p1.y +
             3.0 * u * t**2 * self.p2.y +
             t**3 * self.p3.y)
        return Point2D(x=x, y=y)
```

### `BezierSegment.to_svg_path_data` — `Lines 45–47`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `47` (`Lines 45–47`)
- **الوظيفة:** Format cubic Bézier segment as SVG C command.
- **الكود الفعلي (`Lines 45–47`):**
```python
    def to_svg_path_data(self) -> str:
        """Format cubic Bézier segment as SVG C command."""
        return f"C {self.p1.x:.2f} {self.p1.y:.2f}, {self.p2.x:.2f} {self.p2.y:.2f}, {self.p3.x:.2f} {self.p3.y:.2f}"
```

### `fit_schneider_bezier` — `Lines 50–142`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `142` (`Lines 50–142`)
- **الوظيفة:** Fit a series of digitized points with cubic Bézier segments preserving sharp corners and fidelity.
- **الكود الفعلي (`Lines 50–142`):**
```python
def fit_schneider_bezier(
    points: list[Point2D],
    max_error_px: float = 1.5,
    max_nodes: int = 48,
    closed: bool = False
) -> list[BezierSegment]:
    """Fit a series of digitized points with cubic Bézier segments preserving sharp corners and fidelity."""
    if len(points) < 2:
        return []
    if len(points) == 2:
        p0, p3 = points[0], points[1]
        p1 = Point2D(x=p0.x + (p3.x - p0.x) / 3.0, y=p0.y + (p3.y - p0.y) / 3.0)
        p2 = Point2D(x=p0.x + 2.0 * (p3.x - p0.x) / 3.0, y=p0.y + 2.0 * (p3.y - p0.y) / 3.0)
        return [BezierSegment(p0=p0, p1=p1, p2=p2, p3=p3)]

    pts = list(points)
    # Adaptive corner-preserving simplification if points exceed max_nodes
    if len(pts) > max_nodes and max_nodes >= 6:
        np_pts = np.array([[p.x, p.y] for p in pts], dtype=np.float32).reshape((-1, 1, 2))
        eps = max(0.4, max_error_px * 0.3)
        while len(pts) > max_nodes and eps <= 2.5:
            approx = cv2.approxPolyDP(np_pts, epsilon=eps, closed=closed)
            pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in approx]
            eps += 0.2
        if not closed and points[-1] not in pts:
            pts.append(points[-1])

    n = len(pts)
    if n < 2:
        return []
    if n == 2:
        p0, p3 = pts[0], pts[1]
        p1 = Point2D(x=p0.x + (p3.x - p0.x) / 3.0, y=p0.y + (p3.y - p0.y) / 3.0)
        p2 = Point2D(x=p0.x + 2.0 * (p3.x - p0.x) / 3.0, y=p0.y + 2.0 * (p3.y - p0.y) / 3.0)
        return [BezierSegment(p0=p0, p1=p1, p2=p2, p3=p3)]

    segments: list[BezierSegment] = []
    num_segments = n if closed else n - 1

    for i in range(num_segments):
        p_prev = pts[(i - 1) % n] if closed else pts[max(0, i - 1)]
        p1 = pts[i]
        p2 = pts[(i + 1) % n] if closed else pts[min(n - 1, i + 1)]
        p_next = pts[(i + 2) % n] if closed else pts[min(n - 1, i + 2)]

        chord_dx = p2.x - p1.x
        chord_dy = p2.y - p1.y
        chord_len = math.hypot(chord_dx, chord_dy)
        if chord_len < 1e-4:
            continue

        v_in = (p1.x - p_prev.x, p1.y - p_prev.y)
        len_in = math.hypot(*v_in)
        v_out = (p_next.x - p2.x, p_next.y - p2.y)
        len_out = math.hypot(*v_out)

        # Cusp detection at p1
        is_corner_p1 = False
        if len_in > 1e-4:
            cos_p1 = (v_in[0] * chord_dx + v_in[1] * chord_dy) / (len_in * chord_len)
            if cos_p1 < -0.35:  # Angle < ~110 degrees is a corner cusp
                is_corner_p1 = True

        # Cusp detection at p2
        is_corner_p2 = False
        if len_out > 1e-4:
            cos_p2 = (chord_dx * v_out[0] + chord_dy * v_out[1]) / (chord_len * len_out)
            if cos_p2 < -0.35:
                is_corner_p2 = True

        if is_corner_p1:
            t1 = (chord_dx / chord_len, chord_dy / chord_len)
        else:
            t1_un = (p2.x - p_prev.x, p2.y - p_prev.y)
            t1_len = math.hypot(*t1_un)
            t1 = (t1_un[0] / t1_len, t1_un[1] / t1_len) if t1_len > 1e-4 else (chord_dx / chord_len, chord_dy / chord_len)

        if is_corner_p2:
            t2 = (chord_dx / chord_len, chord_dy / chord_len)
        else:
            t2_un = (p_next.x - p1.x, p_next.y - p1.y)
            t2_len = math.hypot(*t2_un)
            t2 = (t2_un[0] / t2_len, t2_un[1] / t2_len) if t2_len > 1e-4 else (chord_dx / chord_len, chord_dy / chord_len)

        # Handle lengths strictly bounded by 1/3 of chord length to eliminate loops and overshoots
        h1 = chord_len / 3.0
        h2 = chord_len / 3.0

        b1 = Point2D(p1.x + h1 * t1[0], p1.y + h1 * t1[1])
        b2 = Point2D(p2.x - h2 * t2[0], p2.y - h2 * t2[1])
        segments.append(BezierSegment(p0=p1, p1=b1, p2=b2, p3=p2))

    return segments
```
