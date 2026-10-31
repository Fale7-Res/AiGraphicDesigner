# مرآة الكود التفصيلية: `combined_control.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `combined_control.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `combined_control.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `28` (`Lines 1–28`)
- **بصمة الملف (`SHA-256`):** `5d4f40e8aac58d30958ecb54a486a48300ee69e9a4561f115023094713be7b7d`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-COMBINE | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `combined_worker` | `function` | `Lines 11–23` | `def combined_worker():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `combined_worker` — `Lines 11–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `23` (`Lines 11–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 11–23`):**
```python
def combined_worker():
 gate=json.loads((E/'reports/COMBINATION_GATE.json').read_text());assert gate['execute'];protocol=json.loads((E/'protocol.json').read_text())
 rows=json.loads((E/'reports/METRICS.json').read_text())
 for case in protocol['cases']:
  out=output_folder(case);s=json.loads((out/'S.json').read_text());rgb=np.asarray(Image.open(out/'source.png').convert('RGB'));h,w=rgb.shape[:2];graph,audit=integrate(s['accepted'],w,h,rgb)
  (out/'SR_graph.json').write_text(json.dumps(graph));(out/'SR_audit.json').write_text(json.dumps(audit));(out/'SR.svg').write_text(svg_graph(graph,regions=True));(out/'SR_strokes.svg').write_text(svg_graph(graph));(out/'SR.json').write_text(json.dumps(dict(accepted=s['accepted'])))
  m=copy.deepcopy(next(m for m in rows if m['case']==case and m['condition']=='S'));m.update(condition='SR',integration=audit,filled_atomic_faces=audit['bounded_atomic_faces'],render_seconds={})
  for scale in [1,4]:m['render_seconds'][str(scale)]=render(out/'SR.svg',out/f'SR_{scale}x.png',w,h,scale)
  root=ET.parse(out/'S_detail.svg').getroot();roi=root.attrib['viewBox'];dim=list(map(float,roi.split()));g=ET.parse(out/'SR.svg').getroot();g.set('viewBox',roi);g.set('width',str(int(dim[2])));g.set('height',str(int(dim[3])));(out/'SR_detail.svg').write_text(ET.tostring(g,encoding='unicode'))
  for scale in [1,4,16]:m['render_seconds']['detail'+str(scale)]=render(out/'SR_detail.svg',out/f'SR_detail_{scale}x.png',int(dim[2]),int(dim[3]),scale)
  m['svg_bytes']=(out/'SR.svg').stat().st_size;m['rendered_coverage_fraction']=float((np.asarray(Image.open(out/'SR_1x.png').convert('RGBA'))[...,3]>0).mean());(out/'SR_metrics.json').write_text(json.dumps(m,indent=2));rows.append(m)
  print(case,'S+R',audit['bounded_atomic_faces'],flush=True)
 (E/'reports/METRICS.json').write_text(json.dumps(rows,indent=2))
```
