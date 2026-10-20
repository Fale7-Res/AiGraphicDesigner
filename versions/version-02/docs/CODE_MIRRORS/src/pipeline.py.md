# مرآة الكود التفصيلية للإصدار: `version-02/src/pipeline.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-02/src/pipeline.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-02`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/pipeline.py`
- **الإصدار المعماري (`Architecture Version`):** `version-02`
- **إجمالي عدد الأسطر (`Total Lines`):** `125` (`Lines 1–125`)
- **بصمة الملف (`SHA-256`):** `6e683b7458312d1318bcbbd5815e848bd067abf51568b62d625ced7415cd79ad`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-02`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-02` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SemanticPathElement` | `class` | `Lines 16–32` | `class SemanticPathElement:` | Represents a discrete path component (base, shadow, highlight) in a group. |
| `SemanticPathElement.render_d_attribute` | `method` | `Lines 23–32` | `def render_d_attribute(self) -> str:` | Render d attribute path string. |
| `SemanticObjectGroup` | `class` | `Lines 36–72` | `class SemanticObjectGroup:` | Represents a grouped design object containing base, shadow, and clipPath. |
| `SemanticObjectGroup.to_svg_group` | `method` | `Lines 45–72` | `def to_svg_group(self) -> str:` | Render this semantic object as an SVG <g> with non-destructive clipping. |
| `HierarchicalSceneGraphPipeline` | `class` | `Lines 75–124` | `class HierarchicalSceneGraphPipeline:` | Version 02 hierarchical scene graph pipeline. |
| `HierarchicalSceneGraphPipeline.__init__` | `method` | `Lines 78–79` | `def __init__(self, max_nodes_budget: int = 36) -> None:` | رمز برمجي موثق للإصدار. |
| `HierarchicalSceneGraphPipeline.create_semantic_group` | `method` | `Lines 81–113` | `def create_semantic_group(` | Create an optimized semantic object group with base and clipped shadow. |
| `HierarchicalSceneGraphPipeline.export_scene_graph_svg` | `method` | `Lines 115–124` | `def export_scene_graph_svg(self, groups: list[SemanticObjectGroup], width: int = 2048, height: int = 2048) -> str:` | Export all semantic groups into a high-fidelity Clean SVG document. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SemanticPathElement` — `Lines 16–32`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `32` (`Lines 16–32`)
- **الوظيفة:** Represents a discrete path component (base, shadow, highlight) in a group.
- **الكود الفعلي (`Lines 16–32`):**
```python
class SemanticPathElement:
    """Represents a discrete path component (base, shadow, highlight) in a group."""
    role: str
    fill_color_hex: str
    opacity: float = 1.0
    segments: list[OptimizedBezierSegment] = field(default_factory=list)

    def render_d_attribute(self) -> str:
        """Render d attribute path string."""
        if not self.segments:
            return ""
        start = self.segments[0].anchor_start
        cmds = [f"M {start.x:.2f} {start.y:.2f}"]
        for seg in self.segments:
            cmds.append(seg.to_svg_cubic_command())
        cmds.append("Z")
        return " ".join(cmds)
```

### `SemanticPathElement.render_d_attribute` — `Lines 23–32`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `32` (`Lines 23–32`)
- **الوظيفة:** Render d attribute path string.
- **الكود الفعلي (`Lines 23–32`):**
```python
    def render_d_attribute(self) -> str:
        """Render d attribute path string."""
        if not self.segments:
            return ""
        start = self.segments[0].anchor_start
        cmds = [f"M {start.x:.2f} {start.y:.2f}"]
        for seg in self.segments:
            cmds.append(seg.to_svg_cubic_command())
        cmds.append("Z")
        return " ".join(cmds)
```

### `SemanticObjectGroup` — `Lines 36–72`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `72` (`Lines 36–72`)
- **الوظيفة:** Represents a grouped design object containing base, shadow, and clipPath.
- **الكود الفعلي (`Lines 36–72`):**
```python
class SemanticObjectGroup:
    """Represents a grouped design object containing base, shadow, and clipPath."""
    group_id: str
    label: str
    z_index: int
    base_element: SemanticPathElement
    shadow_elements: list[SemanticPathElement] = field(default_factory=list)
    highlight_elements: list[SemanticPathElement] = field(default_factory=list)

    def to_svg_group(self) -> str:
        """Render this semantic object as an SVG <g> with non-destructive clipping."""
        clip_id = f"clip_{self.group_id}"
        base_d = self.base_element.render_d_attribute()
        out = [f'<g id="{self.group_id}" data-semantic-label="{self.label}">']
        out.append(f'  <clipPath id="{clip_id}">')
        out.append(f'    <path d="{base_d}" />')
        out.append('  </clipPath>')
        out.append(f'  <path id="{self.group_id}_base" fill="{self.base_element.fill_color_hex}" d="{base_d}" />')

        for idx, sh in enumerate(self.shadow_elements):
            sh_d = sh.render_d_attribute()
            if sh_d:
                out.append(
                    f'  <path id="{self.group_id}_shadow_{idx}" clip-path="url(#{clip_id})" '
                    f'fill="{sh.fill_color_hex}" opacity="{sh.opacity:.2f}" d="{sh_d}" />'
                )

        for idx, hl in enumerate(self.highlight_elements):
            hl_d = hl.render_d_attribute()
            if hl_d:
                out.append(
                    f'  <path id="{self.group_id}_hl_{idx}" clip-path="url(#{clip_id})" '
                    f'fill="{hl.fill_color_hex}" opacity="{hl.opacity:.2f}" d="{hl_d}" />'
                )

        out.append('</g>')
        return "\n  ".join(out)
```

### `SemanticObjectGroup.to_svg_group` — `Lines 45–72`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `45` إلى السطر `72` (`Lines 45–72`)
- **الوظيفة:** Render this semantic object as an SVG <g> with non-destructive clipping.
- **الكود الفعلي (`Lines 45–72`):**
```python
    def to_svg_group(self) -> str:
        """Render this semantic object as an SVG <g> with non-destructive clipping."""
        clip_id = f"clip_{self.group_id}"
        base_d = self.base_element.render_d_attribute()
        out = [f'<g id="{self.group_id}" data-semantic-label="{self.label}">']
        out.append(f'  <clipPath id="{clip_id}">')
        out.append(f'    <path d="{base_d}" />')
        out.append('  </clipPath>')
        out.append(f'  <path id="{self.group_id}_base" fill="{self.base_element.fill_color_hex}" d="{base_d}" />')

        for idx, sh in enumerate(self.shadow_elements):
            sh_d = sh.render_d_attribute()
            if sh_d:
                out.append(
                    f'  <path id="{self.group_id}_shadow_{idx}" clip-path="url(#{clip_id})" '
                    f'fill="{sh.fill_color_hex}" opacity="{sh.opacity:.2f}" d="{sh_d}" />'
                )

        for idx, hl in enumerate(self.highlight_elements):
            hl_d = hl.render_d_attribute()
            if hl_d:
                out.append(
                    f'  <path id="{self.group_id}_hl_{idx}" clip-path="url(#{clip_id})" '
                    f'fill="{hl.fill_color_hex}" opacity="{hl.opacity:.2f}" d="{hl_d}" />'
                )

        out.append('</g>')
        return "\n  ".join(out)
```

### `HierarchicalSceneGraphPipeline` — `Lines 75–124`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `75` إلى السطر `124` (`Lines 75–124`)
- **الوظيفة:** Version 02 hierarchical scene graph pipeline.
- **الكود الفعلي (`Lines 75–124`):**
```python
class HierarchicalSceneGraphPipeline:
    """Version 02 hierarchical scene graph pipeline."""

    def __init__(self, max_nodes_budget: int = 36) -> None:
        self.max_nodes_budget = max_nodes_budget

    def create_semantic_group(
        self,
        group_id: str,
        label: str,
        base_points: list[tuple[float, float]],
        base_color_hex: str,
        shadow_points: list[tuple[float, float]] | None = None,
        shadow_color_hex: str = "#000000",
        shadow_opacity: float = 0.35,
    ) -> SemanticObjectGroup:
        """Create an optimized semantic object group with base and clipped shadow."""
        base_vpts = [VectorPoint(x=p[0], y=p[1]) for p in base_points]
        base_segs = fit_smooth_curve(base_vpts, max_nodes=self.max_nodes_budget)
        base_elem = SemanticPathElement(role="base", fill_color_hex=base_color_hex, opacity=1.0, segments=base_segs)

        shadow_elems: list[SemanticPathElement] = []
        if shadow_points:
            sh_vpts = [VectorPoint(x=p[0], y=p[1]) for p in shadow_points]
            sh_segs = fit_smooth_curve(sh_vpts, max_nodes=self.max_nodes_budget)
            shadow_elems.append(SemanticPathElement(
                role="shadow",
                fill_color_hex=shadow_color_hex,
                opacity=shadow_opacity,
                segments=sh_segs,
            ))

        return SemanticObjectGroup(
            group_id=group_id,
            label=label,
            z_index=0,
            base_element=base_elem,
            shadow_elements=shadow_elems,
        )

    def export_scene_graph_svg(self, groups: list[SemanticObjectGroup], width: int = 2048, height: int = 2048) -> str:
        """Export all semantic groups into a high-fidelity Clean SVG document."""
        sorted_groups = sorted(groups, key=lambda g: g.z_index)
        body = "\n  ".join(g.to_svg_group() for g in sorted_groups)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
            f'  <desc>Generated by AI Graphic Designer version-02 (Hierarchical Scene Graph)</desc>\n'
            f'  {body}\n'
            f'</svg>'
        )
```

### `HierarchicalSceneGraphPipeline.__init__` — `Lines 78–79`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `78` إلى السطر `79` (`Lines 78–79`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 78–79`):**
```python
    def __init__(self, max_nodes_budget: int = 36) -> None:
        self.max_nodes_budget = max_nodes_budget
```

### `HierarchicalSceneGraphPipeline.create_semantic_group` — `Lines 81–113`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `113` (`Lines 81–113`)
- **الوظيفة:** Create an optimized semantic object group with base and clipped shadow.
- **الكود الفعلي (`Lines 81–113`):**
```python
    def create_semantic_group(
        self,
        group_id: str,
        label: str,
        base_points: list[tuple[float, float]],
        base_color_hex: str,
        shadow_points: list[tuple[float, float]] | None = None,
        shadow_color_hex: str = "#000000",
        shadow_opacity: float = 0.35,
    ) -> SemanticObjectGroup:
        """Create an optimized semantic object group with base and clipped shadow."""
        base_vpts = [VectorPoint(x=p[0], y=p[1]) for p in base_points]
        base_segs = fit_smooth_curve(base_vpts, max_nodes=self.max_nodes_budget)
        base_elem = SemanticPathElement(role="base", fill_color_hex=base_color_hex, opacity=1.0, segments=base_segs)

        shadow_elems: list[SemanticPathElement] = []
        if shadow_points:
            sh_vpts = [VectorPoint(x=p[0], y=p[1]) for p in shadow_points]
            sh_segs = fit_smooth_curve(sh_vpts, max_nodes=self.max_nodes_budget)
            shadow_elems.append(SemanticPathElement(
                role="shadow",
                fill_color_hex=shadow_color_hex,
                opacity=shadow_opacity,
                segments=sh_segs,
            ))

        return SemanticObjectGroup(
            group_id=group_id,
            label=label,
            z_index=0,
            base_element=base_elem,
            shadow_elements=shadow_elems,
        )
```

### `HierarchicalSceneGraphPipeline.export_scene_graph_svg` — `Lines 115–124`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `115` إلى السطر `124` (`Lines 115–124`)
- **الوظيفة:** Export all semantic groups into a high-fidelity Clean SVG document.
- **الكود الفعلي (`Lines 115–124`):**
```python
    def export_scene_graph_svg(self, groups: list[SemanticObjectGroup], width: int = 2048, height: int = 2048) -> str:
        """Export all semantic groups into a high-fidelity Clean SVG document."""
        sorted_groups = sorted(groups, key=lambda g: g.z_index)
        body = "\n  ".join(g.to_svg_group() for g in sorted_groups)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">\n'
            f'  <desc>Generated by AI Graphic Designer version-02 (Hierarchical Scene Graph)</desc>\n'
            f'  {body}\n'
            f'</svg>'
        )
```
