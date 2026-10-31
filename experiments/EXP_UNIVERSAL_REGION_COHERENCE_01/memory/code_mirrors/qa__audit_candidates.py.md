# مرآة الكود التفصيلية: `qa/audit_candidates.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_candidates.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_candidates.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `151` (`Lines 1–151`)
- **بصمة الملف (`SHA-256`):** `1407317ce9416781e5d0bee4a86111f4dec237b311cecf43e1276722a5cda218`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `check` | `function` | `Lines 22–24` | `def check(ok, message):` | رمز برمجي موثق. |
| `sampled` | `function` | `Lines 26–29` | `def sampled(curves, count=65):` | رمز برمجي موثق. |
| `parse_svg` | `function` | `Lines 31–64` | `def parse_svg(path, expected=None):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `check` — `Lines 22–24`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `24` (`Lines 22–24`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 22–24`):**
```python
def check(ok, message):
    if not ok:
        failures.append(message)
```

### `sampled` — `Lines 26–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `29` (`Lines 26–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–29`):**
```python
def sampled(curves, count=65):
    u = np.linspace(0, 1, count)[:,None]
    pieces = [((1-u)**3*c[0] + 3*(1-u)**2*u*c[1] + 3*(1-u)*u*u*c[2] + u**3*c[3]) for c in np.asarray(curves)]
    return np.concatenate([x[:-1] for x in pieces]+[pieces[-1][-1:]])
```

### `parse_svg` — `Lines 31–64`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `64` (`Lines 31–64`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–64`):**
```python
def parse_svg(path, expected=None):
    root = ET.parse(path).getroot()
    all_paths = []
    for element in root.iter():
        tag = element.tag.rsplit('}',1)[-1]
        check(tag in ('svg','path'), str(path)+': unexpected SVG element '+tag)
        if tag != 'path':
            continue
        tokens = token.findall(element.attrib.get('d',''))
        i = 0
        substart = None
        current = None
        curves = []
        closes = 0
        while i < len(tokens):
            command=tokens[i];i+=1
            if command=='M':
                current=np.array([float(x) for x in tokens[i:i+2]]);i+=2;substart=current.copy()
            elif command=='C':
                check(current is not None,str(path)+': cubic before move')
                coords=np.array([float(x) for x in tokens[i:i+6]]).reshape(3,2);i+=6
                curves.append(np.vstack([current,coords]));current=coords[-1]
            elif command=='Z':
                check(substart is not None,str(path)+': close before move')
                check(np.array_equal(current,substart),str(path)+': unintended close line')
                current=substart.copy();closes+=1
            else:
                raise AssertionError(str(path)+': unexpected command '+command)
        all_paths.append({'curves':curves,'closes':closes})
    if expected is not None:
        check(len(all_paths)==len(expected),str(path)+': path count does not match accepted records')
        for a,b in zip(all_paths,expected):
            check(np.array_equal(np.asarray(a['curves']),np.asarray(b['curves'])),str(path)+': controls differ from accepted record')
    return len(all_paths)
```
