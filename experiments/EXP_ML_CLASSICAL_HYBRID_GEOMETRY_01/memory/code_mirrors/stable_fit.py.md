# مرآة الكود التفصيلية: `stable_fit.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `stable_fit.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `stable_fit.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `129` (`Lines 1–129`)
- **بصمة الملف (`SHA-256`):** `87b1e442a53c6d7a412b0a7e90994575c33e0c2f4e273afc72d825a943a7c471`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-FIT-CONTROL | 2026-10-30T07:55:54Z | CREATED | Author: fitting_stability

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `flatten` | `function` | `Lines 16–30` | `def flatten(curve, epsilon=.002, depth=0):` | Adaptive control-hull distance bound, excluding unresolved recursion. |
| `sample_segments` | `function` | `Lines 33–38` | `def sample_segments(points, step=.01):` | رمز برمجي موثق. |
| `measure` | `function` | `Lines 41–60` | `def measure(points, curves, step=.01, epsilon=.002):` | Segment distances, never nearest sampled-vertex distances. |
| `construct` | `function` | `Lines 63–81` | `def construct(vertices):` | Per-chord handles; long neighbors cannot stretch a short chord's handle. |
| `fit` | `function` | `Lines 84–128` | `def fit(points, maximum_deviation=.6, maximum_segments=64):` | Frozen RDP, chord handles, <=8 rounds subdivision, no grid fallback. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `flatten` — `Lines 16–30`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `30` (`Lines 16–30`)
- **الوظيفة:** Adaptive control-hull distance bound, excluding unresolved recursion.
- **الكود الفعلي (`Lines 16–30`):**
```python
def flatten(curve, epsilon=.002, depth=0):
    """Adaptive control-hull distance bound, excluding unresolved recursion."""
    p = np.asarray(curve, float)
    chord = p[3]-p[0]
    denom = float(chord@chord)
    t = np.clip((p[1:3]-p[0])@chord/denom, 0, 1) if denom else np.zeros(2)
    if np.linalg.norm(p[1:3]-(p[0]+t[:, None]*chord), axis=1).max() <= epsilon:
        return np.array([p[0], p[3]])
    if depth >= 24:
        raise ValueError('Unresolved curve flattening')
    a = (p[:-1]+p[1:])/2
    b = (a[:-1]+a[1:])/2
    c = (b[0]+b[1])/2
    return np.concatenate([flatten([p[0],a[0],b[0],c], epsilon, depth+1)[:-1],
                           flatten([c,b[1],a[2],p[3]], epsilon, depth+1)])
```

### `sample_segments` — `Lines 33–38`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `33` إلى السطر `38` (`Lines 33–38`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 33–38`):**
```python
def sample_segments(points, step=.01):
    pieces = []
    for a,b in zip(points[:-1],points[1:]):
        n = max(1,int(math.ceil(np.linalg.norm(b-a)/step)))
        pieces.append(a+(b-a)*np.arange(n)[:,None]/n)
    return np.concatenate(pieces+[np.asarray(points[-1:])])
```

### `measure` — `Lines 41–60`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `41` إلى السطر `60` (`Lines 41–60`)
- **الوظيفة:** Segment distances, never nearest sampled-vertex distances.
- **الكود الفعلي (`Lines 41–60`):**
```python
def measure(points, curves, step=.01, epsilon=.002):
    """Segment distances, never nearest sampled-vertex distances.

    Dense numerical estimates include step/2 + flatten tolerance envelopes.
    Floating predicates and flattening are not exact arithmetic certificates.
    """
    flat = np.concatenate([flatten(c,epsilon)[:-1] for c in curves]+[curves[-1,-1:]])
    raw_line, fit_line = LineString(points), LineString(flat)
    raw_samples, fit_samples = sample_segments(points,step), sample_segments(flat,step)
    # Shapely 2 vectorized distance avoids a Python Point object per sample.
    import shapely
    rd = shapely.distance(shapely.points(raw_samples), fit_line)
    fd = shapely.distance(shapely.points(fit_samples), raw_line)
    return {'raw_to_curve_max_px':float(rd.max()),'curve_to_raw_max_px':float(fd.max()),
            'numerical_upper_envelope_px':float(max(rd.max(),fd.max())+step/2+epsilon),
            'curve_to_raw_worst_xy':fit_samples[int(np.argmax(fd))].tolist(),
            'raw_to_curve_worst_xy':raw_samples[int(np.argmax(rd))].tolist(),
            'flatten_tolerance_px':epsilon,'sampling_step_px':step,
            'curve_is_simple_numerical':bool(fit_line.is_simple),
            'continuous_exact_certification':False}
```

### `construct` — `Lines 63–81`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `63` إلى السطر `81` (`Lines 63–81`)
- **الوظيفة:** Per-chord handles; long neighbors cannot stretch a short chord's handle.
- **الكود الفعلي (`Lines 63–81`):**
```python
def construct(vertices):
    """Per-chord handles; long neighbors cannot stretch a short chord's handle."""
    delta=np.diff(vertices,axis=0)
    lengths=np.linalg.norm(delta,axis=1)
    units=delta/np.maximum(lengths[:,None],1e-12)
    tangents=[None]*len(vertices)
    corners=np.ones(len(vertices),bool)
    for i in range(1,len(vertices)-1):
        angle=math.degrees(math.acos(float(np.clip(units[i-1]@units[i],-1,1))))
        if angle < 60:
            direction=units[i-1]+units[i]
            tangents[i]=direction/max(np.linalg.norm(direction),1e-12)
            corners[i]=False
    curves=[]
    for i,(a,b) in enumerate(zip(vertices[:-1],vertices[1:])):
        ta=units[i] if corners[i] else tangents[i]
        tb=units[i] if corners[i+1] else tangents[i+1]
        curves.append([a,a+ta*lengths[i]/3,b-tb*lengths[i]/3,b])
    return np.asarray(curves),int(corners[1:-1].sum())
```

### `fit` — `Lines 84–128`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `84` إلى السطر `128` (`Lines 84–128`)
- **الوظيفة:** Frozen RDP, chord handles, <=8 rounds subdivision, no grid fallback.
- **الكود الفعلي (`Lines 84–128`):**
```python
def fit(points, maximum_deviation=.6, maximum_segments=64):
    """Frozen RDP, chord handles, <=8 rounds subdivision, no grid fallback.

    An unsafe candidate is rejected. Refinement adds a raw support vertex only
    when a measured failure identifies a local interval; never emits raw boxes.
    """
    started=time.perf_counter()
    points=np.asarray(points,float)
    if points.ndim!=2 or points.shape[1]!=2 or len(points)<2 or not np.isfinite(points).all():
        return None,{'reason':'invalid_input'}
    if np.any(np.linalg.norm(np.diff(points,axis=0),axis=1)<=1e-12):
        return None,{'reason':'duplicate_adjacent_points'}
    vertices=cv2.approxPolyDP(points.astype(np.float32).reshape(-1,1,2),.35,False).reshape(-1,2).astype(float)
    if len(vertices)<2:
        return None,{'reason':'insufficient_vertices'}
    # RDP vertices are original samples; establish increasing raw intervals.
    indices=[];previous=-1
    for vertex in vertices:
        remaining=np.arange(previous+1,len(points))
        found=remaining[np.argmin(np.linalg.norm(points[remaining]-vertex,axis=1))]
        indices.append(int(found));previous=int(found)
    for round_index in range(9):
        if len(indices)-1>maximum_segments:
            return None,{'reason':'cubic_budget','segments':len(indices)-1}
        if time.perf_counter()-started>30:
            return None,{'reason':'wall_budget'}
        curves,corners=construct(points[indices])
        metrics=measure(points,curves)
        if metrics['numerical_upper_envelope_px']<=maximum_deviation:
            return curves,dict(metrics,reason='accepted',segments=len(curves),
                               subdivision_rounds=round_index,intentional_corner_count=corners,
                               wall_seconds=time.perf_counter()-started)
        if round_index==8:
            break
        # Match each curve only to its frozen raw interval, conservatively
        # refining the worst interval and retaining every existing knot.
        scores=[]
        for i,c in enumerate(curves):
            local=points[indices[i]:indices[i+1]+1]
            scores.append(measure(local,np.asarray([c]))['numerical_upper_envelope_px'])
        worst=int(np.argmax(scores));lo,hi=indices[worst:worst+2]
        if hi-lo<2:
            return None,dict(metrics,reason='no_subdivision_support',segments=len(curves))
        indices.insert(worst+1,(lo+hi)//2)
    return None,dict(metrics,reason='deviation_budget',segments=len(curves))
```
