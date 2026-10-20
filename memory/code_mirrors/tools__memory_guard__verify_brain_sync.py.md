# مرآة الكود التفصيلية: `tools/memory_guard/verify_brain_sync.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `tools/memory_guard/verify_brain_sync.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `tools/memory_guard/verify_brain_sync.py`
- **الدور المعماري (`Architectural Role`):** Memory Guard — Automated External Brain & Line-Number Auditor
- **إجمالي عدد الأسطر (`Total Lines`):** `527` (`Lines 1–527`)
- **بصمة الملف (`SHA-256`):** `e1f38030e75f3cb86778b570043f6c5bfe0597b8d7e05e0561e331708d4dcf1f`
- **الوصف التفصيلي:** يتحقق آلياً من أن كل ملف برمجي في المشروع يمتلك ملف مرآة محدثاً في memory/code_mirrors/، وأن أرقام الأسطر (Lines Start–End) والمقتطفات في المرآة وفي memory/FUNCTION_REGISTRY.md مطابقة 100% للكود الفعلي، مع التحقق من عدم وجود دوال مكررة ومن توافق قواعد Antigravity مع سقف 24KB والـ YAML Frontmatter.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `جميع ملفات الكود + memory/code_mirrors/*.md + memory/FUNCTION_REGISTRY.md` | بيانات الدوال الفعلية مقارنةً بأرقام الأسطر والمقتطفات المسجلة في الذاكرة | يكتشف فوراً أي نسيان لتحديث الذاكرة بعد تعديل الكود. |
| **يأخذ من (`Takes From`)** | `.agents/rules/*.md & .agent_rules/*.md & AGENTS.md & GEMINI.md` | محتوى وأحجام ملفات القواعد والـ YAML Frontmatter | يضمن عدم تجاوز حد الـ 24KB الخاص بـ Antigravity وعدم سقوط أي قاعدة. |
| **يرمي إلى (`Throws To`)** | `tools/memory_guard/brain_validation.json` | تقرير JSON مفصل بنتيجة فحص تزامن الذاكرة الحية وأرقام الأسطر وفحص عدم التكرار | يُعتمد عليه في بوابة الجودة (Quality Gate) وبوابة الإغلاق (Stop Hook). |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `verify_antigravity_rules` | `function` | `Lines 44–82` | `def verify_antigravity_rules() -> list[str]:` | تفحص جميع ملفات القواعد في .agents/rules/ للتأكد من وجود YAML frontmatter صالح (trigger, description) وعدم تجاوز حجم 24,000 بايت. |
| `verify_immutable_owner_vision` | `function` | `Lines 85–156` | `def verify_immutable_owner_vision() -> list[str]:` | تقارن نص رؤية المالك في OWNER_ORIGINAL_VISION.md حرفياً وجملةً بجملة مع النسخة المرجعية المحفوظة وملف البصمات لكشف أي تعديل داخلي حتى لو بقي العنوان والمقدمة. |
| `verify_owner_approval_provenance` | `function` | `Lines 159–325` | `def verify_owner_approval_provenance() -> list[str]:` | تمنع أي ادعاء مزور بـ OWNER_APPROVED للمعمارية أو المرحلة P0 وترفض أي نصوص توكن مخترعة مثل OWNER_AUTHORIZATION_TOKEN. |
| `verify_code_mirrors_and_lines` | `function` | `Lines 328–388` | `def verify_code_mirrors_and_lines() -> tuple[list[str], dict]:` | تقارن الدوال وأرقام الأسطر الفعلية في الكود مع ما هو مكتوب في memory/code_mirrors/ وmemory/FUNCTION_REGISTRY.md وتكشف أي اختلاف أو نقص. |
| `verify_version_code_mirrors` | `function` | `Lines 392–463` | `def verify_version_code_mirrors(version_id: str) -> tuple[list[str], dict]:` | Verify 1:1 code mirrors, exact line numbers, verbatim snippets, and zero duplicates for a specific version. |
| `verify_all_versions` | `function` | `Lines 466–474` | `def verify_all_versions() -> tuple[list[str], dict]:` | Verify code mirrors and function registries across all registered versions. |
| `main` | `function` | `Lines 478–523` | `def main() -> None:` | تشغل جميع فحوصات تزامن الذاكرة وتكتب التقرير النهائي في brain_validation.json وترجع كود الخروج (0 للنجاح، 1 للفشل). |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `verify_antigravity_rules` — `Lines 44–82`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `82` (`Lines 44–82`)
- **الوظيفة:** تفحص جميع ملفات القواعد في .agents/rules/ للتأكد من وجود YAML frontmatter صالح (trigger, description) وعدم تجاوز حجم 24,000 بايت.
- **الكود الفعلي (`Lines 44–82`):**
```python
def verify_antigravity_rules() -> list[str]:
    """Validate YAML frontmatter, 24KB size ceiling, and .agent_rules <-> .agents/rules parity."""
    errors: list[str] = []
    for root_doc in ["AGENTS.md", "GEMINI.md"]:
        p = ROOT / root_doc
        if not p.exists():
            errors.append(f"Missing root entry file: {root_doc}")
        elif p.stat().st_size > ANTIGRAVITY_MAX_RULE_BYTES:
            errors.append(f"Root file exceeds 24KB Antigravity limit: {root_doc} ({p.stat().st_size} bytes)")

    sync_res = sr.sync_or_check(write_mode=False)
    if sync_res["status"] != "SYNCHRONIZED":
        errors.append(f"Rules out of sync between .agent_rules/ and .agents/rules/: {sync_res}")

    rules_dir = ROOT / ".agents" / "rules"
    if not rules_dir.exists():
        errors.append("Missing .agents/rules directory")
        return errors

    for rule_file in sorted(rules_dir.glob("*.md")):
        size_bytes = rule_file.stat().st_size
        if size_bytes > ANTIGRAVITY_MAX_RULE_BYTES:
            errors.append(f"Rule file exceeds 24KB limit: {rule_file.name} ({size_bytes} bytes)")
        text = rule_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"Missing YAML frontmatter in {rule_file.name}")
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            errors.append(f"Unclosed YAML frontmatter in {rule_file.name}")
            continue
        fm = parts[1]
        trig_match = re.search(r"^trigger:\s*(\S+)", fm, re.M)
        desc_match = re.search(r"^description:\s*.+", fm, re.M)
        if not trig_match or trig_match.group(1) not in VALID_TRIGGERS:
            errors.append(f"Invalid or missing trigger in {rule_file.name}")
        if not desc_match:
            errors.append(f"Missing description in frontmatter of {rule_file.name}")
    return errors
```

### `verify_immutable_owner_vision` — `Lines 85–156`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `85` إلى السطر `156` (`Lines 85–156`)
- **الوظيفة:** تقارن نص رؤية المالك في OWNER_ORIGINAL_VISION.md حرفياً وجملةً بجملة مع النسخة المرجعية المحفوظة وملف البصمات لكشف أي تعديل داخلي حتى لو بقي العنوان والمقدمة.
- **الكود الفعلي (`Lines 85–156`):**
```python
def verify_immutable_owner_vision() -> list[str]:
    """Verify docs/product/OWNER_ORIGINAL_VISION.md against immutable baseline copy, sentence registry, and traceability."""
    errors: list[str] = []
    vision_path = ROOT / "docs" / "product" / "OWNER_ORIGINAL_VISION.md"
    archive_path = ROOT / "docs" / "history" / "immutable_baselines" / "OWNER_ORIGINAL_VISION.baseline.md"
    baseline_json_path = HERE / "immutable_vision_baseline.json"
    trace_path = ROOT / "docs" / "product" / "VISION_TO_REQUIREMENTS_TRACEABILITY.md"
    derived_path = ROOT / "docs" / "PRODUCT_VISION_AND_MODES.md"

    if not vision_path.is_file():
        return ["Missing authoritative owner vision file: docs/product/OWNER_ORIGINAL_VISION.md"]
    if not archive_path.is_file():
        errors.append("Missing immutable baseline archive: docs/history/immutable_baselines/OWNER_ORIGINAL_VISION.baseline.md")
    if not baseline_json_path.is_file():
        errors.append("Missing immutable vision baseline metadata: tools/memory_guard/immutable_vision_baseline.json")
        return errors

    v_bytes = vision_path.read_bytes()
    v_text = v_bytes.decode("utf-8")
    v_sha = hashlib.sha256(v_bytes).hexdigest()
    b_meta = json.loads(baseline_json_path.read_text(encoding="utf-8"))

    if archive_path.is_file():
        arch_text = archive_path.read_text(encoding="utf-8")
        if v_text != arch_text:
            errors.append(
                "Immutable owner vision modified: docs/product/OWNER_ORIGINAL_VISION.md differs from docs/history/immutable_baselines/OWNER_ORIGINAL_VISION.baseline.md"
            )

    m = re.search(
        r"<!-- BEGIN_VERBATIM_OWNER_VISION -->\n(.*?)\n<!-- END_VERBATIM_OWNER_VISION -->",
        v_text,
        re.S,
    )
    if not m:
        errors.append("Missing <!-- BEGIN_VERBATIM_OWNER_VISION --> markers in docs/product/OWNER_ORIGINAL_VISION.md")
    else:
        payload = m.group(1)
        payload_sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
        if payload_sha != b_meta.get("verbatim_payload_sha256") or len(payload) != b_meta.get("verbatim_payload_char_length"):
            errors.append("Immutable owner vision modified: verbatim payload SHA-256 or character count mismatch")

        actual_lines = payload.splitlines()
        expected_lines = b_meta.get("verbatim_lines", [])
        if len(actual_lines) != len(expected_lines):
            errors.append(
                f"Immutable owner vision modified: line count changed ({len(actual_lines)} vs {len(expected_lines)})"
            )
        else:
            for idx, exp_line in enumerate(expected_lines):
                if actual_lines[idx] != exp_line.get("text"):
                    errors.append(
                        f"Immutable owner vision modified at verbatim line {idx + 1}: content does not match original owner text"
                    )

        for sent in b_meta.get("verbatim_sentences", []):
            stext = sent.get("text", "")
            if stext not in payload:
                errors.append(
                    f"Immutable owner vision modified: sentence #{sent.get('sentence_index')} on line {sent.get('line')} was altered or removed"
                )

    if v_sha != b_meta.get("full_file_sha256") or len(v_bytes) != b_meta.get("full_file_byte_length"):
        errors.append("Immutable owner vision modified: full file SHA-256 or byte length differs from baseline")

    if not trace_path.is_file():
        errors.append("Missing vision traceability matrix: docs/product/VISION_TO_REQUIREMENTS_TRACEABILITY.md")

    if not derived_path.is_file() or "DERIVED_ARCHITECTURAL_INTERPRETATION" not in derived_path.read_text(encoding="utf-8"):
        errors.append("docs/PRODUCT_VISION_AND_MODES.md must explicitly declare DERIVED_ARCHITECTURAL_INTERPRETATION")

    return errors
```

### `verify_owner_approval_provenance` — `Lines 159–325`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `159` إلى السطر `325` (`Lines 159–325`)
- **الوظيفة:** تمنع أي ادعاء مزور بـ OWNER_APPROVED للمعمارية أو المرحلة P0 وترفض أي نصوص توكن مخترعة مثل OWNER_AUTHORIZATION_TOKEN.
- **الكود الفعلي (`Lines 159–325`):**
```python
def verify_owner_approval_provenance() -> list[str]:
    """Enforce single authoritative approval state across the entire repository and validate transitions."""
    errors: list[str] = []
    dec_path = ROOT / "memory" / "decisions" / "DECISION_LOG.md"
    mp_path = ROOT / "MASTER_PLAN.md"
    chk_path = ROOT / "memory" / "session" / "CURRENT_TASK_CHECKPOINT.md"
    prov_path = ROOT / "memory" / "decisions" / "OWNER_APPROVAL_PROVENANCE.json"
    prov_base_path = ROOT / "docs" / "history" / "immutable_baselines" / "OWNER_APPROVAL_PROVENANCE.baseline.json"
    app_base_path = HERE / "approval_baseline.json"

    for p in [dec_path, mp_path, chk_path, prov_path, prov_base_path, app_base_path]:
        if not p.is_file():
            errors.append(f"Missing required approval governance file: {p.relative_to(ROOT).as_posix()}")
    if errors:
        return errors

    app_base = json.loads(app_base_path.read_text(encoding="utf-8"))
    prov = json.loads(prov_path.read_text(encoding="utf-8"))
    prov_base = json.loads(prov_base_path.read_text(encoding="utf-8"))

    # 1. Verify initial baseline immutability
    if prov_base.get("architecture_approval_status") != "NOT_APPROVED" or prov_base.get("revision_no", 0) != 0:
        errors.append("Immutable baseline OWNER_APPROVAL_PROVENANCE.baseline.json was tampered with")

    rev_no = prov.get("revision_no", 0)
    auth_arch_approved = False

    if rev_no == 0:
        # Must match the initial NOT_APPROVED baseline exactly
        if prov != prov_base:
            errors.append(
                "Unauthorized modification of memory/decisions/OWNER_APPROVAL_PROVENANCE.json at revision 0"
            )
    else:
        # Controlled transition: verify every precondition (experiment reports + revision archive chain)
        rev_hist = prov.get("approval_revision_history", [])
        if len(rev_hist) != rev_no:
            errors.append(f"Invalid approval_revision_history length in OWNER_APPROVAL_PROVENANCE.json (expected {rev_no})")
        else:
            expected_prev_sha = hashlib.sha256(prov_base_path.read_bytes()).hexdigest()
            for r_idx, rev_entry in enumerate(rev_hist, start=1):
                if rev_entry.get("revision_no") != r_idx:
                    errors.append(f"Non-sequential revision_no in approval_revision_history at index {r_idx}")
                if not rev_entry.get("owner_identifier") or not rev_entry.get("owner_confirmation_note"):
                    errors.append(f"Approval revision {r_idx} missing owner_identifier or owner_confirmation_note")
                arch_rel = rev_entry.get("archived_prior_baseline", "")
                arch_p = ROOT / arch_rel if arch_rel else None
                if not arch_p or not arch_p.is_file():
                    errors.append(f"Missing archived prior provenance baseline '{arch_rel}' for revision {r_idx}")
                else:
                    actual_arch_sha = hashlib.sha256(arch_p.read_bytes()).hexdigest()
                    if actual_arch_sha != rev_entry.get("previous_provenance_sha256") or actual_arch_sha != expected_prev_sha:
                        errors.append(f"Broken provenance baseline hash chain at revision {r_idx}")
                    expected_prev_sha = actual_arch_sha

                # Verify all required experiment reports exist and pass
                req_reports = app_base.get("required_experiment_reports_before_approval", [])
                rec_reports = rev_entry.get("validated_experiment_reports", {})
                for rep_rel in req_reports:
                    ok, err, rep_sha = ma.validate_experiment_report(rep_rel)
                    if not ok:
                        errors.append(f"Approval transition precondition failed: {err}")
                    elif rec_reports.get(rep_rel) != rep_sha:
                        errors.append(f"Experiment report SHA-256 mismatch for {rep_rel} in approval revision {r_idx}")

            if not errors and prov.get("architecture_approval_status") == "OWNER_APPROVED":
                auth_arch_approved = True

    # 2. Enforce consistency on core status documents (DECISION_LOG.md, MASTER_PLAN.md, CURRENT_TASK_CHECKPOINT.md)
    for doc_path in [dec_path, mp_path, chk_path]:
        text = doc_path.read_text(encoding="utf-8")
        rel_name = doc_path.relative_to(ROOT).as_posix()

        if not auth_arch_approved:
            if "ARCHITECTURE_AND_GOVERNANCE_PREPARATION" not in text:
                errors.append(f"{rel_name} must preserve PROJECT_STAGE as ARCHITECTURE_AND_GOVERNANCE_PREPARATION")
            if "NOT_APPROVED" not in text or "BLOCKED_PENDING_OWNER_APPROVAL" not in text:
                errors.append(
                    f"Missing owner approval gate in {rel_name}: must remain NOT_APPROVED and BLOCKED_PENDING_OWNER_APPROVAL"
                )
        else:
            if "ARCHITECTURE_APPROVED_READY_FOR_P0" not in text or "OWNER_APPROVED" not in text:
                errors.append(
                    f"{rel_name} is out of sync with authorized OWNER_APPROVED transition in OWNER_APPROVAL_PROVENANCE.json"
                )

    dec_text = dec_path.read_text(encoding="utf-8")
    for adr in app_base.get("must_remain_not_approved_adrs", ["ADR-001", "ADR-002", "ADR-003", "ADR-004", "ADR-007"]):
        row_match = re.search(rf"^\|\s*`{adr}`\s*\|([^\n]+)$", dec_text, re.M)
        if not row_match:
            errors.append(f"Missing required decision row '{adr}' in memory/decisions/DECISION_LOG.md")
        else:
            row_body = row_match.group(1)
            is_adr_approved = adr in prov.get("approved_architecture_decisions", []) and auth_arch_approved
            if not is_adr_approved and ("OWNER_APPROVED" in row_body or "NOT_APPROVED" not in row_body):
                errors.append(
                    f"Unauthorized approval status change on '{adr}' in memory/decisions/DECISION_LOG.md: must remain NOT_APPROVED"
                )
            elif is_adr_approved and "OWNER_APPROVED" not in row_body:
                errors.append(f"Decision row '{adr}' in DECISION_LOG.md not synchronized to OWNER_APPROVED")

    # 3. REPOSITORY-WIDE ENFORCEMENT: Scan ALL Markdown and JSON files so derived docs cannot independently claim OWNER_APPROVED
    excluded_dirs = {".git", "node_modules", "__pycache__", ".venv", "packages", "baselines", "latest"}
    skip_files = {
        "tools/tests/test_governance_suite.py",
        "memory/code_mirrors/tools__tests__test_governance_suite.py.md",
        "memory/code_mirrors/tools__memory_guard__verify_brain_sync.py.md",
        "memory/code_mirrors/tools__memory_guard__manage_approvals.py.md",
        "tools/memory_guard/brain_validation.json",
        "tools/memory_guard/approval_baseline.json",
    }

    re_arch_claim = re.compile(
        r"(?:ARCHITECTURE_APPROVAL_STATUS|Architecture Approval Status|حالة اعتماد المعمارية|P0_IMPLEMENTATION_GATE|P0 Implementation Gate|بوابة تنفيذ المنتج|بوابة المرحلة التأسيسية|Final Technology Commitment|حالة اعتماد المالك للمعمارية)[^\n]*?:\s*`?(?:OWNER_APPROVED|APPROVED|UNBLOCKED|READY)`?",
        re.I,
    )
    re_generic_status_claim = re.compile(
        r"^\s*(?:[-*]\s*)?\*{0,2}`?(?:Status|Approval Status|Architecture Status|Decision Status|Current Status|الحالة|حالة الاعتماد)`?\*{0,2}\s*:\s*`?OWNER_APPROVED`?",
        re.I | re.M,
    )
    re_table_owner_approved = re.compile(
        r"^\|\s*(?:`?(?:ADR-00[12347]|EXP-0[1-5])`?|\*{0,2}[1-6]\.[^|]+)\|[^\n]*\|\s*`?OWNER_APPROVED`?\s*\|",
        re.I | re.M,
    )

    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in {".md", ".json"}:
            continue
        if any(part in excluded_dirs for part in p.relative_to(ROOT).parts[:-1]):
            continue
        rel_p = p.relative_to(ROOT).as_posix()
        if rel_p in skip_files:
            continue
        content = p.read_text(encoding="utf-8")

        for forbidden_tok in app_base.get("forbid_token_strings", ["OWNER_AUTHORIZATION_TOKEN"]):
            if re.search(rf"{re.escape(forbidden_tok)}\s*[:=]\s*[`']?[A-Za-z0-9_-]+", content):
                errors.append(
                    f"Fabricated authorization token '{forbidden_tok}' detected in {rel_p}; arbitrary token strings are never valid owner authorization"
                )

        # Derived documents must NEVER declare ARCHITECTURE_APPROVAL_STATUS: OWNER_APPROVED or Status: OWNER_APPROVED
        is_authoritative_status_doc = (
            rel_p in {
                "memory/decisions/OWNER_APPROVAL_PROVENANCE.json",
                "memory/decisions/DECISION_LOG.md",
                "MASTER_PLAN.md",
                "memory/session/CURRENT_TASK_CHECKPOINT.md",
            }
            or rel_p.startswith("docs/history/promoted_targets/memory__decisions__DECISION_LOG.md")
            or rel_p.startswith("docs/history/immutable_baselines/OWNER_APPROVAL_PROVENANCE.")
        )
        if not auth_arch_approved or not is_authoritative_status_doc:
            if re_arch_claim.search(content):
                errors.append(
                    f"Fabricated or unauthorized OWNER_APPROVED architecture claim detected in '{rel_p}' (derived documents may never independently create owner-approved decisions)"
                )
            if re_generic_status_claim.search(content):
                errors.append(
                    f"Unauthorized 'Status: OWNER_APPROVED' claim detected in '{rel_p}' outside authoritative provenance"
                )
            if re_table_owner_approved.search(content):
                errors.append(
                    f"Unauthorized table row marked OWNER_APPROVED in '{rel_p}' without authoritative owner provenance"
                )

    return errors
```

### `verify_code_mirrors_and_lines` — `Lines 328–388`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `328` إلى السطر `388` (`Lines 328–388`)
- **الوظيفة:** تقارن الدوال وأرقام الأسطر الفعلية في الكود مع ما هو مكتوب في memory/code_mirrors/ وmemory/FUNCTION_REGISTRY.md وتكشف أي اختلاف أو نقص.
- **الكود الفعلي (`Lines 328–388`):**
```python
def verify_code_mirrors_and_lines() -> tuple[list[str], dict]:
    """Verify 1:1 code mirrors, exact line numbers, verbatim snippets, and zero duplicate/undocumented symbols."""
    errors: list[str] = []
    code_files = scm.discover_code_files()
    registry_path = ROOT / "memory" / "FUNCTION_REGISTRY.md"
    registry_text = registry_path.read_text(encoding="utf-8") if registry_path.exists() else ""
    if not registry_text:
        errors.append("Missing or empty memory/FUNCTION_REGISTRY.md")

    reg_rows = re.findall(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", registry_text, re.M)
    seen_reg_keys: set[tuple[str, str]] = set()
    for sym_name, sym_kind, owner_file in reg_rows:
        key = (sym_name, owner_file)
        if key in seen_reg_keys:
            errors.append(f"Duplicate symbol entry in FUNCTION_REGISTRY.md: {sym_name} in {owner_file}")
        seen_reg_keys.add(key)

    all_symbols: dict[str, list[dict]] = {}
    for file_path in code_files:
        rel_path = file_path.relative_to(ROOT).as_posix()
        raw_bytes = file_path.read_bytes()
        actual_sha = hashlib.sha256(raw_bytes).hexdigest()
        symbols = (
            scm.extract_python_symbols(file_path)
            if file_path.suffix.lower() == ".py"
            else scm.extract_ts_js_symbols(file_path)
        )
        all_symbols[rel_path] = symbols
        mirror_name = scm.mirror_filename_for(rel_path)
        mirror_path = ROOT / "memory" / "code_mirrors" / mirror_name
        if not mirror_path.exists():
            errors.append(f"Missing code mirror for {rel_path}: memory/code_mirrors/{mirror_name}")
            continue
        mirror_text = mirror_path.read_text(encoding="utf-8")
        if f"`{actual_sha}`" not in mirror_text:
            errors.append(f"Stale code mirror SHA-256 in {mirror_name} for {rel_path}")

        for sym in symbols:
            expected_range = f"Lines {sym['start_line']}–{sym['end_line']}"
            if f"### `{sym['name']}` — `{expected_range}`" not in mirror_text:
                errors.append(
                    f"Stale line reference or undocumented symbol in mirror {mirror_name}: expected {sym['name']} at {expected_range}"
                )
            if sym["snippet"] not in mirror_text:
                errors.append(f"Verbatim code snippet out of sync in mirror {mirror_name} for symbol {sym['name']}")
            reg_row_pattern = f"| `{sym['name']}` | `{sym['kind']}` | `{rel_path}` | `{expected_range}` |"
            if reg_row_pattern not in registry_text:
                errors.append(
                    f"Undocumented or stale symbol in FUNCTION_REGISTRY.md for {sym['name']} in {rel_path} ({expected_range})"
                )

    duplicates = scm.detect_duplicate_functions(all_symbols)
    if duplicates:
        errors.append(f"Duplicated functions detected across codebase: {duplicates}")

    stats = {
        "code_files_count": len(code_files),
        "symbols_verified": sum(len(v) for v in all_symbols.values()),
        "duplicate_functions_count": len(duplicates),
    }
    return errors, stats
```

### `verify_version_code_mirrors` — `Lines 392–463`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `392` إلى السطر `463` (`Lines 392–463`)
- **الوظيفة:** Verify 1:1 code mirrors, exact line numbers, verbatim snippets, and zero duplicates for a specific version.
- **الكود الفعلي (`Lines 392–463`):**
```python
def verify_version_code_mirrors(version_id: str) -> tuple[list[str], dict]:
    """Verify 1:1 code mirrors, exact line numbers, verbatim snippets, and zero duplicates for a specific version."""
    errors: list[str] = []
    vdir = scm.VERSIONS_DIR / version_id
    if not vdir.is_dir():
        return [f"Version directory not found: {vdir}"], {
            "version_id": version_id,
            "code_files_count": 0,
            "symbols_verified": 0,
            "duplicate_functions_count": 0,
        }

    code_files = scm.discover_version_code_files(version_id)
    reg_path = vdir / "docs" / "FUNCTION_REGISTRY.md"
    reg_text = reg_path.read_text(encoding="utf-8") if reg_path.exists() else ""
    if not reg_text:
        errors.append(f"Missing or empty {vdir.name}/docs/FUNCTION_REGISTRY.md")

    reg_rows = re.findall(r"^\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|", reg_text, re.M)
    seen_reg_keys: set[tuple[str, str]] = set()
    for sym_name, sym_kind, owner_file in reg_rows:
        key = (sym_name, owner_file)
        if key in seen_reg_keys:
            errors.append(f"Duplicate symbol entry in {version_id}/docs/FUNCTION_REGISTRY.md: {sym_name} in {owner_file}")
        seen_reg_keys.add(key)

    all_symbols: dict[str, list[dict]] = {}
    mirrors_dir = vdir / "docs" / "CODE_MIRRORS"

    for file_path in code_files:
        rel_in_version = file_path.relative_to(vdir).as_posix()
        raw_bytes = file_path.read_bytes()
        actual_sha = hashlib.sha256(raw_bytes).hexdigest()
        symbols = (
            scm.extract_python_symbols(file_path)
            if file_path.suffix.lower() == ".py"
            else scm.extract_ts_js_symbols(file_path)
        )
        all_symbols[rel_in_version] = symbols
        mirror_path = mirrors_dir / f"{rel_in_version}.md"
        if not mirror_path.exists():
            errors.append(f"Missing version code mirror for {rel_in_version}: {vdir.name}/docs/CODE_MIRRORS/{rel_in_version}.md")
            continue
        mirror_text = mirror_path.read_text(encoding="utf-8")
        if f"`{actual_sha}`" not in mirror_text:
            errors.append(f"Stale code mirror SHA-256 in {vdir.name}/docs/CODE_MIRRORS/{rel_in_version}.md for {rel_in_version}")

        for sym in symbols:
            expected_range = f"Lines {sym['start_line']}–{sym['end_line']}"
            if f"### `{sym['name']}` — `{expected_range}`" not in mirror_text:
                errors.append(
                    f"Stale line reference or undocumented symbol in mirror {vdir.name}/docs/CODE_MIRRORS/{rel_in_version}.md: expected {sym['name']} at {expected_range}"
                )
            if sym["snippet"] not in mirror_text:
                errors.append(f"Verbatim code snippet out of sync in mirror {rel_in_version}.md for symbol {sym['name']}")
            reg_row_pattern = f"| `{sym['name']}` | `{sym['kind']}` | `{rel_in_version}` | `{expected_range}` |"
            if reg_row_pattern not in reg_text:
                errors.append(
                    f"Undocumented or stale symbol in {version_id}/docs/FUNCTION_REGISTRY.md for {sym['name']} in {rel_in_version} ({expected_range})"
                )

    duplicates = scm.detect_duplicate_functions(all_symbols)
    if duplicates:
        errors.append(f"Duplicated functions detected in version {version_id}: {duplicates}")

    stats = {
        "version_id": version_id,
        "code_files_count": len(code_files),
        "symbols_verified": sum(len(v) for v in all_symbols.values()),
        "duplicate_functions_count": len(duplicates),
    }
    return errors, stats
```

### `verify_all_versions` — `Lines 466–474`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `466` إلى السطر `474` (`Lines 466–474`)
- **الوظيفة:** Verify code mirrors and function registries across all registered versions.
- **الكود الفعلي (`Lines 466–474`):**
```python
def verify_all_versions() -> tuple[list[str], dict]:
    """Verify code mirrors and function registries across all registered versions."""
    all_errors: list[str] = []
    version_stats: dict[str, dict] = {}
    for vid in scm.discover_version_ids():
        errs, st = verify_version_code_mirrors(vid)
        all_errors.extend(errs)
        version_stats[vid] = st
    return all_errors, version_stats
```

### `main` — `Lines 478–523`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `478` إلى السطر `523` (`Lines 478–523`)
- **الوظيفة:** تشغل جميع فحوصات تزامن الذاكرة وتكتب التقرير النهائي في brain_validation.json وترجع كود الخروج (0 للنجاح، 1 للفشل).
- **الكود الفعلي (`Lines 478–523`):**
```python
def main() -> None:
    """Run all External Brain, Vision, Repo-Wide Approval Provenance, Findings & Antigravity checks."""
    rule_errors = verify_antigravity_rules()
    vision_errors = verify_immutable_owner_vision()
    approval_errors = verify_owner_approval_provenance()
    mirror_errors, stats = verify_code_mirrors_and_lines()
    finding_errors, finding_stats = mf.verify_findings()

    # START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED | Author: Governance maintainer
    provenance_errors = ct.verify()
    all_errors = rule_errors + vision_errors + approval_errors + mirror_errors + finding_errors + provenance_errors
    # END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:54:49Z | EDITED

    # START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:48:00Z | EDITED | Author: orchestrator-planner
    version_arg = None
    for idx, arg in enumerate(sys.argv):
        if arg == "--version" and idx + 1 < len(sys.argv):
            version_arg = sys.argv[idx + 1]

    if version_arg:
        v_errors, v_stats = verify_version_code_mirrors(version_arg)
        all_errors.extend(v_errors)
        v_report = {version_arg: v_stats}
    else:
        v_errors, v_stats_map = verify_all_versions()
        all_errors.extend(v_errors)
        v_report = v_stats_map
    # END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:48:00Z | EDITED

    result = {
        "date": date.today().isoformat(),
        "status": "PASSED" if not all_errors else "FAILED",
        "code_files_verified": stats["code_files_count"],
        "symbols_and_line_ranges_verified": stats["symbols_verified"],
        "duplicate_functions_count": stats["duplicate_functions_count"],
        "findings_verified": finding_stats["total_findings"],
        "antigravity_rules_valid": len(rule_errors) == 0,
        "immutable_vision_valid": len(vision_errors) == 0,
        "approval_provenance_valid": len(approval_errors) == 0,
        "versions_verified": v_report,
        "errors": all_errors,
    }
    out_path = HERE / "brain_validation.json"
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(1 if all_errors else 0)
```
