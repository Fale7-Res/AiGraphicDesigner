# مرآة الكود التفصيلية للإصدار: `version-01/experiments/stage_error_analysis/test_grad_step.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/experiments/stage_error_analysis/test_grad_step.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `experiments/stage_error_analysis/test_grad_step.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `85` (`Lines 1–85`)
- **بصمة الملف (`SHA-256`):** `b257d9dce81a6c74afadbea0aae31e46b85b140402ca6e6e2e0254344c6c9b8c`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `test_contour_203` | `function` | `Lines 15–82` | `def test_contour_203():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `test_contour_203` — `Lines 15–82`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `82` (`Lines 15–82`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 15–82`):**
```python
def test_contour_203():
    img = cv2.imread(str(ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"))
    smooth = cv2.bilateralFilter(img, 5, 25, 10)
    lab = cv2.cvtColor(smooth, cv2.COLOR_BGR2LAB)
    pixels = np.float32(lab.reshape(-1, 3))
    cv2.setRNGSeed(0)
    _, labels, centers = cv2.kmeans(pixels, 16, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2), 5, cv2.KMEANS_PP_CENTERS)
    labels_img = labels.reshape(img.shape[:2])

    mask = (labels_img == 7).astype(np.uint8) * 255
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[203]

    c_mask = np.zeros(img.shape[:2], dtype=np.uint8)
    cv2.drawContours(c_mask, [cnt], -1, 255, -1)
    ys, xs = np.where(c_mask > 0)
    bgr_vals = img[ys, xs].astype(float)
    mean_col = np.mean(bgr_vals, axis=0)

    y_c = ys - np.mean(ys)
    x_c = xs - np.mean(xs)
    X = np.column_stack([x_c, y_c])
    XtX = X.T @ X + np.eye(2)*1e-4
    XtY = X.T @ (bgr_vals - mean_col)
    slopes = np.linalg.solve(XtX, XtY)

    pred = mean_col + X @ slopes
    ss_tot = np.sum((bgr_vals - mean_col)**2)
    ss_res = np.sum((bgr_vals - pred)**2)
    r2 = 1.0 - (ss_res / ss_tot)
    print(f"Contour 203: pixels={len(xs)}, R2={r2:.3f}")

    y_min, y_max = np.percentile(ys, 5), np.percentile(ys, 95)
    x_mid = float(np.mean(xs))
    c_top = np.clip(mean_col + (y_min - np.mean(ys)) * slopes[1], 0, 255)
    c_bot = np.clip(mean_col + (y_max - np.mean(ys)) * slopes[1], 0, 255)
    hex_top = f"#{int(round(c_top[2])):02x}{int(round(c_top[1])):02x}{int(round(c_top[0])):02x}"
    hex_bot = f"#{int(round(c_bot[2])):02x}{int(round(c_bot[1])):02x}{int(round(c_bot[0])):02x}"
    print(f"Grad: (x={x_mid:.1f}, y={y_min:.1f}) {hex_top} -> (x={x_mid:.1f}, y={y_max:.1f}) {hex_bot}")

    cv2.setRNGSeed(42)
    p = SequentialPipeline()
    svg_base, _ = p.process_image(str(ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"), n_colors=16)
    
    doc_base = pymupdf.open(stream=svg_base.encode(), filetype="svg")
    pix_base = doc_base[0].get_pixmap()
    rend_base = cv2.cvtColor(np.frombuffer(pix_base.samples, dtype=np.uint8).reshape((249, 369, 3)), cv2.COLOR_RGB2BGR)
    mse_base = np.mean((img.astype(float) - rend_base.astype(float))**2)

    grad_def = (
        f'  <defs>\n'
        f'    <linearGradient id="test_exact" x1="{x_mid:.1f}" y1="{y_min:.1f}" x2="{x_mid:.1f}" y2="{y_max:.1f}" gradientUnits="userSpaceOnUse">\n'
        f'      <stop offset="0%" stop-color="{hex_top}" />\n'
        f'      <stop offset="100%" stop-color="{hex_bot}" />\n'
        f'    </linearGradient>\n'
        f'  </defs>\n'
    )
    svg_mod = svg_base.replace("</desc>\n", f"</desc>\n{grad_def}")
    # Replace first occurrence of fill in cluster 7
    svg_mod, n_sub = re.subn(r'(id="layer_c7_\d+"[^>]*fill=")#d29744(")', r'\g<1>url(#test_exact)\g<2>', svg_mod, count=1)
    print(f"Substitutions made: {n_sub}")
    
    doc_mod = pymupdf.open(stream=svg_mod.encode(), filetype="svg")
    pix_mod = doc_mod[0].get_pixmap()
    rend_mod = cv2.cvtColor(np.frombuffer(pix_mod.samples, dtype=np.uint8).reshape((249, 369, 3)), cv2.COLOR_RGB2BGR)
    mse_mod = np.mean((img.astype(float) - rend_mod.astype(float))**2)
    
    print(f"BASE MSE: {mse_base:.2f} -> EXACT GRADIENT MSE: {mse_mod:.2f} (Delta: {mse_mod - mse_base:+.2f})")
```
