# START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED | Author: orchestrator-planner
"""Data models and schemas for the Incremental Update Packaging System."""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Dict, List, Optional
import json


class PackageMode(str, Enum):
    """Update packaging mode."""
    REVIEW = "REVIEW"
    COMPLETE = "COMPLETE"


class UpdateStatus(str, Enum):
    """Lifecycle state of an update package."""
    CREATED = "CREATED"
    EXPORTED = "EXPORTED"
    DELIVERED = "DELIVERED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    SUPERSEDED = "SUPERSEDED"


class FileOperation(str, Enum):
    """File mutation operation in an update delta."""
    ADD = "ADD"
    MODIFY = "MODIFY"
    DELETE = "DELETE"
    RENAME = "RENAME"


@dataclass
class FileRecord:
    """Record of an individual file in a workspace inventory."""
    path: str
    sha256: str
    size_bytes: int
    is_binary: bool = False
    last_modified_utc: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> FileRecord:
        return cls(
            path=data["path"],
            sha256=data["sha256"],
            size_bytes=int(data["size_bytes"]),
            is_binary=bool(data.get("is_binary", False)),
            last_modified_utc=data.get("last_modified_utc")
        )


@dataclass
class BaselineInventory:
    """Complete inventory snapshot of a verified repository baseline."""
    baseline_id: str
    repo_identity: str
    created_at_utc: str
    tool_version: str
    schema_version: str = "1.0.0"
    git_commit: Optional[str] = None
    inclusion_policy: str = "tracked_first_party"
    exclusion_policy: str = "standard_anti_leak"
    trust_status: str = "VALID"
    invalidation_reason: Optional[str] = None
    files: Dict[str, FileRecord] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "baseline_id": self.baseline_id,
            "repo_identity": self.repo_identity,
            "created_at_utc": self.created_at_utc,
            "tool_version": self.tool_version,
            "schema_version": self.schema_version,
            "git_commit": self.git_commit,
            "inclusion_policy": self.inclusion_policy,
            "exclusion_policy": self.exclusion_policy,
            "trust_status": self.trust_status,
            "invalidation_reason": self.invalidation_reason,
            "files": {path: rec.to_dict() for path, rec in sorted(self.files.items())}
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2) + "\n"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> BaselineInventory:
        files = {
            path: FileRecord.from_dict(rec)
            for path, rec in data.get("files", {}).items()
        }
        return cls(
            baseline_id=data["baseline_id"],
            repo_identity=data["repo_identity"],
            created_at_utc=data["created_at_utc"],
            tool_version=data["tool_version"],
            schema_version=data.get("schema_version", "1.0.0"),
            git_commit=data.get("git_commit"),
            inclusion_policy=data.get("inclusion_policy", "tracked_first_party"),
            exclusion_policy=data.get("exclusion_policy", "standard_anti_leak"),
            trust_status=data.get("trust_status", "VALID"),
            invalidation_reason=data.get("invalidation_reason"),
            files=files
        )


@dataclass
class ManifestEntry:
    """Single file mutation entry in the update manifest."""
    path: str
    operation: str
    previous_sha256: Optional[str] = None
    new_sha256: Optional[str] = None
    size_bytes: int = 0
    is_binary: bool = False
    payload_path: Optional[str] = None
    payload_sha256: Optional[str] = None
    renamed_from: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ManifestEntry:
        return cls(
            path=data["path"],
            operation=data["operation"],
            previous_sha256=data.get("previous_sha256"),
            new_sha256=data.get("new_sha256"),
            size_bytes=int(data.get("size_bytes", 0)),
            is_binary=bool(data.get("is_binary", False)),
            payload_path=data.get("payload_path"),
            payload_sha256=data.get("payload_sha256"),
            renamed_from=data.get("renamed_from")
        )


@dataclass
class ExclusionRecord:
    """Record of a changed file deliberately excluded from a package mode."""
    path: str
    size_bytes: int
    sha256: str
    reason: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ExclusionRecord:
        return cls(
            path=data["path"],
            size_bytes=int(data["size_bytes"]),
            sha256=data["sha256"],
            reason=data["reason"]
        )


@dataclass
class UpdateManifest:
    """Complete manifest embedded at the root of the update package."""
    package_format_version: str
    update_id: str
    base_snapshot_id: str
    base_snapshot_hash: str
    target_snapshot_id: str
    target_snapshot_hash: str
    created_at_utc: str
    creator_tool: str
    package_mode: str
    status: str
    task_ids: List[str] = field(default_factory=list)
    base_git_commit: Optional[str] = None
    target_git_commit: Optional[str] = None
    operations_summary: Dict[str, int] = field(default_factory=dict)
    entries: List[ManifestEntry] = field(default_factory=list)
    exclusions_count: int = 0
    validation_status: str = "UNVALIDATED"
    # START CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED | Author: orchestrator-planner
    base_snapshot_trust_status: str = "VALID"
    base_snapshot_invalidation_reason: Optional[str] = None
    # END CHANGE TASK-UPDATE-SYS-CORRECTION-02 | 2026-10-18T02:30:00Z | EDITED

    def to_dict(self) -> Dict[str, Any]:
        return {
            "package_format_version": self.package_format_version,
            "update_id": self.update_id,
            "base_snapshot_id": self.base_snapshot_id,
            "base_snapshot_hash": self.base_snapshot_hash,
            "target_snapshot_id": self.target_snapshot_id,
            "target_snapshot_hash": self.target_snapshot_hash,
            "created_at_utc": self.created_at_utc,
            "creator_tool": self.creator_tool,
            "package_mode": self.package_mode,
            "status": self.status,
            "task_ids": self.task_ids,
            "base_git_commit": self.base_git_commit,
            "target_git_commit": self.target_git_commit,
            "operations_summary": self.operations_summary,
            "entries": [e.to_dict() for e in self.entries],
            "exclusions_count": self.exclusions_count,
            "validation_status": self.validation_status,
            "base_snapshot_trust_status": self.base_snapshot_trust_status,
            "base_snapshot_invalidation_reason": self.base_snapshot_invalidation_reason
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2) + "\n"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> UpdateManifest:
        entries = [ManifestEntry.from_dict(e) for e in data.get("entries", [])]
        return cls(
            package_format_version=data["package_format_version"],
            update_id=data["update_id"],
            base_snapshot_id=data["base_snapshot_id"],
            base_snapshot_hash=data["base_snapshot_hash"],
            target_snapshot_id=data["target_snapshot_id"],
            target_snapshot_hash=data["target_snapshot_hash"],
            created_at_utc=data["created_at_utc"],
            creator_tool=data["creator_tool"],
            package_mode=data["package_mode"],
            status=data["status"],
            task_ids=data.get("task_ids", []),
            base_git_commit=data.get("base_git_commit"),
            target_git_commit=data.get("target_git_commit"),
            operations_summary=data.get("operations_summary", {}),
            entries=entries,
            exclusions_count=int(data.get("exclusions_count", 0)),
            validation_status=data.get("validation_status", "UNVALIDATED"),
            base_snapshot_trust_status=data.get("base_snapshot_trust_status", "VALID"),
            base_snapshot_invalidation_reason=data.get("base_snapshot_invalidation_reason")
        )
# END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:15:00Z | CREATED
