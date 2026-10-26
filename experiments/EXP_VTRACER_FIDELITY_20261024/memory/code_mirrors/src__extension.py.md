# مرآة الكود التفصيلية: `src/extension.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `src/extension.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `src/extension.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `57` (`Lines 1–57`)
- **بصمة الملف (`SHA-256`):** `bdee43c83507b8d5ec09c289c28463c0aaedd482cf550f6a4217c7438c502107`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `development` | `function` | `Lines 13–33` | `def development():` | Three fixed mechanistic probes per development case; freeze one if it helps. |
| `holdout` | `function` | `Lines 35–50` | `def holdout():` | Apply one previously frozen extra configuration to other eight images. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `development` — `Lines 13–33`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `33` (`Lines 13–33`)
- **الوظيفة:** Three fixed mechanistic probes per development case; freeze one if it helps.
- **الكود الفعلي (`Lines 13–33`):**
```python
def development():
    """Three fixed mechanistic probes per development case; freeze one if it helps."""
    root=ROOT/'extension';root.mkdir(exist_ok=True)
    if (root/'freeze.json').exists():
        frozen=json.loads((root/'freeze.json').read_text())
        if frozen['winner_config'] not in PROBES:raise ValueError('Frozen configuration differs from declared probes')
        return frozen
    plan={'created_utc':datetime.now(timezone.utc).isoformat(),'development':DEVELOPMENT,'configs':PROBES,'reason':'Visible-color refit negligible; probe diagonal clustering switch at layer_difference0 vs1 and previously untested pixel cutout. Post-hoc diagnostic, no claim of exhaustive optimum.','selection':'Choose highest mean composite score among3probes, compare to pixelstacked0. Require mean score improvement>0.0001 before extending to holdout.'}
    if not (root/'plan.json').exists():(root/'plan.json').write_text(json.dumps(plan,indent=2))
    results={}
    for case in DEVELOPMENT:
        source=ROOT/'results'/case/'normalized.png';results[case]=[]
        for index,config in enumerate(PROBES):
            out=root/case/f'probe_{index}'
            result=json.loads((out/'result.json').read_text()) if (out/'result.json').exists() else run_trial(source,out,config)
            if result.get('status')!='ok':raise RuntimeError(f'Failed development probe: {out}')
            results[case].append(result);print(case,index,result.get('score'),flush=True)
    means=[sum(results[case][i].get('score',0) for case in DEVELOPMENT)/len(DEVELOPMENT) for i in range(3)]
    base=sum(json.loads((ROOT/'results'/case/'trial_07/result.json').read_text())['score'] for case in DEVELOPMENT)/len(DEVELOPMENT)
    winner=max(range(3),key=lambda i:means[i]);freeze={'frozen_utc':datetime.now(timezone.utc).isoformat(),'development_mean_scores':means,'base_pixel_stacked_mean':base,'winner_index':winner,'winner_config':PROBES[winner],'mean_gain':means[winner]-base,'advance_to_holdout':means[winner]-base>.0001,'development_results':results}
    (root/'freeze.json').write_text(json.dumps(freeze,indent=2));print({k:v for k,v in freeze.items() if k!='development_results'},flush=True)
```

### `holdout` — `Lines 35–50`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `50` (`Lines 35–50`)
- **الوظيفة:** Apply one previously frozen extra configuration to other eight images.
- **الكود الفعلي (`Lines 35–50`):**
```python
def holdout():
    """Apply one previously frozen extra configuration to other eight images."""
    root=ROOT/'extension';freeze=json.loads((root/'freeze.json').read_text())
    if not freeze['advance_to_holdout']:raise ValueError('Development gate failed; no holdout expansion')
    cases=[ROOT/'results'/p.stem for p in sorted((ROOT/'inputs').glob('*.png')) if p.stem not in DEVELOPMENT]
    if len(cases)!=8 or any(not (c/'normalized.png').exists() for c in cases):raise ValueError('Need exactly eight complete holdout inputs')
    for case in cases:
        if not case.is_dir() or case.name in DEVELOPMENT:continue
        if not (case/'normalized.png').exists():continue
        out=root/case.name/'frozen'
        if (out/'result.json').exists():
            if json.loads((out/'result.json').read_text()).get('status')!='ok':raise RuntimeError(f'Existing failed holdout: {out}')
            continue
        r=run_trial(case/'normalized.png',out,freeze['winner_config'])
        if r.get('status')!='ok':raise RuntimeError(f'Failed holdout: {out}')
        print(case.name,r.get('score'),flush=True)
```
