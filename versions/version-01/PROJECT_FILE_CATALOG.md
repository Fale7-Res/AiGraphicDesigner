# الفهرس الشامل لملفات الإصدار وعلاقاتها (`PROJECT_FILE_CATALOG.md` — `version-01`)

**تاريخ التحديث:** `2026-10-19` | **إجمالي الملفات المفهرسة:** `163` (`100% Coverage`)

يوثق هذا الفهرس الحي كافة ملفات الإصدار المعماري `version-01` والغرض منها وعلاقاتها المتبادلة.

## سجل الملفات التفصيلي (`Detailed File Entries`)

### `PROJECT_FILE_CATALOG.md`
- **Path:** `PROJECT_FILE_CATALOG.md`
- **Type:** Version File Catalog & Relationship Index
- **Purpose:** Catalogs every file within version-01 with its purpose and intra-version relationships.
- **Contents summary:** Directory map, per-file metadata entries, and explicit Related Files dependency blocks.
- **Why it exists:** Maintain complete intra-version navigation and file relationship isolation.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Version version-01 file catalog.
- **Update trigger:** Same-task update whenever any file in this version is added, removed, or changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `README.md`
- **Path:** `README.md`
- **Type:** Version Overview & Architecture Entry Point
- **Purpose:** Overview of version-01 architecture hypothesis, module structure, and execution instructions.
- **Contents summary:** Hypothesis summary, directory tree, dependency requirements, and run guides.
- **Why it exists:** Provide clear architectural entry point and isolation boundaries for this experimental version.
- **Current status:** ACTIVE / EXPERIMENTAL
- **Source of truth / authority:** Version version-01 documentation authority.
- **Update trigger:** When version architecture, modules, or hypotheses change.
- **Related Files:** Yes
#### `docs/ARCHITECTURE.md`
- **Relationship:** Links version overview to detailed architecture specification
- **Direction:** `README.md -> docs/ARCHITECTURE.md`
- **Change impact:** Keep overview aligned with architecture doc.
- **Evidence:** Version architecture overview link

### `dependencies/requirements.txt`
- **Path:** `dependencies/requirements.txt`
- **Type:** Version Dependencies Configuration
- **Purpose:** Dependency declarations and environment requirements for version-01.
- **Contents summary:** Requirements or package definitions for this version.
- **Why it exists:** Isolate third-party library requirements per architecture version.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 environment specification.
- **Update trigger:** When version dependencies change.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/ARCHITECTURE.md`
- **Path:** `docs/ARCHITECTURE.md`
- **Type:** Version Architecture Specification
- **Purpose:** Architecture and technical specifications for version-01.
- **Contents summary:** Component diagrams, pipeline flows, and design decisions for this version.
- **Why it exists:** Document version-specific design rationale and trade-offs.
- **Current status:** ACTIVE / SPECIFICATION
- **Source of truth / authority:** Version version-01 specification authority.
- **Update trigger:** When version design or contracts evolve.
- **Related Files:** Yes
#### `README.md`
- **Relationship:** Links version overview to detailed architecture specification
- **Direction:** `README.md -> docs/ARCHITECTURE.md`
- **Change impact:** Keep overview aligned with architecture doc.
- **Evidence:** Version architecture overview link

### `docs/CODE_MIRRORS/experiments/geometry_correct_planar/planar_tracer.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/geometry_correct_planar/planar_tracer.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/geometry_correct_planar/planar_tracer.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/geometry_correct_planar/run_planar_benchmark.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/geometry_correct_planar/run_planar_benchmark.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/geometry_correct_planar/run_planar_benchmark.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/preliminary_visual_tests/run_preliminary_tests.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/preliminary_visual_tests/run_preliminary_tests.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/preliminary_visual_tests/run_preliminary_tests.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/check_grad_eval.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/check_grad_eval.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/check_grad_eval.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/diagnostic_exact_boundary.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/diagnostic_exact_boundary.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/diagnostic_exact_boundary.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/run_all_12_benchmark.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/run_all_12_benchmark.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/run_all_12_benchmark.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/stage_by_stage_error_analysis.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/stage_by_stage_error_analysis.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/stage_by_stage_error_analysis.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_enhanced_pipeline.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_enhanced_pipeline.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/test_enhanced_pipeline.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_grad_step.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_grad_step.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/test_grad_step.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_gradient_integration.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_gradient_integration.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/test_gradient_integration.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_seeds.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/stage_error_analysis/test_seeds.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/stage_error_analysis/test_seeds.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/experiments/synthetic_illumination/generate_and_benchmark_synthetic.py.md`
- **Path:** `docs/CODE_MIRRORS/experiments/synthetic_illumination/generate_and_benchmark_synthetic.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/experiments/synthetic_illumination/generate_and_benchmark_synthetic.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/CODE_MIRRORS/src/geometry/bezier.py.md`
- **Path:** `docs/CODE_MIRRORS/src/geometry/bezier.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/src/geometry/bezier.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** Yes
#### `src/geometry/bezier.py`
- **Relationship:** 1:1 Version Codebase Markdown Mirror documenting functions and line numbers
- **Direction:** `src/geometry/bezier.py -> docs/CODE_MIRRORS/src/geometry/bezier.py.md`
- **Change impact:** Run `python3 tools/memory_guard/sync_code_mirrors.py --version version-01 --write` when this file changes.
- **Evidence:** Version AST extraction via sync_code_mirrors.py

### `docs/CODE_MIRRORS/src/pipeline.py.md`
- **Path:** `docs/CODE_MIRRORS/src/pipeline.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/src/pipeline.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** Yes
#### `src/pipeline.py`
- **Relationship:** 1:1 Version Codebase Markdown Mirror documenting functions and line numbers
- **Direction:** `src/pipeline.py -> docs/CODE_MIRRORS/src/pipeline.py.md`
- **Change impact:** Run `python3 tools/memory_guard/sync_code_mirrors.py --version version-01 --write` when this file changes.
- **Evidence:** Version AST extraction via sync_code_mirrors.py

### `docs/CODE_MIRRORS/tests/test_version.py.md`
- **Path:** `docs/CODE_MIRRORS/tests/test_version.py.md`
- **Type:** Version 1:1 Codebase Markdown Mirror
- **Purpose:** Documents functions, exact line numbers, and verbatim snippets for docs/CODE_MIRRORS/tests/test_version.py.md within version-01.
- **Contents summary:** File overview, relationships, symbol table, and verbatim code blocks.
- **Why it exists:** Serve as External Brain code mirror scoped strictly to version-01.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Generated mirror via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever the corresponding source file in this version changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `docs/FUNCTION_REGISTRY.md`
- **Path:** `docs/FUNCTION_REGISTRY.md`
- **Type:** Version Central Function Registry
- **Purpose:** Registers all functions, classes, line numbers, and signatures within version-01 to prevent intra-version duplication.
- **Contents summary:** Symbol index table, line ranges, signatures, and descriptions for this version.
- **Why it exists:** Enforce zero duplicate functions within this architectural version.
- **Current status:** ACTIVE / AUTO_SYNCHRONIZED
- **Source of truth / authority:** Version version-01 function registry synchronized via sync_code_mirrors.py --version version-01.
- **Update trigger:** Same-turn update whenever source files in this version change.
- **Related Files:** Yes
#### `src/geometry/bezier.py`
- **Relationship:** Registers all functions and exact lines in the version function registry
- **Direction:** `src/geometry/bezier.py -> docs/FUNCTION_REGISTRY.md`
- **Change impact:** Update version registry on code change.
- **Evidence:** Version function registry index
#### `src/pipeline.py`
- **Relationship:** Registers all functions and exact lines in the version function registry
- **Direction:** `src/pipeline.py -> docs/FUNCTION_REGISTRY.md`
- **Change impact:** Update version registry on code change.
- **Evidence:** Version function registry index

### `experiments/EXPERIMENT_CONFIG.json`
- **Path:** `experiments/EXPERIMENT_CONFIG.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/EXPERIMENT_LOG.md`
- **Path:** `experiments/EXPERIMENT_LOG.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/V01_FINAL_INVESTIGATION_PORTABLE_HANDOFF.zip`
- **Path:** `experiments/V01_FINAL_INVESTIGATION_PORTABLE_HANDOFF.zip`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/V01_FINAL_PERFORMANCE_AND_MEMORY_AUDIT.md`
- **Path:** `experiments/V01_FINAL_PERFORMANCE_AND_MEMORY_AUDIT.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_baseline_diff.png`
- **Path:** `experiments/fidelity_diagnostics/A01_baseline_diff.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_baseline_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/A01_baseline_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_k24_diff.png`
- **Path:** `experiments/fidelity_diagnostics/A01_k24_diff.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_k24_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/A01_k24_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_v01_improved.svg`
- **Path:** `experiments/fidelity_diagnostics/A01_v01_improved.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_v01_improved_diff.png`
- **Path:** `experiments/fidelity_diagnostics/A01_v01_improved_diff.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/A01_v01_improved_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/A01_v01_improved_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/STAGE_A_FIDELITY_REPORT.md`
- **Path:** `experiments/fidelity_diagnostics/STAGE_A_FIDELITY_REPORT.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/VERSION_01_VISUAL_CORRECTION_CYCLE_REPORT.md`
- **Path:** `experiments/fidelity_diagnostics/VERSION_01_VISUAL_CORRECTION_CYCLE_REPORT.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/all_12_rerun_metrics.json`
- **Path:** `experiments/fidelity_diagnostics/all_12_rerun_metrics.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/diff_quant_svg.png`
- **Path:** `experiments/fidelity_diagnostics/diff_quant_svg.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/quant.png`
- **Path:** `experiments/fidelity_diagnostics/quant.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rend_bgr.png`
- **Path:** `experiments/fidelity_diagnostics/rend_bgr.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A01_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A01_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A02_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A02_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A03_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A03_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A04_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A04_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A05_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A05_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A06_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A06_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A07_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A07_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A08_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A08_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A09_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A09_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A10_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A10_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A11_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A11_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/rendered_pngs/A12_rendered.png`
- **Path:** `experiments/fidelity_diagnostics/rendered_pngs/A12_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/fidelity_diagnostics/stage_by_stage_benchmark.json`
- **Path:** `experiments/fidelity_diagnostics/stage_by_stage_benchmark.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/00_quantized.png`
- **Path:** `experiments/geometry_correct_planar/A01_shield/00_quantized.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m1_baseline_stroke1.svg`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m1_baseline_stroke1.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m1_baseline_stroke1_rendered.png`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m1_baseline_stroke1_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m2_baseline_no_stroke.svg`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m2_baseline_no_stroke.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m2_baseline_no_stroke_rendered.png`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m2_baseline_no_stroke_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m3_exact_planar.svg`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m3_exact_planar.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m3_exact_planar_rendered.png`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m3_exact_planar_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m4_smooth_planar_rendered.png`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m4_smooth_planar_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/A01_shield/m4_smooth_planar_zero_bloat.svg`
- **Path:** `experiments/geometry_correct_planar/A01_shield/m4_smooth_planar_zero_bloat.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/PLANAR_EXPERIMENT_REPORT.md`
- **Path:** `experiments/geometry_correct_planar/PLANAR_EXPERIMENT_REPORT.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/planar_benchmark_results.json`
- **Path:** `experiments/geometry_correct_planar/planar_benchmark_results.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/planar_tracer.py`
- **Path:** `experiments/geometry_correct_planar/planar_tracer.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/run_planar_benchmark.py`
- **Path:** `experiments/geometry_correct_planar/run_planar_benchmark.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/00_quantized.png`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/00_quantized.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m1_baseline_stroke1.svg`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m1_baseline_stroke1.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m1_baseline_stroke1_rendered.png`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m1_baseline_stroke1_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m2_baseline_no_stroke.svg`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m2_baseline_no_stroke.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m2_baseline_no_stroke_rendered.png`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m2_baseline_no_stroke_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m3_exact_planar.svg`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m3_exact_planar.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m3_exact_planar_rendered.png`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m3_exact_planar_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m4_smooth_planar_rendered.png`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m4_smooth_planar_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/geometry_correct_planar/synthetic_nested/m4_smooth_planar_zero_bloat.svg`
- **Path:** `experiments/geometry_correct_planar/synthetic_nested/m4_smooth_planar_zero_bloat.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/PRELIMINARY_VISUAL_TESTS_REPORT.md`
- **Path:** `experiments/preliminary_visual_tests/PRELIMINARY_VISUAL_TESTS_REPORT.md`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A01_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A01_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A02_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A02_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A03_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A03_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A04_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A04_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A05_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A05_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A06_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A06_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A07_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A07_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A08_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A08_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A09_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A09_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A10_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A10_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A11_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A11_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/outputs/A12_v01_vector.svg`
- **Path:** `experiments/preliminary_visual_tests/outputs/A12_v01_vector.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/results_summary.json`
- **Path:** `experiments/preliminary_visual_tests/results_summary.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/preliminary_visual_tests/run_preliminary_tests.py`
- **Path:** `experiments/preliminary_visual_tests/run_preliminary_tests.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/00_original.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/00_original.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/01_diff_quant.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/01_diff_quant.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/01_quantized.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/01_quantized.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/02_diff_poly.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/02_diff_poly.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/02_polygon_raster.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/02_polygon_raster.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/03_bezier_rendered.svg`
- **Path:** `experiments/stage_error_analysis/A01_shield/03_bezier_rendered.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/04_diff_svg.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/04_diff_svg.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/04_rendered_svg.png`
- **Path:** `experiments/stage_error_analysis/A01_shield/04_rendered_svg.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_shield/stage_error_report.json`
- **Path:** `experiments/stage_error_analysis/A01_shield/stage_error_report.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_test_improved.png`
- **Path:** `experiments/stage_error_analysis/A01_test_improved.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/A01_test_improved.svg`
- **Path:** `experiments/stage_error_analysis/A01_test_improved.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/check_grad_eval.py`
- **Path:** `experiments/stage_error_analysis/check_grad_eval.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/check_pipe.png`
- **Path:** `experiments/stage_error_analysis/check_pipe.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/diagnostic_exact_boundary.py`
- **Path:** `experiments/stage_error_analysis/diagnostic_exact_boundary.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/grad_test.png`
- **Path:** `experiments/stage_error_analysis/grad_test.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/improved_rendered.png`
- **Path:** `experiments/stage_error_analysis/improved_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/01_quantized.png`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/01_quantized.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_diff_svg_vs_quant.png`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_diff_svg_vs_quant.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_pixel_run.svg`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_pixel_run.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_pixel_run_rendered.png`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/exp1_pixel_run_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/exp2_raw_centers_rendered.png`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/exp2_raw_centers_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/exp2_raw_diff_quant.png`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/exp2_raw_diff_quant.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/iteration_07_diagnostics/iteration_07_experiment_report.json`
- **Path:** `experiments/stage_error_analysis/iteration_07_diagnostics/iteration_07_experiment_report.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/nc_12.png`
- **Path:** `experiments/stage_error_analysis/nc_12.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/nc_16.png`
- **Path:** `experiments/stage_error_analysis/nc_16.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/nc_20.png`
- **Path:** `experiments/stage_error_analysis/nc_20.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/nc_24.png`
- **Path:** `experiments/stage_error_analysis/nc_24.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/nc_8.png`
- **Path:** `experiments/stage_error_analysis/nc_8.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/run_all_12_benchmark.py`
- **Path:** `experiments/stage_error_analysis/run_all_12_benchmark.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/seed_0.png`
- **Path:** `experiments/stage_error_analysis/seed_0.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/seed_100.png`
- **Path:** `experiments/stage_error_analysis/seed_100.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/seed_1234.png`
- **Path:** `experiments/stage_error_analysis/seed_1234.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/seed_42.png`
- **Path:** `experiments/stage_error_analysis/seed_42.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/stage_a_check.png`
- **Path:** `experiments/stage_error_analysis/stage_a_check.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/stage_by_stage_error_analysis.py`
- **Path:** `experiments/stage_error_analysis/stage_by_stage_error_analysis.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/test_enhanced_pipeline.py`
- **Path:** `experiments/stage_error_analysis/test_enhanced_pipeline.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/test_grad_step.py`
- **Path:** `experiments/stage_error_analysis/test_grad_step.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/test_gradient_integration.py`
- **Path:** `experiments/stage_error_analysis/test_gradient_integration.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/stage_error_analysis/test_seeds.py`
- **Path:** `experiments/stage_error_analysis/test_seeds.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_flat_red.png`
- **Path:** `experiments/synthetic_illumination/S01_flat_red.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_A.svg`
- **Path:** `experiments/synthetic_illumination/S01_method_A.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_A_rendered.png`
- **Path:** `experiments/synthetic_illumination/S01_method_A_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_B.svg`
- **Path:** `experiments/synthetic_illumination/S01_method_B.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_B_rendered.png`
- **Path:** `experiments/synthetic_illumination/S01_method_B_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_C.svg`
- **Path:** `experiments/synthetic_illumination/S01_method_C.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S01_method_C_rendered.png`
- **Path:** `experiments/synthetic_illumination/S01_method_C_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_A.svg`
- **Path:** `experiments/synthetic_illumination/S02_method_A.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_A_rendered.png`
- **Path:** `experiments/synthetic_illumination/S02_method_A_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_B.svg`
- **Path:** `experiments/synthetic_illumination/S02_method_B.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_B_rendered.png`
- **Path:** `experiments/synthetic_illumination/S02_method_B_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_C.svg`
- **Path:** `experiments/synthetic_illumination/S02_method_C.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_method_C_rendered.png`
- **Path:** `experiments/synthetic_illumination/S02_method_C_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S02_smooth_red_sphere.png`
- **Path:** `experiments/synthetic_illumination/S02_smooth_red_sphere.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_metallic_gold.png`
- **Path:** `experiments/synthetic_illumination/S03_metallic_gold.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_A.svg`
- **Path:** `experiments/synthetic_illumination/S03_method_A.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_A_rendered.png`
- **Path:** `experiments/synthetic_illumination/S03_method_A_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_B.svg`
- **Path:** `experiments/synthetic_illumination/S03_method_B.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_B_rendered.png`
- **Path:** `experiments/synthetic_illumination/S03_method_B_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_C.svg`
- **Path:** `experiments/synthetic_illumination/S03_method_C.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S03_method_C_rendered.png`
- **Path:** `experiments/synthetic_illumination/S03_method_C_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_A.svg`
- **Path:** `experiments/synthetic_illumination/S04_method_A.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_A_rendered.png`
- **Path:** `experiments/synthetic_illumination/S04_method_A_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_B.svg`
- **Path:** `experiments/synthetic_illumination/S04_method_B.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_B_rendered.png`
- **Path:** `experiments/synthetic_illumination/S04_method_B_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_C.svg`
- **Path:** `experiments/synthetic_illumination/S04_method_C.svg`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_method_C_rendered.png`
- **Path:** `experiments/synthetic_illumination/S04_method_C_rendered.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/S04_transparency.png`
- **Path:** `experiments/synthetic_illumination/S04_transparency.png`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/generate_and_benchmark_synthetic.py`
- **Path:** `experiments/synthetic_illumination/generate_and_benchmark_synthetic.py`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `experiments/synthetic_illumination/synthetic_benchmark_results.json`
- **Path:** `experiments/synthetic_illumination/synthetic_benchmark_results.json`
- **Type:** Version Experiment Configuration & Results
- **Purpose:** Experiment parameters, execution logs, and benchmark observations for version-01.
- **Contents summary:** Experiment configurations, execution logs, and objective telemetry records.
- **Why it exists:** Record reproducible experimentation history without fabrication.
- **Current status:** ACTIVE / EXPERIMENTAL_RECORD
- **Source of truth / authority:** Version version-01 experiment history.
- **Update trigger:** When experiments are configured or executed.
- **Related Files:** No
- **Related Files:** None currently identified.

### `files from owner to antigravity/A01_detailed_original_old_new_diff.png`
- **Path:** `files from owner to antigravity/A01_detailed_original_old_new_diff.png`
- **Type:** Version First-Party File
- **Purpose:** File files from owner to antigravity/A01_detailed_original_old_new_diff.png supporting version version-01.
- **Contents summary:** Supporting configuration, asset, or documentation.
- **Why it exists:** Maintain completeness of version-01.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 file.
- **Update trigger:** When file content changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `files from owner to antigravity/agd_v7_comparison_12.png`
- **Path:** `files from owner to antigravity/agd_v7_comparison_12.png`
- **Type:** Version First-Party File
- **Purpose:** File files from owner to antigravity/agd_v7_comparison_12.png supporting version version-01.
- **Contents summary:** Supporting configuration, asset, or documentation.
- **Why it exists:** Maintain completeness of version-01.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 file.
- **Update trigger:** When file content changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `files from owner to antigravity/all_12_independently_rerun_improved_code.png`
- **Path:** `files from owner to antigravity/all_12_independently_rerun_improved_code.png`
- **Type:** Version First-Party File
- **Purpose:** File files from owner to antigravity/all_12_independently_rerun_improved_code.png supporting version version-01.
- **Contents summary:** Supporting configuration, asset, or documentation.
- **Why it exists:** Maintain completeness of version-01.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 file.
- **Update trigger:** When file content changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `files from owner to antigravity/all_12_source_vs_svg.png`
- **Path:** `files from owner to antigravity/all_12_source_vs_svg.png`
- **Type:** Version First-Party File
- **Purpose:** File files from owner to antigravity/all_12_source_vs_svg.png supporting version version-01.
- **Contents summary:** Supporting configuration, asset, or documentation.
- **Why it exists:** Maintain completeness of version-01.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 file.
- **Update trigger:** When file content changes.
- **Related Files:** No
- **Related Files:** None currently identified.

### `src/geometry/bezier.py`
- **Path:** `src/geometry/bezier.py`
- **Type:** Version Core Source Code
- **Purpose:** Implementation source code for src/geometry/bezier.py in version-01.
- **Contents summary:** Classes, functions, algorithms, and domain logic for this architectural approach.
- **Why it exists:** Execute the specific architectural hypothesis of version-01.
- **Current status:** ACTIVE / EXPERIMENTAL
- **Source of truth / authority:** Version version-01 source implementation.
- **Update trigger:** When implementation logic is updated.
- **Related Files:** Yes
#### `docs/CODE_MIRRORS/src/geometry/bezier.py.md`
- **Relationship:** 1:1 Version Codebase Markdown Mirror documenting functions and line numbers
- **Direction:** `src/geometry/bezier.py -> docs/CODE_MIRRORS/src/geometry/bezier.py.md`
- **Change impact:** Run `python3 tools/memory_guard/sync_code_mirrors.py --version version-01 --write` when this file changes.
- **Evidence:** Version AST extraction via sync_code_mirrors.py
#### `docs/FUNCTION_REGISTRY.md`
- **Relationship:** Registers all functions and exact lines in the version function registry
- **Direction:** `src/geometry/bezier.py -> docs/FUNCTION_REGISTRY.md`
- **Change impact:** Update version registry on code change.
- **Evidence:** Version function registry index

### `src/pipeline.py`
- **Path:** `src/pipeline.py`
- **Type:** Version Core Source Code
- **Purpose:** Implementation source code for src/pipeline.py in version-01.
- **Contents summary:** Classes, functions, algorithms, and domain logic for this architectural approach.
- **Why it exists:** Execute the specific architectural hypothesis of version-01.
- **Current status:** ACTIVE / EXPERIMENTAL
- **Source of truth / authority:** Version version-01 source implementation.
- **Update trigger:** When implementation logic is updated.
- **Related Files:** Yes
#### `docs/CODE_MIRRORS/src/pipeline.py.md`
- **Relationship:** 1:1 Version Codebase Markdown Mirror documenting functions and line numbers
- **Direction:** `src/pipeline.py -> docs/CODE_MIRRORS/src/pipeline.py.md`
- **Change impact:** Run `python3 tools/memory_guard/sync_code_mirrors.py --version version-01 --write` when this file changes.
- **Evidence:** Version AST extraction via sync_code_mirrors.py
#### `docs/FUNCTION_REGISTRY.md`
- **Relationship:** Registers all functions and exact lines in the version function registry
- **Direction:** `src/pipeline.py -> docs/FUNCTION_REGISTRY.md`
- **Change impact:** Update version registry on code change.
- **Evidence:** Version function registry index
#### `tests/test_version.py`
- **Relationship:** Tests version pipeline implementation
- **Direction:** `tests/test_version.py -> src/pipeline.py`
- **Change impact:** Run test suite when pipeline logic changes.
- **Evidence:** Version test import

### `tests/test_version.py`
- **Path:** `tests/test_version.py`
- **Type:** Version Test Suite
- **Purpose:** Unit, integration, and verification tests for version-01.
- **Contents summary:** Test cases validating functionality, performance, and invariants for this version.
- **Why it exists:** Ensure rigorous automated testing of version-01.
- **Current status:** ACTIVE
- **Source of truth / authority:** Version version-01 test specification.
- **Update trigger:** When features or test scenarios for this version change.
- **Related Files:** Yes
#### `src/pipeline.py`
- **Relationship:** Tests version pipeline implementation
- **Direction:** `tests/test_version.py -> src/pipeline.py`
- **Change impact:** Run test suite when pipeline logic changes.
- **Evidence:** Version test import
