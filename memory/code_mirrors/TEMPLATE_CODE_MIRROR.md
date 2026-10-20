# قالب مرآة الملف البرمجي (`TEMPLATE_CODE_MIRROR.md`)

> يُستخدم هذا القالب (أو يُولد آلياً عبر `python tools/memory_guard/sync_code_mirrors.py --write`) لكل ملف برمجي في المشروع داخل `memory/code_mirrors/`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `path/to/file.py`
- **الدور المعماري (`Architectural Role`):** وصف واضح لوظيفة الملف في النظام.
- **إجمالي عدد الأسطر (`Total Lines`):** `N`
- **بصمة الملف (`SHA-256`):** `<sha256>`

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related File / Endpoint`) | ماذا يأخذ أو يرمي؟ (`Data / Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From / Upstream`)** | `path/to/caller.py` | يستقبل كائن كذا أو يُستدعى من دالة كذا | إذا تغيرت مدخلات هذا الملف يجب تحديث المستدعي. |
| **يرمي إلى (`Throws To / Downstream`)** | `path/to/callee.py` | يرسل مخرجات كذا أو يستدعي دالة كذا | إذا تغير هيكل المخرجات يجب تحديث المستقبل. |

## 3. فهرس الدوال والكلاسات (`Functions & Classes Summary`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Lines Start–End`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `example_func` | `function` | `Lines 1–5` | `example_func() -> None` | شرح دقيق لما تفعله الدالة لمنع تكرارها. |

## 4. التفاصيل بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

#### `example_func` (`Lines 1–5`)
- **الوظيفة:** تطبع رسالة ترحيبية وتتحقق من جاهزية البيئة.
- **الكود الفعلي (`Lines 1–5`):**
```python
def example_func() -> None:
    msg = "hello world"
    print(msg)
    return None
```
