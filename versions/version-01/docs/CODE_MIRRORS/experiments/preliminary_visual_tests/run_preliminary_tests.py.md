# مرآة الكود التفصيلية للإصدار: `version-01/experiments/preliminary_visual_tests/run_preliminary_tests.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `versions/version-01/experiments/preliminary_visual_tests/run_preliminary_tests.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version version-01`.

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `experiments/preliminary_visual_tests/run_preliminary_tests.py`
- **الإصدار المعماري (`Architecture Version`):** `version-01`
- **إجمالي عدد الأسطر (`Total Lines`):** `96` (`Lines 1–96`)
- **بصمة الملف (`SHA-256`):** `d7676b4e1a56d621b6bf61377c9197cc15117397f16154cf8957ebad75008bb5`
- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `version-01`.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **حوكمة الإصدار الأب (`Parent Version`)** | `version-01` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |
| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_preliminary_tests` | `function` | `Lines 25–91` | `def run_preliminary_tests() -> dict:` | رمز برمجي موثق للإصدار. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_preliminary_tests` — `Lines 25–91`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `91` (`Lines 25–91`)
- **الوظيفة:** رمز برمجي موثق للإصدار.
- **الكود الفعلي (`Lines 25–91`):**
```python
def run_preliminary_tests() -> dict:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    pipeline = SequentialPipeline(error_tolerance_px=2.0, max_nodes_per_path=36)

    manifest_path = INPUT_DIR / "DATASET_MANIFEST.json"
    images_meta = {}
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            meta = json.load(f)
            for item in meta.get("images", []):
                images_meta[item["file"]] = item

    results: list[dict] = []
    print("=" * 80)
    print("STARTING PRELIMINARY VISUAL TESTS — VERSION 01 SEQUENTIAL BASELINE")
    print("=" * 80)

    for img_file in sorted(INPUT_DIR.glob("*.png")):
        meta_info = images_meta.get(img_file.name, {})
        img_id = meta_info.get("id", img_file.stem)
        difficulty = meta_info.get("difficulty", "unknown")

        print(f"\nProcessing [{img_id}] {img_file.name} (Tier: {difficulty})...")
        svg_content, telemetry = pipeline.process_image(
            image_path=img_file,
            n_colors=6,
            min_contour_area=16.0,
        )

        out_svg_path = OUTPUT_DIR / f"{img_id}_v01_vector.svg"
        with open(out_svg_path, "w", encoding="utf-8") as f:
            f.write(svg_content)

        res_entry = {
            "id": img_id,
            "filename": img_file.name,
            "difficulty": difficulty,
            "dimensions": telemetry["dimensions"],
            "clusters_count": telemetry["clusters_count"],
            "total_layers": telemetry["total_layers"],
            "total_paths": telemetry["total_paths"],
            "total_nodes": telemetry["total_nodes"],
            "elapsed_ms": telemetry["elapsed_ms"],
            "svg_size_bytes": telemetry["svg_size_bytes"],
            "svg_path": str(out_svg_path.relative_to(PROJECT_ROOT)),
        }
        results.append(res_entry)
        print(f"  -> Generated {telemetry['total_paths']} paths, {telemetry['total_nodes']} nodes, "
              f"{telemetry['svg_size_bytes']} bytes in {telemetry['elapsed_ms']} ms")

    summary_payload = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "version_id": "version-01",
        "pipeline_strategy": "Sequential Monolith (K-Means RGB/LAB + Schneider Bézier)",
        "test_status": "COMPLETED_PRELIMINARY_TESTS",
        "total_images_tested": len(results),
        "results": results,
    }

    summary_file = HERE / "results_summary.json"
    with open(summary_file, "w", encoding="utf-8") as f:
        json.dump(summary_payload, f, indent=2)

    print("\n" + "=" * 80)
    print(f"ALL 12 PRELIMINARY TESTS COMPLETED! Summary saved to {summary_file}")
    print("=" * 80)
    return summary_payload
```
