# مرآة الكود التفصيلية: `tools/update_packages/verifier.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/verifier.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/verifier.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `433` (`Lines 1–433`)
- **بصمة الملف (`SHA-256`):** `e508522989c9b47ad1d74ff7316988617ef1c12b573fdce542c1454de2f28ae5`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `is_safe_relative_path` | `function` | `Lines 34–71` | `def is_safe_relative_path(path_str: str) -> Tuple[bool, str]:` | Audit a path against directory traversal, absolute paths, drive letters, and invalid characters. |
| `is_safe_archive_path` | `function` | `Lines 75–78` | `def is_safe_archive_path(path_str: str) -> bool:` | Audit archive entry path against directory traversal vulnerabilities. |
| `audit_path_ancestry_safety` | `function` | `Lines 81–135` | `def audit_path_ancestry_safety(target_dir: Path, rel_path: str) -> Tuple[bool, str]:` | Validates that rel_path resolves strictly within target_dir, and no component |
| `PackageVerifier` | `class` | `Lines 139–432` | `class PackageVerifier:` | Verifies format, path safety, and byte-level hash integrity of update archives. |
| `PackageVerifier.verify_package` | `method` | `Lines 144–432` | `def verify_package(` | Verify the integrity, safety, and content authenticity of an update ZIP. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `is_safe_relative_path` — `Lines 34–71`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `34` إلى السطر `71` (`Lines 34–71`)
- **الوظيفة:** Audit a path against directory traversal, absolute paths, drive letters, and invalid characters.
- **الكود الفعلي (`Lines 34–71`):**
```python
def is_safe_relative_path(path_str: str) -> Tuple[bool, str]:
    """Audit a path against directory traversal, absolute paths, drive letters, and invalid characters."""
    if not path_str or not isinstance(path_str, str):
        return False, "Path is empty or not a string"
    if "\x00" in path_str:
        return False, "Path contains null byte"

    norm = path_str.replace("\\", "/")
    if norm.startswith("/"):
        return False, "Leading root slash not allowed"
    if norm.startswith("//") or path_str.startswith("\\\\"):
        return False, "UNC path not allowed"
    if re.match(r"^[a-zA-Z]:", norm):
        return False, "Windows drive letter not allowed"
    if ":" in norm:
        return False, "Colon in path not allowed"

    parts = norm.split("/")
    if any(part == ".." for part in parts):
        return False, "Directory traversal '..' component not allowed"
    if any(part == "." for part in parts if len(parts) > 1):
        return False, "Dot '.' segment in multi-part path not allowed"
    if any(part == "" for part in parts):
        return False, "Empty path segment or trailing slash not allowed"

    for part in parts:
        stem = part.split(".")[0].upper()
        if stem in WINDOWS_RESERVED_NAMES:
            return False, f"Windows reserved device name: {stem}"

    try:
        pure = PurePosixPath(norm)
        if pure.is_absolute() or ".." in pure.parts:
            return False, "PurePosixPath normalization detected traversal or absolute path"
    except Exception as e:
        return False, f"Path normalization failed: {e}"

    return True, ""
```

### `is_safe_archive_path` — `Lines 75–78`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `75` إلى السطر `78` (`Lines 75–78`)
- **الوظيفة:** Audit archive entry path against directory traversal vulnerabilities.
- **الكود الفعلي (`Lines 75–78`):**
```python
def is_safe_archive_path(path_str: str) -> bool:
    """Audit archive entry path against directory traversal vulnerabilities."""
    safe, _ = is_safe_relative_path(path_str)
    return safe
```

### `audit_path_ancestry_safety` — `Lines 81–135`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `81` إلى السطر `135` (`Lines 81–135`)
- **الوظيفة:** Validates that rel_path resolves strictly within target_dir, and no component
- **الكود الفعلي (`Lines 81–135`):**
```python
def audit_path_ancestry_safety(target_dir: Path, rel_path: str) -> Tuple[bool, str]:
    """
    Validates that rel_path resolves strictly within target_dir, and no component
    in its ancestry or the destination itself escapes target_dir via symlinks, junctions, or hardlinks.
    Rejects unsafe symlink destinations and symlink-based target replacements.
    """
    canonical_root = target_dir.resolve()
    safe, reason = is_safe_relative_path(rel_path)
    if not safe:
        return False, f"Relative path syntax violation: {reason}"

    # Walk each component from canonical root down to leaf
    parts = Path(rel_path).parts
    curr = canonical_root
    for part in parts:
        curr = curr / part
        # Check if curr is a symlink or junction
        if curr.is_symlink():
            try:
                resolved_link = curr.resolve()
                resolved_link.relative_to(canonical_root)
            except ValueError:
                return False, f"Symlink component '{part}' (at '{curr}') resolves outside repository root to '{resolved_link}'"
        elif curr.exists():
            try:
                resolved = curr.resolve()
                resolved.relative_to(canonical_root)
            except ValueError:
                return False, f"Component '{part}' (at '{curr}') resolves outside repository root to '{resolved}'"

    # Also resolve deepest existing ancestor for paths that don't exist yet
    target_file = target_dir / rel_path
    deepest = target_file
    non_existing: List[str] = []
    while not deepest.exists() and not deepest.is_symlink():
        if deepest == canonical_root or deepest.parent == deepest:
            break
        non_existing.append(deepest.name)
        deepest = deepest.parent

    try:
        resolved_deepest = deepest.resolve()
        resolved_deepest.relative_to(canonical_root)
    except ValueError:
        return False, f"Deepest existing parent component '{deepest}' resolves outside repository root to '{resolved_deepest}'"

    for part in reversed(non_existing):
        resolved_deepest = resolved_deepest / part

    try:
        resolved_deepest.relative_to(canonical_root)
    except ValueError:
        return False, f"Target path '{rel_path}' resolves outside repository root to '{resolved_deepest}'"

    return True, ""
```

### `PackageVerifier` — `Lines 139–432`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `139` إلى السطر `432` (`Lines 139–432`)
- **الوظيفة:** Verifies format, path safety, and byte-level hash integrity of update archives.
- **الكود الفعلي (`Lines 139–432`):**
```python
class PackageVerifier:
    """Verifies format, path safety, and byte-level hash integrity of update archives."""

    # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
    @staticmethod
    def verify_package(
        zip_path: Path,
        expected_base_inventory: Any = None,
        workspace_root: Optional[Path] = None
    ) -> Dict[str, Any]:
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED
        """Verify the integrity, safety, and content authenticity of an update ZIP."""
        zip_path = zip_path.resolve()
        if not zip_path.exists():
            return {
                "status": "INVALID",
                "errors": [f"Archive file not found: {zip_path}"],
                "manifest": None
            }

        errors: List[str] = []
        manifest: Any = None
        try:
            with ZipFile(zip_path, "r") as zf:
                names = zf.namelist()

                # 1. Audit archive entry name safety and boundary
                for name in names:
                    safe, reason = is_safe_relative_path(name)
                    if not safe:
                        errors.append(f"Unsafe archive entry path: {name} ({reason})")
                    elif name not in ALLOWED_ROOT_FILES and not name.startswith("payload/"):
                        errors.append(f"Unexpected archive entry outside root controls or payload/: {name}")

                if errors:
                    return {"status": "INVALID", "errors": errors, "manifest": None}

                # 2. Check manifest existence
                if "UPDATE_MANIFEST.json" not in names:
                    return {
                        "status": "INVALID",
                        "errors": ["Missing UPDATE_MANIFEST.json at root of archive"],
                        "manifest": None
                    }

                # 3. Read and parse manifest
                try:
                    manifest_bytes = zf.read("UPDATE_MANIFEST.json")
                    manifest_data = json.loads(manifest_bytes.decode("utf-8"))
                    manifest = UpdateManifest.from_dict(manifest_data)
                except Exception as e:
                    return {
                        "status": "INVALID",
                        "errors": [f"Malformed UPDATE_MANIFEST.json: {str(e)}"],
                        "manifest": None
                    }

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED | Author: orchestrator-planner
                # 3.1 Validate base_snapshot_hash against trusted baseline serialization if resolvable
                base_to_verify = expected_base_inventory
                if not base_to_verify and manifest.base_snapshot_id:
                    # Search for baseline in registry relative to workspace_root, archive dir, or cwd
                    search_dirs = []
                    if workspace_root:
                        search_dirs.append(workspace_root.resolve())
                    search_dirs.append(zip_path.parent.resolve())
                    search_dirs.append(Path.cwd().resolve())
                    for sd in search_dirs:
                        candidate_base_file = sd / "tools" / "update_packages" / "registry" / "baselines" / f"{manifest.base_snapshot_id}.json"
                        if candidate_base_file.exists():
                            try:
                                candidate_data = json.loads(candidate_base_file.read_text(encoding="utf-8"))
                                base_to_verify = BaselineInventory.from_dict(candidate_data)
                                break
                            except Exception:
                                pass

                if base_to_verify:
                    expected_base_hash = compute_bytes_sha256(base_to_verify.to_json().encode("utf-8"))
                    if manifest.base_snapshot_hash and manifest.base_snapshot_hash.lower() != expected_base_hash.lower():
                        errors.append(
                            f"Tampered or mismatched base_snapshot_hash: manifest declares '{manifest.base_snapshot_hash}', "
                            f"expected '{expected_base_hash}' from trusted baseline '{base_to_verify.baseline_id}'."
                        )
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
                # 3.2 Validate TARGET_INVENTORY.json and target_snapshot_hash
                is_complete_mode = getattr(manifest, "package_mode", "").upper() == "COMPLETE"
                if is_complete_mode and "TARGET_INVENTORY.json" not in names:
                    errors.append("COMPLETE mode package requires TARGET_INVENTORY.json at archive root, but it is missing.")

                if "TARGET_INVENTORY.json" in names:
                    try:
                        target_inv_bytes = zf.read("TARGET_INVENTORY.json")
                        actual_target_hash = compute_bytes_sha256(target_inv_bytes)

                        # Validate target_snapshot_hash against raw archive file
                        if manifest.target_snapshot_hash and manifest.target_snapshot_hash.lower() != actual_target_hash.lower():
                            errors.append(
                                f"Tampered or mismatched target_snapshot_hash: manifest declares '{manifest.target_snapshot_hash}', "
                                f"but declared TARGET_INVENTORY.json serialization hash is '{actual_target_hash}'."
                            )

                        # Validate schema and canonical serialization
                        target_inv_data = json.loads(target_inv_bytes.decode("utf-8"))
                        target_inv_obj = BaselineInventory.from_dict(target_inv_data)
                        canonical_target_bytes = target_inv_obj.to_json().encode("utf-8")
                        canonical_target_hash = compute_bytes_sha256(canonical_target_bytes)
                        if canonical_target_hash.lower() != actual_target_hash.lower():
                            errors.append(
                                f"TARGET_INVENTORY.json is not in canonical serialization format: "
                                f"file hash is '{actual_target_hash}', canonical serialization hash is '{canonical_target_hash}'."
                            )

                        t_files = target_inv_obj.files

                        # Derive expected complete target inventory from baseline + manifest operations
                        if base_to_verify:
                            derived_files: Dict[str, Tuple[str, int, bool]] = {
                                p: (rec.sha256, rec.size_bytes, rec.is_binary)
                                for p, rec in base_to_verify.files.items()
                            }
                            for entry in manifest.entries:
                                if entry.operation in ("ADD", "MODIFY"):
                                    derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes, entry.is_binary)
                                elif entry.operation == "DELETE":
                                    derived_files.pop(entry.path, None)
                                elif entry.operation == "RENAME":
                                    if entry.renamed_from:
                                        derived_files.pop(entry.renamed_from, None)
                                    derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes, entry.is_binary)

                            # Check for missing files in TARGET_INVENTORY.json
                            missing_in_target = set(derived_files.keys()) - set(t_files.keys())
                            if missing_in_target:
                                errors.append(
                                    f"TARGET_INVENTORY.json is missing {len(missing_in_target)} files derived from baseline and manifest operations: {sorted(missing_in_target)[:5]}"
                                )

                            # Check for unexpected extra files in TARGET_INVENTORY.json
                            extra_in_target = set(t_files.keys()) - set(derived_files.keys())
                            if extra_in_target:
                                errors.append(
                                    f"TARGET_INVENTORY.json contains {len(extra_in_target)} unexpected extra files not derived from baseline and manifest: {sorted(extra_in_target)[:5]}"
                                )

                            # Check hash and size for every derived file (including unchanged files)
                            for p, (exp_sha, exp_size, exp_bin) in derived_files.items():
                                t_rec = t_files.get(p)
                                if t_rec:
                                    if t_rec.sha256.lower() != exp_sha.lower():
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry for '{p}' contradicts derived target state: "
                                            f"expected sha256 '{exp_sha}', declared '{t_rec.sha256}'."
                                        )
                                    if t_rec.size_bytes != exp_size:
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry for '{p}' size mismatch: "
                                            f"expected {exp_size} bytes, declared {t_rec.size_bytes} bytes."
                                        )
                        elif is_complete_mode and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                            # In COMPLETE mode with a required non-empty baseline that cannot be resolved
                            if expected_base_inventory is not None or workspace_root is not None:
                                errors.append(
                                    f"COMPLETE mode package requires verifiable baseline '{manifest.base_snapshot_id}' to validate target inventory consistency, but baseline could not be resolved."
                                )
                        else:
                            # Baseline is empty/null or not provided in non-complete mode; verify manifest entries
                            for entry in manifest.entries:
                                if entry.operation in ("ADD", "MODIFY"):
                                    t_rec = t_files.get(entry.path)
                                    if not t_rec or t_rec.sha256.lower() != (entry.new_sha256 or "").lower():
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry inconsistent with manifest for '{entry.path}'"
                                        )
                                elif entry.operation == "DELETE":
                                    if entry.path in t_files:
                                        errors.append(
                                            f"TARGET_INVENTORY.json contains file '{entry.path}' declared as DELETE in manifest"
                                        )
                    except Exception as e:
                        errors.append(f"Failed to inspect TARGET_INVENTORY.json: {e}")
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

                # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
                # Enforce complete mode integrity: COMPLETE packages must have zero exclusions
                if getattr(manifest, "package_mode", "").upper() == "COMPLETE" and manifest.exclusions_count > 0:
                    errors.append(
                        f"COMPLETE package declares {manifest.exclusions_count} exclusions; COMPLETE mode updates must have zero required content exclusions."
                    )
                # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

                # 4. Strictly audit manifest entry paths against traversal and collisions
                seen_target_paths: Set[str] = set()
                declared_payload_paths: Set[str] = set()
                sha_hex_pattern = re.compile(r"^[0-9a-f]{64}$")

                for entry in manifest.entries:
                    # Validate entry.path
                    safe, reason = is_safe_relative_path(entry.path)
                    if not safe:
                        errors.append(f"Unsafe target path in manifest entry: {entry.path} ({reason})")

                    if entry.path in seen_target_paths:
                        errors.append(f"Duplicate target path declared in manifest: {entry.path}")
                    seen_target_paths.add(entry.path)

                    # Validate payload_path if present
                    if entry.payload_path:
                        safe_pay, pay_reason = is_safe_relative_path(entry.payload_path)
                        if not safe_pay:
                            errors.append(f"Unsafe payload_path in manifest entry for {entry.path}: {entry.payload_path} ({pay_reason})")
                        elif not entry.payload_path.startswith("payload/"):
                            errors.append(f"Payload path does not start with payload/: {entry.payload_path}")
                        declared_payload_paths.add(entry.payload_path)

                    # Validate renamed_from if present
                    if entry.renamed_from:
                        safe_ren, ren_reason = is_safe_relative_path(entry.renamed_from)
                        if not safe_ren:
                            errors.append(f"Unsafe renamed_from path in manifest entry: {entry.renamed_from} ({ren_reason})")

                    # Validate hash formats
                    if entry.new_sha256 and not sha_hex_pattern.match(entry.new_sha256):
                        errors.append(f"Invalid new_sha256 format for {entry.path}: {entry.new_sha256}")
                    if entry.previous_sha256 and not sha_hex_pattern.match(entry.previous_sha256):
                        errors.append(f"Invalid previous_sha256 format for {entry.path}: {entry.previous_sha256}")

                    # Validate payload content and byte hash against manifest
                    if entry.payload_path:
                        if entry.payload_path not in names:
                            errors.append(f"Payload file missing in archive: {entry.payload_path}")
                            continue

                        payload_bytes = zf.read(entry.payload_path)
                        payload_sha = compute_bytes_sha256(payload_bytes)

                        if payload_sha != entry.new_sha256:
                            errors.append(
                                f"Corrupted payload for {entry.path}: expected {entry.new_sha256}, got {payload_sha}"
                            )
                        if len(payload_bytes) != entry.size_bytes:
                            errors.append(
                                f"Byte size mismatch for {entry.path}: expected {entry.size_bytes}, got {len(payload_bytes)}"
                            )

                # 5. Check for undeclared payload files in ZIP
                actual_payload_files = {name for name in names if name.startswith("payload/")}
                undeclared_payloads = actual_payload_files - declared_payload_paths
                if undeclared_payloads:
                    for up in sorted(undeclared_payloads):
                        errors.append(f"Undeclared payload file found in archive: {up}")

                # 6. Validate auxiliary EXCLUSIONS.json if present
                if "EXCLUSIONS.json" in names:
                    try:
                        excl_bytes = zf.read("EXCLUSIONS.json")
                        excl_list = json.loads(excl_bytes.decode("utf-8"))
                        if not isinstance(excl_list, list):
                            errors.append("EXCLUSIONS.json must be a JSON array")
                        else:
                            for ex in excl_list:
                                ex_path = ex.get("path", "")
                                safe_ex, ex_reason = is_safe_relative_path(ex_path)
                                if not safe_ex:
                                    errors.append(f"Unsafe path in EXCLUSIONS.json: {ex_path} ({ex_reason})")
                    except Exception as e:
                        errors.append(f"Malformed EXCLUSIONS.json: {e}")

        except BadZipFile:
            return {
                "status": "INVALID",
                "errors": [f"Corrupted or invalid ZIP file: {zip_path}"],
                "manifest": None
            }
        except Exception as e:
            return {
                "status": "INVALID",
                "errors": [f"Unexpected error inspecting archive: {str(e)}"],
                "manifest": None
            }

        if errors:
            return {"status": "INVALID", "errors": errors, "manifest": manifest.to_dict() if manifest else None}

        return {
            "status": "VALID",
            "errors": [],
            "manifest": manifest.to_dict(),
            "entries_count": len(manifest.entries),
            "payload_files_count": len([e for e in manifest.entries if e.payload_path]),
            "mode": manifest.package_mode
        }
```

### `PackageVerifier.verify_package` — `Lines 144–432`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `144` إلى السطر `432` (`Lines 144–432`)
- **الوظيفة:** Verify the integrity, safety, and content authenticity of an update ZIP.
- **الكود الفعلي (`Lines 144–432`):**
```python
    def verify_package(
        zip_path: Path,
        expected_base_inventory: Any = None,
        workspace_root: Optional[Path] = None
    ) -> Dict[str, Any]:
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED
        """Verify the integrity, safety, and content authenticity of an update ZIP."""
        zip_path = zip_path.resolve()
        if not zip_path.exists():
            return {
                "status": "INVALID",
                "errors": [f"Archive file not found: {zip_path}"],
                "manifest": None
            }

        errors: List[str] = []
        manifest: Any = None
        try:
            with ZipFile(zip_path, "r") as zf:
                names = zf.namelist()

                # 1. Audit archive entry name safety and boundary
                for name in names:
                    safe, reason = is_safe_relative_path(name)
                    if not safe:
                        errors.append(f"Unsafe archive entry path: {name} ({reason})")
                    elif name not in ALLOWED_ROOT_FILES and not name.startswith("payload/"):
                        errors.append(f"Unexpected archive entry outside root controls or payload/: {name}")

                if errors:
                    return {"status": "INVALID", "errors": errors, "manifest": None}

                # 2. Check manifest existence
                if "UPDATE_MANIFEST.json" not in names:
                    return {
                        "status": "INVALID",
                        "errors": ["Missing UPDATE_MANIFEST.json at root of archive"],
                        "manifest": None
                    }

                # 3. Read and parse manifest
                try:
                    manifest_bytes = zf.read("UPDATE_MANIFEST.json")
                    manifest_data = json.loads(manifest_bytes.decode("utf-8"))
                    manifest = UpdateManifest.from_dict(manifest_data)
                except Exception as e:
                    return {
                        "status": "INVALID",
                        "errors": [f"Malformed UPDATE_MANIFEST.json: {str(e)}"],
                        "manifest": None
                    }

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED | Author: orchestrator-planner
                # 3.1 Validate base_snapshot_hash against trusted baseline serialization if resolvable
                base_to_verify = expected_base_inventory
                if not base_to_verify and manifest.base_snapshot_id:
                    # Search for baseline in registry relative to workspace_root, archive dir, or cwd
                    search_dirs = []
                    if workspace_root:
                        search_dirs.append(workspace_root.resolve())
                    search_dirs.append(zip_path.parent.resolve())
                    search_dirs.append(Path.cwd().resolve())
                    for sd in search_dirs:
                        candidate_base_file = sd / "tools" / "update_packages" / "registry" / "baselines" / f"{manifest.base_snapshot_id}.json"
                        if candidate_base_file.exists():
                            try:
                                candidate_data = json.loads(candidate_base_file.read_text(encoding="utf-8"))
                                base_to_verify = BaselineInventory.from_dict(candidate_data)
                                break
                            except Exception:
                                pass

                if base_to_verify:
                    expected_base_hash = compute_bytes_sha256(base_to_verify.to_json().encode("utf-8"))
                    if manifest.base_snapshot_hash and manifest.base_snapshot_hash.lower() != expected_base_hash.lower():
                        errors.append(
                            f"Tampered or mismatched base_snapshot_hash: manifest declares '{manifest.base_snapshot_hash}', "
                            f"expected '{expected_base_hash}' from trusted baseline '{base_to_verify.baseline_id}'."
                        )
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED

                # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED | Author: orchestrator-planner
                # 3.2 Validate TARGET_INVENTORY.json and target_snapshot_hash
                is_complete_mode = getattr(manifest, "package_mode", "").upper() == "COMPLETE"
                if is_complete_mode and "TARGET_INVENTORY.json" not in names:
                    errors.append("COMPLETE mode package requires TARGET_INVENTORY.json at archive root, but it is missing.")

                if "TARGET_INVENTORY.json" in names:
                    try:
                        target_inv_bytes = zf.read("TARGET_INVENTORY.json")
                        actual_target_hash = compute_bytes_sha256(target_inv_bytes)

                        # Validate target_snapshot_hash against raw archive file
                        if manifest.target_snapshot_hash and manifest.target_snapshot_hash.lower() != actual_target_hash.lower():
                            errors.append(
                                f"Tampered or mismatched target_snapshot_hash: manifest declares '{manifest.target_snapshot_hash}', "
                                f"but declared TARGET_INVENTORY.json serialization hash is '{actual_target_hash}'."
                            )

                        # Validate schema and canonical serialization
                        target_inv_data = json.loads(target_inv_bytes.decode("utf-8"))
                        target_inv_obj = BaselineInventory.from_dict(target_inv_data)
                        canonical_target_bytes = target_inv_obj.to_json().encode("utf-8")
                        canonical_target_hash = compute_bytes_sha256(canonical_target_bytes)
                        if canonical_target_hash.lower() != actual_target_hash.lower():
                            errors.append(
                                f"TARGET_INVENTORY.json is not in canonical serialization format: "
                                f"file hash is '{actual_target_hash}', canonical serialization hash is '{canonical_target_hash}'."
                            )

                        t_files = target_inv_obj.files

                        # Derive expected complete target inventory from baseline + manifest operations
                        if base_to_verify:
                            derived_files: Dict[str, Tuple[str, int, bool]] = {
                                p: (rec.sha256, rec.size_bytes, rec.is_binary)
                                for p, rec in base_to_verify.files.items()
                            }
                            for entry in manifest.entries:
                                if entry.operation in ("ADD", "MODIFY"):
                                    derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes, entry.is_binary)
                                elif entry.operation == "DELETE":
                                    derived_files.pop(entry.path, None)
                                elif entry.operation == "RENAME":
                                    if entry.renamed_from:
                                        derived_files.pop(entry.renamed_from, None)
                                    derived_files[entry.path] = (entry.new_sha256 or "", entry.size_bytes, entry.is_binary)

                            # Check for missing files in TARGET_INVENTORY.json
                            missing_in_target = set(derived_files.keys()) - set(t_files.keys())
                            if missing_in_target:
                                errors.append(
                                    f"TARGET_INVENTORY.json is missing {len(missing_in_target)} files derived from baseline and manifest operations: {sorted(missing_in_target)[:5]}"
                                )

                            # Check for unexpected extra files in TARGET_INVENTORY.json
                            extra_in_target = set(t_files.keys()) - set(derived_files.keys())
                            if extra_in_target:
                                errors.append(
                                    f"TARGET_INVENTORY.json contains {len(extra_in_target)} unexpected extra files not derived from baseline and manifest: {sorted(extra_in_target)[:5]}"
                                )

                            # Check hash and size for every derived file (including unchanged files)
                            for p, (exp_sha, exp_size, exp_bin) in derived_files.items():
                                t_rec = t_files.get(p)
                                if t_rec:
                                    if t_rec.sha256.lower() != exp_sha.lower():
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry for '{p}' contradicts derived target state: "
                                            f"expected sha256 '{exp_sha}', declared '{t_rec.sha256}'."
                                        )
                                    if t_rec.size_bytes != exp_size:
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry for '{p}' size mismatch: "
                                            f"expected {exp_size} bytes, declared {t_rec.size_bytes} bytes."
                                        )
                        elif is_complete_mode and manifest.base_snapshot_id not in ("EMPTY_REPO", "BOOTSTRAP_EMPTY", None):
                            # In COMPLETE mode with a required non-empty baseline that cannot be resolved
                            if expected_base_inventory is not None or workspace_root is not None:
                                errors.append(
                                    f"COMPLETE mode package requires verifiable baseline '{manifest.base_snapshot_id}' to validate target inventory consistency, but baseline could not be resolved."
                                )
                        else:
                            # Baseline is empty/null or not provided in non-complete mode; verify manifest entries
                            for entry in manifest.entries:
                                if entry.operation in ("ADD", "MODIFY"):
                                    t_rec = t_files.get(entry.path)
                                    if not t_rec or t_rec.sha256.lower() != (entry.new_sha256 or "").lower():
                                        errors.append(
                                            f"TARGET_INVENTORY.json entry inconsistent with manifest for '{entry.path}'"
                                        )
                                elif entry.operation == "DELETE":
                                    if entry.path in t_files:
                                        errors.append(
                                            f"TARGET_INVENTORY.json contains file '{entry.path}' declared as DELETE in manifest"
                                        )
                    except Exception as e:
                        errors.append(f"Failed to inspect TARGET_INVENTORY.json: {e}")
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | EDITED

                # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
                # Enforce complete mode integrity: COMPLETE packages must have zero exclusions
                if getattr(manifest, "package_mode", "").upper() == "COMPLETE" and manifest.exclusions_count > 0:
                    errors.append(
                        f"COMPLETE package declares {manifest.exclusions_count} exclusions; COMPLETE mode updates must have zero required content exclusions."
                    )
                # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

                # 4. Strictly audit manifest entry paths against traversal and collisions
                seen_target_paths: Set[str] = set()
                declared_payload_paths: Set[str] = set()
                sha_hex_pattern = re.compile(r"^[0-9a-f]{64}$")

                for entry in manifest.entries:
                    # Validate entry.path
                    safe, reason = is_safe_relative_path(entry.path)
                    if not safe:
                        errors.append(f"Unsafe target path in manifest entry: {entry.path} ({reason})")

                    if entry.path in seen_target_paths:
                        errors.append(f"Duplicate target path declared in manifest: {entry.path}")
                    seen_target_paths.add(entry.path)

                    # Validate payload_path if present
                    if entry.payload_path:
                        safe_pay, pay_reason = is_safe_relative_path(entry.payload_path)
                        if not safe_pay:
                            errors.append(f"Unsafe payload_path in manifest entry for {entry.path}: {entry.payload_path} ({pay_reason})")
                        elif not entry.payload_path.startswith("payload/"):
                            errors.append(f"Payload path does not start with payload/: {entry.payload_path}")
                        declared_payload_paths.add(entry.payload_path)

                    # Validate renamed_from if present
                    if entry.renamed_from:
                        safe_ren, ren_reason = is_safe_relative_path(entry.renamed_from)
                        if not safe_ren:
                            errors.append(f"Unsafe renamed_from path in manifest entry: {entry.renamed_from} ({ren_reason})")

                    # Validate hash formats
                    if entry.new_sha256 and not sha_hex_pattern.match(entry.new_sha256):
                        errors.append(f"Invalid new_sha256 format for {entry.path}: {entry.new_sha256}")
                    if entry.previous_sha256 and not sha_hex_pattern.match(entry.previous_sha256):
                        errors.append(f"Invalid previous_sha256 format for {entry.path}: {entry.previous_sha256}")

                    # Validate payload content and byte hash against manifest
                    if entry.payload_path:
                        if entry.payload_path not in names:
                            errors.append(f"Payload file missing in archive: {entry.payload_path}")
                            continue

                        payload_bytes = zf.read(entry.payload_path)
                        payload_sha = compute_bytes_sha256(payload_bytes)

                        if payload_sha != entry.new_sha256:
                            errors.append(
                                f"Corrupted payload for {entry.path}: expected {entry.new_sha256}, got {payload_sha}"
                            )
                        if len(payload_bytes) != entry.size_bytes:
                            errors.append(
                                f"Byte size mismatch for {entry.path}: expected {entry.size_bytes}, got {len(payload_bytes)}"
                            )

                # 5. Check for undeclared payload files in ZIP
                actual_payload_files = {name for name in names if name.startswith("payload/")}
                undeclared_payloads = actual_payload_files - declared_payload_paths
                if undeclared_payloads:
                    for up in sorted(undeclared_payloads):
                        errors.append(f"Undeclared payload file found in archive: {up}")

                # 6. Validate auxiliary EXCLUSIONS.json if present
                if "EXCLUSIONS.json" in names:
                    try:
                        excl_bytes = zf.read("EXCLUSIONS.json")
                        excl_list = json.loads(excl_bytes.decode("utf-8"))
                        if not isinstance(excl_list, list):
                            errors.append("EXCLUSIONS.json must be a JSON array")
                        else:
                            for ex in excl_list:
                                ex_path = ex.get("path", "")
                                safe_ex, ex_reason = is_safe_relative_path(ex_path)
                                if not safe_ex:
                                    errors.append(f"Unsafe path in EXCLUSIONS.json: {ex_path} ({ex_reason})")
                    except Exception as e:
                        errors.append(f"Malformed EXCLUSIONS.json: {e}")

        except BadZipFile:
            return {
                "status": "INVALID",
                "errors": [f"Corrupted or invalid ZIP file: {zip_path}"],
                "manifest": None
            }
        except Exception as e:
            return {
                "status": "INVALID",
                "errors": [f"Unexpected error inspecting archive: {str(e)}"],
                "manifest": None
            }

        if errors:
            return {"status": "INVALID", "errors": errors, "manifest": manifest.to_dict() if manifest else None}

        return {
            "status": "VALID",
            "errors": [],
            "manifest": manifest.to_dict(),
            "entries_count": len(manifest.entries),
            "payload_files_count": len([e for e in manifest.entries if e.payload_path]),
            "mode": manifest.package_mode
        }
```
