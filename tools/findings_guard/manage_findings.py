#!/usr/bin/env python3
"""Transactional Subagent Findings Lifecycle, Document Revision & 5-Way Reconciliation Engine.

Provides validated, concurrency-safe, crash-recoverable lifecycle operations:
  - capture: Create a new isolated subagent finding + isolated subagent WAL entry.
  - submit: Submit a captured finding to PENDING_PARENT_REVIEW.
  - review / approve / reject: Append an immutable parent review event (rejecting self-approval
    and duplicate event submissions).
  - promote: Promote an APPROVED_FOR_PROMOTION finding into a target document, creating an
    immutable snapshot in docs/history/promoted_targets/ and updating manifests & ledgers.
  - record-doc-revision: Authorize a legitimate subsequent revision to an already-promoted
    document (preserving the original promotion snapshot and verifying that all previously
    promoted verbatim blocks remain intact or are explicitly superseded with preserved history).
  - recover-tx: Roll back any uncommitted interrupted transaction recorded in .tx_journal.json.
  - compile-ledger: Compile memory/findings/FINDINGS_LEDGER.md from isolated entries.
  - verify: Run 5-way inventory reconciliation, promotion content integrity, and revision checks.
"""
from pathlib import Path
from datetime import datetime, timezone
import contextlib
import hashlib
import json
import os
import re
import shutil
import sys

# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | EDITED | Author: Governance maintainer
from file_lock import repository_lock
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | EDITED

ROOT = Path(__file__).resolve().parents[2]
FINDINGS_DIR = ROOT / "memory" / "findings"
ENTRIES_DIR = FINDINGS_DIR / "entries"
LEDGER_PATH = FINDINGS_DIR / "FINDINGS_LEDGER.md"
MANIFEST_PATH = FINDINGS_DIR / "findings_manifest.json"
DOC_REV_MANIFEST_PATH = FINDINGS_DIR / "document_revisions_manifest.json"
BASELINE_MANIFEST_PATH = ROOT / "docs" / "history" / "immutable_baselines" / "findings_manifest.baseline.json"
LOCKS_PATH = FINDINGS_DIR / "subagent_ownership_locks.json"
TX_JOURNAL_PATH = FINDINGS_DIR / ".tx_journal.json"

VALID_CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
VALID_STATES = {
    "CAPTURED",
    "PENDING_PARENT_REVIEW",
    "APPROVED_FOR_PROMOTION",
    "PROMOTED",
    "REJECTED",
    "NEEDS_REVISION",
}
REQUIRED_FINDING_KEYS = {
    "finding_id",
    "task_id",
    "subagent_id",
    "created_at",
    "source_file_paths",
    "line_ranges",
    "source_revisions",
    "evidence",
    "confidence",
    "proposed_action",
    "current_approval_state",
    "review_events",
    "promotion_record",
}


def compute_file_sha256(rel_path: str) -> str:
    """Return hex SHA-256 of a repository file."""
    target = ROOT / rel_path
    if not target.is_file():
        return ""
    return hashlib.sha256(target.read_bytes()).hexdigest()


# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
def atomic_write_bytes(path: Path, data: bytes) -> None:
    """Atomically write raw bytes to path via a temporary sibling file and os.replace."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp.{os.getpid()}")
    tmp_path.write_bytes(data)
    os.replace(tmp_path, path)


def atomic_write_text(path: Path, content: str) -> None:
    """Atomically write UTF-8 text to path via a temporary sibling file and os.replace."""
    atomic_write_bytes(path, content.encode("utf-8"))
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED


# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | EDITED | Author: Governance maintainer
@contextlib.contextmanager
def transactional_operation(op_name: str, affected_rel_paths: list[str]):
    """Serialize lifecycle operations on all OSes; journal before changes."""
    FINDINGS_DIR.mkdir(parents=True, exist_ok=True)
    with repository_lock(ROOT, "findings"):
        if TX_JOURNAL_PATH.is_file():
            raise RuntimeError(
                "Uncommitted findings transaction journal (.tx_journal.json) detected! "
                "Run `manage_findings.py recover-tx` first."
            )
        backups: dict[str, str | None] = {}
        for rel in affected_rel_paths:
            p = ROOT / rel
            backups[rel] = p.read_text(encoding="utf-8") if p.is_file() else None
        journal = {
            "operation": op_name,
            "started_at": datetime.now(timezone.utc).isoformat(),
            "status": "IN_PROGRESS",
            "backups": backups,
        }
        atomic_write_text(TX_JOURNAL_PATH, json.dumps(journal, ensure_ascii=False, indent=2) + "\n")
        yield
        TX_JOURNAL_PATH.unlink(missing_ok=True)


def recover_interrupted_transaction() -> dict:
    """Recover findings transaction under the same cross-process exclusive lock."""
    FINDINGS_DIR.mkdir(parents=True, exist_ok=True)
    with repository_lock(ROOT, "findings"):
        if not TX_JOURNAL_PATH.is_file():
            return {"status": "NO_PENDING_TRANSACTION", "restored_files": [], "removed_files": []}
        journal = json.loads(TX_JOURNAL_PATH.read_text(encoding="utf-8"))
        restored: list[str] = []
        removed: list[str] = []
        for rel, prior_content in journal.get("backups", {}).items():
            target = (ROOT / rel).resolve()
            if not target.is_relative_to(ROOT.resolve()):
                raise RuntimeError(f"Unsafe recovery path outside repository: {rel}")
            if prior_content is None:
                if target.is_file():
                    target.unlink()
                    removed.append(rel)
            else:
                atomic_write_text(target, prior_content)
                restored.append(rel)
        TX_JOURNAL_PATH.unlink()
        return {
            "status": "ROLLED_BACK_CLEAN",
            "operation": journal.get("operation"),
            "restored_files": restored,
            "removed_files": removed,
        }
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | EDITED

def load_all_findings() -> list[tuple[Path, dict]]:
    """Load all isolated finding JSON files sorted by finding_id."""
    ENTRIES_DIR.mkdir(parents=True, exist_ok=True)
    records: list[tuple[Path, dict]] = []
    for p in sorted(ENTRIES_DIR.glob("*.json")):
        records.append((p, json.loads(p.read_text(encoding="utf-8"))))
    return records


def find_entry_by_id(finding_id: str) -> tuple[Path, dict]:
    """Locate a finding JSON file by its finding_id."""
    for path, fnd in load_all_findings():
        if fnd.get("finding_id") == finding_id:
            return path, fnd
    raise SystemExit(f"Finding not found: {finding_id}")


def capture_finding(
    finding_id: str,
    task_id: str,
    subagent_id: str,
    source_spec: str,
    evidence: str,
    confidence: str,
    proposed_action: str,
    simulate_interrupt: bool = False,
) -> dict:
    """Transactionally capture a new subagent finding in an isolated entry file and update manifest/ledger."""
    if confidence not in VALID_CONFIDENCE:
        raise SystemExit(f"Invalid confidence: {confidence}")
    # Check duplicate finding_id
    for _, existing in load_all_findings():
        if existing.get("finding_id") == finding_id:
            raise SystemExit(f"DUPLICATE_FINDING_ERROR: Finding '{finding_id}' already exists.")

    # Parse source_spec ("path:start-end,path2:start-end")
    src_paths: list[str] = []
    line_ranges: list[dict] = []
    src_revs: list[dict] = []
    for item in [s.strip() for s in source_spec.split(",") if s.strip()]:
        fpath, rng = item.split(":", 1)
        s_str, e_str = rng.split("-", 1)
        s_line, e_line = int(s_str), int(e_str)
        full_p = ROOT / fpath
        if not full_p.is_file():
            raise SystemExit(f"Source file does not exist: {fpath}")
        t_lines = len(full_p.read_text(encoding="utf-8").splitlines())
        if s_line < 1 or e_line < s_line or e_line > max(t_lines, 1):
            raise SystemExit(f"Invalid line range {s_line}..{e_line} for {fpath} (total {t_lines})")
        src_paths.append(fpath)
        line_ranges.append({"file": fpath, "start_line": s_line, "end_line": e_line})
        src_revs.append({"file": fpath, "sha256": compute_file_sha256(fpath)})

    entry_rel = f"memory/findings/entries/{task_id}__{subagent_id}__{finding_id}.json"
    wal_rel = f"memory/session/subagent_wals/{subagent_id}__{task_id}.wal.md"
    affected = [
        entry_rel,
        wal_rel,
        "memory/findings/findings_manifest.json",
        "memory/findings/FINDINGS_LEDGER.md",
    ]
    now_iso = datetime.now(timezone.utc).isoformat()
    fnd_obj = {
        "finding_id": finding_id,
        "task_id": task_id,
        "subagent_id": subagent_id,
        "created_at": now_iso,
        "source_file_paths": src_paths,
        "line_ranges": line_ranges,
        "source_revisions": src_revs,
        "evidence": evidence,
        "confidence": confidence,
        "proposed_action": proposed_action,
        "current_approval_state": "CAPTURED",
        "review_events": [],
        "promotion_record": None,
    }

    with transactional_operation(f"capture:{finding_id}", affected):
        atomic_write_text(ROOT / entry_rel, json.dumps(fnd_obj, ensure_ascii=False, indent=2) + "\n")
        if simulate_interrupt:
            raise RuntimeError("SIMULATED_INTERRUPTION_AFTER_ENTRY_WRITE")

        wal_p = ROOT / wal_rel
        if wal_p.is_file():
            wal_txt = wal_p.read_text(encoding="utf-8").rstrip() + f"\n- `[CAPTURE-{finding_id}]`: Recorded finding `{finding_id}` ({now_iso}).\n"
        else:
            wal_txt = (
                f"# سجل العمل المعزول للـ Sub-Agent (`{subagent_id}` — المهمة `{task_id}`)\n\n"
                f"- **الوكيل (`Subagent ID`):** `{subagent_id}`\n"
                f"- **المهمة (`Task ID`):** `{task_id}`\n\n"
                f"## سجل الخطوات الفورية (`Isolated Subagent WAL Entries`)\n"
                f"1. `[STEP-01]`: `[CAPTURE-{finding_id}]` Recorded finding `{finding_id}` ({now_iso}).\n"
            )
        atomic_write_text(wal_p, wal_txt)

        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        manifest["registered_findings"][finding_id] = {
            "finding_id": finding_id,
            "task_id": task_id,
            "subagent_id": subagent_id,
            "entry_file": entry_rel,
            "created_at": now_iso,
            "current_approval_state": "CAPTURED",
            "entry_sha256": compute_file_sha256(entry_rel),
            "deleted": False,
        }
        manifest.setdefault("audit_trail", []).append({
            "audit_id": f"FAUD-{len(manifest.get('audit_trail', [])) + 1:04d}",
            "timestamp": now_iso,
            "action": "CAPTURE",
            "finding_id": finding_id,
            "actor": subagent_id,
        })
        atomic_write_text(MANIFEST_PATH, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        compile_ledger()

    return {"status": "CAPTURED", "finding_id": finding_id, "entry_file": entry_rel}


def submit_finding(finding_id: str, actor: str) -> dict:
    """Transition a CAPTURED or NEEDS_REVISION finding to PENDING_PARENT_REVIEW."""
    entry_path, fnd = find_entry_by_id(finding_id)
    entry_rel = entry_path.relative_to(ROOT).as_posix()
    if fnd["current_approval_state"] == "PENDING_PARENT_REVIEW":
        raise SystemExit(f"DUPLICATE_SUBMISSION_ERROR: Finding '{finding_id}' is already PENDING_PARENT_REVIEW.")
    if fnd["current_approval_state"] not in {"CAPTURED", "NEEDS_REVISION"}:
        raise SystemExit(f"INVALID_TRANSITION: Cannot submit finding in state '{fnd['current_approval_state']}'.")

    affected = [entry_rel, "memory/findings/findings_manifest.json", "memory/findings/FINDINGS_LEDGER.md"]
    now_iso = datetime.now(timezone.utc).isoformat()
    with transactional_operation(f"submit:{finding_id}", affected):
        fnd["current_approval_state"] = "PENDING_PARENT_REVIEW"
        atomic_write_text(entry_path, json.dumps(fnd, ensure_ascii=False, indent=2) + "\n")

        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        manifest["registered_findings"][finding_id]["current_approval_state"] = "PENDING_PARENT_REVIEW"
        manifest["registered_findings"][finding_id]["entry_sha256"] = compute_file_sha256(entry_rel)
        manifest.setdefault("audit_trail", []).append({
            "audit_id": f"FAUD-{len(manifest.get('audit_trail', [])) + 1:04d}",
            "timestamp": now_iso,
            "action": "SUBMIT_FOR_REVIEW",
            "finding_id": finding_id,
            "actor": actor,
        })
        atomic_write_text(MANIFEST_PATH, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        compile_ledger()

    return {"status": "PENDING_PARENT_REVIEW", "finding_id": finding_id}


def review_finding(
    finding_id: str,
    reviewer_agent: str,
    decision: str,
    event_id: str = "",
    rejection_reason: str = "",
    notes: str = "",
) -> dict:
    """Append an immutable parent review event to a finding (blocking self-approval and duplicate events)."""
    if decision not in {"APPROVED_FOR_PROMOTION", "REJECTED", "NEEDS_REVISION"}:
        raise SystemExit(f"Invalid review decision: {decision}")
    entry_path, fnd = find_entry_by_id(finding_id)
    entry_rel = entry_path.relative_to(ROOT).as_posix()

    if not reviewer_agent or reviewer_agent == fnd["subagent_id"]:
        raise SystemExit(f"SELF_APPROVAL_FORBIDDEN: Subagent '{fnd['subagent_id']}' cannot review its own finding.")
    if decision in {"REJECTED", "NEEDS_REVISION"} and not rejection_reason.strip():
        raise SystemExit(f"MISSING_REJECTION_REASON: Decision '{decision}' requires --reason.")

    existing_events = fnd.get("review_events", [])
    if not event_id:
        event_id = f"REV-{finding_id}-{len(existing_events) + 1:03d}"

    for ev in existing_events:
        if ev.get("event_id") == event_id:
            raise SystemExit(f"DUPLICATE_EVENT_ERROR: Review event '{event_id}' already exists on {finding_id}.")
    if existing_events:
        last = existing_events[-1]
        if (
            last.get("reviewer_agent") == reviewer_agent
            and last.get("decision") == decision
            and last.get("rejection_reason", "") == rejection_reason.strip()
            and last.get("notes", "") == notes.strip()
        ):
            raise SystemExit(f"DUPLICATE_EVENT_ERROR: Identical consecutive review event submitted for {finding_id}.")

    affected = [entry_rel, "memory/findings/findings_manifest.json", "memory/findings/FINDINGS_LEDGER.md"]
    now_iso = datetime.now(timezone.utc).isoformat()
    with transactional_operation(f"review:{finding_id}:{event_id}", affected):
        fnd.setdefault("review_events", []).append({
            "event_id": event_id,
            "timestamp": now_iso,
            "reviewer_agent": reviewer_agent,
            "decision": decision,
            "rejection_reason": rejection_reason.strip(),
            "notes": notes.strip(),
        })
        fnd["current_approval_state"] = decision
        atomic_write_text(entry_path, json.dumps(fnd, ensure_ascii=False, indent=2) + "\n")

        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        manifest["registered_findings"][finding_id]["current_approval_state"] = decision
        manifest["registered_findings"][finding_id]["entry_sha256"] = compute_file_sha256(entry_rel)
        manifest.setdefault("audit_trail", []).append({
            "audit_id": f"FAUD-{len(manifest.get('audit_trail', [])) + 1:04d}",
            "timestamp": now_iso,
            "action": f"REVIEW_{decision}",
            "finding_id": finding_id,
            "actor": reviewer_agent,
            "event_id": event_id,
        })
        atomic_write_text(MANIFEST_PATH, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        compile_ledger()

    return {"status": decision, "finding_id": finding_id, "event_id": event_id}


def promote_finding(
    finding_id: str,
    target_file: str,
    marker: str,
    line_start: int,
    line_end: int,
    actor: str = "orchestrator-planner",
) -> dict:
    """Transactionally promote an APPROVED_FOR_PROMOTION finding and snapshot the target document."""
    entry_path, fnd = find_entry_by_id(finding_id)
    entry_rel = entry_path.relative_to(ROOT).as_posix()
    if fnd["current_approval_state"] != "APPROVED_FOR_PROMOTION":
        raise SystemExit(
            f"INVALID_PROMOTION_STATE: Finding '{finding_id}' must be APPROVED_FOR_PROMOTION (got '{fnd['current_approval_state']}')."
        )
    tp = ROOT / target_file
    if not tp.is_file():
        raise SystemExit(f"Target document does not exist: {target_file}")
    t_text = tp.read_text(encoding="utf-8")
    t_lines = t_text.splitlines()
    if line_start < 1 or line_end < line_start or line_end > len(t_lines):
        raise SystemExit(f"Invalid promoted block lines {line_start}..{line_end} in {target_file}")
    verbatim_block = "\n".join(t_lines[line_start - 1 : line_end])
    if len(verbatim_block.strip()) < 30:
        raise SystemExit("Promoted verbatim block must be at least 30 characters of substantive content.")
    if marker and marker not in verbatim_block:
        raise SystemExit(f"Verification marker '{marker}' not found inside lines {line_start}..{line_end} of {target_file}")

    encoded_target = target_file.replace("/", "__")
    snap_rel = f"docs/history/promoted_targets/{finding_id}__{encoded_target}.snapshot.md"
    target_sha = compute_file_sha256(target_file)
    block_sha = hashlib.sha256(verbatim_block.encode("utf-8")).hexdigest()
    now_iso = datetime.now(timezone.utc).isoformat()

    affected = [
        entry_rel,
        snap_rel,
        "memory/findings/findings_manifest.json",
        "memory/findings/FINDINGS_LEDGER.md",
    ]
# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
    with transactional_operation(f"promote:{finding_id}", affected):
        atomic_write_bytes(ROOT / snap_rel, (ROOT / target_file).read_bytes())
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED
        fnd["current_approval_state"] = "PROMOTED"
        fnd["promotion_record"] = {
            "promoted_at": now_iso,
            "target_documents": [target_file],
            "target_section_or_id": marker,
            "verification_marker": marker,
            "target_sha256_after": target_sha,
            "retained_after_promotion": True,
            "promoted_targets": [
                {
                    "target_file": target_file,
                    "verification_marker": marker,
                    "promoted_block_line_start": line_start,
                    "promoted_block_line_end": line_end,
                    "promoted_verbatim_block": verbatim_block,
                    "promoted_block_sha256": block_sha,
                    "target_file_sha256": target_sha,
                    "snapshot_file": snap_rel,
                }
            ],
        }
        atomic_write_text(entry_path, json.dumps(fnd, ensure_ascii=False, indent=2) + "\n")

        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        manifest["registered_findings"][finding_id]["current_approval_state"] = "PROMOTED"
        manifest["registered_findings"][finding_id]["entry_sha256"] = compute_file_sha256(entry_rel)
        manifest.setdefault("audit_trail", []).append({
            "audit_id": f"FAUD-{len(manifest.get('audit_trail', [])) + 1:04d}",
            "timestamp": now_iso,
            "action": "PROMOTE",
            "finding_id": finding_id,
            "target_file": target_file,
            "actor": actor,
        })
        atomic_write_text(MANIFEST_PATH, json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
        compile_ledger()

    return {"status": "PROMOTED", "finding_id": finding_id, "snapshot_file": snap_rel}


def is_valid_superseding_event(event_id: str, superseded_fid: str, target_file: str) -> bool:
    """Verify that event_id is either a promoted superseding finding or an authorized owner approval transition."""
    if not event_id:
        return False
    # Case 1: Authorized owner approval transition in OWNER_APPROVAL_PROVENANCE.json
    prov_p = ROOT / "memory" / "decisions" / "OWNER_APPROVAL_PROVENANCE.json"
    if prov_p.is_file():
        prov = json.loads(prov_p.read_text(encoding="utf-8"))
        if prov.get("revision_no", 0) >= 1 and prov.get("architecture_approval_status") == "OWNER_APPROVED":
            for rev in prov.get("approval_revision_history", []):
                if rev.get("authorization_id") == event_id:
                    return True
    # Case 2: Another PROMOTED finding explicitly superseding superseded_fid on target_file
    for _, fnd in load_all_findings():
        if fnd.get("finding_id") == event_id and fnd.get("current_approval_state") == "PROMOTED":
            if fnd.get("supersedes_finding_id") == superseded_fid:
                return True
    return False


def record_document_revision(
    target_file: str,
    author: str,
    reason: str,
    superseding_finding_id: str = "",
) -> dict:
    """Authorize a legitimate subsequent revision to an already-promoted document.

    Preserves all historical promotion snapshots untouched and verifies that every
    previously promoted verbatim block in target_file remains 100% intact (unless
    explicitly superseded by a promoted superseding_finding_id that retains the old
    text in a historical section).
    """
    tp = ROOT / target_file
    if not tp.is_file():
        raise SystemExit(f"Target file does not exist: {target_file}")
    if not author.strip() or not reason.strip():
        raise SystemExit("Both --author and --reason are required to record a document revision.")

    current_text = tp.read_text(encoding="utf-8")
    current_lines = current_text.splitlines()
    current_sha = compute_file_sha256(target_file)

    # Check all promoted findings targeting target_file
    records = load_all_findings()
    preserved_promotions: list[dict] = []
    initial_promo_sha = ""

    for _, fnd in records:
        if fnd.get("current_approval_state") != "PROMOTED":
            continue
        fid = fnd["finding_id"]
        promo = fnd.get("promotion_record") or {}
        for pt in promo.get("promoted_targets", []):
            if pt.get("target_file") != target_file:
                continue
            initial_promo_sha = pt.get("target_file_sha256", "")
            snap_rel = pt.get("snapshot_file", "")
            snap_p = ROOT / snap_rel
            if not snap_p.is_file() or compute_file_sha256(snap_rel) != initial_promo_sha:
                raise SystemExit(
                    f"HISTORICAL_SNAPSHOT_CORRUPTED: Promotion snapshot '{snap_rel}' for {fid} was missing or altered!"
                )
            expected_block = pt.get("promoted_verbatim_block", "")
            if expected_block not in current_text:
                if not superseding_finding_id or not is_valid_superseding_event(superseding_finding_id, fid, target_file):
                    raise SystemExit(
                        f"UNAUTHORIZED_PROMOTED_CONTENT_EDIT: Cannot record revision for '{target_file}' because previously promoted content for finding '{fid}' was altered or removed without a verified superseding event!"
                    )
            # Locate updated line range of expected_block in current_text
            block_lines = expected_block.splitlines()
            new_start = 0
            for idx in range(len(current_lines) - len(block_lines) + 1):
                if current_lines[idx : idx + len(block_lines)] == block_lines:
                    new_start = idx + 1
                    break
            preserved_promotions.append({
                "finding_id": fid,
                "promoted_block_sha256": pt.get("promoted_block_sha256"),
                "new_line_start": new_start,
                "new_line_end": new_start + len(block_lines) - 1 if new_start else 0,
                "superseded_by": superseding_finding_id or None,
            })

    if not preserved_promotions:
        raise SystemExit(f"File '{target_file}' has no promoted findings to version.")

    doc_revs = (
        json.loads(DOC_REV_MANIFEST_PATH.read_text(encoding="utf-8"))
        if DOC_REV_MANIFEST_PATH.is_file()
        else {"schema_version": "1.0", "policy": "IMMUTABLE_PROMOTION_SNAPSHOTS_WITH_VERSIONED_DOCUMENT_EVOLUTION", "documents": {}}
    )
    doc_entry = doc_revs.setdefault("documents", {}).setdefault(target_file, {
        "initial_promotion_sha256": initial_promo_sha,
        "current_authorized_sha256": initial_promo_sha,
        "revisions": [],
    })
    prev_sha = doc_entry["current_authorized_sha256"]
    if current_sha == prev_sha:
        return {"status": "UNCHANGED", "target_file": target_file, "sha256": current_sha}

    rev_num = len(doc_entry["revisions"]) + 1
    rev_id = f"DOCREV-{rev_num:04d}"
    encoded_target = target_file.replace("/", "__")
    rev_snap_rel = f"docs/history/promoted_targets/{encoded_target}__{rev_id}.snapshot.md"

    with transactional_operation(
        f"record-doc-revision:{target_file}:{rev_id}",
        ["memory/findings/document_revisions_manifest.json", rev_snap_rel],
    ):
# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
        atomic_write_bytes(ROOT / rev_snap_rel, tp.read_bytes())
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED
        doc_entry["current_authorized_sha256"] = current_sha
        doc_entry["revisions"].append({
            "revision_id": rev_id,
            "recorded_at": datetime.now(timezone.utc).isoformat(),
            "author": author.strip(),
            "reason": reason.strip(),
            "previous_sha256": prev_sha,
            "new_sha256": current_sha,
            "snapshot_file": rev_snap_rel,
            "preserved_promotions": preserved_promotions,
        })
        atomic_write_text(DOC_REV_MANIFEST_PATH, json.dumps(doc_revs, ensure_ascii=False, indent=2) + "\n")

    return {
        "status": "REVISION_RECORDED",
        "target_file": target_file,
        "revision_id": rev_id,
        "previous_sha256": prev_sha,
        "new_sha256": current_sha,
    }


def verify_ownership_locks() -> list[str]:
    """Verify that no two ACTIVE subagents hold overlapping write file locks."""
    errors: list[str] = []
    if not LOCKS_PATH.exists():
        return ["Missing memory/findings/subagent_ownership_locks.json"]
    data = json.loads(LOCKS_PATH.read_text(encoding="utf-8"))
    locks = data.get("locks", [])
    claimed_by: dict[str, str] = {}
    for item in locks:
        if item.get("status") != "ACTIVE":
            continue
        agent = item.get("subagent_id", "")
        task = item.get("task_id", "")
        owner_key = f"{agent}:{task}"
        for fpath in item.get("write_files", []):
            if fpath in claimed_by and claimed_by[fpath] != owner_key:
                errors.append(
                    f"Conflicting subagent ownership lock on '{fpath}' between '{claimed_by[fpath]}' and '{owner_key}'"
                )
            else:
                claimed_by[fpath] = owner_key
    return errors


def reconcile_findings_inventories(records: list[tuple[Path, dict]]) -> list[str]:
    """Reconcile findings across disk entries, manifest, immutable baseline, ledger, catalog, locks, and WAL."""
    errors: list[str] = []
    if TX_JOURNAL_PATH.is_file():
        errors.append("Uncommitted findings transaction journal (.tx_journal.json) present; run `manage_findings.py recover-tx`")

    disk_by_id: dict[str, tuple[str, dict]] = {}
    for path, fnd in records:
        fid = fnd.get("finding_id", path.stem)
        rel_p = path.relative_to(ROOT).as_posix()
        disk_by_id[fid] = (rel_p, fnd)

    if not MANIFEST_PATH.is_file():
        errors.append("Missing memory/findings/findings_manifest.json")
        return errors
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    reg_map: dict[str, dict] = manifest.get("registered_findings", {})

    if not BASELINE_MANIFEST_PATH.is_file():
        errors.append("Missing immutable baseline: docs/history/immutable_baselines/findings_manifest.baseline.json")
    else:
        base_manifest = json.loads(BASELINE_MANIFEST_PATH.read_text(encoding="utf-8"))
        base_reg: dict[str, dict] = base_manifest.get("registered_findings", {})
        for b_fid, b_info in base_reg.items():
            if b_fid not in reg_map:
                errors.append(
                    f"Deleted or missing finding detected: '{b_fid}' was removed from memory/findings/findings_manifest.json (violates append-only non-deletion policy)"
                )
            if b_fid not in disk_by_id:
                errors.append(
                    f"Deleted or missing finding file on disk: '{b_fid}' ({b_info.get('entry_file')}) is missing from memory/findings/entries/"
                )

    for m_fid, m_info in reg_map.items():
        if m_info.get("deleted") is True:
            errors.append(f"Finding '{m_fid}' marked deleted=true in findings_manifest.json; findings must never be deleted")
        if m_fid not in disk_by_id:
            errors.append(f"Deleted or missing finding '{m_fid}': registered in findings_manifest.json but file '{m_info.get('entry_file')}' is missing")
        else:
            rel_p, fnd = disk_by_id[m_fid]
            if rel_p != m_info.get("entry_file"):
                errors.append(f"Finding path mismatch for {m_fid}: disk='{rel_p}' vs manifest='{m_info.get('entry_file')}'")
            actual_sha = compute_file_sha256(rel_p)
            if actual_sha != m_info.get("entry_sha256"):
                errors.append(f"Finding entry SHA-256 mismatch for {m_fid} against findings_manifest.json")

    for d_fid, (rel_p, _) in disk_by_id.items():
        if d_fid not in reg_map:
            errors.append(f"Unregistered finding on disk: '{d_fid}' ({rel_p}) is missing from findings_manifest.json")

    if not LEDGER_PATH.is_file():
        errors.append("Missing memory/findings/FINDINGS_LEDGER.md")
    else:
        ledger_text = LEDGER_PATH.read_text(encoding="utf-8")
        ledger_ids = set(re.findall(r"^### `(FND-[^`]+)`", ledger_text, re.M))
        expected_ids = set(disk_by_id.keys()) | set(reg_map.keys())
        if ledger_ids != expected_ids:
            errors.append(
                f"FINDINGS_LEDGER.md out of sync with findings inventory: ledger={sorted(ledger_ids)} vs expected={sorted(expected_ids)}"
            )

    if LOCKS_PATH.is_file():
        locks_data = json.loads(LOCKS_PATH.read_text(encoding="utf-8"))
        for lk in locks_data.get("locks", []):
            for wf in lk.get("write_files", []):
                if wf.startswith("memory/findings/entries/") and not (ROOT / wf).is_file():
                    errors.append(f"Deleted finding file referenced in subagent_ownership_locks.json: '{wf}'")

    wal_path = ROOT / "memory" / "session" / "ACTIVE_SESSION_WAL.md"
    if wal_path.is_file():
        wal_ids = set(re.findall(r"`(FND-[0-9]{8}-[0-9]{3})`", wal_path.read_text(encoding="utf-8")))
        for w_fid in sorted(wal_ids):
            if w_fid not in disk_by_id:
                errors.append(f"Deleted finding detected: '{w_fid}' is recorded in ACTIVE_SESSION_WAL.md but missing from memory/findings/entries/")

    catalog_path = ROOT / "PROJECT_FILE_CATALOG.md"
    if catalog_path.is_file():
        cat_entries = set(re.findall(r"^### `(memory/findings/entries/[^`]+\.json)`$", catalog_path.read_text(encoding="utf-8"), re.M))
        for c_entry in sorted(cat_entries):
            if not (ROOT / c_entry).is_file():
                errors.append(f"Deleted finding file detected via PROJECT_FILE_CATALOG.md reconciliation: '{c_entry}' is missing on disk")

    return errors


def verify_promotion_evidence_integrity(fid: str, promo: dict) -> list[str]:
    """Verify historical promotion snapshot immutability, promoted block integrity, and versioned evolution chains."""
    errors: list[str] = []
    if promo.get("retained_after_promotion") is not True:
        errors.append(f"Finding {fid} must have retained_after_promotion=true")
    targets = promo.get("target_documents", [])
    if not targets:
        errors.append(f"Finding {fid} promotion_record has empty target_documents")

    promoted_targets = promo.get("promoted_targets", [])
    if not promoted_targets:
        errors.append(f"Finding {fid} promotion_record is missing detailed 'promoted_targets' evidence blocks")
        return errors

    doc_revs = (
        json.loads(DOC_REV_MANIFEST_PATH.read_text(encoding="utf-8")).get("documents", {})
        if DOC_REV_MANIFEST_PATH.is_file()
        else {}
    )

    for pt in promoted_targets:
        tfile = pt.get("target_file", "")
        tp = ROOT / tfile
        if not tp.is_file():
            errors.append(f"Finding {fid} promoted target document does not exist: {tfile}")
            continue

        t_bytes = tp.read_bytes()
        t_text = t_bytes.decode("utf-8")
        t_lines = t_text.splitlines()
        actual_file_sha = hashlib.sha256(t_bytes).hexdigest()
        promo_sha = pt.get("target_file_sha256", "")

        # 1. Historical promotion snapshot at promotion time must NEVER be modified or deleted
        snap_rel = pt.get("snapshot_file", "")
        snap_path = ROOT / snap_rel if snap_rel else None
        if not snap_path or not snap_path.is_file():
            errors.append(f"Missing promoted target historical snapshot file '{snap_rel}' for finding {fid}")
        else:
            snap_sha = hashlib.sha256(snap_path.read_bytes()).hexdigest()
            if snap_sha != promo_sha:
                errors.append(
                    f"Historical promotion snapshot '{snap_rel}' for finding {fid} was tampered with (sha256 mismatch against promotion record)"
                )

        # 2. The promoted substantive content block must remain intact in the current document
        marker = pt.get("verification_marker", "")
        if marker and marker not in t_text:
            errors.append(f"Finding {fid} verification marker '{marker}' missing from {tfile}")

        expected_block = pt.get("promoted_verbatim_block", "")
        if not expected_block or len(expected_block.strip()) < 30:
            errors.append(f"Finding {fid} has insufficient promoted_verbatim_block for {tfile}")
            continue

# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
        if expected_block.replace("\r\n", "\n") not in t_text.replace("\r\n", "\n"):
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED
            # Check if an authorized revision explicitly superseded this block via a verified event
            superseded_ok = False
            doc_rev_entry_chk = doc_revs.get(tfile)
            if doc_rev_entry_chk and doc_rev_entry_chk.get("current_authorized_sha256") == actual_file_sha:
                for r_item in doc_rev_entry_chk.get("revisions", []):
                    for pp in r_item.get("preserved_promotions", []):
                        sup_id = pp.get("superseded_by")
                        if pp.get("finding_id") == fid and sup_id and is_valid_superseding_event(sup_id, fid, tfile):
                            superseded_ok = True
            if not superseded_ok:
                errors.append(
                    f"Promoted target content modified in '{tfile}' for finding {fid}: exact promoted_verbatim_block was altered or removed"
                )

        # 3. Check whether document is at initial promotion SHA-256 or has evolved via an authorized revision chain
        if actual_file_sha == promo_sha:
            l_start = pt.get("promoted_block_line_start", 0)
            l_end = pt.get("promoted_block_line_end", 0)
            if l_start < 1 or l_end < l_start or l_end > len(t_lines):
                errors.append(f"Promoted target line bounds ({l_start}..{l_end}) out of range in '{tfile}' for finding {fid}")
            else:
                actual_slice = "\n".join(t_lines[l_start - 1 : l_end])
                actual_slice_sha = hashlib.sha256(actual_slice.encode("utf-8")).hexdigest()
                if actual_slice != expected_block or actual_slice_sha != pt.get("promoted_block_sha256"):
                    errors.append(
                        f"Promoted target content modified at lines {l_start}..{l_end} in '{tfile}' for finding {fid}"
                    )
        else:
            # Document evolved after initial promotion: verify revision chain in document_revisions_manifest.json
            doc_rev_entry = doc_revs.get(tfile)
            if not doc_rev_entry:
                errors.append(
                    f"Promoted target '{tfile}' modified after promotion of {fid} without an authorized revision entry in document_revisions_manifest.json"
                )
            else:
                if doc_rev_entry.get("current_authorized_sha256") != actual_file_sha:
                    errors.append(
                        f"Promoted target '{tfile}' has unrecorded modifications not matching current_authorized_sha256 in document_revisions_manifest.json"
                    )
                revs = doc_rev_entry.get("revisions", [])
                if not revs:
                    errors.append(f"Empty revisions list in document_revisions_manifest.json for evolved document '{tfile}'")
                else:
                    expected_prev = doc_rev_entry.get("initial_promotion_sha256", promo_sha)
                    for r_item in revs:
                        if r_item.get("previous_sha256") != expected_prev:
                            errors.append(
                                f"Broken revision hash chain in document_revisions_manifest.json for '{tfile}' at {r_item.get('revision_id')}"
                            )
                        r_snap = r_item.get("snapshot_file", "")
                        if not r_snap or not (ROOT / r_snap).is_file() or compute_file_sha256(r_snap) != r_item.get("new_sha256"):
                            errors.append(
                                f"Missing or mismatched revision snapshot '{r_snap}' for '{tfile}' at {r_item.get('revision_id')}"
                            )
                        expected_prev = r_item.get("new_sha256", "")

    return errors


def verify_findings() -> tuple[list[str], dict]:
    """Validate all subagent findings, 5-way inventory reconciliation, review events, and promotions."""
    errors: list[str] = []
    errors.extend(verify_ownership_locks())
    records = load_all_findings()
    errors.extend(reconcile_findings_inventories(records))

    seen_ids: set[str] = set()
    counts = {s: 0 for s in VALID_STATES}

    for path, fnd in records:
        missing_keys = REQUIRED_FINDING_KEYS - set(fnd.keys())
        if missing_keys:
            errors.append(f"Finding {path.name} missing required keys: {sorted(missing_keys)}")
            continue
        fid = fnd["finding_id"]
        if fid in seen_ids:
            errors.append(f"Duplicate finding_id '{fid}' across finding files")
        seen_ids.add(fid)

        state = fnd["current_approval_state"]
        if state not in VALID_STATES:
            errors.append(f"Invalid current_approval_state '{state}' in {fid}")
        else:
            counts[state] += 1

        if fnd["confidence"] not in VALID_CONFIDENCE:
            errors.append(f"Invalid confidence '{fnd['confidence']}' in {fid}")

        if not fnd["source_file_paths"] or not fnd["line_ranges"] or not fnd["source_revisions"]:
            errors.append(f"Finding {fid} must specify non-empty source_file_paths, line_ranges, and source_revisions")

        for lr in fnd.get("line_ranges", []):
            src_file = ROOT / lr.get("file", "")
            if not src_file.is_file():
                errors.append(f"Finding {fid} references nonexistent source file '{lr.get('file')}'")
                continue
            total_lines = len(src_file.read_text(encoding="utf-8").splitlines())
            s_line = lr.get("start_line", 0)
            e_line = lr.get("end_line", 0)
            if s_line < 1 or e_line < s_line or e_line > max(total_lines, 1):
                errors.append(
                    f"Finding {fid} has invalid line range {s_line}..{e_line} for {lr.get('file')} (total lines: {total_lines})"
                )

        for rev in fnd.get("source_revisions", []):
            sha = rev.get("sha256", "")
            if not isinstance(sha, str) or len(sha) != 64:
                errors.append(f"Finding {fid} has invalid source revision sha256 for {rev.get('file')}")

        review_events = fnd.get("review_events", [])
        if state in {"APPROVED_FOR_PROMOTION", "PROMOTED", "REJECTED", "NEEDS_REVISION"} and not review_events:
            errors.append(f"Finding {fid} is in state '{state}' but has no parent review_events")

        seen_ev_ids: set[str] = set()
        for ev in review_events:
            ev_id = ev.get("event_id", "")
            if ev_id in seen_ev_ids:
                errors.append(f"Duplicate review event_id '{ev_id}' in finding {fid}")
            seen_ev_ids.add(ev_id)
            reviewer = ev.get("reviewer_agent", "")
            decision = ev.get("decision", "")
            if not reviewer or reviewer == fnd["subagent_id"]:
                errors.append(
                    f"Invalid finding approval in {fid}: subagent '{fnd['subagent_id']}' cannot self-approve (reviewer='{reviewer}')"
                )
            if decision in {"REJECTED", "NEEDS_REVISION"} and not str(ev.get("rejection_reason", "")).strip():
                errors.append(f"Invalid finding review in {fid}: decision '{decision}' requires an explicit rejection_reason")

        if state == "APPROVED_FOR_PROMOTION":
            errors.append(
                f"Approved finding not promoted: {fid} is APPROVED_FOR_PROMOTION but has not been promoted into authoritative documentation"
            )

        if state == "PROMOTED":
            has_approval = any(ev.get("decision") == "APPROVED_FOR_PROMOTION" for ev in review_events)
            if not has_approval:
                errors.append(f"Finding {fid} is marked PROMOTED without an APPROVED_FOR_PROMOTION parent review event")
            promo = fnd.get("promotion_record")
            if not isinstance(promo, dict):
                errors.append(f"Finding {fid} is PROMOTED but promotion_record is missing")
            else:
                errors.extend(verify_promotion_evidence_integrity(fid, promo))

    summary = {
        "total_findings": len(records),
        "state_counts": counts,
        "errors": errors,
    }
    return errors, summary


def compile_ledger() -> str:
    """Compile the human-readable memory/findings/FINDINGS_LEDGER.md from isolated entries."""
    records = load_all_findings()
    lines: list[str] = [
        "# السجل الموحد لمكتشفات الـ Sub-Agents وحالة مراجعتها وترقيتها (`memory/findings/FINDINGS_LEDGER.md`)",
        "",
        "> **ملاحظة آلية (`Auto-Generated Ledger`):** يُبنى هذا الملف آلياً عبر `python3 tools/findings_guard/manage_findings.py compile-ledger` من ملفات المكتشفات المعزولة في `memory/findings/entries/*.json`. لا تعدل هذا الملف يدوياً، ولا تحذف أي اكتشاف بعد ترقيته.",
        "",
        f"- **إجمالي المكتشفات المسجلة:** `{len(records)}`",
        "",
        "## جدول المكتشفات والترقية (`Subagent Findings & Promotion Table`)",
        "",
        "| رقم الاكتشاف (`ID`) | المهمة (`Task`) | الـ Sub-Agent | المصادر والأسطر (`Source & Lines`) | درجة الثقة | الحالة (`State`) | المراجع (`Parent Reviewer`) | الوثائق المرقّى إليها (`Promoted Targets`) |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for _, fnd in records:
        fid = fnd["finding_id"]
        loc_str = ", ".join(
            f"`{lr['file']}` (`L{lr['start_line']}–L{lr['end_line']}`)" for lr in fnd.get("line_ranges", [])
        )
        reviewer = fnd["review_events"][-1]["reviewer_agent"] if fnd.get("review_events") else "PENDING"
        promo = fnd.get("promotion_record") or {}
        targets = ", ".join(f"`{t}`" for t in promo.get("target_documents", [])) or "—"
        lines.append(
            f"| `{fid}` | `{fnd['task_id']}` | `{fnd['subagent_id']}` | {loc_str} | `{fnd['confidence']}` | `{fnd['current_approval_state']}` | `{reviewer}` | {targets} |"
        )

    lines.extend(["", "## تفاصيل المكتشفات وسجل المراجعة الإلحاقي (`Detailed Findings & Append-Only Reviews`)", ""])
    for path, fnd in records:
        fid = fnd["finding_id"]
        lines.extend([
            f"### `{fid}` — بواسطة `{fnd['subagent_id']}` (المهمة: `{fnd['task_id']}`)",
            f"- **ملف السجل المعزول:** `memory/findings/entries/{path.name}`",
            f"- **تاريخ الإنشاء:** `{fnd['created_at']}`",
            f"- **الدليل (`Evidence`):** {fnd['evidence']}",
            f"- **الإجراء المقترح (`Proposed Action`):** {fnd['proposed_action']}",
            f"- **الحالة الحالية:** `{fnd['current_approval_state']}`",
            "- **سجل أحداث المراجعة الإلحاقي (`Append-Only Review Events`):**",
        ])
        for ev in fnd.get("review_events", []):
            reason_note = f" | السبب/الملاحظة: {ev.get('notes') or ev.get('rejection_reason', '')}"
            lines.append(
                f"  - `{ev['event_id']}` ({ev['timestamp']}): المراجع `{ev['reviewer_agent']}` -> القرار `{ev['decision']}`{reason_note}"
            )
        if fnd.get("promotion_record"):
            pr = fnd["promotion_record"]
            lines.append(
                f"- **سجل الترقية (`Promotion Record`):** تمت الترقية بتاريخ `{pr['promoted_at']}` إلى `{pr['target_documents']}` (محفوظ بعد الترقية: `{pr['retained_after_promotion']}`)."
            )
        lines.append("")

    content = "\n".join(lines).strip() + "\n"
    atomic_write_text(LEDGER_PATH, content)
    return content


def arg_val(flag: str, default: str = "") -> str:
    """Return CLI argument value following flag."""
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return default


def main() -> None:
    """CLI entrypoint for transactional subagent findings lifecycle and verification."""
    cmd = sys.argv[1] if len(sys.argv) > 1 else "verify"
    if cmd == "compile-ledger":
        compile_ledger()
        print(json.dumps({"status": "LEDGER_COMPILED", "path": str(LEDGER_PATH.relative_to(ROOT))}, ensure_ascii=False))
    elif cmd == "verify":
# START CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED | Author: orchestrator-planner
        errors, summary = verify_findings()
        print(json.dumps(summary, ensure_ascii=False), flush=True)
# END CHANGE P0-ARCH-REVIEW-ENV | 2026-10-17T07:41:00Z | EDITED
        if errors:
            raise SystemExit(1)
    elif cmd == "recover-tx":
        print(json.dumps(recover_interrupted_transaction(), ensure_ascii=False))
    elif cmd == "capture":
        res = capture_finding(
            finding_id=arg_val("--id"),
            task_id=arg_val("--task"),
            subagent_id=arg_val("--subagent"),
            source_spec=arg_val("--sources"),
            evidence=arg_val("--evidence"),
            confidence=arg_val("--confidence", "HIGH"),
            proposed_action=arg_val("--action"),
            simulate_interrupt="--simulate-interrupt" in sys.argv,
        )
        print(json.dumps(res, ensure_ascii=False))
    elif cmd == "submit":
        res = submit_finding(finding_id=arg_val("--id"), actor=arg_val("--actor", "subagent"))
        print(json.dumps(res, ensure_ascii=False))
    elif cmd in {"review", "approve", "reject"}:
        dec = (
            "APPROVED_FOR_PROMOTION"
            if cmd == "approve"
            else ("REJECTED" if cmd == "reject" else arg_val("--decision"))
        )
        res = review_finding(
            finding_id=arg_val("--id"),
            reviewer_agent=arg_val("--reviewer", "orchestrator-planner"),
            decision=dec,
            event_id=arg_val("--event-id"),
            rejection_reason=arg_val("--reason"),
            notes=arg_val("--notes"),
        )
        print(json.dumps(res, ensure_ascii=False))
    elif cmd == "promote":
        res = promote_finding(
            finding_id=arg_val("--id"),
            target_file=arg_val("--target-file"),
            marker=arg_val("--marker"),
            line_start=int(arg_val("--line-start", "1")),
            line_end=int(arg_val("--line-end", "1")),
            actor=arg_val("--actor", "orchestrator-planner"),
        )
        print(json.dumps(res, ensure_ascii=False))
    elif cmd == "record-doc-revision":
        res = record_document_revision(
            target_file=arg_val("--file"),
            author=arg_val("--author", "orchestrator-planner"),
            reason=arg_val("--reason"),
            superseding_finding_id=arg_val("--superseding-finding"),
        )
        print(json.dumps(res, ensure_ascii=False))
    else:
        raise SystemExit(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main()
