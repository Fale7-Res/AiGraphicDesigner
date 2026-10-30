# مرآة الكود التفصيلية: `infer_dexined.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `infer_dexined.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `infer_dexined.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `33` (`Lines 1–33`)
- **بصمة الملف (`SHA-256`):** `117e3676bd78a8274082767441d0e2d05c8aff342f9e2eac5631e9f2fbaaac7a`
- **الوصف التفصيلي:** # START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `infer` | `function` | `Lines 13–29` | `def infer(source,weights,out):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `infer` — `Lines 13–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `13` إلى السطر `29` (`Lines 13–29`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 13–29`):**
```python
def infer(source,weights,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    cv2.setNumThreads(2)
    rgb=np.asarray(Image.open(source).convert('RGB'));h,w=rgb.shape[:2]
    started=time.perf_counter();net=cv2.dnn.readNetFromONNX(str(weights))
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV);net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    load=time.perf_counter()-started
    blob=cv2.dnn.blobFromImage(rgb[...,::-1].copy(),1.,(256,256),(103.5,116.2,123.6),swapRB=False,crop=False)
    net.setInput(blob);started=time.perf_counter();outputs=net.forward();elapsed=time.perf_counter()-started
    logits=np.asarray(outputs,dtype=np.float32)
    # Published OpenCV wrapper treats last first-axis prediction as fused.
    fuse=np.squeeze(logits[-1]);assert fuse.ndim==2,fuse.shape
    probability=cv2.resize(expit(fuse),(w,h),interpolation=cv2.INTER_LINEAR)
    np.savez_compressed(out/'predictions.npz',raw_outputs=logits,native_sigmoid=probability)
    Image.fromarray(np.rint(probability*255).astype('uint8')).save(out/'sigmoid.png')
    report={'opencv':cv2.__version__,'model_load_seconds':load,'inference_seconds':elapsed,'output_shape':list(logits.shape),'native_size':[w,h],'sigmoid_min':float(probability.min()),'sigmoid_max':float(probability.max()),'model_sha256':hashlib.sha256(Path(weights).read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),'device':'CPU','threads':2,'inference_shape':[256,256],'resource_fallback':True,'normalization':'sigmoid only, no per-image minmax','training':False}
    (out/'inference.json').write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)
```
