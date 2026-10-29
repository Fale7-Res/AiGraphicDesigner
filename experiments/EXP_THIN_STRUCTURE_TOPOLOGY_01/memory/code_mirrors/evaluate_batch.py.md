# مرآة الكود التفصيلية: `evaluate_batch.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `evaluate_batch.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `evaluate_batch.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `25` (`Lines 1–25`)
- **بصمة الملف (`SHA-256`):** `59201d1566a8fb6a9367234de7e9caa15ed2b2a05db2c851d6305f1f602ff76c`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-EVALUATION-BATCH | 2026-10-29T11:43:50Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 7–21` | `def main():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 7–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `21` (`Lines 7–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–21`):**
```python
def main():
    rows=[]
    for case in CASES:
        for name in ['baseline','A','B','AB']:
            out=destination(case);target=out/(name+'.json')
            if not target.exists():continue
            m=evaluate_candidate(case,name)
            audit=json.loads((out/(name+'_audit.json')).read_text(encoding='utf-8'))
            row={k:m[k] for k in ['case','condition','raw_nonzero_fit_degenerate_rings','invalid_fit_rings','invalid_raw_rings','crossing_or_overlap_pairs','shared_reference_failures','max_junction_gap_px','self_intersecting_chains','near_intersection_unresolved_pairs','chains','cubics','geometry_acceptance','raw_to_fit']}
            if 'known_geometry' in m:row['known_geometry']=m['known_geometry']
            if 'arabic_source_proxy' in m:row['arabic_source_proxy']=m['arabic_source_proxy']
            row['accepted_bridges']=audit.get('accepted_bridges',0);row['accepted_chains']=len(audit.get('accepted_chains',[]))
            row['coverage']=m['coverage'];rows.append(row);dump(ROOT/'reports/SUMMARY.json',rows)
            print(json.dumps({k:v for k,v in row.items() if k not in ['known_geometry','arabic_source_proxy','raw_to_fit','coverage']}),flush=True)
    return rows
```
