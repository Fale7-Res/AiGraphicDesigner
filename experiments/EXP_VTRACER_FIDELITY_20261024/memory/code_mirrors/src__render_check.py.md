# مرآة الكود التفصيلية: `src/render_check.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/render_check.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/render_check.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `20` (`Lines 1–20`)
- **بصمة الملف (`SHA-256`):** `d6cf535355b1fee8549c3dcf8a42a4d8a5dde0f01cf2f2a6c0915e435c4f1873`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `check` | `function` | `Lines 8–17` | `def check():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `check` — `Lines 8–17`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `8` إلى السطر `17` (`Lines 8–17`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 8–17`):**
```python
def check():
    output=ROOT/'renderer_check';output.mkdir(exist_ok=True);records={}
    for case in ['A03_burger_layers','A09_arabic_calligraphy']:
        directory=output/case;directory.mkdir(exist_ok=True);source=load_rgb(ROOT/'inputs'/f'{case}.png');h,w=source.shape[:2]
        svg=ROOT/'results'/case/'best.svg';png=directory/'cairo_native.png';start=time.perf_counter()
        cairosvg.svg2png(url=str(svg),write_to=str(png),output_width=w,output_height=h)
        cairo=load_rgb(png);native=load_rgb(ROOT/'results'/case/'best.png')
        records[case]={'renderer':'CairoSVG '+cairosvg.__version__,'wall_seconds':time.perf_counter()-start,'versus_inkscape':compare(native,cairo),'versus_source':compare(source,cairo)}
        render_svg(svg,directory/'inkscape_native400.png',w*4,h*4)
    (output/'results.json').write_text(json.dumps(records,indent=2));print(json.dumps(records,indent=2))
```
