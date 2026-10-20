# مرآة الكود التفصيلية: `tools/governance/change_tracking.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/governance/change_tracking.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/governance/change_tracking.py`
- **الدور المعماري (`Architectural Role`):** First-Party Source Module
- **إجمالي عدد الأسطر (`Total Lines`):** `239` (`Lines 1–239`)
- **بصمة الملف (`SHA-256`):** `9c1e5584f8213fa4972573dec2870278d2ffb97fabcaeba9c361d659c4d3be29`
- **الوصف التفصيلي:** ملف برمجي ضمن معمارية AI Graphic Designer.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `utcnow` | `function` | `Lines 39–41` | `def utcnow():` | Current instant formatted as portable UTC ISO-8601. |
| `sha` | `function` | `Lines 44–46` | `def sha(data):` | SHA-256 of a UTF-8 string. |
| `governed_doc` | `function` | `Lines 50–60` | `def governed_doc(relative):` | Decide whether a Markdown file is safe for inline mutable provenance. |
| `iter_files` | `function` | `Lines 64–72` | `def iter_files():` | Discover tracked first-party files, excluding generated runtime directories. |
| `markdown_header` | `function` | `Lines 75–79` | `def markdown_header(meta):` | Produce machine-readable inline provenance with explicit legacy unknowns. |
| `embed_header` | `function` | `Lines 82–92` | `def embed_header(text, meta):` | Update an existing header or insert it after frontmatter, preserving Markdown/YAML semantics. |
| `load_manifest` | `function` | `Lines 95–99` | `def load_manifest():` | Read the authority record or create an empty structure. |
| `initialize` | `function` | `Lines 102–123` | `def initialize():` | Import existing mutable docs; import does NOT fabricate past creation time. |
| `edit_document` | `function` | `Lines 126–150` | `def edit_document(rel, kind, change_id, editor):` | Update doc timestamps and digest; never silently rewrite historical event entries. |
| `check_source_stamps` | `function` | `Lines 153–185` | `def check_source_stamps(rel, text):` | Detect malformed timestamps, unmatched regions, mismatched IDs, and misplaced END markers. |
| `verify` | `function` | `Lines 188–212` | `def verify():` | Verify all human documentation metadata and syntax of source-region stamps. |
| `main` | `function` | `Lines 215–234` | `def main():` | CLI entrypoint. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `utcnow` — `Lines 39–41`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `39` إلى السطر `41` (`Lines 39–41`)
- **الوظيفة:** Current instant formatted as portable UTC ISO-8601.
- **الكود الفعلي (`Lines 39–41`):**
```python
def utcnow():
    """Current instant formatted as portable UTC ISO-8601."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
```

### `sha` — `Lines 44–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `46` (`Lines 44–46`)
- **الوظيفة:** SHA-256 of a UTF-8 string.
- **الكود الفعلي (`Lines 44–46`):**
```python
def sha(data):
    """SHA-256 of a UTF-8 string."""
    return sha256(data.encode("utf-8")).hexdigest()
```

### `governed_doc` — `Lines 50–60`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `50` إلى السطر `60` (`Lines 50–60`)
- **الوظيفة:** Decide whether a Markdown file is safe for inline mutable provenance.
- **الكود الفعلي (`Lines 50–60`):**
```python
def governed_doc(relative):
    """Decide whether a Markdown file is safe for inline mutable provenance."""
    if relative in SKIP_DOC_PATHS:
        return False
    if relative.startswith(("docs/history/", "memory/code_mirrors/", ".agents/rules/")):
        return False
    if "/docs/CODE_MIRRORS/" in relative:
        return False
    if relative.endswith("PROJECT_FILE_CATALOG.md") or relative.endswith("FUNCTION_REGISTRY.md"):
        return False
    return relative.endswith(".md")
```

### `iter_files` — `Lines 64–72`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `64` إلى السطر `72` (`Lines 64–72`)
- **الوظيفة:** Discover tracked first-party files, excluding generated runtime directories.
- **الكود الفعلي (`Lines 64–72`):**
```python
def iter_files():
    """Discover tracked first-party files, excluding generated runtime directories."""
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or any(part in OMITTED_DIRS for part in p.relative_to(ROOT).parts[:-1]):
            continue
        if p.relative_to(ROOT).as_posix().startswith("updates/"):
            # static guidance docs in updates are still eligible
            pass
        yield p, p.relative_to(ROOT).as_posix()
```

### `markdown_header` — `Lines 75–79`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `75` إلى السطر `79` (`Lines 75–79`)
- **الوظيفة:** Produce machine-readable inline provenance with explicit legacy unknowns.
- **الكود الفعلي (`Lines 75–79`):**
```python
def markdown_header(meta):
    """Produce machine-readable inline provenance with explicit legacy unknowns."""
    return ("<!-- DOC_PROVENANCE\n"
            + json.dumps(meta, ensure_ascii=False, sort_keys=True)
            + "\nEND_DOC_PROVENANCE -->")
```

### `embed_header` — `Lines 82–92`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `82` إلى السطر `92` (`Lines 82–92`)
- **الوظيفة:** Update an existing header or insert it after frontmatter, preserving Markdown/YAML semantics.
- **الكود الفعلي (`Lines 82–92`):**
```python
def embed_header(text, meta):
    """Update an existing header or insert it after frontmatter, preserving Markdown/YAML semantics."""
    current = PROVENANCE_RE.search(text)
    if current:
        return text[:current.start()] + markdown_header(meta) + text[current.end():]
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end >= 0:
            pos = end + 5
            return text[:pos] + markdown_header(meta) + "\n" + text[pos:]
    return markdown_header(meta) + "\n" + text
```

### `load_manifest` — `Lines 95–99`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `95` إلى السطر `99` (`Lines 95–99`)
- **الوظيفة:** Read the authority record or create an empty structure.
- **الكود الفعلي (`Lines 95–99`):**
```python
def load_manifest():
    """Read the authority record or create an empty structure."""
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {
        "schema": "1.0", "policy": "BASELINE_WITH_APPEND_ONLY_EVENTS", "documents": {}
    }
```

### `initialize` — `Lines 102–123`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `102` إلى السطر `123` (`Lines 102–123`)
- **الوظيفة:** Import existing mutable docs; import does NOT fabricate past creation time.
- **الكود الفعلي (`Lines 102–123`):**
```python
def initialize():
    """Import existing mutable docs; import does NOT fabricate past creation time."""
    if MANIFEST.exists():
        raise SystemExit("Already initialized; use edit-document for subsequent edits")
    instant = utcnow()
    record = load_manifest()
    for p, rel in iter_files():
        if not governed_doc(rel):
            continue
        orig = p.read_text(encoding="utf-8")
        meta = {
            "created_at_utc": None, "last_edited_at_utc": None,
            "tracking_started_at_utc": instant, "last_action": "IMPORTED_LEGACY",
            "last_change_id": "BASELINE-IMPORT", "last_editor": "governance-baseline",
        }
        result = embed_header(orig, meta)
        p.write_text(result, encoding="utf-8")
        record["documents"][rel] = {"metadata": meta, "sha256": sha(result),
                                    "events": [{"at_utc": instant, "action": "IMPORTED_LEGACY", "change_id": "BASELINE-IMPORT"}]}
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("Imported", len(record["documents"]), "mutable documentation records")
```

### `edit_document` — `Lines 126–150`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `126` إلى السطر `150` (`Lines 126–150`)
- **الوظيفة:** Update doc timestamps and digest; never silently rewrite historical event entries.
- **الكود الفعلي (`Lines 126–150`):**
```python
def edit_document(rel, kind, change_id, editor):
    """Update doc timestamps and digest; never silently rewrite historical event entries."""
    if not governed_doc(rel):
        raise ValueError("Immutable/generated/promotion-tracked file: requires its own governance protocol")
    p = (ROOT / rel).resolve()
    if not p.is_relative_to(ROOT.resolve()) or not p.is_file():
        raise ValueError("Target doc missing or escapes repository")
    manifest = load_manifest()
    old = manifest["documents"].get(rel)
    if kind == "CREATED" and old:
        raise ValueError("CREATED cannot overwrite a previously registered document")
    if kind == "EDITED" and not old:
        raise ValueError("Untracked file cannot be labeled edited; classify CREATED or import")
    instant = utcnow()
    meta = dict(old["metadata"]) if old else {
        "created_at_utc": instant, "tracking_started_at_utc": instant,
    }
    meta.update(last_edited_at_utc=instant, last_action=kind,
                last_change_id=change_id, last_editor=editor)
    updated = embed_header(p.read_text(encoding="utf-8"), meta)
    p.write_text(updated, encoding="utf-8")
    events = list(old["events"]) if old else []
    events.append({"at_utc": instant, "action": kind, "change_id": change_id, "editor": editor})
    manifest["documents"][rel] = {"metadata": meta, "sha256": sha(updated), "events": events}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
```

### `check_source_stamps` — `Lines 153–185`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `153` إلى السطر `185` (`Lines 153–185`)
- **الوظيفة:** Detect malformed timestamps, unmatched regions, mismatched IDs, and misplaced END markers.
- **الكود الفعلي (`Lines 153–185`):**
```python
def check_source_stamps(rel, text):
    """Detect malformed timestamps, unmatched regions, mismatched IDs, and misplaced END markers."""
    errors = []
    stack = []
    for ln, line in enumerate(text.splitlines(), 1):
        if not re.match(r"^\s*(?:#|//|/\*|\*)\s+(?:START|END) CHANGE ", line):
            continue
        if not line.lstrip().startswith(("# ", "// ", "/* ", "* ")):
            errors.append(f"{rel}:{ln} change marker must be inside a language comment")
            continue
        m = CHANGE_RE.search(line)
        if not m:
            errors.append(f"{rel}:{ln} malformed change marker")
            continue
        try:
            datetime.strptime(m.group(2), "%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            errors.append(f"{rel}:{ln} invalid UTC date/time")
        signature = m.group(1, 2, 3)
        if "START CHANGE " in line:
            if not m.group(4):
                errors.append(f"{rel}:{ln} START requires author")
            stack.append((signature, ln))
        else:
            if not stack:
                errors.append(f"{rel}:{ln} orphan END CHANGE")
            else:
                opened, open_line = stack.pop()
                if opened != signature:
                    errors.append(f"{rel}:{open_line}-{ln} mismatched change region")
    if stack:
        errors.extend(f"{rel}:{line} unterminated START CHANGE" for _, line in stack)
    return errors
```

### `verify` — `Lines 188–212`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `188` إلى السطر `212` (`Lines 188–212`)
- **الوظيفة:** Verify all human documentation metadata and syntax of source-region stamps.
- **الكود الفعلي (`Lines 188–212`):**
```python
def verify():
    """Verify all human documentation metadata and syntax of source-region stamps."""
    errors = []
    record = load_manifest()
    docs = {rel for _, rel in iter_files() if governed_doc(rel)}
    if docs != set(record["documents"]):
        errors.append(f"Documentation registry drift: missing={sorted(docs-set(record['documents']))} stale={sorted(set(record['documents'])-docs)}")
    for p, rel in iter_files():
        text = p.read_text(encoding="utf-8", errors="replace") if p.suffix.lower() in (".md", ".py", ".js", ".ts", ".tsx", ".jsx") else ""
        if governed_doc(rel):
            match = PROVENANCE_RE.search(text)
            ent = record["documents"].get(rel)
            if not match or not ent:
                errors.append(f"Missing provenance metadata: {rel}")
                continue
            try:
                meta = json.loads(match.group(1))
            except json.JSONDecodeError:
                errors.append(f"Broken provenance JSON: {rel}")
                continue
            if meta != ent["metadata"] or sha(text) != ent["sha256"]:
                errors.append(f"Stale or unauthorized Markdown provenance: {rel}")
        if p.suffix.lower() in (".py", ".js", ".ts", ".tsx", ".jsx"):
            errors.extend(check_source_stamps(rel, text))
    return errors
```

### `main` — `Lines 215–234`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `215` إلى السطر `234` (`Lines 215–234`)
- **الوظيفة:** CLI entrypoint.
- **الكود الفعلي (`Lines 215–234`):**
```python
def main():
    """CLI entrypoint."""
    cli = argparse.ArgumentParser()
    cli.add_argument("command", choices=["initialize", "verify", "edit-document"])
    cli.add_argument("--file", default="")
    cli.add_argument("--kind", choices=["CREATED", "EDITED"])
    cli.add_argument("--change-id", default="")
    cli.add_argument("--editor", default="")
    args = cli.parse_args()
    if args.command == "initialize":
        initialize()
    elif args.command == "edit-document":
        if not all((args.file, args.kind, args.change_id, args.editor)):
            raise SystemExit("edit-document needs --file --kind --change-id --editor")
        edit_document(args.file, args.kind, args.change_id, args.editor)
    else:
        errors = verify()
        print(json.dumps({"status": "PASS" if not errors else "FAIL", "documents": len(load_manifest().get("documents", {})), "errors": errors}, ensure_ascii=False))
        if errors:
            raise SystemExit(1)
```
