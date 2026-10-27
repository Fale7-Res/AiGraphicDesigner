"""Audit unchanged selection AST and helper math; test Windows process cleanup."""
# START CHANGE AGD-CODEX-WIN-VERIFY | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
import ast
import hashlib
import json
import sys
import tempfile
from pathlib import Path
import psutil
from windows_search import OWNER, run_trial, supervise
ROOT=Path(__file__).resolve().parent

def verify_sources() -> dict:
    """Compare selected derived function ASTs excluding docstrings only."""
    sources={
      'historical_optimizer':ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027'/'optimizer.py',
      'historical_search':ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'/'src'/'search.py',
      'historical_evaluate':ROOT.parent/'EXP_VTRACER_FIDELITY_20261024'/'src'/'evaluate.py',
      'derived_optimizer':ROOT/'optimizer.py','derived_search':ROOT/'windows_search.py'}
    trees={key:ast.parse(path.read_text(encoding='utf-8')) for key,path in sources.items()}
    def function_body(key: str,name: str) -> str:
        function=next(n for n in trees[key].body if isinstance(n,ast.FunctionDef) and n.name==name)
        if isinstance(function.body[0],ast.Expr) and isinstance(function.body[0].value,ast.Constant):
            function.body=function.body[1:]
        return ast.dump(function,include_attributes=False)
    matched={}
    for name in ('canonical','pilots','neighborhood','optimize'):
        matched['optimizer.'+name]=function_body('historical_optimizer',name)==function_body('derived_optimizer',name)
    for name in ('prepare_input','extra_metrics','fidelity_score'):
        matched['search.'+name]=function_body('historical_search',name)==function_body('derived_search',name)
    report={'source_files':{key:{'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()} for key,path in sources.items()},
            'function_ast_equivalence_excluding_docstrings':matched,
            'derived_copy_rationale':'Isolate Windows worker/resource and renderer adaptation; historical POSIX resource import prevents native Windows import. No runtime source rewriting or fake resource module.',
            'historical_evaluate':'Imported unchanged directly for load_rgb, compare, svg_structure.',
            # START CHANGE AGD-CODEX-WIN-SCOPE-EVIDENCE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
            'intended_historical_write_scope':'none; historical changes checked separately against Git baseline'}
    # END CHANGE AGD-CODEX-WIN-SCOPE-EVIDENCE | 2026-10-27T10:36:21Z | EDITED | Author: windows_extension
    (ROOT/'source_provenance.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if not all(matched.values()): raise AssertionError(matched)
    return report

def verify_timeout() -> dict:
    """Run an actual child+grandchild and verify whole observed tree exits."""
    folder=ROOT/'reports';folder.mkdir(exist_ok=True)
    # Only the test processes created here are terminated by the supervisor.
    code='import subprocess,sys,time; subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"]); time.sleep(30)'
    result=supervise([sys.executable,'-c',code],folder/'timeout_cleanup.log',timeout=1.5)
    surviving=[]
    for pid in result['observed_pids']:
        if psutil.pid_exists(pid): surviving.append(pid)
    result['surviving_observed_pids']=surviving
    result['passed']=result['termination_reason']=='timeout' and len(result['observed_pids'])>=2 and not surviving
    (folder/'timeout_cleanup.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    if not result['passed']: raise AssertionError(result)
    return result

# START CHANGE AGD-CODEX-WIN-GUARD-QA | 2026-10-27T10:41:16Z | CREATED | Author: windows_extension
def verify_trial_history_guard() -> dict:
    """Ensure trial replay cannot overwrite even an arbitrary prior sentinel."""
    with tempfile.TemporaryDirectory() as directory:
        folder=Path(directory);sentinel=folder/'prior-evidence.txt';sentinel.write_text('preserve',encoding='utf-8')
        rejected=False
        try: run_trial(folder/'not-opened.png',folder,OWNER)
        except FileExistsError: rejected=True
        preserved=sentinel.read_text(encoding='utf-8')=='preserve' and list(folder.iterdir())==[sentinel]
        report={'passed':rejected and preserved,'rejected_nonempty_trial':rejected,'prior_evidence_preserved':preserved}
    (ROOT/'reports'/'trial_history_guard.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    if not report['passed']: raise AssertionError(report)
    return report

if __name__=='__main__':
    verify_sources();verify_timeout();verify_trial_history_guard()
    print('Source equivalence, process-tree timeout, and trial history checks passed.')
# END CHANGE AGD-CODEX-WIN-GUARD-QA | 2026-10-27T10:41:16Z | CREATED | Author: windows_extension
# END CHANGE AGD-CODEX-WIN-VERIFY | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
