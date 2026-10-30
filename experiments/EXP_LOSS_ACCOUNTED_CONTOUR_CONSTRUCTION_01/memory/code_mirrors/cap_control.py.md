# مرآة الكود التفصيلية: `cap_control.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `cap_control.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `cap_control.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `20` (`Lines 1–20`)
- **بصمة الملف (`SHA-256`):** `2dc18177f6fc8ce9958931cdcbe9f3fa1704be270a38f2f85b4ee4ea44dab278`
- **الوصف التفصيلي:** # START CHANGE AGD-CONTOUR-CLOSURE | 2026-10-30T15:21:28Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `execute_cap_only` | `function` | `Lines 8–16` | `def execute_cap_only(arm):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `execute_cap_only` — `Lines 8–16`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `16` (`Lines 8–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–16`):**
```python
def execute_cap_only(arm):
    protocol=json.loads((E/'protocol.json').read_text());base=Path(protocol['cases']['K01_linear_corner_hole']['base']);a=json.loads((base/arm/'construction.json').read_text());out=E/'results/K01_linear_corner_hole'/arm
    assert not (out/'CAP512.json').exists();records=[];accepted=[];start=time.monotonic()
    for trace in a['traces']:
        points=np.asarray(trace['source_points_xy']);curves,meta=fit(points,maximum_deviation=.6,maximum_segments=512)
        records.append({'trace_id':trace['trace_id'],'old_reason':trace['reason'],'new_status':meta['reason'],'meta':meta,'length_px':trace['length_px']})
        if curves is not None:accepted.append({'trace_id':trace['trace_id'],'curves':curves.tolist()})
    result={'case':'K01_linear_corner_hole','arm':arm,'condition':'CAP512_DIAGNOSTIC','only_change':'oldstablefitmaximum_segments64to512;no partition/periodic/changed .6gate','records':records,'accepted':accepted,'wall_seconds':time.monotonic()-start,'not_main_condition':True}
    (out/'CAP512.json').write_text(json.dumps(result,indent=2));(out/'CAP512.svg').write_text(svg_graph(chain_graph(accepted,192,160)),encoding='utf-8');print(arm,[(r['trace_id'],r['new_status']) for r in records],flush=True)
```
