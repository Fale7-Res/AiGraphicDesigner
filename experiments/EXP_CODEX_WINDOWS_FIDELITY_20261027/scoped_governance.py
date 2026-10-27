"""Reuse existing governance tools with explicitly isolated experiment paths.

No historical tool is copied or edited. Globals are set only on private imported
module instances, keeping all generated writes inside this experiment.
"""
# START CHANGE AGD-CODEX-WIN-GOV | 2026-10-27T10:44:02Z | EDITED | Author: root
import argparse
import importlib.util
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HISTORY=ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027'/'tools'

def load_scoped_tool(relative: str):
    """Load historical governance implementation with isolated output constants."""
    path=HISTORY/relative
    spec=importlib.util.spec_from_file_location('isolated_'+path.stem,path)
    tool=importlib.util.module_from_spec(spec);spec.loader.exec_module(tool)
    tool.ROOT=ROOT
    return tool

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

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--mirrors',action='store_true')
    parser.add_argument('--documents',action='store_true');args=parser.parse_args()
    if args.mirrors: print(json.dumps(sync_scoped_mirrors(),ensure_ascii=True))
    if args.documents: print(json.dumps(track_scoped_documents(),ensure_ascii=True))
# END CHANGE AGD-CODEX-WIN-GOV | 2026-10-27T10:44:02Z | EDITED | Author: root
