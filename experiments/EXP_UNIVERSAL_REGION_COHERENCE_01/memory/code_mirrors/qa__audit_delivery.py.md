# مرآة الكود التفصيلية: `qa/audit_delivery.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_delivery.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_delivery.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `44` (`Lines 1–44`)
- **بصمة الملف (`SHA-256`):** `8132136c3a524ed5fa7a6e9a2ec7015740a35eeecb17689b1b4ae3dca341cd9f`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `Links` | `class` | `Lines 12–16` | `class Links(HTMLParser):` | رمز برمجي موثق. |
| `Links.__init__` | `method` | `Lines 13–13` | `def __init__(self):super().__init__();self.links=[]` | رمز برمجي موثق. |
| `Links.handle_starttag` | `method` | `Lines 14–16` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `Links` — `Lines 12–16`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `16` (`Lines 12–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–16`):**
```python
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key in ('href','src') and value:self.links.append(value)
```

### `Links.__init__` — `Lines 13–13`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `13` (`Lines 13–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–13`):**
```python
    def __init__(self):super().__init__();self.links=[]
```

### `Links.handle_starttag` — `Lines 14–16`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `16` (`Lines 14–16`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–16`):**
```python
    def handle_starttag(self,tag,attrs):
        for key,value in attrs:
            if key in ('href','src') and value:self.links.append(value)
```
