# مرآة الكود التفصيلية: `scoped_governance.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `scoped_governance.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `scoped_governance.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `70` (`Lines 1–70`)
- **بصمة الملف (`SHA-256`):** `ae20cac156c6fce086fb843da02c3dae5e5dbb275773a60e5fe971cf9dd62f50`
- **الوصف التفصيلي:** """Reuse existing governance tools with explicitly isolated experiment paths.

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `load_scoped_tool` | `function` | `Lines 14–20` | `def load_scoped_tool(relative: str):` | Load historical governance implementation with isolated output constants. |
| `sync_scoped_mirrors` | `function` | `Lines 22–42` | `def sync_scoped_mirrors() -> dict:` | Generate existing AST/line-number mirrors without touching root memory. |
| `track_scoped_documents` | `function` | `Lines 44–63` | `def track_scoped_documents() -> dict:` | Register new/changed mutable experiment docs using existing provenance CLI. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `load_scoped_tool` — `Lines 14–20`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `20` (`Lines 14–20`)
- **الوظيفة:** Load historical governance implementation with isolated output constants.
- **الكود الفعلي (`Lines 14–20`):**
```python
def load_scoped_tool(relative: str):
    """Load historical governance implementation with isolated output constants."""
    path=HISTORY/relative
    spec=importlib.util.spec_from_file_location('isolated_'+path.stem,path)
    tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)
    tool.ROOT=ROOT
    return tool
```

### `sync_scoped_mirrors` — `Lines 22–42`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `22` إلى السطر `42` (`Lines 22–42`)
- **الوظيفة:** Generate existing AST/line-number mirrors without touching root memory.
- **الكود الفعلي (`Lines 22–42`):**
```python
def sync_scoped_mirrors() -> dict:
    """Generate existing AST/line-number mirrors without touching root memory."""
    tool=load_scoped_tool('memory_guard/sync_code_mirrors.py')
    tool.MIRRORS_DIR=ROOT/'memory'/'code_mirrors'
    tool.REGISTRY_PATH=ROOT/'memory'/'FUNCTION_REGISTRY.md'
    tool.METADATA_PATH=ROOT/'memory'/'mirror_metadata.json'
    files={}
    for path in sorted(ROOT.glob('*.py')):
        files[path.name]={'role':'Isolated Windows fidelity validation experiment',
          'summary':path.read_text(encoding='utf-8').splitlines()[0],
          'takes_from':[{'source':'historical adaptive optimizer and fidelity evaluator',
                        'payload':'source images, candidate configurations, metric arrays',
                        'impact':'preserve baseline behavior; native execution only'}],
          'throws_to':[{'target':'isolated experiment reports and SVG/render trial directories',
                       'payload':'generated vectors, PNGs, metrics, process measurements',
                       'impact':'research evidence only; architecture NOT_APPROVED'}]}
    tool.MIRRORS_DIR.mkdir(parents=True,exist_ok=True)
    tool.METADATA_PATH.write_text(json.dumps({'files':files},indent=2),encoding='utf-8')
    result=tool.sync_root(write_mode=True)
    if result['duplicate_functions_found']: raise RuntimeError(result)
    return result
```

### `track_scoped_documents` — `Lines 44–63`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `44` إلى السطر `63` (`Lines 44–63`)
- **الوظيفة:** Register new/changed mutable experiment docs using existing provenance CLI.
- **الكود الفعلي (`Lines 44–63`):**
```python
def track_scoped_documents() -> dict:
    """Register new/changed mutable experiment docs using existing provenance CLI."""
    tool=load_scoped_tool('governance/change_tracking.py')
    tool.MANIFEST=ROOT/'memory'/'DOCUMENT_PROVENANCE.json'
    tool.MANIFEST.parent.mkdir(parents=True,exist_ok=True)
    record=tool.load_manifest()
    for path,relative in tool.iter_files():
        if not tool.governed_doc(relative): continue
        old=record['documents'].get(relative)
        content=path.read_text(encoding='utf-8')
        if old and tool.sha(content)==old['sha256']: continue
        tool.edit_document(relative,'EDITED' if old else 'CREATED',
                           'AGD-CODEX-WIN-PORT','root')
    errors=tool.verify()
    result={'status':'PASS' if not errors else 'FAIL','errors':errors,
            # START CHANGE AGD-CODEX-WIN-GOV-SCOPE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
            'scope':str(ROOT),'intended_historical_write_scope':'none; checked separately against Git baseline'}
    # END CHANGE AGD-CODEX-WIN-GOV-SCOPE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
    if errors: raise RuntimeError(result)
    return result
```
