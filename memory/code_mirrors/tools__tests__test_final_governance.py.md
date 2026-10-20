# مرآة الكود التفصيلية: `tools/tests/test_final_governance.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/tests/test_final_governance.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/tests/test_final_governance.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `112` (`Lines 1–112`)
- **بصمة الملف (`SHA-256`):** `16398167aa9774b209ac667dee4f3eb596fda3778fa5e899394dc22157d10b93`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run` | `function` | `Lines 16–18` | `def run(repo, *args):` | Execute local Python CLI against an isolated checked-out fixture. |
| `FinalGovernanceTests` | `class` | `Lines 21–107` | `class FinalGovernanceTests(unittest.TestCase):` | Cover new governance invariants independently of the previous 24 tests. |
| `FinalGovernanceTests.setUp` | `method` | `Lines 24–28` | `def setUp(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_document_tampering_detected` | `method` | `Lines 30–35` | `def test_document_tampering_detected(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_malformed_source_region_detected` | `method` | `Lines 37–42` | `def test_malformed_source_region_detected(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_created_then_edited_document` | `method` | `Lines 44–58` | `def test_created_then_edited_document(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.add_synthetic_reports` | `method` | `Lines 60–65` | `def add_synthetic_reports(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.approve` | `method` | `Lines 67–68` | `def approve(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_approval_transition_all_validators` | `method` | `Lines 70–78` | `def test_approval_transition_all_validators(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_failed_approval_rolls_back` | `method` | `Lines 80–90` | `def test_failed_approval_rolls_back(self):` | رمز برمجي موثق. |
| `FinalGovernanceTests.test_lock_serializes_cooperative_processes` | `method` | `Lines 92–107` | `def test_lock_serializes_cooperative_processes(self):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run` — `Lines 16–18`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `18` (`Lines 16–18`)
- **الوظيفة:** Execute local Python CLI against an isolated checked-out fixture.
- **الكود الفعلي (`Lines 16–18`):**
```python
def run(repo, *args):
    """Execute local Python CLI against an isolated checked-out fixture."""
    return subprocess.run([sys.executable, *args], cwd=repo, capture_output=True, text=True, check=False)
```

### `FinalGovernanceTests` — `Lines 21–107`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `107` (`Lines 21–107`)
- **الوظيفة:** Cover new governance invariants independently of the previous 24 tests.
- **الكود الفعلي (`Lines 21–107`):**
```python
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
```

### `FinalGovernanceTests.setUp` — `Lines 24–28`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `24` إلى السطر `28` (`Lines 24–28`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 24–28`):**
```python
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="agd-governance-final-")
        self.addCleanup(self.tmp.cleanup)
        self.repo = Path(self.tmp.name) / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns("__pycache__", ".venv", ".git", "*.pyc"))
```

### `FinalGovernanceTests.test_document_tampering_detected` — `Lines 30–35`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `35` (`Lines 30–35`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 30–35`):**
```python
    def test_document_tampering_detected(self):
        p = self.repo / "AGENTS.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nUnrecorded documentation edit.\n", encoding="utf-8")
        v = run(self.repo, "tools/governance/change_tracking.py", "verify")
        self.assertNotEqual(v.returncode, 0)
        self.assertIn("Stale or unauthorized Markdown provenance", v.stdout)
```

### `FinalGovernanceTests.test_malformed_source_region_detected` — `Lines 37–42`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `42` (`Lines 37–42`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 37–42`):**
```python
    def test_malformed_source_region_detected(self):
        p = self.repo / "make_project_zip.py"
        p.write_text(p.read_text(encoding="utf-8") + "\n# START CHANGE TASK-ERR | 2026-10-17T08:00:00Z | CREATED | Author: agent\n", encoding="utf-8")
        v = run(self.repo, "tools/governance/change_tracking.py", "verify")
        self.assertNotEqual(v.returncode, 0)
        self.assertIn("unterminated START CHANGE", v.stdout)
```

### `FinalGovernanceTests.test_created_then_edited_document` — `Lines 44–58`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `58` (`Lines 44–58`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–58`):**
```python
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
```

### `FinalGovernanceTests.add_synthetic_reports` — `Lines 60–65`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `60` إلى السطر `65` (`Lines 60–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 60–65`):**
```python
    def add_synthetic_reports(self):
        # Test fixture only: these self-declared metrics are NOT scientific evidence or owner identity.
        for i in range(1, 6):
            path = self.repo / "docs" / "architecture" / "experiments" / f"EXP-0{i}_report.json"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({"experiment_id":f"EXP-0{i}", "status":"EXPERIMENTALLY_VALIDATED", "pass_criteria_met":True, "benchmark_assets_tested":["synthetic"], "measured_metrics":{"iou":0.99}}), encoding="utf-8")
```

### `FinalGovernanceTests.approve` — `Lines 67–68`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `67` إلى السطر `68` (`Lines 67–68`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 67–68`):**
```python
    def approve(self):
        return run(self.repo, "tools/memory_guard/manage_approvals.py", "authorize", "--confirm-owner-authorized", "--by", "FixtureOwner", "--note", "Synthetic end-to-end regression; not real owner consent")
```

### `FinalGovernanceTests.test_approval_transition_all_validators` — `Lines 70–78`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `70` إلى السطر `78` (`Lines 70–78`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 70–78`):**
```python
    def test_approval_transition_all_validators(self):
        self.add_synthetic_reports()
        result = self.approve()
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        for rel in ["tools/governance/change_tracking.py", "tools/memory_guard/verify_brain_sync.py", "tools/findings_guard/manage_findings.py", "tools/project_catalog/verify_catalog.py"]:
            args=[rel, "verify"] if rel.endswith("manage_findings.py") or rel.endswith("change_tracking.py") else [rel]
            check=run(self.repo,*args)
            self.assertEqual(check.returncode, 0, rel+": "+check.stdout+check.stderr)
        self.assertFalse((self.repo / "memory/decisions/.approval_tx_journal.json").exists())
```

### `FinalGovernanceTests.test_failed_approval_rolls_back` — `Lines 80–90`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `80` إلى السطر `90` (`Lines 80–90`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 80–90`):**
```python
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
```

### `FinalGovernanceTests.test_lock_serializes_cooperative_processes` — `Lines 92–107`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `92` إلى السطر `107` (`Lines 92–107`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 92–107`):**
```python
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
```
