# مرآة الكود التفصيلية: `tools/update_packages/state_manager.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/state_manager.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/state_manager.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `183` (`Lines 1–183`)
- **بصمة الملف (`SHA-256`):** `6bd01c996a15310dbd1b97f8f398fae17d6f13d78577a29bb5e4ad1720b47a47`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `UpdateStateManager` | `class` | `Lines 15–182` | `class UpdateStateManager:` | Manages baseline snapshots, acknowledged states, and export history. |
| `UpdateStateManager.__init__` | `method` | `Lines 18–25` | `def __init__(self, workspace_root: Path, registry_dir: Optional[Path] = None):` | رمز برمجي موثق. |
| `UpdateStateManager._ensure_state_file` | `method` | `Lines 27–37` | `def _ensure_state_file(self) -> None:` | رمز برمجي موثق. |
| `UpdateStateManager._read_state` | `method` | `Lines 40–50` | `def _read_state(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `UpdateStateManager._write_state` | `method` | `Lines 52–54` | `def _write_state(self, state: Dict[str, Any]) -> None:` | رمز برمجي موثق. |
| `UpdateStateManager.get_git_commit` | `method` | `Lines 57–72` | `def get_git_commit(self) -> Optional[str]:` | Detect current Git HEAD commit if git repository is active and trustworthy. |
| `UpdateStateManager.initialize_baseline` | `method` | `Lines 74–108` | `def initialize_baseline(self, baseline_id: Optional[str] = None) -> BaselineInventory:` | Scan workspace and persist a new baseline inventory. |
| `UpdateStateManager.save_baseline` | `method` | `Lines 111–115` | `def save_baseline(self, inventory: BaselineInventory) -> None:` | Persist an existing or updated baseline inventory to disk. |
| `UpdateStateManager.get_baseline` | `method` | `Lines 119–128` | `def get_baseline(self, baseline_id: str) -> Optional[BaselineInventory]:` | Load an existing baseline inventory by ID. |
| `UpdateStateManager.get_active_baseline` | `method` | `Lines 130–136` | `def get_active_baseline(self) -> Optional[BaselineInventory]:` | Retrieve the currently designated active baseline. |
| `UpdateStateManager.acknowledge_baseline` | `method` | `Lines 138–161` | `def acknowledge_baseline(self, baseline_id: str, acknowledged_by: str = "Owner", note: str = "Acknowledged") -> Dict[str, Any]:` | Explicitly record user or owner acknowledgment of a baseline. |
| `UpdateStateManager.record_export` | `method` | `Lines 163–167` | `def record_export(self, export_record: Dict[str, Any]) -> None:` | Record an exported package into the state history without advancing baseline automatically. |
| `UpdateStateManager.record_application` | `method` | `Lines 169–173` | `def record_application(self, application_record: Dict[str, Any]) -> None:` | Record an applied package into the state history. |
| `UpdateStateManager.get_next_sequence_number` | `method` | `Lines 175–178` | `def get_next_sequence_number(self) -> int:` | Calculate next package sequence number. |
| `UpdateStateManager.list_history` | `method` | `Lines 180–182` | `def list_history(self) -> Dict[str, Any]:` | Return complete state and export history. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `UpdateStateManager` — `Lines 15–182`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `182` (`Lines 15–182`)
- **الوظيفة:** Manages baseline snapshots, acknowledged states, and export history.
- **الكود الفعلي (`Lines 15–182`):**
```python
class UpdateStateManager:
    """Manages baseline snapshots, acknowledged states, and export history."""

    def __init__(self, workspace_root: Path, registry_dir: Optional[Path] = None):
        self.workspace_root = workspace_root.resolve()
        self.registry_dir = (registry_dir or (self.workspace_root / "tools" / "update_packages" / "registry")).resolve()
        self.baselines_dir = self.registry_dir / "baselines"
        self.state_file = self.registry_dir / "update_state.json"

        self.baselines_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_state_file()

    def _ensure_state_file(self) -> None:
        if not self.state_file.exists():
            initial_state = {
                "active_baseline_id": None,
                "acknowledged_baseline_id": None,
                "acknowledgment_history": [],
                "export_history": [],
                "application_history": []
            }
            # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
            self.state_file.write_bytes((json.dumps(initial_state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
            # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

    def _read_state(self) -> Dict[str, Any]:
        try:
            return json.loads(self.state_file.read_text(encoding="utf-8"))
        except Exception:
            return {
                "active_baseline_id": None,
                "acknowledged_baseline_id": None,
                "acknowledgment_history": [],
                "export_history": [],
                "application_history": []
            }

    def _write_state(self, state: Dict[str, Any]) -> None:
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        self.state_file.write_bytes((json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

    def get_git_commit(self) -> Optional[str]:
        """Detect current Git HEAD commit if git repository is active and trustworthy."""
        try:
            res = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=str(self.workspace_root),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout.strip()
        except Exception:
            pass
        return None

    def initialize_baseline(self, baseline_id: Optional[str] = None) -> BaselineInventory:
        """Scan workspace and persist a new baseline inventory."""
        now_utc = datetime.now(timezone.utc)
        if not baseline_id:
            ts = now_utc.strftime("%Y%m%dT%H%M%SZ")
            baseline_id = f"BASE_{ts}"

        scanner = WorkspaceScanner(self.workspace_root)
        files = scanner.scan()
        git_commit = self.get_git_commit()

        inventory = BaselineInventory(
            baseline_id=baseline_id,
            repo_identity="AI Graphic Designer",
            created_at_utc=now_utc.isoformat(),
            tool_version="1.0.0",
            schema_version="1.0.0",
            git_commit=git_commit,
            inclusion_policy="tracked_first_party",
            exclusion_policy="standard_anti_leak",
            files=files
        )

        baseline_file = self.baselines_dir / f"{baseline_id}.json"
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        baseline_file.write_bytes(inventory.to_json().encode("utf-8"))
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

        state = self._read_state()
        state["active_baseline_id"] = baseline_id
        if not state.get("acknowledged_baseline_id"):
            state["acknowledged_baseline_id"] = baseline_id
        self._write_state(state)

        return inventory

    # START CHANGE TASK-UPDATE-SYS-CORRECTION-01 | 2026-10-18T02:00:00Z | CREATED | Author: orchestrator-planner
    def save_baseline(self, inventory: BaselineInventory) -> None:
        """Persist an existing or updated baseline inventory to disk."""
        baseline_file = self.baselines_dir / f"{inventory.baseline_id}.json"
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        baseline_file.write_bytes(inventory.to_json().encode("utf-8"))
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED
    # END CHANGE TASK-UPDATE-SYS-CORRECTION-01 | 2026-10-18T02:00:00Z | CREATED

    def get_baseline(self, baseline_id: str) -> Optional[BaselineInventory]:
        """Load an existing baseline inventory by ID."""
        baseline_file = self.baselines_dir / f"{baseline_id}.json"
        if not baseline_file.exists():
            return None
        try:
            data = json.loads(baseline_file.read_text(encoding="utf-8"))
            return BaselineInventory.from_dict(data)
        except Exception:
            return None

    def get_active_baseline(self) -> Optional[BaselineInventory]:
        """Retrieve the currently designated active baseline."""
        state = self._read_state()
        base_id = state.get("active_baseline_id") or state.get("acknowledged_baseline_id")
        if not base_id:
            return None
        return self.get_baseline(base_id)

    def acknowledge_baseline(self, baseline_id: str, acknowledged_by: str = "Owner", note: str = "Acknowledged") -> Dict[str, Any]:
        """Explicitly record user or owner acknowledgment of a baseline."""
        inventory = self.get_baseline(baseline_id)
        if not inventory:
            raise FileNotFoundError(f"Baseline not found: {baseline_id}")

        now_utc = datetime.now(timezone.utc).isoformat()
        state = self._read_state()
        state["acknowledged_baseline_id"] = baseline_id
        state["active_baseline_id"] = baseline_id
        state.setdefault("acknowledgment_history", []).append({
            "baseline_id": baseline_id,
            "acknowledged_by": acknowledged_by,
            "note": note,
            "acknowledged_at_utc": now_utc
        })
        self._write_state(state)

        return {
            "status": "ACKNOWLEDGED",
            "baseline_id": baseline_id,
            "acknowledged_by": acknowledged_by,
            "acknowledged_at_utc": now_utc
        }

    def record_export(self, export_record: Dict[str, Any]) -> None:
        """Record an exported package into the state history without advancing baseline automatically."""
        state = self._read_state()
        state.setdefault("export_history", []).append(export_record)
        self._write_state(state)

    def record_application(self, application_record: Dict[str, Any]) -> None:
        """Record an applied package into the state history."""
        state = self._read_state()
        state.setdefault("application_history", []).append(application_record)
        self._write_state(state)

    def get_next_sequence_number(self) -> int:
        """Calculate next package sequence number."""
        state = self._read_state()
        return len(state.get("export_history", [])) + 1

    def list_history(self) -> Dict[str, Any]:
        """Return complete state and export history."""
        return self._read_state()
```

### `UpdateStateManager.__init__` — `Lines 18–25`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `18` إلى السطر `25` (`Lines 18–25`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 18–25`):**
```python
    def __init__(self, workspace_root: Path, registry_dir: Optional[Path] = None):
        self.workspace_root = workspace_root.resolve()
        self.registry_dir = (registry_dir or (self.workspace_root / "tools" / "update_packages" / "registry")).resolve()
        self.baselines_dir = self.registry_dir / "baselines"
        self.state_file = self.registry_dir / "update_state.json"

        self.baselines_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_state_file()
```

### `UpdateStateManager._ensure_state_file` — `Lines 27–37`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `37` (`Lines 27–37`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 27–37`):**
```python
    def _ensure_state_file(self) -> None:
        if not self.state_file.exists():
            initial_state = {
                "active_baseline_id": None,
                "acknowledged_baseline_id": None,
                "acknowledgment_history": [],
                "export_history": [],
                "application_history": []
            }
            # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
            self.state_file.write_bytes((json.dumps(initial_state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
```

### `UpdateStateManager._read_state` — `Lines 40–50`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `40` إلى السطر `50` (`Lines 40–50`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 40–50`):**
```python
    def _read_state(self) -> Dict[str, Any]:
        try:
            return json.loads(self.state_file.read_text(encoding="utf-8"))
        except Exception:
            return {
                "active_baseline_id": None,
                "acknowledged_baseline_id": None,
                "acknowledgment_history": [],
                "export_history": [],
                "application_history": []
            }
```

### `UpdateStateManager._write_state` — `Lines 52–54`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `52` إلى السطر `54` (`Lines 52–54`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 52–54`):**
```python
    def _write_state(self, state: Dict[str, Any]) -> None:
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        self.state_file.write_bytes((json.dumps(state, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
```

### `UpdateStateManager.get_git_commit` — `Lines 57–72`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `72` (`Lines 57–72`)
- **الوظيفة:** Detect current Git HEAD commit if git repository is active and trustworthy.
- **الكود الفعلي (`Lines 57–72`):**
```python
    def get_git_commit(self) -> Optional[str]:
        """Detect current Git HEAD commit if git repository is active and trustworthy."""
        try:
            res = subprocess.run(
                ["git", "rev-parse", "HEAD"],
                cwd=str(self.workspace_root),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if res.returncode == 0 and res.stdout.strip():
                return res.stdout.strip()
        except Exception:
            pass
        return None
```

### `UpdateStateManager.initialize_baseline` — `Lines 74–108`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `74` إلى السطر `108` (`Lines 74–108`)
- **الوظيفة:** Scan workspace and persist a new baseline inventory.
- **الكود الفعلي (`Lines 74–108`):**
```python
    def initialize_baseline(self, baseline_id: Optional[str] = None) -> BaselineInventory:
        """Scan workspace and persist a new baseline inventory."""
        now_utc = datetime.now(timezone.utc)
        if not baseline_id:
            ts = now_utc.strftime("%Y%m%dT%H%M%SZ")
            baseline_id = f"BASE_{ts}"

        scanner = WorkspaceScanner(self.workspace_root)
        files = scanner.scan()
        git_commit = self.get_git_commit()

        inventory = BaselineInventory(
            baseline_id=baseline_id,
            repo_identity="AI Graphic Designer",
            created_at_utc=now_utc.isoformat(),
            tool_version="1.0.0",
            schema_version="1.0.0",
            git_commit=git_commit,
            inclusion_policy="tracked_first_party",
            exclusion_policy="standard_anti_leak",
            files=files
        )

        baseline_file = self.baselines_dir / f"{baseline_id}.json"
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        baseline_file.write_bytes(inventory.to_json().encode("utf-8"))
        # END CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED

        state = self._read_state()
        state["active_baseline_id"] = baseline_id
        if not state.get("acknowledged_baseline_id"):
            state["acknowledged_baseline_id"] = baseline_id
        self._write_state(state)

        return inventory
```

### `UpdateStateManager.save_baseline` — `Lines 111–115`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `111` إلى السطر `115` (`Lines 111–115`)
- **الوظيفة:** Persist an existing or updated baseline inventory to disk.
- **الكود الفعلي (`Lines 111–115`):**
```python
    def save_baseline(self, inventory: BaselineInventory) -> None:
        """Persist an existing or updated baseline inventory to disk."""
        baseline_file = self.baselines_dir / f"{inventory.baseline_id}.json"
        # START CHANGE TASK-UPDATE-SYS-DEFECTS-01 | 2026-10-18T07:57:00Z | EDITED | Author: orchestrator-planner
        baseline_file.write_bytes(inventory.to_json().encode("utf-8"))
```

### `UpdateStateManager.get_baseline` — `Lines 119–128`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `119` إلى السطر `128` (`Lines 119–128`)
- **الوظيفة:** Load an existing baseline inventory by ID.
- **الكود الفعلي (`Lines 119–128`):**
```python
    def get_baseline(self, baseline_id: str) -> Optional[BaselineInventory]:
        """Load an existing baseline inventory by ID."""
        baseline_file = self.baselines_dir / f"{baseline_id}.json"
        if not baseline_file.exists():
            return None
        try:
            data = json.loads(baseline_file.read_text(encoding="utf-8"))
            return BaselineInventory.from_dict(data)
        except Exception:
            return None
```

### `UpdateStateManager.get_active_baseline` — `Lines 130–136`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `130` إلى السطر `136` (`Lines 130–136`)
- **الوظيفة:** Retrieve the currently designated active baseline.
- **الكود الفعلي (`Lines 130–136`):**
```python
    def get_active_baseline(self) -> Optional[BaselineInventory]:
        """Retrieve the currently designated active baseline."""
        state = self._read_state()
        base_id = state.get("active_baseline_id") or state.get("acknowledged_baseline_id")
        if not base_id:
            return None
        return self.get_baseline(base_id)
```

### `UpdateStateManager.acknowledge_baseline` — `Lines 138–161`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `138` إلى السطر `161` (`Lines 138–161`)
- **الوظيفة:** Explicitly record user or owner acknowledgment of a baseline.
- **الكود الفعلي (`Lines 138–161`):**
```python
    def acknowledge_baseline(self, baseline_id: str, acknowledged_by: str = "Owner", note: str = "Acknowledged") -> Dict[str, Any]:
        """Explicitly record user or owner acknowledgment of a baseline."""
        inventory = self.get_baseline(baseline_id)
        if not inventory:
            raise FileNotFoundError(f"Baseline not found: {baseline_id}")

        now_utc = datetime.now(timezone.utc).isoformat()
        state = self._read_state()
        state["acknowledged_baseline_id"] = baseline_id
        state["active_baseline_id"] = baseline_id
        state.setdefault("acknowledgment_history", []).append({
            "baseline_id": baseline_id,
            "acknowledged_by": acknowledged_by,
            "note": note,
            "acknowledged_at_utc": now_utc
        })
        self._write_state(state)

        return {
            "status": "ACKNOWLEDGED",
            "baseline_id": baseline_id,
            "acknowledged_by": acknowledged_by,
            "acknowledged_at_utc": now_utc
        }
```

### `UpdateStateManager.record_export` — `Lines 163–167`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `163` إلى السطر `167` (`Lines 163–167`)
- **الوظيفة:** Record an exported package into the state history without advancing baseline automatically.
- **الكود الفعلي (`Lines 163–167`):**
```python
    def record_export(self, export_record: Dict[str, Any]) -> None:
        """Record an exported package into the state history without advancing baseline automatically."""
        state = self._read_state()
        state.setdefault("export_history", []).append(export_record)
        self._write_state(state)
```

### `UpdateStateManager.record_application` — `Lines 169–173`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `169` إلى السطر `173` (`Lines 169–173`)
- **الوظيفة:** Record an applied package into the state history.
- **الكود الفعلي (`Lines 169–173`):**
```python
    def record_application(self, application_record: Dict[str, Any]) -> None:
        """Record an applied package into the state history."""
        state = self._read_state()
        state.setdefault("application_history", []).append(application_record)
        self._write_state(state)
```

### `UpdateStateManager.get_next_sequence_number` — `Lines 175–178`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `175` إلى السطر `178` (`Lines 175–178`)
- **الوظيفة:** Calculate next package sequence number.
- **الكود الفعلي (`Lines 175–178`):**
```python
    def get_next_sequence_number(self) -> int:
        """Calculate next package sequence number."""
        state = self._read_state()
        return len(state.get("export_history", [])) + 1
```

### `UpdateStateManager.list_history` — `Lines 180–182`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `180` إلى السطر `182` (`Lines 180–182`)
- **الوظيفة:** Return complete state and export history.
- **الكود الفعلي (`Lines 180–182`):**
```python
    def list_history(self) -> Dict[str, Any]:
        """Return complete state and export history."""
        return self._read_state()
```
