#!/usr/bin/env python3
"""Independent regression checks for provenance, Windows-portable lock, and approval integration."""
# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:59:46Z | CREATED | Author: Governance maintainer
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]


def run(repo, *args):
    """Execute local Python CLI against an isolated checked-out fixture."""
    return subprocess.run([sys.executable, *args], cwd=repo, capture_output=True, text=True, check=False)


class FinalGovernanceTests(unittest.TestCase):
    """Cover new governance invariants independently of the previous 24 tests."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="agd-governance-final-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns("__pycache__", ".venv", ".git", "*.pyc"))

    def test_document_tampering_detected(self):
        p = self.repo / "AGENTS.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nUnrecorded documentation edit.\n", encoding="utf-8")
        v = run(self.repo, "tools/governance/change_tracking.py", "verify")
        self.assertNotEqual(v.returncode, 0)
        self.assertIn("Stale or unauthorized Markdown provenance", v.stdout)

    def test_malformed_source_region_detected(self):
        p = self.repo / "make_project_zip.py"
        p.write_text(p.read_text(encoding="utf-8") + "\n# START CHANGE TASK-ERR | 2026-10-17T08:00:00Z | CREATED | Author: agent\n", encoding="utf-8")
        v = run(self.repo, "tools/governance/change_tracking.py", "verify")
        self.assertNotEqual(v.returncode, 0)
        self.assertIn("unterminated START CHANGE", v.stdout)

    def test_created_then_edited_document(self):
        p = self.repo / "docs" / "NEW_TASK_NOTE.md"
        p.write_text("# New Task Note\n\nInitial content.\n", encoding="utf-8")
        before = run(self.repo, "tools/governance/change_tracking.py", "verify")
        self.assertNotEqual(before.returncode, 0)
        stamp = run(self.repo, "tools/governance/change_tracking.py", "edit-document", "--file", "docs/NEW_TASK_NOTE.md", "--kind", "CREATED", "--change-id", "TASK-1", "--editor", "test-agent")
        self.assertEqual(stamp.returncode, 0, stamp.stderr)
        self.assertEqual(run(self.repo, "tools/governance/change_tracking.py", "verify").returncode, 0)
        p.write_text(p.read_text(encoding="utf-8") + "Next revision.\n", encoding="utf-8")
        self.assertNotEqual(run(self.repo, "tools/governance/change_tracking.py", "verify").returncode, 0)
        stamp2 = run(self.repo, "tools/governance/change_tracking.py", "edit-document", "--file", "docs/NEW_TASK_NOTE.md", "--kind", "EDITED", "--change-id", "TASK-2", "--editor", "test-agent")
        self.assertEqual(stamp2.returncode, 0, stamp2.stderr)
        self.assertEqual(run(self.repo, "tools/governance/change_tracking.py", "verify").returncode, 0)
        metadata = json.loads((self.repo / "memory" / "DOCUMENT_PROVENANCE.json").read_text(encoding="utf-8"))["documents"]["docs/NEW_TASK_NOTE.md"]
        self.assertEqual([e["action"] for e in metadata["events"]], ["CREATED", "EDITED"])

    def add_synthetic_reports(self):
        # Test fixture only: these self-declared metrics are NOT scientific evidence or owner identity.
        for i in range(1, 6):
            path = self.repo / "docs" / "architecture" / "experiments" / f"EXP-0{i}_report.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"experiment_id":f"EXP-0{i}", "status":"EXPERIMENTALLY_VALIDATED", "pass_criteria_met":True, "benchmark_assets_tested":["synthetic"], "measured_metrics":{"iou":0.99}}), encoding="utf-8")

    def approve(self):
        return run(self.repo, "tools/memory_guard/manage_approvals.py", "authorize", "--confirm-owner-authorized", "--by", "FixtureOwner", "--note", "Synthetic end-to-end regression; not real owner consent")

    def test_approval_transition_all_validators(self):
        self.add_synthetic_reports()
        result = self.approve()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        for rel in ["tools/governance/change_tracking.py", "tools/memory_guard/verify_brain_sync.py", "tools/findings_guard/manage_findings.py", "tools/project_catalog/verify_catalog.py"]:
            args=[rel, "verify"] if rel.endswith("manage_findings.py") or rel.endswith("change_tracking.py") else [rel]
            check=run(self.repo,*args)
            self.assertEqual(check.returncode, 0, rel+": "+check.stdout+check.stderr)
        self.assertFalse((self.repo / "memory/decisions/.approval_tx_journal.json").exists())

    def test_failed_approval_rolls_back(self):
        self.add_synthetic_reports()
        prov = self.repo / "memory/decisions/OWNER_APPROVAL_PROVENANCE.json"
        initial=hashlib.sha256(prov.read_bytes()).hexdigest()
        derived=self.repo / "docs/architecture/TECHNOLOGY_COMPARISON_AND_GATES.md"
        derived.write_text(derived.read_text(encoding="utf-8")+"\nARCHITECTURE_APPROVAL_STATUS: " + "OWNER_APPROVED\n",encoding="utf-8")
        result=self.approve()
        self.assertNotEqual(result.returncode,0)
        self.assertEqual(hashlib.sha256(prov.read_bytes()).hexdigest(), initial)
        self.assertFalse((self.repo / "memory/decisions/.approval_tx_journal.json").exists())
        self.assertFalse((self.repo / "docs/history/immutable_baselines/OWNER_APPROVAL_PROVENANCE.rev0000.baseline.json").exists())

    def test_lock_serializes_cooperative_processes(self):
        # Portable POSIX / Windows process-lock unit test (native Windows CI still required).
        test_script = self.repo / "tools" / "findings_guard" / "_lock_test_runtime.py"
        test_script.write_text("from file_lock import repository_lock\nfrom pathlib import Path\nimport sys, time\nwith repository_lock(Path(sys.argv[1]), 'test-lock'):\n print('ACQUIRED', flush=True)\n time.sleep(0.3)\n",encoding="utf-8")
        try:
            first=subprocess.Popen([sys.executable,str(test_script),str(self.repo)],cwd=self.repo,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            self.assertEqual(first.stdout.readline().strip(),"ACQUIRED")
            second=run(self.repo,str(test_script),str(self.repo))
            self.assertEqual(second.returncode,0,second.stderr)
            self.assertEqual(second.stdout.strip(),"ACQUIRED")
            first.wait(timeout=10)
            if first.stdout: first.stdout.close()
            if first.stderr: first.stderr.close()
            self.assertEqual(first.returncode,0)
        finally:
            test_script.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:59:46Z | CREATED
