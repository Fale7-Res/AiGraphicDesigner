# مرآة الكود التفصيلية: `verify_portability.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `verify_portability.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `verify_portability.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `75` (`Lines 1–75`)
- **بصمة الملف (`SHA-256`):** `d0800fc15b226a3b3fc82c3bde03ab398d334ba1fdb8e2dc083380945588527c`
- **الوصف التفصيلي:** """Audit unchanged selection AST and helper math; test Windows process cleanup."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `verify_sources` | `function` | `Lines 13–40` | `def verify_sources() -> dict:` | Compare selected derived function ASTs excluding docstrings only. |
| `verify_sources.function_body` | `nested_function` | `Lines 21–25` | `def function_body(key: str,name: str) -> str:` | رمز برمجي موثق. |
| `verify_timeout` | `function` | `Lines 42–55` | `def verify_timeout() -> dict:` | Run an actual child+grandchild and verify whole observed tree exits. |
| `verify_trial_history_guard` | `function` | `Lines 58–69` | `def verify_trial_history_guard() -> dict:` | Ensure trial replay cannot overwrite even an arbitrary prior sentinel. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `verify_sources` — `Lines 13–40`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `40` (`Lines 13–40`)
- **الوظيفة:** Compare selected derived function ASTs excluding docstrings only.
- **الكود الفعلي (`Lines 13–40`):**
```python
def verify_sources() -> dict:
    """Compare selected derived function ASTs excluding docstrings only."""
    sources={
      'historical_optimizer':ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027'/'optimizer.py',
      'historical_search':ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'/'src'/'search.py',
      'historical_evaluate':ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'/'src'/'evaluate.py',
      'derived_optimizer':ROOT/'optimizer.py','derived_search':ROOT/'windows_search.py'}
    trees={key:ast.parse(path.read_text(encoding='utf-8')) for key,path in sources.items()}
    def function_body(key: str,name: str) -> str:
        function=next(n for n in trees[key].body if isinstance(n,ast.FunctionDef) and n.name==name)
        if isinstance(function.body[0],ast.Expr) and isinstance(function.body[0].value,ast.Constant):
            function.body=function.body[1:]
        return ast.dump(function,include_attributes=False)
    matched={}
    for name in ('canonical','pilots','neighborhood','optimize'):
        matched['optimizer.'+name]=function_body('historical_optimizer',name)==function_body('derived_optimizer',name)
    for name in ('prepare_input','extra_metrics','fidelity_score'):
        matched['search.'+name]=function_body('historical_search',name)==function_body('derived_search',name)
    report={'source_files':{key:{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for key,path in sources.items()},
            'function_ast_equivalence_excluding_docstrings':matched,
            'derived_copy_rationale':'Isolate Windows worker/resource and renderer adaptation; historical POSIX resource import prevents native Windows import. No runtime source rewriting or fake resource module.',
            'historical_evaluate':'Imported unchanged directly for load_rgb, compare, svg_structure.',
            # START CHANGE AGD-CODEX-WIN-SCOPE-EVIDENCE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
            'intended_historical_write_scope':'none; historical changes checked separately against Git baseline'}
    # END CHANGE AGD-CODEX-WIN-SCOPE-EVIDENCE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
    (ROOT/'source_provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if not all(matched.values()): raise AssertionError(matched)
    return report
```

### `verify_sources.function_body` — `Lines 21–25`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `25` (`Lines 21–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–25`):**
```python
    def function_body(key: str,name: str) -> str:
        function=next(n for n in trees[key].body if isinstance(n,ast.FunctionDef) and n.name==name)
        if isinstance(function.body[0],ast.Expr) and isinstance(function.body[0].value,ast.Constant):
            function.body=function.body[1:]
        return ast.dump(function,include_attributes=False)
```

### `verify_timeout` — `Lines 42–55`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `42` إلى السطر `55` (`Lines 42–55`)
- **الوظيفة:** Run an actual child+grandchild and verify whole observed tree exits.
- **الكود الفعلي (`Lines 42–55`):**
```python
def verify_timeout() -> dict:
    """Run an actual child+grandchild and verify whole observed tree exits."""
    folder=ROOT/'reports';folder.mkdir(exist_ok=True)
    # Only the test processes created here are terminated by the supervisor.
    code='import subprocess,sys,time; subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"]); time.sleep(30)'
    result=supervise([sys.executable,'-c',code],folder/'timeout_cleanup.log',timeout=1.5)
    surviving=[]
    for pid in result['observed_pids']:
        if psutil.pid_exists(pid): surviving.append(pid)
    result['surviving_observed_pids']=surviving
    result['passed']=result['termination_reason']=='timeout' and len(result['observed_pids'])>=2 and not surviving
    (folder/'timeout_cleanup.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    if not result['passed']: raise AssertionError(result)
    return result
```

### `verify_trial_history_guard` — `Lines 58–69`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `58` إلى السطر `69` (`Lines 58–69`)
- **الوظيفة:** Ensure trial replay cannot overwrite even an arbitrary prior sentinel.
- **الكود الفعلي (`Lines 58–69`):**
```python
def verify_trial_history_guard() -> dict:
    """Ensure trial replay cannot overwrite even an arbitrary prior sentinel."""
    with tempfile.TemporaryDirectory() as directory:
        folder=Path(directory);sentinel=folder/'prior-evidence.txt';sentinel.write_text('preserve',encoding='utf-8')
        rejected=False
        try: run_trial(folder/'not-opened.png',folder,OWNER)
        except FileExistsError: rejected=True
        preserved=sentinel.read_text(encoding='utf-8')=='preserve' and list(folder.iterdir())==[sentinel]
        report={'passed':rejected and preserved,'rejected_nonempty_trial':rejected,'prior_evidence_preserved':preserved}
    (ROOT/'reports'/'trial_history_guard.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if not report['passed']: raise AssertionError(report)
    return report
```
