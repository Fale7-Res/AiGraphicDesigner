# مرآة الكود التفصيلية: `safe_monitor.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `safe_monitor.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `safe_monitor.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `45` (`Lines 1–45`)
- **بصمة الملف (`SHA-256`):** `ab0d38aa660b84b61309428bcd38e4cb3f3ffe7dcb08a0d66d6a0acf10b0b812`
- **الوصف التفصيلي:** """Bounded isolated Windows research workers; PID reuse guarded, no history edits."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `monitor` | `function` | `Lines 7–44` | `def monitor(command,log,timeout=900,memory_mib=4096):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `monitor` — `Lines 7–44`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `44` (`Lines 7–44`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–44`):**
```python
def monitor(command,log,timeout=900,memory_mib=4096):
    start=time.monotonic();peak=0;samples=0;reason=None;identities={}
    with Path(log).open('w',encoding='utf-8') as stream:
        p=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        root=psutil.Process(p.pid)
        while p.poll() is None:
            try:members=[root]+root.children(recursive=True)
            except psutil.Error:members=[]
            rss=0
            for child in members:
                try:identities[(child.pid,child.create_time())]=None;rss+=child.memory_info().rss
                except psutil.Error:pass
            peak=max(peak,rss);samples+=1
            if time.monotonic()-start>timeout:reason='timeout';break
            if rss>memory_mib*1024**2:reason='sampled_memory_limit';break
            time.sleep(.05)
        if reason:
            for pid,birth in identities:
                try:
                    child=psutil.Process(pid)
                    if child.create_time()==birth:child.kill()
                except psutil.Error:pass
            if p.poll() is None:p.kill()
        code=p.wait(timeout=15)
        remaining=[]
        if reason:
            deadline=time.monotonic()+2
            while True:
                remaining=[]
                for pid,birth in identities:
                    try:
                        child=psutil.Process(pid)
                        if child.create_time()==birth and child.is_running():remaining.append(pid)
                    except psutil.NoSuchProcess:pass
                    except psutil.Error:remaining.append(pid)
                if not remaining or time.monotonic()>=deadline:break
                time.sleep(.05)
    return {'returncode':code,'termination_reason':reason,'wall_seconds':time.monotonic()-start,'sampled_tree_peak_mib':peak/1024**2,'samples':samples,'cleanup_unverified_pids':remaining,'note':'50ms requested sampling plus enumeration overhead; PID/create-time identity checked before killing only owned observed workers; bounded2s descendant drain ontimeout, errors reported not hidden; short peaks or unobserved descendants may be missed'}
```
