# السجل الموحد للدوال والكلاسات للإصدار `version-04-claude-challenger` (`FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار الخاصة بالإصدار (`Version Source Authority & Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي يمنع وجود دالتين بنفس الاسم عبر ملفات الإصدار `version-04-claude-challenger`.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية المتطابقة داخل الإصدار.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** تدقيق مهندس الإصدار والمراجع المستقل لمنع إعادة اختراع الوظائف المتاحة.

- **معرف الإصدار المعماري (`Version ID`):** `version-04-claude-challenger`
- **إجمالي الملفات البرمجية المفحوصة في الإصدار:** `7`
- **إجمالي الرموز المسجلة بالسطر:** `51`
- **عدد الدوال المتطابقة الاسم غير المسموحة:** `0`
- **مرشحات التشابه الهيكلي:** `1`

## جدول جميع الدوال والكلاسات والرموز في الإصدار (`Version Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `Config` | `class` | `src/challenger.py` | `Lines 22–28` | `class Config:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `Leaf` | `class` | `src/challenger.py` | `Lines 32–52` | `class Leaf:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `Leaf.width` | `method` | `src/challenger.py` | `Lines 47–48` | `def width(self) -> int:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `Leaf.height` | `method` | `src/challenger.py` | `Lines 51–52` | `def height(self) -> int:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats` | `class` | `src/challenger.py` | `Lines 55–153` | `class IntegralStats:` | Rectangle color moments, enabling O(1) local regression statistics. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats.__init__` | `method` | `src/challenger.py` | `Lines 58–78` | `def __init__(self, rgb: np.ndarray):` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats.rect` | `method` | `src/challenger.py` | `Lines 81–82` | `def rect(integral: np.ndarray, x0: int, y0: int, x1: int, y1: int) -> float:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats.vector` | `method` | `src/challenger.py` | `Lines 84–85` | `def vector(self, bundle: list[np.ndarray], x0: int, y0: int, x1: int, y1: int) -> np.ndarray:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats.edge_mean` | `method` | `src/challenger.py` | `Lines 87–89` | `def edge_mean(self, x0: int, y0: int, x1: int, y1: int) -> float:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `IntegralStats.statistics` | `method` | `src/challenger.py` | `Lines 91–153` | `def statistics(self, x0: int, y0: int, x1: int, y1: int):` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface` | `class` | `src/challenger.py` | `Lines 156–304` | `class AdaptiveVectorSurface:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface.__init__` | `method` | `src/challenger.py` | `Lines 157–160` | `def __init__(self, config: Config | None = None):` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface._hex` | `method` | `src/challenger.py` | `Lines 163–164` | `def _hex(rgb: tuple[int, int, int]) -> str:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface._node` | `method` | `src/challenger.py` | `Lines 166–170` | `def _node(self, x0: int, y0: int, x1: int, y1: int) -> Leaf:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface._split` | `method` | `src/challenger.py` | `Lines 172–185` | `def _split(self, node: Leaf) -> list[Leaf]:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface.vectorize` | `method` | `src/challenger.py` | `Lines 187–304` | `def vectorize(self, image: str | Path | np.ndarray) -> tuple[str, dict]:` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `AdaptiveVectorSurface.vectorize.enqueue` | `nested_function` | `src/challenger.py` | `Lines 214–224` | `def enqueue(node: Leaf):` | رمز برمجي موثق للإصدار. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `rasterize_svg` | `function` | `src/challenger.py` | `Lines 307–323` | `def rasterize_svg(svg_path: str | Path, png_path: str | Path, width: int, height: int,` | Rasterize with local Inkscape CLI; returns render wall time in milliseconds. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `add_edge_residual_layer` | `function` | `src/challenger.py` | `Lines 326–402` | `def add_edge_residual_layer(svg: str, image: str | Path | np.ndarray, dilation: int = 1,` | Add an edge-band appearance correction as SVG vector subregions. | [src/challenger.py.md](CODE_MIRRORS/src/challenger.py.md) |
| `Sampler` | `class` | `src/finalize_metrics.py` | `Lines 18–33` | `class Sampler:` | Sample this Python process RSS every 10ms; not a system-wide peak. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `Sampler.__init__` | `method` | `src/finalize_metrics.py` | `Lines 20–21` | `def __init__(self):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `Sampler._loop` | `method` | `src/finalize_metrics.py` | `Lines 22–26` | `def _loop(self):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `Sampler.__enter__` | `method` | `src/finalize_metrics.py` | `Lines 27–29` | `def __enter__(self):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `Sampler.__exit__` | `method` | `src/finalize_metrics.py` | `Lines 30–33` | `def __exit__(self, *args):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `mean` | `function` | `src/finalize_metrics.py` | `Lines 36–38` | `def mean(rows, key):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `write_report` | `function` | `src/finalize_metrics.py` | `Lines 41–107` | `def write_report(rows, summary):` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `save_progress` | `function` | `src/finalize_metrics.py` | `Lines 110–116` | `def save_progress(rows):` | Durable per-image checkpoint so one slow SVG does not lose completed work. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `main` | `function` | `src/finalize_metrics.py` | `Lines 119–243` | `def main():` | رمز برمجي موثق للإصدار. | [src/finalize_metrics.py.md](CODE_MIRRORS/src/finalize_metrics.py.md) |
| `main` | `function` | `src/measure_renders.py` | `Lines 13–38` | `def main():` | رمز برمجي موثق للإصدار. | [src/measure_renders.py.md](CODE_MIRRORS/src/measure_renders.py.md) |
| `PeakRssSampler` | `class` | `src/run_benchmark.py` | `Lines 33–57` | `class PeakRssSampler:` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `PeakRssSampler.__init__` | `method` | `src/run_benchmark.py` | `Lines 34–39` | `def __init__(self, interval=0.005):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `PeakRssSampler._run` | `method` | `src/run_benchmark.py` | `Lines 40–46` | `def _run(self):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `PeakRssSampler.__enter__` | `method` | `src/run_benchmark.py` | `Lines 47–50` | `def __enter__(self):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `PeakRssSampler.__exit__` | `method` | `src/run_benchmark.py` | `Lines 51–55` | `def __exit__(self, *args):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `PeakRssSampler.mb` | `method` | `src/run_benchmark.py` | `Lines 57–57` | `def mb(self): return self.peak / (1024 * 1024)` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `load_rgb` | `function` | `src/run_benchmark.py` | `Lines 60–61` | `def load_rgb(path: Path) -> np.ndarray:` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `svg_structure` | `function` | `src/run_benchmark.py` | `Lines 64–92` | `def svg_structure(path: Path) -> dict:` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `_edge_metrics` | `function` | `src/run_benchmark.py` | `Lines 95–125` | `def _edge_metrics(ref: np.ndarray, pred: np.ndarray) -> dict:` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `compare` | `function` | `src/run_benchmark.py` | `Lines 128–137` | `def compare(ref: np.ndarray, rendered: np.ndarray) -> dict:` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `render_font` | `function` | `src/run_benchmark.py` | `Lines 140–142` | `def render_font(size=18):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `make_comparison` | `function` | `src/run_benchmark.py` | `Lines 145–159` | `def make_comparison(stem: str, source_path: Path, v01_path: Path, v04_path: Path, target: Path):` | رمز برمجي موثق للإصدار. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `make_contact_sheet` | `function` | `src/run_benchmark.py` | `Lines 162–185` | `def make_contact_sheet(records: list[dict], target: Path):` | Contact sheet with non-overlapping image IDs and panel labels. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `main` | `function` | `src/run_benchmark.py` | `Lines 187–219` | `def main():` | Reproducible entry point for A01 budget sweep and final 12-image run. | [src/run_benchmark.py.md](CODE_MIRRORS/src/run_benchmark.py.md) |
| `make_synthetic` | `function` | `src/run_synthetic.py` | `Lines 19–70` | `def make_synthetic(width=320, height=240, scale=3):` | رمز برمجي موثق للإصدار. | [src/run_synthetic.py.md](CODE_MIRRORS/src/run_synthetic.py.md) |
| `main` | `function` | `src/run_synthetic.py` | `Lines 73–108` | `def main():` | رمز برمجي موثق للإصدار. | [src/run_synthetic.py.md](CODE_MIRRORS/src/run_synthetic.py.md) |
| `main` | `function` | `src/verify_outputs.py` | `Lines 11–53` | `def main():` | رمز برمجي موثق للإصدار. | [src/verify_outputs.py.md](CODE_MIRRORS/src/verify_outputs.py.md) |
| `ChallengerTests` | `class` | `tests/test_challenger.py` | `Lines 16–58` | `class ChallengerTests(unittest.TestCase):` | رمز برمجي موثق للإصدار. | [tests/test_challenger.py.md](CODE_MIRRORS/tests/test_challenger.py.md) |
| `ChallengerTests.test_surface_output_stays_within_leaf_budget_and_contains_no_raster` | `method` | `tests/test_challenger.py` | `Lines 17–26` | `def test_surface_output_stays_within_leaf_budget_and_contains_no_raster(self):` | رمز برمجي موثق للإصدار. | [tests/test_challenger.py.md](CODE_MIRRORS/tests/test_challenger.py.md) |
| `ChallengerTests.test_constant_image_is_valid_svg_and_has_no_gradient_need` | `method` | `tests/test_challenger.py` | `Lines 28–34` | `def test_constant_image_is_valid_svg_and_has_no_gradient_need(self):` | رمز برمجي موثق للإصدار. | [tests/test_challenger.py.md](CODE_MIRRORS/tests/test_challenger.py.md) |
| `ChallengerTests.test_edge_residual_is_explicit_vector_hybrid` | `method` | `tests/test_challenger.py` | `Lines 36–48` | `def test_edge_residual_is_explicit_vector_hybrid(self):` | رمز برمجي موثق للإصدار. | [tests/test_challenger.py.md](CODE_MIRRORS/tests/test_challenger.py.md) |
| `ChallengerTests.test_edge_residual_is_deterministic` | `method` | `tests/test_challenger.py` | `Lines 50–58` | `def test_edge_residual_is_deterministic(self):` | رمز برمجي موثق للإصدار. | [tests/test_challenger.py.md](CODE_MIRRORS/tests/test_challenger.py.md) |
