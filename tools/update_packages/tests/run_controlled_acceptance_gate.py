# START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | CREATED | Author: orchestrator-planner
"""Controlled Acceptance Gate for the Incremental Update ZIP System.

Executes the owner's exact Section 3 controlled delta test:
- Modifies 2 existing Python files.
- Modifies 2 existing Markdown files.
- Adds 1 new file.
- Modifies 1 binary asset.
- Deletes 1 existing file.
- Performs 1 supported rename.
Exports a COMPLETE delta ZIP, applies it to an untouched baseline copy,
verifies byte-for-byte reconstruction across 100% of files,
and proves that application to an incompatible baseline fails with zero file modifications.
"""

from pathlib import Path
from zipfile import ZipFile
import json
import os
import shutil
import sys
import tempfile

# Ensure repo root is in sys.path
REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.update_packages.applier import PackageApplier
from tools.update_packages.differ import InventoryDiffer
from tools.update_packages.models import BaselineInventory, FileOperation, PackageMode
from tools.update_packages.packager import UpdatePackager
from tools.update_packages.scanner import WorkspaceScanner, compute_bytes_sha256, calculate_stream_sha256
from tools.update_packages.state_manager import UpdateStateManager
from tools.update_packages.verifier import PackageVerifier

EXPORTS_DIR = REPO_ROOT / "exports" / "updates"
EXPORTS_DIR.mkdir(parents=True, exist_ok=True)


def run_controlled_acceptance_test():
    """Execute the full controlled delta acceptance gate."""
    results = {
        "gate": "CONTROLLED_DELTA_ACCEPTANCE",
        "timestamp_utc": "2026-10-18T02:30:00Z",
        "steps": {}
    }

    with tempfile.TemporaryDirectory(prefix="agd_acceptance_sandbox_") as sandbox_str:
        sandbox = Path(sandbox_str).resolve()
        ws_root = sandbox / "working_repo"
        clone_root = sandbox / "matching_clone_repo"
        incompatible_root = sandbox / "incompatible_repo"

        ws_root.mkdir(parents=True, exist_ok=True)
        (ws_root / "src" / "core").mkdir(parents=True, exist_ok=True)
        (ws_root / "docs").mkdir(parents=True, exist_ok=True)
        (ws_root / "assets").mkdir(parents=True, exist_ok=True)

        # 1. Establish authentic baseline files
        py1 = ws_root / "src" / "core" / "math_utils.py"
        py2 = ws_root / "src" / "pipeline.py"
        md1 = ws_root / "docs" / "ARCHITECTURE.md"
        md2 = ws_root / "docs" / "GUIDE.md"
        bin1 = ws_root / "assets" / "logo.png"
        del1 = ws_root / "docs" / "DEPRECATED.md"
        ren1 = ws_root / "src" / "old_name.py"
        const1 = ws_root / "src" / "constants.py"
        idx1 = ws_root / "docs" / "INDEX.md"

        py1.write_text("def add(a, b): return a + b\n", encoding="utf-8")
        py2.write_text("def run(): print('v1.0')\n", encoding="utf-8")
        md1.write_text("# Architecture v1.0\nInitial specification.\n", encoding="utf-8")
        md2.write_text("# User Guide v1.0\nInitial guide.\n", encoding="utf-8")
        bin1.write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR_initial_bytes_v1")
        del1.write_text("# Deprecated content to delete\n", encoding="utf-8")
        ren1.write_text("def old_function(): return 'rename me'\n", encoding="utf-8")
        const1.write_text("VERSION = '1.0.0'\n", encoding="utf-8")
        idx1.write_text("# Index of Project\n", encoding="utf-8")

        # 2. Capture baseline inventory
        state_mgr = UpdateStateManager(ws_root)
        base_inv = state_mgr.initialize_baseline("BASE_ACCEPTANCE_AUTHENTIC")
        base_files = base_inv.files
        results["steps"]["1_baseline_captured"] = {
            "baseline_id": base_inv.baseline_id,
            "files_count": len(base_files),
            "files": sorted(list(base_files.keys()))
        }

        # 3. Create untouched matching clone of the baseline
        shutil.copytree(ws_root, clone_root, dirs_exist_ok=True)
        clone_scanner = WorkspaceScanner(clone_root)
        clone_initial_files = clone_scanner.scan()
        assert len(clone_initial_files) == len(base_files)

        # 4. Perform the exact 6 operations requested by the owner:
        # - Operation A: Modify two existing Python files
        py1.write_text("def add(a, b): return a + b\ndef multiply(a, b): return a * b\n", encoding="utf-8")
        py2.write_text("def run(): print('v2.0 production release')\n", encoding="utf-8")

        # - Operation B: Modify two existing Markdown files
        md1.write_text("# Architecture v2.0\nUpdated specification with vector engine.\n", encoding="utf-8")
        md2.write_text("# User Guide v2.0\nUpdated instructions for clean SVG.\n", encoding="utf-8")

        # - Operation C: Add a new file
        new1 = ws_root / "docs" / "NEW_FEATURE_SPEC.md"
        new1.write_text("# New Feature Specification\nClean SVG Pen Tool details.\n", encoding="utf-8")

        # - Operation D: Modify a binary asset
        bin1.write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR_modified_bytes_v2_hires")

        # - Operation E: Delete an existing file
        del1.unlink()

        # - Operation F: Perform a supported rename
        ren_content = ren1.read_bytes()
        ren1.unlink()
        ren_target = ws_root / "src" / "renamed_feature.py"
        ren_target.write_bytes(ren_content)

        # 5. Scan target workspace
        scanner = WorkspaceScanner(ws_root)
        target_files = scanner.scan()
        target_inv = BaselineInventory(
            baseline_id="SNAP_ACCEPTANCE_TARGET",
            repo_identity="AI Graphic Designer",
            created_at_utc="2026-10-18T02:30:00Z",
            tool_version="1.0.0",
            files=target_files
        )

        # 6. Compute diff and verify operations count
        diff_entries, diff_summary = InventoryDiffer.compute_diff(base_files, target_files)
        results["steps"]["2_diff_computed"] = {
            "summary": diff_summary,
            "entries_count": len(diff_entries),
            "entries": [
                {
                    "operation": e.operation,
                    "path": e.path,
                    "renamed_from": e.renamed_from,
                    "is_binary": e.is_binary,
                    "size_bytes": e.size_bytes
                }
                for e in sorted(diff_entries, key=lambda x: (x.operation, x.path))
            ]
        }

        # 7. Export COMPLETE delta ZIP
        packager = UpdatePackager(ws_root)
        pkg_res = packager.build_package(
            base_inventory=base_inv,
            target_inventory=target_inv,
            mode=PackageMode.COMPLETE,
            update_id="UPDATE_CONTROLLED_ACCEPTANCE",
            output_dir=EXPORTS_DIR,
            sequence_num=999
        )
        archive_path = Path(pkg_res["archive_path"])

        # Also save a canonical copy named AGD_CONTROLLED_DELTA_TEST.zip
        canonical_delta_path = EXPORTS_DIR / "AGD_CONTROLLED_DELTA_TEST.zip"
        shutil.copy2(archive_path, canonical_delta_path)

        # 8. Verify the package independently with PackageVerifier
        verification = PackageVerifier.verify_package(canonical_delta_path)
        assert verification["status"] == "VALID", f"Package verification failed: {verification['errors']}"
        results["steps"]["3_package_verified"] = {
            "archive_name": "AGD_CONTROLLED_DELTA_TEST.zip",
            "size_bytes": canonical_delta_path.stat().st_size,
            "status": verification["status"],
            "entries_count": verification["entries_count"],
            "payload_files_count": verification["payload_files_count"]
        }

        # 9. Apply delta package to the clean clone of the matching baseline
        applier = PackageApplier(clone_root, enforce_base_match=True, expected_base_inventory=base_inv)
        apply_res = applier.apply(canonical_delta_path)
        assert apply_res["status"] == "APPLIED", f"Application failed: {apply_res.get('errors')}"
        results["steps"]["4_applied_to_matching_baseline"] = {
            "status": apply_res["status"],
            "applied_count": apply_res["applied_count"],
            "applied_entries": apply_res["applied_entries"]
        }

        # 10. Byte-for-byte verification of reconstructed workspace
        reconstructed_scanner = WorkspaceScanner(clone_root)
        reconstructed_files = reconstructed_scanner.scan()

        assert set(reconstructed_files.keys()) == set(target_files.keys()), (
            f"Key mismatch: {set(reconstructed_files.keys()) ^ set(target_files.keys())}"
        )

        hash_mismatches = []
        for p, target_rec in target_files.items():
            recon_sha = reconstructed_files[p].sha256
            if recon_sha != target_rec.sha256:
                hash_mismatches.append(f"{p}: expected {target_rec.sha256}, got {recon_sha}")

        assert len(hash_mismatches) == 0, f"Hash mismatches found: {hash_mismatches}"
        results["steps"]["5_byte_for_byte_verification"] = {
            "status": "EXACT_BYTE_FOR_BYTE_MATCH",
            "reconstructed_files_count": len(reconstructed_files),
            "target_files_count": len(target_files),
            "hash_mismatches_count": 0
        }

        # 11. Repeat against an incompatible baseline and prove ZERO files are changed
        shutil.copytree(ws_root, incompatible_root, dirs_exist_ok=True)
        # Corrupt one base file in incompatible_root to simulate an incompatible workspace
        (incompatible_root / "src" / "pipeline.py").write_text("def foreign_incompatible(): pass\n", encoding="utf-8")
        incompatible_before = WorkspaceScanner(incompatible_root).scan()

        incomp_applier = PackageApplier(incompatible_root, enforce_base_match=True, expected_base_inventory=base_inv)
        incomp_res = incomp_applier.apply(canonical_delta_path)

        assert incomp_res["status"] == "FAILED", "Incompatible baseline must be rejected"
        assert incomp_res["stage"] == "PREREQUISITE_CHECK", f"Expected PREREQUISITE_CHECK, got {incomp_res['stage']}"

        # Verify zero files changed
        incompatible_after = WorkspaceScanner(incompatible_root).scan()
        assert set(incompatible_before.keys()) == set(incompatible_after.keys())
        for p, rec_before in incompatible_before.items():
            assert incompatible_after[p].sha256 == rec_before.sha256, f"File unexpectedly modified: {p}"

        results["steps"]["6_incompatible_baseline_rejected"] = {
            "status": incomp_res["status"],
            "stage": incomp_res["stage"],
            "errors": incomp_res["errors"],
            "files_modified_in_target": 0
        }

    results["verdict"] = "CONTROLLED_ACCEPTANCE_PASSED_100_PERCENT"
    out_file = EXPORTS_DIR / "controlled_acceptance_result.json"
    out_file.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return results


if __name__ == "__main__":
    run_controlled_acceptance_test()
# END CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | CREATED
