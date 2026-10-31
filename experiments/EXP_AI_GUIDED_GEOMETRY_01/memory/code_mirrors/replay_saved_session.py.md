# مرآة الكود التفصيلية: `replay_saved_session.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `replay_saved_session.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `replay_saved_session.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `16` (`Lines 1–16`)
- **بصمة الملف (`SHA-256`):** `e9d0ccc178dde241355ccf04cb24dd448364464d4469af11d2ce9cadc1ded2e0`
- **الوصف التفصيلي:** # START CHANGE AGD-AGENTIC-REPLAY | 2026-10-31T15:16:13Z | EDITED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `replay_saved` | `function` | `Lines 9–14` | `def replay_saved():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `replay_saved` — `Lines 9–14`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `9` إلى السطر `14` (`Lines 9–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 9–14`):**
```python
def replay_saved():
 protocol=json.loads((E/'protocol.json').read_text());parser=argparse.ArgumentParser();parser.add_argument('--case',choices=list(protocol['cases']),default='K01_linear_corner_hole');parser.add_argument('--condition',choices=['B','M'],default='M');args=parser.parse_args()
 saved=E/'results'/args.case;output=W/'agentic_geometry/owner_replay'/args.case/args.condition
 rgb=np.asarray(Image.open(saved/'source.png').convert('RGB'));traces=json.loads((saved/'frozen_traces.json').read_text())['traces'];initial=json.loads((saved/'A.json').read_text())['accepted'];expected=json.loads((saved/(args.condition+'.json')).read_text());engine=GeometryToolEngine(rgb,traces,initial,output,R,W)
 for event in expected['tool_events']:engine.dispatch(event['tool'],event['arguments'])
 assert engine.state_hash()==expected['state_hash'];assert engine.replay_decision_hash()==expected['decision_hash'];result=dict(replay_passed=True,geometry_hash=engine.state_hash(),decision_hash=engine.replay_decision_hash(),events=len(engine.events),AI_performance='NOT_TESTED');(output/'REPLAY_RESULT.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
```
