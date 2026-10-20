# مرآة الكود التفصيلية: `tools/update_packages/scanner.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/scanner.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/scanner.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `213` (`Lines 1–213`)
- **بصمة الملف (`SHA-256`):** `325f3234ad18a3b7d15ab759d1f7889a0ec668623dc7b95564ca1903a6d370e2`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `ScanningError` | `class` | `Lines 14–16` | `class ScanningError(RuntimeError):` | Raised when an included repository file cannot be safely inspected or scanned. |
| `calculate_stream_sha256` | `function` | `Lines 56–62` | `def calculate_stream_sha256(file_path: Path) -> str:` | Compute the SHA-256 hexadecimal digest of a file safely in 64 KiB chunks. |
| `compute_bytes_sha256` | `function` | `Lines 65–67` | `def compute_bytes_sha256(data: bytes) -> str:` | Compute SHA-256 digest of raw byte content. |
| `is_binary_file` | `function` | `Lines 70–81` | `def is_binary_file(file_path: Path) -> bool:` | Check if file is binary by extension or null-byte heuristic in the first 8 KiB. |
| `is_secret_file` | `function` | `Lines 84–90` | `def is_secret_file(file_path: Path) -> bool:` | Determine if a file name or path suggests it contains credentials/secrets. |
| `WorkspaceScanner` | `class` | `Lines 93–212` | `class WorkspaceScanner:` | Scans repository files and constructs deterministic inventory maps with fail-closed integrity. |
| `WorkspaceScanner.__init__` | `method` | `Lines 96–109` | `def __init__(` | رمز برمجي موثق. |
| `WorkspaceScanner.should_exclude_path` | `method` | `Lines 111–145` | `def should_exclude_path(self, path: Path) -> Tuple[bool, str]:` | Check if a path should be excluded, returning (is_excluded, reason). |
| `WorkspaceScanner.scan` | `method` | `Lines 147–212` | `def scan(self) -> Dict[str, FileRecord]:` | Scan workspace and return a dictionary of normalized_posix_path -> FileRecord. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `ScanningError` — `Lines 14–16`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `16` (`Lines 14–16`)
- **الوظيفة:** Raised when an included repository file cannot be safely inspected or scanned.
- **الكود الفعلي (`Lines 14–16`):**
```python
class ScanningError(RuntimeError):
    """Raised when an included repository file cannot be safely inspected or scanned."""
    pass
```

### `calculate_stream_sha256` — `Lines 56–62`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `56` إلى السطر `62` (`Lines 56–62`)
- **الوظيفة:** Compute the SHA-256 hexadecimal digest of a file safely in 64 KiB chunks.
- **الكود الفعلي (`Lines 56–62`):**
```python
def calculate_stream_sha256(file_path: Path) -> str:
    """Compute the SHA-256 hexadecimal digest of a file safely in 64 KiB chunks."""
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()
```

### `compute_bytes_sha256` — `Lines 65–67`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `67` (`Lines 65–67`)
- **الوظيفة:** Compute SHA-256 digest of raw byte content.
- **الكود الفعلي (`Lines 65–67`):**
```python
def compute_bytes_sha256(data: bytes) -> str:
    """Compute SHA-256 digest of raw byte content."""
    return hashlib.sha256(data).hexdigest()
```

### `is_binary_file` — `Lines 70–81`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `70` إلى السطر `81` (`Lines 70–81`)
- **الوظيفة:** Check if file is binary by extension or null-byte heuristic in the first 8 KiB.
- **الكود الفعلي (`Lines 70–81`):**
```python
def is_binary_file(file_path: Path) -> bool:
    """Check if file is binary by extension or null-byte heuristic in the first 8 KiB."""
    if file_path.suffix.lower() in BINARY_EXTENSIONS:
        return True
    try:
        with file_path.open("rb") as f:
            chunk = f.read(8192)
            if b"\x00" in chunk:
                return True
    except (OSError, PermissionError):
        return False
    return False
```

### `is_secret_file` — `Lines 84–90`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `84` إلى السطر `90` (`Lines 84–90`)
- **الوظيفة:** Determine if a file name or path suggests it contains credentials/secrets.
- **الكود الفعلي (`Lines 84–90`):**
```python
def is_secret_file(file_path: Path) -> bool:
    """Determine if a file name or path suggests it contains credentials/secrets."""
    name = file_path.name
    for pattern in DEFAULT_EXCLUDED_FILE_PATTERNS[:5]:
        if pattern.match(name):
            return True
    return False
```

### `WorkspaceScanner` — `Lines 93–212`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `93` إلى السطر `212` (`Lines 93–212`)
- **الوظيفة:** Scans repository files and constructs deterministic inventory maps with fail-closed integrity.
- **الكود الفعلي (`Lines 93–212`):**
```python
class WorkspaceScanner:
    """Scans repository files and constructs deterministic inventory maps with fail-closed integrity."""

    def __init__(
        self,
        root_dir: Path,
        excluded_dirs: Optional[Set[str]] = None,
        custom_excluded_subpaths: Optional[Set[str]] = None,
        strict: bool = True
    ):
        self.root_dir = root_dir.resolve()
        self.excluded_dirs = set(DEFAULT_EXCLUDED_DIR_NAMES)
        if excluded_dirs:
            self.excluded_dirs.update(excluded_dirs)
        self.custom_excluded_subpaths = custom_excluded_subpaths or set()
        self.strict = strict
        self.errors: List[str] = []

    def should_exclude_path(self, path: Path) -> Tuple[bool, str]:
        """Check if a path should be excluded, returning (is_excluded, reason)."""
        try:
            rel = path.relative_to(self.root_dir)
        except ValueError:
            return True, "Path outside workspace root"

        rel_parts = rel.parts
        # Check parent directories
        for part in rel_parts[:-1]:
            if part in self.excluded_dirs:
                return True, f"Excluded directory: {part}"

        # Check export and output directories to prevent recursion
        posix_rel = rel.as_posix()
        if posix_rel.startswith("exports/updates/") or posix_rel == "exports/updates":
            return True, "Update package output directory"
        if posix_rel.startswith("updates/packages/") or posix_rel.startswith("updates/baselines/"):
            return True, "Legacy update directory"
        if posix_rel.startswith("tools/update_packages/registry/") or posix_rel == "tools/update_packages/registry":
            return True, "Update tool internal state registry"

        for subpath in self.custom_excluded_subpaths:
            if posix_rel.startswith(subpath):
                return True, f"Custom excluded subpath: {subpath}"

        if path.is_file():
            name = path.name
            if is_secret_file(path):
                return True, f"Secret screening exclusion: {name}"
            for pat in DEFAULT_EXCLUDED_FILE_PATTERNS:
                if pat.match(name):
                    return True, f"Excluded file pattern: {pat.pattern}"

        return False, ""

    def scan(self) -> Dict[str, FileRecord]:
        """Scan workspace and return a dictionary of normalized_posix_path -> FileRecord.
        
        Fails closed on any unexpected I/O or permission error when self.strict is True.
        """
        records: Dict[str, FileRecord] = {}
        self.errors.clear()
        if not self.root_dir.exists():
            return records

        for p in sorted(self.root_dir.rglob("*")):
            if not p.is_file():
                continue
            is_excluded, _ = self.should_exclude_path(p)
            if is_excluded:
                continue

            rel_posix = p.relative_to(self.root_dir).as_posix()

            # Audit symlink safety
            if p.is_symlink():
                try:
                    target = p.resolve()
                    if not target.is_relative_to(self.root_dir):
                        err = f"Unsafe symlink pointing outside repository root: {rel_posix} -> {target}"
                        self.errors.append(err)
                        if self.strict:
                            raise ScanningError(err)
                        continue
                except Exception as e:
                    err = f"Broken symlink {rel_posix}: {e}"
                    self.errors.append(err)
                    if self.strict:
                        raise ScanningError(err)
                    continue

            # Read file with concurrent modification check
            try:
                stat1 = p.stat()
                sha = calculate_stream_sha256(p)
                stat2 = p.stat()

                if stat1.st_mtime != stat2.st_mtime or stat1.st_size != stat2.st_size:
                    err = f"Concurrent modification detected during scan of {rel_posix}"
                    self.errors.append(err)
                    if self.strict:
                        raise ScanningError(err)

                mtime_utc = datetime.fromtimestamp(stat2.st_mtime, tz=timezone.utc).isoformat()
                records[rel_posix] = FileRecord(
                    path=rel_posix,
                    sha256=sha,
                    size_bytes=stat2.st_size,
                    is_binary=is_binary_file(p),
                    last_modified_utc=mtime_utc
                )
            except (OSError, PermissionError) as e:
                err = f"I/O or permission error inspecting file {rel_posix}: {e}"
                self.errors.append(err)
                if self.strict:
                    raise ScanningError(err)

        if self.errors and self.strict:
            raise ScanningError(f"Scanning failed closed on {len(self.errors)} error(s): {'; '.join(self.errors)}")

        return records
```

### `WorkspaceScanner.__init__` — `Lines 96–109`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `96` إلى السطر `109` (`Lines 96–109`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 96–109`):**
```python
    def __init__(
        self,
        root_dir: Path,
        excluded_dirs: Optional[Set[str]] = None,
        custom_excluded_subpaths: Optional[Set[str]] = None,
        strict: bool = True
    ):
        self.root_dir = root_dir.resolve()
        self.excluded_dirs = set(DEFAULT_EXCLUDED_DIR_NAMES)
        if excluded_dirs:
            self.excluded_dirs.update(excluded_dirs)
        self.custom_excluded_subpaths = custom_excluded_subpaths or set()
        self.strict = strict
        self.errors: List[str] = []
```

### `WorkspaceScanner.should_exclude_path` — `Lines 111–145`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `111` إلى السطر `145` (`Lines 111–145`)
- **الوظيفة:** Check if a path should be excluded, returning (is_excluded, reason).
- **الكود الفعلي (`Lines 111–145`):**
```python
    def should_exclude_path(self, path: Path) -> Tuple[bool, str]:
        """Check if a path should be excluded, returning (is_excluded, reason)."""
        try:
            rel = path.relative_to(self.root_dir)
        except ValueError:
            return True, "Path outside workspace root"

        rel_parts = rel.parts
        # Check parent directories
        for part in rel_parts[:-1]:
            if part in self.excluded_dirs:
                return True, f"Excluded directory: {part}"

        # Check export and output directories to prevent recursion
        posix_rel = rel.as_posix()
        if posix_rel.startswith("exports/updates/") or posix_rel == "exports/updates":
            return True, "Update package output directory"
        if posix_rel.startswith("updates/packages/") or posix_rel.startswith("updates/baselines/"):
            return True, "Legacy update directory"
        if posix_rel.startswith("tools/update_packages/registry/") or posix_rel == "tools/update_packages/registry":
            return True, "Update tool internal state registry"

        for subpath in self.custom_excluded_subpaths:
            if posix_rel.startswith(subpath):
                return True, f"Custom excluded subpath: {subpath}"

        if path.is_file():
            name = path.name
            if is_secret_file(path):
                return True, f"Secret screening exclusion: {name}"
            for pat in DEFAULT_EXCLUDED_FILE_PATTERNS:
                if pat.match(name):
                    return True, f"Excluded file pattern: {pat.pattern}"

        return False, ""
```

### `WorkspaceScanner.scan` — `Lines 147–212`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `147` إلى السطر `212` (`Lines 147–212`)
- **الوظيفة:** Scan workspace and return a dictionary of normalized_posix_path -> FileRecord.
- **الكود الفعلي (`Lines 147–212`):**
```python
    def scan(self) -> Dict[str, FileRecord]:
        """Scan workspace and return a dictionary of normalized_posix_path -> FileRecord.
        
        Fails closed on any unexpected I/O or permission error when self.strict is True.
        """
        records: Dict[str, FileRecord] = {}
        self.errors.clear()
        if not self.root_dir.exists():
            return records

        for p in sorted(self.root_dir.rglob("*")):
            if not p.is_file():
                continue
            is_excluded, _ = self.should_exclude_path(p)
            if is_excluded:
                continue

            rel_posix = p.relative_to(self.root_dir).as_posix()

            # Audit symlink safety
            if p.is_symlink():
                try:
                    target = p.resolve()
                    if not target.is_relative_to(self.root_dir):
                        err = f"Unsafe symlink pointing outside repository root: {rel_posix} -> {target}"
                        self.errors.append(err)
                        if self.strict:
                            raise ScanningError(err)
                        continue
                except Exception as e:
                    err = f"Broken symlink {rel_posix}: {e}"
                    self.errors.append(err)
                    if self.strict:
                        raise ScanningError(err)
                    continue

            # Read file with concurrent modification check
            try:
                stat1 = p.stat()
                sha = calculate_stream_sha256(p)
                stat2 = p.stat()

                if stat1.st_mtime != stat2.st_mtime or stat1.st_size != stat2.st_size:
                    err = f"Concurrent modification detected during scan of {rel_posix}"
                    self.errors.append(err)
                    if self.strict:
                        raise ScanningError(err)

                mtime_utc = datetime.fromtimestamp(stat2.st_mtime, tz=timezone.utc).isoformat()
                records[rel_posix] = FileRecord(
                    path=rel_posix,
                    sha256=sha,
                    size_bytes=stat2.st_size,
                    is_binary=is_binary_file(p),
                    last_modified_utc=mtime_utc
                )
            except (OSError, PermissionError) as e:
                err = f"I/O or permission error inspecting file {rel_posix}: {e}"
                self.errors.append(err)
                if self.strict:
                    raise ScanningError(err)

        if self.errors and self.strict:
            raise ScanningError(f"Scanning failed closed on {len(self.errors)} error(s): {'; '.join(self.errors)}")

        return records
```
