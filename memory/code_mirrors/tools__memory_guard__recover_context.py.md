# مرآة الكود التفصيلية: `tools/memory_guard/recover_context.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/recover_context.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/recover_context.py`
- **الدور المعماري (`Architectural Role`):** Memory Guard — Deterministic Context Recovery Engine
- **إجمالي عدد الأسطر (`Total Lines`):** `83` (`Lines 1–83`)
- **بصمة الملف (`SHA-256`):** `e0a9e985eb966d162631ea40320d9c4ddede22667d911da998461ebc986bce3e`
- **الوصف التفصيلي:** يسترجع حالة السياق الكاملة بعد أي انقطاع أو Context Compaction عبر قراءة نقطة التوقف وسجل الـ WAL الرئيسي وسجلات الـ WAL المعزولة للـ Subagents والمكتشفات وأقفال الملكية.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `memory/session/CURRENT_TASK_CHECKPOINT.md, ACTIVE_SESSION_WAL.md, subagent_wals/*.wal.md, memory/findings/` | كافة سجلات الجلسة والمكتشفات المعزولة | يبني حزمة استرجاع حتمية بدون الاعتماد على ذاكرة الشات. |
| **يرمي إلى (`Throws To`)** | `memory/session/RECOVERY_PACKET.json` | ملف JSON مهيكل بحالة الجلسة المسترجعة | يمكّن أي Agent جديد من الاستئناف الفوري بعد الانقطاع. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `build_recovery_packet` | `function` | `Lines 21–71` | `def build_recovery_packet() -> dict:` | تجمع حالة الجلسة وسجلات الـ WAL والمكتشفات وتتحقق من حالة عدم اعتماد المعمارية وتكتب RECOVERY_PACKET.json. |
| `main` | `function` | `Lines 74–79` | `def main() -> None:` | تشغل عملية استرجاع السياق وتتحقق من اكتمال ملفات الجلسة. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `build_recovery_packet` — `Lines 21–71`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `71` (`Lines 21–71`)
- **الوظيفة:** تجمع حالة الجلسة وسجلات الـ WAL والمكتشفات وتتحقق من حالة عدم اعتماد المعمارية وتكتب RECOVERY_PACKET.json.
- **الكود الفعلي (`Lines 21–71`):**
```python
def build_recovery_packet() -> dict:
    """Reconstruct complete session and subagent state after interruption or compaction."""
    checkpoint_path = SESSION_DIR / "CURRENT_TASK_CHECKPOINT.md"
    wal_path = SESSION_DIR / "ACTIVE_SESSION_WAL.md"
    decisions_path = ROOT / "memory" / "decisions" / "DECISION_LOG.md"

    checkpoint_text = checkpoint_path.read_text(encoding="utf-8") if checkpoint_path.exists() else ""
    wal_text = wal_path.read_text(encoding="utf-8") if wal_path.exists() else ""
    decisions_text = decisions_path.read_text(encoding="utf-8") if decisions_path.exists() else ""

    wal_entries = re.findall(r"^### `\[(WAL-[0-9]+)\]\s*—\s*([^`]+)`", wal_text, re.M)
    subagent_wals: list[dict] = []
    if SUBAGENT_WALS_DIR.exists():
        for p in sorted(SUBAGENT_WALS_DIR.glob("*.wal.md")):
            txt = p.read_text(encoding="utf-8")
            steps = re.findall(r"`\[(STEP-[0-9]+)\]`", txt)
            subagent_wals.append({
                "file": p.relative_to(ROOT).as_posix(),
                "step_count": len(steps),
                "last_step": steps[-1] if steps else None,
            })

    findings_summary: list[dict] = []
    if FINDINGS_ENTRIES_DIR.exists():
        for p in sorted(FINDINGS_ENTRIES_DIR.glob("*.json")):
            data = json.loads(p.read_text(encoding="utf-8"))
            findings_summary.append({
                "finding_id": data.get("finding_id"),
                "subagent_id": data.get("subagent_id"),
                "state": data.get("current_approval_state"),
            })

    active_locks: list[dict] = []
    if LOCKS_PATH.exists():
        ldata = json.loads(LOCKS_PATH.read_text(encoding="utf-8"))
        active_locks = [lk for lk in ldata.get("locks", []) if lk.get("status") == "ACTIVE"]

    arch_not_approved = "ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED`" in decisions_text
    packet = {
        "recovered_at": datetime.now(timezone.utc).isoformat(),
        "status": "RECOVERED_CLEAN" if (checkpoint_text and wal_text) else "INCOMPLETE_SESSION_FILES",
        "architecture_approval_status": "NOT_APPROVED" if arch_not_approved else "UNKNOWN",
        "main_wal_entry_count": len(wal_entries),
        "latest_main_wal_id": wal_entries[-1][0] if wal_entries else None,
        "isolated_subagent_wals": subagent_wals,
        "active_subagent_locks": active_locks,
        "findings": findings_summary,
    }
    if "--write" in sys.argv:
        RECOVERY_OUT.write_text(json.dumps(packet, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return packet
```

### `main` — `Lines 74–79`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `74` إلى السطر `79` (`Lines 74–79`)
- **الوظيفة:** تشغل عملية استرجاع السياق وتتحقق من اكتمال ملفات الجلسة.
- **الكود الفعلي (`Lines 74–79`):**
```python
def main() -> None:
    """CLI entrypoint for context recovery."""
    packet = build_recovery_packet()
    print(json.dumps(packet, ensure_ascii=False))
    if packet["status"] != "RECOVERED_CLEAN":
        raise SystemExit(1)
```
