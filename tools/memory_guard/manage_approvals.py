#!/usr/bin/env python3
"""Single Authoritative Approval State & Controlled Transition Manager.

Maintains memory/decisions/OWNER_APPROVAL_PROVENANCE.json as the single authoritative
approval registry across the repository and supports controlled, evidence-backed
owner approval transitions without weakening validator rules.

IMPORTANT GOVERNANCE BOUNDARY:
A syntactically valid approval record proves technical preconditions (completed
feasibility experiment reports, chained historical baselines, and cross-document
synchronization), NOT cryptographic human identity. Autonomous AI agents are
strictly forbidden from invoking `authorize` on the owner's behalf; only the
human owner (or an explicitly user-confirmed command passing --confirm-owner-authorized)
may execute an approval transition.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import shutil
import sys

# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED | Author: Governance maintainer
import base64
import os
import subprocess
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "findings_guard"))
from file_lock import repository_lock
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
PROV_PATH = ROOT / "memory" / "decisions" / "OWNER_APPROVAL_PROVENANCE.json"
INIT_BASE_PATH = ROOT / "docs" / "history" / "immutable_baselines" / "OWNER_APPROVAL_PROVENANCE.baseline.json"
HIST_DIR = ROOT / "docs" / "history" / "immutable_baselines"
APP_BASE_PATH = HERE / "approval_baseline.json"


def sha256_file(path: Path) -> str:
    """Compute hex SHA-256 of a file."""
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_experiment_report(exp_rel: str) -> tuple[bool, str, str]:
    """Validate that a required feasibility experiment report exists and passed quantitative gates."""
    p = ROOT / exp_rel
    if not p.is_file():
        return False, f"Missing required feasibility experiment report: {exp_rel}", ""
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except Exception as exc:
        return False, f"Invalid JSON in experiment report {exp_rel}: {exc}", ""
    if data.get("status") != "EXPERIMENTALLY_VALIDATED" or data.get("pass_criteria_met") is not True:
        return False, f"Experiment report {exp_rel} has not passed quantitative gates (status={data.get('status')})", ""
    if not data.get("measured_metrics") or not data.get("benchmark_assets_tested"):
        return False, f"Experiment report {exp_rel} is missing measured_metrics or benchmark_assets_tested", ""
    return True, "", sha256_file(p)


def _apply_architecture_transition(owner_by: str, owner_note: str) -> dict:
    """Execute a controlled, evidence-backed transition to OWNER_APPROVED across authoritative docs."""
    app_base = json.loads(APP_BASE_PATH.read_text(encoding="utf-8"))
    req_reports = app_base.get("required_experiment_reports_before_approval", [])
    validated_reports: dict[str, str] = {}
    for rep_rel in req_reports:
        ok, err, rep_sha = validate_experiment_report(rep_rel)
        if not ok:
            raise SystemExit(f"PRECONDITION_FAILED: {err}")
        validated_reports[rep_rel] = rep_sha

    prov = json.loads(PROV_PATH.read_text(encoding="utf-8"))
    prev_rev = prov.get("revision_no", 0)
    new_rev = prev_rev + 1
    prev_sha = sha256_file(PROV_PATH)

    # Archive current provenance file before mutating
    archive_name = f"OWNER_APPROVAL_PROVENANCE.rev{prev_rev:04d}.baseline.json"
    archive_path = HIST_DIR / archive_name
    shutil.copy2(PROV_PATH, archive_path)

    now_iso = datetime.now(timezone.utc).isoformat()
    auth_id = f"OWN-AUTH-REV-{new_rev:04d}"

    prov["revision_no"] = new_rev
    prov["current_project_stage"] = "ARCHITECTURE_APPROVED_READY_FOR_P0"
    prov["architecture_approval_status"] = "OWNER_APPROVED"
    prov["p0_implementation_gate"] = "OWNER_APPROVED"
    prov["approved_architecture_decisions"] = ["ADR-001", "ADR-002", "ADR-003", "ADR-004", "ADR-007"]
    prov["approved_feasibility_experiments"] = ["EXP-01", "EXP-02", "EXP-03", "EXP-04", "EXP-05"]
    prov["unapproved_technical_proposals"] = []
    prov.setdefault("approval_revision_history", []).append({
        "authorization_id": auth_id,
        "revision_no": new_rev,
        "authorized_at": now_iso,
        "owner_identifier": owner_by,
        "owner_confirmation_note": owner_note,
        "previous_provenance_sha256": prev_sha,
        "archived_prior_baseline": f"docs/history/immutable_baselines/{archive_name}",
        "validated_experiment_reports": validated_reports,
    })
    PROV_PATH.write_text(json.dumps(prov, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    # Synchronize DECISION_LOG.md, MASTER_PLAN.md, and CURRENT_TASK_CHECKPOINT.md
    for doc_rel in [
        "memory/decisions/DECISION_LOG.md",
        "MASTER_PLAN.md",
        "memory/session/CURRENT_TASK_CHECKPOINT.md",
    ]:
        dp = ROOT / doc_rel
        txt = dp.read_text(encoding="utf-8")
        txt = txt.replace(
            "`PROJECT_STAGE`: `ARCHITECTURE_AND_GOVERNANCE_PREPARATION`",
            "`PROJECT_STAGE`: `ARCHITECTURE_APPROVED_READY_FOR_P0`",
        ).replace(
            "**المرحلة (`Project Stage`):** `ARCHITECTURE_AND_GOVERNANCE_PREPARATION`",
            "**المرحلة (`Project Stage`):** `ARCHITECTURE_APPROVED_READY_FOR_P0`",
        ).replace(
            "**المرحلة الحالية للمشروع (`Project Stage`):** `ARCHITECTURE_AND_GOVERNANCE_PREPARATION`",
            "**المرحلة الحالية للمشروع (`Project Stage`):** `ARCHITECTURE_APPROVED_READY_FOR_P0`",
        ).replace(
            "`ARCHITECTURE_APPROVAL_STATUS`: `NOT_APPROVED` (`PROPOSED_ONLY`)",
            f"`ARCHITECTURE_APPROVAL_STATUS`: `OWNER_APPROVED` (`{auth_id}`)",
        ).replace(
            "**حالة اعتماد المعمارية (`Architecture Approval Status`):** `NOT_APPROVED` (`PROPOSED_ONLY` — بانتظار مراجعة المالك وتجارب الجدوى).",
            f"**حالة اعتماد المعمارية (`Architecture Approval Status`):** `OWNER_APPROVED` (`{auth_id}`).",
        ).replace(
            "**حالة اعتماد المعمارية (`Architecture Approval Status`):** `NOT_APPROVED` (`PROPOSED_ONLY`)",
            f"**حالة اعتماد المعمارية (`Architecture Approval Status`):** `OWNER_APPROVED` (`{auth_id}`)",
        ).replace(
            "`P0_IMPLEMENTATION_GATE`: `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_EXPERIMENTS`",
            f"`P0_IMPLEMENTATION_GATE`: `OWNER_APPROVED` (`{auth_id}`)",
        ).replace(
            "**بوابة المرحلة التأسيسية (`P0 Implementation Gate`):** `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_EXPERIMENTS`.",
            f"**بوابة المرحلة التأسيسية (`P0 Implementation Gate`):** `OWNER_APPROVED` (`{auth_id}`).",
        ).replace(
            "**بوابة تنفيذ المنتج (`P0 Implementation Gate`):** `BLOCKED_PENDING_OWNER_APPROVAL_AND_FEASIBILITY_EXPERIMENTS`",
            f"**بوابة تنفيذ المنتج (`P0 Implementation Gate`):** `OWNER_APPROVED` (`{auth_id}`)",
        )
        if doc_rel == "memory/decisions/DECISION_LOG.md":
            for adr in ["ADR-001", "ADR-002", "ADR-003", "ADR-004", "ADR-007"]:
                txt = re.sub(
                    rf"^(\|\s*`{adr}`\s*\|[^\n]*?)`NOT_APPROVED`([^\n]*)$",
                    rf"\1`OWNER_APPROVED` (`{auth_id}`)\2",
                    txt,
                    flags=re.M,
                )
        dp.write_text(txt, encoding="utf-8")

    # If DECISION_LOG.md is a promoted finding target, record its authorized document revision so promotion snapshots remain intact
    import subprocess
    subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools" / "findings_guard" / "manage_findings.py"),
            "record-doc-revision",
            "--file",
            "memory/decisions/DECISION_LOG.md",
            "--author",
            owner_by,
            "--reason",
            f"Controlled owner architecture approval transition {auth_id}",
            "--superseding-finding",
            auth_id,
        ],
        cwd=str(ROOT),
        check=True,
    )

    return {
        "status": "TRANSITION_AUTHORIZED",
        "authorization_id": auth_id,
        "revision_no": new_rev,
        "validated_reports_count": len(validated_reports),
    }


# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED | Author: Governance maintainer
TX_JOURNAL = ROOT / "memory" / "decisions" / ".approval_tx_journal.json"


def _snapshot_repository() -> dict[str, str]:
    """Capture first-party bytes before any authorization write for deterministic rollback."""
    omitted = {".git", "node_modules", "__pycache__", ".venv", "packages", "latest", "baselines"}
    result = {}
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == TX_JOURNAL:
            continue
        rel = path.relative_to(ROOT)
        if any(part in omitted for part in rel.parts[:-1]):
            continue
        result[rel.as_posix()] = base64.b64encode(path.read_bytes()).decode("ascii")
    return result


def _restore_repository_snapshot(snapshot: dict[str, str]) -> None:
    """Restore tracked files and remove files created during the interrupted transition."""
    prior = set(snapshot)
    current = _snapshot_repository()
    for rel in current.keys() - prior:
        (ROOT / rel).unlink()
    for rel, encoded in snapshot.items():
        dest = (ROOT / rel).resolve()
        if not dest.is_relative_to(ROOT.resolve()):
            raise RuntimeError("Unsafe approval recovery path")
        original = base64.b64decode(encoded)
        if not dest.is_file() or dest.read_bytes() != original:
            dest.parent.mkdir(parents=True, exist_ok=True)
            tmp = dest.with_name(dest.name + ".approval-restore.tmp")
            tmp.write_bytes(original)
            os.replace(tmp, dest)


def recover_approval_transaction() -> dict:
    """Rollback an interrupted multi-file approval using its durable in-repository journal."""
    with repository_lock(ROOT, "approval"):
        if not TX_JOURNAL.is_file():
            return {"status": "NO_PENDING_TRANSACTION"}
        journal = json.loads(TX_JOURNAL.read_text(encoding="utf-8"))
        _restore_repository_snapshot(journal["previous_files"])
        TX_JOURNAL.unlink()
        return {"status": "ROLLED_BACK_CLEAN", "transaction_started": journal["started_at"]}


def _validated_run(script: str, *args: str) -> None:
    cmd = [sys.executable, str(ROOT / script), *args]
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, check=False)
    if result.returncode:
        raise RuntimeError(f"Validation failed: {script}: {result.stdout} {result.stderr}")


def authorize_architecture_transition(owner_by: str, owner_note: str) -> dict:
    """Fail closed and rollback if ANY post-approval validator or catalog rebuild fails.

    Approval identity remains an external human/host trust boundary; CLI flag is
    a declaration only. The transaction does not validate scientific authenticity.
    """
    with repository_lock(ROOT, "approval"):
        if TX_JOURNAL.is_file():
            raise RuntimeError("Pending approval transaction; run recover-tx first")
        prior = _snapshot_repository()
        journal = {
            "started_at": datetime.now(timezone.utc).isoformat(),
            "previous_files": prior,
        }
        TX_JOURNAL.write_text(json.dumps(journal, ensure_ascii=False), encoding="utf-8")
        try:
            result = _apply_architecture_transition(owner_by, owner_note)
            # START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED | Author: Governance maintainer
            # Update Markdown timestamps atomically with architecture approval.
            sys.path.insert(0, str(ROOT / "tools" / "governance"))
            import change_tracking as ct
            ct.edit_document("MASTER_PLAN.md", "EDITED", "OWNER-AUTH-TRANSITION", owner_by)
            # END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED
            # Generated, newly created reports and provenance archives must all be cataloged.
            _validated_run("tools/project_catalog/build_catalog.py", "--write")
            _validated_run("tools/memory_guard/verify_brain_sync.py")
            _validated_run("tools/findings_guard/manage_findings.py", "verify")
            _validated_run("tools/project_catalog/verify_catalog.py")
        except BaseException:
            _restore_repository_snapshot(prior)
            TX_JOURNAL.unlink(missing_ok=True)
            raise
        TX_JOURNAL.unlink()
        return result
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED


def main() -> None:
    """CLI entrypoint for manage_approvals.py."""
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    if cmd == "recover-tx":
        print(json.dumps(recover_approval_transaction(), ensure_ascii=False))
    elif cmd == "authorize":
        if "--confirm-owner-authorized" not in sys.argv:
            raise SystemExit(
                "REFUSED: Autonomous approval is prohibited. Require explicit --confirm-owner-authorized flag."
            )
        by = sys.argv[sys.argv.index("--by") + 1] if "--by" in sys.argv else ""
        note = sys.argv[sys.argv.index("--note") + 1] if "--note" in sys.argv else ""
        if not by.strip() or not note.strip():
            raise SystemExit("REFUSED: Both --by <owner> and --note <reason> are required.")
        res = authorize_architecture_transition(by.strip(), note.strip())
        print(json.dumps(res, ensure_ascii=False))
    else:
        prov = json.loads(PROV_PATH.read_text(encoding="utf-8"))
        print(json.dumps(prov, ensure_ascii=False))


if __name__ == "__main__":
    main()
