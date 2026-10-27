# مرآة الكود التفصيلية: `run_inherited_tests.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_inherited_tests.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_inherited_tests.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `38` (`Lines 1–38`)
- **بصمة الملف (`SHA-256`):** `1013496010303464a80f7b2354181e9e8e8445e26024986b8255c2b5d193070b`
- **الوصف التفصيلي:** """Run historical tests unchanged, explicitly against the Windows derived optimizer."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_tests` | `function` | `Lines 16–35` | `def run_tests() -> bool:` | Load exact historical bytes, keeping unittest patch target optimizer local. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_tests` — `Lines 16–35`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `35` (`Lines 16–35`)
- **الوظيفة:** Load exact historical bytes, keeping unittest patch target optimizer local.
- **الكود الفعلي (`Lines 16–35`):**
```python
def run_tests() -> bool:
    """Load exact historical bytes, keeping unittest patch target optimizer local."""
    spec=importlib.util.spec_from_file_location('historical_optimizer_tests_unchanged',HISTORY)
    tests=importlib.util.module_from_spec(spec);spec.loader.exec_module(tests)
    suite=unittest.defaultTestLoader.loadTestsFromModule(tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    # START CHANGE AGD-CODEX-WIN-TEST-EVIDENCE | 2026-10-27T10:27:57Z | EDITED | Author: windows_extension
    report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
            'python_executable':sys.executable,'python_version':sys.version,'vtracer_version':version('vtracer'),
            'test_source':str(HISTORY),'test_source_sha256':hashlib.sha256(HISTORY.read_bytes()).hexdigest(),
            'optimizer_under_test':str(Path(optimizer.__file__).resolve()),
            'scope':'unchanged four historical tests against Windows-derived optimizer; historical direct Windows import remains unsupported',
            'tests_run':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
            'passed':result.wasSuccessful(),
            'error_details':[(str(test),traceback) for test,traceback in result.errors],
            'failure_details':[(str(test),traceback) for test,traceback in result.failures]}
    # END CHANGE AGD-CODEX-WIN-TEST-EVIDENCE | 2026-10-27T10:27:57Z | EDITED | Author: windows_extension
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports'/'inherited_tests.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return result.wasSuccessful()
```
