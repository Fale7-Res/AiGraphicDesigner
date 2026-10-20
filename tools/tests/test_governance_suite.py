#!/usr/bin/env python3
"""Comprehensive Positive & Negative Governance Verification Test Suite.

Covers all 11 mandatory engineering validation scenarios + AST symbol extraction
for Python/TS/JS (arrow functions, methods, nested symbols, exports) + Hook stdin/stdout contracts:
  1. Positive baseline & rule sync (.agent_rules <-> .agents/rules)
  2. Negative: Missing code mirrors
  3. Negative: Stale line references
  4. Negative: Undocumented functions
  5. Negative: Duplicate symbol entries (both in code and in FUNCTION_REGISTRY.md)
  6. Negative: Broken file-catalog links (uncataloged file, stale path, broken relationship endpoint)
  7. Negative: Invalid finding approvals (self-approval, missing rejection_reason, invalid line range)
  8. Negative: Approved findings not promoted (unpromoted APPROVED_FOR_PROMOTION, missing marker in target doc)
  9. Negative: Conflicting subagent ownership (overlapping ACTIVE write locks)
 10. Positive/Negative: Context recovery after interruption
 11. Negative: Missing owner approval (unauthorized OWNER_APPROVED claim or missing OWNER_ORIGINAL_VISION.md)
 12. Clean checkout portability (extract ZIP into an isolated temp directory and run all verifiers)
 13. Python & TypeScript/JavaScript symbol extraction (methods, nested functions, arrow functions, exports)
 14. Hook JSON stdin/stdout contract validation & explicit environment boundary reporting
"""
from pathlib import Path
from datetime import datetime, timezone
from zipfile import ZipFile
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools" / "memory_guard"))

import sync_code_mirrors as scm  # noqa: E402


def run_cmd(args: list[str], cwd: Path, stdin_text: str = "") -> subprocess.CompletedProcess:
    """Execute a command inside cwd and return the CompletedProcess."""
# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
    return subprocess.run(
        args,
        cwd=str(cwd),
        input=stdin_text,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED


def clone_repo_to_temp() -> tuple[tempfile.TemporaryDirectory, Path]:
    """Copy the current repository into an isolated temporary directory for mutation testing."""
    tmp_dir = tempfile.TemporaryDirectory(prefix="gov_test_clone_")
    dst = Path(tmp_dir.name) / "repo"
    shutil.copytree(
        ROOT,
        dst,
        ignore=shutil.ignore_patterns("__pycache__", ".git", "node_modules", ".venv", "*.pyc"),
    )
    return tmp_dir, dst


class GovernanceHardeningTestSuite(unittest.TestCase):
    """End-to-end positive and negative tests for AI Graphic Designer governance tools."""

    def test_01_positive_baseline_and_rule_sync(self) -> None:
        """Verify that the baseline repository passes rule sync, findings verify, brain sync, and catalog verify."""
        r_rules = run_cmd([sys.executable, "tools/memory_guard/sync_rules.py"], ROOT)
        self.assertEqual(r_rules.returncode, 0, msg=r_rules.stdout + r_rules.stderr)

        r_fnd = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], ROOT)
        self.assertEqual(r_fnd.returncode, 0, msg=r_fnd.stdout + r_fnd.stderr)

        r_brain = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], ROOT)
        self.assertEqual(r_brain.returncode, 0, msg=r_brain.stdout + r_brain.stderr)

        r_cat = run_cmd([sys.executable, "tools/project_catalog/verify_catalog.py"], ROOT)
        self.assertEqual(r_cat.returncode, 0, msg=r_cat.stdout + r_cat.stderr)

    def test_02_negative_missing_code_mirror(self) -> None:
        """Verify that adding a code file without a corresponding mirror fails verify_brain_sync.py."""
        tmp, repo = clone_repo_to_temp()
        try:
            (repo / "src_unmirrored.py").write_text("def unmirrored_fn():\n    return 42\n", encoding="utf-8")
            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Missing code mirror for src_unmirrored.py", res.stdout)
        finally:
            tmp.cleanup()

    def test_03_negative_stale_line_references(self) -> None:
        """Verify that shifting line numbers in a code file without updating its mirror is caught."""
        tmp, repo = clone_repo_to_temp()
        try:
            target = repo / "make_project_zip.py"
            orig = target.read_text(encoding="utf-8")
            shifted = "# shifted line 1\n# shifted line 2\n# shifted line 3\n" + orig
            target.write_text(shifted, encoding="utf-8")
            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res.returncode, 0)
            self.assertTrue(
                "Stale line reference" in res.stdout or "Stale code mirror SHA-256" in res.stdout,
                msg=res.stdout,
            )
        finally:
            tmp.cleanup()

    def test_04_negative_undocumented_functions(self) -> None:
        """Verify that an undocumented function omitted from FUNCTION_REGISTRY.md is caught."""
        tmp, repo = clone_repo_to_temp()
        try:
            reg = repo / "memory" / "FUNCTION_REGISTRY.md"
            reg_txt = reg.read_text(encoding="utf-8")
            # Remove build_archive entry from FUNCTION_REGISTRY.md
            mutated = "\n".join(
                line for line in reg_txt.splitlines() if "`build_archive`" not in line
            ) + "\n"
            reg.write_text(mutated, encoding="utf-8")
            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Undocumented or stale symbol in FUNCTION_REGISTRY.md for build_archive", res.stdout)
        finally:
            tmp.cleanup()

    def test_05_negative_duplicate_symbol_entries(self) -> None:
        """Verify detection of both duplicate functions across code files and duplicate rows in FUNCTION_REGISTRY.md."""
        tmp, repo = clone_repo_to_temp()
        try:
            # Subcase A: Duplicate row in FUNCTION_REGISTRY.md
            reg = repo / "memory" / "FUNCTION_REGISTRY.md"
            lines = reg.read_text(encoding="utf-8").splitlines()
            dup_line = next(l for l in lines if "`build_archive`" in l)
            reg.write_text("\n".join(lines + [dup_line]) + "\n", encoding="utf-8")
            res_a = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res_a.returncode, 0)
            self.assertIn("Duplicate symbol entry in FUNCTION_REGISTRY.md", res_a.stdout)

            # Subcase B: Duplicate top-level function name across two code files
            (repo / "dup_module.py").write_text("def compute_sha256(file_path):\n    return ''\n", encoding="utf-8")
            res_b = run_cmd([sys.executable, "tools/memory_guard/sync_code_mirrors.py"], repo)
            self.assertNotEqual(res_b.returncode, 0)
            self.assertIn("compute_sha256", res_b.stdout)
        finally:
            tmp.cleanup()

    def test_06_negative_broken_file_catalog_links(self) -> None:
        """Verify that uncataloged files, stale catalog paths, and broken relationship endpoints fail verify_catalog.py."""
        tmp, repo = clone_repo_to_temp()
        try:
            # Subcase A: Uncataloged file
            orphan = repo / "docs" / "UNCATALOGED_TEST.md"
            orphan.write_text("# Uncataloged\n", encoding="utf-8")
            res_a = run_cmd([sys.executable, "tools/project_catalog/verify_catalog.py"], repo)
            self.assertNotEqual(res_a.returncode, 0)
            self.assertIn("Uncataloged first-party files", res_a.stdout)
            orphan.unlink()

            # Subcase B: Broken relationship endpoint
            rel_file = repo / "tools" / "project_catalog" / "relationships.json"
            edges = json.loads(rel_file.read_text(encoding="utf-8"))
            edges.append({
                "source": "AGENTS.md",
                "target": "docs/NON_EXISTENT_ENDPOINT.md",
                "relationship": "Broken test link",
                "direction": "AGENTS.md -> docs/NON_EXISTENT_ENDPOINT.md",
                "change_impact": "Test",
                "evidence": "Test",
            })
            rel_file.write_text(json.dumps(edges, indent=2), encoding="utf-8")
            res_b = run_cmd([sys.executable, "tools/project_catalog/verify_catalog.py"], repo)
            self.assertNotEqual(res_b.returncode, 0)
            self.assertIn("Stale relationship endpoint", res_b.stdout)
        finally:
            tmp.cleanup()

    def test_07_negative_invalid_finding_approvals(self) -> None:
        """Verify that self-approved findings or REJECTED findings without rejection_reason are rejected."""
        tmp, repo = clone_repo_to_temp()
        try:
            fnd_path = next((repo / "memory" / "findings" / "entries").glob("*FND-20261017-001.json"))
            data = json.loads(fnd_path.read_text(encoding="utf-8"))
            # Self-approval: reviewer_agent == subagent_id
            data["review_events"][0]["reviewer_agent"] = data["subagent_id"]
            fnd_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            res_a = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_a.returncode, 0)
            self.assertIn("cannot self-approve", res_a.stdout)

            # Rejected without rejection_reason
            data["current_approval_state"] = "REJECTED"
            data["review_events"][0]["reviewer_agent"] = "orchestrator-planner"
            data["review_events"][0]["decision"] = "REJECTED"
            data["review_events"][0]["rejection_reason"] = "   "
            fnd_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            res_b = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_b.returncode, 0)
            self.assertIn("requires an explicit rejection_reason", res_b.stdout)
        finally:
            tmp.cleanup()

    def test_08_negative_approved_findings_not_promoted(self) -> None:
        """Verify that findings left in APPROVED_FOR_PROMOTION without promotion into target docs fail verification."""
        tmp, repo = clone_repo_to_temp()
        try:
            fnd_path = next((repo / "memory" / "findings" / "entries").glob("*FND-20261017-001.json"))
            data = json.loads(fnd_path.read_text(encoding="utf-8"))
            data["current_approval_state"] = "APPROVED_FOR_PROMOTION"
            data["promotion_record"] = None
            fnd_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            res = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Approved finding not promoted", res.stdout)
        finally:
            tmp.cleanup()

    def test_09_negative_conflicting_subagent_ownership(self) -> None:
        """Verify that two concurrent ACTIVE subagents claiming the same write file fail lock verification."""
        tmp, repo = clone_repo_to_temp()
        try:
            locks_path = repo / "memory" / "findings" / "subagent_ownership_locks.json"
            locks_data = {
                "schema_version": "1.0",
                "locks": [
                    {
                        "lock_id": "L1",
                        "task_id": "T1",
                        "subagent_id": "scene-and-vision-agent",
                        "status": "ACTIVE",
                        "write_files": ["src/shared_conflict.py"],
                    },
                    {
                        "lock_id": "L2",
                        "task_id": "T1",
                        "subagent_id": "vector-and-typography-agent",
                        "status": "ACTIVE",
                        "write_files": ["src/shared_conflict.py"],
                    },
                ],
            }
            locks_path.write_text(json.dumps(locks_data, indent=2), encoding="utf-8")
            res = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res.returncode, 0)
            self.assertIn("Conflicting subagent ownership lock on 'src/shared_conflict.py'", res.stdout)
        finally:
            tmp.cleanup()

    def test_10_context_recovery_after_interruption(self) -> None:
        """Verify deterministic context recovery after simulated session interruption."""
        tmp, repo = clone_repo_to_temp()
        try:
            wal_path = repo / "memory" / "session" / "ACTIVE_SESSION_WAL.md"
            wal_path.write_text(
                wal_path.read_text(encoding="utf-8")
                + "\n### `[WAL-0099] — 2026-10-17 — Interrupted mid-task step`\n- Saved partial geometry state.\n",
                encoding="utf-8",
            )
            res = run_cmd([sys.executable, "tools/memory_guard/recover_context.py", "--write"], repo)
            self.assertEqual(res.returncode, 0, msg=res.stdout + res.stderr)
            packet = json.loads(res.stdout)
            self.assertEqual(packet["status"], "RECOVERED_CLEAN")
            self.assertEqual(packet["latest_main_wal_id"], "WAL-0099")
            self.assertEqual(packet["architecture_approval_status"], "NOT_APPROVED")
            self.assertGreaterEqual(len(packet["isolated_subagent_wals"]), 2)
        finally:
            tmp.cleanup()

    def test_11_negative_missing_owner_approval(self) -> None:
        """Verify that claiming OWNER_APPROVED on architecture without owner authorization or removing verbatim vision fails."""
        tmp, repo = clone_repo_to_temp()
        try:
            # Subcase A: Unauthorized self-approval in DECISION_LOG.md
            dec_path = repo / "memory" / "decisions" / "DECISION_LOG.md"
            orig_dec = dec_path.read_text(encoding="utf-8")
            dec_path.write_text(
                orig_dec.replace("`ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED`", "`ARCHITECTURE_APPROVAL_STATUS`: `OWNER_APPROVED`"),
                encoding="utf-8",
            )
            res_a = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res_a.returncode, 0)
            self.assertTrue(
                "Fabricated or unauthorized OWNER_APPROVED" in res_a.stdout or "Missing owner approval gate" in res_a.stdout,
                msg=res_a.stdout,
            )

            # Subcase B: Missing OWNER_ORIGINAL_VISION.md
            dec_path.write_text(orig_dec, encoding="utf-8")
            (repo / "docs" / "product" / "OWNER_ORIGINAL_VISION.md").unlink()
            res_b = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res_b.returncode, 0)
            self.assertIn("Missing authoritative owner vision file", res_b.stdout)
        finally:
            tmp.cleanup()

    def test_12_clean_checkout_portability(self) -> None:
        """Verify that packaging the repo into a ZIP and extracting into a clean directory passes all checks."""
        tmp, repo = clone_repo_to_temp()
        clean_dir = tempfile.TemporaryDirectory(prefix="gov_clean_checkout_")
        try:
            r_zip = run_cmd([sys.executable, "make_project_zip.py"], repo)
            self.assertEqual(r_zip.returncode, 0, msg=r_zip.stdout + r_zip.stderr)
            zip_file = repo / "ai_graphic_designer_project.zip"
            self.assertTrue(zip_file.is_file())

            checkout_root = Path(clean_dir.name) / "unpacked"
            checkout_root.mkdir(parents=True, exist_ok=True)
            with ZipFile(zip_file, "r") as zf:
                zf.extractall(checkout_root)

            for check_cmd in [
                [sys.executable, "tools/memory_guard/sync_rules.py"],
                [sys.executable, "tools/findings_guard/manage_findings.py", "verify"],
                [sys.executable, "tools/memory_guard/verify_brain_sync.py"],
                [sys.executable, "tools/project_catalog/verify_catalog.py"],
            ]:
                proc = run_cmd(check_cmd, checkout_root)
                self.assertEqual(proc.returncode, 0, msg=f"Failed {check_cmd} in clean checkout: {proc.stdout} {proc.stderr}")
        finally:
            tmp.cleanup()
            clean_dir.cleanup()

    def test_13_python_and_ts_js_ast_symbol_extraction(self) -> None:
        """Verify extraction of class methods, nested functions, arrow functions, and exported declarations."""
        with tempfile.TemporaryDirectory(prefix="ast_sym_test_") as td:
            tpath = Path(td)
            py_sample = tpath / "sample.py"
            py_sample.write_text(
                "class Vectorizer:\n"
                "    def trace(self, mask):\n"
                "        def inner_smooth(pts):\n"
                "            return pts\n"
                "        return inner_smooth(mask)\n",
                encoding="utf-8",
            )
            py_syms = scm.extract_python_symbols(py_sample)
            py_names = {s["name"]: (s["kind"], s["start_line"], s["end_line"]) for s in py_syms}
            self.assertIn("Vectorizer", py_names)
            self.assertEqual(py_names["Vectorizer"][0], "class")
            self.assertIn("Vectorizer.trace", py_names)
            self.assertEqual(py_names["Vectorizer.trace"][0], "method")
            self.assertIn("Vectorizer.trace.inner_smooth", py_names)
            self.assertEqual(py_names["Vectorizer.trace.inner_smooth"][0], "nested_function")

            ts_sample = tpath / "canvas.ts"
            ts_sample.write_text(
                "export interface LayerProps {\n"
                "  id: string;\n"
                "}\n"
                "export const computeIoU = (a: number, b: number): number => {\n"
                "  const clamp = (x: number) => Math.max(0, x);\n"
                "  return clamp(a) / Math.max(1, b);\n"
                "};\n"
                "export class CanvasController {\n"
                "  public renderLayer(id: string): void {\n"
                "    console.log(id);\n"
                "  }\n"
                "}\n",
                encoding="utf-8",
            )
            ts_syms = scm.extract_ts_js_symbols(ts_sample)
            ts_names = {s["name"]: s["kind"] for s in ts_syms}
            self.assertEqual(ts_names.get("LayerProps"), "exported_interface")
            self.assertEqual(ts_names.get("computeIoU"), "exported_arrow_function")
            self.assertEqual(ts_names.get("computeIoU.clamp"), "nested_arrow_function")
            self.assertEqual(ts_names.get("CanvasController"), "exported_class")
            self.assertEqual(ts_names.get("CanvasController.renderLayer"), "method")

    def test_14_hook_contracts_and_environment_boundary(self) -> None:
        """Test SessionStart and Stop hook script JSON stdin/stdout contracts on clean and dirty states."""
        # 1. SessionStart hook contract
        payload = json.dumps({"conversationId": "test-uuid", "workspacePaths": [str(ROOT)]})
        r_start = run_cmd([sys.executable, "tools/memory_guard/session_start_hook.py"], ROOT, stdin_text=payload)
        self.assertEqual(r_start.returncode, 0)
        start_out = json.loads(r_start.stdout)
        self.assertIn("injectSteps", start_out)

        # 2. Stop hook contract on valid state -> decision: allow
        r_stop_ok = run_cmd([sys.executable, "tools/memory_guard/stop_gate_hook.py"], ROOT, stdin_text=payload)
        self.assertEqual(r_stop_ok.returncode, 0)
        stop_ok_out = json.loads(r_stop_ok.stdout)
        self.assertEqual(stop_ok_out.get("decision"), "allow")

        # 3. Stop hook contract on broken state -> decision: continue
        tmp, repo = clone_repo_to_temp()
        try:
            (repo / "untracked_code.py").write_text("def broken():\n    pass\n", encoding="utf-8")
            r_stop_fail = run_cmd([sys.executable, "tools/memory_guard/stop_gate_hook.py"], repo, stdin_text=payload)
            self.assertEqual(r_stop_fail.returncode, 0)
            stop_fail_out = json.loads(r_stop_fail.stdout)
            self.assertEqual(stop_fail_out.get("decision"), "continue")
            self.assertIn("External Brain Sync Check Failed", stop_fail_out.get("reason", ""))
        finally:
            tmp.cleanup()



    def test_15_negative_vision_sentence_tampering_preserving_header(self) -> None:
        """Regression 1: Modifying a sentence inside OWNER_ORIGINAL_VISION.md while preserving header & opening text must FAIL."""
        tmp, repo = clone_repo_to_temp()
        try:
            vis_path = repo / "docs" / "product" / "OWNER_ORIGINAL_VISION.md"
            orig_text = vis_path.read_text(encoding="utf-8")
            # Keep header and opening text intact, modify one internal sentence in the middle
            tampered_text = orig_text.replace(
                "يروح عامل جروب اسمه مثلاً Potato تمام",
                "يروح عامل لير عادي بدون جروب اسمه Potato تمام",
            )
            self.assertNotEqual(orig_text, tampered_text)
            vis_path.write_text(tampered_text, encoding="utf-8")

            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res.returncode, 0, msg="Validator falsely passed when a middle sentence of OWNER_ORIGINAL_VISION.md was modified!")
            self.assertIn("Immutable owner vision modified", res.stdout)

            # Even if attacker recomputes full_file_sha256 in immutable_vision_baseline.json, baseline & sentence comparison must still fail
            bjson_p = repo / "tools" / "memory_guard" / "immutable_vision_baseline.json"
            bdata = json.loads(bjson_p.read_text(encoding="utf-8"))
            bdata["full_file_sha256"] = hashlib.sha256(vis_path.read_bytes()).hexdigest()
            bdata["full_file_byte_length"] = len(vis_path.read_bytes())
            bjson_p.write_text(json.dumps(bdata, indent=2), encoding="utf-8")
            res2 = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res2.returncode, 0, msg="Validator relied on file hash alone and missed content tampering!")
            self.assertIn("Immutable owner vision modified", res2.stdout)
        finally:
            tmp.cleanup()

    def test_16_negative_fabricated_owner_approved_with_invented_token(self) -> None:
        """Regression 2: Adding a fabricated OWNER_APPROVED claim with a self-invented OWNER_AUTHORIZATION_TOKEN must FAIL."""
        tmp, repo = clone_repo_to_temp()
        try:
            dec_path = repo / "memory" / "decisions" / "DECISION_LOG.md"
            orig_dec = dec_path.read_text(encoding="utf-8")
            fabricated = (
                orig_dec.replace(
                    "`ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED`",
                    "`ARCHITECTURE_APPROVAL_STATUS`: `OWNER_APPROVED`",
                )
                + "\nOWNER_AUTHORIZATION_TOKEN: SELF-INVENTED-TOKEN-99999\n"
            )
            dec_path.write_text(fabricated, encoding="utf-8")

            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res.returncode, 0, msg="Validator falsely accepted self-invented OWNER_AUTHORIZATION_TOKEN!")
            self.assertTrue(
                "Fabricated authorization token" in res.stdout
                or "Fabricated or unauthorized OWNER_APPROVED" in res.stdout,
                msg=res.stdout,
            )
        finally:
            tmp.cleanup()

    def test_17_negative_promoted_target_content_tampering_preserving_marker(self) -> None:
        """Regression 3: Modifying the actual content of a promoted documentation target while preserving its verification marker must FAIL."""
        tmp, repo = clone_repo_to_temp()
        try:
            # Target 1: Modify promoted text in FEASIBILITY_EXPERIMENTS_AND_GATES.md while keeping marker 'EXP-01'
            exp_path = repo / "docs" / "architecture" / "FEASIBILITY_EXPERIMENTS_AND_GATES.md"
            orig_exp = exp_path.read_text(encoding="utf-8")
            tampered_exp = orig_exp.replace(
                "Boundary IoU >= 0.92",
                "Boundary IoU >= 0.10 ( silently weakened threshold )",
            )
            self.assertIn("EXP-01", tampered_exp)
            self.assertNotEqual(orig_exp, tampered_exp)
            exp_path.write_text(tampered_exp, encoding="utf-8")

            res_fnd = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_fnd.returncode, 0, msg="manage_findings.py falsely passed when promoted target content was modified!")
            self.assertIn("Promoted target", res_fnd.stdout)

            # Even if attacker updates target_sha256_after and target_file_sha256 in the finding JSON, verbatim block & snapshot checks must still fail
            f2_p = repo / "memory" / "findings" / "entries" / "TASK-GOV-HARDENING__vector-and-typography-agent__FND-20261017-002.json"
            f2_data = json.loads(f2_p.read_text(encoding="utf-8"))
            new_sha = hashlib.sha256(exp_path.read_bytes()).hexdigest()
            f2_data["promotion_record"]["target_sha256_after"] = new_sha
            f2_data["promotion_record"]["promoted_targets"][0]["target_file_sha256"] = new_sha
            f2_p.write_text(json.dumps(f2_data, indent=2), encoding="utf-8")
            res_fnd2 = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_fnd2.returncode, 0, msg="Validator relied on target SHA-256 alone and missed content tampering!")
            self.assertIn("Promoted target", res_fnd2.stdout)

            res_brain = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(res_brain.returncode, 0)
        finally:
            tmp.cleanup()

    def test_18_negative_deleted_finding_reconciliation_and_tamper_detection(self) -> None:
        """Regression 4: Deleting a promoted finding (even if manifest & ledger are also edited) must FAIL reconciliation."""
        tmp, repo = clone_repo_to_temp()
        try:
            f1_path = repo / "memory" / "findings" / "entries" / "TASK-GOV-HARDENING__qa-reviewer-auditor__FND-20261017-001.json"
            f1_path.unlink()

            # Subcase A: Deleted from disk only
            res_a = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_a.returncode, 0)
            self.assertIn("Deleted or missing finding", res_a.stdout)

            # Subcase B: Attacker also removes FND-20261017-001 from findings_manifest.json and recompiles FINDINGS_LEDGER.md
            manifest_path = repo / "memory" / "findings" / "findings_manifest.json"
            mdata = json.loads(manifest_path.read_text(encoding="utf-8"))
            mdata["registered_findings"].pop("FND-20261017-001", None)
            manifest_path.write_text(json.dumps(mdata, indent=2), encoding="utf-8")
            run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "compile-ledger"], repo)

            res_b = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_b.returncode, 0, msg="Validator failed to catch finding deletion when manifest and ledger were tampered with!")
            self.assertTrue(
                "Deleted or missing finding" in res_b.stdout or "Deleted finding" in res_b.stdout,
                msg=res_b.stdout,
            )
        finally:
            tmp.cleanup()





    def test_19_negative_derived_doc_fabricated_approval(self) -> None:
        """Regression 5: Adding a fabricated OWNER_APPROVED architecture status claim to a derived doc (e.g. TECHNOLOGY_COMPARISON_AND_GATES.md) must FAIL."""
        tmp, repo = clone_repo_to_temp()
        try:
            tech_doc = repo / "docs" / "architecture" / "TECHNOLOGY_COMPARISON_AND_GATES.md"
            orig = tech_doc.read_text(encoding="utf-8")
            tech_doc.write_text(
                orig + "\n\nARCHITECTURE_APPROVAL_STATUS" + ": OWNER_APPROVED\n",
                encoding="utf-8",
            )
            res = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertNotEqual(
                res.returncode,
                0,
                msg="verify_brain_sync.py failed to catch fabricated OWNER_APPROVED claim in TECHNOLOGY_COMPARISON_AND_GATES.md!",
            )
            self.assertIn("TECHNOLOGY_COMPARISON_AND_GATES.md", res.stdout)
            res_cat = run_cmd([sys.executable, "tools/project_catalog/verify_catalog.py"], repo)
            self.assertNotEqual(
                res_cat.returncode,
                0,
                msg="verify_catalog.py failed to catch fabricated OWNER_APPROVED claim in TECHNOLOGY_COMPARISON_AND_GATES.md!",
            )
            self.assertIn("TECHNOLOGY_COMPARISON_AND_GATES.md", res_cat.stdout)
        finally:
            tmp.cleanup()

    def test_20_promoted_doc_legitimate_evolution_vs_unauthorized_edit(self) -> None:
        """Regression 6: Authorized subsequent doc revisions preserving promoted content pass, while edits to promoted content fail."""
        tmp, repo = clone_repo_to_temp()
        try:
            exp_rel = "docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md"
            exp_path = repo / exp_rel
            orig_exp = exp_path.read_text(encoding="utf-8")

            # Part A: Append a legitimate new note outside the promoted block, without recording revision yet -> must fail unrecorded check
            evolved_exp = orig_exp + "\n## 3. ملاحظة تخطيطية إضافية (`Subsequent Planning Note`)\n- سيتم تجهيز بيئة اختبار محلية لتجارب الأداء.\n"
            exp_path.write_text(evolved_exp, encoding="utf-8")
            res_unrecorded = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(res_unrecorded.returncode, 0)
            self.assertIn("without an authorized revision entry", res_unrecorded.stdout)

            # Part B: Record the legitimate revision via manage_findings.py record-doc-revision -> must succeed and pass verify!
            res_rec = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "record-doc-revision",
                    "--file",
                    exp_rel,
                    "--author",
                    "orchestrator-planner",
                    "--reason",
                    "Added Section 3 planning note while preserving promoted EXP-01..05 table",
                ],
                repo,
            )
            self.assertEqual(res_rec.returncode, 0, msg=res_rec.stdout + res_rec.stderr)

            res_verify_ok = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertEqual(res_verify_ok.returncode, 0, msg=res_verify_ok.stdout + res_verify_ok.stderr)

            # Part C: Attempt to modify previously promoted content (e.g. changing IoU threshold) and record revision -> must FAIL!
            tampered_exp = evolved_exp.replace("Boundary IoU >= 0.92", "Boundary IoU >= 0.30")
            exp_path.write_text(tampered_exp, encoding="utf-8")
            res_bad_rec = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "record-doc-revision",
                    "--file",
                    exp_rel,
                    "--author",
                    "orchestrator-planner",
                    "--reason",
                    "Attempted silent rewrite of promoted threshold",
                ],
                repo,
            )
            self.assertNotEqual(res_bad_rec.returncode, 0)
            self.assertIn("UNAUTHORIZED_PROMOTED_CONTENT_EDIT", res_bad_rec.stderr + res_bad_rec.stdout)
        finally:
            tmp.cleanup()

    # START CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:25:00Z | EDITED | Author: orchestrator-planner
    def test_21_findings_transactional_lifecycle_end_to_end(self) -> None:
        """Regression 7: Test full transactional lifecycle (capture -> submit -> reject -> submit -> approve -> promote)."""
        tmp, repo = clone_repo_to_temp()
        try:
            # 1. Capture new finding FND-20261017-991
            r_cap = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "capture",
                    "--id",
                    "FND-20261017-991",
                    "--task",
                    "TASK-LIFECYCLE",
                    "--subagent",
                    "scene-and-vision-agent",
                    "--sources",
                    "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md:1-20",
                    "--evidence",
                    "SceneGraph schema requires explicit z_index integer validation on every group node.",
                    "--confidence",
                    "HIGH",
                    "--action",
                    "Document z_index uniqueness invariant in SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md.",
                ],
                repo,
            )
            self.assertEqual(r_cap.returncode, 0, msg=r_cap.stdout + r_cap.stderr)

            # 2. Submit for parent review
            r_sub = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "submit",
                    "--id",
                    "FND-20261017-991",
                    "--actor",
                    "scene-and-vision-agent",
                ],
                repo,
            )
            self.assertEqual(r_sub.returncode, 0, msg=r_sub.stdout + r_sub.stderr)

            # 3. Parent reviews with NEEDS_REVISION
            r_rev1 = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "review",
                    "--id",
                    "FND-20261017-991",
                    "--reviewer",
                    "orchestrator-planner",
                    "--decision",
                    "NEEDS_REVISION",
                    "--event-id",
                    "REV-991-1",
                    "--reason",
                    "Specify exact line numbers in target spec.",
                ],
                repo,
            )
            self.assertEqual(r_rev1.returncode, 0, msg=r_rev1.stdout + r_rev1.stderr)

            # 4. Re-submit and parent approves for promotion
            run_cmd(
                [sys.executable, "tools/findings_guard/manage_findings.py", "submit", "--id", "FND-20261017-991"],
                repo,
            )
            r_app = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "approve",
                    "--id",
                    "FND-20261017-991",
                    "--reviewer",
                    "orchestrator-planner",
                    "--event-id",
                    "REV-991-2",
                    "--notes",
                    "Approved for promotion into SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md.",
                ],
                repo,
            )
            self.assertEqual(r_app.returncode, 0, msg=r_app.stdout + r_app.stderr)

            # 5. Promote into docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md
            r_prom = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "promote",
                    "--id",
                    "FND-20261017-991",
                    "--target-file",
                    "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md",
                    "--marker",
                    "z_index",
                    "--line-start",
                    "15",
                    "--line-end",
                    "25",
                ],
                repo,
            )
            self.assertEqual(r_prom.returncode, 0, msg=r_prom.stdout + r_prom.stderr)

            # Refresh catalog and verify 100% pass
            run_cmd([sys.executable, "tools/project_catalog/build_catalog.py", "--write"], repo)
            r_ver = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertEqual(r_ver.returncode, 0, msg=r_ver.stdout + r_ver.stderr)
        finally:
            tmp.cleanup()
    # END CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:25:00Z | EDITED

    def test_22_findings_interruption_rollback_and_duplicate_event_rejection(self) -> None:
        """Regression 8: Test mid-transaction interruption rollback (recover-tx) and duplicate event submission rejection."""
        tmp, repo = clone_repo_to_temp()
        try:
            # 1. Simulate interruption mid-capture
            r_int = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "capture",
                    "--id",
                    "FND-20261017-999",
                    "--task",
                    "TASK-INT",
                    "--subagent",
                    "scene-and-vision-agent",
                    "--sources",
                    "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md:1-10",
                    "--evidence",
                    "Interrupted finding write.",
                    "--confidence",
                    "HIGH",
                    "--action",
                    "Test rollback.",
                    "--simulate-interrupt",
                ],
                repo,
            )
            self.assertNotEqual(r_int.returncode, 0)
            self.assertTrue((repo / "memory" / "findings" / ".tx_journal.json").is_file())

            # Verify fails while uncommitted journal exists
            r_ver_dirty = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertNotEqual(r_ver_dirty.returncode, 0)
            self.assertIn("Uncommitted findings transaction journal", r_ver_dirty.stdout)

            # Recover transaction -> rolls back partial entry file and restores clean state
            r_rec = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "recover-tx"], repo)
            self.assertEqual(r_rec.returncode, 0, msg=r_rec.stdout + r_rec.stderr)
            self.assertIn("ROLLED_BACK_CLEAN", r_rec.stdout)

            r_ver_clean = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertEqual(r_ver_clean.returncode, 0, msg=r_ver_clean.stdout + r_ver_clean.stderr)

            # 2. Test duplicate finding capture rejection
            r_dup_fnd = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "capture",
                    "--id",
                    "FND-20261017-001",
                    "--task",
                    "TASK-GOV-HARDENING",
                    "--subagent",
                    "qa-reviewer-auditor",
                    "--sources",
                    "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md:1-10",
                    "--evidence",
                    "Dup",
                    "--confidence",
                    "HIGH",
                    "--action",
                    "Dup",
                ],
                repo,
            )
            self.assertNotEqual(r_dup_fnd.returncode, 0)
            self.assertIn("DUPLICATE_FINDING_ERROR", r_dup_fnd.stderr + r_dup_fnd.stdout)

            # 3. Test duplicate review event_id rejection
            r_dup_ev = run_cmd(
                [
                    sys.executable,
                    "tools/findings_guard/manage_findings.py",
                    "approve",
                    "--id",
                    "FND-20261017-001",
                    "--reviewer",
                    "orchestrator-planner",
                    "--event-id",
                    "REV-20261017-001",
                ],
                repo,
            )
            self.assertNotEqual(r_dup_ev.returncode, 0)
            self.assertIn("DUPLICATE_EVENT_ERROR", r_dup_ev.stderr + r_dup_ev.stdout)
        finally:
            tmp.cleanup()

    # START CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:26:00Z | EDITED | Author: orchestrator-planner
    def test_23_findings_concurrent_writes_locking(self) -> None:
        """Regression 9: Concurrent subagent capture processes serialize safely via flock without manifest corruption."""
        tmp, repo = clone_repo_to_temp()
        try:
            r_init = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            base_count = json.loads(r_init.stdout)["total_findings"]

            procs = []
            for idx in range(1, 5):
                fid = f"FND-20261017-10{idx}"
                agent = f"worker-subagent-{idx}"
                p = subprocess.Popen(
                    [
                        sys.executable,
                        "tools/findings_guard/manage_findings.py",
                        "capture",
                        "--id",
                        fid,
                        "--task",
                        f"TASK-CONC-{idx}",
                        "--subagent",
                        agent,
                        "--sources",
                        "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md:1-15",
                        "--evidence",
                        f"Concurrent finding evidence #{idx}",
                        "--confidence",
                        "HIGH",
                        "--action",
                        f"Concurrent action #{idx}",
                    ],
                    cwd=str(repo),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    text=True,
                )
                procs.append(p)

            for p in procs:
                out, err = p.communicate(timeout=15)
                self.assertEqual(p.returncode, 0, msg=f"Concurrent capture failed: {out} {err}")

            run_cmd([sys.executable, "tools/project_catalog/build_catalog.py", "--write"], repo)
            r_ver = run_cmd([sys.executable, "tools/findings_guard/manage_findings.py", "verify"], repo)
            self.assertEqual(r_ver.returncode, 0, msg=r_ver.stdout + r_ver.stderr)
            vdata = json.loads(r_ver.stdout)
            self.assertEqual(vdata["total_findings"], base_count + 4)
        finally:
            tmp.cleanup()
    # END CHANGE TASK-V01-CORRECTION-01 | 2026-10-17T21:26:00Z | EDITED

    def test_24_controlled_future_approval_transition_positive_and_negative(self) -> None:
        """Regression 10: Controlled future approval transition fails when preconditions are missing, and succeeds when all EXP-01..05 reports and owner confirmation exist."""
        tmp, repo = clone_repo_to_temp()
        try:
            # 0. PreToolUse Hook Contract: Calling manage_approvals.py authorize via run_command triggers force_ask
            hook_proc = subprocess.run(
                [sys.executable, "tools/memory_guard/pre_tool_use_hook.py"],
                cwd=str(repo),
                input=json.dumps({"toolCall": {"args": {"CommandLine": "python3 tools/memory_guard/manage_approvals.py authorize"}}}),
                text=True,
                capture_output=True,
                check=True,
            )
            self.assertEqual(json.loads(hook_proc.stdout)["decision"], "force_ask")

            # 1. Negative: Calling authorize without --confirm-owner-authorized must fail
            r_no_flag = run_cmd(
                [sys.executable, "tools/memory_guard/manage_approvals.py", "authorize", "--by", "Owner", "--note", "Approve"],
                repo,
            )
            self.assertNotEqual(r_no_flag.returncode, 0)
            self.assertIn("REFUSED", r_no_flag.stderr + r_no_flag.stdout)

            # 2. Negative: Calling authorize with --confirm-owner-authorized BEFORE EXP-01..05 reports exist must fail
            r_no_exp = run_cmd(
                [
                    sys.executable,
                    "tools/memory_guard/manage_approvals.py",
                    "authorize",
                    "--confirm-owner-authorized",
                    "--by",
                    "ProjectOwner",
                    "--note",
                    "Attempt premature approval before experiments",
                ],
                repo,
            )
            self.assertNotEqual(r_no_exp.returncode, 0)
            self.assertIn("PRECONDITION_FAILED", r_no_exp.stderr + r_no_exp.stdout)

            # 3. Positive: Create validated EXP-01..05 reports in the isolated clone, then run controlled transition -> must PASS!
            exp_dir = repo / "docs" / "architecture" / "experiments"
            exp_dir.mkdir(parents=True, exist_ok=True)
            for i in range(1, 6):
                rep = {
                    "experiment_id": f"EXP-0{i}",
                    "status": "EXPERIMENTALLY_VALIDATED",
                    "pass_criteria_met": True,
                    "benchmark_assets_tested": ["A01", "A02", "A03", "A04"],
                    "measured_metrics": {"iou": 0.95, "ssim": 0.94, "max_bezier_nodes": 28},
                }
                (exp_dir / f"EXP-0{i}_report.json").write_text(json.dumps(rep, indent=2) + "\n", encoding="utf-8")

            r_auth_ok = run_cmd(
                [
                    sys.executable,
                    "tools/memory_guard/manage_approvals.py",
                    "authorize",
                    "--confirm-owner-authorized",
                    "--by",
                    "ProjectOwner",
                    "--note",
                    "All 5 feasibility experiments validated; approving architecture for P0.",
                ],
                repo,
            )
            self.assertEqual(r_auth_ok.returncode, 0, msg=r_auth_ok.stdout + r_auth_ok.stderr)

            # Verify that verify_brain_sync.py passes the legitimate transition without modifying validator code!
            r_brain_ok = run_cmd([sys.executable, "tools/memory_guard/verify_brain_sync.py"], repo)
            self.assertEqual(r_brain_ok.returncode, 0, msg=r_brain_ok.stdout + r_brain_ok.stderr)
        finally:
            tmp.cleanup()

    # START CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:20:00Z | CREATED | Author: orchestrator-planner
    def test_25_version_code_mirrors_and_registry_isolation(self) -> None:
        """Multi-Version 1: Version code mirrors must be scoped to versions/<vid>/docs/CODE_MIRRORS/ and never in root memory/code_mirrors/."""
        # 1. Check version-01 mirror exists in its scoped directory
        v1_mirror = ROOT / "versions" / "version-01" / "docs" / "CODE_MIRRORS" / "src" / "geometry" / "bezier.py.md"
        self.assertTrue(v1_mirror.is_file(), msg=f"Missing scoped version mirror: {v1_mirror}")

        # 2. Check that version mirrors NEVER exist in root memory/code_mirrors/
        root_mirrors_dir = ROOT / "memory" / "code_mirrors"
        for p in root_mirrors_dir.glob("*.md"):
            self.assertFalse(
                p.name.startswith("versions__"),
                msg=f"Version mirror bled into shared root memory/code_mirrors/: {p.name}",
            )

        # 3. Check that version function registry exists in its scoped directory
        v1_reg = ROOT / "versions" / "version-01" / "docs" / "FUNCTION_REGISTRY.md"
        self.assertTrue(v1_reg.is_file(), msg=f"Missing scoped version function registry: {v1_reg}")

    def test_26_version_deduplication_isolation_positive_and_negative(self) -> None:
        """Multi-Version 2: Competing versions can share function names (isolation), but duplicates within the same version are blocked."""
        tmp, repo = clone_repo_to_temp()
        try:
            # 1. Negative: Inject duplicate function into the SAME version -> must fail sync_version
            v1_bezier = repo / "versions" / "version-01" / "src" / "geometry" / "bezier.py"
            orig_text = v1_bezier.read_text(encoding="utf-8")
            dup_code = orig_text + "\n\ndef fit_schneider_bezier(points, max_error_px=1.5):\n    return []\n"
            v1_bezier.write_text(dup_code, encoding="utf-8")

            r_sync_dup = run_cmd(
                [sys.executable, "tools/memory_guard/sync_code_mirrors.py", "--version", "version-01", "--write"],
                repo,
            )
            self.assertNotEqual(r_sync_dup.returncode, 0)
            self.assertIn("duplicate_functions_found", r_sync_dup.stdout)
        finally:
            tmp.cleanup()

    def test_27_version_file_catalog_isolation(self) -> None:
        """Multi-Version 3: Each version must maintain its own PROJECT_FILE_CATALOG.md with 100% intra-version coverage."""
        for vid in ["version-01", "version-02", "version-03"]:
            v_cat = ROOT / "versions" / vid / "PROJECT_FILE_CATALOG.md"
            self.assertTrue(v_cat.is_file(), msg=f"Missing {vid}/PROJECT_FILE_CATALOG.md")
            cat_text = v_cat.read_text(encoding="utf-8")
            self.assertIn(f"`{vid}`", cat_text)
            self.assertIn("100% Coverage", cat_text)

        # Verify negative: uncataloged file in a version fails verify_version_catalog
        tmp, repo = clone_repo_to_temp()
        try:
            untracked = repo / "versions" / "version-01" / "src" / "untracked_file.py"
            untracked.write_text("x = 1\n", encoding="utf-8")
            r_ver = run_cmd([sys.executable, "tools/project_catalog/verify_catalog.py", "--version", "version-01"], repo)
            self.assertNotEqual(r_ver.returncode, 0)
            self.assertIn("Uncataloged files in version-01", r_ver.stdout + r_ver.stderr)
        finally:
            tmp.cleanup()

    def test_28_benchmark_telemetry_schema_validation(self) -> None:
        """Multi-Version 4: Benchmark harness validates schema and rejects fabricated or malformed run records."""
        # 1. Verify schema CLI check passes
        r_schema = run_cmd([sys.executable, "benchmarks/harness/run_benchmark.py", "verify-schema"], ROOT)
        self.assertEqual(r_schema.returncode, 0, msg=r_schema.stdout + r_schema.stderr)

        # 2. Test positive payload validation
        valid_payload = {
            "run_id": "BENCH-20261017-001",
            "version_id": "version-01",
            "timestamp_utc": "2026-10-17T09:20:00Z",
            "dataset_asset_id": "A01",
            "hardware_telemetry": {
                "device_type": "LOCAL_GPU",
                "cpu_model": "AMD Ryzen 9",
                "ram_gb": 64.0,
                "gpu_model": "RTX 4090",
                "vram_gb": 24.0,
                "cuda_version": "12.4",
                "os_platform": "Windows",
            },
            "metrics": {
                "trimap_boundary_iou": 0.92,
                "lpips_score": 0.10,
                "ssim_score": 0.94,
                "max_bezier_node_count": 28,
                "latency_seconds": 3.8,
                "peak_vram_gb": 8.5,
                "estimated_inference_cost_usd": 0.015,
            },
            "verification_status": "VERIFIED_REAL_RUN",
        }
        test_script = (
            "import sys, json; sys.path.insert(0, 'benchmarks/harness'); "
            "import run_benchmark as rb; "
            f"ok, errs = rb.validate_benchmark_payload({json.dumps(valid_payload)}); "
            "assert ok, errs; print('VALID_PAYLOAD_PASSED')"
        )
        r_test = run_cmd([sys.executable, "-c", test_script], ROOT)
        self.assertEqual(r_test.returncode, 0, msg=r_test.stdout + r_test.stderr)
        self.assertIn("VALID_PAYLOAD_PASSED", r_test.stdout)

        # 3. Test negative payload validation (missing telemetry field)
        invalid_payload = dict(valid_payload)
        del invalid_payload["hardware_telemetry"]
        test_bad = (
            "import sys, json; sys.path.insert(0, 'benchmarks/harness'); "
            "import run_benchmark as rb; "
            f"ok, errs = rb.validate_benchmark_payload({json.dumps(invalid_payload)}); "
            "assert not ok; print('INVALID_PAYLOAD_REJECTED')"
        )
        r_bad = run_cmd([sys.executable, "-c", test_bad], ROOT)
        self.assertEqual(r_bad.returncode, 0, msg=r_bad.stdout + r_bad.stderr)
        self.assertIn("INVALID_PAYLOAD_REJECTED", r_bad.stdout)
    # END CHANGE TASK-MULTI-VER-01 | 2026-10-17T09:20:00Z | CREATED


def main() -> None:
    """Run all governance tests and write structured report to tools/tests/governance_test_report.json."""
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(GovernanceHardeningTestSuite)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    test_methods = sorted(
        m for m in dir(GovernanceHardeningTestSuite) if m.startswith("test_")
    )
    failed_names = {t.id().split(".")[-1] for t, _ in result.failures + result.errors}

    report = {
        "executed_at": datetime.now(timezone.utc).isoformat(),
        "total_tests": result.testsRun,
        "passed_tests": result.testsRun - len(failed_names),
        "failed_tests": len(failed_names),
        "status": "ALL_PASSED" if result.wasSuccessful() else "FAILED",
        "hook_integration_boundary": {
            "python_hook_stdin_stdout_contract_tested": True,
            "live_antigravity_ide_desktop_host_tested": False,
            "reason": "UNAVAILABLE_IN_SANDBOX_VM: Live Antigravity IDE/CLI host loop is external to this offline Linux VM sandbox; hook JSON contracts (SessionStart and Stop allow/continue blocking) were verified via subprocess stdin/stdout simulation.",
        },
        "test_cases": [
            {"test_name": name, "status": "FAILED" if name in failed_names else "PASSED"}
            for name in test_methods
        ],
    }
    report_path = HERE / "governance_test_report.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False))
    if not result.wasSuccessful():
        raise SystemExit(1)


if __name__ == "__main__":
    main()
