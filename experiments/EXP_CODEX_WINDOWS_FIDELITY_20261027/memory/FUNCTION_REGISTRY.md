# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `10`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `30`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `0`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `prepare_transparent_input` | `function` | `alpha_optimizer.py` | `Lines 26–48` | `def prepare_transparent_input(source: Path,folder: Path,max_pixels: int=1048576) -> dict:` | Retain unassociated RGB and alpha; convert declared ICC to sRGB once. | [alpha_optimizer.py.md](code_mirrors/alpha_optimizer.py.md) |
| `apply_vector_alpha` | `function` | `alpha_optimizer.py` | `Lines 52–93` | `def apply_vector_alpha(rgb_svg: Path,alpha_png: Path,destination: Path) -> dict:` | Attach alpha run paths at native integer pixel coordinates; no raster tags. | [alpha_optimizer.py.md](code_mirrors/alpha_optimizer.py.md) |
| `evaluate_alpha` | `function` | `alpha_optimizer.py` | `Lines 97–118` | `def evaluate_alpha(reference_rgba: Path,svg: Path,folder: Path) -> dict:` | Measure native alpha and visible fidelity on white, black, and blue-gray. | [alpha_optimizer.py.md](code_mirrors/alpha_optimizer.py.md) |
| `optimize_alpha` | `function` | `alpha_optimizer.py` | `Lines 122–137` | `def optimize_alpha(source: Path,output: Path,max_candidates: int=13,max_seconds: float=720.) -> dict:` | Run inherited opaque RGB search, then experimentally preserve source alpha. | [alpha_optimizer.py.md](code_mirrors/alpha_optimizer.py.md) |
| `canonical` | `function` | `optimizer.py` | `Lines 16–29` | `def canonical(c):` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `pilots` | `function` | `optimizer.py` | `Lines 31–42` | `def pilots():` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `neighborhood` | `function` | `optimizer.py` | `Lines 44–51` | `def neighborhood(c):` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `optimize` | `function` | `optimizer.py` | `Lines 53–98` | `def optimize(source,output,max_candidates=24,max_seconds=720,alpha_policy='reject'):` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `optimize.budget` | `nested_function` | `optimizer.py` | `Lines 66–66` | `def budget():return len(rows)>=max_candidates or time.monotonic()-start>=max_seconds` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `optimize.trial` | `nested_function` | `optimizer.py` | `Lines 67–72` | `def trial(c,phase):` | رمز برمجي موثق. | [optimizer.py.md](code_mirrors/optimizer.py.md) |
| `run_alpha_comparison` | `function` | `run_alpha_validation.py` | `Lines 10–39` | `def run_alpha_comparison(renderer_exe: Path,baseline_ranking: Path) -> dict:` | Compare explicit-white inherited policy to vector-mask alpha experiment. | [run_alpha_validation.py.md](code_mirrors/run_alpha_validation.py.md) |
| `run_tests` | `function` | `run_inherited_tests.py` | `Lines 16–35` | `def run_tests() -> bool:` | Load exact historical bytes, keeping unittest patch target optimizer local. | [run_inherited_tests.py.md](code_mirrors/run_inherited_tests.py.md) |
| `load_scoped_tool` | `function` | `scoped_governance.py` | `Lines 14–20` | `def load_scoped_tool(relative: str):` | Load historical governance implementation with isolated output constants. | [scoped_governance.py.md](code_mirrors/scoped_governance.py.md) |
| `sync_scoped_mirrors` | `function` | `scoped_governance.py` | `Lines 22–42` | `def sync_scoped_mirrors() -> dict:` | Generate existing AST/line-number mirrors without touching root memory. | [scoped_governance.py.md](code_mirrors/scoped_governance.py.md) |
| `track_scoped_documents` | `function` | `scoped_governance.py` | `Lines 44–63` | `def track_scoped_documents() -> dict:` | Register new/changed mutable experiment docs using existing provenance CLI. | [scoped_governance.py.md](code_mirrors/scoped_governance.py.md) |
| `audit_saved_metrics` | `function` | `validate_local.py` | `Lines 12–26` | `def audit_saved_metrics():` | Recompute twelve selected saved renders; this is not retracing twelve images. | [validate_local.py.md](code_mirrors/validate_local.py.md) |
| `audit_local_case` | `function` | `validate_local.py` | `Lines 28–69` | `def audit_local_case(name,repeat=False):` | Check every candidate and winner, recompute metrics, optionally retrace winner. | [validate_local.py.md](code_mirrors/validate_local.py.md) |
| `verify_alpha_runs` | `function` | `verify_alpha_geometry.py` | `Lines 13–43` | `def verify_alpha_runs() -> dict:` | Reconstruct all 256 alpha levels and boundary cases from serialized paths. | [verify_alpha_geometry.py.md](code_mirrors/verify_alpha_geometry.py.md) |
| `verify_sources` | `function` | `verify_portability.py` | `Lines 13–40` | `def verify_sources() -> dict:` | Compare selected derived function ASTs excluding docstrings only. | [verify_portability.py.md](code_mirrors/verify_portability.py.md) |
| `verify_sources.function_body` | `nested_function` | `verify_portability.py` | `Lines 21–25` | `def function_body(key: str,name: str) -> str:` | رمز برمجي موثق. | [verify_portability.py.md](code_mirrors/verify_portability.py.md) |
| `verify_timeout` | `function` | `verify_portability.py` | `Lines 42–55` | `def verify_timeout() -> dict:` | Run an actual child+grandchild and verify whole observed tree exits. | [verify_portability.py.md](code_mirrors/verify_portability.py.md) |
| `verify_trial_history_guard` | `function` | `verify_portability.py` | `Lines 58–69` | `def verify_trial_history_guard() -> dict:` | Ensure trial replay cannot overwrite even an arbitrary prior sentinel. | [verify_portability.py.md](code_mirrors/verify_portability.py.md) |
| `prepare_input` | `function` | `windows_search.py` | `Lines 21–34` | `def prepare_input(source,destination):` | Historical derived copy: ICC to sRGB and explicitly composite on white. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `extra_metrics` | `function` | `windows_search.py` | `Lines 36–41` | `def extra_metrics(source,pred):` | Historical derived copy: unchanged color and high-frequency diagnostics. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `fidelity_score` | `function` | `windows_search.py` | `Lines 43–50` | `def fidelity_score(metrics):` | Historical derived copy: fixed multi-metric score, no complexity penalty. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `terminate_tree` | `function` | `windows_search.py` | `Lines 54–63` | `def terminate_tree(process: psutil.Process, known: dict) -> None:` | Kill root and known descendants; wait for termination. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `supervise` | `function` | `windows_search.py` | `Lines 65–108` | `def supervise(command: list[str], log: Path, timeout: float=180., memory_limit_mib: float=4096.) -> dict:` | Sample simultaneous tree RSS incl renderer. Peaks/CPU are sampling bounds. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `render_svg` | `function` | `windows_search.py` | `Lines 112–132` | `def render_svg(path: Path,png: Path,width: int,height: int) -> dict:` | Explicit renderer selection; never silently fall back from Inkscape. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `run_trial` | `function` | `windows_search.py` | `Lines 136–155` | `def run_trial(source: Path,folder: Path,config: dict) -> dict:` | Run isolated native worker; retain failed configs, logs, and measurements. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
| `worker` | `function` | `windows_search.py` | `Lines 157–172` | `def worker(source: Path,folder: Path) -> None:` | Generate real SVG; historical validation and metrics, native renderer. | [windows_search.py.md](code_mirrors/windows_search.py.md) |
