# مرآة الكود التفصيلية: `run_alpha_validation.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_alpha_validation.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_alpha_validation.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `45` (`Lines 1–45`)
- **بصمة الملف (`SHA-256`):** `098cef2f908845972674afcfc6130ea2625a0e9f2bd2567508761ac5e211bba7`
- **الوصف التفصيلي:** """Bounded sequential native alpha comparison, gated on completed baseline search."""

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_alpha_comparison` | `function` | `Lines 10–39` | `def run_alpha_comparison(renderer_exe: Path,baseline_ranking: Path) -> dict:` | Compare explicit-white inherited policy to vector-mask alpha experiment. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_alpha_comparison` — `Lines 10–39`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `10` إلى السطر `39` (`Lines 10–39`)
- **الوظيفة:** Compare explicit-white inherited policy to vector-mask alpha experiment.
- **الكود الفعلي (`Lines 10–39`):**
```python
def run_alpha_comparison(renderer_exe: Path,baseline_ranking: Path) -> dict:
    """Compare explicit-white inherited policy to vector-mask alpha experiment."""
    ranking=json.loads(Path(baseline_ranking).read_text(encoding='utf-8'))
    if not ranking.get('ranked') or ranking.get('evaluated_candidates',0)<13:
        raise RuntimeError('A completed successful inherited baseline search is required first')
    if not Path(renderer_exe).is_file(): raise FileNotFoundError(renderer_exe)
    os.environ['AGD_RENDERER']='resvg';os.environ['AGD_RENDERER_EXE']=str(Path(renderer_exe).resolve())
    from optimizer import optimize
    from alpha_optimizer import optimize_alpha, evaluate_alpha
    source=ROOT/'inputs'/'N02_local_soft_alpha.png'
    white=ROOT/'results'/'N02_white_baseline';alpha=ROOT/'results'/'N02_alpha_preserve'
    print('N02: inherited explicit-white search, 13 candidates',flush=True)
    white_rank=optimize(source,white,13,720.,'white')
    if not white_rank['ranked']: raise RuntimeError('White baseline produced no successful candidate')
    print('N02: unassociated RGB search + vector alpha, 13 candidates',flush=True)
    alpha_report=optimize_alpha(source,alpha,13,720.)
    if 'evaluation' not in alpha_report: raise RuntimeError('Alpha prototype produced no successful candidate')
    white_eval=evaluate_alpha(alpha/'input'/'reference_srgb_rgba.png',white/'best.svg',white/'alpha_evaluation')
    improved=alpha_report['evaluation']
    report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'source':str(source),
            'completed_baseline_ranking':str(Path(baseline_ranking).resolve()),
            'protocol':'Sequential 13 candidates each; explicit inherited white baseline versus unassociated RGB + vector mask. Post-selection alpha and three-background metrics; resvg differs from historical Inkscape.',
            'white_baseline':white_eval,'alpha_preserve':improved,
            'alpha_mae_reduction':white_eval['alpha_mae_0_255']-improved['alpha_mae_0_255'],
            'mean_background_score_increase':improved['mean_background_fidelity_score']-white_eval['mean_background_fidelity_score'],
            'white_candidates':white_rank['evaluated_candidates'],'alpha_candidates':alpha_report['rgb_search_candidates'],
            'architecture_status':'NOT_APPROVED','owner_acceptance':'NOT_REQUESTED_BY_SCRIPT'}
    (ROOT/'reports'/'alpha_comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False),encoding='utf-8')
    print(json.dumps({key:report[key] for key in ('alpha_mae_reduction','mean_background_score_increase','white_candidates','alpha_candidates')},indent=2),flush=True)
    return report
```
