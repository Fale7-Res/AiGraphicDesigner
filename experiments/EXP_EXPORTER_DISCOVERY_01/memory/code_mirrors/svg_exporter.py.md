# مرآة الكود التفصيلية: `svg_exporter.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `svg_exporter.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `svg_exporter.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `115` (`Lines 1–115`)
- **بصمة الملف (`SHA-256`):** `934c0a68f613e46b63127e48f700b1f51e399f1549a69e14781523a19878a8ea`
- **الوصف التفصيلي:** # START CHANGE AGD-EXPORTER-CORRECTNESS | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `_point` | `function` | `Lines 12–15` | `def _point(value):` | رمز برمجي موثق. |
| `_same` | `function` | `Lines 18–19` | `def _same(a, b):` | رمز برمجي موثق. |
| `chain_segments` | `function` | `Lines 22–54` | `def chain_segments(chain, raw=False, forward=True):` | Return directed L/C segments, including a logical chain closure. |
| `_coordinate` | `function` | `Lines 57–58` | `def _coordinate(point, precision):` | رمز برمجي موثق. |
| `_commands` | `function` | `Lines 61–65` | `def _commands(segments, move=True, precision=17):` | رمز برمجي موثق. |
| `_color` | `function` | `Lines 68–70` | `def _color(label):` | رمز برمجي موثق. |
| `svg_graph` | `function` | `Lines 73–114` | `def svg_graph(graph, raw=False, regions=False, foreground=None, *, precision=17):` | API-compatible strict replacement for research geometry_eval.svg_graph. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `_point` — `Lines 12–15`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `15` (`Lines 12–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–15`):**
```python
def _point(value):
    if len(value) != 2 or not all(math.isfinite(float(x)) for x in value):
        raise ValueError('A finite 2D point is required')
    return tuple(float(x) for x in value)
```

### `_same` — `Lines 18–19`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `19` (`Lines 18–19`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–19`):**
```python
def _same(a, b):
    return math.dist(a, b) <= 1e-8
```

### `chain_segments` — `Lines 22–54`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `54` (`Lines 22–54`)
- **الوظيفة:** Return directed L/C segments, including a logical chain closure.
- **الكود الفعلي (`Lines 22–54`):**
```python
def chain_segments(chain, raw=False, forward=True):
    """Return directed L/C segments, including a logical chain closure.

    Reverse the complete geometric walk, including its implied closure. Merely
    reversing the stored segments first rotates an implicitly closed chain's
    anchor and can disconnect its shared junction from its containing face.
    """
    result = []
    if raw:
        points = [_point(p) for p in chain['pixel_crack_vertices']]
        if len(points) < 2:
            raise ValueError('Chain needs at least two raw points')
        result = [('L', (a, b)) for a, b in zip(points, points[1:])]
    else:
        for segment in chain['segments']:
            kind = segment['type']
            if kind == 'L':
                points = (_point(segment['p0']), _point(segment['p3']))
            elif kind == 'C':
                points = tuple(_point(segment[k]) for k in ('p0','p1','p2','p3'))
            else:
                raise ValueError('Unsupported segment type: ' + str(kind))
            if result and not _same(result[-1][1][-1], points[0]):
                raise ValueError('Disconnected chain segments')
            result.append((kind, points))
        if not result:
            raise ValueError('Empty fitted chain')
    start, end = result[0][1][0], result[-1][1][-1]
    if chain.get('closed') and not _same(start, end):
        result.append(('L', (end, start)))
    if not forward:
        result = [(kind, tuple(reversed(points))) for kind, points in reversed(result)]
    return result
```

### `_coordinate` — `Lines 57–58`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `58` (`Lines 57–58`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–58`):**
```python
def _coordinate(point, precision):
    return ','.join(format(value, f'.{precision}g') for value in point)
```

### `_commands` — `Lines 61–65`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `61` إلى السطر `65` (`Lines 61–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 61–65`):**
```python
def _commands(segments, move=True, precision=17):
    result = ['M' + _coordinate(segments[0][1][0], precision)] if move else []
    result.extend(kind + ' '.join(_coordinate(p, precision) for p in points[1:])
                  for kind, points in segments)
    return ' '.join(result)
```

### `_color` — `Lines 68–70`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `68` إلى السطر `70` (`Lines 68–70`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 68–70`):**
```python
def _color(label):
    value = (int(label) * 0x9e3779) & 0xffffff
    return '#%06x' % value
```

### `svg_graph` — `Lines 73–114`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `114` (`Lines 73–114`)
- **الوظيفة:** API-compatible strict replacement for research geometry_eval.svg_graph.
- **الكود الفعلي (`Lines 73–114`):**
```python
def svg_graph(graph, raw=False, regions=False, foreground=None, *, precision=17):
    """API-compatible strict replacement for research geometry_eval.svg_graph.

    Region contours must already form connected closed walks. No snapping,
    bridge creation, polygon repair, orientation changes, or topology changes.
    The inherited evenodd rule is preserved for compound regions and holes.
    """
    if precision not in (8,17):
        raise ValueError('Only 8-significant-digit legacy isolation or 17-digit roundtrip is supported')
    chains = {chain['id']: chain for chain in graph['chains']}
    if len(chains) != len(graph['chains']):
        raise ValueError('Duplicate chain IDs')
    parts = []
    if regions:
        for label, loops in graph['faces'].items():
            if int(label) == 0 or (foreground is not None and int(label) not in foreground):
                continue
            contours = []
            for refs in loops:
                joined = []
                if not refs:
                    raise ValueError('Empty face contour')
                for ref in refs:
                    directed = chain_segments(chains[ref['chain']], raw, ref['forward'])
                    if joined and not _same(joined[-1][1][-1], directed[0][1][0]):
                        raise ValueError('Disconnected face contour')
                    joined.extend(directed)
                if not _same(joined[-1][1][-1], joined[0][1][0]):
                    raise ValueError('Open face contour; exporter will not repair it')
                contours.append(_commands(joined, precision=precision) + ' Z')
            color = 'black' if foreground is not None else _color(label)
            parts.append(f'<path data-region="{escape(str(label), quote=True)}" fill="{color}" fill-rule="evenodd" d="{" ".join(contours)}"/>')
    else:
        for chain in graph['chains']:
            directed = chain_segments(chain, raw)
            data = _commands(directed, precision=precision) + (' Z' if chain.get('closed') else '')
            color = '#607d8b' if 0 in chain['adjacent_face_labels'] else '#111827'
            parts.append(f'<path data-chain="{escape(str(chain["id"]), quote=True)}" d="{data}" fill="none" stroke="{color}" stroke-width="0.35"/>')
    width, height = float(graph['width']), float(graph['height'])
    if not all(math.isfinite(v) and v > 0 for v in (width, height)):
        raise ValueError('Positive finite SVG dimensions required')
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.17g}" height="{height:.17g}" viewBox="0 0 {width:.17g} {height:.17g}">' + ''.join(parts) + '</svg>'
```
