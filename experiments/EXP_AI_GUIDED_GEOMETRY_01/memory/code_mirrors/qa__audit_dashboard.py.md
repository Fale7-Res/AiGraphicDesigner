# مرآة الكود التفصيلية: `qa/audit_dashboard.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `qa/audit_dashboard.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `qa/audit_dashboard.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `43` (`Lines 1–43`)
- **بصمة الملف (`SHA-256`):** `a3c9724e0810a5bdf448d2a6306ce353d7bfa672e821f7b5c0a9c7fdea3b2f2e`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `DashboardLinks` | `class` | `Lines 12–17` | `class DashboardLinks(HTMLParser):` | رمز برمجي موثق. |
| `DashboardLinks.__init__` | `method` | `Lines 13–15` | `def __init__(self):` | رمز برمجي موثق. |
| `DashboardLinks.handle_starttag` | `method` | `Lines 16–17` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `DashboardLinks` — `Lines 12–17`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `17` (`Lines 12–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–17`):**
```python
class DashboardLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('src','href') and value)
```

### `DashboardLinks.__init__` — `Lines 13–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `15` (`Lines 13–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–15`):**
```python
    def __init__(self):
        super().__init__()
        self.links=[]
```

### `DashboardLinks.handle_starttag` — `Lines 16–17`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `17` (`Lines 16–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–17`):**
```python
    def handle_starttag(self,tag,attrs):
        self.links.extend(value for key,value in attrs if key in ('src','href') and value)
```
