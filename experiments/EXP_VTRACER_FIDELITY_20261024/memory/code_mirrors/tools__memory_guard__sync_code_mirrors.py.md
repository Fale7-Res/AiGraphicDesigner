# مرآة الكود التفصيلية: `tools/memory_guard/sync_code_mirrors.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/sync_code_mirrors.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/sync_code_mirrors.py`
- **الدور المعماري (`Architectural Role`):** Bounded isolated research or verification
- **إجمالي عدد الأسطر (`Total Lines`):** `743` (`Lines 1–743`)
- **بصمة الملف (`SHA-256`):** `01b7b505fdbaf369fb6c197dd56c02292b8c94570a29e791510e0f0354462708`
- **الوصف التفصيلي:** #!/usr/bin/env python3

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `source PNG, frozen SVG, configuration or saved evidence` | geometry, RGB, metrics | Reproducible scoped research |
| **يرمي إلى (`Throws To`)** | `results, reports, or scoped memory` | SVG, native renders or verification evidence | No production change |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `mirror_filename_for` | `function` | `Lines 37–40` | `def mirror_filename_for(rel_path: str) -> str:` | Convert a repository-relative file path into its memory/code_mirrors/ filename. |
| `discover_code_files` | `function` | `Lines 43–54` | `def discover_code_files() -> list[Path]:` | Return sorted list of all first-party code files in the repository. |
| `compute_python_ast_skeleton` | `function` | `Lines 57–85` | `def compute_python_ast_skeleton(node: ast.AST) -> str:` | Compute a normalized structural skeleton string for a Python AST function/method node. |
| `extract_python_symbols` | `function` | `Lines 88–130` | `def extract_python_symbols(file_path: Path) -> list[dict]:` | Recursively parse a Python file via AST and extract classes, methods, functions, and nested symbols. |
| `extract_python_symbols.visit_block` | `nested_function` | `Lines 95–127` | `def visit_block(body: list[ast.stmt], parent_qual: str = "", parent_kind: str = "") -> None:` | رمز برمجي موثق. |
| `strip_js_comments_and_strings` | `function` | `Lines 133–138` | `def strip_js_comments_and_strings(line: str) -> str:` | Replace string literals and line comments with spaces while preserving brace structure. |
| `find_block_end` | `function` | `Lines 141–162` | `def find_block_end(lines: list[str], start_idx: int) -> int:` | Find 1-indexed end line of a brace-delimited or statement block starting at 0-indexed start_idx. |
| `extract_ts_js_symbols` | `function` | `Lines 165–311` | `def extract_ts_js_symbols(file_path: Path) -> list[dict]:` | Extract functions, arrow functions, classes, class methods, nested symbols, and exported declarations in TS/JS. |
| `detect_duplicate_functions` | `function` | `Lines 314–340` | `def detect_duplicate_functions(all_file_symbols: dict[str, list[dict]]) -> list[dict]:` | Level 1 (Deterministic Blocking): Detect exact-name duplicate top-level functions/classes across files. |
| `detect_structural_similarity` | `function` | `Lines 343–361` | `def detect_structural_similarity(all_file_symbols: dict[str, list[dict]]) -> list[dict]:` | Level 2 (Heuristic AST Skeleton Check): Identify functions with identical non-trivial AST skeletons. |
| `render_mirror_markdown` | `function` | `Lines 364–442` | `def render_mirror_markdown(rel_path: str, file_path: Path, symbols: list[dict], meta: dict) -> str:` | Render the 1:1 Code Mirror Markdown file with explicit source-authority header. |
| `render_function_registry` | `function` | `Lines 445–484` | `def render_function_registry(` | Render the central memory/FUNCTION_REGISTRY.md file with 3-tier deduplication status. |
| `discover_version_ids` | `function` | `Lines 488–492` | `def discover_version_ids() -> list[str]:` | Return sorted list of all active version directory names in versions/. |
| `discover_version_code_files` | `function` | `Lines 495–510` | `def discover_version_code_files(version_id: str) -> list[Path]:` | Return sorted list of code files belonging to a specific version. |
| `render_version_mirror_markdown` | `function` | `Lines 513–568` | `def render_version_mirror_markdown(rel_in_version: str, file_path: Path, symbols: list[dict], version_id: str) -> str:` | Render 1:1 Code Mirror for a version-scoped source file. |
| `render_version_function_registry` | `function` | `Lines 571–605` | `def render_version_function_registry(` | Render the version-scoped FUNCTION_REGISTRY.md with 3-tier deduplication. |
| `sync_version` | `function` | `Lines 608–657` | `def sync_version(version_id: str, write_mode: bool = False) -> dict:` | Synchronize code mirrors and function registry for a specific version. |
| `sync_root` | `function` | `Lines 660–702` | `def sync_root(write_mode: bool = False) -> dict:` | Synchronize root codebase mirrors and central FUNCTION_REGISTRY.md. |
| `main` | `function` | `Lines 705–737` | `def main() -> None:` | Synchronize all code mirrors and function registries across root and registered versions. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `mirror_filename_for` — `Lines 37–40`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `37` إلى السطر `40` (`Lines 37–40`)
- **الوظيفة:** Convert a repository-relative file path into its memory/code_mirrors/ filename.
- **الكود الفعلي (`Lines 37–40`):**
```python
def mirror_filename_for(rel_path: str) -> str:
    """Convert a repository-relative file path into its memory/code_mirrors/ filename."""
    safe_name = rel_path.replace("/", "__").replace("\\", "__")
    return f"{safe_name}.md"
```

### `discover_code_files` — `Lines 43–54`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `43` إلى السطر `54` (`Lines 43–54`)
- **الوظيفة:** Return sorted list of all first-party code files in the repository.
- **الكود الفعلي (`Lines 43–54`):**
```python
def discover_code_files() -> list[Path]:
    """Return sorted list of all first-party code files in the repository."""
    found: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(ROOT).parts
        if any(part in EXCLUDED_DIRS for part in rel_parts[:-1]):
            continue
        if path.suffix.lower() in CODE_EXTENSIONS:
            found.append(path)
    return sorted(found, key=lambda p: p.relative_to(ROOT).as_posix())
```

### `compute_python_ast_skeleton` — `Lines 57–85`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `85` (`Lines 57–85`)
- **الوظيفة:** Compute a normalized structural skeleton string for a Python AST function/method node.
- **الكود الفعلي (`Lines 57–85`):**
```python
def compute_python_ast_skeleton(node: ast.AST) -> str:
    """Compute a normalized structural skeleton string for a Python AST function/method node."""
    tokens: list[str] = []
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        tokens.append(f"Func(args={len(node.args.args)})")
    for child in ast.walk(node):
        if isinstance(child, (ast.For, ast.AsyncFor)):
            tokens.append("For")
        elif isinstance(child, ast.While):
            tokens.append("While")
        elif isinstance(child, ast.If):
            tokens.append("If")
        elif isinstance(child, ast.Try):
            tokens.append("Try")
        elif isinstance(child, (ast.With, ast.AsyncWith)):
            tokens.append("With")
        elif isinstance(child, ast.Return):
            tokens.append("Return")
        elif isinstance(child, (ast.Yield, ast.YieldFrom)):
            tokens.append("Yield")
        elif isinstance(child, ast.Raise):
            tokens.append("Raise")
        elif isinstance(child, ast.ListComp):
            tokens.append("ListComp")
        elif isinstance(child, ast.DictComp):
            tokens.append("DictComp")
        elif isinstance(child, ast.Call):
            tokens.append("Call")
    return "->".join(tokens)
```

### `extract_python_symbols` — `Lines 88–130`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `88` إلى السطر `130` (`Lines 88–130`)
- **الوظيفة:** Recursively parse a Python file via AST and extract classes, methods, functions, and nested symbols.
- **الكود الفعلي (`Lines 88–130`):**
```python
def extract_python_symbols(file_path: Path) -> list[dict]:
    """Recursively parse a Python file via AST and extract classes, methods, functions, and nested symbols."""
    source_text = file_path.read_text(encoding="utf-8")
    lines = source_text.splitlines()
    tree = ast.parse(source_text, filename=str(file_path))
    symbols: list[dict] = []

    def visit_block(body: list[ast.stmt], parent_qual: str = "", parent_kind: str = "") -> None:
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start_line = node.lineno
                end_line = getattr(node, "end_lineno", start_line)
                qual_name = f"{parent_qual}.{node.name}" if parent_qual else node.name
                if isinstance(node, ast.ClassDef):
                    kind = "nested_class" if parent_qual else "class"
                else:
                    if parent_kind in {"class", "nested_class"}:
                        kind = "method"
                    elif parent_qual:
                        kind = "nested_function"
                    else:
                        kind = "function"

                snippet_lines = lines[start_line - 1 : end_line]
                signature = lines[start_line - 1].strip()
                docstring = ast.get_docstring(node) or ""
                skeleton = compute_python_ast_skeleton(node) if kind != "class" else f"Class(methods={len(node.body)})"
                symbols.append({
                    "name": qual_name,
                    "raw_name": node.name,
                    "kind": kind,
                    "start_line": start_line,
                    "end_line": end_line,
                    "signature": signature,
                    "docstring": docstring.splitlines()[0] if docstring else "",
                    "snippet": "\n".join(snippet_lines),
                    "ast_skeleton": skeleton,
                    "language": "python",
                })
                visit_block(node.body, parent_qual=qual_name, parent_kind=kind)

    visit_block(tree.body)
    return symbols
```

### `extract_python_symbols.visit_block` — `Lines 95–127`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `95` إلى السطر `127` (`Lines 95–127`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 95–127`):**
```python
    def visit_block(body: list[ast.stmt], parent_qual: str = "", parent_kind: str = "") -> None:
        for node in body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                start_line = node.lineno
                end_line = getattr(node, "end_lineno", start_line)
                qual_name = f"{parent_qual}.{node.name}" if parent_qual else node.name
                if isinstance(node, ast.ClassDef):
                    kind = "nested_class" if parent_qual else "class"
                else:
                    if parent_kind in {"class", "nested_class"}:
                        kind = "method"
                    elif parent_qual:
                        kind = "nested_function"
                    else:
                        kind = "function"

                snippet_lines = lines[start_line - 1 : end_line]
                signature = lines[start_line - 1].strip()
                docstring = ast.get_docstring(node) or ""
                skeleton = compute_python_ast_skeleton(node) if kind != "class" else f"Class(methods={len(node.body)})"
                symbols.append({
                    "name": qual_name,
                    "raw_name": node.name,
                    "kind": kind,
                    "start_line": start_line,
                    "end_line": end_line,
                    "signature": signature,
                    "docstring": docstring.splitlines()[0] if docstring else "",
                    "snippet": "\n".join(snippet_lines),
                    "ast_skeleton": skeleton,
                    "language": "python",
                })
                visit_block(node.body, parent_qual=qual_name, parent_kind=kind)
```

### `strip_js_comments_and_strings` — `Lines 133–138`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `133` إلى السطر `138` (`Lines 133–138`)
- **الوظيفة:** Replace string literals and line comments with spaces while preserving brace structure.
- **الكود الفعلي (`Lines 133–138`):**
```python
def strip_js_comments_and_strings(line: str) -> str:
    """Replace string literals and line comments with spaces while preserving brace structure."""
    out = re.sub(r"//.*$", "", line)
    out = re.sub(r'"(?:\\.|[^"\\])*"|`(?:\\.|[^`\\])*`', '""', out)
    out = re.sub(r"\x27(?:\\.|[^\x27\\])*\x27", '""', out)
    return out
```

### `find_block_end` — `Lines 141–162`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `141` إلى السطر `162` (`Lines 141–162`)
- **الوظيفة:** Find 1-indexed end line of a brace-delimited or statement block starting at 0-indexed start_idx.
- **الكود الفعلي (`Lines 141–162`):**
```python
def find_block_end(lines: list[str], start_idx: int) -> int:
    """Find 1-indexed end line of a brace-delimited or statement block starting at 0-indexed start_idx."""
    brace_depth = 0
    paren_depth = 0
    saw_open_brace = False
    for idx in range(start_idx, len(lines)):
        cleaned = strip_js_comments_and_strings(lines[idx])
        for ch in cleaned:
            if ch == "(":
                paren_depth += 1
            elif ch == ")":
                paren_depth = max(0, paren_depth - 1)
            elif ch == "{":
                brace_depth += 1
                saw_open_brace = True
            elif ch == "}":
                brace_depth -= 1
        if saw_open_brace and brace_depth <= 0 and paren_depth == 0:
            return idx + 1
        if not saw_open_brace and paren_depth == 0 and cleaned.rstrip().endswith(";"):
            return idx + 1
    return start_idx + 1
```

### `extract_ts_js_symbols` — `Lines 165–311`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `165` إلى السطر `311` (`Lines 165–311`)
- **الوظيفة:** Extract functions, arrow functions, classes, class methods, nested symbols, and exported declarations in TS/JS.
- **الكود الفعلي (`Lines 165–311`):**
```python
def extract_ts_js_symbols(file_path: Path) -> list[dict]:
    """Extract functions, arrow functions, classes, class methods, nested symbols, and exported declarations in TS/JS."""
    source_text = file_path.read_text(encoding="utf-8")
    lines = source_text.splitlines()
    symbols: list[dict] = []

    re_func = re.compile(
        r"^\s*(export\s+)?(default\s+)?(async\s+)?function\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*[<(]"
    )
    re_class = re.compile(
        r"^\s*(export\s+)?(default\s+)?(abstract\s+)?class\s+([A-Za-z_$][A-Za-z0-9_$]*)"
    )
    re_arrow_or_fn_expr = re.compile(
        r"^\s*(export\s+)?(?:const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*)\s*(?::[^=]+)?=\s*(?:async\s+)?(?:<[^>]+>\s*)?(?:\([^)]*\)|[A-Za-z_$][A-Za-z0-9_$]*)\s*(?::[^=]+)?=>"
    )
    re_exported_decl = re.compile(
        r"^\s*export\s+(?:(interface|type|enum|const|let|var)\s+([A-Za-z_$][A-Za-z0-9_$]*))"
    )
    re_method = re.compile(
        r"^\s*(?:(?:public|private|protected|static|readonly|async|override|get|set)\s+)*([A-Za-z_$][A-Za-z0-9_$]*)\s*(?:<[^>]*>)?\s*\([^;]*\)\s*(?::\s*[^{]+)?\{"
    )
    re_class_arrow = re.compile(
        r"^\s*(?:(?:public|private|protected|static|readonly)\s+)*([A-Za-z_$][A-Za-z0-9_$]*)\s*(?::[^=]+)?=\s*(?:async\s+)?\([^)]*\)\s*(?::[^=]+)?=>"
    )
    reserved_keywords = {"if", "for", "while", "switch", "catch", "function", "return", "constructor"}

    active_scopes: list[tuple[str, str, int]] = []  # (qual_name, kind, end_line)

    for idx0, raw_line in enumerate(lines):
        line_no = idx0 + 1
        while active_scopes and line_no > active_scopes[-1][2]:
            active_scopes.pop()

        cleaned = strip_js_comments_and_strings(raw_line)
        if not cleaned.strip():
            continue

        parent_qual = active_scopes[-1][0] if active_scopes else ""
        parent_kind = active_scopes[-1][1] if active_scopes else ""

        m_cls = re_class.match(cleaned)
        if m_cls:
            exported = bool(m_cls.group(1))
            name = m_cls.group(4)
            qual = f"{parent_qual}.{name}" if parent_qual else name
            end_line = find_block_end(lines, idx0)
            kind = "exported_class" if exported and not parent_qual else ("nested_class" if parent_qual else "class")
            symbols.append({
                "name": qual,
                "raw_name": name,
                "kind": kind,
                "start_line": line_no,
                "end_line": end_line,
                "signature": raw_line.strip(),
                "docstring": "",
                "snippet": "\n".join(lines[idx0:end_line]),
                "ast_skeleton": f"TSClass({name})",
                "language": "typescript" if file_path.suffix in {".ts", ".tsx"} else "javascript",
            })
            active_scopes.append((qual, "class", end_line))
            continue

        m_fn = re_func.match(cleaned)
        if m_fn:
            exported = bool(m_fn.group(1))
            name = m_fn.group(4)
            qual = f"{parent_qual}.{name}" if parent_qual else name
            end_line = find_block_end(lines, idx0)
            kind = "nested_function" if parent_qual else ("exported_function" if exported else "function")
            symbols.append({
                "name": qual,
                "raw_name": name,
                "kind": kind,
                "start_line": line_no,
                "end_line": end_line,
                "signature": raw_line.strip(),
                "docstring": "",
                "snippet": "\n".join(lines[idx0:end_line]),
                "ast_skeleton": "TSFunc",
                "language": "typescript" if file_path.suffix in {".ts", ".tsx"} else "javascript",
            })
            active_scopes.append((qual, "function", end_line))
            continue

        m_arr = re_arrow_or_fn_expr.match(cleaned)
        if m_arr:
            exported = bool(m_arr.group(1))
            name = m_arr.group(2)
            qual = f"{parent_qual}.{name}" if parent_qual else name
            end_line = find_block_end(lines, idx0)
            kind = "nested_arrow_function" if parent_qual else ("exported_arrow_function" if exported else "arrow_function")
            symbols.append({
                "name": qual,
                "raw_name": name,
                "kind": kind,
                "start_line": line_no,
                "end_line": end_line,
                "signature": raw_line.strip(),
                "docstring": "",
                "snippet": "\n".join(lines[idx0:end_line]),
                "ast_skeleton": "TSArrowFunc",
                "language": "typescript" if file_path.suffix in {".ts", ".tsx"} else "javascript",
            })
            active_scopes.append((qual, "function", end_line))
            continue

        if parent_kind == "class":
            m_meth = re_method.match(cleaned) or re_class_arrow.match(cleaned)
            if m_meth:
                mname = m_meth.group(1)
                if mname not in reserved_keywords:
                    qual = f"{parent_qual}.{mname}"
                    end_line = find_block_end(lines, idx0)
                    symbols.append({
                        "name": qual,
                        "raw_name": mname,
                        "kind": "method",
                        "start_line": line_no,
                        "end_line": end_line,
                        "signature": raw_line.strip(),
                        "docstring": "",
                        "snippet": "\n".join(lines[idx0:end_line]),
                        "ast_skeleton": "TSMethod",
                        "language": "typescript" if file_path.suffix in {".ts", ".tsx"} else "javascript",
                    })
                    active_scopes.append((qual, "method", end_line))
                    continue

        if not parent_qual:
            m_exp = re_exported_decl.match(cleaned)
            if m_exp:
                decl_kind, name = m_exp.group(1), m_exp.group(2)
                end_line = find_block_end(lines, idx0)
                symbols.append({
                    "name": name,
                    "raw_name": name,
                    "kind": f"exported_{decl_kind}",
                    "start_line": line_no,
                    "end_line": end_line,
                    "signature": raw_line.strip(),
                    "docstring": "",
                    "snippet": "\n".join(lines[idx0:end_line]),
                    "ast_skeleton": f"TSExport({decl_kind})",
                    "language": "typescript" if file_path.suffix in {".ts", ".tsx"} else "javascript",
                })

    return symbols
```

### `detect_duplicate_functions` — `Lines 314–340`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `314` إلى السطر `340` (`Lines 314–340`)
- **الوظيفة:** Level 1 (Deterministic Blocking): Detect exact-name duplicate top-level functions/classes across files.
- **الكود الفعلي (`Lines 314–340`):**
```python
def detect_duplicate_functions(all_file_symbols: dict[str, list[dict]]) -> list[dict]:
    """Level 1 (Deterministic Blocking): Detect exact-name duplicate top-level functions/classes across files."""
    allowed_entrypoints = {"main"}
    checkable_kinds = {
        "function",
        "exported_function",
        "arrow_function",
        "exported_arrow_function",
        "class",
        "exported_class",
    }
    by_name: dict[str, list[dict]] = {}
    for rel_path, symbols in all_file_symbols.items():
        for sym in symbols:
            if sym["kind"] not in checkable_kinds or sym["name"] in allowed_entrypoints:
                continue
            by_name.setdefault(sym["name"], []).append({
                "file": rel_path,
                "start_line": sym["start_line"],
                "end_line": sym["end_line"],
                "signature": sym["signature"],
            })
    duplicates: list[dict] = []
    for name, occurrences in sorted(by_name.items()):
        if len(occurrences) > 1:
            duplicates.append({"function_name": name, "occurrences": occurrences})
    return duplicates
```

### `detect_structural_similarity` — `Lines 343–361`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `343` إلى السطر `361` (`Lines 343–361`)
- **الوظيفة:** Level 2 (Heuristic AST Skeleton Check): Identify functions with identical non-trivial AST skeletons.
- **الكود الفعلي (`Lines 343–361`):**
```python
def detect_structural_similarity(all_file_symbols: dict[str, list[dict]]) -> list[dict]:
    """Level 2 (Heuristic AST Skeleton Check): Identify functions with identical non-trivial AST skeletons."""
    by_skeleton: dict[str, list[dict]] = {}
    for rel_path, symbols in all_file_symbols.items():
        for sym in symbols:
            skel = sym.get("ast_skeleton", "")
            # Only flag non-trivial skeletons with >= 6 control/call nodes
            if sym["name"] == "main" or skel.count("->") < 6:
                continue
            by_skeleton.setdefault(skel, []).append({
                "symbol": sym["name"],
                "file": rel_path,
                "lines": f"{sym['start_line']}–{sym['end_line']}",
            })
    candidates: list[dict] = []
    for skel, items in sorted(by_skeleton.items()):
        if len(items) > 1:
            candidates.append({"ast_skeleton": skel, "candidates": items})
    return candidates
```

### `render_mirror_markdown` — `Lines 364–442`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `364` إلى السطر `442` (`Lines 364–442`)
- **الوظيفة:** Render the 1:1 Code Mirror Markdown file with explicit source-authority header.
- **الكود الفعلي (`Lines 364–442`):**
```python
def render_mirror_markdown(rel_path: str, file_path: Path, symbols: list[dict], meta: dict) -> str:
    """Render the 1:1 Code Mirror Markdown file with explicit source-authority header."""
    raw_bytes = file_path.read_bytes()
    sha256_hex = hashlib.sha256(raw_bytes).hexdigest()
    total_lines = len(raw_bytes.decode("utf-8").splitlines())
    file_meta = meta.get("files", {}).get(rel_path, {})
    role = file_meta.get("role", "First-Party Source Module")
    summary = file_meta.get("summary", "ملف برمجي ضمن معمارية AI Graphic Designer.")
    takes_from = file_meta.get("takes_from", [])
    throws_to = file_meta.get("throws_to", [])
    sym_descriptions = file_meta.get("symbols", {})

    out: list[str] = [
        f"# مرآة الكود التفصيلية: `{rel_path}`",
        "",
        "> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**",
        f"> الملف البرمجي الأصلي `{rel_path}` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).",
        "",
        "## 1. بطاقة تعريف الملف (`File Overview`)",
        f"- **المسار الفعلي (`Source File`):** `{rel_path}`",
        f"- **الدور المعماري (`Architectural Role`):** {role}",
        f"- **إجمالي عدد الأسطر (`Total Lines`):** `{total_lines}` (`Lines 1–{total_lines}`)",
        f"- **بصمة الملف (`SHA-256`):** `{sha256_hex}`",
        f"- **الوصف التفصيلي:** {summary}",
        "",
        "## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)",
        "",
        "| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |",
        "| :--- | :--- | :--- | :--- |",
    ]
    for item in takes_from:
        out.append(f"| **يأخذ من (`Takes From`)** | `{item['source']}` | {item['payload']} | {item['impact']} |")
    for item in throws_to:
        out.append(f"| **يرمي إلى (`Throws To`)** | `{item['target']}` | {item['payload']} | {item['impact']} |")
    if not takes_from and not throws_to:
        out.append("| **مستقل (`Standalone`)** | `None` | لا توجد ارتباطات خارجية مباشرة حالياً | مراجعة هذا الملف فقط عند التعديل. |")

    out.extend([
        "",
        "## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)",
        "",
        "| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ])
    for sym in symbols:
        desc = (
            sym_descriptions.get(sym["name"])
            or sym_descriptions.get(sym.get("raw_name", ""))
            or sym["docstring"]
            or "رمز برمجي موثق."
        )
        out.append(
            f"| `{sym['name']}` | `{sym['kind']}` | `Lines {sym['start_line']}–{sym['end_line']}` | `{sym['signature']}` | {desc} |"
        )

    out.extend([
        "",
        "## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)",
        "",
    ])
    for sym in symbols:
        desc = (
            sym_descriptions.get(sym["name"])
            or sym_descriptions.get(sym.get("raw_name", ""))
            or sym["docstring"]
            or "رمز برمجي موثق."
        )
        out.extend([
            f"### `{sym['name']}` — `Lines {sym['start_line']}–{sym['end_line']}`",
            f"- **النوع:** `{sym['kind']}`",
            f"- **نطاق الأسطر الدقيق:** من السطر `{sym['start_line']}` إلى السطر `{sym['end_line']}` (`Lines {sym['start_line']}–{sym['end_line']}`)",
            f"- **الوظيفة:** {desc}",
            f"- **الكود الفعلي (`Lines {sym['start_line']}–{sym['end_line']}`):**",
            f"```{sym['language']}",
            sym["snippet"],
            "```",
            "",
        ])
    return "\n".join(out).strip() + "\n"
```

### `render_function_registry` — `Lines 445–484`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `445` إلى السطر `484` (`Lines 445–484`)
- **الوظيفة:** Render the central memory/FUNCTION_REGISTRY.md file with 3-tier deduplication status.
- **الكود الفعلي (`Lines 445–484`):**
```python
def render_function_registry(
    all_file_symbols: dict[str, list[dict]],
    meta: dict,
    duplicates: list[dict],
    structural_candidates: list[dict],
) -> str:
    """Render the central memory/FUNCTION_REGISTRY.md file with 3-tier deduplication status."""
    total_funcs = sum(len(v) for v in all_file_symbols.values())
    out: list[str] = [
        "# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)",
        "",
        "> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**",
        "> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.",
        "> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.",
        "> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).",
        "",
        f"- **إجمالي الملفات البرمجية المفحوصة:** `{len(all_file_symbols)}`",
        f"- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `{total_funcs}`",
        f"- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `{len(duplicates)}`",
        f"- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `{len(structural_candidates)}`",
        "",
        "## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)",
        "",
        "| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for rel_path, symbols in sorted(all_file_symbols.items()):
        sym_descriptions = meta.get("files", {}).get(rel_path, {}).get("symbols", {})
        mirror_name = mirror_filename_for(rel_path)
        for sym in symbols:
            desc = (
                sym_descriptions.get(sym["name"])
                or sym_descriptions.get(sym.get("raw_name", ""))
                or sym["docstring"]
                or "رمز برمجي موثق."
            )
            out.append(
                f"| `{sym['name']}` | `{sym['kind']}` | `{rel_path}` | `Lines {sym['start_line']}–{sym['end_line']}` | `{sym['signature']}` | {desc} | [{mirror_name}](code_mirrors/{mirror_name}) |"
            )
    return "\n".join(out).strip() + "\n"
```

### `discover_version_ids` — `Lines 488–492`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `488` إلى السطر `492` (`Lines 488–492`)
- **الوظيفة:** Return sorted list of all active version directory names in versions/.
- **الكود الفعلي (`Lines 488–492`):**
```python
def discover_version_ids() -> list[str]:
    """Return sorted list of all active version directory names in versions/."""
    if not VERSIONS_DIR.exists():
        return []
    return sorted(p.name for p in VERSIONS_DIR.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))
```

### `discover_version_code_files` — `Lines 495–510`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `495` إلى السطر `510` (`Lines 495–510`)
- **الوظيفة:** Return sorted list of code files belonging to a specific version.
- **الكود الفعلي (`Lines 495–510`):**
```python
def discover_version_code_files(version_id: str) -> list[Path]:
    """Return sorted list of code files belonging to a specific version."""
    vdir = VERSIONS_DIR / version_id
    if not vdir.exists():
        return []
    found: list[Path] = []
    v_excluded = {".git", "node_modules", "__pycache__", ".venv", "packages", "baselines", "latest", "CODE_MIRRORS"}
    for p in vdir.rglob("*"):
        if not p.is_file():
            continue
        rel_parts = p.relative_to(vdir).parts
        if any(part in v_excluded for part in rel_parts[:-1]):
            continue
        if p.suffix.lower() in CODE_EXTENSIONS:
            found.append(p)
    return sorted(found, key=lambda x: x.relative_to(vdir).as_posix())
```

### `render_version_mirror_markdown` — `Lines 513–568`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `513` إلى السطر `568` (`Lines 513–568`)
- **الوظيفة:** Render 1:1 Code Mirror for a version-scoped source file.
- **الكود الفعلي (`Lines 513–568`):**
```python
def render_version_mirror_markdown(rel_in_version: str, file_path: Path, symbols: list[dict], version_id: str) -> str:
    """Render 1:1 Code Mirror for a version-scoped source file."""
    raw_bytes = file_path.read_bytes()
    sha256_hex = hashlib.sha256(raw_bytes).hexdigest()
    total_lines = len(raw_bytes.decode("utf-8").splitlines())

    out: list[str] = [
        f"# مرآة الكود التفصيلية للإصدار: `{version_id}/{rel_in_version}`",
        "",
        "> **تنبيه مرجعية الكود (`AUTO-GENERATED VERSION MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**",
        f"> الملف البرمجي الأصلي `versions/{version_id}/{rel_in_version}` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)** لهذا الإصدار. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py --version {version_id}`.",
        "",
        "## 1. بطاقة تعريف الملف (`File Overview`)",
        f"- **المسار الفعلي (`Source File`):** `{rel_in_version}`",
        f"- **الإصدار المعماري (`Architecture Version`):** `{version_id}`",
        f"- **إجمالي عدد الأسطر (`Total Lines`):** `{total_lines}` (`Lines 1–{total_lines}`)",
        f"- **بصمة الملف (`SHA-256`):** `{sha256_hex}`",
        f"- **الوصف:** موديول برمجي تنفيذي ضمن معمارية الإصدار `{version_id}`.",
        "",
        "## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)",
        "",
        "| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |",
        "| :--- | :--- | :--- | :--- |",
        f"| **حوكمة الإصدار الأب (`Parent Version`)** | `{version_id}` | يتبع مواصفة معمارية هذا الإصدار | مراجعة تكامل الإصدار عند التعديل. |",
        "| **الحوكمة المركزية (`Global Governance`)** | `AGENTS.md` | يخضع للدستور وقواعد منع التكرار المشتركة | التحقق الحوكمي الإلزامي. |",
        "",
        "## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)",
        "",
        "| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]
    for sym in symbols:
        desc = sym["docstring"] or "رمز برمجي موثق للإصدار."
        out.append(
            f"| `{sym['name']}` | `{sym['kind']}` | `Lines {sym['start_line']}–{sym['end_line']}` | `{sym['signature']}` | {desc} |"
        )

    out.extend([
        "",
        "## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)",
        "",
    ])
    for sym in symbols:
        desc = sym["docstring"] or "رمز برمجي موثق للإصدار."
        out.extend([
            f"### `{sym['name']}` — `Lines {sym['start_line']}–{sym['end_line']}`",
            f"- **النوع:** `{sym['kind']}`",
            f"- **نطاق الأسطر الدقيق:** من السطر `{sym['start_line']}` إلى السطر `{sym['end_line']}` (`Lines {sym['start_line']}–{sym['end_line']}`)",
            f"- **الوظيفة:** {desc}",
            f"- **الكود الفعلي (`Lines {sym['start_line']}–{sym['end_line']}`):**",
            f"```{sym['language']}",
            sym["snippet"],
            "```",
            "",
        ])
    return "\n".join(out).strip() + "\n"
```

### `render_version_function_registry` — `Lines 571–605`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `571` إلى السطر `605` (`Lines 571–605`)
- **الوظيفة:** Render the version-scoped FUNCTION_REGISTRY.md with 3-tier deduplication.
- **الكود الفعلي (`Lines 571–605`):**
```python
def render_version_function_registry(
    version_id: str,
    all_file_symbols: dict[str, list[dict]],
    duplicates: list[dict],
    structural_candidates: list[dict],
) -> str:
    """Render the version-scoped FUNCTION_REGISTRY.md with 3-tier deduplication."""
    total_funcs = sum(len(v) for v in all_file_symbols.values())
    out: list[str] = [
        f"# السجل الموحد للدوال والكلاسات للإصدار `{version_id}` (`FUNCTION_REGISTRY.md`)",
        "",
        "> **مرجعية الكود ومستويات منع التكرار الخاصة بالإصدار (`Version Source Authority & Deduplication Policy`):**",
        f"> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي يمنع وجود دالتين بنفس الاسم عبر ملفات الإصدار `{version_id}`.",
        "> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية المتطابقة داخل الإصدار.",
        "> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** تدقيق مهندس الإصدار والمراجع المستقل لمنع إعادة اختراع الوظائف المتاحة.",
        "",
        f"- **معرف الإصدار المعماري (`Version ID`):** `{version_id}`",
        f"- **إجمالي الملفات البرمجية المفحوصة في الإصدار:** `{len(all_file_symbols)}`",
        f"- **إجمالي الرموز المسجلة بالسطر:** `{total_funcs}`",
        f"- **عدد الدوال المتطابقة الاسم غير المسموحة:** `{len(duplicates)}`",
        f"- **مرشحات التشابه الهيكلي:** `{len(structural_candidates)}`",
        "",
        "## جدول جميع الدوال والكلاسات والرموز في الإصدار (`Version Symbol Index`)",
        "",
        "| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]
    for rel_path, symbols in sorted(all_file_symbols.items()):
        for sym in symbols:
            desc = sym["docstring"] or "رمز برمجي موثق للإصدار."
            mirror_rel = f"CODE_MIRRORS/{rel_path}.md"
            out.append(
                f"| `{sym['name']}` | `{sym['kind']}` | `{rel_path}` | `Lines {sym['start_line']}–{sym['end_line']}` | `{sym['signature']}` | {desc} | [{rel_path}.md]({mirror_rel}) |"
            )
    return "\n".join(out).strip() + "\n"
```

### `sync_version` — `Lines 608–657`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `608` إلى السطر `657` (`Lines 608–657`)
- **الوظيفة:** Synchronize code mirrors and function registry for a specific version.
- **الكود الفعلي (`Lines 608–657`):**
```python
def sync_version(version_id: str, write_mode: bool = False) -> dict:
    """Synchronize code mirrors and function registry for a specific version."""
    vdir = VERSIONS_DIR / version_id
    if not vdir.is_dir():
        raise ValueError(f"Version directory not found: {vdir}")

    code_files = discover_version_code_files(version_id)
    all_symbols: dict[str, list[dict]] = {}
    mirrors_dir = vdir / "docs" / "CODE_MIRRORS"
    mirrors_dir.mkdir(parents=True, exist_ok=True)
    expected_mirrors: set[Path] = set()

    for file_path in code_files:
        rel_in_version = file_path.relative_to(vdir).as_posix()
        symbols = (
            extract_python_symbols(file_path)
            if file_path.suffix.lower() == ".py"
            else extract_ts_js_symbols(file_path)
        )
        all_symbols[rel_in_version] = symbols
        target_mirror = mirrors_dir / f"{rel_in_version}.md"
        expected_mirrors.add(target_mirror)
        if write_mode:
            target_mirror.parent.mkdir(parents=True, exist_ok=True)
            mirror_md = render_version_mirror_markdown(rel_in_version, file_path, symbols, version_id)
            target_mirror.write_text(mirror_md, encoding="utf-8")

    if write_mode and mirrors_dir.exists():
        for existing in mirrors_dir.rglob("*.md"):
            if existing not in expected_mirrors:
                existing.unlink()

    duplicates = detect_duplicate_functions(all_symbols)
    structural_candidates = detect_structural_similarity(all_symbols)
    registry_path = vdir / "docs" / "FUNCTION_REGISTRY.md"
    if write_mode:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry_md = render_version_function_registry(version_id, all_symbols, duplicates, structural_candidates)
        registry_path.write_text(registry_md, encoding="utf-8")

    summary = {
        "version_id": version_id,
        "code_files_scanned": len(code_files),
        "total_symbols_indexed": sum(len(v) for v in all_symbols.values()),
        "duplicate_functions_found": len(duplicates),
        "duplicates": duplicates,
        "structural_similarity_candidates_count": len(structural_candidates),
        "write_mode": write_mode,
    }
    return summary
```

### `sync_root` — `Lines 660–702`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `660` إلى السطر `702` (`Lines 660–702`)
- **الوظيفة:** Synchronize root codebase mirrors and central FUNCTION_REGISTRY.md.
- **الكود الفعلي (`Lines 660–702`):**
```python
def sync_root(write_mode: bool = False) -> dict:
    """Synchronize root codebase mirrors and central FUNCTION_REGISTRY.md."""
    meta = json.loads(METADATA_PATH.read_text(encoding="utf-8")) if METADATA_PATH.exists() else {"files": {}}
    code_files = discover_code_files()
    all_symbols: dict[str, list[dict]] = {}

    MIRRORS_DIR.mkdir(parents=True, exist_ok=True)
    expected_mirrors = {"TEMPLATE_CODE_MIRROR.md"}
    for file_path in code_files:
        rel_path = file_path.relative_to(ROOT).as_posix()
        symbols = (
            extract_python_symbols(file_path)
            if file_path.suffix.lower() == ".py"
            else extract_ts_js_symbols(file_path)
        )
        all_symbols[rel_path] = symbols
        mname = mirror_filename_for(rel_path)
        expected_mirrors.add(mname)
        if write_mode:
            mirror_md = render_mirror_markdown(rel_path, file_path, symbols, meta)
            (MIRRORS_DIR / mname).write_text(mirror_md, encoding="utf-8")

    if write_mode:
        for existing_mirror in MIRRORS_DIR.glob("*.md"):
            if existing_mirror.name not in expected_mirrors:
                existing_mirror.unlink()

    duplicates = detect_duplicate_functions(all_symbols)
    structural_candidates = detect_structural_similarity(all_symbols)
    if write_mode:
        registry_md = render_function_registry(all_symbols, meta, duplicates, structural_candidates)
        REGISTRY_PATH.write_text(registry_md, encoding="utf-8")

    summary = {
        "scope": "root",
        "code_files_scanned": len(code_files),
        "total_symbols_indexed": sum(len(v) for v in all_symbols.values()),
        "duplicate_functions_found": len(duplicates),
        "duplicates": duplicates,
        "structural_similarity_candidates_count": len(structural_candidates),
        "write_mode": write_mode,
    }
    return summary
```

### `main` — `Lines 705–737`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `705` إلى السطر `737` (`Lines 705–737`)
- **الوظيفة:** Synchronize all code mirrors and function registries across root and registered versions.
- **الكود الفعلي (`Lines 705–737`):**
```python
def main() -> None:
    """Synchronize all code mirrors and function registries across root and registered versions."""
    write_mode = "--write" in sys.argv
    version_arg = None
    all_versions = "--all-versions" in sys.argv

    for idx, arg in enumerate(sys.argv):
        if arg == "--version" and idx + 1 < len(sys.argv):
            version_arg = sys.argv[idx + 1]

    if version_arg:
        res = sync_version(version_arg, write_mode=write_mode)
        print(json.dumps(res, ensure_ascii=False))
        if res["duplicate_functions_found"] > 0:
            raise SystemExit(1)
        return

    root_res = sync_root(write_mode=write_mode)
    results = {"root": root_res}
    has_dup = root_res["duplicate_functions_found"] > 0

    if all_versions:
        v_results = {}
        for vid in discover_version_ids():
            vres = sync_version(vid, write_mode=write_mode)
            v_results[vid] = vres
            if vres["duplicate_functions_found"] > 0:
                has_dup = True
        results["versions"] = v_results

    print(json.dumps(results, ensure_ascii=False))
    if has_dup:
        raise SystemExit(1)
```
