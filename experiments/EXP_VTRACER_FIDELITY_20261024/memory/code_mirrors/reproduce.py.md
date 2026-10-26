# مرآة الكود التفصيلية: `reproduce.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `reproduce.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `reproduce.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `24` (`Lines 1–24`)
- **بصمة الملف (`SHA-256`):** `b6ccc4aafc187c2460ab31875ff4256a8c9ee9b7583c6f189d3b87ece95484f9`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `prepare` | `function` | `Lines 6–14` | `def prepare(destination):` | رمز برمجي موثق. |
| `execute` | `function` | `Lines 15–20` | `def execute(destination):` | رمز برمجي موثق. |
| `execute.run` | `nested_function` | `Lines 16–16` | `def run(*args):subprocess.run([sys.executable,*args],cwd=destination,check=True)` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `prepare` — `Lines 6–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `6` إلى السطر `14` (`Lines 6–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 6–14`):**
```python
def prepare(destination):
    destination=destination.resolve()
    if destination.exists():raise FileExistsError('Destination must not exist')
    if len(list((ROOT/'inputs').glob('*.png')))!=12:raise ValueError('Expected twelve inputs')
    destination.mkdir(parents=True)
    for name in ['src','inputs','baselines','annotations']:shutil.copytree(ROOT/name,destination/name,ignore=shutil.ignore_patterns('__pycache__','.*'))
    for name in ['run_benchmark.py','summarize.py','requirements.txt','protocol.json']:shutil.copy2(ROOT/name,destination/name)
    (destination/'reports').mkdir()
    return destination
```

### `execute` — `Lines 15–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `20` (`Lines 15–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–20`):**
```python
def execute(destination):
    def run(*args):subprocess.run([sys.executable,*args],cwd=destination,check=True)
    run('-m','unittest','discover','-s','src','-p','test*.py');run('run_benchmark.py');run('src/baselines.py')
    for case in ['A01_shield','A03_burger_layers','A05_orange_juice_transparency','A10_restaurant_logo']:
        run('src/refine.py','--source',f'inputs/{case}.png','--svg',f'results/{case}/trial_07/output.svg','--config',f'results/{case}/trial_07/config.json','--output',f'refinement/{case}')
    run('src/extension.py','development');run('src/extension.py','holdout');run('summarize.py');run('src/render_check.py');run('src/test_color_contract.py','--output','reports/color_contract')
```

### `execute.run` — `Lines 16–16`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `16` (`Lines 16–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–16`):**
```python
    def run(*args):subprocess.run([sys.executable,*args],cwd=destination,check=True)
```
