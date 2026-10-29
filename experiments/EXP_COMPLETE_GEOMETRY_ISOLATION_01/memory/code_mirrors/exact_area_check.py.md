# مرآة الكود التفصيلية: `exact_area_check.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `exact_area_check.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `exact_area_check.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `34` (`Lines 1–34`)
- **بصمة الملف (`SHA-256`):** `478231bde013ef861f0a8a593311625201acff907f49170e373ec82b80f2fdce`
- **الوصف التفصيلي:** # START CHANGE AGD-ISOLATION-EXACT-AREA-CHECK | 2026-10-29T06:48:34Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `segment_area` | `function` | `Lines 7–13` | `def segment_area(s):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `segment_area` — `Lines 7–13`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `7` إلى السطر `13` (`Lines 7–13`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 7–13`):**
```python
def segment_area(s):
 if s['type']=='L':return np.cross(np.array(s['p0']),np.array(s['p3']))/2
 p=np.array([s['p0'],s['p1'],s['p2'],s['p3']],float)
 c=np.array([p[0],3*(p[1]-p[0]),3*(p[2]-2*p[1]+p[0]),p[3]-3*p[2]+3*p[1]-p[0]])
 x=c[:,0];y=c[:,1];dx=np.arange(1,4)*x[1:];dy=np.arange(1,4)*y[1:]
 q=np.polynomial.polynomial.polymul(x,dy)-np.polynomial.polynomial.polymul(y,dx)
 return float(np.sum(q/np.arange(1,len(q)+1))/2)
```
