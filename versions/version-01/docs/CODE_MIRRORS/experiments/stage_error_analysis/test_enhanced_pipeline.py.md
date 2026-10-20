# مرآة الكود التفصيلية للإصدار: `version-01/experiments/stage_error_analysis/test_enhanced_pipeline.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/experiments/stage_error_analysis/test_enhanced_pipeline.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `experiments/stage_error_analysis/test_enhanced_pipeline.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `195` (`Lines 1–195`)
- **بصمة الملف (`SHA-256`):** `b89fd3b12d568751f8710bc4ac207ceda9c78d03950d8db18030b38a72f330a9`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_test` | `function` | `Lines 21–192` | `def run_test():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_test` — `Lines 21–192`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `192` (`Lines 21–192`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 21–192`):**
```python
def run_test():
    img_path = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12" / "A01_shield.png"
    img_bgr = cv2.imread(str(img_path))
    h, w = img_bgr.shape[:2]
    
    cv2.setRNGSeed(42)
    np.random.seed(42)
    
    smooth_bgr = cv2.bilateralFilter(img_bgr, d=5, sigmaColor=25, sigmaSpace=10)
    img_lab = cv2.cvtColor(smooth_bgr, cv2.COLOR_BGR2LAB)
    
    k = 24
    pixels = np.float32(img_lab.reshape(-1, 3))
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 25, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 1, cv2.KMEANS_PP_CENTERS)
    labels_img = labels.reshape((h, w)).astype(np.uint8)
    
    centers_lab = np.uint8(centers.reshape((1, k, 3)))
    centers_bgr = cv2.cvtColor(centers_lab, cv2.COLOR_LAB2BGR).reshape((k, 3))
    
    cluster_areas = [(np.sum(labels_img == ci), ci) for ci in range(k)]
    cluster_areas.sort(key=lambda x: x[0], reverse=True)
    bg_ci = cluster_areas[0][1]
    bg_hex = f"#{centers_bgr[bg_ci][2]:02x}{centers_bgr[bg_ci][1]:02x}{centers_bgr[bg_ci][0]:02x}"
    
    defs = []
    body_elements = [f'<rect width="{w}" height="{h}" fill="{bg_hex}" />']
    
    total_nodes = 0
    total_paths = 0
    
    for z_rank, (_, ci) in enumerate(cluster_areas):
        b, g, r = int(centers_bgr[ci][0]), int(centers_bgr[ci][1]), int(centers_bgr[ci][2])
        hex_color = f"#{r:02x}{g:02x}{b:02x}"
        mask = (labels_img == ci).astype(np.uint8) * 255
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        if hierarchy is None or len(contours) == 0:
            continue
            
        hierarchy_arr = hierarchy[0]
        for i, h_node in enumerate(hierarchy_arr):
            if h_node[3] != -1:
                continue
            outer_cnt = contours[i]
            area = cv2.contourArea(outer_cnt)
            if area < 2.0:
                continue
                
            outer_approx = cv2.approxPolyDP(outer_cnt, epsilon=0.5, closed=True)
            if len(outer_approx) < 3:
                continue
                
            outer_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in outer_approx]
            outer_segs = fit_schneider_bezier(outer_pts, max_error_px=0.5, max_nodes=48, closed=True)
            if not outer_segs:
                continue
            subpaths = [outer_segs]
            total_nodes += len(outer_segs)
            
            # Holes
            ch_idx = h_node[2]
            while ch_idx != -1:
                hole_cnt = contours[ch_idx]
                if cv2.contourArea(hole_cnt) >= 2.0:
                    hole_approx = cv2.approxPolyDP(hole_cnt, epsilon=0.5, closed=True)
                    if len(hole_approx) >= 3:
                        hole_pts = [Point2D(float(p[0][0]), float(p[0][1])) for p in hole_approx]
                        hole_segs = fit_schneider_bezier(hole_pts, max_error_px=0.5, max_nodes=48, closed=True)
                        if hole_segs:
                            subpaths.append(hole_segs)
                            total_nodes += len(hole_segs)
                ch_idx = hierarchy_arr[ch_idx][0]
                
            # Check linear gradient for this contour
            fill_val = hex_color
            if area >= 60.0:
                c_mask = np.zeros((h, w), dtype=np.uint8)
                cv2.drawContours(c_mask, [outer_cnt], -1, 255, -1)
                ch_idx = h_node[2]
                while ch_idx != -1:
                    cv2.drawContours(c_mask, [contours[ch_idx]], -1, 0, -1)
                    ch_idx = hierarchy_arr[ch_idx][0]
                    
                ys, xs = np.where(c_mask > 0)
                if len(xs) >= 40:
                    bgr_vals = img_bgr[ys, xs].astype(np.float64)
                    mean_col = np.mean(bgr_vals, axis=0)
                    std_col = np.std(bgr_vals, axis=0)
                    total_std = np.sqrt(np.mean(std_col**2))
                    
                    if total_std >= 8.0:
                        xc = xs - np.mean(xs)
                        yc = ys - np.mean(ys)
                        X = np.column_stack([xc, yc])
                        XtX = X.T @ X + np.eye(2) * 1e-4
                        XtY = X.T @ (bgr_vals - mean_col)
                        slopes = np.linalg.solve(XtX, XtY)
                        pred = mean_col + X @ slopes
                        ss_tot = np.sum((bgr_vals - mean_col)**2)
                        ss_res = np.sum((bgr_vals - pred)**2)
                        r2 = 1.0 - (ss_res / ss_tot) if ss_tot > 1e-5 else 0.0
                        
                        if r2 >= 0.40:
                            grad_x = float(np.mean(slopes[0, :]))
                            grad_y = float(np.mean(slopes[1, :]))
                            norm = math.hypot(grad_x, grad_y)
                            if norm > 1e-4:
                                ux, uy = grad_x / norm, grad_y / norm
                                t = xc * ux + yc * uy
                                t_min, t_max = float(np.percentile(t, 5)), float(np.percentile(t, 95))
                                if t_max - t_min >= 6.0:
                                    x1 = float(np.mean(xs) + t_min * ux)
                                    y1 = float(np.mean(ys) + t_min * uy)
                                    x2 = float(np.mean(xs) + t_max * ux)
                                    y2 = float(np.mean(ys) + t_max * uy)
                                    
                                    c_start = np.clip(mean_col + t_min * (slopes[0, :]*ux + slopes[1, :]*uy), 0, 255)
                                    c_end = np.clip(mean_col + t_max * (slopes[0, :]*ux + slopes[1, :]*uy), 0, 255)
                                    
                                    hex_start = f"#{int(c_start[2]):02x}{int(c_start[1]):02x}{int(c_start[0]):02x}"
                                    hex_end = f"#{int(c_end[2]):02x}{int(c_end[1]):02x}{int(c_end[0]):02x}"
                                    
                                    gid = f"grad_c{ci}_{i}"
                                    defs.append(
                                        f'<linearGradient id="{gid}" x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" gradientUnits="userSpaceOnUse">\n'
                                        f'      <stop offset="0%" stop-color="{hex_start}" />\n'
                                        f'      <stop offset="100%" stop-color="{hex_end}" />\n'
                                        f'    </linearGradient>'
                                    )
                                    fill_val = f"url(#{gid})"
                                    
            d_parts = []
            for sub in subpaths:
                if not sub:
                    continue
                start = sub[0].p0
                part = [f"M {start.x:.2f} {start.y:.2f}"]
                for seg in sub:
                    part.append(seg.to_svg_path_data())
                part.append("Z")
                d_parts.append(" ".join(part))
                
            d_attr = " ".join(d_parts)
            rule = ' fill-rule="evenodd"' if len(d_parts) > 1 else ''
            stroke_attr = f' stroke="{hex_color}" stroke-width="1.0" stroke-linejoin="round"'
            body_elements.append(f'<path id="layer_c{ci}_{i}" fill="{fill_val}"{rule}{stroke_attr} d="{d_attr}" />')
            total_paths += 1
            
    defs_str = "  <defs>\n    " + "\n    ".join(defs) + "\n  </defs>\n" if defs else ""
    svg_body = "\n  ".join(body_elements)
    svg_str = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">\n'
        f'  <desc>Generated by AI Graphic Designer version-01 (Gradient-Aware Stage A)</desc>\n'
        f'{defs_str}'
        f'  {svg_body}\n'
        f'</svg>'
    )
    
    out_svg_path = ROOT / "versions" / "version-01" / "experiments" / "stage_error_analysis" / "A01_test_improved.svg"
    out_svg_path.write_text(svg_str, encoding="utf-8")
    
    # Render with PyMuPDF
    doc = pymupdf.open(stream=svg_str.encode("utf-8"), filetype="svg")
    pix = doc[0].get_pixmap()
    out_png_path = ROOT / "versions" / "version-01" / "experiments" / "stage_error_analysis" / "A01_test_improved.png"
    pix.save(str(out_png_path))
    
    rendered_bgr = cv2.imread(str(out_png_path))
    metrics = compute_metrics(img_bgr, rendered_bgr)
    print("RESULTS FOR GRADIENT-AWARE PIPELINE ON A01_shield:")
    print(metrics)
    print(f"Total paths: {total_paths}, Total nodes: {total_nodes}, Linear Gradients: {len(defs)}")
```
