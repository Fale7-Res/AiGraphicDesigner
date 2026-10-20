# مرآة الكود التفصيلية: `tools/update_packages/models.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/models.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/models.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `239` (`Lines 1–239`)
- **بصمة الملف (`SHA-256`):** `28ce68fab2f77dd8d167e92e125c0c3de069871fdc8b76b3658c584cdcbffbed`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `PackageMode` | `class` | `Lines 11–14` | `class PackageMode(str, Enum):` | Update packaging mode. |
| `UpdateStatus` | `class` | `Lines 17–24` | `class UpdateStatus(str, Enum):` | Lifecycle state of an update package. |
| `FileOperation` | `class` | `Lines 27–32` | `class FileOperation(str, Enum):` | File mutation operation in an update delta. |
| `FileRecord` | `class` | `Lines 36–55` | `class FileRecord:` | Record of an individual file in a workspace inventory. |
| `FileRecord.to_dict` | `method` | `Lines 44–45` | `def to_dict(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `FileRecord.from_dict` | `method` | `Lines 48–55` | `def from_dict(cls, data: Dict[str, Any]) -> FileRecord:` | رمز برمجي موثق. |
| `BaselineInventory` | `class` | `Lines 59–109` | `class BaselineInventory:` | Complete inventory snapshot of a verified repository baseline. |
| `BaselineInventory.to_dict` | `method` | `Lines 73–86` | `def to_dict(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `BaselineInventory.to_json` | `method` | `Lines 88–89` | `def to_json(self) -> str:` | رمز برمجي موثق. |
| `BaselineInventory.from_dict` | `method` | `Lines 92–109` | `def from_dict(cls, data: Dict[str, Any]) -> BaselineInventory:` | رمز برمجي موثق. |
| `ManifestEntry` | `class` | `Lines 113–140` | `class ManifestEntry:` | Single file mutation entry in the update manifest. |
| `ManifestEntry.to_dict` | `method` | `Lines 125–126` | `def to_dict(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `ManifestEntry.from_dict` | `method` | `Lines 129–140` | `def from_dict(cls, data: Dict[str, Any]) -> ManifestEntry:` | رمز برمجي موثق. |
| `ExclusionRecord` | `class` | `Lines 144–161` | `class ExclusionRecord:` | Record of a changed file deliberately excluded from a package mode. |
| `ExclusionRecord.to_dict` | `method` | `Lines 151–152` | `def to_dict(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `ExclusionRecord.from_dict` | `method` | `Lines 155–161` | `def from_dict(cls, data: Dict[str, Any]) -> ExclusionRecord:` | رمز برمجي موثق. |
| `UpdateManifest` | `class` | `Lines 165–238` | `class UpdateManifest:` | Complete manifest embedded at the root of the update package. |
| `UpdateManifest.to_dict` | `method` | `Lines 189–210` | `def to_dict(self) -> Dict[str, Any]:` | رمز برمجي موثق. |
| `UpdateManifest.to_json` | `method` | `Lines 212–213` | `def to_json(self) -> str:` | رمز برمجي موثق. |
| `UpdateManifest.from_dict` | `method` | `Lines 216–238` | `def from_dict(cls, data: Dict[str, Any]) -> UpdateManifest:` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `PackageMode` — `Lines 11–14`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `11` إلى السطر `14` (`Lines 11–14`)
- **الوظيفة:** Update packaging mode.
- **الكود الفعلي (`Lines 11–14`):**
```python
class PackageMode(str, Enum):
    """Update packaging mode."""
    REVIEW = "REVIEW"
    COMPLETE = "COMPLETE"
```

### `UpdateStatus` — `Lines 17–24`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `24` (`Lines 17–24`)
- **الوظيفة:** Lifecycle state of an update package.
- **الكود الفعلي (`Lines 17–24`):**
```python
class UpdateStatus(str, Enum):
    """Lifecycle state of an update package."""
    CREATED = "CREATED"
    EXPORTED = "EXPORTED"
    DELIVERED = "DELIVERED"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    SUPERSEDED = "SUPERSEDED"
```

### `FileOperation` — `Lines 27–32`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `27` إلى السطر `32` (`Lines 27–32`)
- **الوظيفة:** File mutation operation in an update delta.
- **الكود الفعلي (`Lines 27–32`):**
```python
class FileOperation(str, Enum):
    """File mutation operation in an update delta."""
    ADD = "ADD"
    MODIFY = "MODIFY"
    DELETE = "DELETE"
    RENAME = "RENAME"
```

### `FileRecord` — `Lines 36–55`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `36` إلى السطر `55` (`Lines 36–55`)
- **الوظيفة:** Record of an individual file in a workspace inventory.
- **الكود الفعلي (`Lines 36–55`):**
```python
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
```

### `FileRecord.to_dict` — `Lines 44–45`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `45` (`Lines 44–45`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 44–45`):**
```python
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
```

### `FileRecord.from_dict` — `Lines 48–55`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `55` (`Lines 48–55`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–55`):**
```python
    def from_dict(cls, data: Dict[str, Any]) -> FileRecord:
        return cls(
            path=data["path"],
            sha256=data["sha256"],
            size_bytes=int(data["size_bytes"]),
            is_binary=bool(data.get("is_binary", False)),
            last_modified_utc=data.get("last_modified_utc")
        )
```

### `BaselineInventory` — `Lines 59–109`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `59` إلى السطر `109` (`Lines 59–109`)
- **الوظيفة:** Complete inventory snapshot of a verified repository baseline.
- **الكود الفعلي (`Lines 59–109`):**
```python
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
```

### `BaselineInventory.to_dict` — `Lines 73–86`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `73` إلى السطر `86` (`Lines 73–86`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 73–86`):**
```python
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
```

### `BaselineInventory.to_json` — `Lines 88–89`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `88` إلى السطر `89` (`Lines 88–89`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 88–89`):**
```python
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2) + "\n"
```

### `BaselineInventory.from_dict` — `Lines 92–109`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `92` إلى السطر `109` (`Lines 92–109`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 92–109`):**
```python
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
```

### `ManifestEntry` — `Lines 113–140`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `113` إلى السطر `140` (`Lines 113–140`)
- **الوظيفة:** Single file mutation entry in the update manifest.
- **الكود الفعلي (`Lines 113–140`):**
```python
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
```

### `ManifestEntry.to_dict` — `Lines 125–126`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `125` إلى السطر `126` (`Lines 125–126`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 125–126`):**
```python
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
```

### `ManifestEntry.from_dict` — `Lines 129–140`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `129` إلى السطر `140` (`Lines 129–140`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 129–140`):**
```python
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
```

### `ExclusionRecord` — `Lines 144–161`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `144` إلى السطر `161` (`Lines 144–161`)
- **الوظيفة:** Record of a changed file deliberately excluded from a package mode.
- **الكود الفعلي (`Lines 144–161`):**
```python
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
```

### `ExclusionRecord.to_dict` — `Lines 151–152`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `151` إلى السطر `152` (`Lines 151–152`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 151–152`):**
```python
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
```

### `ExclusionRecord.from_dict` — `Lines 155–161`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `155` إلى السطر `161` (`Lines 155–161`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 155–161`):**
```python
    def from_dict(cls, data: Dict[str, Any]) -> ExclusionRecord:
        return cls(
            path=data["path"],
            size_bytes=int(data["size_bytes"]),
            sha256=data["sha256"],
            reason=data["reason"]
        )
```

### `UpdateManifest` — `Lines 165–238`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `165` إلى السطر `238` (`Lines 165–238`)
- **الوظيفة:** Complete manifest embedded at the root of the update package.
- **الكود الفعلي (`Lines 165–238`):**
```python
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
```

### `UpdateManifest.to_dict` — `Lines 189–210`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `189` إلى السطر `210` (`Lines 189–210`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 189–210`):**
```python
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
```

### `UpdateManifest.to_json` — `Lines 212–213`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `212` إلى السطر `213` (`Lines 212–213`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 212–213`):**
```python
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2) + "\n"
```

### `UpdateManifest.from_dict` — `Lines 216–238`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `216` إلى السطر `238` (`Lines 216–238`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 216–238`):**
```python
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
```
