# مرآة الكود التفصيلية: `tools/update_packages/applier.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/applier.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/applier.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `515` (`Lines 1–515`)
- **بصمة الملف (`SHA-256`):** `d1b6ac32511fd5f5761134f74d9aaca50e05c250d34604fb507e5edf1805210e`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PackageApplier` | `class` | `Lines 23–513` | `class PackageApplier:` | Applies verified update packages safely and transactionally to a target workspace with 100% rollback. |
| `PackageApplier.__init__` | `method` | `Lines 26–38` | `def __init__(` | رمز برمجي موثق. |
| `PackageApplier.apply` | `method` | `Lines 40–513` | `def apply(self, zip_path: Path, dry_run: bool = False) -> Dict[str, Any]:` | Apply an update ZIP package transactionally to the target directory. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PackageApplier` — `Lines 23–513`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `23` إلى السطر `513` (`Lines 23–513`)
- **الوظيفة:** Applies verified update packages safely and transactionally to a target workspace with 100% rollback.
- **الكود الفعلي (`Lines 23–513`):**
```python
class PackageApplier:
    """Applies verified update packages safely and transactionally to a target workspace with 100% rollback."""

    def __init__(
        self,
        target_dir: Path,
        enforce_base_match: bool = True,
        expected_base_inventory: Optional[BaselineInventory] = None,
        force_unsafe_unverified_base: bool = False,
        allow_review_mode: bool = False
    ):
        self.target_dir = target_dir.resolve()
        self.enforce_base_match = enforce_base_match and not force_unsafe_unverified_base
        self.expected_base_inventory = expected_base_inventory
        self.force_unsafe_unverified_base = force_unsafe_unverified_base
        self.allow_review_mode = allow_review_mode

    def apply(self, zip_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """Apply an update ZIP package transactionally to the target directory."""
        # 1. Verify archive format, safety, and hashes
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
        verification = PackageVerifier.verify_package(zip_path)
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED
        if verification["status"] != "VALID":
            return {
                "status": "FAILED",
                "stage": "VERIFICATION",
                "errors": verification["errors"]
            }

        manifest = UpdateManifest.from_dict(verification["manifest"])

        # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
        # 1.1 Package Mode Audit: REVIEW mode cannot be applied as complete repository reconstruction
        if getattr(manifest, "package_mode", "").upper() == "REVIEW" and not self.allow_review_mode:
            return {
                "status": "FAILED",
                "stage": "PACKAGE_MODE_AUDIT",
                "errors": [
                    f"Package '{manifest.update_id}' is in REVIEW mode (declared exclusions: {manifest.exclusions_count}). "
                    "REVIEW packages contain partial audit payloads and cannot be applied as complete repository reconstruction. "
                    "Applying a REVIEW package as a repository reconstruction is blocked. "
                    "Use a COMPLETE package, or explicitly pass allow_review_mode=True (CLI: --allow-review-mode) for review extraction only."
                ]
            }

        # 2. Audit all manifest entry paths and destination ancestry at point of application
        path_errors: List[str] = []
        for entry in manifest.entries:
            safe, reason = audit_path_ancestry_safety(self.target_dir, entry.path)
            if not safe:
                path_errors.append(f"Unsafe target path or escaping ancestry: {entry.path} ({reason})")
            if entry.payload_path:
                safe_pay, pay_reason = is_safe_relative_path(entry.payload_path)
                if not safe_pay:
                    path_errors.append(f"Unsafe payload path at application time: {entry.payload_path} ({pay_reason})")
            if entry.renamed_from:
                safe_ren, ren_reason = audit_path_ancestry_safety(self.target_dir, entry.renamed_from)
                if not safe_ren:
                    path_errors.append(f"Unsafe rename source or escaping ancestry: {entry.renamed_from} ({ren_reason})")

        if path_errors:
            return {
                "status": "FAILED",
                "stage": "PATH_SECURITY_AUDIT",
                "errors": path_errors
            }
        # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

        # 3. Scan current target workspace and verify prerequisites
        scanner = WorkspaceScanner(self.target_dir)
        current_target_files = scanner.scan()

        prereq_errors: List[str] = []

        # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
        # Check base snapshot trust status
        manifest_base_trust = getattr(manifest, "base_snapshot_trust_status", "VALID")
        if manifest_base_trust != "VALID" or (manifest.status and manifest.status.startswith("UNTRUSTED")):
            if not self.force_unsafe_unverified_base:
                prereq_errors.append(
                    f"Package was built from an untrusted/invalid baseline ({manifest_base_trust}: {getattr(manifest, 'base_snapshot_invalidation_reason', '')}). "
                    "Applying updates generated from untrusted baselines is strictly blocked. Use force_unsafe_unverified_base=True to override at your own risk."
                )
        # END CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED

        # Resolve base inventory if provided or discoverable
        base_inv: Optional[BaselineInventory] = self.expected_base_inventory
        if not base_inv and (self.target_dir / "tools" / "update_packages" / "registry").exists():
            try:
                state_mgr = UpdateStateManager(self.target_dir)
                base_inv = state_mgr.get_baseline(manifest.base_snapshot_id)
            except Exception:
                base_inv = None

        # Enforce complete base inventory match if in COMPLETE mode or if base inventory is known
        if self.enforce_base_match:
            # Check for empty directory when a non-empty base is declared
            is_empty_workspace = len(current_target_files) == 0
            if is_empty_workspace and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                prereq_errors.append(
                    f"Target workspace is empty, but package declares required base snapshot: {manifest.base_snapshot_id}"
                )

            # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
            # Defect 1 Fix: In verified mode, an unresolvable or missing required base inventory MUST fail closed immediately
            if not base_inv and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                prereq_errors.append(
                    f"Required base snapshot '{manifest.base_snapshot_id}' cannot be resolved or loaded in target workspace or baseline registry. "
                    "In verified mode, applying updates against an unverified/nonexistent base baseline is strictly rejected."
                )

            if base_inv:
                # Complete inventory match check
                for b_path, b_rec in base_inv.files.items():
                    curr_rec = current_target_files.get(b_path)
                    if not curr_rec:
                        prereq_errors.append(f"Required base file missing from target workspace: {b_path}")
                    elif curr_rec.sha256 != b_rec.sha256:
                        prereq_errors.append(
                            f"Base file content mismatch for {b_path}: expected {b_rec.sha256[:12]}..., got {curr_rec.sha256[:12]}..."
                        )

                # Check for unexpected extra files in strict base mode
                extra_files = set(current_target_files.keys()) - set(base_inv.files.keys())
                if extra_files:
                    prereq_errors.append(
                        f"Target workspace contains {len(extra_files)} unexpected extra files not present in baseline {base_inv.baseline_id}: {sorted(extra_files)[:5]}"
                    )

                # Defect 2 Fix: Base snapshot hash validation against trusted baseline
                expected_base_hash = compute_bytes_sha256(base_inv.to_json().encode("utf-8"))
                if manifest.base_snapshot_hash and manifest.base_snapshot_hash.lower() != expected_base_hash.lower():
                    prereq_errors.append(
                        f"Base snapshot hash tampering detected: manifest declares base_snapshot_hash '{manifest.base_snapshot_hash}', "
                        f"but trusted baseline '{base_inv.baseline_id}' serialization hash is '{expected_base_hash}'."
                    )
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

        # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
        # Defect A & B: Target snapshot and TARGET_INVENTORY.json consistency validation
        is_complete_mode = getattr(manifest, "package_mode", "").upper() == "COMPLETE"
        target_inv: Optional[BaselineInventory] = None
        try:
            with ZipFile(zip_path, "r") as zf:
                names = zf.namelist()
                if is_complete_mode and "TARGET_INVENTORY.json" not in names:
                    prereq_errors.append("COMPLETE mode package requires TARGET_INVENTORY.json, but it is missing from archive root")
                elif "TARGET_INVENTORY.json" in names:
                    decl_target_bytes = zf.read("TARGET_INVENTORY.json")
                    decl_target_hash = compute_bytes_sha256(decl_target_bytes)
                    if manifest.target_snapshot_hash and manifest.target_snapshot_hash.lower() != decl_target_hash.lower():
                        prereq_errors.append(
                            f"Target snapshot hash tampering detected: manifest declares target_snapshot_hash '{manifest.target_snapshot_hash}', "
                            f"but package TARGET_INVENTORY.json has hash '{decl_target_hash}'."
                        )
                    else:
                        try:
                            decl_target_data = json.loads(decl_target_bytes.decode("utf-8"))
                            target_inv = BaselineInventory.from_dict(decl_target_data)
                            canonical_target_bytes = target_inv.to_json().encode("utf-8")
                            canonical_target_hash = compute_bytes_sha256(canonical_target_bytes)
                            if canonical_target_hash.lower() != decl_target_hash.lower():
                                prereq_errors.append(
                                    f"TARGET_INVENTORY.json is not in canonical serialization format: "
                                    f"declared hash '{decl_target_hash}', canonical serialization hash '{canonical_target_hash}'."
                                )

                            # If base_inv is loaded, derive expected target inventory and compare 1:1
                            if base_inv:
                                derived_files: Dict[str, Tuple[str, int]] = {
                                    p: (rec.sha256, rec.size_bytes)
                                    for p, rec in base_inv.files.items()
                                }
                                for entry in manifest.entries:
                                    if entry.operation in (FileOperation.ADD.value, FileOperation.MODIFY.value):
                                        derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes)
                                    elif entry.operation == FileOperation.DELETE.value:
                                        derived_files.pop(entry.path, None)
                                    elif entry.operation == FileOperation.RENAME.value:
                                        if entry.renamed_from:
                                            derived_files.pop(entry.renamed_from, None)
                                        derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes)

                                # Check for missing files in TARGET_INVENTORY.json
                                missing_in_target = set(derived_files.keys()) - set(target_inv.files.keys())
                                if missing_in_target:
                                    prereq_errors.append(
                                        f"TARGET_INVENTORY.json is missing {len(missing_in_target)} files derived from baseline and manifest: {sorted(missing_in_target)[:5]}"
                                    )

                                # Check for unexpected extra files in TARGET_INVENTORY.json
                                extra_in_target = set(target_inv.files.keys()) - set(derived_files.keys())
                                if extra_in_target:
                                    prereq_errors.append(
                                        f"TARGET_INVENTORY.json contains {len(extra_in_target)} unexpected extra files: {sorted(extra_in_target)[:5]}"
                                    )

                                # Check hash and size for every derived file (including unchanged files)
                                for p, (exp_sha, exp_size) in derived_files.items():
                                    t_rec = target_inv.files.get(p)
                                    if t_rec:
                                        if t_rec.sha256.lower() != exp_sha.lower():
                                            prereq_errors.append(
                                                f"TARGET_INVENTORY.json entry for '{p}' contradicts derived target state: "
                                                f"expected sha256 '{exp_sha}', declared '{t_rec.sha256}'."
                                            )
                                        if t_rec.size_bytes != exp_size:
                                            prereq_errors.append(
                                                f"TARGET_INVENTORY.json entry for '{p}' size mismatch: "
                                                f"expected {exp_size} bytes, declared {t_rec.size_bytes} bytes."
                                            )
                        except Exception as parse_ex:
                            prereq_errors.append(f"TARGET_INVENTORY.json schema/parsing error: {parse_ex}")
        except Exception as e:
            prereq_errors.append(f"Cannot inspect archive target inventory: {e}")
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

        # Check operation-specific prerequisites
        for entry in manifest.entries:
            target_path = self.target_dir / entry.path
            current_rec = current_target_files.get(entry.path)

            # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
            if entry.operation == FileOperation.ADD.value:
                if target_path.is_symlink():
                    prereq_errors.append(f"Cannot ADD over existing symlink: {entry.path}")
                elif current_rec:
                    if self.enforce_base_match and current_rec.sha256 != entry.new_sha256:
                        prereq_errors.append(f"Cannot ADD file; path already exists with differing content: {entry.path}")

            elif entry.operation in (FileOperation.MODIFY.value, FileOperation.DELETE.value):
                if target_path.is_symlink():
                    try:
                        target_path.resolve().relative_to(self.target_dir.resolve())
                    except ValueError:
                        prereq_errors.append(f"Unsafe symlink target for {entry.operation} escapes repository root: {entry.path}")
                if not current_rec and not target_path.exists():
                    prereq_errors.append(f"Expected file to {entry.operation.lower()} not found in target: {entry.path}")
                elif self.enforce_base_match and entry.previous_sha256 and current_rec and current_rec.sha256 != entry.previous_sha256:
                    prereq_errors.append(
                        f"Base hash collision for {entry.path}: expected {entry.previous_sha256[:12]}..., found {current_rec.sha256[:12]}..."
                    )

            elif entry.operation == FileOperation.RENAME.value:
                if target_path.is_symlink():
                    prereq_errors.append(f"Cannot RENAME over existing symlink destination: {entry.path}")
                old_file = self.target_dir / entry.renamed_from if entry.renamed_from else None
                if old_file and old_file.is_symlink():
                    try:
                        old_file.resolve().relative_to(self.target_dir.resolve())
                    except ValueError:
                        prereq_errors.append(f"Cannot RENAME escaping symlink source: {entry.renamed_from}")
                old_rec = current_target_files.get(entry.renamed_from) if entry.renamed_from else None
                if not old_rec and not (old_file and old_file.exists()):
                    prereq_errors.append(f"Source file for rename not found: {entry.renamed_from}")
                elif self.enforce_base_match and entry.previous_sha256 and old_rec and old_rec.sha256 != entry.previous_sha256:
                    prereq_errors.append(
                        f"Base hash collision for rename source {entry.renamed_from}: expected {entry.previous_sha256[:12]}..."
                    )
            # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

        if prereq_errors:
            return {
                "status": "FAILED",
                "stage": "PREREQUISITE_CHECK",
                "errors": prereq_errors
            }

        if dry_run:
            return {
                "status": "DRY_RUN_PASSED",
                "stage": "PREREQUISITE_CHECK",
                "update_id": manifest.update_id,
                "operations_count": len(manifest.entries),
                "target_dir": str(self.target_dir)
            }

        # 4. Transactional Application: Safe Staging, Backup, and Atomic Rollback
        with tempfile.TemporaryDirectory(prefix="agd_stage_") as stage_dir_str, \
             tempfile.TemporaryDirectory(prefix="agd_backup_") as backup_dir_str:

            stage_dir = Path(stage_dir_str)
            backup_dir = Path(backup_dir_str)

            # A. Extract and verify payload into staging directory
            try:
                with ZipFile(zip_path, "r") as zf:
                    for entry in manifest.entries:
                        if entry.payload_path:
                            dest = stage_dir / entry.path
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            payload_bytes = zf.read(entry.payload_path)
                            dest.write_bytes(payload_bytes)
            except Exception as e:
                return {
                    "status": "FAILED",
                    "stage": "STAGING_EXTRACTION",
                    "errors": [f"Failed to extract payload to staging: {str(e)}"],
                    "rolled_back": False
                }

            # B. Pre-backup affected files for atomic rollback
            journal: List[Tuple[str, str, Optional[Path], Optional[Path]]] = []
            try:
                for entry in manifest.entries:
                    target_file = self.target_dir / entry.path

                    if entry.operation == FileOperation.ADD.value:
                        journal.append(("ADD", entry.path, target_file, None))

                    elif entry.operation == FileOperation.MODIFY.value:
                        backup_file = backup_dir / entry.path
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if target_file.exists():
                            shutil.copy2(target_file, backup_file)
                        journal.append(("MODIFY", entry.path, target_file, backup_file))

                    elif entry.operation == FileOperation.DELETE.value:
                        backup_file = backup_dir / entry.path
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if target_file.exists():
                            shutil.copy2(target_file, backup_file)
                        journal.append(("DELETE", entry.path, target_file, backup_file))

                    elif entry.operation == FileOperation.RENAME.value:
                        old_file = self.target_dir / entry.renamed_from if entry.renamed_from else None
                        backup_file = backup_dir / (entry.renamed_from or "renamed_orig")
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if old_file and old_file.exists():
                            shutil.copy2(old_file, backup_file)
                        journal.append(("RENAME", entry.path, target_file, backup_file))

            except Exception as e:
                return {
                    "status": "FAILED",
                    "stage": "BACKUP_PREPARATION",
                    "errors": [f"Failed to prepare atomic backup: {str(e)}"],
                    "rolled_back": False
                }

            # C. Execute modifications with atomic rollback on failure
            applied_entries: List[str] = []
            rollback_needed = False
            execution_error = ""

            try:
                for entry in manifest.entries:
                    target_file = self.target_dir / entry.path

                    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
                    # Revalidate destination path safety immediately before mutating (TOCTOU protection)
                    safe, reason = audit_path_ancestry_safety(self.target_dir, entry.path)
                    if not safe:
                        raise PermissionError(f"Pre-mutation safety audit failed for {entry.path}: {reason}")

                    if entry.operation in (FileOperation.ADD.value, FileOperation.MODIFY.value):
                        staged_file = stage_dir / entry.path
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            target_file.parent.resolve().relative_to(self.target_dir.resolve())
                        except ValueError:
                            raise PermissionError(f"Target directory ancestry escaped root after creation: {target_file.parent}")

                        if target_file.is_symlink():
                            target_file.unlink()

                        shutil.copy2(staged_file, target_file)
                        applied_entries.append(f"{entry.operation}: {entry.path}")

                    elif entry.operation == FileOperation.RENAME.value:
                        if entry.renamed_from:
                            safe_ren, ren_reason = audit_path_ancestry_safety(self.target_dir, entry.renamed_from)
                            if not safe_ren:
                                raise PermissionError(f"Pre-mutation safety audit failed for rename source {entry.renamed_from}: {ren_reason}")
                            old_file = self.target_dir / entry.renamed_from
                            if old_file.exists() or old_file.is_symlink():
                                old_file.unlink()
                        staged_file = stage_dir / entry.path
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            target_file.parent.resolve().relative_to(self.target_dir.resolve())
                        except ValueError:
                            raise PermissionError(f"Target directory ancestry escaped root after creation: {target_file.parent}")

                        if target_file.is_symlink():
                            target_file.unlink()

                        shutil.copy2(staged_file, target_file)
                        applied_entries.append(f"RENAME: {entry.renamed_from} -> {entry.path}")

                    elif entry.operation == FileOperation.DELETE.value:
                        if target_file.exists() or target_file.is_symlink():
                            target_file.unlink()
                            applied_entries.append(f"DELETE: {entry.path}")
                    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

                # D. Post-application verification of all modified files
                for entry in manifest.entries:
                    if entry.operation != FileOperation.DELETE.value:
                        target_file = self.target_dir / entry.path
                        if not target_file.exists():
                            raise FileNotFoundError(f"Applied file missing after write: {entry.path}")
                        written_sha = calculate_stream_sha256(target_file)
                        if written_sha != entry.new_sha256:
                            raise ValueError(
                                f"Post-apply verification failed for {entry.path}: expected {entry.new_sha256}, got {written_sha}"
                            )

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
                # E. Direct workspace audit against declared TARGET_INVENTORY.json for COMPLETE mode
                if getattr(manifest, "package_mode", "").upper() == "COMPLETE":
                    if not target_inv:
                        raise ValueError("Post-apply verification failed: TARGET_INVENTORY.json is missing or was not validated")

                    post_scanner = WorkspaceScanner(self.target_dir)
                    final_files = post_scanner.scan()

                    missing_in_target = set(target_inv.files.keys()) - set(final_files.keys())
                    if missing_in_target:
                        raise ValueError(
                            f"Post-apply verification against TARGET_INVENTORY.json missing {len(missing_in_target)} files in workspace: {sorted(missing_in_target)[:5]}"
                        )

                    extra_in_target = set(final_files.keys()) - set(target_inv.files.keys())
                    if extra_in_target:
                        raise ValueError(
                            f"Post-apply verification against TARGET_INVENTORY.json found {len(extra_in_target)} unexpected extra files in workspace: {sorted(extra_in_target)[:5]}"
                        )

                    for p, t_rec in target_inv.files.items():
                        actual_rec = final_files.get(p)
                        if not actual_rec:
                            raise ValueError(f"Post-apply verification missing file: {p}")
                        if actual_rec.sha256.lower() != t_rec.sha256.lower():
                            raise ValueError(
                                f"Post-apply verification hash mismatch for '{p}': TARGET_INVENTORY.json declared '{t_rec.sha256}', workspace has '{actual_rec.sha256}'"
                            )
                        if actual_rec.size_bytes != t_rec.size_bytes:
                            raise ValueError(
                                f"Post-apply verification size mismatch for '{p}': TARGET_INVENTORY.json declared {t_rec.size_bytes} bytes, workspace has {actual_rec.size_bytes} bytes"
                            )
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

            except Exception as e:
                rollback_needed = True
                execution_error = str(e)

            # E. Perform atomic rollback if failure occurred
            if rollback_needed:
                for op_type, path_str, tgt_file, bkp_file in reversed(journal):
                    try:
                        if op_type == "ADD":
                            if tgt_file and tgt_file.exists():
                                tgt_file.unlink()
                        elif op_type in ("MODIFY", "DELETE"):
                            if bkp_file and bkp_file.exists():
                                tgt_file.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(bkp_file, tgt_file)
                        elif op_type == "RENAME":
                            if tgt_file and tgt_file.exists():
                                tgt_file.unlink()
                            # Restore old file
                            entry_obj = next((e for e in manifest.entries if e.path == path_str), None)
                            if entry_obj and entry_obj.renamed_from and bkp_file and bkp_file.exists():
                                orig_target = self.target_dir / entry_obj.renamed_from
                                orig_target.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(bkp_file, orig_target)
                    except Exception as rb_ex:
                        logger.error(f"Error during rollback of {path_str}: {rb_ex}")

                return {
                    "status": "FAILED",
                    "stage": "APPLICATION_EXECUTION",
                    "errors": [f"Fatal error during apply (rolled back cleanly): {execution_error}"],
                    "applied_before_failure": applied_entries,
                    "rolled_back": True
                }

        # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
        is_untrusted_apply = getattr(manifest, "base_snapshot_trust_status", "VALID") != "VALID" or self.force_unsafe_unverified_base
        return {
            "status": "APPLIED",
            "trust_status": "APPLIED_FROM_UNTRUSTED_PACKAGE" if is_untrusted_apply else "VERIFIED_TRUSTED",
            "update_id": manifest.update_id,
            "mode": manifest.package_mode,
            "applied_count": len(applied_entries),
            "applied_entries": applied_entries,
            "target_dir": str(self.target_dir),
            "errors": []
        }
```

### `PackageApplier.__init__` — `Lines 26–38`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `38` (`Lines 26–38`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–38`):**
```python
    def __init__(
        self,
        target_dir: Path,
        enforce_base_match: bool = True,
        expected_base_inventory: Optional[BaselineInventory] = None,
        force_unsafe_unverified_base: bool = False,
        allow_review_mode: bool = False
    ):
        self.target_dir = target_dir.resolve()
        self.enforce_base_match = enforce_base_match and not force_unsafe_unverified_base
        self.expected_base_inventory = expected_base_inventory
        self.force_unsafe_unverified_base = force_unsafe_unverified_base
        self.allow_review_mode = allow_review_mode
```

### `PackageApplier.apply` — `Lines 40–513`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `40` إلى السطر `513` (`Lines 40–513`)
- **الوظيفة:** Apply an update ZIP package transactionally to the target directory.
- **الكود الفعلي (`Lines 40–513`):**
```python
    def apply(self, zip_path: Path, dry_run: bool = False) -> Dict[str, Any]:
        """Apply an update ZIP package transactionally to the target directory."""
        # 1. Verify archive format, safety, and hashes
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
        verification = PackageVerifier.verify_package(zip_path)
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED
        if verification["status"] != "VALID":
            return {
                "status": "FAILED",
                "stage": "VERIFICATION",
                "errors": verification["errors"]
            }

        manifest = UpdateManifest.from_dict(verification["manifest"])

        # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
        # 1.1 Package Mode Audit: REVIEW mode cannot be applied as complete repository reconstruction
        if getattr(manifest, "package_mode", "").upper() == "REVIEW" and not self.allow_review_mode:
            return {
                "status": "FAILED",
                "stage": "PACKAGE_MODE_AUDIT",
                "errors": [
                    f"Package '{manifest.update_id}' is in REVIEW mode (declared exclusions: {manifest.exclusions_count}). "
                    "REVIEW packages contain partial audit payloads and cannot be applied as complete repository reconstruction. "
                    "Applying a REVIEW package as a repository reconstruction is blocked. "
                    "Use a COMPLETE package, or explicitly pass allow_review_mode=True (CLI: --allow-review-mode) for review extraction only."
                ]
            }

        # 2. Audit all manifest entry paths and destination ancestry at point of application
        path_errors: List[str] = []
        for entry in manifest.entries:
            safe, reason = audit_path_ancestry_safety(self.target_dir, entry.path)
            if not safe:
                path_errors.append(f"Unsafe target path or escaping ancestry: {entry.path} ({reason})")
            if entry.payload_path:
                safe_pay, pay_reason = is_safe_relative_path(entry.payload_path)
                if not safe_pay:
                    path_errors.append(f"Unsafe payload path at application time: {entry.payload_path} ({pay_reason})")
            if entry.renamed_from:
                safe_ren, ren_reason = audit_path_ancestry_safety(self.target_dir, entry.renamed_from)
                if not safe_ren:
                    path_errors.append(f"Unsafe rename source or escaping ancestry: {entry.renamed_from} ({ren_reason})")

        if path_errors:
            return {
                "status": "FAILED",
                "stage": "PATH_SECURITY_AUDIT",
                "errors": path_errors
            }
        # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

        # 3. Scan current target workspace and verify prerequisites
        scanner = WorkspaceScanner(self.target_dir)
        current_target_files = scanner.scan()

        prereq_errors: List[str] = []

        # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
        # Check base snapshot trust status
        manifest_base_trust = getattr(manifest, "base_snapshot_trust_status", "VALID")
        if manifest_base_trust != "VALID" or (manifest.status and manifest.status.startswith("UNTRUSTED")):
            if not self.force_unsafe_unverified_base:
                prereq_errors.append(
                    f"Package was built from an untrusted/invalid baseline ({manifest_base_trust}: {getattr(manifest, 'base_snapshot_invalidation_reason', '')}). "
                    "Applying updates generated from untrusted baselines is strictly blocked. Use force_unsafe_unverified_base=True to override at your own risk."
                )
        # END CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED

        # Resolve base inventory if provided or discoverable
        base_inv: Optional[BaselineInventory] = self.expected_base_inventory
        if not base_inv and (self.target_dir / "tools" / "update_packages" / "registry").exists():
            try:
                state_mgr = UpdateStateManager(self.target_dir)
                base_inv = state_mgr.get_baseline(manifest.base_snapshot_id)
            except Exception:
                base_inv = None

        # Enforce complete base inventory match if in COMPLETE mode or if base inventory is known
        if self.enforce_base_match:
            # Check for empty directory when a non-empty base is declared
            is_empty_workspace = len(current_target_files) == 0
            if is_empty_workspace and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                prereq_errors.append(
                    f"Target workspace is empty, but package declares required base snapshot: {manifest.base_snapshot_id}"
                )

            # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
            # Defect 1 Fix: In verified mode, an unresolvable or missing required base inventory MUST fail closed immediately
            if not base_inv and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                prereq_errors.append(
                    f"Required base snapshot '{manifest.base_snapshot_id}' cannot be resolved or loaded in target workspace or baseline registry. "
                    "In verified mode, applying updates against an unverified/nonexistent base baseline is strictly rejected."
                )

            if base_inv:
                # Complete inventory match check
                for b_path, b_rec in base_inv.files.items():
                    curr_rec = current_target_files.get(b_path)
                    if not curr_rec:
                        prereq_errors.append(f"Required base file missing from target workspace: {b_path}")
                    elif curr_rec.sha256 != b_rec.sha256:
                        prereq_errors.append(
                            f"Base file content mismatch for {b_path}: expected {b_rec.sha256[:12]}..., got {curr_rec.sha256[:12]}..."
                        )

                # Check for unexpected extra files in strict base mode
                extra_files = set(current_target_files.keys()) - set(base_inv.files.keys())
                if extra_files:
                    prereq_errors.append(
                        f"Target workspace contains {len(extra_files)} unexpected extra files not present in baseline {base_inv.baseline_id}: {sorted(extra_files)[:5]}"
                    )

                # Defect 2 Fix: Base snapshot hash validation against trusted baseline
                expected_base_hash = compute_bytes_sha256(base_inv.to_json().encode("utf-8"))
                if manifest.base_snapshot_hash and manifest.base_snapshot_hash.lower() != expected_base_hash.lower():
                    prereq_errors.append(
                        f"Base snapshot hash tampering detected: manifest declares base_snapshot_hash '{manifest.base_snapshot_hash}', "
                        f"but trusted baseline '{base_inv.baseline_id}' serialization hash is '{expected_base_hash}'."
                    )
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

        # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
        # Defect A & B: Target snapshot and TARGET_INVENTORY.json consistency validation
        is_complete_mode = getattr(manifest, "package_mode", "").upper() == "COMPLETE"
        target_inv: Optional[BaselineInventory] = None
        try:
            with ZipFile(zip_path, "r") as zf:
                names = zf.namelist()
                if is_complete_mode and "TARGET_INVENTORY.json" not in names:
                    prereq_errors.append("COMPLETE mode package requires TARGET_INVENTORY.json, but it is missing from archive root")
                elif "TARGET_INVENTORY.json" in names:
                    decl_target_bytes = zf.read("TARGET_INVENTORY.json")
                    decl_target_hash = compute_bytes_sha256(decl_target_bytes)
                    if manifest.target_snapshot_hash and manifest.target_snapshot_hash.lower() != decl_target_hash.lower():
                        prereq_errors.append(
                            f"Target snapshot hash tampering detected: manifest declares target_snapshot_hash '{manifest.target_snapshot_hash}', "
                            f"but package TARGET_INVENTORY.json has hash '{decl_target_hash}'."
                        )
                    else:
                        try:
                            decl_target_data = json.loads(decl_target_bytes.decode("utf-8"))
                            target_inv = BaselineInventory.from_dict(decl_target_data)
                            canonical_target_bytes = target_inv.to_json().encode("utf-8")
                            canonical_target_hash = compute_bytes_sha256(canonical_target_bytes)
                            if canonical_target_hash.lower() != decl_target_hash.lower():
                                prereq_errors.append(
                                    f"TARGET_INVENTORY.json is not in canonical serialization format: "
                                    f"declared hash '{decl_target_hash}', canonical serialization hash '{canonical_target_hash}'."
                                )

                            # If base_inv is loaded, derive expected target inventory and compare 1:1
                            if base_inv:
                                derived_files: Dict[str, Tuple[str, int]] = {
                                    p: (rec.sha256, rec.size_bytes)
                                    for p, rec in base_inv.files.items()
                                }
                                for entry in manifest.entries:
                                    if entry.operation in (FileOperation.ADD.value, FileOperation.MODIFY.value):
                                        derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes)
                                    elif entry.operation == FileOperation.DELETE.value:
                                        derived_files.pop(entry.path, None)
                                    elif entry.operation == FileOperation.RENAME.value:
                                        if entry.renamed_from:
                                            derived_files.pop(entry.renamed_from, None)
                                        derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes)

                                # Check for missing files in TARGET_INVENTORY.json
                                missing_in_target = set(derived_files.keys()) - set(target_inv.files.keys())
                                if missing_in_target:
                                    prereq_errors.append(
                                        f"TARGET_INVENTORY.json is missing {len(missing_in_target)} files derived from baseline and manifest: {sorted(missing_in_target)[:5]}"
                                    )

                                # Check for unexpected extra files in TARGET_INVENTORY.json
                                extra_in_target = set(target_inv.files.keys()) - set(derived_files.keys())
                                if extra_in_target:
                                    prereq_errors.append(
                                        f"TARGET_INVENTORY.json contains {len(extra_in_target)} unexpected extra files: {sorted(extra_in_target)[:5]}"
                                    )

                                # Check hash and size for every derived file (including unchanged files)
                                for p, (exp_sha, exp_size) in derived_files.items():
                                    t_rec = target_inv.files.get(p)
                                    if t_rec:
                                        if t_rec.sha256.lower() != exp_sha.lower():
                                            prereq_errors.append(
                                                f"TARGET_INVENTORY.json entry for '{p}' contradicts derived target state: "
                                                f"expected sha256 '{exp_sha}', declared '{t_rec.sha256}'."
                                            )
                                        if t_rec.size_bytes != exp_size:
                                            prereq_errors.append(
                                                f"TARGET_INVENTORY.json entry for '{p}' size mismatch: "
                                                f"expected {exp_size} bytes, declared {t_rec.size_bytes} bytes."
                                            )
                        except Exception as parse_ex:
                            prereq_errors.append(f"TARGET_INVENTORY.json schema/parsing error: {parse_ex}")
        except Exception as e:
            prereq_errors.append(f"Cannot inspect archive target inventory: {e}")
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

        # Check operation-specific prerequisites
        for entry in manifest.entries:
            target_path = self.target_dir / entry.path
            current_rec = current_target_files.get(entry.path)

            # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
            if entry.operation == FileOperation.ADD.value:
                if target_path.is_symlink():
                    prereq_errors.append(f"Cannot ADD over existing symlink: {entry.path}")
                elif current_rec:
                    if self.enforce_base_match and current_rec.sha256 != entry.new_sha256:
                        prereq_errors.append(f"Cannot ADD file; path already exists with differing content: {entry.path}")

            elif entry.operation in (FileOperation.MODIFY.value, FileOperation.DELETE.value):
                if target_path.is_symlink():
                    try:
                        target_path.resolve().relative_to(self.target_dir.resolve())
                    except ValueError:
                        prereq_errors.append(f"Unsafe symlink target for {entry.operation} escapes repository root: {entry.path}")
                if not current_rec and not target_path.exists():
                    prereq_errors.append(f"Expected file to {entry.operation.lower()} not found in target: {entry.path}")
                elif self.enforce_base_match and entry.previous_sha256 and current_rec and current_rec.sha256 != entry.previous_sha256:
                    prereq_errors.append(
                        f"Base hash collision for {entry.path}: expected {entry.previous_sha256[:12]}..., found {current_rec.sha256[:12]}..."
                    )

            elif entry.operation == FileOperation.RENAME.value:
                if target_path.is_symlink():
                    prereq_errors.append(f"Cannot RENAME over existing symlink destination: {entry.path}")
                old_file = self.target_dir / entry.renamed_from if entry.renamed_from else None
                if old_file and old_file.is_symlink():
                    try:
                        old_file.resolve().relative_to(self.target_dir.resolve())
                    except ValueError:
                        prereq_errors.append(f"Cannot RENAME escaping symlink source: {entry.renamed_from}")
                old_rec = current_target_files.get(entry.renamed_from) if entry.renamed_from else None
                if not old_rec and not (old_file and old_file.exists()):
                    prereq_errors.append(f"Source file for rename not found: {entry.renamed_from}")
                elif self.enforce_base_match and entry.previous_sha256 and old_rec and old_rec.sha256 != entry.previous_sha256:
                    prereq_errors.append(
                        f"Base hash collision for rename source {entry.renamed_from}: expected {entry.previous_sha256[:12]}..."
                    )
            # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

        if prereq_errors:
            return {
                "status": "FAILED",
                "stage": "PREREQUISITE_CHECK",
                "errors": prereq_errors
            }

        if dry_run:
            return {
                "status": "DRY_RUN_PASSED",
                "stage": "PREREQUISITE_CHECK",
                "update_id": manifest.update_id,
                "operations_count": len(manifest.entries),
                "target_dir": str(self.target_dir)
            }

        # 4. Transactional Application: Safe Staging, Backup, and Atomic Rollback
        with tempfile.TemporaryDirectory(prefix="agd_stage_") as stage_dir_str, \
             tempfile.TemporaryDirectory(prefix="agd_backup_") as backup_dir_str:

            stage_dir = Path(stage_dir_str)
            backup_dir = Path(backup_dir_str)

            # A. Extract and verify payload into staging directory
            try:
                with ZipFile(zip_path, "r") as zf:
                    for entry in manifest.entries:
                        if entry.payload_path:
                            dest = stage_dir / entry.path
                            dest.parent.mkdir(parents=True, exist_ok=True)
                            payload_bytes = zf.read(entry.payload_path)
                            dest.write_bytes(payload_bytes)
            except Exception as e:
                return {
                    "status": "FAILED",
                    "stage": "STAGING_EXTRACTION",
                    "errors": [f"Failed to extract payload to staging: {str(e)}"],
                    "rolled_back": False
                }

            # B. Pre-backup affected files for atomic rollback
            journal: List[Tuple[str, str, Optional[Path], Optional[Path]]] = []
            try:
                for entry in manifest.entries:
                    target_file = self.target_dir / entry.path

                    if entry.operation == FileOperation.ADD.value:
                        journal.append(("ADD", entry.path, target_file, None))

                    elif entry.operation == FileOperation.MODIFY.value:
                        backup_file = backup_dir / entry.path
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if target_file.exists():
                            shutil.copy2(target_file, backup_file)
                        journal.append(("MODIFY", entry.path, target_file, backup_file))

                    elif entry.operation == FileOperation.DELETE.value:
                        backup_file = backup_dir / entry.path
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if target_file.exists():
                            shutil.copy2(target_file, backup_file)
                        journal.append(("DELETE", entry.path, target_file, backup_file))

                    elif entry.operation == FileOperation.RENAME.value:
                        old_file = self.target_dir / entry.renamed_from if entry.renamed_from else None
                        backup_file = backup_dir / (entry.renamed_from or "renamed_orig")
                        backup_file.parent.mkdir(parents=True, exist_ok=True)
                        if old_file and old_file.exists():
                            shutil.copy2(old_file, backup_file)
                        journal.append(("RENAME", entry.path, target_file, backup_file))

            except Exception as e:
                return {
                    "status": "FAILED",
                    "stage": "BACKUP_PREPARATION",
                    "errors": [f"Failed to prepare atomic backup: {str(e)}"],
                    "rolled_back": False
                }

            # C. Execute modifications with atomic rollback on failure
            applied_entries: List[str] = []
            rollback_needed = False
            execution_error = ""

            try:
                for entry in manifest.entries:
                    target_file = self.target_dir / entry.path

                    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
                    # Revalidate destination path safety immediately before mutating (TOCTOU protection)
                    safe, reason = audit_path_ancestry_safety(self.target_dir, entry.path)
                    if not safe:
                        raise PermissionError(f"Pre-mutation safety audit failed for {entry.path}: {reason}")

                    if entry.operation in (FileOperation.ADD.value, FileOperation.MODIFY.value):
                        staged_file = stage_dir / entry.path
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            target_file.parent.resolve().relative_to(self.target_dir.resolve())
                        except ValueError:
                            raise PermissionError(f"Target directory ancestry escaped root after creation: {target_file.parent}")

                        if target_file.is_symlink():
                            target_file.unlink()

                        shutil.copy2(staged_file, target_file)
                        applied_entries.append(f"{entry.operation}: {entry.path}")

                    elif entry.operation == FileOperation.RENAME.value:
                        if entry.renamed_from:
                            safe_ren, ren_reason = audit_path_ancestry_safety(self.target_dir, entry.renamed_from)
                            if not safe_ren:
                                raise PermissionError(f"Pre-mutation safety audit failed for rename source {entry.renamed_from}: {ren_reason}")
                            old_file = self.target_dir / entry.renamed_from
                            if old_file.exists() or old_file.is_symlink():
                                old_file.unlink()
                        staged_file = stage_dir / entry.path
                        target_file.parent.mkdir(parents=True, exist_ok=True)
                        try:
                            target_file.parent.resolve().relative_to(self.target_dir.resolve())
                        except ValueError:
                            raise PermissionError(f"Target directory ancestry escaped root after creation: {target_file.parent}")

                        if target_file.is_symlink():
                            target_file.unlink()

                        shutil.copy2(staged_file, target_file)
                        applied_entries.append(f"RENAME: {entry.renamed_from} -> {entry.path}")

                    elif entry.operation == FileOperation.DELETE.value:
                        if target_file.exists() or target_file.is_symlink():
                            target_file.unlink()
                            applied_entries.append(f"DELETE: {entry.path}")
                    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

                # D. Post-application verification of all modified files
                for entry in manifest.entries:
                    if entry.operation != FileOperation.DELETE.value:
                        target_file = self.target_dir / entry.path
                        if not target_file.exists():
                            raise FileNotFoundError(f"Applied file missing after write: {entry.path}")
                        written_sha = calculate_stream_sha256(target_file)
                        if written_sha != entry.new_sha256:
                            raise ValueError(
                                f"Post-apply verification failed for {entry.path}: expected {entry.new_sha256}, got {written_sha}"
                            )

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
                # E. Direct workspace audit against declared TARGET_INVENTORY.json for COMPLETE mode
                if getattr(manifest, "package_mode", "").upper() == "COMPLETE":
                    if not target_inv:
                        raise ValueError("Post-apply verification failed: TARGET_INVENTORY.json is missing or was not validated")

                    post_scanner = WorkspaceScanner(self.target_dir)
                    final_files = post_scanner.scan()

                    missing_in_target = set(target_inv.files.keys()) - set(final_files.keys())
                    if missing_in_target:
                        raise ValueError(
                            f"Post-apply verification against TARGET_INVENTORY.json missing {len(missing_in_target)} files in workspace: {sorted(missing_in_target)[:5]}"
                        )

                    extra_in_target = set(final_files.keys()) - set(target_inv.files.keys())
                    if extra_in_target:
                        raise ValueError(
                            f"Post-apply verification against TARGET_INVENTORY.json found {len(extra_in_target)} unexpected extra files in workspace: {sorted(extra_in_target)[:5]}"
                        )

                    for p, t_rec in target_inv.files.items():
                        actual_rec = final_files.get(p)
                        if not actual_rec:
                            raise ValueError(f"Post-apply verification missing file: {p}")
                        if actual_rec.sha256.lower() != t_rec.sha256.lower():
                            raise ValueError(
                                f"Post-apply verification hash mismatch for '{p}': TARGET_INVENTORY.json declared '{t_rec.sha256}', workspace has '{actual_rec.sha256}'"
                            )
                        if actual_rec.size_bytes != t_rec.size_bytes:
                            raise ValueError(
                                f"Post-apply verification size mismatch for '{p}': TARGET_INVENTORY.json declared {t_rec.size_bytes} bytes, workspace has {actual_rec.size_bytes} bytes"
                            )
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

            except Exception as e:
                rollback_needed = True
                execution_error = str(e)

            # E. Perform atomic rollback if failure occurred
            if rollback_needed:
                for op_type, path_str, tgt_file, bkp_file in reversed(journal):
                    try:
                        if op_type == "ADD":
                            if tgt_file and tgt_file.exists():
                                tgt_file.unlink()
                        elif op_type in ("MODIFY", "DELETE"):
                            if bkp_file and bkp_file.exists():
                                tgt_file.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(bkp_file, tgt_file)
                        elif op_type == "RENAME":
                            if tgt_file and tgt_file.exists():
                                tgt_file.unlink()
                            # Restore old file
                            entry_obj = next((e for e in manifest.entries if e.path == path_str), None)
                            if entry_obj and entry_obj.renamed_from and bkp_file and bkp_file.exists():
                                orig_target = self.target_dir / entry_obj.renamed_from
                                orig_target.parent.mkdir(parents=True, exist_ok=True)
                                shutil.copy2(bkp_file, orig_target)
                    except Exception as rb_ex:
                        logger.error(f"Error during rollback of {path_str}: {rb_ex}")

                return {
                    "status": "FAILED",
                    "stage": "APPLICATION_EXECUTION",
                    "errors": [f"Fatal error during apply (rolled back cleanly): {execution_error}"],
                    "applied_before_failure": applied_entries,
                    "rolled_back": True
                }

        # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
        is_untrusted_apply = getattr(manifest, "base_snapshot_trust_status", "VALID") != "VALID" or self.force_unsafe_unverified_base
        return {
            "status": "APPLIED",
            "trust_status": "APPLIED_FROM_UNTRUSTED_PACKAGE" if is_untrusted_apply else "VERIFIED_TRUSTED",
            "update_id": manifest.update_id,
            "mode": manifest.package_mode,
            "applied_count": len(applied_entries),
            "applied_entries": applied_entries,
            "target_dir": str(self.target_dir),
            "errors": []
        }
```
