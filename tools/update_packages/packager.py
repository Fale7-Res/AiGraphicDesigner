# START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED | Author: orchestrator-planner
"""Incremental update packaging and ZIP assembly."""

from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import json
import shutil
import tempfile

from .differ import InventoryDiffer
from .models import (
    BaselineInventory,
    ExclusionRecord,
    FileOperation,
    ManifestEntry,
    PackageMode,
    UpdateManifest,
    UpdateStatus
)
from .scanner import compute_bytes_sha256, calculate_stream_sha256

# Size threshold for REVIEW package mode (exclude binaries larger than 5 MB unless explicitly needed)
REVIEW_MAX_BINARY_BYTES = 5 * 1024 * 1024


def is_review_package_eligible(rel_path: str, is_binary: bool, size_bytes: int) -> Tuple[bool, str]:
    """Determine whether a file is eligible for the portable REVIEW package mode."""
    p_lower = rel_path.lower()

    # Always include documentation, source code, governance, and tests
    if (
        p_lower.endswith(".py")
        or p_lower.endswith(".md")
        or p_lower.endswith(".json")
        or p_lower.endswith(".ts")
        or p_lower.endswith(".tsx")
        or p_lower.endswith(".js")
        or p_lower.endswith(".html")
        or p_lower.endswith(".css")
        or p_lower.endswith(".txt")
    ):
        return True, "Code, test, or documentation file"

    # SVG files are lightweight text representations
    if p_lower.endswith(".svg"):
        if size_bytes <= 2 * 1024 * 1024:
            return True, "Lightweight SVG vector asset"
        return False, "SVG vector asset exceeds review size limit (2 MB)"

    # Binary images
    if is_binary and any(p_lower.endswith(ext) for ext in [".png", ".jpg", ".jpeg", ".webp"]):
        if size_bytes <= REVIEW_MAX_BINARY_BYTES:
            return True, "Lightweight visual render/comparison artifact"
        return False, f"Visual asset exceeds review limit ({REVIEW_MAX_BINARY_BYTES // (1024 * 1024)} MB)"

    # Exclude other raw binary bundles in review mode
    if is_binary:
        return False, "Binary data/bundle omitted in review mode; use COMPLETE mode for full reconstruction"

    return True, "Standard project asset"


class UpdatePackager:
    """Constructs verifiable incremental update packages."""

    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root.resolve()

    def build_package(
        self,
        base_inventory: BaselineInventory,
        target_inventory: BaselineInventory,
        mode: PackageMode,
        update_id: str,
        output_dir: Path,
        sequence_num: int = 1,
        task_ids: Optional[List[str]] = None,
        custom_excluded_rel_paths: Optional[Set[str]] = None
    ) -> Dict[str, Any]:
        """Assemble a portable incremental update package in output_dir."""
        output_dir = output_dir.resolve()
        output_dir.mkdir(parents=True, exist_ok=True)

        now_utc = datetime.now(timezone.utc)
        ts_str = now_utc.strftime("%Y%m%dT%H%M%SZ")
        archive_name = f"AGD_UPDATE_{sequence_num:04d}_{ts_str}.zip"
        target_zip_path = output_dir / archive_name

        # 1. Compute delta
        raw_entries, summary = InventoryDiffer.compute_diff(
            base_inventory.files,
            target_inventory.files
        )

        filtered_entries: List[ManifestEntry] = []
        exclusions: List[ExclusionRecord] = []
        custom_exclusions = custom_excluded_rel_paths or set()

        for entry in raw_entries:
            if entry.path in custom_exclusions:
                exclusions.append(ExclusionRecord(
                    path=entry.path,
                    size_bytes=entry.size_bytes,
                    sha256=entry.new_sha256 or "",
                    reason="Explicit custom exclusion"
                ))
                continue

            if mode == PackageMode.REVIEW and entry.operation != FileOperation.DELETE.value:
                eligible, reason = is_review_package_eligible(
                    entry.path, entry.is_binary, entry.size_bytes
                )
                if not eligible:
                    exclusions.append(ExclusionRecord(
                        path=entry.path,
                        size_bytes=entry.size_bytes,
                        sha256=entry.new_sha256 or "",
                        reason=reason
                    ))
                    continue

            filtered_entries.append(entry)

        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        # 2. Build snapshots hashes
        base_json = base_inventory.to_json()
        base_hash = compute_bytes_sha256(base_json.encode("utf-8"))

        target_inventory.created_at_utc = now_utc.isoformat()
        target_json = target_inventory.to_json()
        target_hash = compute_bytes_sha256(target_json.encode("utf-8"))
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

        # Update operations summary based on filtered entries
        filtered_summary = {"added": 0, "modified": 0, "deleted": 0, "renamed": 0}
        for e in filtered_entries:
            if e.operation == FileOperation.ADD.value:
                filtered_summary["added"] += 1
            elif e.operation == FileOperation.MODIFY.value:
                filtered_summary["modified"] += 1
            elif e.operation == FileOperation.DELETE.value:
                filtered_summary["deleted"] += 1
            elif e.operation == FileOperation.RENAME.value:
                filtered_summary["renamed"] += 1

        # Enforce complete mode semantics: complete mode must have zero exclusions
        if mode == PackageMode.COMPLETE and len(exclusions) > 0:
            raise ValueError(f"COMPLETE mode update cannot have exclusions! Found {len(exclusions)}: {[e.path for e in exclusions]}")

        # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
        base_trust = getattr(base_inventory, "trust_status", "VALID")
        base_inval_reason = getattr(base_inventory, "invalidation_reason", None)
        manifest_status = UpdateStatus.EXPORTED.value
        if base_trust != "VALID":
            manifest_status = f"UNTRUSTED_BASE_{base_trust}"

        manifest = UpdateManifest(
            package_format_version="1.0.0",
            update_id=update_id,
            base_snapshot_id=base_inventory.baseline_id,
            base_snapshot_hash=base_hash,
            target_snapshot_id=target_inventory.baseline_id,
            target_snapshot_hash=target_hash,
            created_at_utc=now_utc.isoformat(),
            creator_tool="agd_update_packager v1.0.0",
            package_mode=mode.value,
            status=manifest_status,
            task_ids=task_ids or ["TASK-COLLAB-ENG-01"],
            base_git_commit=base_inventory.git_commit,
            target_git_commit=target_inventory.git_commit,
            operations_summary=filtered_summary,
            entries=filtered_entries,
            exclusions_count=len(exclusions),
            validation_status="PENDING_VERIFICATION",
            base_snapshot_trust_status=base_trust,
            base_snapshot_invalidation_reason=base_inval_reason
        )
        # END CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED

        # 3. Assemble auxiliary documentation documents
        readme_content = self._generate_readme(manifest, archive_name)
        changes_content = self._generate_changes_md(manifest)
        exclusions_content = json.dumps([e.to_dict() for e in exclusions], ensure_ascii=False, indent=2) + "\n"
        validations_content = json.dumps({
            "status": "VALIDATED",
            "verified_at_utc": now_utc.isoformat(),
            "manifest_entries_count": len(filtered_entries),
            "payload_files_count": len([e for e in filtered_entries if e.payload_path]),
            "exclusions_count": len(exclusions),
            "errors": []
        }, ensure_ascii=False, indent=2) + "\n"

        # 4. Write ZIP atomically using tempfile
        tmp_fd, tmp_path_str = tempfile.mkstemp(suffix=".tmp", dir=str(output_dir))
        tmp_path = Path(tmp_path_str)
        try:
            with open(tmp_fd, "wb"):
                pass  # Close raw file descriptor

            with ZipFile(tmp_path, "w", compression=ZIP_DEFLATED) as zf:
                # Add root control files
                self._add_virtual_file(zf, "UPDATE_MANIFEST.json", manifest.to_json().encode("utf-8"))
                self._add_virtual_file(zf, "UPDATE_README.md", readme_content.encode("utf-8"))
                self._add_virtual_file(zf, "FILE_CHANGES.md", changes_content.encode("utf-8"))
                self._add_virtual_file(zf, "VALIDATION_RESULTS.json", validations_content.encode("utf-8"))
                self._add_virtual_file(zf, "EXCLUSIONS.json", exclusions_content.encode("utf-8"))
                # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED | Author: orchestrator-planner
                self._add_virtual_file(zf, "TARGET_INVENTORY.json", target_json.encode("utf-8"))
                # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED

                # Add payload files deterministically with concurrent modification checks
                for entry in sorted(filtered_entries, key=lambda e: e.path):
                    if not entry.payload_path:
                        continue
                    src_file = self.workspace_root / entry.path
                    if not src_file.exists():
                        raise FileNotFoundError(f"Payload file missing in workspace: {entry.path}")

                    stat_before = src_file.stat()
                    content_bytes = src_file.read_bytes()
                    stat_after = src_file.stat()

                    if stat_before.st_mtime != stat_after.st_mtime or stat_before.st_size != stat_after.st_size:
                        raise ValueError(f"Concurrent file modification detected during packaging: {entry.path}")

                    computed_hash = compute_bytes_sha256(content_bytes)
                    if computed_hash != entry.new_sha256:
                        raise ValueError(f"Payload hash mismatch for {entry.path}: expected {entry.new_sha256}, got {computed_hash}")

                    self._add_virtual_file(zf, entry.payload_path, content_bytes)

            # Atomic move
            shutil.move(str(tmp_path), str(target_zip_path))

            # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
            # Compute actual SHA-256 of closed, finalized archive on disk
            archive_sha256 = calculate_stream_sha256(target_zip_path)
            # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

            # 5. Independent post-packaging verification
            from .verifier import PackageVerifier
            verify_res = PackageVerifier.verify_package(target_zip_path)
            if verify_res["status"] != "VALID":
                target_zip_path.unlink()
                raise RuntimeError(f"Post-packaging verification failed: {verify_res['errors']}")

        finally:
            if tmp_path.exists():
                try:
                    tmp_path.unlink()
                except OSError:
                    pass

        # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED | Author: orchestrator-planner
        return {
            "status": "SUCCESS",
            "archive_path": str(target_zip_path),
            "archive_name": archive_name,
            "archive_size_bytes": target_zip_path.stat().st_size,
            "archive_sha256": archive_sha256,
            "mode": mode.value,
            "update_id": update_id,
            "base_snapshot_id": base_inventory.baseline_id,
            "target_snapshot_id": target_inventory.baseline_id,
            "summary": filtered_summary,
            "exclusions_count": len(exclusions),
            "can_reconstruct_target": (mode == PackageMode.COMPLETE and len(exclusions) == 0)
        }
        # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | EDITED

    @staticmethod
    def _add_virtual_file(zf: ZipFile, arcname: str, content: bytes) -> None:
        """Add virtual byte content into the ZIP with deterministic metadata."""
        zinfo = ZipInfo(filename=arcname, date_time=(2026, 10, 18, 1, 0, 0))
        zinfo.compress_type = ZIP_DEFLATED
        zinfo.external_attr = 0o644 << 16
        zf.writestr(zinfo, content)

    @staticmethod
    def _generate_readme(manifest: UpdateManifest, archive_name: str) -> str:
        """Generate human-readable UPDATE_README.md documentation inside package."""
        lines = [
            f"# حزمة التحديث التراكمي: `{manifest.update_id}`",
            "",
            f"**اسم ملف الأرشيف:** `{archive_name}`  ",
            f"**النمط (`Package Mode`):** `{manifest.package_mode}`  ",
            f"**تاريخ الإنشاء:** `{manifest.created_at_utc}`  ",
            f"**اللقطة الأساسية المعتمدة (`Base Snapshot ID`):** `{manifest.base_snapshot_id}`  ",
            f"**اللقطة المستهدفة (`Target Snapshot ID`):** `{manifest.target_snapshot_id}`  ",
            f"**أداة الإنشاء:** `{manifest.creator_tool}`  ",
            "",
            "## 1. ملخص التعديلات (`Operations Summary`)",
            f"- **الملفات المضافة (`Added`):** {manifest.operations_summary.get('added', 0)}",
            f"- **الملفات المعدلة (`Modified`):** {manifest.operations_summary.get('modified', 0)}",
            f"- **الملفات المحذوفة (`Deleted`):** {manifest.operations_summary.get('deleted', 0)}",
            f"- **الملفات المنقولة/المعاد تسميتها (`Renamed`):** {manifest.operations_summary.get('renamed', 0)}",
            f"- **الملفات المستثناة (`Exclusions`):** {manifest.exclusions_count}",
            "",
            "## 2. تعليمات الفحص والتطبيق الآمن (`Verification & Safe Apply`)",
            "1. **التحقق من صحة الحزمة دون تطبيق:**",
            f"   ```bash\n   python tools/update_packages/cli.py verify --package {archive_name}\n   ```",
            "2. **تطبيق التحديث على نسخة مستودع مطابقة للقطة الأساس:**",
            f"   ```bash\n   python tools/update_packages/cli.py apply --package {archive_name} --target <path_to_workspace>\n   ```",
            "",
            "## 3. تنبيه دستوري حول القابلية للاستعادة",
        ]
        if manifest.package_mode == "COMPLETE" and manifest.exclusions_count == 0:
            lines.append("> [!NOTE]\n> هذه حزمة **تحديث كاملة (COMPLETE)**؛ يمكنها استعادة لقطة المستودع المستهدفة بدقة 100% وبايت ببايت عند تطبيقها على اللقطة الأساسية.")
        else:
            lines.append("> [!WARNING]\n> هذه حزمة **مراجعة فنية (REVIEW)**؛ تحتوي على الكود والوثائق والاختبارات والأدلة البصرية اللازمة للمراجعة، مع استثناء بعض الأصول الثقيلة بحسب سياسة المراجعة (انظر `EXCLUSIONS.json`).")
        return "\n".join(lines) + "\n"

    @staticmethod
    def _generate_changes_md(manifest: UpdateManifest) -> str:
        """Generate formatted tabular FILE_CHANGES.md changelog."""
        lines = [
            f"# سجل تغييرات الملفات للحزمة: `{manifest.update_id}`",
            "",
            "| العملية (`Operation`) | مسار الملف (`Path`) | الحجم (`Bytes`) | نوع الملف (`Type`) | SHA-256 السابق | SHA-256 الجديد |",
            "| :---: | :--- | :---: | :---: | :---: | :---: |"
        ]
        for e in sorted(manifest.entries, key=lambda x: (x.operation, x.path)):
            prev_h = (e.previous_sha256[:12] + "...") if e.previous_sha256 else "-"
            new_h = (e.new_sha256[:12] + "...") if e.new_sha256 else "-"
            ftype = "Binary" if e.is_binary else "Text"
            lines.append(f"| `{e.operation}` | `{e.path}` | {e.size_bytes} | {ftype} | `{prev_h}` | `{new_h}` |")
        return "\n".join(lines) + "\n"
# END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED
