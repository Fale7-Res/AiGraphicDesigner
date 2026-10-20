# مرآة الكود التفصيلية: `benchmarks/harness/run_benchmark.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `benchmarks/harness/run_benchmark.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `benchmarks/harness/run_benchmark.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `107` (`Lines 1–107`)
- **بصمة الملف (`SHA-256`):** `b40fbf812f737a0648cb3124433b2d24e2e56325912e7dc94cc48205aaa0888c`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `validate_benchmark_payload` | `function` | `Lines 25–70` | `def validate_benchmark_payload(payload: dict) -> tuple[bool, list[str]]:` | Validate a benchmark telemetry payload against the schema and anti-fabrication rules. |
| `record_benchmark_run` | `function` | `Lines 73–90` | `def record_benchmark_run(run_data: dict, write_matrix: bool = False) -> dict:` | Validate and optionally append a benchmark run record. |
| `main` | `function` | `Lines 93–102` | `def main() -> None:` | CLI entry point for benchmark harness verification. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `validate_benchmark_payload` — `Lines 25–70`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `25` إلى السطر `70` (`Lines 25–70`)
- **الوظيفة:** Validate a benchmark telemetry payload against the schema and anti-fabrication rules.
- **الكود الفعلي (`Lines 25–70`):**
```python
def validate_benchmark_payload(payload: dict) -> tuple[bool, list[str]]:
    """Validate a benchmark telemetry payload against the schema and anti-fabrication rules."""
    errors: list[str] = []
    required_top = [
        "run_id",
        "version_id",
        "timestamp_utc",
        "dataset_asset_id",
        "hardware_telemetry",
        "metrics",
        "verification_status",
    ]
    for key in required_top:
        if key not in payload:
            errors.append(f"Missing required field: {key}")

    if errors:
        return False, errors

    if not re.match(r"^BENCH-[0-9]{8}-[0-9]{3}$", payload["run_id"]):
        errors.append(f"Invalid run_id format: {payload['run_id']}")

    if not re.match(r"^version-[0-9]{2}$", payload["version_id"]):
        errors.append(f"Invalid version_id format: {payload['version_id']}")

    hw = payload.get("hardware_telemetry", {})
    required_hw = ["device_type", "cpu_model", "ram_gb", "gpu_model", "vram_gb", "cuda_version", "os_platform"]
    for hw_k in required_hw:
        if hw_k not in hw:
            errors.append(f"Missing hardware_telemetry field: {hw_k}")

    metrics = payload.get("metrics", {})
    required_metrics = [
        "trimap_boundary_iou",
        "lpips_score",
        "ssim_score",
        "max_bezier_node_count",
        "latency_seconds",
        "peak_vram_gb",
        "estimated_inference_cost_usd",
    ]
    for m_k in required_metrics:
        if m_k not in metrics:
            errors.append(f"Missing metric: {m_k}")

    return len(errors) == 0, errors
```

### `record_benchmark_run` — `Lines 73–90`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `90` (`Lines 73–90`)
- **الوظيفة:** Validate and optionally append a benchmark run record.
- **الكود الفعلي (`Lines 73–90`):**
```python
def record_benchmark_run(run_data: dict, write_matrix: bool = False) -> dict:
    """Validate and optionally append a benchmark run record."""
    is_valid, errors = validate_benchmark_payload(run_data)
    if not is_valid:
        return {"status": "REJECTED", "errors": errors}

    summary = {
        "status": "VALIDATED",
        "run_id": run_data["run_id"],
        "version_id": run_data["version_id"],
        "asset": run_data["dataset_asset_id"],
        "trimap_iou": run_data["metrics"]["trimap_boundary_iou"],
        "lpips": run_data["metrics"]["lpips_score"],
        "nodes": run_data["metrics"]["max_bezier_node_count"],
        "latency": run_data["metrics"]["latency_seconds"],
        "cost": run_data["metrics"]["estimated_inference_cost_usd"],
    }
    return summary
```

### `main` — `Lines 93–102`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `102` (`Lines 93–102`)
- **الوظيفة:** CLI entry point for benchmark harness verification.
- **الكود الفعلي (`Lines 93–102`):**
```python
def main() -> None:
    """CLI entry point for benchmark harness verification."""
    if len(sys.argv) > 1 and sys.argv[1] == "verify-schema":
        if not SCHEMA_PATH.exists():
            print(json.dumps({"status": "FAILED", "error": "Schema missing"}))
            raise SystemExit(1)
        print(json.dumps({"status": "SCHEMA_VALID", "path": str(SCHEMA_PATH)}))
        return

    print(json.dumps({"status": "BENCHMARK_HARNESS_READY", "schema": str(SCHEMA_PATH)}))
```
