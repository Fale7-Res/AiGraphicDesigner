# مرآة الكود التفصيلية: `run_cycle.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_cycle.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_cycle.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `85` (`Lines 1–85`)
- **بصمة الملف (`SHA-256`):** `13de4014b93758371f1deb20ae2ad559c6ef7c0f4f0014290e1c7b0ae6e2f733`
- **الوصف التفصيلي:** # START CHANGE AGD-BOTTLENECK-RUNNER | 2026-10-28T03:34:28Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `verify_inventory` | `function` | `Lines 8–14` | `def verify_inventory(path):` | رمز برمجي موثق. |
| `artifact_inventory` | `function` | `Lines 16–21` | `def artifact_inventory(target):` | رمز برمجي موثق. |
| `run_bounded` | `function` | `Lines 23–27` | `def run_bounded(name,args,timeout):` | رمز برمجي موثق. |
| `oracle_dashboard` | `function` | `Lines 29–35` | `def oracle_dashboard():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `verify_inventory` — `Lines 8–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `14` (`Lines 8–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–14`):**
```python
def verify_inventory(path):
    record=json.loads(Path(path).read_text(encoding='utf-8'))
    if not record.get('files'):raise ValueError('Missing artifact inventory')
    for relative,row in record['files'].items():
        file=(ROOT/relative).resolve()
        if not file.is_relative_to(ROOT.resolve()):raise ValueError('Inventory path outside experiment')
        assert file.is_file() and hashlib.sha256(file.read_bytes()).hexdigest()==row['sha256'],relative
```

### `artifact_inventory` — `Lines 16–21`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `21` (`Lines 16–21`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–21`):**
```python
def artifact_inventory(target):
    target=Path(target);files={}
    for file in target.rglob('*'):
        if file.is_file() and file.name not in ['FILE_INVENTORY.json','index.html']:
            files[file.relative_to(ROOT).as_posix()]={'bytes':file.stat().st_size,'sha256':hashlib.sha256(file.read_bytes()).hexdigest()}
    (target/'FILE_INVENTORY.json').write_text(json.dumps({'files':files},indent=2))
```

### `run_bounded` — `Lines 23–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `27` (`Lines 23–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 23–27`):**
```python
def run_bounded(name,args,timeout):
    result=monitor([sys.executable,*map(str,args)],ROOT/'reports'/f'{name}.log',timeout,4096)
    (ROOT/'reports'/f'{name}_resources.json').write_text(json.dumps(result,indent=2))
    if result['returncode'] or result['termination_reason']:raise RuntimeError(result)
    print(name,result,flush=True)
```

### `oracle_dashboard` — `Lines 29–35`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `29` إلى السطر `35` (`Lines 29–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 29–35`):**
```python
def oracle_dashboard():
    rows=[]
    for folder in sorted((ROOT/'results/oracle').glob('K*')):
        rows.append(f'<h2>{folder.name}</h2><p>Exact geometry is privileged diagnostic data; not a deployable reconstruction.</p>')
        for name in ['comparison.png','center_4x.png','center_16x.png']:rows.append(f'<div style="overflow:auto"><img src="{folder.name}/{name}"></div>')
        rows.append('<p>'+' | '.join(f'<a href="{folder.name}/{name}.svg">{name}</a>' for name in ['oracle_truth','oracle_C','oracle_D'])+'</p>')
    (ROOT/'results/oracle/index.html').write_text('<!doctype html><meta charset="utf-8"><title>Geometry oracle</title><h1>Geometry oracle — NOT_APPROVED architecture</h1>'+''.join(rows),encoding='utf-8')
```
