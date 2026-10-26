# مرآة الكود التفصيلية: `run_benchmark.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_benchmark.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_benchmark.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `47` (`Lines 1–47`)
- **بصمة الملف (`SHA-256`):** `90a50e4dc71d34bb24cec86d9268cdbe8077b42d983c9cd4cee59724dcfafc95`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_benchmark` | `function` | `Lines 9–42` | `def run_benchmark(destination=ROOT):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_benchmark` — `Lines 9–42`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `42` (`Lines 9–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–42`):**
```python
def run_benchmark(destination=ROOT):
    destination=Path(destination).resolve();destination.mkdir(parents=True,exist_ok=True)
    protocol=json.loads((ROOT/'protocol.json').read_text());images=sorted((ROOT/'inputs').glob('*.png'))
    for p in images:
        if p.stem[:3] in protocol['development']:
            out=destination/'results'/p.stem
            if not (out/'ranking.json').exists():search(p,out)
    common={}
    for p in images:
        if p.stem[:3] not in protocol['development']:continue
        r=json.loads((destination/'results'/p.stem/'ranking.json').read_text())
        for v in r['ranked']:
            if v['phase']!='pilot':continue
            key=json.dumps(v['config'],sort_keys=True)
            common.setdefault(key,[]).append(v['score'])
    eligible=[(sum(scores)/4,key,scores) for key,scores in common.items() if len(scores)==4]
    if not eligible:raise RuntimeError('No successful common pilot across development')
    score,key,scores=max(eligible);config=json.loads(key)
    frozen=destination/'frozen_common.json'
    if frozen.exists():
        previous=json.loads(frozen.read_text());assert previous['config']==config
    else:
        frozen.write_text(json.dumps({'config':config,'development_mean_score':score,'development_scores':scores,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'config_sha256':hashlib.sha256(key.encode()).hexdigest(),'selection':'Only13shared pilots evaluated on4development images; holdout not used'},indent=2))
    for p in images:
        if p.stem[:3] not in protocol['holdout']:continue
        out=destination/'holdout_common'/p.stem
        if not (out/'ranking.json').exists():search(p,out,configs=[config],refine=False)
    # All eight common-preset evaluations complete BEFORE per-image holdout tuning.
    marker=destination/'holdout_evaluation_completed.json'
    if not marker.exists():marker.write_text(json.dumps({'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'frozen_sha256':hashlib.sha256(frozen.read_bytes()).hexdigest()}))
    for p in images:
        if p.stem[:3] not in protocol['holdout']:continue
        out=destination/'results'/p.stem
        if not (out/'ranking.json').exists():search(p,out)
```
