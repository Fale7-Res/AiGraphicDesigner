# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `16`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `33`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `1`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `execute_cap_only` | `function` | `cap_control.py` | `Lines 8–16` | `def execute_cap_only(arm):` | رمز برمجي موثق. | [cap_control.py.md](code_mirrors/cap_control.py.md) |
| `topology_diagnostics` | `function` | `evaluate.py` | `Lines 18–46` | `def topology_diagnostics(items,raws):` | رمز برمجي موثق. | [evaluate.py.md](code_mirrors/evaluate.py.md) |
| `references` | `function` | `evaluate.py` | `Lines 48–63` | `def references(case,source):` | رمز برمجي موثق. | [evaluate.py.md](code_mirrors/evaluate.py.md) |
| `micro_diagnostics` | `function` | `evaluate.py` | `Lines 65–71` | `def micro_diagnostics(items):` | رمز برمجي موثق. | [evaluate.py.md](code_mirrors/evaluate.py.md) |
| `evaluate_arm` | `function` | `evaluate.py` | `Lines 73–136` | `def evaluate_arm(case,arm):` | رمز برمجي موثق. | [evaluate.py.md](code_mirrors/evaluate.py.md) |
| `supervise` | `function` | `monitor.py` | `Lines 6–36` | `def supervise(args,log,wall_seconds=300,memory_mib=768,reserve_mib=700,interval=.1):` | رمز برمجي موثق. | [monitor.py.md](code_mirrors/monitor.py.md) |
| `signed_area` | `function` | `partition_fit.py` | `Lines 21–23` | `def signed_area(points):` | رمز برمجي موثق. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `flattened` | `function` | `partition_fit.py` | `Lines 26–27` | `def flattened(curves):` | رمز برمجي موثق. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `source_partitions` | `function` | `partition_fit.py` | `Lines 30–62` | `def source_partitions(points):` | Source-index cuts preserve anchors, with disjoint edge intervals [lo, hi). | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `periodic_handles` | `function` | `partition_fit.py` | `Lines 65–94` | `def periodic_handles(points, intervals, candidates, corners):` | Closed raw loop: match directional tangents at smooth partition junctions. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `construct` | `function` | `partition_fit.py` | `Lines 97–180` | `def construct(points, condition="Q", deadline=None, maximum_trace_cubics=TRACE_CUBICS):` | Return accepted chains + exhaustive original-edge ledger for one trace. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `construct.rejected_all` | `nested_function` | `partition_fit.py` | `Lines 108–109` | `def rejected_all(reason):` | رمز برمجي موثق. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `fit_trace` | `function` | `partition_fit.py` | `Lines 183–185` | `def fit_trace(points, periodic=False, deadline=None, maximum_trace_cubics=TRACE_CUBICS):` | Caller-facing alias: periodic False=P and True=Q; no case/image inputs. | [partition_fit.py.md](code_mirrors/partition_fit.py.md) |
| `Links` | `class` | `qa/audit_final_links.py` | `Lines 20–24` | `class Links(HTMLParser):` | رمز برمجي موثق. | [qa__audit_final_links.py.md](code_mirrors/qa__audit_final_links.py.md) |
| `Links.__init__` | `method` | `qa/audit_final_links.py` | `Lines 21–21` | `def __init__(self):super().__init__();self.items=[]` | رمز برمجي موثق. | [qa__audit_final_links.py.md](code_mirrors/qa__audit_final_links.py.md) |
| `Links.handle_starttag` | `method` | `qa/audit_final_links.py` | `Lines 22–24` | `def handle_starttag(self,tag,attrs):` | رمز برمجي موثق. | [qa__audit_final_links.py.md](code_mirrors/qa__audit_final_links.py.md) |
| `dashboard` | `function` | `review.py` | `Lines 6–42` | `def dashboard(target,include_local):` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `dashboard.image` | `nested_function` | `review.py` | `Lines 9–9` | `def image(p,title):return '<figure><a href="'+html.escape(link(p))+'"><img loading="lazy" src="'+html.escape(link(p))+'"></a><figcaption>'+html.escape(title)+'</figcaption></figure>'` | رمز برمجي موثق. | [review.py.md](code_mirrors/review.py.md) |
| `destination` | `function` | `run_case.py` | `Lines 18–18` | `def destination(case,arm):return (W/'contour_construction/local_only'/case if case=='fine_features' else E/'results'/case)/arm` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `veto_chain` | `function` | `run_case.py` | `Lines 20–24` | `def veto_chain(result,chain,reason):` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `construct_condition` | `function` | `run_case.py` | `Lines 26–71` | `def construct_condition(frozen,condition,deadline):` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `execute` | `function` | `run_case.py` | `Lines 73–86` | `def execute(case,arm):` | رمز برمجي موثق. | [run_case.py.md](code_mirrors/run_case.py.md) |
| `PartitionFitTests` | `class` | `test_partition_fit.py` | `Lines 9–67` | `class PartitionFitTests(unittest.TestCase):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.assert_accounted` | `method` | `test_partition_fit.py` | `Lines 10–14` | `def assert_accounted(self,p,result):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_circle_periodic_closed` | `method` | `test_partition_fit.py` | `Lines 16–24` | `def test_circle_periodic_closed(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_square_sharp_corners` | `method` | `test_partition_fit.py` | `Lines 26–30` | `def test_square_sharp_corners(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_long_contour_no_lost_edges` | `method` | `test_partition_fit.py` | `Lines 32–37` | `def test_long_contour_no_lost_edges(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_open_junction_endpoints_and_same_conditions` | `method` | `test_partition_fit.py` | `Lines 39–42` | `def test_open_junction_endpoints_and_same_conditions(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_nested_loop_winding` | `method` | `test_partition_fit.py` | `Lines 44–47` | `def test_nested_loop_winding(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_budget_rejection_is_explicit` | `method` | `test_partition_fit.py` | `Lines 49–53` | `def test_budget_rejection_is_explicit(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_deadline_ledger` | `method` | `test_partition_fit.py` | `Lines 55–58` | `def test_deadline_ledger(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_short_trace_and_duplicate_explicit` | `method` | `test_partition_fit.py` | `Lines 60–62` | `def test_short_trace_and_duplicate_explicit(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
| `PartitionFitTests.test_two_source_junction_traces_keep_same_endpoint` | `method` | `test_partition_fit.py` | `Lines 64–67` | `def test_two_source_junction_traces_keep_same_endpoint(self):` | رمز برمجي موثق. | [test_partition_fit.py.md](code_mirrors/test_partition_fit.py.md) |
