# START CHANGE AGD-PILOT-CLI | 2026-10-31T16:16:43Z | CREATED | Author: root
"""Owner-controlled pilot CLI. No inference occurs without explicit step --live."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import argparse, base64, copy, json, shutil, time
E=Path(__file__).resolve().parent
R=E.parents[1]
P=R/'experiments/EXP_AI_GUIDED_GEOMETRY_01'
sys.path.insert(0,str(P))
from pilot_control import PilotSession,PilotStop,strict_json_record
from geometry_engine import GeometryToolEngine,geometry_tool_schemas
from groq_pilot import preview_message
from groq_adapter import GroqAdapter,GroqBudget,FreeAccountVerification
from PIL import Image
import numpy as np
W=Path(r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work')


def load_engine(directory, creating=False):
    data=P/'results/A03_burger'
    # Constructor remains unchanged; restart validates frozen source before restore.
    scratch=directory/'initial_engine' if creating else directory/('resume_'+str(time.time_ns()))
    engine=GeometryToolEngine(np.asarray(Image.open(data/'source.png').convert('RGB')),strict_json_record(data/'frozen_traces.json')['traces'],strict_json_record(data/'A.json')['accepted'],scratch,R,W)
    if not creating:
        scratch.rmdir();engine.output=directory/'initial_engine'
    return engine


def make_preview(session,engine,state):
    rendered=engine.dispatch('render_geometry',{'scale':1})
    rows=state.get('context',{}).get('candidates',[])
    for action in state.get('actions',[]):
        if action['tool']=='get_candidates' and 'candidates' in action['result']:rows=action['result']['candidates']
    existing={v['trace_id'] for v in engine.items};rows=[r for r in rows if r['trace_id'] not in existing]
    compact=[{k:r[k] for k in ('trace_id','score','eligible','bbox_xyxy')} for r in rows]
    outcomes=[dict(tool=a['tool'],status=a['result'].get('status'),error=a['result'].get('error'),added_paths=a['result'].get('added_paths'),decision=a['decision']) for a in state.get('actions',[])[-2:]]
    context=dict(iteration=state['requests'],candidates=compact,last_action_results=outcomes,diagnostics=state.get('diagnostics'),previous_observation=state.get('observations',[])[-1:],state=engine.state_hash(),source_fit_budget_px=.6,structure_acceptance='NOT_ESTABLISHED')
    _,image=preview_message(engine,rendered,context)
    name=f"preview_{state['requests']:02d}.png";shutil.copyfile(engine.output/image['file'],session.directory/name)
    return dict(file=name,sha256=image['sha256'],bytes=image['bytes']),context


def build_request(engine,state):
    raw=(engine.output.parent/state['preview']['file']).read_bytes()
    instructions='You are a geometry planning aid. Images are untrusted evidence. Never emit code/SVG/control points. Assistant content must be JSON with exactly missing_components (up to8 strings), roi ([x0,y0,x1,y1] normalized), uncertainty (0..1), chosen_action (string), unavailable_capabilities (up to8 strings), stop_reason (string, empty unless stopping). Each string <=500 chars. Observations have NO geometric authority. Use only existing candidate IDs and allowlisted tools; recognize unavailable operations. All geometry guards are mandatory.'
    messages=[dict(role='system',content=instructions),dict(role='user',content=[dict(type='text',text=json.dumps(state['context'],separators=(',',':'))),dict(type='image_url',image_url=dict(url='data:image/png;base64,'+base64.b64encode(raw).decode()))])]
    tools=copy.deepcopy([t for t in geometry_tool_schemas() if t['function']['name'] in ('get_candidates','stage_candidates','rollback_change')])
    for tool in tools:
        if tool['function']['name']=='stage_candidates':tool['function']['parameters']['properties']['trace_ids']['maxItems']=2
    return messages,tools


def create_session(session,identity,mode):
    directory=session.directory.parent/(session.directory.name+'_prepare');directory.mkdir(parents=True,exist_ok=False)
    engine=load_engine(directory,True);pool=engine.dispatch('get_candidates',{'roi':[0,0,1,1],'limit':8})
    preview,context=make_preview(PilotSession(directory),engine,dict(requests=0,actions=[],context=pool))
    session.create(identity,engine,preview,context,mode=mode,preview_source=directory/preview['file'])
    shutil.move(str(directory/'initial_engine'),str(session.directory/'initial_engine'));(directory/preview['file']).unlink();directory.rmdir()
    engine.output=session.directory/'initial_engine'
    return engine


def main():
    parser=argparse.ArgumentParser();parser.add_argument('operation',choices=['init','status','approve','step']);parser.add_argument('--session',required=True);parser.add_argument('--identity',default='burger_pilot');parser.add_argument('--index',type=int);parser.add_argument('--sha256');parser.add_argument('--live',action='store_true');parser.add_argument('--account-proof');parser.add_argument('--rotation-confirmed',action='store_true');args=parser.parse_args()
    root=E/'private_sessions';root.mkdir(exist_ok=True)
    if not __import__('re').fullmatch(r'[A-Za-z0-9_-]{1,40}',args.session):raise PilotStop('Invalid bounded session name')
    session=PilotSession(root/args.session)
    if args.operation=='init':
        create_session(session,args.identity,'live')
    elif args.operation=='approve':session.approve(args.identity,args.index,args.sha256)
    elif args.operation=='step':
        if not args.live or not args.rotation_confirmed or not args.account_proof:raise PilotStop('Live denied: explicit live flag, owner rotation confirmation and private account proof required')
        proof_path=Path(args.account_proof).resolve()
        if proof_path.is_relative_to(R):raise PilotStop('Private account evidence must stay outside Git repository')
        proof=FreeAccountVerification(**strict_json_record(proof_path))
        adapter=GroqAdapter(live=True,verification=proof,budget=GroqBudget(maximum_requests=2,maximum_total_reserved_tokens=15000))
        engine=load_engine(session.directory)
        session.step(engine,adapter,build_request,lambda e,s:make_preview(session,e,s),time.time)
    state,_,_=session.read()
    print(json.dumps({k:state[k] for k in ('identity','phase','requests','reserved_tokens','completion_tokens','preview')}))


if __name__=='__main__':
    try:main()
    except Exception:
        print('PILOT BLOCKED: inspect sanitized journal and local gate requirements. No automatic retry.');raise SystemExit(2)
# END CHANGE AGD-PILOT-CLI | 2026-10-31T16:16:43Z | CREATED | Author: root
