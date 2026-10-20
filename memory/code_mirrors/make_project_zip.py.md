# مرآة الكود التفصيلية: `make_project_zip.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `make_project_zip.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `make_project_zip.py`
- **الدور المعماري (`Architectural Role`):** Utility — Full Repository ZIP Archiver
- **إجمالي عدد الأسطر (`Total Lines`):** `35` (`Lines 1–35`)
- **بصمة الملف (`SHA-256`):** `4d22cd66883670a567abe194a5146daf460c693eb50c1904cf4ba794391be889`
- **الوصف التفصيلي:** أداة مساعدة لضغط كامل ملفات المشروع في أرشيف مضغوط واحد جاهز للنقل أو النسخ الاحتياطي السريع.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `جميع ملفات المستودع` | ملفات القواعد والذاكرة والوثائق والأدوات | يجمع كل شيء في ملف .zip واحد. |
| **يرمي إلى (`Throws To`)** | `ai_graphic_designer_project.zip` | الأرشيف المضغوط الكامل للمشروع | نسخة محمولة جاهزة للاستخدام. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `build_archive` | `function` | `Lines 19–31` | `def build_archive() -> Path:` | تجمع كافة ملفات المستودع (باستثناء ملفات الكاش المؤقت والأرشيف الناتج نفسه) وتضغطها بصيغة ZIP_DEFLATED. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `build_archive` — `Lines 19–31`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `19` إلى السطر `31` (`Lines 19–31`)
- **الوظيفة:** تجمع كافة ملفات المستودع (باستثناء ملفات الكاش المؤقت والأرشيف الناتج نفسه) وتضغطها بصيغة ZIP_DEFLATED.
- **الكود الفعلي (`Lines 19–31`):**
```python
def build_archive() -> Path:
    """Create a clean ZIP archive of all project files."""
    with ZipFile(OUTPUT_ZIP, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(SOURCE_DIR.rglob("*")):
            if not file_path.is_file():
                continue
            if file_path.resolve() == OUTPUT_ZIP.resolve():
                continue
            if any(part in EXCLUDED_DIRS for part in file_path.relative_to(SOURCE_DIR).parts[:-1]):
                continue
            archive.write(file_path, file_path.relative_to(SOURCE_DIR))
    print(f"تم إنشاء الأرشيف بنجاح: {OUTPUT_ZIP}")
    return OUTPUT_ZIP
```
