# START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED | Author: orchestrator-planner
"""Baseline registry, state management, and export history tracking."""

from __future__ import annotations
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
import json
import subprocess

from .models import BaselineInventory, FileRecord
from .scanner import WorkspaceScanner, compute_bytes_sha256


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
# END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED
