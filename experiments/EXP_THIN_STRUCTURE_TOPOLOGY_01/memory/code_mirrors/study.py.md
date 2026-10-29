# مرآة الكود التفصيلية: `study.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `study.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `study.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `30` (`Lines 1–30`)
- **بصمة الملف (`SHA-256`):** `fa718c2d2f799d1b1f70e5e5dc69b29f56ad70ccb0575971032106592ac1f373`
- **الوصف التفصيلي:** # START CHANGE AGD-THIN-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `destination` | `function` | `Lines 13–14` | `def destination(case):` | رمز برمجي موثق. |
| `load_baseline` | `function` | `Lines 16–20` | `def load_baseline(case):` | رمز برمجي موثق. |
| `initialize_labels` | `function` | `Lines 22–28` | `def initialize_labels(labels):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `destination` — `Lines 13–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `14` (`Lines 13–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–14`):**
```python
def destination(case):
    return (WORK/'thin_structure_topology/external_results' if case=='fine_features' else ROOT/'results')/case
```

### `load_baseline` — `Lines 16–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `20` (`Lines 16–20`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–20`):**
```python
def load_baseline(case):
    import numpy as np
    from PIL import Image
    base=inherited_case_dir(case)
    return np.asarray(Image.open(base/'working.png').convert('RGB')),np.load(base/'S_A.npy',allow_pickle=False),json.loads((base/'S_A_F_A_common_faces.json').read_text(encoding='utf-8'))
```

### `initialize_labels` — `Lines 22–28`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `28` (`Lines 22–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–28`):**
```python
def initialize_labels(labels):
    # Calls the existing unmodified external initializer, geometry primitives
    # only. The historical read-only import explicitly denies Cairo rendering.
    _,gm,fm,hashes=arena_modules()
    g=gm.construct(labels);stats=fm.initialize(g,labels.shape[1],labels.shape[0],tolerance=.8,smooth=1.)
    result=gm.serialize(g,labels.shape[1],labels.shape[0]);result['stats']=stats;result['external_source_hashes']=hashes
    return result
```
