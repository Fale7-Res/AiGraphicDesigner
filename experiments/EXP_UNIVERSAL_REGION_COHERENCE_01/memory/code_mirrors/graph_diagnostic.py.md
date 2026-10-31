# مرآة الكود التفصيلية: `graph_diagnostic.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `graph_diagnostic.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `graph_diagnostic.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `23` (`Lines 1–23`)
- **بصمة الملف (`SHA-256`):** `029e0e2f2583f8bfe234081cf4b75b255391b356ecd82c62958448176181dd54`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-GRAPH-DIAG | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `endpoint_graph_stats` | `function` | `Lines 5–13` | `def endpoint_graph_stats(paths):` | رمز برمجي موثق. |
| `endpoint_graph_stats.find` | `nested_function` | `Lines 7–10` | `def find(a):` | رمز برمجي موثق. |
| `graph_diagnostic` | `function` | `Lines 14–21` | `def graph_diagnostic():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `endpoint_graph_stats` — `Lines 5–13`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `5` إلى السطر `13` (`Lines 5–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 5–13`):**
```python
def endpoint_graph_stats(paths):
 parent={};degree=collections.Counter()
 def find(a):
  parent.setdefault(a,a)
  if parent[a]!=a:parent[a]=find(parent[a])
  return parent[a]
 for p in paths:
  a,b=tuple(p[0]),tuple(p[-1]);ra,rb=find(a),find(b);parent[ra]=rb;degree[a]+=1;degree[b]+=1
 components=len({find(a) for a in parent});return dict(edges=len(paths),vertices=len(parent),components=components,cycle_rank=len(paths)-len(parent)+components,junctions=sum(d>=3 for d in degree.values()),degree1_ends=sum(d==1 for d in degree.values()),limit='Exact trace-endpoint multigraph potential only; cycles are not validated simple faces, physical regions or semantic holes.')
```

### `endpoint_graph_stats.find` — `Lines 7–10`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `10` (`Lines 7–10`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–10`):**
```python
 def find(a):
  parent.setdefault(a,a)
  if parent[a]!=a:parent[a]=find(parent[a])
  return parent[a]
```

### `graph_diagnostic` — `Lines 14–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `21` (`Lines 14–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–21`):**
```python
def graph_diagnostic():
 rows=[]
 for case in json.loads((E/'protocol.json').read_text())['cases']:
  out=output_folder(case);f=json.loads((out/'frozen_traces.json').read_text());raw={t['trace_id']:t for t in f['traces']};p=json.loads((out/'P.json').read_text());s=json.loads((out/'S.json').read_text())
  paths={'all_raw':[t['source_points_xy'] for t in f['traces']],'eligible6':[t['source_points_xy'] for t in f['traces'] if t['length_px']>=6]}
  for tag,d in [('P_selected',p),('S_selected',s)]:paths[tag]=[raw[t['trace_id']]['source_points_xy'] for t in d['traces'] if t['selection']=='selected']
  row=dict(case=case,stages={k:endpoint_graph_stats(v) for k,v in paths.items()});rows.append(row);(out/'endpoint_graph_diagnostic.json').write_text(json.dumps(row,indent=2));print(case,[(k,v['cycle_rank'],v['degree1_ends']) for k,v in row['stages'].items()])
 (E/'reports/ENDPOINT_GRAPH_DIAGNOSTIC.json').write_text(json.dumps(rows,indent=2))
```
