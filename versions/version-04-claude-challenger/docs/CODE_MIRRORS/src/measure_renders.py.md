# مرآة الكود التفصيلية للإصدار: `version-04-claude-challenger/src/measure_renders.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-04-claude-challenger/src/measure_renders.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-04-claude-challenger`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/measure_renders.py`
- **الإصدار المعماري (`Architecture Version`):** `version-04-claude-challenger`
- **إجمالي عدد الأسطر (`Total Lines`):** `39` (`Lines 1–39`)
- **بصمة الملف (`SHA-256`):** `45fe06f082884c158edd4f35f8a8cd2500a12c2d40d35880944da130d0029582`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-04-claude-challenger`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-04-claude-challenger` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `main` | `function` | `Lines 13–38` | `def main():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `main` — `Lines 13–38`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `38` (`Lines 13–38`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 13–38`):**
```python
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--ids',default='A01,A02,A03,A04,A05,A06,A07,A08,A09,A10,A11,A12')
    ap.add_argument('--inkscape',default='inkscape')
    args=ap.parse_args()
    if shutil.which(args.inkscape) is None and not Path(args.inkscape).exists(): raise SystemExit('Inkscape not found')
    target=OUT/'metrics'/'render_performance.csv'; target.parent.mkdir(parents=True,exist_ok=True)
    existing={}
    if target.exists():
        with target.open(newline='',encoding='utf-8') as f:
            for r in csv.DictReader(f): existing[r['image_id']]=r
    base=OUT/'rendered'/'performance_v01'; new=OUT/'rendered'/'performance_v04'
    base.mkdir(parents=True,exist_ok=True); new.mkdir(parents=True,exist_ok=True)
    for aid in [x.strip() for x in args.ids.split(',') if x.strip()]:
        src_path=next((p for p in SRC_DIR.glob(f'{aid}_*.png')),None)
        if src_path is None: raise FileNotFoundError(f'No source for {aid}')
        src=load_rgb(src_path); h,w=src.shape[:2]
        v01=V01_SVG_DIR/f'{aid}_v01_vector.svg'
        v04=next(OUT.joinpath('outputs').glob(f'{aid}_*_v04.svg'))
        t0=rasterize_svg(v01,base/f'{aid}_v01.png',w,h,args.inkscape)
        t1=rasterize_svg(v04,new/f'{aid}_v04.png',w,h,args.inkscape)
        existing[aid]={'image_id':aid,'width':w,'height':h,'renderer':'Inkscape CLI','v01_render_ms':round(t0,3),'v04_render_ms':round(t1,3),'v01_svg_bytes':v01.stat().st_size,'v04_svg_bytes':v04.stat().st_size}
        rows=[existing[k] for k in sorted(existing)]
        with target.open('w',newline='',encoding='utf-8') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader(); writer.writerows(rows)
        print(f'{aid}: V01 {t0:.1f} ms, V04 hybrid {t1:.1f} ms',flush=True)
```
