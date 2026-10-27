#!/usr/bin/env python3
"""Source-region START/END stamps and human-authored Markdown provenance.

A source change stamp describes the newly authored/edited region; it is NOT
historical proof of the original creation time of surrounding legacy code.
The Markdown manifest is an auditable repository record, not a cryptographic
owner-signature or tamper-proof archive. Use protected Git review to secure it.
"""
# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:52:14Z | CREATED | Author: Governance maintainer
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
import argparse
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "memory" / "DOCUMENT_PROVENANCE.json"
SOURCE_EXT = {".py": "#", ".ts": "//", ".tsx": "//", ".js": "//", ".jsx": "//", ".css": "/*"}
OMITTED_DIRS = {"__pycache__", ".git", ".venv", "node_modules", "baselines", "latest", "packages"}
SKIP_DOC_PATHS = {
    "docs/product/OWNER_ORIGINAL_VISION.md",
    "docs/SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md",  # historical promotion target
    "docs/architecture/FEASIBILITY_EXPERIMENTS_AND_GATES.md",  # historical promotion target
    "memory/decisions/DECISION_LOG.md",  # historical promotion target
    "PROJECT_FILE_CATALOG.md", "memory/FUNCTION_REGISTRY.md",
    "memory/findings/FINDINGS_LEDGER.md", "memory/session/ACTIVE_SESSION_WAL.md",
    "memory/session/CURRENT_TASK_CHECKPOINT.md",
}
PROVENANCE_RE = re.compile(r"<!-- DOC_PROVENANCE\n(.*?)\nEND_DOC_PROVENANCE -->", re.S)
CHANGE_RE = re.compile(
    r"(?:START|END) CHANGE ([A-Za-z0-9_-]+) \| "
    r"(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ) \| "
    r"(CREATED|EDITED)(?: \| Author: (.*))?"
)


def utcnow():
    """Current instant formatted as portable UTC ISO-8601."""
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def sha(data):
    """SHA-256 of a UTF-8 string."""
    return sha256(data.encode("utf-8")).hexdigest()


# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:43:00Z | EDITED | Author: orchestrator-planner
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
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:43:00Z | EDITED


def iter_files():
    """Discover tracked first-party files, excluding generated runtime directories."""
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or any(part in OMITTED_DIRS for part in p.relative_to(ROOT).parts[:-1]):
            continue
        if p.relative_to(ROOT).as_posix().startswith("updates/"):
            # static guidance docs in updates are still eligible
            pass
        yield p, p.relative_to(ROOT).as_posix()


def markdown_header(meta):
    """Produce machine-readable inline provenance with explicit legacy unknowns."""
    return ("<!-- DOC_PROVENANCE\n"
            + json.dumps(meta, ensure_ascii=False, sort_keys=True)
            + "\nEND_DOC_PROVENANCE -->")


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


def load_manifest():
    """Read the authority record or create an empty structure."""
    return json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {
        "schema": "1.0", "policy": "BASELINE_WITH_APPEND_ONLY_EVENTS", "documents": {}
    }


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


if __name__ == "__main__":
    main()
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:52:14Z | CREATED
