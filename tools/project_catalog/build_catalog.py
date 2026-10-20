#!/usr/bin/env python3
"""Repository-wide File Catalog & Relationship Graph Builder for AI Graphic Designer.

Requires --write to update PROJECT_FILE_CATALOG.md, file_metadata.json, and relationships.json.
"""
from pathlib import Path
from datetime import date
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:50:00Z | EDITED | Author: orchestrator-planner
sys.path.insert(0, str(ROOT / "tools" / "memory_guard"))
import sync_code_mirrors as scm
EXCLUDED_DIRS = {".git", "node_modules", "__pycache__", ".venv", "packages", "baselines", "latest", "versions"}
VERSIONS_DIR = ROOT / "versions"
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:50:00Z | EDITED
DERIVED_SELF_OUTPUTS = {
    "tools/project_catalog/file_metadata.json",
    "tools/project_catalog/relationships.json",
    "tools/project_catalog/validation.json",
    "tools/memory_guard/brain_validation.json",
    "tools/tests/governance_test_report.json",
    "memory/session/RECOVERY_PACKET.json",
}


def discover_first_party_files() -> list[str]:
    """Return sorted list of all first-party repository-relative file paths."""
    files: list[str] = []
    for p in ROOT.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        # START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED | Author: Governance maintainer
        if rel == "memory/decisions/.approval_tx_journal.json":
            continue  # transient recovery journal; never an authoritative catalog entry
        # END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:50:37Z | EDITED
        # START CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:35:00Z | EDITED | Author: orchestrator-planner
        if rel.startswith("tools/update_packages/registry/") or rel.startswith("exports/updates/"):
            continue  # update packaging runtime state and generated archives; not source code
        # END CHANGE TASK-UPDATE-SYS-01 | 2026-10-18T01:35:00Z | EDITED
        # START CHANGE TASK-V01-PORTABILITY-01 | 2026-10-17T17:48:00Z | EDITED | Author: orchestrator-planner
        if rel.endswith((".zip", ".tar.gz", ".tar")):
            continue  # archive distributions are transport packages, not source code
        if any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts[:-1]):
            continue
        # END CHANGE TASK-V01-PORTABILITY-01 | 2026-10-17T17:48:00Z | EDITED
        files.append(rel)
    return sorted(files)


def describe_file(rel: str) -> dict[str, str]:
    """Return structured catalog metadata for a repository file path."""
    if rel in {"AGENTS.md", "GEMINI.md"}:
        return {
            "type": "Agent Entry Point & Always-On Constitution",
            "purpose": "Defines startup memory recall, the 5 Iron Laws against Vibe Coding bugs, and rule routing.",
            "contents": "Startup sequence, Full-File Read rule, WAL anti-compaction rule, Code Mirror rule, Sub-agent reviewer gate.",
            "why": "Ensure every agent or subagent in Antigravity starts with full context and strict guardrails.",
            "status": "ACTIVE / LIVING_CONSTITUTION",
            "authority": "Primary workspace agent instructions subordinate to direct user commands.",
            "trigger": "Any change to rule files, memory architecture, or startup sequence.",
        }
    if rel == "MASTER_PLAN.md":
        return {
            "type": "Master Plan & Modular Blueprint",
            "purpose": "Defines the 3 operational modes and 8 modular workstreams of AI Graphic Designer without forcing a single starting point.",
            "contents": "System vision, Clean SVG invariants, M01-M08 module matrix, and completion states.",
            "why": "Keep long-term architectural coherence across all modes of the AI Graphic Designer.",
            "status": "ACTIVE / LIVING_PLAN",
            "authority": "Project roadmap authority.",
            "trigger": "Module progress, new milestones, or architectural scope updates.",
        }
    if rel == "PROJECT_FILE_CATALOG.md":
        return {
            "type": "Repository Navigation & Relationship Index",
            "purpose": "Catalogs every first-party file in the repository with its purpose and upstream/downstream relationships.",
            "contents": "Directory map, per-file metadata entries, and explicit Related Files dependency blocks.",
            "why": "Let humans and AI agents locate any file and understand change impact without scanning the raw tree blindly.",
            "status": "ACTIVE / LIVING_DOCUMENT",
            "authority": "Repository navigation map verified by tools/project_catalog/verify_catalog.py.",
            "trigger": "Same-task update whenever any file is added, removed, moved, or changes responsibility.",
        }
    if rel.startswith(".agent_rules/") or rel.startswith(".agents/rules/"):
        name = Path(rel).stem.replace("_", " ").title()
        return {
            "type": "Agent Governance Rule",
            "purpose": f"Enforces {name} across the AI Graphic Designer workspace.",
            "contents": f"YAML frontmatter trigger and detailed operational constraints for {name}.",
            "why": "Prevent hallucinations, partial file reads, duplicate functions, context compaction amnesia, and messy SVG outputs.",
            "status": "ACTIVE",
            "authority": "Workspace rule enforced by AGENTS.md, GEMINI.md, and Antigravity.",
            "trigger": "When engineering standards or governance policies for this domain evolve.",
        }
    if rel.startswith(".agents/agents/"):
        name = Path(rel).stem
        return {
            "type": "Antigravity Custom Subagent Definition",
            "purpose": f"Defines the specialized `{name}` subagent persona, allowed tools, and system prompt.",
            "contents": "YAML frontmatter (name, description, tools, subagent, model) and specialized system instructions.",
            "why": "Enable isolated multi-agent task execution and mandatory independent QA review in Antigravity.",
            "status": "ACTIVE",
            "authority": "Subagent configuration discovered automatically by Antigravity `/agents` and `invoke_subagent`.",
            "trigger": "When subagent responsibilities, tool permissions, or review checklists change.",
        }
    if rel.startswith(".agents/skills/"):
        return {
            "type": "Antigravity Agent Skill",
            "purpose": "Provides a repeatable procedural workflow for synchronizing code mirrors or executing sub-agent review cycles.",
            "contents": "YAML frontmatter and step-by-step execution instructions.",
            "why": "Standardize multi-step memory synchronization and review verification.",
            "status": "ACTIVE",
            "authority": "Procedural skill invoked by agents or slash commands.",
            "trigger": "When CLI commands or verification steps change.",
        }
    if rel == ".agents/hooks.json":
        return {
            "type": "Antigravity Lifecycle Hooks Config",
            "purpose": "Configures SessionStart and Stop hooks for automatic memory recall and pre-stop brain verification.",
            "contents": "JSON hook definitions mapping SessionStart and Stop to tools/memory_guard/ hook scripts.",
            "why": "Automate memory recall at session start and block stopping when code mirrors are out of sync.",
            "status": "ACTIVE",
            "authority": "Enforced by Google Antigravity runtime loop.",
            "trigger": "When adding or modifying lifecycle hook scripts.",
        }
    if rel.startswith("memory/code_mirrors/"):
        return {
            "type": "1:1 Codebase Markdown Mirror",
            "purpose": "Documents every function, exact line numbers (Lines Start-End), verbatim code snippet, and upstream/downstream relationships for its corresponding code file.",
            "contents": "File overview, data-flow relationship table, function index, and line-numbered verbatim code blocks.",
            "why": "Serve as the agent's External Brain so humans and AI understand code and line locations without reading thousands of raw lines.",
            "status": "ACTIVE / AUTO_SYNCHRONIZED",
            "authority": "Synchronized from actual source code via tools/memory_guard/sync_code_mirrors.py.",
            "trigger": "Same-turn update whenever the corresponding source code file changes.",
        }
    if rel.startswith("memory/"):
        return {
            "type": "External Brain Memory Artifact",
            "purpose": f"Persistent project memory file (`{rel}`) storing architecture flow, function registry, live session WAL, or decisions.",
            "contents": "Structured Markdown tables and state records surviving context compaction and session resets.",
            "why": "Eliminate amnesia across context compactions and chat resets.",
            "status": "ACTIVE / LIVING_MEMORY",
            "authority": "Authoritative External Brain state.",
            "trigger": "Updated continuously during task execution (Write-Ahead Logging).",
        }
    if rel.startswith("docs/"):
        return {
            "type": "Domain & Architecture Specification",
            "purpose": f"Detailed specification document (`{rel}`) for AI Graphic Designer modes, Clean SVG rules, Typography, or Antigravity setup.",
            "contents": "Mermaid diagrams, JSON schemas, mathematical invariants, and transformation reports.",
            "why": "Provide complete domain grounding for developers and AI agents.",
            "status": "ACTIVE / SPECIFICATION",
            "authority": "Approved domain specification.",
            "trigger": "When product requirements or technical schemas evolve.",
        }
    if rel.startswith("tools/"):
        return {
            "type": "Governance & Verification Tooling",
            "purpose": f"Automated verification or synchronization artifact (`{rel}`).",
            "contents": "Executable Python script or JSON validation metadata for memory mirrors, catalog, or review exports.",
            "why": "Enforce deterministic verification of line numbers, duplicate functions, and catalog completeness.",
            "status": "ACTIVE",
            "authority": "Automated repository verifier.",
            "trigger": "When verification logic or repository structure changes.",
        }
    return {
        "type": "First-Party Project File",
        "purpose": f"Repository file `{rel}` supporting project packaging and review governance.",
        "contents": "Project configuration, script, or review history record.",
        "why": "Maintain complete repository portability and governance.",
        "status": "ACTIVE",
        "authority": "First-party repository file.",
        "trigger": "When packaging or review export state changes.",
    }


def build_relationships(all_files: list[str]) -> list[dict[str, str]]:
    """Build explicit directed relationships across repository files."""
    edges: list[dict[str, str]] = []
    file_set = set(all_files)

    def add_edge(src: str, dst: str, rel_type: str, direction: str, impact: str, evidence: str) -> None:
        if src in file_set and dst in file_set and src != dst:
            edges.append({
                "source": src,
                "target": dst,
                "relationship": rel_type,
                "direction": direction,
                "change_impact": impact,
                "evidence": evidence,
            })

    add_edge(
        "AGENTS.md",
        "GEMINI.md",
        "Synchronized root agent entry points for standard and Antigravity surfaces",
        "Bidirectional",
        "Keep core rules and startup sequence aligned across both files.",
        "Direct @AGENTS.md reference in GEMINI.md",
    )
    add_edge(
        "AGENTS.md",
        "memory/MEMORY_INDEX.md",
        "Routes every session startup to the External Brain master index",
        "AGENTS.md -> memory/MEMORY_INDEX.md",
        "Update AGENTS.md startup sequence if memory index path or structure changes.",
        "Mandatory Session Startup Sequence in AGENTS.md",
    )
    add_edge(
        "AGENTS.md",
        "MASTER_PLAN.md",
        "Links agent entry constitution to the whole-project modular master plan",
        "AGENTS.md -> MASTER_PLAN.md",
        "Synchronize module codes and completion states.",
        "Rule routing table in AGENTS.md",
    )
    for f in all_files:
        if f.startswith(".agent_rules/"):
            twin = f.replace(".agent_rules/", ".agents/rules/", 1)
            add_edge(
                f,
                twin,
                "Mirrored rule file between .agent_rules/ and Antigravity native .agents/rules/",
                "Bidirectional",
                "Update both files together whenever rule instructions change.",
                "Dual-surface rule compatibility",
            )
            add_edge(
                "AGENTS.md",
                f,
                "Routes tasks to domain-specific governance rule",
                "AGENTS.md -> " + f,
                "Update AGENTS.md routing table if rule scope changes.",
                "Rule Routing Table in AGENTS.md",
            )
        if f.endswith(".py"):
            mirror_name = f.replace("/", "__") + ".md"
            mirror_rel = f"memory/code_mirrors/{mirror_name}"
            add_edge(
                f,
                mirror_rel,
                "1:1 Codebase Markdown Mirror documenting functions, exact lines, snippets, and data flow",
                f"{f} -> {mirror_rel}",
                "Run `python3 tools/memory_guard/sync_code_mirrors.py --write` whenever the Python file changes.",
                "AST extraction via sync_code_mirrors.py",
            )
            add_edge(
                f,
                "memory/FUNCTION_REGISTRY.md",
                "Registers all functions and exact line numbers in the central function index",
                f"{f} -> memory/FUNCTION_REGISTRY.md",
                "Re-sync FUNCTION_REGISTRY.md whenever functions or line numbers change.",
                "Central anti-duplication registry",
            )
    return edges


# START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | CREATED | Author: orchestrator-planner
def discover_version_files(version_id: str) -> list[str]:
    """Return sorted list of relative file paths within a specific version directory."""
    vdir = VERSIONS_DIR / version_id
    if not vdir.is_dir():
        return []
    files: list[str] = []
    for p in vdir.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(vdir).as_posix()
        if any(part in EXCLUDED_DIRS for part in p.relative_to(vdir).parts[:-1]):
            continue
        files.append(rel)
    return sorted(files)


def describe_version_file(rel: str, version_id: str) -> dict[str, str]:
    """Return structured catalog metadata for a version-scoped file path."""
    if rel == "README.md":
        return {
            "type": "Version Overview & Architecture Entry Point",
            "purpose": f"Overview of {version_id} architecture hypothesis, module structure, and execution instructions.",
            "contents": "Hypothesis summary, directory tree, dependency requirements, and run guides.",
            "why": "Provide clear architectural entry point and isolation boundaries for this experimental version.",
            "status": "ACTIVE / EXPERIMENTAL",
            "authority": f"Version {version_id} documentation authority.",
            "trigger": "When version architecture, modules, or hypotheses change.",
        }
    if rel == "PROJECT_FILE_CATALOG.md":
        return {
            "type": "Version File Catalog & Relationship Index",
            "purpose": f"Catalogs every file within {version_id} with its purpose and intra-version relationships.",
            "contents": "Directory map, per-file metadata entries, and explicit Related Files dependency blocks.",
            "why": "Maintain complete intra-version navigation and file relationship isolation.",
            "status": "ACTIVE / AUTO_SYNCHRONIZED",
            "authority": f"Version {version_id} file catalog.",
            "trigger": "Same-task update whenever any file in this version is added, removed, or changes.",
        }
    if rel == "docs/FUNCTION_REGISTRY.md":
        return {
            "type": "Version Central Function Registry",
            "purpose": f"Registers all functions, classes, line numbers, and signatures within {version_id} to prevent intra-version duplication.",
            "contents": "Symbol index table, line ranges, signatures, and descriptions for this version.",
            "why": "Enforce zero duplicate functions within this architectural version.",
            "status": "ACTIVE / AUTO_SYNCHRONIZED",
            "authority": f"Version {version_id} function registry synchronized via sync_code_mirrors.py --version {version_id}.",
            "trigger": "Same-turn update whenever source files in this version change.",
        }
    if rel.startswith("docs/CODE_MIRRORS/"):
        return {
            "type": "Version 1:1 Codebase Markdown Mirror",
            "purpose": f"Documents functions, exact line numbers, and verbatim snippets for {rel} within {version_id}.",
            "contents": "File overview, relationships, symbol table, and verbatim code blocks.",
            "why": f"Serve as External Brain code mirror scoped strictly to {version_id}.",
            "status": "ACTIVE / AUTO_SYNCHRONIZED",
            "authority": f"Generated mirror via sync_code_mirrors.py --version {version_id}.",
            "trigger": "Same-turn update whenever the corresponding source file in this version changes.",
        }
    if rel.startswith("docs/"):
        return {
            "type": "Version Architecture Specification",
            "purpose": f"Architecture and technical specifications for {version_id}.",
            "contents": "Component diagrams, pipeline flows, and design decisions for this version.",
            "why": "Document version-specific design rationale and trade-offs.",
            "status": "ACTIVE / SPECIFICATION",
            "authority": f"Version {version_id} specification authority.",
            "trigger": "When version design or contracts evolve.",
        }
    if rel.startswith("src/"):
        return {
            "type": "Version Core Source Code",
            "purpose": f"Implementation source code for {rel} in {version_id}.",
            "contents": "Classes, functions, algorithms, and domain logic for this architectural approach.",
            "why": f"Execute the specific architectural hypothesis of {version_id}.",
            "status": "ACTIVE / EXPERIMENTAL",
            "authority": f"Version {version_id} source implementation.",
            "trigger": "When implementation logic is updated.",
        }
    if rel.startswith("tests/"):
        return {
            "type": "Version Test Suite",
            "purpose": f"Unit, integration, and verification tests for {version_id}.",
            "contents": "Test cases validating functionality, performance, and invariants for this version.",
            "why": f"Ensure rigorous automated testing of {version_id}.",
            "status": "ACTIVE",
            "authority": f"Version {version_id} test specification.",
            "trigger": "When features or test scenarios for this version change.",
        }
    if rel.startswith("experiments/"):
        return {
            "type": "Version Experiment Configuration & Results",
            "purpose": f"Experiment parameters, execution logs, and benchmark observations for {version_id}.",
            "contents": "Experiment configurations, execution logs, and objective telemetry records.",
            "why": "Record reproducible experimentation history without fabrication.",
            "status": "ACTIVE / EXPERIMENTAL_RECORD",
            "authority": f"Version {version_id} experiment history.",
            "trigger": "When experiments are configured or executed.",
        }
    if rel.startswith("dependencies/"):
        return {
            "type": "Version Dependencies Configuration",
            "purpose": f"Dependency declarations and environment requirements for {version_id}.",
            "contents": "Requirements or package definitions for this version.",
            "why": "Isolate third-party library requirements per architecture version.",
            "status": "ACTIVE",
            "authority": f"Version {version_id} environment specification.",
            "trigger": "When version dependencies change.",
        }
    return {
        "type": "Version First-Party File",
        "purpose": f"File {rel} supporting version {version_id}.",
        "contents": "Supporting configuration, asset, or documentation.",
        "why": f"Maintain completeness of {version_id}.",
        "status": "ACTIVE",
        "authority": f"Version {version_id} file.",
        "trigger": "When file content changes.",
    }


def build_version_relationships(version_files: list[str], version_id: str) -> list[dict[str, str]]:
    """Build directed relationships across files within a specific version."""
    edges: list[dict[str, str]] = []
    file_set = set(version_files)

    for f in version_files:
        if f.startswith("src/") and (f.endswith(".py") or f.endswith(".ts") or f.endswith(".js")):
            mirror_rel = f"docs/CODE_MIRRORS/{f}.md"
            if mirror_rel in file_set:
                edges.append({
                    "source": f,
                    "target": mirror_rel,
                    "relationship": "1:1 Version Codebase Markdown Mirror documenting functions and line numbers",
                    "direction": f"{f} -> {mirror_rel}",
                    "change_impact": f"Run `python3 tools/memory_guard/sync_code_mirrors.py --version {version_id} --write` when this file changes.",
                    "evidence": "Version AST extraction via sync_code_mirrors.py",
                })
            if "docs/FUNCTION_REGISTRY.md" in file_set:
                edges.append({
                    "source": f,
                    "target": "docs/FUNCTION_REGISTRY.md",
                    "relationship": "Registers all functions and exact lines in the version function registry",
                    "direction": f"{f} -> docs/FUNCTION_REGISTRY.md",
                    "change_impact": "Update version registry on code change.",
                    "evidence": "Version function registry index",
                })
        if f.startswith("tests/") and "src/pipeline.py" in file_set:
            edges.append({
                "source": f,
                "target": "src/pipeline.py",
                "relationship": "Tests version pipeline implementation",
                "direction": f"{f} -> src/pipeline.py",
                "change_impact": "Run test suite when pipeline logic changes.",
                "evidence": "Version test import",
            })
        if f == "README.md" and "docs/ARCHITECTURE.md" in file_set:
            edges.append({
                "source": "README.md",
                "target": "docs/ARCHITECTURE.md",
                "relationship": "Links version overview to detailed architecture specification",
                "direction": "README.md -> docs/ARCHITECTURE.md",
                "change_impact": "Keep overview aligned with architecture doc.",
                "evidence": "Version architecture overview link",
            })
    return edges


def build_version_catalog(version_id: str, write_mode: bool = False) -> dict:
    """Build PROJECT_FILE_CATALOG.md for a specific version."""
    vdir = VERSIONS_DIR / version_id
    if not vdir.is_dir():
        raise ValueError(f"Version directory not found: {vdir}")

    catalog_path = vdir / "PROJECT_FILE_CATALOG.md"
    if write_mode and not catalog_path.exists():
        catalog_path.write_text(f"# PROJECT FILE CATALOG — {version_id}\n", encoding="utf-8")

    version_files = discover_version_files(version_id)
    metadata = {f: describe_version_file(f, version_id) for f in version_files}
    edges = build_version_relationships(version_files, version_id)

    by_source: dict[str, list[dict[str, str]]] = {f: [] for f in version_files}
    for e in edges:
        by_source[e["source"]].append(e)
        by_source[e["target"]].append({
            "source": e["target"],
            "target": e["source"],
            "relationship": e["relationship"],
            "direction": e["direction"],
            "change_impact": e["change_impact"],
            "evidence": e["evidence"],
        })

    lines: list[str] = [
        f"# الفهرس الشامل لملفات الإصدار وعلاقاتها (`PROJECT_FILE_CATALOG.md` — `{version_id}`)",
        "",
        f"**تاريخ التحديث:** `{date.today().isoformat()}` | **إجمالي الملفات المفهرسة:** `{len(version_files)}` (`100% Coverage`)",
        "",
        f"يوثق هذا الفهرس الحي كافة ملفات الإصدار المعماري `{version_id}` والغرض منها وعلاقاتها المتبادلة.",
        "",
        "## سجل الملفات التفصيلي (`Detailed File Entries`)",
        "",
    ]

    for f in version_files:
        info = metadata[f]
        rels = by_source.get(f, [])
        seen_targets: set[str] = set()
        unique_rels = []
        for r in rels:
            if r["target"] not in seen_targets:
                seen_targets.add(r["target"])
                unique_rels.append(r)

        lines.extend([
            f"### `{f}`",
            f"- **Path:** `{f}`",
            f"- **Type:** {info['type']}",
            f"- **Purpose:** {info['purpose']}",
            f"- **Contents summary:** {info['contents']}",
            f"- **Why it exists:** {info['why']}",
            f"- **Current status:** {info['status']}",
            f"- **Source of truth / authority:** {info['authority']}",
            f"- **Update trigger:** {info['trigger']}",
        ])
        if unique_rels:
            lines.append("- **Related Files:** Yes")
            for r in unique_rels:
                lines.extend([
                    f"#### `{r['target']}`",
                    f"- **Relationship:** {r['relationship']}",
                    f"- **Direction:** `{r['direction']}`",
                    f"- **Change impact:** {r['change_impact']}",
                    f"- **Evidence:** {r['evidence']}",
                ])
        else:
            lines.append("- **Related Files:** No")
            lines.append("- **Related Files:** None currently identified.")
        lines.append("")

    if write_mode:
        catalog_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")

    return {
        "version_id": version_id,
        "total_files": len(version_files),
        "relationships": len(edges),
        "write_mode": write_mode,
    }
# END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | CREATED


def main() -> None:
    """Build PROJECT_FILE_CATALOG.md and supporting metadata JSON files."""
    if "--write" not in sys.argv:
        print("Pass --write to generate PROJECT_FILE_CATALOG.md")
        return

    # START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | EDITED | Author: orchestrator-planner
    version_arg = None
    all_versions = "--all-versions" in sys.argv
    for idx, arg in enumerate(sys.argv):
        if arg == "--version" and idx + 1 < len(sys.argv):
            version_arg = sys.argv[idx + 1]

    if version_arg:
        res = build_version_catalog(version_arg, write_mode=True)
        print(json.dumps(res, ensure_ascii=False))
        return
    # END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | EDITED

    # Ensure metadata files exist in the file list by touching them first if needed
    for derived_rel in DERIVED_SELF_OUTPUTS:
        dp = ROOT / derived_rel
        dp.parent.mkdir(parents=True, exist_ok=True)
        if not dp.exists():
            dp.write_text("{}\n", encoding="utf-8")

    catalog_path = ROOT / "PROJECT_FILE_CATALOG.md"
    if not catalog_path.exists():
        catalog_path.write_text("# PROJECT FILE CATALOG\n", encoding="utf-8")

    all_files = discover_first_party_files()
    metadata = {f: describe_file(f) for f in all_files}
    edges = build_relationships(all_files)

    by_source: dict[str, list[dict[str, str]]] = {f: [] for f in all_files}
    for e in edges:
        by_source[e["source"]].append(e)
        by_source[e["target"]].append({
            "source": e["target"],
            "target": e["source"],
            "relationship": e["relationship"],
            "direction": e["direction"],
            "change_impact": e["change_impact"],
            "evidence": e["evidence"],
        })

    lines: list[str] = [
        "# الفهرس الشامل لملفات المشروع وعلاقاتها (`PROJECT_FILE_CATALOG.md`)",
        "",
        f"**تاريخ التحديث:** `{date.today().isoformat()}` | **إجمالي الملفات المفهرسة:** `{len(all_files)}` (`100% Coverage`)",
        "",
        "يوثق هذا الفهرس الحي كل ملف مملوك للمشروع (`First-Party File`) والغرض منه وعلاقاته بالملفات الأخرى (`Related Files`).",
        "",
        "## سجل الملفات التفصيلي (`Detailed File Entries`)",
        "",
    ]

    for f in all_files:
        info = metadata[f]
        rels = by_source.get(f, [])
        seen_targets: set[str] = set()
        unique_rels = []
        for r in rels:
            if r["target"] not in seen_targets:
                seen_targets.add(r["target"])
                unique_rels.append(r)

        lines.extend([
            f"### `{f}`",
            f"- **Path:** `{f}`",
            f"- **Type:** {info['type']}",
            f"- **Purpose:** {info['purpose']}",
            f"- **Contents summary:** {info['contents']}",
            f"- **Why it exists:** {info['why']}",
            f"- **Current status:** {info['status']}",
            f"- **Source of truth / authority:** {info['authority']}",
            f"- **Update trigger:** {info['trigger']}",
        ])
        if unique_rels:
            lines.append("- **Related Files:** Yes")
            for r in unique_rels:
                lines.extend([
                    f"#### `{r['target']}`",
                    f"- **Relationship:** {r['relationship']}",
                    f"- **Direction:** `{r['direction']}`",
                    f"- **Change impact:** {r['change_impact']}",
                    f"- **Evidence:** {r['evidence']}",
                ])
        else:
            lines.append("- **Related Files:** No")
            lines.append("- **Related Files:** None currently identified.")
        lines.append("")

    catalog_path.write_text("\n".join(lines).strip() + "\n", encoding="utf-8")
    (HERE / "file_metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (HERE / "relationships.json").write_text(json.dumps(edges, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    
    # START CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | EDITED | Author: orchestrator-planner
    v_catalogs = {}
    if all_versions:
        for vid in scm.discover_version_ids():
            vres = build_version_catalog(vid, write_mode=True)
            v_catalogs[vid] = vres
    # END CHANGE TASK-MULTI-VER-01 | 2026-10-17T08:52:00Z | EDITED

    print(json.dumps({
        "status": "CATALOG_BUILT",
        "total_files": len(all_files),
        "relationships": len(edges),
        "versions": v_catalogs,
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
