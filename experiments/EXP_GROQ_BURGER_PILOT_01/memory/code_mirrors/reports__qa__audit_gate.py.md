# مرآة الكود التفصيلية: `reports/qa/audit_gate.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `reports/qa/audit_gate.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `reports/qa/audit_gate.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `54` (`Lines 1–54`)
- **بصمة الملف (`SHA-256`):** `d7a4e90530527f9a8515fcda58daef173dcbd2c16199e10376c5031a021eea05`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PilotGateLinkAudit` | `class` | `Lines 26–31` | `class PilotGateLinkAudit(HTMLParser):` | رمز برمجي موثق. |
| `PilotGateLinkAudit.__init__` | `method` | `Lines 27–29` | `def __init__(self):` | رمز برمجي موثق. |
| `PilotGateLinkAudit.handle_starttag` | `method` | `Lines 30–31` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PilotGateLinkAudit` — `Lines 26–31`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `31` (`Lines 26–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–31`):**
```python
class PilotGateLinkAudit(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('href','src') and value)
```

### `PilotGateLinkAudit.__init__` — `Lines 27–29`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `29` (`Lines 27–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–29`):**
```python
    def __init__(self):
        super().__init__()
        self.links=[]
```

### `PilotGateLinkAudit.handle_starttag` — `Lines 30–31`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `31` (`Lines 30–31`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–31`):**
```python
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('href','src') and value)
```
