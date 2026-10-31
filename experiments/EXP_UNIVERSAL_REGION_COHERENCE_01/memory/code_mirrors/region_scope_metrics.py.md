# مرآة الكود التفصيلية: `region_scope_metrics.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `region_scope_metrics.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `region_scope_metrics.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `25` (`Lines 1–25`)
- **بصمة الملف (`SHA-256`):** `3ae102d3edb4725dfffd0c5e60afd263d4330d2895532f6dcbb5db34662ae22e`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-REGION-SCOPE | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `separate_region_scope` | `function` | `Lines 9–23` | `def separate_region_scope():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `separate_region_scope` — `Lines 9–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `23` (`Lines 9–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–23`):**
```python
def separate_region_scope():
 allrows=json.loads((E/'reports/METRICS.json').read_text());p=json.loads((E/'protocol.json').read_text())
 for case in p['cases']:
  out=output_folder(case);_,target,_,tag=references(case,out/'source.png');source=xy(np.load(out/'evidence.npz')['skeleton'])
  for c in ['R','SR']:
   d=json.loads((out/(c+'.json')).read_text());audit=json.loads((out/(c+'_audit.json')).read_text());indices={r['chain_id'] for r in audit['rows'] if r['integrated']};items=[v for i,v in enumerate(d['accepted']) if i in indices];_,pts=samples_from_items(items);m=next(m for m in allrows if m['case']==case and m['condition']==c)
   m['metric_geometry_scope']='Default topology/contour metrics describe ALL preserved P/S proposals including unintegrated strokes. Region SVG shows only integrated atomic faces; separate integrated_only metrics below. A filled region is not inferred from successful stroke rendering.'
   m['integrated_only']=dict(paths=len(items),source_proxy=support_stats(source,pts,1.25),boundary=support_stats(target,pts,1.25) if target is not None else None)
   if m.get('critical_guides'):
    from universal_run import R
    guides=json.loads((R/'experiments/EXP_COMPLETE_GEOMETRY_ISOLATION_01/references/shield_complete_boundary_reference.json').read_text());m['integrated_only']['critical_guides']=[]
    for g in guides['components']+guides['appearance_only']:
     q=np.concatenate([sample_segments(np.asarray(v,float),.25) for v in g['polylines']]);m['integrated_only']['critical_guides'].append(dict(id=g['id'],fitted=support_stats(q,pts,g['uncertainty_px'])))
   (out/(c+'_metrics.json')).write_text(json.dumps(m,indent=2))
 (E/'reports/METRICS.json').write_text(json.dumps(allrows,indent=2))
```
