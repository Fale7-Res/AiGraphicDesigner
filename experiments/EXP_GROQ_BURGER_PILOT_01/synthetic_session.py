# START CHANGE AGD-PILOT-SYNTHETIC | 2026-10-31T16:16:43Z | CREATED | Author: root
"""Replayable two-step local fixture. No provider request or key access."""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
import json, argparse
from hardened_pilot import E,create_session,load_engine,build_request,make_preview
from pilot_control import PilotSession,digest
from groq_adapter import GroqAdapter


class SyntheticPlanner:
    live=False
    def __init__(self,ids,index):self.ids=ids;self.index=index
    def _prepare(self,messages,tools):return GroqAdapter(live=False)._prepare(messages,tools)
    def request(self,*args):
        obs=dict(missing_components=['Synthetic test observation: contour completeness is unverified'],roi=[0,0,1,1],uncertainty=.8,chosen_action='Test existing candidate transaction; not AI reasoning',unavailable_capabilities=['wholly new boundaries','accepted curve movement'],stop_reason='fixture complete' if self.index==1 else '')
        return dict(status='SYNTHETIC',message=dict(content=json.dumps(obs),tool_calls=[dict(id=f'synthetic_{self.index}',type='function',function=dict(name='stage_candidates',arguments=json.dumps(dict(trace_ids=self.ids))))]),usage=dict(prompt_tokens=100,completion_tokens=50,total_tokens=150))


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


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--name',required=True);args=parser.parse_args()
    if not __import__('re').fullmatch('[A-Za-z0-9_-]{1,40}',args.name):raise ValueError('Invalid fixture name')
    result=run_fixture(E/'results'/args.name);print(json.dumps(result))
# END CHANGE AGD-PILOT-SYNTHETIC | 2026-10-31T16:16:43Z | CREATED | Author: root
