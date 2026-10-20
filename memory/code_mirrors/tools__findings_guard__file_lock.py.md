# مرآة الكود التفصيلية: `tools/findings_guard/file_lock.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/findings_guard/file_lock.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/findings_guard/file_lock.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `61` (`Lines 1–61`)
- **بصمة الملف (`SHA-256`):** `5011973ed4aff6855667c09b3273220ad7b1c5ad8f4fdce479b9c6c321de9257`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `repository_lock` | `function` | `Lines 17–60` | `def repository_lock(repository_root: Path, purpose: str, timeout_seconds: float = 90):` | Hold a named OS lock across processes, supporting Windows and POSIX. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `repository_lock` — `Lines 17–60`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `60` (`Lines 17–60`)
- **الوظيفة:** Hold a named OS lock across processes, supporting Windows and POSIX.
- **الكود الفعلي (`Lines 17–60`):**
```python
def repository_lock(repository_root: Path, purpose: str, timeout_seconds: float = 90):
    """Hold a named OS lock across processes, supporting Windows and POSIX."""
    identifier = sha256(str(repository_root.resolve()).casefold().encode("utf-8")).hexdigest()[:22]
    lockfile = Path(tempfile.gettempdir()) / f"agd-{purpose}-{identifier}.lock"
    handle = open(lockfile, "a+b")
    acquired = False
    try:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        end = time.monotonic() + timeout_seconds
        if os.name == "nt":
            import msvcrt
            while not acquired:
                try:
                    handle.seek(0)
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    acquired = True
                except OSError:
                    if time.monotonic() >= end:
                        raise TimeoutError(f"Timed out acquiring {purpose} lock")
                    time.sleep(0.05)
        else:
            import fcntl
            while not acquired:
                try:
                    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    acquired = True
                except BlockingIOError:
                    if time.monotonic() >= end:
                        raise TimeoutError(f"Timed out acquiring {purpose} lock")
                    time.sleep(0.05)
        yield
    finally:
        if acquired:
            if os.name == "nt":
                import msvcrt
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()
```
