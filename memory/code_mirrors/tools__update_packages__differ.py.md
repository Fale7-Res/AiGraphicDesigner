# مرآة الكود التفصيلية: `tools/update_packages/differ.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/update_packages/differ.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/update_packages/differ.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `128` (`Lines 1–128`)
- **بصمة الملف (`SHA-256`):** `7363d07cb8e769b0e75e34cfaa82a9b932f98205f2252ec67d79ac201c40478b`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `InventoryDiffer` | `class` | `Lines 10–127` | `class InventoryDiffer:` | Computes exact, tamper-evident file mutations between base and target inventories. |
| `InventoryDiffer.compute_diff` | `method` | `Lines 14–127` | `def compute_diff(` | Compare base and target file inventories, detecting adds, mods, deletes, and renames. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `InventoryDiffer` — `Lines 10–127`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `127` (`Lines 10–127`)
- **الوظيفة:** Computes exact, tamper-evident file mutations between base and target inventories.
- **الكود الفعلي (`Lines 10–127`):**
```python
class InventoryDiffer:
    """Computes exact, tamper-evident file mutations between base and target inventories."""

    @staticmethod
    def compute_diff(
        base_files: Dict[str, FileRecord],
        target_files: Dict[str, FileRecord]
    ) -> Tuple[List[ManifestEntry], Dict[str, int]]:
        """Compare base and target file inventories, detecting adds, mods, deletes, and renames.

        Returns:
            (manifest_entries, operations_summary)
        """
        base_paths: Set[str] = set(base_files.keys())
        target_paths: Set[str] = set(target_files.keys())

        common_paths = base_paths & target_paths
        raw_added_paths = target_paths - base_paths
        raw_deleted_paths = base_paths - target_paths

        # Index by SHA-256 for rename detection (only for non-empty files)
        deleted_by_hash: Dict[str, List[str]] = {}
        for p in raw_deleted_paths:
            h = base_files[p].sha256
            if base_files[p].size_bytes > 0:
                deleted_by_hash.setdefault(h, []).append(p)

        renames: Dict[str, str] = {}  # new_path -> old_path
        claimed_deleted: Set[str] = set()

        for new_p in sorted(raw_added_paths):
            h = target_files[new_p].sha256
            if h in deleted_by_hash and deleted_by_hash[h]:
                # Candidate rename found
                old_p = deleted_by_hash[h].pop(0)
                renames[new_p] = old_p
                claimed_deleted.add(old_p)

        remaining_added = raw_added_paths - set(renames.keys())
        remaining_deleted = raw_deleted_paths - claimed_deleted

        entries: List[ManifestEntry] = []
        summary = {
            "added": 0,
            "modified": 0,
            "deleted": 0,
            "renamed": 0,
            "unchanged": 0
        }

        # 1. Modified & Unchanged
        for p in sorted(common_paths):
            base_rec = base_files[p]
            target_rec = target_files[p]
            if base_rec.sha256 != target_rec.sha256:
                entries.append(ManifestEntry(
                    path=p,
                    operation=FileOperation.MODIFY.value,
                    previous_sha256=base_rec.sha256,
                    new_sha256=target_rec.sha256,
                    size_bytes=target_rec.size_bytes,
                    is_binary=target_rec.is_binary,
                    payload_path=f"payload/{p}",
                    payload_sha256=target_rec.sha256
                ))
                summary["modified"] += 1
            else:
                summary["unchanged"] += 1

        # 2. Renamed
        for new_p, old_p in sorted(renames.items()):
            target_rec = target_files[new_p]
            base_rec = base_files[old_p]
            entries.append(ManifestEntry(
                path=new_p,
                operation=FileOperation.RENAME.value,
                previous_sha256=base_rec.sha256,
                new_sha256=target_rec.sha256,
                size_bytes=target_rec.size_bytes,
                is_binary=target_rec.is_binary,
                payload_path=f"payload/{new_p}",
                payload_sha256=target_rec.sha256,
                renamed_from=old_p
            ))
            summary["renamed"] += 1

        # 3. Added
        for p in sorted(remaining_added):
            target_rec = target_files[p]
            entries.append(ManifestEntry(
                path=p,
                operation=FileOperation.ADD.value,
                previous_sha256=None,
                new_sha256=target_rec.sha256,
                size_bytes=target_rec.size_bytes,
                is_binary=target_rec.is_binary,
                payload_path=f"payload/{p}",
                payload_sha256=target_rec.sha256
            ))
            summary["added"] += 1

        # 4. Deleted
        for p in sorted(remaining_deleted):
            base_rec = base_files[p]
            entries.append(ManifestEntry(
                path=p,
                operation=FileOperation.DELETE.value,
                previous_sha256=base_rec.sha256,
                new_sha256=None,
                size_bytes=0,
                is_binary=base_rec.is_binary,
                payload_path=None,
                payload_sha256=None
            ))
            summary["deleted"] += 1

        entries.sort(key=lambda e: e.path)
        return entries, summary
```

### `InventoryDiffer.compute_diff` — `Lines 14–127`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `127` (`Lines 14–127`)
- **الوظيفة:** Compare base and target file inventories, detecting adds, mods, deletes, and renames.
- **الكود الفعلي (`Lines 14–127`):**
```python
    def compute_diff(
        base_files: Dict[str, FileRecord],
        target_files: Dict[str, FileRecord]
    ) -> Tuple[List[ManifestEntry], Dict[str, int]]:
        """Compare base and target file inventories, detecting adds, mods, deletes, and renames.

        Returns:
            (manifest_entries, operations_summary)
        """
        base_paths: Set[str] = set(base_files.keys())
        target_paths: Set[str] = set(target_files.keys())

        common_paths = base_paths & target_paths
        raw_added_paths = target_paths - base_paths
        raw_deleted_paths = base_paths - target_paths

        # Index by SHA-256 for rename detection (only for non-empty files)
        deleted_by_hash: Dict[str, List[str]] = {}
        for p in raw_deleted_paths:
            h = base_files[p].sha256
            if base_files[p].size_bytes > 0:
                deleted_by_hash.setdefault(h, []).append(p)

        renames: Dict[str, str] = {}  # new_path -> old_path
        claimed_deleted: Set[str] = set()

        for new_p in sorted(raw_added_paths):
            h = target_files[new_p].sha256
            if h in deleted_by_hash and deleted_by_hash[h]:
                # Candidate rename found
                old_p = deleted_by_hash[h].pop(0)
                renames[new_p] = old_p
                claimed_deleted.add(old_p)

        remaining_added = raw_added_paths - set(renames.keys())
        remaining_deleted = raw_deleted_paths - claimed_deleted

        entries: List[ManifestEntry] = []
        summary = {
            "added": 0,
            "modified": 0,
            "deleted": 0,
            "renamed": 0,
            "unchanged": 0
        }

        # 1. Modified & Unchanged
        for p in sorted(common_paths):
            base_rec = base_files[p]
            target_rec = target_files[p]
            if base_rec.sha256 != target_rec.sha256:
                entries.append(ManifestEntry(
                    path=p,
                    operation=FileOperation.MODIFY.value,
                    previous_sha256=base_rec.sha256,
                    new_sha256=target_rec.sha256,
                    size_bytes=target_rec.size_bytes,
                    is_binary=target_rec.is_binary,
                    payload_path=f"payload/{p}",
                    payload_sha256=target_rec.sha256
                ))
                summary["modified"] += 1
            else:
                summary["unchanged"] += 1

        # 2. Renamed
        for new_p, old_p in sorted(renames.items()):
            target_rec = target_files[new_p]
            base_rec = base_files[old_p]
            entries.append(ManifestEntry(
                path=new_p,
                operation=FileOperation.RENAME.value,
                previous_sha256=base_rec.sha256,
                new_sha256=target_rec.sha256,
                size_bytes=target_rec.size_bytes,
                is_binary=target_rec.is_binary,
                payload_path=f"payload/{new_p}",
                payload_sha256=target_rec.sha256,
                renamed_from=old_p
            ))
            summary["renamed"] += 1

        # 3. Added
        for p in sorted(remaining_added):
            target_rec = target_files[p]
            entries.append(ManifestEntry(
                path=p,
                operation=FileOperation.ADD.value,
                previous_sha256=None,
                new_sha256=target_rec.sha256,
                size_bytes=target_rec.size_bytes,
                is_binary=target_rec.is_binary,
                payload_path=f"payload/{p}",
                payload_sha256=target_rec.sha256
            ))
            summary["added"] += 1

        # 4. Deleted
        for p in sorted(remaining_deleted):
            base_rec = base_files[p]
            entries.append(ManifestEntry(
                path=p,
                operation=FileOperation.DELETE.value,
                previous_sha256=base_rec.sha256,
                new_sha256=None,
                size_bytes=0,
                is_binary=base_rec.is_binary,
                payload_path=None,
                payload_sha256=None
            ))
            summary["deleted"] += 1

        entries.sort(key=lambda e: e.path)
        return entries, summary
```
