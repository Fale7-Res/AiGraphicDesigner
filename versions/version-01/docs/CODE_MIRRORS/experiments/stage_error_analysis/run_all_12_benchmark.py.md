# مرآة الكود التفصيلية للإصدار: `version-01/experiments/stage_error_analysis/run_all_12_benchmark.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/experiments/stage_error_analysis/run_all_12_benchmark.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `experiments/stage_error_analysis/run_all_12_benchmark.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `113` (`Lines 1–113`)
- **بصمة الملف (`SHA-256`):** `c14b5e91098a04ed91ad27be3072897857584e4762e60f0c5cc591902b9e4600`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `compute_fidelity` | `function` | `Lines 18–47` | `def compute_fidelity(orig_bgr: np.ndarray, rend_bgr: np.ndarray) -> dict:` | رمز برمجي موثق للإصدار. |
| `main` | `function` | `Lines 49–110` | `def main():` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `compute_fidelity` — `Lines 18–47`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `47` (`Lines 18–47`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 18–47`):**
```python
def compute_fidelity(orig_bgr: np.ndarray, rend_bgr: np.ndarray) -> dict:
    if orig_bgr.shape != rend_bgr.shape:
        rend_bgr = cv2.resize(rend_bgr, (orig_bgr.shape[1], orig_bgr.shape[0]))
    diff = orig_bgr.astype(np.float64) - rend_bgr.astype(np.float64)
    mse = float(np.mean(diff ** 2))
    rmse = float(math.sqrt(mse))
    psnr = float(10.0 * math.log10((255.0 ** 2) / mse)) if mse > 1e-10 else 99.0
    
    # Fast SSIM on luminance channel
    gray_ref = cv2.cvtColor(orig_bgr, cv2.COLOR_BGR2GRAY).astype(np.float64)
    gray_test = cv2.cvtColor(rend_bgr, cv2.COLOR_BGR2GRAY).astype(np.float64)
    mu_x = cv2.GaussianBlur(gray_ref, (11, 11), 1.5)
    mu_y = cv2.GaussianBlur(gray_test, (11, 11), 1.5)
    mu_x_sq = mu_x ** 2
    mu_y_sq = mu_y ** 2
    mu_xy = mu_x * mu_y
    sigma_x_sq = cv2.GaussianBlur(gray_ref ** 2, (11, 11), 1.5) - mu_x_sq
    sigma_y_sq = cv2.GaussianBlur(gray_test ** 2, (11, 11), 1.5) - mu_y_sq
    sigma_xy = cv2.GaussianBlur(gray_ref * gray_test, (11, 11), 1.5) - mu_xy
    c1 = (0.01 * 255.0) ** 2
    c2 = (0.03 * 255.0) ** 2
    ssim_map = ((2.0 * mu_xy + c1) * (2.0 * sigma_xy + c2)) / ((mu_x_sq + mu_y_sq + c1) * (sigma_x_sq + sigma_y_sq + c2))
    ssim = float(np.mean(ssim_map))
    
    return {
        "mse": round(mse, 2),
        "rmse": round(rmse, 2),
        "psnr_db": round(psnr, 2),
        "ssim": round(ssim, 4),
    }
```

### `main` — `Lines 49–110`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `110` (`Lines 49–110`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 49–110`):**
```python
def main():
    images_dir = ROOT / "AI_Graphic_Designer_Test_Images_Initial_12"
    outputs_dir = ROOT / "versions" / "version-01" / "experiments" / "preliminary_visual_tests" / "outputs"
    rendered_png_dir = ROOT / "versions" / "version-01" / "experiments" / "fidelity_diagnostics" / "rendered_pngs"
    rendered_png_dir.mkdir(parents=True, exist_ok=True)
    
    img_files = sorted([f for f in images_dir.glob("*.png")])
    print(f"Found {len(img_files)} test images in {images_dir.name}")
    
    pipeline = SequentialPipeline(error_tolerance_px=0.5, max_nodes_per_path=48, seed=0, enable_gradients=False)
    
    results = []
    total_time = 0.0
    
    for img_path in img_files:
        name = img_path.stem # e.g. A01_shield
        idx_prefix = name[:3] # e.g. A01
        
        t0 = time.perf_counter()
        svg_str, telemetry = pipeline.process_image(img_path, n_colors=16, min_contour_area=2.0)
        t_proc = (time.perf_counter() - t0) * 1000.0
        total_time += t_proc
        
        # Save committed SVG output
        out_svg = outputs_dir / f"{idx_prefix}_v01_vector.svg"
        out_svg.write_text(svg_str, encoding="utf-8")
        
        # Render SVG via PyMuPDF
        doc = pymupdf.open(stream=svg_str.encode("utf-8"), filetype="svg")
        pix = doc[0].get_pixmap()
        out_png = rendered_png_dir / f"{idx_prefix}_rendered.png"
        pix.save(str(out_png))
        
        # Read back rendered and original images
        orig_img = cv2.imread(str(img_path))
        rend_img = cv2.imread(str(out_png))
        fidelity = compute_fidelity(orig_img, rend_img)
        
        rec = {
            "image_id": idx_prefix,
            "filename": img_path.name,
            "dimensions": telemetry["dimensions"],
            "clusters": telemetry["clusters_count"],
            "paths": telemetry["total_paths"],
            "nodes": telemetry["total_nodes"],
            "svg_size_kb": round(telemetry["svg_size_bytes"] / 1024.0, 1),
            "proc_time_ms": round(t_proc, 1),
            "mse": fidelity["mse"],
            "rmse": fidelity["rmse"],
            "psnr_db": fidelity["psnr_db"],
            "ssim": fidelity["ssim"],
        }
        results.append(rec)
        print(f"[{idx_prefix}] {img_path.name:32s} | PSNR: {fidelity['psnr_db']:5.2f} dB | SSIM: {fidelity['ssim']:6.4f} | MSE: {fidelity['mse']:7.2f} | Paths: {telemetry['total_paths']:4d} | Nodes: {telemetry['total_nodes']:5d} | {rec['svg_size_kb']:6.1f} KB | {t_proc:5.1f} ms")

    summary_file = ROOT / "versions" / "version-01" / "experiments" / "fidelity_diagnostics" / "all_12_rerun_metrics.json"
    summary_file.write_text(json.dumps(results, indent=2), encoding="utf-8")
    
    print("\n" + "="*80)
    print(f"All 12 images successfully processed in {total_time:.1f} ms total!")
    print(f"Results saved to {summary_file}")
    print("="*80)
```
