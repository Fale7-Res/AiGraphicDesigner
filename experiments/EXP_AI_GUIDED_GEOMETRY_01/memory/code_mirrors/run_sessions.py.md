# مرآة الكود التفصيلية: `run_sessions.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `run_sessions.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `run_sessions.py`
- **الدور المعماري (`Architectural Role`):** Isolated restricted geometry tools / controller / Groq adapter / evaluator research
- **إجمالي عدد الأسطر (`Total Lines`):** `56` (`Lines 1–56`)
- **بصمة الملف (`SHA-256`):** `b59cb20e3984efa3371060ae6e7d96a36cbd6cf5d1ce35cd9e44bda5e807ece0`
- **الوصف التفصيلي:** # START CHANGE AGD-TOOL-SESSIONS | 2026-10-31T11:55:00Z | CREATED | Author: root

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `frozen native source/evidence/P curves; provider responses only through strict local tool schemas; evaluator refs only in measurement` | candidate IDs, source coordinates, cubic arrays, typed local requests and budgets | source-only geometry; no unrestricted execution or live requests by default |
| **يرمي إلى (`Throws To`)** | `this isolated experiment` | transaction journals, exact SVG/PNG previews, replay hashes, objective diagnostics and sanitized provider status | offline research; AI NOT_TESTED; geometry NOT_ACCEPTED; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `run_controller` | `function` | `Lines 17–29` | `def run_controller(engine,kind):` | Fixed policy before benchmark. Every action uses the same dispatch contract. |
| `session_worker` | `function` | `Lines 31–46` | `def session_worker(case):` | رمز برمجي موثق. |
| `launch_sessions` | `function` | `Lines 48–52` | `def launch_sessions():` | رمز برمجي موثق. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `run_controller` — `Lines 17–29`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `17` إلى السطر `29` (`Lines 17–29`)
- **الوظيفة:** Fixed policy before benchmark. Every action uses the same dispatch contract.
- **الكود الفعلي (`Lines 17–29`):**
```python
def run_controller(engine,kind):
 """Fixed policy before benchmark. Every action uses the same dispatch contract."""
 rois=[[0,0,1,1],[0,0,1,1]] if kind=='B' else [[0,0,1,.5],[0,.5,1,1]]
 for roi in rois:
  engine.dispatch('inspect_region',{'roi':roi});found=engine.dispatch('get_candidates',{'roi':roi,'limit':16});ids=[x['trace_id'] for x in found['candidates'] if x['eligible']][:2]
  if ids:
   staged=engine.dispatch('stage_candidates',{'trace_ids':ids})
   engine.dispatch('commit_change' if staged.get('added_paths',0) else 'rollback_change',{})
  else:
   engine.dispatch('validate_geometry',{});engine.dispatch('validate_geometry',{})
  engine.dispatch('render_geometry',{'scale':1})
 engine.dispatch('validate_geometry',{});engine.dispatch('render_geometry',{'scale':4})
 return engine.export_state()
```

### `session_worker` — `Lines 31–46`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `31` إلى السطر `46` (`Lines 31–46`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 31–46`):**
```python
def session_worker(case):
 protocol=json.loads((E/'protocol.json').read_text());cfg=protocol['cases'][case];out=E/'results'/case;out.mkdir(exist_ok=False);rgb=np.asarray(Image.open(cfg['source']).convert('RGB'));h,w=rgb.shape[:2];shutil.copy2(cfg['source'],out/'source.png');start=time.monotonic()
 if cfg.get('baseline'):
  frozen=json.loads(Path(cfg['traces']).read_text());p=json.loads(Path(cfg['baseline']).read_text());shutil.copy2(cfg['baseline_svg'],out/'A.svg')
 else:
  frozen,_,_=new_classical(rgb);p=construct_condition(frozen,'P',time.monotonic()+120);(out/'A.svg').write_text(svg_graph(chain_graph(p['accepted'],w,h)),encoding='utf-8')
 (out/'frozen_traces.json').write_text(json.dumps(frozen),encoding='utf-8');(out/'A.json').write_text(json.dumps(dict(accepted=p['accepted'])),encoding='utf-8')
 for kind in ['B','M']:
  eng=GeometryToolEngine(rgb,frozen['traces'],p['accepted'],out/kind,R,W);result=run_controller(eng,kind);result.update(controller='deterministic_fullframe' if kind=='B' else 'MOCK_FIXED_PLAN_NOT_AI',decision_hash=eng.replay_decision_hash(),tool_events=eng.events,api_requests=0,actual_api_cost_usd=0,AI_performance='NOT_TESTED');(out/(kind+'.json')).write_text(json.dumps(result),encoding='utf-8')
  last=next(ev['result'] for ev in reversed(eng.events) if ev['tool']=='render_geometry' and ev['status']=='ok');shutil.copy2(out/kind/last['svg'],out/(kind+'.svg'))
  if kind=='M':
   replay=GeometryToolEngine(rgb,frozen['traces'],p['accepted'],out/'replay_M',R,W)
   for event in eng.events:replay.dispatch(event['tool'],event['arguments'])
   assert replay.state_hash()==eng.state_hash();assert replay.replay_decision_hash()==eng.replay_decision_hash();(out/'REPLAY.json').write_text(json.dumps(dict(passed=True,geometry_hash=result['state_hash'],decision_hash=result['decision_hash'],events=len(eng.events),runtime_hashes_expected_to_differ=True)))
 (out/'C_STATUS.json').write_text(json.dumps(dict(AI_performance='NOT_TESTED',live_requests=0,reason='Account free-tier/quota/no-charge state unverified. No pasted credential used.')))
 (out/'WORKER.json').write_text(json.dumps(dict(wall_seconds=time.monotonic()-start,case=case,conditions=['A','B','M'],C='NOT_TESTED')));print(case,'completed',flush=True)
```

### `launch_sessions` — `Lines 48–52`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `48` إلى السطر `52` (`Lines 48–52`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 48–52`):**
```python
def launch_sessions():
 protocol=json.loads((E/'protocol.json').read_text());results=[]
 for file,pin in protocol['pins'].items():assert hashlib.sha256(Path(file).read_bytes()).hexdigest()==pin['sha256'],file
 for case in protocol['cases']:
  result=supervise([sys.executable,Path(__file__),case],E/'reports'/(case+'.log'));results.append(dict(case=case,**result));(E/'reports/RESOURCES.json').write_text(json.dumps(results,indent=2));print(case,result['status'],result['wall_seconds'],result['sampled_tree_RSS_peak_mib'],flush=True)
```
