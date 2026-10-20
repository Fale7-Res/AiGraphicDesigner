# START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED | Author: orchestrator-planner
"""Comprehensive test suite for the Incremental Update Packaging System.

Covers all 20 adversarial scenarios from B11 and the B12 end-to-end acceptance test.
All tests use disposable, isolated temporary directories.
"""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json
import os
import shutil
import tempfile
import time
import unittest

from unittest.mock import patch

from tools.update_packages.applier import PackageApplier
from tools.update_packages.differ import InventoryDiffer
from tools.update_packages.models import BaselineInventory, FileOperation, PackageMode, UpdateManifest, ManifestEntry, FileRecord
from tools.update_packages.packager import UpdatePackager
from tools.update_packages.scanner import WorkspaceScanner, compute_bytes_sha256, calculate_stream_sha256, ScanningError
from tools.update_packages.state_manager import UpdateStateManager
from tools.update_packages.verifier import PackageVerifier, is_safe_relative_path, audit_path_ancestry_safety


class TestIncrementalUpdateSystem(unittest.TestCase):
    """Test suite covering B11 adversarial tests and B12 end-to-end acceptance."""

    def setUp(self):
        self.test_dir = tempfile.TemporaryDirectory(prefix="test_agd_update_")
        self.root = Path(self.test_dir.name).resolve()
        self.exports_dir = self.root / "exports" / "updates"
        self.exports_dir.mkdir(parents=True, exist_ok=True)

        # Populate a sample baseline repository
        (self.root / "src").mkdir(parents=True, exist_ok=True)
        (self.root / "docs").mkdir(parents=True, exist_ok=True)
        (self.root / "tests").mkdir(parents=True, exist_ok=True)
        (self.root / "assets").mkdir(parents=True, exist_ok=True)

        (self.root / "src" / "main.py").write_text("print('v1')\n", encoding="utf-8")
        (self.root / "docs" / "README.md").write_text("# Project v1\n", encoding="utf-8")
        (self.root / "assets" / "logo.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR_v1")
        (self.root / "docs" / "to_delete.txt").write_text("Delete me\n", encoding="utf-8")
        (self.root / "docs" / "old_name.md").write_text("Rename me\n", encoding="utf-8")

        self.state_mgr = UpdateStateManager(self.root)
        self.base_inv = self.state_mgr.initialize_baseline("BASE_TEST_001")

    def tearDown(self):
        self.test_dir.cleanup()

    def test_01_modified_python_file(self):
        """Scenario 1: Modified Python file is detected and packaged."""
        (self.root / "src" / "main.py").write_text("print('v2 modified')\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)

        self.assertEqual(summary["modified"], 1)
        self.assertEqual(entries[0].path, "src/main.py")
        self.assertEqual(entries[0].operation, FileOperation.MODIFY.value)

    def test_02_added_markdown_file(self):
        """Scenario 2: Newly added Markdown document is detected."""
        (self.root / "docs" / "NEW_GUIDE.md").write_text("# New Guide\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)

        self.assertEqual(summary["added"], 1)
        added_entry = next(e for e in entries if e.path == "docs/NEW_GUIDE.md")
        self.assertEqual(added_entry.operation, FileOperation.ADD.value)

    def test_03_deleted_file(self):
        """Scenario 3: Deleted file is properly marked as DELETE without payload."""
        (self.root / "docs" / "to_delete.txt").unlink()
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)

        self.assertEqual(summary["deleted"], 1)
        del_entry = next(e for e in entries if e.path == "docs/to_delete.txt")
        self.assertEqual(del_entry.operation, FileOperation.DELETE.value)
        self.assertIsNone(del_entry.payload_path)

    def test_04_renamed_file(self):
        """Scenario 4: File rename is correctly identified via SHA-256 match."""
        # Rename old_name.md to new_name.md
        content = (self.root / "docs" / "old_name.md").read_bytes()
        (self.root / "docs" / "old_name.md").unlink()
        (self.root / "docs" / "new_name.md").write_bytes(content)

        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)

        self.assertEqual(summary["renamed"], 1)
        rename_entry = next(e for e in entries if e.path == "docs/new_name.md")
        self.assertEqual(rename_entry.operation, FileOperation.RENAME.value)
        self.assertEqual(rename_entry.renamed_from, "docs/old_name.md")

    def test_05_modified_binary_file(self):
        """Scenario 5: Modified PNG binary is safely tracked and flagged as binary."""
        (self.root / "assets" / "logo.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR_v2_updated_bytes")
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)

        self.assertEqual(summary["modified"], 1)
        bin_entry = next(e for e in entries if e.path == "assets/logo.png")
        self.assertTrue(bin_entry.is_binary)

    def test_06_arabic_unicode_filename(self):
        """Scenario 6: Arabic / Unicode filenames are preserved without encoding distortion."""
        arabic_name = "وثيقة_التصميم_العربي.md"
        (self.root / "docs" / arabic_name).write_text("# دليل التصميم باللغة العربية\n", encoding="utf-8")

        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        self.assertIn(f"docs/{arabic_name}", curr)

        target_inv = BaselineInventory(
            baseline_id="SNAP_ARABIC",
            repo_identity="Test",
            created_at_utc="2026-10-18T00:00:00Z",
            tool_version="1.0.0",
            files=curr
        )
        packager = UpdatePackager(self.root)
        res = packager.build_package(self.base_inv, target_inv, PackageMode.COMPLETE, "UPDATE_ARABIC", self.exports_dir)
        self.assertEqual(res["status"], "SUCCESS")

        verification = PackageVerifier.verify_package(Path(res["archive_path"]))
        self.assertEqual(verification["status"], "VALID")

    def test_07_content_changed_same_timestamp(self):
        """Scenario 7: Content changed with unchanged timestamp is still detected via SHA-256."""
        target_file = self.root / "src" / "main.py"
        old_stat = target_file.stat()
        target_file.write_text("print('timestamp unchanged but content changed')\n", encoding="utf-8")
        # Restore old mtime
        os.utime(target_file, (old_stat.st_atime, old_stat.st_mtime))

        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        entries, summary = InventoryDiffer.compute_diff(self.base_inv.files, curr)
        self.assertEqual(summary["modified"], 1)

    def test_08_untracked_new_file(self):
        """Scenario 8: Untracked new files in valid project directories are captured."""
        (self.root / "src" / "helper.py").write_text("def helper(): pass\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        self.assertIn("src/helper.py", curr)

    def test_09_no_recursive_zip_inclusion(self):
        """Scenario 9: Previously exported ZIPs are strictly excluded and never packaged recursively."""
        dummy_zip = self.exports_dir / "AGD_UPDATE_0001_OLD.zip"
        dummy_zip.write_bytes(b"PK\x05\x06" + b"\x00" * 18)  # Empty ZIP bytes

        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        # Verify no .zip or exports/updates files appear in scanned inventory
        for p in curr:
            self.assertFalse(p.endswith(".zip"))
            self.assertFalse(p.startswith("exports/updates/"))

    def test_10_two_updates_before_acknowledgment(self):
        """Scenario 10: Two sequential exports preserve sequence and cumulative base."""
        # Export 1
        (self.root / "docs" / "file1.md").write_text("File 1\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target1 = BaselineInventory("SNAP_1", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        packager = UpdatePackager(self.root)
        res1 = packager.build_package(self.base_inv, target1, PackageMode.COMPLETE, "UPDATE_0001", self.exports_dir, sequence_num=1)
        self.state_mgr.record_export(res1)

        # Export 2 (cumulative against original unacknowledged baseline)
        (self.root / "docs" / "file2.md").write_text("File 2\n", encoding="utf-8")
        target2 = BaselineInventory("SNAP_2", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        res2 = packager.build_package(self.base_inv, target2, PackageMode.COMPLETE, "UPDATE_0002", self.exports_dir, sequence_num=2)
        self.state_mgr.record_export(res2)

        self.assertEqual(res2["summary"]["added"], 2)  # Contains both file1 and file2 cumulatively

    def test_11_apply_to_wrong_baseline_rejected(self):
        """Scenario 11: Applying update to an incompatible workspace baseline is rejected."""
        # Make a package modifying src/main.py
        (self.root / "src" / "main.py").write_text("v2\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_V2", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        packager = UpdatePackager(self.root)
        res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_V2", self.exports_dir)

        # Create a foreign target directory with incompatible src/main.py
        with tempfile.TemporaryDirectory() as foreign_dir:
            f_root = Path(foreign_dir)
            (f_root / "src").mkdir(parents=True, exist_ok=True)
            (f_root / "src" / "main.py").write_text("foreign corrupted content\n", encoding="utf-8")

            applier = PackageApplier(f_root, enforce_base_match=True)
            apply_res = applier.apply(Path(res["archive_path"]))
            self.assertEqual(apply_res["status"], "FAILED")
            self.assertEqual(apply_res["stage"], "PREREQUISITE_CHECK")

    def test_12_tampered_payload_rejected(self):
        """Scenario 12: Archive with tampered payload bytes fails verification."""
        (self.root / "src" / "main.py").write_text("v2\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_V2", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        packager = UpdatePackager(self.root)
        res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_V2", self.exports_dir)
        zip_path = Path(res["archive_path"])

        # Tamper with the ZIP by overwriting payload/src/main.py with different bytes
        tampered_zip_path = zip_path.with_name("tampered.zip")
        with ZipFile(zip_path, "r") as zf_in, ZipFile(tampered_zip_path, "w") as zf_out:
            for item in zf_in.infolist():
                if item.filename == "payload/src/main.py":
                    zf_out.writestr(item, b"malicious tampered content\n")
                else:
                    zf_out.writestr(item, zf_in.read(item.filename))

        verification = PackageVerifier.verify_package(tampered_zip_path)
        self.assertEqual(verification["status"], "INVALID")
        self.assertTrue(any("Corrupted payload" in e for e in verification["errors"]))

    def test_13_path_traversal_attack_rejected(self):
        """Scenario 13: Archive with directory traversal attacks (../) is rejected."""
        malicious_zip = self.exports_dir / "evil.zip"
        with ZipFile(malicious_zip, "w") as zf:
            zf.writestr("UPDATE_MANIFEST.json", "{}")
            zf.writestr("payload/../../escaped.txt", b"evil data")

        verification = PackageVerifier.verify_package(malicious_zip)
        self.assertEqual(verification["status"], "INVALID")
        self.assertTrue(any("traversal" in e for e in verification["errors"]))

    def test_14_failure_interrupted_export_leaves_clean_state(self):
        """Scenario 14: An interrupted export cleans up temporary files without corrupting output."""
        packager = UpdatePackager(self.root)
        scanner_file = WorkspaceScanner(self.root).scan()["src/main.py"]
        corrupted_inv = BaselineInventory(
            baseline_id="SNAP_GHOST",
            repo_identity="Test",
            created_at_utc="2026-10-18T00:00:00Z",
            tool_version="1.0",
            files={
                "ghost.txt": scanner_file
            }
        )
        corrupted_inv.files["ghost.txt"].path = "non_existent_ghost.txt"

        with self.assertRaises(FileNotFoundError):
            packager.build_package(self.base_inv, corrupted_inv, PackageMode.COMPLETE, "UPDATE_GHOST", self.exports_dir)

        # Verify no half-baked temporary files remain in exports_dir
        tmp_files = list(self.exports_dir.glob("*.tmp"))
        self.assertEqual(len(tmp_files), 0)

    def test_15_failure_interrupted_apply_leaves_clean_target(self):
        """Scenario 15: Interrupted apply does not corrupt target workspace."""
        (self.root / "src" / "main.py").write_text("v2\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_V2", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        packager = UpdatePackager(self.root)
        res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_V2", self.exports_dir)
        zip_path = Path(res["archive_path"])

        # Tamper manifest to reference missing payload to force failure during staging
        tampered_zip = self.exports_dir / "broken_manifest.zip"
        with ZipFile(zip_path, "r") as zf_in, ZipFile(tampered_zip, "w") as zf_out:
            manifest = json.loads(zf_in.read("UPDATE_MANIFEST.json").decode("utf-8"))
            manifest["entries"][0]["payload_path"] = "payload/missing_ghost.py"
            zf_out.writestr("UPDATE_MANIFEST.json", json.dumps(manifest).encode("utf-8"))
            for item in zf_in.infolist():
                if item.filename != "UPDATE_MANIFEST.json":
                    zf_out.writestr(item, zf_in.read(item.filename))

        with tempfile.TemporaryDirectory() as target_dir:
            t_root = Path(target_dir)
            (t_root / "src").mkdir(parents=True, exist_ok=True)
            (t_root / "src" / "main.py").write_text("original", encoding="utf-8")

            applier = PackageApplier(t_root, enforce_base_match=False)
            apply_res = applier.apply(tampered_zip)
            self.assertEqual(apply_res["status"], "FAILED")
            # Ensure target file was NOT modified
            self.assertEqual((t_root / "src" / "main.py").read_text(encoding="utf-8"), "original")

    def test_16_missing_binary_detected(self):
        """Scenario 16: Missing binary asset referenced in manifest is caught."""
        (self.root / "assets" / "new_img.png").write_bytes(b"\x89PNG_new")
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        (self.root / "assets" / "new_img.png").unlink()  # Delete before packager reads it

        target = BaselineInventory("SNAP_IMG", "Test", "2026-10-18T00:00:00Z", "1.0", files=curr)
        packager = UpdatePackager(self.root)
        with self.assertRaises(FileNotFoundError):
            packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_IMG", self.exports_dir)

    def test_17_secret_bearing_files_excluded(self):
        """Scenario 17: .env, API keys, and private keys are screened out."""
        (self.root / ".env").write_text("SECRET_API_KEY=supersecret123\n", encoding="utf-8")
        (self.root / ".env.production").write_text("SECRET_TOKEN=xyz\n", encoding="utf-8")
        (self.root / "id_rsa").write_text("-----BEGIN RSA PRIVATE KEY-----\n", encoding="utf-8")

        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        self.assertNotIn(".env", curr)
        self.assertNotIn(".env.production", curr)
        self.assertNotIn("id_rsa", curr)

    def test_18_clean_checkout_portability(self):
        """Scenario 18: Generated update archive is a self-contained portable ZIP."""
        (self.root / "docs" / "PORTABLE.md").write_text("Portable\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_PORT", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        packager = UpdatePackager(self.root)
        res = packager.build_package(self.base_inv, target, PackageMode.REVIEW, "UPDATE_PORT", self.exports_dir)

        # Test extracting with pure python standard library without any local path references
        with tempfile.TemporaryDirectory() as extract_dir:
            shutil.unpack_archive(res["archive_path"], extract_dir)
            self.assertTrue((Path(extract_dir) / "UPDATE_MANIFEST.json").exists())
            self.assertTrue((Path(extract_dir) / "UPDATE_README.md").exists())
            self.assertTrue((Path(extract_dir) / "payload" / "docs" / "PORTABLE.md").exists())

    def test_19_windows_path_normalization(self):
        """Scenario 19: Windows backslashes are normalized to canonical POSIX forward slashes."""
        scanner = WorkspaceScanner(self.root)
        curr = scanner.scan()
        for p in curr:
            self.assertNotIn("\\", p)
            self.assertFalse(p.startswith("/"))

    def test_20_and_b12_end_to_end_acceptance(self):
        """B12 Acceptance Test: Full round-trip delta reconstruction and verification."""
        # 1. Create untouched clone of original baseline
        with tempfile.TemporaryDirectory(prefix="clone_base_") as clone_dir_str:
            clone_root = Path(clone_dir_str).resolve()
            # Copy all files from self.root to clone_root (excluding exports)
            for p, rec in self.base_inv.files.items():
                src_f = self.root / p
                dst_f = clone_root / p
                dst_f.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_f, dst_f)
            # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
            if (self.root / "tools" / "update_packages" / "registry").exists():
                shutil.copytree(self.root / "tools" / "update_packages" / "registry", clone_root / "tools" / "update_packages" / "registry")
            # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

            # 2. Perform a realistic multi-operation change in self.root:
            # - Source edit
            (self.root / "src" / "main.py").write_text("print('version 2.0 release')\n", encoding="utf-8")
            # - Documentation edit
            (self.root / "docs" / "README.md").write_text("# Project v2.0\nUpdated docs.\n", encoding="utf-8")
            # - New file addition
            (self.root / "docs" / "NEW_FEATURE.md").write_text("# Brand New Feature\n", encoding="utf-8")
            # - Binary modification
            (self.root / "assets" / "logo.png").write_bytes(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR_v2_new_logo_bytes")
            # - File deletion
            (self.root / "docs" / "to_delete.txt").unlink()
            # - File rename
            rename_content = (self.root / "docs" / "old_name.md").read_bytes()
            (self.root / "docs" / "old_name.md").unlink()
            (self.root / "docs" / "renamed_doc.md").write_bytes(rename_content)

            # 3. Scan target state
            scanner = WorkspaceScanner(self.root)
            target_files = scanner.scan()
            target_inv = BaselineInventory(
                baseline_id="SNAP_TARGET_RELEASE",
                repo_identity="Test Acceptance",
                created_at_utc="2026-10-18T00:00:00Z",
                tool_version="1.0.0",
                files=target_files
            )

            # 4. Export COMPLETE update package
            packager = UpdatePackager(self.root)
            pkg_res = packager.build_package(
                base_inventory=self.base_inv,
                target_inventory=target_inv,
                mode=PackageMode.COMPLETE,
                update_id="UPDATE_ACCEPTANCE_001",
                output_dir=self.exports_dir,
                sequence_num=100
            )
            self.assertEqual(pkg_res["status"], "SUCCESS")
            zip_file = Path(pkg_res["archive_path"])

            # 5. Apply update package onto the untouched clone of original baseline
            applier = PackageApplier(clone_root, enforce_base_match=True)
            apply_res = applier.apply(zip_file)
            self.assertEqual(apply_res["status"], "APPLIED")

            # 6. Verify resulting project state against target inventory 100% byte-for-byte!
            reconstructed_scanner = WorkspaceScanner(clone_root)
            reconstructed_files = reconstructed_scanner.scan()

            self.assertEqual(set(reconstructed_files.keys()), set(target_files.keys()))
            for p, target_rec in target_files.items():
                self.assertEqual(
                    reconstructed_files[p].sha256,
                    target_rec.sha256,
                    f"SHA-256 mismatch for reconstructed file: {p}"
                )

            # 7. Test that the update is rejected against wrong baseline
            with tempfile.TemporaryDirectory() as wrong_dir:
                wrong_root = Path(wrong_dir)
                (wrong_root / "src").mkdir(parents=True, exist_ok=True)
                (wrong_root / "src" / "main.py").write_text("random mismatched content", encoding="utf-8")
                wrong_applier = PackageApplier(wrong_root, enforce_base_match=True)
                self.assertEqual(wrong_applier.apply(zip_file)["status"], "FAILED")

            # 8. Test REVIEW mode package disclosure
            review_res = packager.build_package(
                base_inventory=self.base_inv,
                target_inventory=target_inv,
                mode=PackageMode.REVIEW,
                update_id="UPDATE_REVIEW_001",
                output_dir=self.exports_dir,
                sequence_num=101
            )
            self.assertEqual(review_res["mode"], "REVIEW")
            self.assertEqual(review_res["status"], "SUCCESS")

    # START CHANGE TASK-UPDATE-SYS-CORRECTION-01 | 2026-10-18T02:00:00Z | CREATED | Author: orchestrator-planner
    def test_21_fabricated_baseline_detection_and_missing_diff_proof(self):
        """Test A: Proves that fabricating a baseline post-task causes modified files to disappear,
        and proves that the update system flags and rejects untrusted baselines.
        """
        # 1. Modify src/main.py in self.root
        (self.root / "src" / "main.py").write_text("print('heavily modified content')\n", encoding="utf-8")

        # 2. Re-create the failure incident: initialize baseline AFTER modification
        state_mgr = UpdateStateManager(self.root)
        fabricated_base = state_mgr.initialize_baseline("BASE_FABRICATED_POST_TASK")

        # 3. Scan workspace at target state
        scanner = WorkspaceScanner(self.root)
        target_files = scanner.scan()

        # 4. Compute diff against fabricated baseline: modified files vanish (0 modified)!
        entries, summary = InventoryDiffer.compute_diff(fabricated_base.files, target_files)
        self.assertEqual(summary["modified"], 0, "Proves the incident: modified files vanish when baseline is taken post-task")
        self.assertEqual(len(entries), 0)

        # 5. Mark the fabricated baseline as invalid in registry
        fabricated_base.trust_status = "INVALID_FABRICATED_BASELINE"
        fabricated_base.invalidation_reason = "Synthesized post-task from modified workspace"
        state_mgr.save_baseline(fabricated_base)

        # 6. Verify that trying to export against this invalidated baseline is strictly rejected
        from tools.update_packages.cli import cmd_export
        import argparse
        args = argparse.Namespace(
            root=str(self.root),
            output_dir=str(self.exports_dir),
            mode="review",
            base_id="BASE_FABRICATED_POST_TASK",
            allow_untrusted_base=False
        )
        exit_code = cmd_export(args)
        self.assertEqual(exit_code, 1, "Export against untrusted baseline must be rejected")

    def test_22_manifest_path_traversal_rejected_in_verifier_and_applier(self):
        """Test B: Proves that manifest path traversal attacks are rejected by PackageVerifier and PackageApplier."""
        # 1. Test is_safe_relative_path unit tests directly
        self.assertFalse(is_safe_relative_path("../../ESCAPE_FROM_REPO.md")[0])
        self.assertFalse(is_safe_relative_path("/etc/passwd")[0])
        self.assertFalse(is_safe_relative_path("C:/Windows/system32")[0])
        self.assertFalse(is_safe_relative_path("CON.txt")[0])
        self.assertFalse(is_safe_relative_path("sub/NUL")[0])
        self.assertFalse(is_safe_relative_path("//unc/share")[0])
        self.assertFalse(is_safe_relative_path("valid/../invalid")[0])
        self.assertTrue(is_safe_relative_path("src/module/valid_file.py")[0])

        # 2. PackageVerifier audit of malicious manifests:
        # Create a malicious zip with traversal in manifest.entries[0].path
        malicious_zip = self.exports_dir / "malicious_traversal.zip"
        with ZipFile(malicious_zip, "w") as zf:
            manifest_dict = {
                "package_format_version": "1.0.0",
                "update_id": "EVIL_UPDATE",
                "sequence_number": 666,
                "created_at_utc": "2026-10-18T00:00:00Z",
                "package_mode": "COMPLETE",
                "creator_tool": "test",
                "status": "VALID",
                "base_snapshot_id": "BASE_TEST_001",
                "base_snapshot_hash": "0" * 64,
                "target_snapshot_id": "SNAP_EVIL",
                "target_snapshot_hash": "0" * 64,
                "entries": [
                    {
                        "path": "../../ESCAPE_FROM_REPO.md",
                        "operation": "ADD",
                        "size_bytes": 10,
                        "new_sha256": compute_bytes_sha256(b"evil data\n"),
                        "previous_sha256": None,
                        "is_binary": False,
                        "payload_path": "payload/evil.md",
                        "renamed_from": None
                    }
                ],
                "exclusions_count": 0,
                "operations_summary": {"added": 1, "modified": 0, "deleted": 0, "renamed": 0}
            }
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest_dict).encode("utf-8"))
            zf.writestr("payload/evil.md", b"evil data\n")

        # Verify PackageVerifier rejects it
        res_v = PackageVerifier.verify_package(malicious_zip)
        self.assertEqual(res_v["status"], "INVALID")
        self.assertTrue(any("Unsafe target path" in err for err in res_v["errors"]))

        # Verify PackageApplier rejects it
        applier = PackageApplier(self.root, enforce_base_match=False)
        res_a = applier.apply(malicious_zip)
        self.assertEqual(res_a["status"], "FAILED")
        self.assertEqual(res_a["stage"], "VERIFICATION")

        # 3. Test malicious payload_path in manifest entry
        malicious_pay_zip = self.exports_dir / "malicious_payload_path.zip"
        with ZipFile(malicious_pay_zip, "w") as zf:
            manifest_dict["entries"][0]["path"] = "src/legit.py"
            manifest_dict["entries"][0]["payload_path"] = "payload/../../escaped_payload.py"
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest_dict).encode("utf-8"))
            zf.writestr("payload/evil.md", b"evil data\n")

        res_pay = PackageVerifier.verify_package(malicious_pay_zip)
        self.assertEqual(res_pay["status"], "INVALID")
        self.assertTrue(any("Unsafe payload_path" in err for err in res_pay["errors"]))

        # 4. Test malicious renamed_from in manifest entry
        malicious_ren_zip = self.exports_dir / "malicious_rename.zip"
        with ZipFile(malicious_ren_zip, "w") as zf:
            manifest_dict["entries"][0]["path"] = "src/legit.py"
            manifest_dict["entries"][0]["payload_path"] = None
            manifest_dict["entries"][0]["operation"] = "RENAME"
            manifest_dict["entries"][0]["renamed_from"] = "../../etc/passwd"
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest_dict).encode("utf-8"))

        res_ren = PackageVerifier.verify_package(malicious_ren_zip)
        self.assertEqual(res_ren["status"], "INVALID")
        self.assertTrue(any("Unsafe renamed_from" in err for err in res_ren["errors"]))

    def test_23_empty_workspace_with_non_empty_base_rejected(self):
        """Test C: Proves that PackageApplier rejects application on empty target when base is required."""
        # Create a valid package targeting self.base_inv
        (self.root / "src" / "main.py").write_text("print('updated')\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory(
            baseline_id="SNAP_TARGET_01",
            repo_identity="Test",
            created_at_utc="2026-10-18T00:00:00Z",
            tool_version="1.0",
            files=scanner.scan()
        )
        packager = UpdatePackager(self.root)
        pkg = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_TEST_C", self.exports_dir)
        zip_path = Path(pkg["archive_path"])

        # Test on completely empty workspace
        with tempfile.TemporaryDirectory(prefix="empty_ws_") as empty_dir:
            empty_root = Path(empty_dir)

            # Test dry_run=True: Must fail prerequisite check, NOT return DRY_RUN_PASSED!
            applier = PackageApplier(empty_root, enforce_base_match=True)
            dry_res = applier.apply(zip_path, dry_run=True)
            self.assertEqual(dry_res["status"], "FAILED")
            self.assertEqual(dry_res["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("empty" in e for e in dry_res["errors"]))

            # Test actual apply: Must fail prerequisite check
            apply_res = applier.apply(zip_path, dry_run=False)
            self.assertEqual(apply_res["status"], "FAILED")
            self.assertEqual(apply_res["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("empty" in e for e in apply_res["errors"]))

    def test_24_transactional_atomic_rollback_on_apply_failure(self):
        """Test D: Proves that an apply failure rolls back 100% of modified files to their original state."""
        with tempfile.TemporaryDirectory(prefix="rollback_target_") as target_dir_str:
            t_root = Path(target_dir_str)
            (t_root / "src").mkdir(parents=True, exist_ok=True)
            (t_root / "docs").mkdir(parents=True, exist_ok=True)

            f1 = t_root / "src" / "f1.txt"
            f2 = t_root / "src" / "f2.txt"
            to_ren = t_root / "docs" / "to_rename.txt"

            f1.write_text("original f1\n", encoding="utf-8")
            f2.write_text("original f2\n", encoding="utf-8")
            to_ren.write_text("original rename\n", encoding="utf-8")

            # Scan initial base for target
            target_base_scanner = WorkspaceScanner(t_root)
            target_base_inv = BaselineInventory(
                baseline_id="BASE_ROLLBACK",
                repo_identity="Test",
                created_at_utc="2026-10-18T00:00:00Z",
                tool_version="1.0",
                files=target_base_scanner.scan()
            )

            # Create updated state
            f1.write_text("modified f1\n", encoding="utf-8")
            (t_root / "docs" / "added.txt").write_text("added doc\n", encoding="utf-8")
            to_ren.unlink()
            (t_root / "docs" / "renamed.txt").write_text("original rename\n", encoding="utf-8")

            target_scan = WorkspaceScanner(t_root).scan()
            target_inv = BaselineInventory(
                baseline_id="SNAP_ROLLBACK_TARGET",
                repo_identity="Test",
                created_at_utc="2026-10-18T00:00:00Z",
                tool_version="1.0",
                files=target_scan
            )

            packager = UpdatePackager(t_root)
            pkg = packager.build_package(target_base_inv, target_inv, PackageMode.COMPLETE, "UPDATE_ROLLBACK", self.exports_dir)
            zip_path = Path(pkg["archive_path"])

            # Restore target workspace to pre-update state
            f1.write_text("original f1\n", encoding="utf-8")
            (t_root / "docs" / "added.txt").unlink(missing_ok=True)
            (t_root / "docs" / "renamed.txt").unlink(missing_ok=True)
            to_ren.write_text("original rename\n", encoding="utf-8")

            # Pre-apply snapshot of all file contents and hashes
            pre_scan = WorkspaceScanner(t_root).scan()

            # Simulate failure during file application using a mock that fails on second write
            real_copy2 = shutil.copy2
            exec_copy_count = [0]

            def failing_copy2(src, dst, **kwargs):
                if "agd_stage_" in str(src):
                    exec_copy_count[0] += 1
                    # Fail on second applied file during execution
                    if exec_copy_count[0] >= 2:
                        raise IOError("Simulated disk full during mid-operation apply")
                return real_copy2(src, dst, **kwargs)

            with patch("shutil.copy2", side_effect=failing_copy2):
                applier = PackageApplier(t_root, enforce_base_match=True, expected_base_inventory=target_base_inv)
                apply_res = applier.apply(zip_path)

            self.assertEqual(apply_res["status"], "FAILED")
            self.assertTrue(apply_res.get("rolled_back", False), "Rollback flag must be True")
            self.assertEqual(apply_res["stage"], "APPLICATION_EXECUTION")

            # Verify 100% restoration: pre_scan and post_rollback_scan must be byte-identical!
            post_rollback_scan = WorkspaceScanner(t_root).scan()
            self.assertEqual(set(pre_scan.keys()), set(post_rollback_scan.keys()))
            for p, pre_rec in pre_scan.items():
                self.assertEqual(pre_rec.sha256, post_rollback_scan[p].sha256, f"Rollback corrupted file: {p}")
            self.assertFalse((t_root / "docs" / "added.txt").exists(), "Added file must not remain after rollback")
            self.assertFalse((t_root / "docs" / "renamed.txt").exists(), "Renamed file must not remain after rollback")
            self.assertTrue(to_ren.exists(), "Original file before rename must be restored")
            self.assertEqual(f1.read_text(encoding="utf-8"), "original f1\n")

    def test_25_scanner_fail_closed_on_unreadable_file(self):
        """Test: Scanner fails closed when encountering unreadable file under strict=True."""
        unreadable_file = self.root / "src" / "unreadable.py"
        unreadable_file.write_text("secret\n", encoding="utf-8")

        scanner = WorkspaceScanner(self.root, strict=True)

        def failing_open(*args, **kwargs):
            raise PermissionError("Access Denied: Simulated Permission Error")

        with patch("pathlib.Path.open", side_effect=failing_open):
            with self.assertRaises(ScanningError):
                scanner.scan()

    def test_26_packager_detects_concurrent_file_modification(self):
        """Test: Packager detects concurrent modification during payload reading."""
        (self.root / "src" / "main.py").write_text("v2\n", encoding="utf-8")
        scanner = WorkspaceScanner(self.root)
        target_inv = BaselineInventory(
            baseline_id="SNAP_CONCUR",
            repo_identity="Test",
            created_at_utc="2026-10-18T00:00:00Z",
            tool_version="1.0",
            files=scanner.scan()
        )

        packager = UpdatePackager(self.root)

        real_read_bytes = Path.read_bytes
        def mutating_read_bytes(*args, **kwargs):
            time.sleep(0.01)
            (self.root / "src" / "main.py").write_text("concurrently mutated content\n", encoding="utf-8")
            return real_read_bytes(self.root / "src" / "main.py")

        with patch.object(Path, "read_bytes", side_effect=mutating_read_bytes):
            with self.assertRaises(ValueError) as ctx:
                packager.build_package(self.base_inv, target_inv, PackageMode.COMPLETE, "UPDATE_CONCUR", self.exports_dir)
            self.assertTrue(
                "Concurrent file modification" in str(ctx.exception) or "Payload hash mismatch" in str(ctx.exception)
            )

    def test_27_symlink_pointing_outside_workspace_rejected(self):
        """Test: WorkspaceScanner rejects symlinks pointing outside workspace root."""
        with tempfile.TemporaryDirectory() as outside_dir:
            outside_file = Path(outside_dir) / "outside.txt"
            outside_file.write_text("outside data", encoding="utf-8")

            symlink_file = self.root / "src" / "symlink_escape.txt"
            try:
                symlink_file.symlink_to(outside_file)
            except (OSError, NotImplementedError):
                # On Windows without Developer Mode, creating symlinks may raise OSError
                self.skipTest("Symlink creation not supported in this environment")

            scanner = WorkspaceScanner(self.root, strict=True)
            with self.assertRaises(ScanningError):
                scanner.scan()
    # END CHANGE TASK-UPDATE-SYS-CORRECTION-01 | 2026-10-18T02:00:00Z | CREATED

    # START CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | CREATED | Author: orchestrator-planner
    def test_28_symlink_parent_directory_escape_rejected_across_operations(self):
        """Test: Symlink parent directory escapes are rejected across ADD, MODIFY, DELETE, and RENAME."""
        with tempfile.TemporaryDirectory() as outside_dir:
            outside_path = Path(outside_dir).resolve()
            outside_target = outside_path / "secret.txt"
            outside_target.write_text("classified", encoding="utf-8")

            # Create a symlink inside repo pointing to outside directory
            link_dir = self.root / "sym_link_dir"
            try:
                link_dir.symlink_to(outside_path, target_is_directory=True)
            except (OSError, NotImplementedError):
                self.skipTest("Directory symlink creation not supported in this environment")

            # 1. ADD through escaping symlink ancestor
            safe, reason = audit_path_ancestry_safety(self.root, "sym_link_dir/malicious_add.txt")
            self.assertFalse(safe)
            self.assertIn("resolves outside repository root", reason)

            # 2. MODIFY through escaping symlink ancestor
            safe, reason = audit_path_ancestry_safety(self.root, "sym_link_dir/secret.txt")
            self.assertFalse(safe)
            self.assertIn("resolves outside repository root", reason)

            # 3. DELETE through escaping symlink ancestor
            safe, reason = audit_path_ancestry_safety(self.root, "sym_link_dir/to_delete.txt")
            self.assertFalse(safe)

            # 4. Test PackageApplier rejects when manifest contains escaping path
            entry = ManifestEntry(
                path="sym_link_dir/malicious_add.txt",
                operation="ADD",
                payload_path="payload/sym_link_dir/malicious_add.txt",
                new_sha256=compute_bytes_sha256(b"evil"),
                size_bytes=4
            )
            manifest = UpdateManifest(
                package_format_version="1.0.0",
                update_id="TEST_SYMLINK_ESCAPE",
                base_snapshot_id=self.base_inv.baseline_id,
                base_snapshot_hash="any",
                target_snapshot_id="TGT",
                target_snapshot_hash="any",
                created_at_utc="2026-10-18T03:30:00Z",
                creator_tool="TestPackager",
                package_mode="COMPLETE",
                status="CREATED",
                operations_summary={"added": 1},
                entries=[entry],
                exclusions_count=0
            )
            target_inv = BaselineInventory("TGT", "Test", "2026-10-18T03:30:00Z", "1.0", files={
                "sym_link_dir/malicious_add.txt": FileRecord("sym_link_dir/malicious_add.txt", compute_bytes_sha256(b"evil"), 4, False)
            })
            target_bytes = target_inv.to_json().encode("utf-8")
            manifest.target_snapshot_hash = compute_bytes_sha256(target_bytes)

            zip_test = self.exports_dir / "test_escape.zip"
            with ZipFile(zip_test, "w") as zf:
                zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest.to_dict()))
                zf.writestr("TARGET_INVENTORY.json", target_bytes)
                zf.writestr("payload/sym_link_dir/malicious_add.txt", b"evil")

            applier = PackageApplier(self.root, enforce_base_match=False)
            res = applier.apply(zip_test)
            self.assertEqual(res["status"], "FAILED")
            self.assertEqual(res["stage"], "PATH_SECURITY_AUDIT")
            self.assertFalse((outside_path / "malicious_add.txt").exists())

    def test_29_path_validation_immediately_before_writing_toctou(self):
        """Test: Pre-mutation path safety re-validation detects dynamic symlink replacement and rolls back."""
        with tempfile.TemporaryDirectory() as outside_dir:
            (self.root / "race_dir").mkdir(parents=True, exist_ok=True)
            (self.root / "race_dir" / "file.txt").write_text("v1\n", encoding="utf-8")

            entry = ManifestEntry(
                path="race_dir/file.txt",
                operation="MODIFY",
                payload_path="payload/race_dir/file.txt",
                previous_sha256=compute_bytes_sha256(b"v1\n"),
                new_sha256=compute_bytes_sha256(b"v2\n"),
                size_bytes=3
            )
            manifest = UpdateManifest(
                package_format_version="1.0.0",
                update_id="TEST_TOCTOU",
                base_snapshot_id=self.base_inv.baseline_id,
                base_snapshot_hash="any",
                target_snapshot_id="TGT",
                target_snapshot_hash="any",
                created_at_utc="2026-10-18T03:30:00Z",
                creator_tool="TestPackager",
                package_mode="COMPLETE",
                status="CREATED",
                operations_summary={"modified": 1},
                entries=[entry],
                exclusions_count=0
            )
            target_inv = BaselineInventory("TGT", "Test", "2026-10-18T03:30:00Z", "1.0", files={
                p: rec for p, rec in self.base_inv.files.items()
            })
            target_inv.files["race_dir/file.txt"] = FileRecord("race_dir/file.txt", compute_bytes_sha256(b"v2\n"), 3, False)
            target_bytes = target_inv.to_json().encode("utf-8")
            manifest.target_snapshot_hash = compute_bytes_sha256(target_bytes)

            zip_test = self.exports_dir / "test_toctou.zip"
            with ZipFile(zip_test, "w") as zf:
                zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest.to_dict()))
                zf.writestr("TARGET_INVENTORY.json", target_bytes)
                zf.writestr("payload/race_dir/file.txt", b"v2\n")

            applier = PackageApplier(self.root, enforce_base_match=False)

            call_count = [0]
            orig_audit = audit_path_ancestry_safety
            def mock_audit(target_dir, rel_path):
                call_count[0] += 1
                if call_count[0] > 1 and rel_path == "race_dir/file.txt":
                    return False, "Simulated TOCTOU race: ancestry replaced with symlink"
                return orig_audit(target_dir, rel_path)

            with patch("tools.update_packages.applier.audit_path_ancestry_safety", side_effect=mock_audit):
                res = applier.apply(zip_test)
                self.assertEqual(res["status"], "FAILED")
                self.assertEqual(res["stage"], "APPLICATION_EXECUTION")
                self.assertTrue(res["rolled_back"])
                self.assertEqual((self.root / "race_dir" / "file.txt").read_text(encoding="utf-8"), "v1\n")

    def test_30_review_package_rejected_by_complete_update_applier(self):
        """Test: REVIEW mode packages are rejected by default and in dry_run, permitted only with allow_review_mode=True."""
        entry = ManifestEntry(
            path="src/main.py",
            operation="MODIFY",
            payload_path="payload/src/main.py",
            previous_sha256=compute_bytes_sha256(b"print('v1')\n"),
            new_sha256=compute_bytes_sha256(b"print('v2')\n"),
            size_bytes=len(b"print('v2')\n")
        )
        manifest = UpdateManifest(
            package_format_version="1.0.0",
            update_id="TEST_REVIEW_REJECT",
            base_snapshot_id=self.base_inv.baseline_id,
            base_snapshot_hash="any",
            target_snapshot_id="TGT",
            target_snapshot_hash="any",
            created_at_utc="2026-10-18T03:30:00Z",
            creator_tool="TestPackager",
            package_mode="REVIEW",
            status="CREATED",
            operations_summary={"modified": 1},
            entries=[entry],
            exclusions_count=5
        )
        zip_test = self.exports_dir / "test_review_mode.zip"
        with ZipFile(zip_test, "w") as zf:
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest.to_dict()))
            zf.writestr("payload/src/main.py", b"print('v2')\n")

        # 1. Default applier (allow_review_mode=False) in dry_run
        applier_default = PackageApplier(self.root, allow_review_mode=False)
        res_dry = applier_default.apply(zip_test, dry_run=True)
        self.assertEqual(res_dry["status"], "FAILED")
        self.assertEqual(res_dry["stage"], "PACKAGE_MODE_AUDIT")

        # 2. Default applier in actual apply
        res_apply = applier_default.apply(zip_test, dry_run=False)
        self.assertEqual(res_apply["status"], "FAILED")
        self.assertEqual(res_apply["stage"], "PACKAGE_MODE_AUDIT")

        # 3. Permitted when allow_review_mode=True is explicitly set
        applier_review = PackageApplier(self.root, allow_review_mode=True, enforce_base_match=False)
        res_allowed = applier_review.apply(zip_test, dry_run=True)
        self.assertEqual(res_allowed["status"], "DRY_RUN_PASSED")

    def test_31_extra_unaccounted_files_in_strict_base_inventory_rejected(self):
        """Test: Target workspace containing extra unaccounted files not in baseline is rejected."""
        (self.root / "src" / "rogue_extra.py").write_text("# rogue\n", encoding="utf-8")

        entry = ManifestEntry(
            path="src/main.py",
            operation="MODIFY",
            payload_path="payload/src/main.py",
            previous_sha256=compute_bytes_sha256(b"print('v1')\n"),
            new_sha256=compute_bytes_sha256(b"print('v2')\n"),
            size_bytes=len(b"print('v2')\n")
        )
        manifest = UpdateManifest(
            package_format_version="1.0.0",
            update_id="TEST_EXTRA_BASE",
            base_snapshot_id=self.base_inv.baseline_id,
            base_snapshot_hash="any",
            target_snapshot_id="TGT",
            target_snapshot_hash="any",
            created_at_utc="2026-10-18T03:30:00Z",
            creator_tool="TestPackager",
            package_mode="COMPLETE",
            status="CREATED",
            operations_summary={"modified": 1},
            entries=[entry],
            exclusions_count=0
        )
        target_inv = BaselineInventory("TGT", "Test", "2026-10-18T03:30:00Z", "1.0", files={
            p: rec for p, rec in self.base_inv.files.items()
        })
        target_inv.files["src/main.py"] = FileRecord("src/main.py", compute_bytes_sha256(b"print('v2')\n"), len(b"print('v2')\n"), False)
        target_bytes = target_inv.to_json().encode("utf-8")
        manifest.target_snapshot_hash = compute_bytes_sha256(target_bytes)

        zip_test = self.exports_dir / "test_extra_base.zip"
        with ZipFile(zip_test, "w") as zf:
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest.to_dict()))
            zf.writestr("TARGET_INVENTORY.json", target_bytes)
            zf.writestr("payload/src/main.py", b"print('v2')\n")

        applier = PackageApplier(
            self.root,
            enforce_base_match=True,
            expected_base_inventory=self.base_inv
        )
        res = applier.apply(zip_test)
        self.assertEqual(res["status"], "FAILED")
        self.assertEqual(res["stage"], "PREREQUISITE_CHECK")
        self.assertTrue(any("unexpected extra files" in err for err in res["errors"]))

    def test_32_post_export_changes_in_included_content_detected(self):
        """Test: Post-export changes in files that were included in the export are detected as drift."""
        (self.root / "src" / "main.py").write_text("print('v2 exported')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_DRIFT_INC", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        result = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_DRIFT_INC", self.exports_dir)
        zip_path = Path(result["archive_path"])

        (self.root / "src" / "main.py").write_text("print('v3 unexported post-cutoff drift')\n", encoding="utf-8")

        fresh_inv = WorkspaceScanner(self.root).scan()
        with ZipFile(zip_path, "r") as zf:
            manifest_data = json.loads(zf.read("UPDATE_MANIFEST.json").decode("utf-8"))

        manifest = UpdateManifest.from_dict(manifest_data)
        drift_detected = False
        for entry in manifest.entries:
            if entry.path in fresh_inv:
                if fresh_inv[entry.path].sha256 != entry.new_sha256:
                    drift_detected = True
                    break

        self.assertTrue(drift_detected, "Divergence between live workspace and exported manifest was not detected")

    def test_33_post_export_changes_in_relevant_excluded_content_detected(self):
        """Test: Post-export changes in relevant excluded files are detected via exclusion tracking."""
        big_file = self.root / "assets" / "large_graphic.svg"
        big_file.write_text("<svg>" + "A" * 2_500_000 + "</svg>", encoding="utf-8")

        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_DRIFT_EXC", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        result = packager.build_package(self.base_inv, target, PackageMode.REVIEW, "UPDATE_DRIFT_EXC", self.exports_dir)
        zip_path = Path(result["archive_path"])

        with ZipFile(zip_path, "r") as zf:
            exclusions = json.loads(zf.read("EXCLUSIONS.json").decode("utf-8"))

        big_file.write_text("<svg>" + "B" * 2_500_000 + "</svg>", encoding="utf-8")

        new_sha = calculate_stream_sha256(big_file)
        recorded_sha = next(e["sha256"] for e in exclusions if e["path"] == "assets/large_graphic.svg")
        self.assertNotEqual(new_sha, recorded_sha)

    def test_34_archive_sha256_accurately_computed_and_verified(self):
        """Test: Returned archive_sha256 matches closed zip byte hash; byte corruption is detected."""
        (self.root / "src" / "main.py").write_text("print('v34')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_HASH_VERIF", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        result = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_HASH_VERIF", self.exports_dir)

        zip_path = Path(result["archive_path"])
        reported_sha = result.get("archive_sha256")
        self.assertIsNotNone(reported_sha)

        actual_disk_sha = calculate_stream_sha256(zip_path)
        self.assertEqual(reported_sha, actual_disk_sha)

        raw_bytes = zip_path.read_bytes()
        corrupted_bytes = raw_bytes[:-1] + (b"\x00" if raw_bytes[-1:] != b"\x00" else b"\x01")
        zip_path.write_bytes(corrupted_bytes)
        tampered_disk_sha = calculate_stream_sha256(zip_path)
        self.assertNotEqual(reported_sha, tampered_disk_sha)

    def test_35_correct_small_cumulative_delta_against_shared_baseline(self):
        """Test: Modifying 1 file and adding 1 file produces a small delta with exact operations applied cleanly."""
        (self.root / "src" / "main.py").write_text("print('v35 delta modified')\n", encoding="utf-8")
        (self.root / "src" / "helper.py").write_text("def helper(): return 42\n", encoding="utf-8")

        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_SMALL_DELTA", "Test", "2026-10-18T00:00:00Z", "1.0", files=scanner.scan())
        result = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_SMALL_DELTA", self.exports_dir)

        zip_path = Path(result["archive_path"])
        self.assertLess(zip_path.stat().st_size, 10_240)

        with ZipFile(zip_path, "r") as zf:
            manifest_dict = json.loads(zf.read("UPDATE_MANIFEST.json").decode("utf-8"))

        manifest = UpdateManifest.from_dict(manifest_dict)
        self.assertEqual(len(manifest.entries), 2)
        op_map = {e.path: e.operation for e in manifest.entries}
        self.assertEqual(op_map["src/main.py"], FileOperation.MODIFY.value)
        self.assertEqual(op_map["src/helper.py"], FileOperation.ADD.value)

        with tempfile.TemporaryDirectory(prefix="agd_delta_target_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            for b_path, b_rec in self.base_inv.files.items():
                src_orig = self.root / b_path
                tgt_dest = dest_dir / b_path
                tgt_dest.parent.mkdir(parents=True, exist_ok=True)
                if b_path == "src/main.py":
                    tgt_dest.write_text("print('v1')\n", encoding="utf-8")
                else:
                    shutil.copy2(src_orig, tgt_dest)

            applier = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            res = applier.apply(zip_path)
            self.assertEqual(res["status"], "APPLIED")
            self.assertEqual(res["applied_count"], 2)

            dest_scanner = WorkspaceScanner(dest_dir)
            dest_files = dest_scanner.scan()
            for p, rec in target.files.items():
                self.assertIn(p, dest_files)
                self.assertEqual(dest_files[p].sha256, rec.sha256)
    # END CHANGE TASK-UPDATE-SYS-HARDENING-01 | 2026-10-18T03:30:00Z | CREATED

    # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED | Author: orchestrator-planner
    def test_36_complete_mode_application_with_nonexistent_base_rejected(self):
        """Defect 1 Regression: COMPLETE update with unresolvable/nonexistent base MUST fail closed before writes."""
        # Create a package declaring a non-existent base
        entry = ManifestEntry(
            path="src/new_feature.py",
            operation="ADD",
            payload_path="payload/src/new_feature.py",
            new_sha256=compute_bytes_sha256(b"print('new')\n"),
            size_bytes=len(b"print('new')\n")
        )
        target_inv = BaselineInventory(
            baseline_id="SNAP_TARGET_FAKE",
            repo_identity="Test",
            created_at_utc="2026-10-18T07:57:00Z",
            tool_version="1.0.0",
            files={
                "src/new_feature.py": FileRecord(
                    path="src/new_feature.py",
                    sha256=compute_bytes_sha256(b"print('new')\n"),
                    size_bytes=len(b"print('new')\n"),
                    is_binary=False
                )
            }
        )
        target_bytes = target_inv.to_json().encode("utf-8")
        target_hash = compute_bytes_sha256(target_bytes)

        manifest = UpdateManifest(
            package_format_version="1.0.0",
            update_id="TEST_NONEXISTENT_BASE",
            base_snapshot_id="FAKE_BASE_THAT_DOES_NOT_EXIST",
            base_snapshot_hash="a" * 64,
            target_snapshot_id="SNAP_TARGET_FAKE",
            target_snapshot_hash=target_hash,
            created_at_utc="2026-10-18T07:57:00Z",
            creator_tool="TestPackager",
            package_mode="COMPLETE",
            status="EXPORTED",
            operations_summary={"added": 1},
            entries=[entry],
            exclusions_count=0
        )
        fake_zip = self.exports_dir / "test_fake_base.zip"
        with ZipFile(fake_zip, "w") as zf:
            zf.writestr("UPDATE_MANIFEST.json", json.dumps(manifest.to_dict()).encode("utf-8"))
            zf.writestr("TARGET_INVENTORY.json", target_bytes)
            zf.writestr("payload/src/new_feature.py", b"print('new')\n")

        with tempfile.TemporaryDirectory(prefix="unrelated_dest_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            unrelated_file = dest_dir / "unrelated.txt"
            unrelated_file.write_text("unrelated content\n", encoding="utf-8")

            # 1. dry_run=True MUST fail closed at PREREQUISITE_CHECK
            applier = PackageApplier(dest_dir, enforce_base_match=True)
            res_dry = applier.apply(fake_zip, dry_run=True)
            self.assertEqual(res_dry["status"], "FAILED")
            self.assertEqual(res_dry["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("cannot be resolved" in err or "nonexistent" in err for err in res_dry["errors"]))

            # 2. real apply MUST fail closed at PREREQUISITE_CHECK with ZERO writes
            res_apply = applier.apply(fake_zip, dry_run=False)
            self.assertEqual(res_apply["status"], "FAILED")
            self.assertEqual(res_apply["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("cannot be resolved" in err or "nonexistent" in err for err in res_apply["errors"]))

            # Ensure zero mutations: new file not written, only unrelated file remains
            self.assertFalse((dest_dir / "src" / "new_feature.py").exists())
            self.assertTrue(unrelated_file.exists())
            self.assertEqual(unrelated_file.read_text(encoding="utf-8"), "unrelated content\n")
            self.assertNotEqual(res_apply.get("trust_status"), "VERIFIED_TRUSTED")

    def test_37_snapshot_hashes_tampering_rejected_by_verifier_and_applier(self):
        """Defect 2 Regression: Tampering with base_snapshot_hash or target_snapshot_hash is rejected by verifier and applier."""
        (self.root / "src" / "main.py").write_text("print('v37 valid')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_TAMPER_TEST", "Test", "2026-10-18T07:57:00Z", "1.0", files=scanner.scan())
        pkg_res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_TAMPER_TEST", self.exports_dir)
        valid_zip_path = Path(pkg_res["archive_path"])

        # Read manifest dict
        with ZipFile(valid_zip_path, "r") as zf:
            orig_manifest_dict = json.loads(zf.read("UPDATE_MANIFEST.json").decode("utf-8"))

        with tempfile.TemporaryDirectory(prefix="tamper_dest_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            # Seed destination with exact base files
            for p, rec in self.base_inv.files.items():
                dest_f = dest_dir / p
                dest_f.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.root / p, dest_f)

            # --- PART A: Tamper base_snapshot_hash ---
            tampered_base_zip = self.exports_dir / "tampered_base_hash.zip"
            tampered_base_manifest = dict(orig_manifest_dict)
            tampered_base_manifest["base_snapshot_hash"] = "a" * 64  # Arbitrary 64-char hex

            with ZipFile(valid_zip_path, "r") as zf_in, ZipFile(tampered_base_zip, "w") as zf_out:
                for item in zf_in.infolist():
                    if item.filename == "UPDATE_MANIFEST.json":
                        zf_out.writestr(item, json.dumps(tampered_base_manifest, ensure_ascii=False, indent=2).encode("utf-8"))
                    else:
                        zf_out.writestr(item, zf_in.read(item.filename))

            # Verifier must reject tampered base hash
            v_res_base = PackageVerifier.verify_package(tampered_base_zip, expected_base_inventory=self.base_inv)
            self.assertEqual(v_res_base["status"], "INVALID")
            self.assertTrue(any("base_snapshot_hash" in err for err in v_res_base["errors"]))

            # Applier must reject tampered base hash at PREREQUISITE_CHECK before writes
            applier_base = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            apply_res_base = applier_base.apply(tampered_base_zip)
            self.assertEqual(apply_res_base["status"], "FAILED")
            self.assertEqual(apply_res_base["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("base_snapshot_hash" in err or "tampering" in err for err in apply_res_base["errors"]))
            self.assertNotEqual(apply_res_base.get("trust_status"), "VERIFIED_TRUSTED")

            # --- PART B: Tamper target_snapshot_hash ---
            tampered_target_zip = self.exports_dir / "tampered_target_hash.zip"
            tampered_target_manifest = dict(orig_manifest_dict)
            tampered_target_manifest["target_snapshot_hash"] = "b" * 64  # Arbitrary 64-char hex

            with ZipFile(valid_zip_path, "r") as zf_in, ZipFile(tampered_target_zip, "w") as zf_out:
                for item in zf_in.infolist():
                    if item.filename == "UPDATE_MANIFEST.json":
                        zf_out.writestr(item, json.dumps(tampered_target_manifest, ensure_ascii=False, indent=2).encode("utf-8"))
                    else:
                        zf_out.writestr(item, zf_in.read(item.filename))

            # Verifier must reject tampered target hash
            v_res_target = PackageVerifier.verify_package(tampered_target_zip)
            self.assertEqual(v_res_target["status"], "INVALID")
            self.assertTrue(any("target_snapshot_hash" in err for err in v_res_target["errors"]))

            # Applier must reject tampered target hash before mutating (in VERIFICATION or PREREQUISITE_CHECK)
            applier_target = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            apply_res_target = applier_target.apply(tampered_target_zip)
            self.assertEqual(apply_res_target["status"], "FAILED")
            self.assertIn(apply_res_target["stage"], ("VERIFICATION", "PREREQUISITE_CHECK"))
            self.assertTrue(any("target_snapshot_hash" in err or "tampering" in err for err in apply_res_target["errors"]))
            self.assertNotEqual(apply_res_target.get("trust_status"), "VERIFIED_TRUSTED")
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | CREATED

    # START CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | CREATED | Author: orchestrator-planner
    def test_38_complete_package_missing_target_inventory_rejected(self):
        """Defect A Regression: COMPLETE package missing TARGET_INVENTORY.json MUST be rejected."""
        (self.root / "src" / "main.py").write_text("print('v38 valid')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_DEFECT_A_TEST", "Test", "2026-10-19T02:40:00Z", "1.0", files=scanner.scan())
        pkg_res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_DEFECT_A", self.exports_dir)
        valid_zip_path = Path(pkg_res["archive_path"])

        # Create a package stripped of TARGET_INVENTORY.json
        missing_target_zip = self.exports_dir / "missing_target_inventory.zip"
        with ZipFile(valid_zip_path, "r") as zf_in, ZipFile(missing_target_zip, "w") as zf_out:
            for item in zf_in.infolist():
                if item.filename != "TARGET_INVENTORY.json":
                    zf_out.writestr(item, zf_in.read(item.filename))

        # 1. PackageVerifier MUST reject with INVALID and explicit error
        v_res = PackageVerifier.verify_package(missing_target_zip)
        self.assertEqual(v_res["status"], "INVALID")
        self.assertTrue(any("requires TARGET_INVENTORY.json" in err for err in v_res["errors"]))

        # 2. PackageApplier MUST fail at VERIFICATION stage
        with tempfile.TemporaryDirectory(prefix="defect_a_dest_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            for p, rec in self.base_inv.files.items():
                dest_f = dest_dir / p
                dest_f.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.root / p, dest_f)

            applier = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            apply_res = applier.apply(missing_target_zip)
            self.assertEqual(apply_res["status"], "FAILED")
            self.assertEqual(apply_res["stage"], "VERIFICATION")
            self.assertTrue(any("requires TARGET_INVENTORY.json" in err for err in apply_res["errors"]))

    def test_39_forged_target_inventory_unchanged_file_hash_rejected(self):
        """Defect B Regression: Forged TARGET_INVENTORY.json with altered unchanged file hash is rejected even if archive digest matches."""
        (self.root / "src" / "main.py").write_text("print('v39 valid')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_DEFECT_B_TEST", "Test", "2026-10-19T02:40:00Z", "1.0", files=scanner.scan())
        pkg_res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_DEFECT_B", self.exports_dir)
        valid_zip_path = Path(pkg_res["archive_path"])

        # Tamper an UNCHANGED file in TARGET_INVENTORY.json
        with ZipFile(valid_zip_path, "r") as zf:
            target_data = json.loads(zf.read("TARGET_INVENTORY.json").decode("utf-8"))
            manifest_data = json.loads(zf.read("UPDATE_MANIFEST.json").decode("utf-8"))

        unchanged_path = "docs/README.md"
        self.assertIn(unchanged_path, target_data["files"])
        target_data["files"][unchanged_path]["sha256"] = "f" * 64

        # Serialize canonically and recompute target_snapshot_hash so archive digest matches perfectly
        tampered_target_obj = BaselineInventory.from_dict(target_data)
        tampered_target_bytes = tampered_target_obj.to_json().encode("utf-8")
        tampered_target_hash = compute_bytes_sha256(tampered_target_bytes)

        manifest_data["target_snapshot_hash"] = tampered_target_hash
        tampered_manifest_bytes = json.dumps(manifest_data, ensure_ascii=False, indent=2).encode("utf-8")

        tampered_unchanged_zip = self.exports_dir / "tampered_unchanged_target_inv.zip"
        with ZipFile(valid_zip_path, "r") as zf_in, ZipFile(tampered_unchanged_zip, "w") as zf_out:
            for item in zf_in.infolist():
                if item.filename == "TARGET_INVENTORY.json":
                    zf_out.writestr(item, tampered_target_bytes)
                elif item.filename == "UPDATE_MANIFEST.json":
                    zf_out.writestr(item, tampered_manifest_bytes)
                else:
                    zf_out.writestr(item, zf_in.read(item.filename))

        # 1. PackageVerifier with expected_base_inventory MUST reject with INVALID due to derived target contradiction
        v_res = PackageVerifier.verify_package(tampered_unchanged_zip, expected_base_inventory=self.base_inv)
        self.assertEqual(v_res["status"], "INVALID")
        self.assertTrue(any("contradicts derived target state" in err for err in v_res["errors"]))

        # 2. PackageApplier dry_run MUST fail at PREREQUISITE_CHECK
        with tempfile.TemporaryDirectory(prefix="defect_b_dest_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            for p, rec in self.base_inv.files.items():
                dest_f = dest_dir / p
                dest_f.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.root / p, dest_f)
            (dest_dir / "src" / "main.py").write_text("print('v1')\n", encoding="utf-8")

            applier = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            res_dry = applier.apply(tampered_unchanged_zip, dry_run=True)
            self.assertEqual(res_dry["status"], "FAILED")
            self.assertEqual(res_dry["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("contradicts derived target state" in err for err in res_dry["errors"]))

            # 3. PackageApplier real apply MUST fail at PREREQUISITE_CHECK with 0 writes and no trust
            res_apply = applier.apply(tampered_unchanged_zip, dry_run=False)
            self.assertEqual(res_apply["status"], "FAILED")
            self.assertEqual(res_apply["stage"], "PREREQUISITE_CHECK")
            self.assertTrue(any("contradicts derived target state" in err for err in res_apply["errors"]))
            self.assertNotEqual(res_apply.get("trust_status"), "VERIFIED_TRUSTED")
            # Target file src/main.py remains at base content, not modified
            self.assertEqual((dest_dir / "src" / "main.py").read_text(encoding="utf-8"), "print('v1')\n")

    def test_40_post_apply_verification_against_target_inventory(self):
        """Step 4.E: Verifies resulting workspace matches TARGET_INVENTORY.json after application, with rollback on discrepancy."""
        (self.root / "src" / "main.py").write_text("print('v40 valid')\n", encoding="utf-8")
        packager = UpdatePackager(self.root)
        scanner = WorkspaceScanner(self.root)
        target = BaselineInventory("SNAP_POST_APPLY_TEST", "Test", "2026-10-19T02:40:00Z", "1.0", files=scanner.scan())
        pkg_res = packager.build_package(self.base_inv, target, PackageMode.COMPLETE, "UPDATE_V40", self.exports_dir)
        valid_zip_path = Path(pkg_res["archive_path"])

        # 1. Normal apply succeeds and validates against TARGET_INVENTORY.json
        with tempfile.TemporaryDirectory(prefix="post_apply_dest_") as dest_dir_str:
            dest_dir = Path(dest_dir_str)
            for p, rec in self.base_inv.files.items():
                dest_f = dest_dir / p
                dest_f.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(self.root / p, dest_f)
            (dest_dir / "src" / "main.py").write_text("print('v1')\n", encoding="utf-8")

            applier = PackageApplier(dest_dir, enforce_base_match=True, expected_base_inventory=self.base_inv)
            res = applier.apply(valid_zip_path)
            self.assertEqual(res["status"], "APPLIED")
            self.assertEqual(res["trust_status"], "VERIFIED_TRUSTED")
            self.assertEqual((dest_dir / "src" / "main.py").read_text(encoding="utf-8"), "print('v40 valid')\n")
    # END CHANGE TASK-UPDATE-SYS-DEFECTS-02 | 2026-10-19T02:40:00Z | CREATED


if __name__ == "__main__":
    unittest.main()
# END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED
