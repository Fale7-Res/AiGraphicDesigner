# مرآة الكود التفصيلية: `tools/memory_guard/sync_rules.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/sync_rules.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/sync_rules.py`
- **الدور المعماري (`Architectural Role`):** Memory Guard — Automated Rule Synchronizer (.agent_rules/ -> .agents/rules/)
- **إجمالي عدد الأسطر (`Total Lines`):** `75` (`Lines 1–75`)
- **بصمة الملف (`SHA-256`):** `717f6cc867b760f8122143866b18473519cb6d967c1084af2e2095585aad346a`
- **الوصف التفصيلي:** يمنع التكرار اليدوي لملفات القواعد باعتبار .agent_rules/ المصدر الوحيد للتأليف ومزامنته آلياً مع .agents/rules/ والتحقق من تطابق البايتات.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `.agent_rules/*.md` | ملفات القواعد الأصلية المعتمدة | أي تعديل في .agent_rules/ يُنسخ آلياً إلى .agents/rules/. |
| **يرمي إلى (`Throws To`)** | `.agents/rules/*.md & tools/memory_guard/verify_brain_sync.py` | ملفات القواعد المتوافقة مع Antigravity وحالة التزامن | يضمن عدم انحراف القواعد بين المسارين. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `sha256_bytes` | `function` | `Lines 18–20` | `def sha256_bytes(data: bytes) -> str:` | تحسب بصمة SHA-256 لمحتوى ملف القاعدة. |
| `sync_or_check` | `function` | `Lines 23–62` | `def sync_or_check(write_mode: bool) -> dict:` | تطابق أو تنسخ ملفات القواعد من .agent_rules/ إلى .agents/rules/ وتكشف أي اختلاف أو ملف يتيم. |
| `main` | `function` | `Lines 65–71` | `def main() -> None:` | نقطة الدخول لتشغيل المزامنة (--write) أو فحص التطابق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `sha256_bytes` — `Lines 18–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `20` (`Lines 18–20`)
- **الوظيفة:** تحسب بصمة SHA-256 لمحتوى ملف القاعدة.
- **الكود الفعلي (`Lines 18–20`):**
```python
def sha256_bytes(data: bytes) -> str:
    """Return hex SHA-256 of raw bytes."""
    return hashlib.sha256(data).hexdigest()
```

### `sync_or_check` — `Lines 23–62`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `62` (`Lines 23–62`)
- **الوظيفة:** تطابق أو تنسخ ملفات القواعد من .agent_rules/ إلى .agents/rules/ وتكشف أي اختلاف أو ملف يتيم.
- **الكود الفعلي (`Lines 23–62`):**
```python
def sync_or_check(write_mode: bool) -> dict:
    """Synchronize or verify parity between .agent_rules/ and .agents/rules/."""
    ANTIGRAVITY_DIR.mkdir(parents=True, exist_ok=True)
    canonical_files = {p.name: p for p in sorted(CANONICAL_DIR.glob("*.md"))}
    target_files = {p.name: p for p in sorted(ANTIGRAVITY_DIR.glob("*.md"))}

    drifted: list[str] = []
    missing_in_target: list[str] = []
    orphan_in_target: list[str] = []

    for name, src_path in canonical_files.items():
        dst_path = ANTIGRAVITY_DIR / name
        if not dst_path.exists():
            if write_mode:
                shutil.copy2(src_path, dst_path)
            else:
                missing_in_target.append(name)
        else:
            if sha256_bytes(src_path.read_bytes()) != sha256_bytes(dst_path.read_bytes()):
                if write_mode:
                    shutil.copy2(src_path, dst_path)
                else:
                    drifted.append(name)

    for name, dst_path in target_files.items():
        if name not in canonical_files:
            if write_mode:
                dst_path.unlink()
            else:
                orphan_in_target.append(name)

    ok = not (drifted or missing_in_target or orphan_in_target)
    return {
        "status": "SYNCHRONIZED" if ok else "OUT_OF_SYNC",
        "canonical_count": len(canonical_files),
        "drifted": drifted,
        "missing_in_target": missing_in_target,
        "orphan_in_target": orphan_in_target,
        "write_mode": write_mode,
    }
```

### `main` — `Lines 65–71`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `71` (`Lines 65–71`)
- **الوظيفة:** نقطة الدخول لتشغيل المزامنة (--write) أو فحص التطابق.
- **الكود الفعلي (`Lines 65–71`):**
```python
def main() -> None:
    """CLI entrypoint for sync_rules.py."""
    write_mode = "--write" in sys.argv
    res = sync_or_check(write_mode=write_mode)
    print(json.dumps(res, ensure_ascii=False))
    if res["status"] != "SYNCHRONIZED":
        raise SystemExit(1)
```
