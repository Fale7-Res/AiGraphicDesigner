# مرآة الكود التفصيلية: `deliver.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `deliver.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `deliver.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `130` (`Lines 1–130`)
- **بصمة الملف (`SHA-256`):** `be224c1bbb72d18260f2c49990b64b7fcbc0aa8c3a46d20c41accf3d8ef85ad9`
- **الوصف التفصيلي:** # START CHANGE AGD-AGENTIC-DELIVER | 2026-10-31T15:16:13Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `review_page` | `function` | `Lines 104–128` | `def review_page(local):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `review_page` — `Lines 104–128`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `104` إلى السطر `128` (`Lines 104–128`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 104–128`):**
```python
def review_page(local):
 page=['<!doctype html><meta charset="utf-8"><title>Restricted geometry tools — offline evidence</title><style>body{font:16px system-ui;background:#eef2f5;color:#17242d;margin:24px}section{background:white;border-radius:12px;margin:20px 0;padding:20px}.grid{display:grid;grid-template-columns:repeat(4,minmax(200px,1fr));gap:12px}figure{margin:0}img{max-width:100%;background:white;border:1px solid #bcc}figcaption{font-weight:bold;padding:6px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:8px;border:1px solid #bbc}.warning{background:#ffe0dc;padding:16px}.note{background:#fff1c4;padding:14px}.zoom{overflow:auto;max-height:550px}.zoom img{max-width:none}details{margin:12px 0}a{color:#0753a2}</style><h1>Geometry tool-controller proof of concept</h1><p><b>Geometry NOT_ACCEPTED · Architecture NOT_APPROVED</b></p><p class="warning"><b>Real Groq inference: NOT_TESTED.</b> No API requests or image uploads. B is deterministic; M is a fixed mock, NOT AI. Current account free-tier, quota and billing state are unverified. No AI result is represented by these SVGs.</p><p>Actual seven-case A/B/M comparison. A=automatic P; B=full-frame tool controller; M=fixed top/bottom plan. Both use12calls/2commits, same tools. Tiny support gains do not complete crown, Burger, Arabic or regions. C remains unavailable until verified free-only access and image permission.</p>']
 for case in p['cases']:
  out=E/'results'/case;base=out.as_uri()+'/' if local else f'results/{case}/';page.append(f'<section id="{case}"><h2>{case}</h2><div class="grid">')
  a_caption='A automatic P (new holdout control)' if case=='H03_original_vector' else 'A saved automatic P'
  for title,name in [('Source raster','source.png'),(a_caption,'A_1x.png'),('B deterministic tools','B_1x.png'),('M FIXED MOCK — NOT AI','M_1x.png')]:page.append(f'<figure><img loading="lazy" src="{base+name}"><figcaption>{title}</figcaption></figure>')
  page.append('</div><p>Actual vector files: '+ ' · '.join(f'<a href="{base+c}.svg">{c} SVG</a>' for c in ['A','B','M'])+f' · <a href="{base}REPLAY.json">deterministic mock replay</a></p><p class="warning">C Groq-guided result: NOT_TESTED. No image shown as a substitute.</p>')
  page.append('<table><tr><th>Control</th><th>Paths/cubics</th><th>Source support proxy</th><th>Known/proxy recall</th><th>Atomic faces</th><th>Tiny cubic length fraction</th></tr>')
  for c in ['A','B','M']:
   m=look[(case,c)];t=m.get('boundary_1_25px',{}).get('recall');page.append(f'<tr><td>{c}</td><td>{m["paths"]}/{m["cubics"]}</td><td>{m["source_trace_support"]["recall"]:.4f}</td><td>{f"{t:.4f}" if t is not None else "No exact truth"}</td><td>{m["atomic_faces"]}</td><td>{m["micro"]["tiny_cubic_length_weighted_fraction"]:.4f}</td></tr>')
  page.append('</table><p class="note">Source trace support includes texture/reflections; it is not structural precision. Atomic faces are evaluator diagnostics, not reconstructed semantic objects. Arabic uses threshold proxies; Shield guides have1.2–2px uncertainty.</p>')
  if case=='A01_shield':page.append('<h3>Crown, ornament, tips and lower band</h3><p>Crown guide recall A0.3036 / B0.3082 / M0.3201. Central ornament and upper/lower band support are unchanged. Complete internal geometry still fails.</p>')
  for scale in [1,4,16]:
   page.append(f'<details><summary>True SVG-rendered detail {scale}×'+(' — crown' if case=='A01_shield' else '')+'</summary><div class="grid">')
   for c in ['A','B','M']:page.append(f'<figure><figcaption>{c}</figcaption><div class="zoom"><img loading="lazy" src="{base+c}_detail_{scale}x.png"></div><a href="{base+c}_detail.svg">Detail SVG</a></figure>')
   page.append('</div></details>')
  page.append('<details><summary>Missing frozen source evidence (magenta), not verified missing artwork</summary><div class="grid">'+''.join(f'<figure><figcaption>{c}</figcaption><img loading="lazy" src="{base+c}_missing_source_trace.png"></figure>' for c in ['A','B','M'])+'</div></details>')
  for c in ['B','M']:
   data=json.loads((out/(c+'.json')).read_text());page.append(f'<details><summary>{c} tool-call timeline — {data["calls"]} calls / {data["commits"]} commits; no model</summary><table><tr><th>#</th><th>Tool/arguments</th><th>Outcome</th><th>State changed</th><th>Immutable record</th></tr>')
   for ev in data['tool_events']:
    result=ev['result'];summary={k:result[k] for k in ['status','error','added_paths','paths','pending','geometry'] if k in result};page.append(f'<tr><td>{ev["sequence"]}</td><td>{html.escape(ev["tool"])} {html.escape(json.dumps(ev["arguments"]))}</td><td>{html.escape(json.dumps(summary))}</td><td>{ev["before_hash"]!=ev["after_hash"]}</td><td><a href="{base+c}/event_{ev["sequence"]:03d}.json">event JSON</a></td></tr>')
   page.append('</table></details>')
  page.append('</section>')
 page.append('<section><h2>Live gate / reproduction</h2><p>Selected provider Groq Cloud; requested model qwen/qwen3.8-27b verified in official docs. Account access/free billing/quota NOT_VERIFIED. The actual dry-run request and local contact sheet are preserved; generated second previews require explicit authorization. Zero live calls; AI value NOT_TESTED.</p><p>Burger first attempt hit available-RAM reserve and is preserved; same-budget retry completed. The main seven-case outputs include that disclosed retry. See report and resource records.</p><p>No secret, external private image, final appearance or arbitrary executable is exposed as a tool. Use the scoped publisher in the owner terminal; publication remains unverified until remote SHA matches.</p></section>')
 return ''.join(page)
```
