# مرآة الكود التفصيلية: `tools/update_packages/cli.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/cli.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/cli.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `295` (`Lines 1–295`)
- **بصمة الملف (`SHA-256`):** `de3173e813235259fe127988c2ffbcae9b6a331be6f09fba18aa60add5f4a953`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `cmd_init_baseline` | `function` | `Lines 27–41` | `def cmd_init_baseline(args: argparse.Namespace) -> int:` | Initialize a verified repository baseline snapshot. |
| `cmd_status` | `function` | `Lines 44–90` | `def cmd_status(args: argparse.Namespace) -> int:` | Show pending workspace file modifications against the active baseline. |
| `cmd_export` | `function` | `Lines 93–165` | `def cmd_export(args: argparse.Namespace) -> int:` | Export an incremental review or complete update package. |
| `cmd_verify` | `function` | `Lines 168–176` | `def cmd_verify(args: argparse.Namespace) -> int:` | Verify package structure, path safety, and hash integrity. |
| `cmd_apply` | `function` | `Lines 179–196` | `def cmd_apply(args: argparse.Namespace) -> int:` | Apply an update package safely to a target workspace. |
| `cmd_acknowledge` | `function` | `Lines 199–209` | `def cmd_acknowledge(args: argparse.Namespace) -> int:` | Acknowledge a baseline as accepted by the owner/reviewer. |
| `cmd_history` | `function` | `Lines 212–217` | `def cmd_history(args: argparse.Namespace) -> int:` | Print package export and baseline acknowledgment history. |
| `build_parser` | `function` | `Lines 220–283` | `def build_parser() -> argparse.ArgumentParser:` | رمز برمجي موثق. |
| `main` | `function` | `Lines 286–290` | `def main() -> None:` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `cmd_init_baseline` — `Lines 27–41`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `41` (`Lines 27–41`)
- **الوظيفة:** Initialize a verified repository baseline snapshot.
- **الكود الفعلي (`Lines 27–41`):**
```python
def cmd_init_baseline(args: argparse.Namespace) -> int:
    """Initialize a verified repository baseline snapshot."""
    root = Path(args.root).resolve() if args.root else REPO_ROOT
    state_mgr = UpdateStateManager(root)
    inventory = state_mgr.initialize_baseline(args.baseline_id)
    output = {
        "status": "INITIALIZED",
        "baseline_id": inventory.baseline_id,
        "files_count": len(inventory.files),
        "created_at_utc": inventory.created_at_utc,
        "git_commit": inventory.git_commit,
        "registry_file": str(state_mgr.baselines_dir / f"{inventory.baseline_id}.json")
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0
```

### `cmd_status` — `Lines 44–90`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `90` (`Lines 44–90`)
- **الوظيفة:** Show pending workspace file modifications against the active baseline.
- **الكود الفعلي (`Lines 44–90`):**
```python
def cmd_status(args: argparse.Namespace) -> int:
    """Show pending workspace file modifications against the active baseline."""
    root = Path(args.root).resolve() if args.root else REPO_ROOT
    state_mgr = UpdateStateManager(root)
    base_inv = state_mgr.get_active_baseline()
    if not base_inv:
        print(json.dumps({
            "status": "UNINITIALIZED",
            "message": "No active baseline found. Run 'init-baseline' first."
        }, ensure_ascii=False, indent=2))
        return 1

    scanner = WorkspaceScanner(root)
    current_files = scanner.scan()

    entries, summary = InventoryDiffer.compute_diff(base_inv.files, current_files)
    total_mutations = summary["added"] + summary["modified"] + summary["deleted"] + summary["renamed"]

    changes_list = []
    for e in entries:
        local_p = str(root / e.path)
        payload_p = f"payload/{e.path}" if e.operation != "DELETE" else None
        item: Dict[str, Any] = {
            "operation": e.operation,
            "repository_path": e.path,
            "payload_path": payload_p,
            "size_bytes": e.size_bytes,
            "previous_sha256": e.previous_sha256,
            "current_sha256": e.new_sha256,
            "is_binary": e.is_binary,
            "renamed_from": e.renamed_from,
        }
        if getattr(args, "show_absolute_paths", False):
            item["local_windows_path"] = local_p
        changes_list.append(item)

    output = {
        "status": "PENDING_CHANGES" if total_mutations > 0 else "CLEAN_SYNC",
        "active_baseline_id": base_inv.baseline_id,
        "baseline_trust_status": getattr(base_inv, "trust_status", "VALID"),
        "baseline_files_count": len(base_inv.files),
        "current_files_count": len(current_files),
        "summary": summary,
        "changes": changes_list
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0
```

### `cmd_export` — `Lines 93–165`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `165` (`Lines 93–165`)
- **الوظيفة:** Export an incremental review or complete update package.
- **الكود الفعلي (`Lines 93–165`):**
```python
def cmd_export(args: argparse.Namespace) -> int:
    """Export an incremental review or complete update package."""
    root = Path(args.root).resolve() if args.root else REPO_ROOT
    exports_dir = Path(args.output_dir).resolve() if args.output_dir else DEFAULT_EXPORTS_DIR
    mode = PackageMode.COMPLETE if args.mode.lower() == "complete" else PackageMode.REVIEW

    state_mgr = UpdateStateManager(root)
    base_inv = state_mgr.get_baseline(args.base_id) if args.base_id else state_mgr.get_active_baseline()
    if not base_inv:
        print(json.dumps({
            "status": "ERROR",
            "message": "No valid base snapshot found. Run 'init-baseline' before exporting."
        }, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    # Audit baseline trust status
    if getattr(base_inv, "trust_status", "VALID") != "VALID" and not getattr(args, "allow_untrusted_base", False):
        print(json.dumps({
            "status": "ERROR",
            "message": f"Baseline {base_inv.baseline_id} is marked as {base_inv.trust_status}: {getattr(base_inv, 'invalidation_reason', '')}. Exports against invalid baselines are prohibited."
        }, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    # Scan current target state
    scanner = WorkspaceScanner(root)
    current_files = scanner.scan()
    now_utc = datetime.now(timezone.utc)
    target_inv = BaselineInventory(
        baseline_id=f"SNAP_{now_utc.strftime('%Y%m%dT%H%M%SZ')}",
        repo_identity="AI Graphic Designer",
        created_at_utc=now_utc.isoformat(),
        tool_version="1.0.0",
        schema_version="1.0.0",
        git_commit=state_mgr.get_git_commit(),
        inclusion_policy="tracked_first_party",
        exclusion_policy="standard_anti_leak",
        files=current_files
    )

    seq_num = state_mgr.get_next_sequence_number()
    update_id = args.update_id or f"UPDATE_{seq_num:04d}"

    packager = UpdatePackager(root)
    result = packager.build_package(
        base_inventory=base_inv,
        target_inventory=target_inv,
        mode=mode,
        update_id=update_id,
        output_dir=exports_dir,
        sequence_num=seq_num,
        task_ids=[args.task_id] if args.task_id else ["TASK-COLLAB-ENG-01"]
    )

    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
    # Record export in state history with verified archive sha256
    state_mgr.record_export({
        "update_id": update_id,
        "archive_name": result["archive_name"],
        "archive_path": result["archive_path"],
        "archive_sha256": result.get("archive_sha256"),
        "mode": result["mode"],
        "base_snapshot_id": result["base_snapshot_id"],
        "target_snapshot_id": result["target_snapshot_id"],
        "exported_at_utc": now_utc.isoformat(),
        "summary": result["summary"]
    })
    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

    if getattr(args, "show_absolute_paths", False):
        result["local_windows_archive_path"] = str(Path(result["archive_path"]).resolve())

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0
```

### `cmd_verify` — `Lines 168–176`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `168` إلى السطر `176` (`Lines 168–176`)
- **الوظيفة:** Verify package structure, path safety, and hash integrity.
- **الكود الفعلي (`Lines 168–176`):**
```python
def cmd_verify(args: argparse.Namespace) -> int:
    """Verify package structure, path safety, and hash integrity."""
    pkg_path = Path(args.package).resolve()
    # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
    root = Path(args.root).resolve() if getattr(args, "root", None) else REPO_ROOT
    res = PackageVerifier.verify_package(pkg_path, workspace_root=root)
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res["status"] == "VALID" else 1
```

### `cmd_apply` — `Lines 179–196`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `179` إلى السطر `196` (`Lines 179–196`)
- **الوظيفة:** Apply an update package safely to a target workspace.
- **الكود الفعلي (`Lines 179–196`):**
```python
def cmd_apply(args: argparse.Namespace) -> int:
    """Apply an update package safely to a target workspace."""
    pkg_path = Path(args.package).resolve()
    target_dir = Path(args.target).resolve() if args.target else REPO_ROOT

    force_unsafe = getattr(args, "force_unsafe_unverified_base", False)
    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
    allow_review = getattr(args, "allow_review_mode", False)
    applier = PackageApplier(
        target_dir=target_dir,
        enforce_base_match=not force_unsafe,
        force_unsafe_unverified_base=force_unsafe,
        allow_review_mode=allow_review
    )
    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED
    res = applier.apply(pkg_path, dry_run=args.dry_run)
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0 if res["status"] in ("APPLIED", "DRY_RUN_PASSED") else 1
```

### `cmd_acknowledge` — `Lines 199–209`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `199` إلى السطر `209` (`Lines 199–209`)
- **الوظيفة:** Acknowledge a baseline as accepted by the owner/reviewer.
- **الكود الفعلي (`Lines 199–209`):**
```python
def cmd_acknowledge(args: argparse.Namespace) -> int:
    """Acknowledge a baseline as accepted by the owner/reviewer."""
    root = Path(args.root).resolve() if args.root else REPO_ROOT
    state_mgr = UpdateStateManager(root)
    res = state_mgr.acknowledge_baseline(
        baseline_id=args.baseline_id,
        acknowledged_by=args.by or "Owner",
        note=args.note or "Confirmed"
    )
    print(json.dumps(res, ensure_ascii=False, indent=2))
    return 0
```

### `cmd_history` — `Lines 212–217`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `212` إلى السطر `217` (`Lines 212–217`)
- **الوظيفة:** Print package export and baseline acknowledgment history.
- **الكود الفعلي (`Lines 212–217`):**
```python
def cmd_history(args: argparse.Namespace) -> int:
    """Print package export and baseline acknowledgment history."""
    root = Path(args.root).resolve() if args.root else REPO_ROOT
    state_mgr = UpdateStateManager(root)
    print(json.dumps(state_mgr.list_history(), ensure_ascii=False, indent=2))
    return 0
```

### `build_parser` — `Lines 220–283`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `220` إلى السطر `283` (`Lines 220–283`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 220–283`):**
```python
def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Incremental Update Packaging Tool for AI Graphic Designer",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init-baseline
    p_init = subparsers.add_parser("init-baseline", help="Initialize workspace baseline inventory")
    p_init.add_argument("--root", type=str, default=None, help="Repository root path")
    p_init.add_argument("--baseline-id", type=str, default=None, help="Explicit baseline ID")
    p_init.set_defaults(func=cmd_init_baseline)

    # status
    p_status = subparsers.add_parser("status", help="Show pending changes against active baseline")
    p_status.add_argument("--root", type=str, default=None, help="Repository root path")
    p_status.add_argument("--show-absolute-paths", action="store_true", help="Display full absolute local Windows filesystem paths")
    p_status.set_defaults(func=cmd_status)

    # export
    p_export = subparsers.add_parser("export", help="Export incremental update package")
    p_export.add_argument("--root", type=str, default=None, help="Repository root path")
    p_export.add_argument("--mode", type=str, default="review", choices=["review", "complete"], help="Package mode")
    p_export.add_argument("--base-id", type=str, default=None, help="Specific base snapshot ID")
    p_export.add_argument("--output-dir", type=str, default=None, help="Custom export output directory")
    p_export.add_argument("--update-id", type=str, default=None, help="Explicit update ID")
    p_export.add_argument("--task-id", type=str, default=None, help="Associated research/governance task ID")
    p_export.add_argument("--show-absolute-paths", action="store_true", help="Display full absolute local Windows filesystem paths in summary")
    p_export.add_argument("--allow-untrusted-base", action="store_true", help="Allow exporting against an unverified/untrusted baseline")
    p_export.set_defaults(func=cmd_export)

    # verify
    p_verify = subparsers.add_parser("verify", help="Verify package archive integrity and hashes")
    p_verify.add_argument("--package", type=str, required=True, help="Path to ZIP archive")
    # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
    p_verify.add_argument("--root", type=str, default=None, help="Repository root path for registry resolution")
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED
    p_verify.set_defaults(func=cmd_verify)

    # apply
    p_apply = subparsers.add_parser("apply", help="Apply package safely to target workspace")
    p_apply.add_argument("--package", type=str, required=True, help="Path to ZIP archive")
    p_apply.add_argument("--target", type=str, default=None, help="Target workspace path")
    p_apply.add_argument("--dry-run", action="store_true", help="Perform prerequisite checks without writing")
    p_apply.add_argument("--force-unsafe-unverified-base", action="store_true", help="Unsafely bypass strict base hash enforcement")
    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
    p_apply.add_argument("--allow-review-mode", action="store_true", help="Allow applying a REVIEW mode package for review extraction only (NOT complete reconstruction)")
    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED
    p_apply.set_defaults(func=cmd_apply)

    # acknowledge
    p_ack = subparsers.add_parser("acknowledge", help="Acknowledge accepted baseline")
    p_ack.add_argument("--root", type=str, default=None, help="Repository root path")
    p_ack.add_argument("--baseline-id", type=str, required=True, help="Baseline ID to acknowledge")
    p_ack.add_argument("--by", type=str, default="Owner", help="Reviewer identity")
    p_ack.add_argument("--note", type=str, default="Confirmed", help="Acknowledgment note")
    p_ack.set_defaults(func=cmd_acknowledge)

    # history
    p_hist = subparsers.add_parser("history", help="Show export and baseline history")
    p_hist.add_argument("--root", type=str, default=None, help="Repository root path")
    p_hist.set_defaults(func=cmd_history)

    return parser
```

### `main` — `Lines 286–290`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `286` إلى السطر `290` (`Lines 286–290`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 286–290`):**
```python
def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    exit_code = args.func(args)
    sys.exit(exit_code)
```
