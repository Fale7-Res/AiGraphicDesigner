# مرآة الكود التفصيلية: `synthetic_session.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `synthetic_session.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `synthetic_session.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `41` (`Lines 1–41`)
- **بصمة الملف (`SHA-256`):** `e220e4ee4e63d17a9fe5880a66cadda358da3014d39e0b8efecf669a954ac309`
- **الوصف التفصيلي:** # START CHANGE AGD-PILOT-SYNTHETIC | 2026-10-31T16:16:43Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `SyntheticPlanner` | `class` | `Lines 12–18` | `class SyntheticPlanner:` | رمز برمجي موثق. |
| `SyntheticPlanner.__init__` | `method` | `Lines 14–14` | `def __init__(self,ids,index):self.ids=ids;self.index=index` | رمز برمجي موثق. |
| `SyntheticPlanner._prepare` | `method` | `Lines 15–15` | `def _prepare(self,messages,tools):return GroqAdapter(live=False)._prepare(messages,tools)` | رمز برمجي موثق. |
| `SyntheticPlanner.request` | `method` | `Lines 16–18` | `def request(self,*args):` | رمز برمجي موثق. |
| `run_fixture` | `function` | `Lines 21–34` | `def run_fixture(directory):` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `SyntheticPlanner` — `Lines 12–18`
- **النوع:** `class`
- **نطاق الأسطر الدقيق:** من السطر `12` إلى السطر `18` (`Lines 12–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 12–18`):**
```python
class SyntheticPlanner:
    live=False
    def __init__(self,ids,index):self.ids=ids;self.index=index
    def _prepare(self,messages,tools):return GroqAdapter(live=False)._prepare(messages,tools)
    def request(self,*args):
        obs=dict(missing_components=['Synthetic test observation: contour completeness is unverified'],roi=[0,0,1,1],uncertainty=.8,chosen_action='Test existing candidate transaction; not AI reasoning',unavailable_capabilities=['wholly new boundaries','accepted curve movement'],stop_reason='fixture complete' if self.index==1 else '')
        return dict(status='SYNTHETIC',message=dict(content=json.dumps(obs),tool_calls=[dict(id=f'synthetic_{self.index}',type='function',function=dict(name='stage_candidates',arguments=json.dumps(dict(trace_ids=self.ids))))]),usage=dict(prompt_tokens=100,completion_tokens=50,total_tokens=150))
```

### `SyntheticPlanner.__init__` — `Lines 14–14`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `14` إلى السطر `14` (`Lines 14–14`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 14–14`):**
```python
    def __init__(self,ids,index):self.ids=ids;self.index=index
```

### `SyntheticPlanner._prepare` — `Lines 15–15`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `15` إلى السطر `15` (`Lines 15–15`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 15–15`):**
```python
    def _prepare(self,messages,tools):return GroqAdapter(live=False)._prepare(messages,tools)
```

### `SyntheticPlanner.request` — `Lines 16–18`
- **النوع:** `method`
- **نطاق الأسطر الدقيق:** من السطر `16` إلى السطر `18` (`Lines 16–18`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 16–18`):**
```python
    def request(self,*args):
        obs=dict(missing_components=['Synthetic test observation: contour completeness is unverified'],roi=[0,0,1,1],uncertainty=.8,chosen_action='Test existing candidate transaction; not AI reasoning',unavailable_capabilities=['wholly new boundaries','accepted curve movement'],stop_reason='fixture complete' if self.index==1 else '')
        return dict(status='SYNTHETIC',message=dict(content=json.dumps(obs),tool_calls=[dict(id=f'synthetic_{self.index}',type='function',function=dict(name='stage_candidates',arguments=json.dumps(dict(trace_ids=self.ids))))]),usage=dict(prompt_tokens=100,completion_tokens=50,total_tokens=150))
```

### `run_fixture` — `Lines 21–34`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `34` (`Lines 21–34`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–34`):**
```python
def run_fixture(directory):
    session=PilotSession(directory);engine=create_session(session,'synthetic_burger','synthetic')
    chosen=set()
    for i in range(2):
        # Explicitly construct a new controller/engine instance to exercise restart.
        session=PilotSession(directory);state,_,_=session.read()
        session.approve('synthetic_burger',i,state['preview']['sha256'])
        engine=load_engine(directory)
        ids=[r['trace_id'] for r in state['context']['candidates'] if r['eligible'] and r['trace_id'] not in chosen][:2]
        chosen.update(ids)
        state=session.step(engine,SyntheticPlanner(ids,i),build_request,lambda e,s:make_preview(session,e,s),lambda:100.+61*i)
    summary=dict(status=state['phase'],requests_synthetic=state['requests'],real_requests=0,real_cost_usd=0,AI_performance='NOT_TESTED',reserved_tokens=state['reserved_tokens'],synthetic_completion_tokens=state['completion_tokens'],tool_calls=len(state['engine']['events']),commits=state['engine']['commits'],observations=state['observations'],geometry_hash=state['geometry_hash'],final_preview=state['preview'],paths=len(state['engine']['items']),actions=[dict(tool=a['tool'],added_paths=a['result'].get('added_paths'),decision=a['decision']) for a in state['actions']])
    (directory/'SUMMARY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    return summary
```
