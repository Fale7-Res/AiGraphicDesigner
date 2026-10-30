# مرآة الكود التفصيلية: `qa/diagnose_rejected_fit.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/diagnose_rejected_fit.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/diagnose_rejected_fit.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `101` (`Lines 1–101`)
- **بصمة الملف (`SHA-256`):** `620043e5a00cc389b2931013bcd52d0066fbf555d50ac18477fe9872bea43fc8`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `diagnostic` | `function` | `Lines 19–96` | `def diagnostic(source_json, target):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `diagnostic` — `Lines 19–96`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `96` (`Lines 19–96`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 19–96`):**
```python
def diagnostic(source_json, target):
    source = Path(source_json); before = hashlib.sha256(source.read_bytes()).hexdigest()
    audit = json.loads(source.read_text(encoding='utf-8'))
    output = Path(target); output.mkdir(parents=True, exist_ok=False)
    results = []; svg = []
    for reject in audit['rejected']:
        if reject['reason'] != 'curve_deviation':
            continue
        raw = np.asarray(reject['source_points_xy'], float)
        captured = {}
        def trace(frame, event, argument):
            if frame.f_code is ds._fit.__code__ and event == 'return':
                captured.update(frame.f_locals)
            return trace
        sys.settrace(trace)
        try:
            returned, info = ds._fit(raw)
        finally:
            sys.settrace(None)
        assert returned is None and info['reason'] == 'curve_deviation'
        curves = np.asarray(captured['curves'])
        flat = []
        for curve in curves:
            points = flatten_cubic(curve, .01)
            flat.extend(points if not flat else points[1:])
        raw_line = LineString(raw); curve_line = LineString(flat)
        raw_dense = uniform_points(raw, .01); curve_dense = uniform_points(flat, .01)
        rd = np.asarray([curve_line.distance(Point(p)) for p in raw_dense])
        cd = np.asarray([raw_line.distance(Point(p)) for p in curve_dense])
        raw_samples = captured['raw']; curve_samples = captured['fitted']
        pointwise_rc = np.asarray([curve_line.distance(Point(p)) for p in raw_samples])
        pointwise_cr = np.asarray([raw_line.distance(Point(p)) for p in curve_samples])
        coarse_raw, coarse_fit = np.asarray(raw_samples), np.asarray(curve_samples)
        from scipy.spatial import cKDTree
        nn_r = cKDTree(coarse_fit).query(coarse_raw)[0]
        nn_c = cKDTree(coarse_raw).query(coarse_fit)[0]
        approx = cv2.approxPolyDP(raw.astype(np.float32).reshape(-1,1,2), .35, False).reshape(-1,2)
        segment_rows = []
        for index, curve in enumerate(curves):
            dense = uniform_points(flatten_cubic(curve, .01), .01)
            distances = np.asarray([raw_line.distance(Point(p)) for p in dense])
            segment_rows.append({'segment': index, 'maximum_distance_px': float(distances.max()),
                                 'chord_length_px': float(np.linalg.norm(curve[3]-curve[0])),
                                 'controls': curve.tolist(),
                                 'location_xy': dense[int(np.argmax(distances))].tolist()})
        row = {'chain_id': reject['chain_id'], 'status': 'REJECTED_UNCHANGED',
               'saved_sampled_deviation': reject['sampled_symmetric_deviation_px'],
               'recomputed_sampled_deviation': info['sampled_symmetric_deviation_px'],
               'adaptive_flattening_tolerance_px': .01, 'dense_sampling_step_px': .01,
               'raw_to_flattened_curve_dense_max_px': float(rd.max()),
               'flattened_curve_to_raw_dense_max_px': float(cd.max()),
               'shapely_discrete_hausdorff_px': float(raw_line.hausdorff_distance(curve_line)),
               'rdp_polyline_hausdorff_px': float(raw_line.hausdorff_distance(LineString(approx))),
               'saved_curve_samples_to_raw_segments_max_px': float(pointwise_cr.max()),
               'saved_raw_samples_to_curve_segments_max_px': float(pointwise_rc.max()),
               'raw_point_nn_peak_vs_exact_segment_distance': [float(nn_r.max()), float(pointwise_rc[np.argmax(nn_r)])],
               'curve_point_nn_peak_vs_exact_segment_distance': [float(nn_c.max()), float(pointwise_cr[np.argmax(nn_c)])],
               'maximum_overshoot_xy': curve_dense[int(np.argmax(cd))].tolist(),
               'raw_maximum_displacement_xy': raw_dense[int(np.argmax(rd))].tolist(),
               'worst_curve_segments': sorted(segment_rows, key=lambda r: -r['maximum_distance_px'])[:3],
               'cubic_segments': len(curves),
               'continuous_distance_certified': False}
        results.append(row)
        d = 'M'+' L'.join(','.join(map(str,p)) for p in raw)
        svg.append(f'<path d="{d}" fill="none" stroke="#0077cc" stroke-width="0.3"/>')
        d = 'M'+','.join(map(str, curves[0,0]))
        for curve in curves:
            d += ' C' + ','.join(map(str, curve[1:].ravel()))
        svg.append(f'<path d="{d}" fill="none" stroke="#dd2222" stroke-width="0.25"/>')
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    assert before == after
    summary = {'input_sha256': before, 'input_unchanged': True, 'results': results,
               'scope': 'Read-only explanation, no regenerated accepted candidate or threshold change'}
    (output/'rejection_analysis.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    (output/'REJECTED_CURVES_DIAGNOSTIC_ONLY.svg').write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="128" height="96" viewBox="0 0 128 96">'
        '<title>REJECTED diagnostic only; blue raw source skeleton, red rejected cubics</title>' + ''.join(svg)+'</svg>', encoding='utf-8')
    print(json.dumps(summary, indent=2))
```
