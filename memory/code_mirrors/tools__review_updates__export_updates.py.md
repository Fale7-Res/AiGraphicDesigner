# مرآة الكود التفصيلية: `tools/review_updates/export_updates.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/review_updates/export_updates.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/review_updates/export_updates.py`
- **الدور المعماري (`Architectural Role`):** Portable Review Governance — Incremental Update Exporter & Validator
- **إجمالي عدد الأسطر (`Total Lines`):** `153` (`Lines 1–153`)
- **بصمة الملف (`SHA-256`):** `08d9cb3aace38b54ef6c112d4ff4e9d775fe08c5df546711f45740be938383e1`
- **الوصف التفصيلي:** ينشئ حزم مراجعة تراكمية مضغوطة (UPDATE-NNNN.zip) في مجلد updates/ مع حساب بصمات SHA-256 والتحقق من سلامة الأرشيف وفصل حالة التصدير عن حالة تأكيد المراجع.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `جميع ملفات المشروع + updates/baselines/state.json` | الملفات الحالية وبصمات SHA-256 الخاصة بها | يرصد الملفات المضافة أو المعدلة أو المحذوفة منذ آخر خط أساس. |
| **يرمي إلى (`Throws To`)** | `updates/packages/UPDATE-NNNN.zip & updates/latest/AI_DESIGNER_LATEST.zip & updates/UPDATE_HISTORY.md` | حزمة المراجعة المضغوطة وملفUPDATE_MANIFEST.json وسجل التحديثات | يمكّن المالك من مراجعة نسخ المشروع بشكل تراكمي وموثوق. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `compute_sha256` | `function` | `Lines 26–32` | `def compute_sha256(file_path: Path) -> str:` | تحسب بصمة SHA-256 لأي ملف على القرص بدقة. |
| `scan_workspace_files` | `function` | `Lines 35–46` | `def scan_workspace_files() -> dict[str, dict]:` | تمسح ملفات المشروع المصدرية التي تدخل في نطاق المراجعة مع استبعاد الحزم المولدة نفسها لمنع التكرار اللانهائي. |
| `export_package` | `function` | `Lines 49–98` | `def export_package() -> dict:` | تنشئ حزمة تحديث مرقمة جديدة (مثل UPDATE-0001) وتكتب المانيفست والأرشيف المضغوط وتحدث state.json. |
| `validate_package` | `function` | `Lines 101–113` | `def validate_package(update_id: str) -> dict:` | تتحقق من سلامة ملف الـ ZIP والمانيفست وتطابق بصمات SHA-256 لجميع الملفات المضمنة. |
| `acknowledge_package` | `function` | `Lines 116–126` | `def acknowledge_package(update_id: str, reviewer: str, note: str) -> dict:` | تسجل تأكيد استلام ومراجعة الحزمة من قِبل المستخدم عند تمرير --confirm-reviewed صراحةً. |
| `main` | `function` | `Lines 129–149` | `def main() -> None:` | تعالج أوامر سطر الأوامر (export, validate, status, acknowledge). |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `compute_sha256` — `Lines 26–32`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `32` (`Lines 26–32`)
- **الوظيفة:** تحسب بصمة SHA-256 لأي ملف على القرص بدقة.
- **الكود الفعلي (`Lines 26–32`):**
```python
def compute_sha256(file_path: Path) -> str:
    """Compute hex SHA-256 digest of a file."""
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
```

### `scan_workspace_files` — `Lines 35–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `35` إلى السطر `46` (`Lines 35–46`)
- **الوظيفة:** تمسح ملفات المشروع المصدرية التي تدخل في نطاق المراجعة مع استبعاد الحزم المولدة نفسها لمنع التكرار اللانهائي.
- **الكود الفعلي (`Lines 35–46`):**
```python
def scan_workspace_files() -> dict[str, dict]:
    """Scan all first-party tracked files and return path -> {sha256, size}."""
    records: dict[str, dict] = {}
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts[:-1]):
            continue
        rel = p.relative_to(ROOT).as_posix()
        records[rel] = {"sha256": compute_sha256(p), "size": p.stat().st_size}
    return records
```

### `export_package` — `Lines 49–98`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `49` إلى السطر `98` (`Lines 49–98`)
- **الوظيفة:** تنشئ حزمة تحديث مرقمة جديدة (مثل UPDATE-0001) وتكتب المانيفست والأرشيف المضغوط وتحدث state.json.
- **الكود الفعلي (`Lines 49–98`):**
```python
def export_package() -> dict:
    """Generate a numbered incremental update package in updates/packages/."""
    for d in [BASELINES_DIR, PACKAGES_DIR, LATEST_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.exists() else {
        "local_scan_baseline": None,
        "exported_update": None,
        "reviewer_acknowledged_baseline": None,
        "history": [],
    }
    next_num = len(state.get("history", [])) + 1
    update_id = f"UPDATE-{next_num:04d}"
    pkg_dir = PACKAGES_DIR / update_id
    pkg_files_dir = pkg_dir / "files"
    pkg_files_dir.mkdir(parents=True, exist_ok=True)

    current_scan = scan_workspace_files()
    for rel in current_scan:
        src = ROOT / rel
        dst = pkg_files_dir / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

    manifest = {
        "update_id": update_id,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "base_acknowledged": state.get("reviewer_acknowledged_baseline"),
        "file_count": len(current_scan),
        "files": current_scan,
    }
    (pkg_dir / "UPDATE_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    zip_path = PACKAGES_DIR / f"{update_id}.zip"
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as zf:
        for f in sorted(pkg_dir.rglob("*")):
            if f.is_file():
                zf.write(f, f.relative_to(pkg_dir))

    latest_zip = LATEST_DIR / "AI_DESIGNER_LATEST.zip"
    shutil.copy2(zip_path, latest_zip)

    state["local_scan_baseline"] = update_id
    state["exported_update"] = update_id
    state.setdefault("history", []).append({
        "update_id": update_id,
        "generated_at": manifest["generated_at"],
        "file_count": len(current_scan),
    })
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "EXPORTED", "update_id": update_id, "zip_path": str(zip_path.relative_to(ROOT))}
```

### `validate_package` — `Lines 101–113`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `101` إلى السطر `113` (`Lines 101–113`)
- **الوظيفة:** تتحقق من سلامة ملف الـ ZIP والمانيفست وتطابق بصمات SHA-256 لجميع الملفات المضمنة.
- **الكود الفعلي (`Lines 101–113`):**
```python
def validate_package(update_id: str) -> dict:
    """Validate that all files in the numbered package match their manifest SHA-256 hashes."""
    pkg_dir = PACKAGES_DIR / update_id
    manifest_path = pkg_dir / "UPDATE_MANIFEST.json"
    if not manifest_path.exists():
        raise SystemExit(f"Missing manifest for {update_id}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    mismatches: list[str] = []
    for rel, info in manifest.get("files", {}).items():
        copied = pkg_dir / "files" / rel
        if not copied.exists() or compute_sha256(copied) != info["sha256"]:
            mismatches.append(rel)
    return {"status": "VALID" if not mismatches else "INVALID", "update_id": update_id, "mismatches": mismatches}
```

### `acknowledge_package` — `Lines 116–126`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `116` إلى السطر `126` (`Lines 116–126`)
- **الوظيفة:** تسجل تأكيد استلام ومراجعة الحزمة من قِبل المستخدم عند تمرير --confirm-reviewed صراحةً.
- **الكود الفعلي (`Lines 116–126`):**
```python
def acknowledge_package(update_id: str, reviewer: str, note: str) -> dict:
    """Record explicit user-confirmed reviewer acknowledgment."""
    state = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    state["reviewer_acknowledged_baseline"] = {
        "update_id": update_id,
        "acknowledged_by": reviewer,
        "note": note,
        "acknowledged_at": datetime.now(timezone.utc).isoformat(),
    }
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {"status": "ACKNOWLEDGED", "update_id": update_id, "by": reviewer}
```

### `main` — `Lines 129–149`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `129` إلى السطر `149` (`Lines 129–149`)
- **الوظيفة:** تعالج أوامر سطر الأوامر (export, validate, status, acknowledge).
- **الكود الفعلي (`Lines 129–149`):**
```python
def main() -> None:
    """CLI entrypoint for export_updates.py."""
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "export":
        print(json.dumps(export_package(), ensure_ascii=False))
    elif cmd == "validate":
        uid = sys.argv[sys.argv.index("--update") + 1] if "--update" in sys.argv else "UPDATE-0001"
        res = validate_package(uid)
        print(json.dumps(res, ensure_ascii=False))
        if res["status"] != "VALID":
            raise SystemExit(1)
    elif cmd == "acknowledge":
        if "--confirm-reviewed" not in sys.argv:
            raise SystemExit("Refusing automatic acknowledgment without --confirm-reviewed")
        uid = sys.argv[sys.argv.index("--update") + 1]
        by = sys.argv[sys.argv.index("--by") + 1] if "--by" in sys.argv else "Owner"
        note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else "Reviewed"
        print(json.dumps(acknowledge_package(uid, by, note), ensure_ascii=False))
    else:
        state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.exists() else {"status": "UNINITIALIZED"}
        print(json.dumps(state, ensure_ascii=False))
```
