# مرآة الكود التفصيلية: `audit_exporter_calls.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `audit_exporter_calls.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `audit_exporter_calls.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `30` (`Lines 1–30`)
- **بصمة الملف (`SHA-256`):** `42e674eb5ed936549ac11b03620cadf6bef17849a8b945dea1f922241c09ce91`
- **الوصف التفصيلي:** # START CHANGE AGD-EXPORTER-AUDIT | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `audit` | `function` | `Lines 9–23` | `def audit(root):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `audit` — `Lines 9–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `23` (`Lines 9–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–23`):**
```python
def audit(root):
    hits=[];definitions=[];other=[]
    for path in sorted(root.rglob('*')):
        if path.suffix not in {'.py','.rs','.js','.ts'}:continue
        if any(x in {'.git','node_modules','.venv','venv','__pycache__','target','build','memory'} for x in path.parts):continue
        try:text=path.read_text(encoding='utf-8')
        except (UnicodeError,OSError):continue
        relative=path.relative_to(root).as_posix()
        for number,line in enumerate(text.splitlines(),1):
            if 'svg_graph(' in line:
                hits.append({'file':relative,'line':number,'text':line.strip()})
            if 'def svg_graph(' in line:definitions.append({'file':relative,'line':number})
            if any(token in line for token in ('def export_svg','def to_svg','fn to_svg','fn write_svg')):
                other.append({'file':relative,'line':number,'text':line.strip()})
    return {'scope':'Source inspection, not exhaustive dynamic dependency proof','svg_graph_mentions':hits,'svg_graph_definitions':definitions,'other_exporter_definitions':other}
```
