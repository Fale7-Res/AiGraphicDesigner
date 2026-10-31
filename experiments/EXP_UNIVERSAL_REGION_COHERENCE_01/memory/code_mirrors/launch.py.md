# مرآة الكود التفصيلية: `launch.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `launch.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `launch.py`
- **الدور المعماري (`Architectural Role`):** Isolated universal geometry measurement/selection/integration/coherence research
- **إجمالي عدد الأسطر (`Total Lines`):** `23` (`Lines 1–23`)
- **بصمة الملف (`SHA-256`):** `a3716cac71a574c93375526e3638f2c9173a05b25c54ac181e44d7032b6d65cb`
- **الوصف التفصيلي:** # START CHANGE AGD-UNIVERSAL-LAUNCH | 2026-10-31T11:07:29Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen Classical trace evidence / P controls / native RGB; evaluator-only references only in measurement modules` | source coordinates, cubic arrays, source-evidence scores and validity ledgers | strict condition isolation; no new inference or appearance |
| **يرمي إلى (`Throws To`)** | `this isolated experiment and owner-local restricted fixture output` | SVG curves/atomic faces, PNG review evidence, loss/topology/resource metrics | research only; geometry NOT_ACCEPTED, architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `launch_universal` | `function` | `Lines 6–21` | `def launch_universal():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `launch_universal` — `Lines 6–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `21` (`Lines 6–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–21`):**
```python
def launch_universal():
 protocol=json.loads((E/'protocol.json').read_text());records=[];started=time.monotonic()
 for name,pin in protocol['pins'].items():assert hashlib.sha256(Path(name).read_bytes()).hexdigest()==pin['sha256'],name
 # Validate tree monitoring with a deliberately touched64MiBchild before claims.
 child=W/'universal_geometry/monitor_child.py';parent=W/'universal_geometry/monitor_parent.py'
 child.write_text('import time\nx=bytearray(64*1024*1024)\nfor i in range(0,len(x),4096):x[i]=1\ntime.sleep(2)\n')
 parent.write_text('import subprocess,sys\nsubprocess.run([sys.executable,r"'+str(child)+'"],check=True)\n')
 a=supervise([sys.executable,parent],E/'reports/monitor_normal.log',wall_seconds=8,memory_mib=256,reserve_mib=0,interval=.02);b=supervise([sys.executable,parent],E/'reports/monitor_stopped.log',wall_seconds=8,memory_mib=48,reserve_mib=0,interval=.02)
 assert a['exit_code']==0 and a['sampled_tree_RSS_peak_mib']-a['sampled_root_RSS_peak_mib']>48 and b['status']=='STOPPED_MEMORY'
 (E/'reports/MONITOR_VALIDATION.json').write_text(json.dumps(dict(normal=a,stop=b,passed=True),indent=2))
 for case in protocol['cases']:
  if time.monotonic()-started>5400:raise RuntimeError('totalbudget')
  out=(W/'universal_geometry/local_only'/case if case=='fine_features' else E/'results'/case)
  if (out/'WORKER.json').exists():raise RuntimeError('Do not rerun completed case')
  result=supervise([sys.executable,E/'universal_run.py',case],E/'reports'/(case+'.log'))
  records.append(dict(case=case,**result));(E/'reports/RESOURCES.json').write_text(json.dumps(records,indent=2));print(case,result['status'],result['wall_seconds'],result['sampled_tree_RSS_peak_mib'],flush=True)
```
