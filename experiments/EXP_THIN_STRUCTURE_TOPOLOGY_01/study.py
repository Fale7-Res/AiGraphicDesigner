# START CHANGE AGD-THIN-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
"""Shared paths and inherited helpers; construction never receives references."""
from pathlib import Path
import os,sys,importlib.util,json,hashlib
os.environ['OPENBLAS_NUM_THREADS']='1';os.environ['OMP_NUM_THREADS']='1'
ROOT=Path(__file__).resolve().parent
PREVIOUS=ROOT.parent/'EXP_COMPLETE_GEOMETRY_ISOLATION_01'
WORK=Path(os.environ.get('AGD_ISOLATION_WORK',r'C:\Users\Mohamed\Documents\Codex\2026-10-27\https-chatgpt-com-codex-desktop-auth\work'))
sys.path[:0]=[str(PREVIOUS),str(WORK/'geometry-deps')]
from isolation import dump,digest,arena_modules,case_dir as inherited_case_dir
CASES=['fine_features','G06_arabic','A01_shield','K01_linear_corner_hole']

def destination(case):
    return (WORK/'thin_structure_topology/external_results' if case=='fine_features' else ROOT/'results')/case

def load_baseline(case):
    import numpy as np
    from PIL import Image
    base=inherited_case_dir(case)
    return np.asarray(Image.open(base/'working.png').convert('RGB')),np.load(base/'S_A.npy',allow_pickle=False),json.loads((base/'S_A_F_A_common_faces.json').read_text(encoding='utf-8'))

def initialize_labels(labels):
    # Calls the existing unmodified external initializer, geometry primitives
    # only. The historical read-only import explicitly denies Cairo rendering.
    _,gm,fm,hashes=arena_modules()
    g=gm.construct(labels);stats=fm.initialize(g,labels.shape[1],labels.shape[0],tolerance=.8,smooth=1.)
    result=gm.serialize(g,labels.shape[1],labels.shape[0]);result['stats']=stats;result['external_source_hashes']=hashes
    return result

# END CHANGE AGD-THIN-STUDY | 2026-10-29T08:39:37Z | CREATED | Author: root
