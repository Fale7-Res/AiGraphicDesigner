"""Independent reconstruction checks for vector alpha run geometry, no renderer claim."""
# START CHANGE AGD-CODEX-ALPHA-GEOMETRY-QA | 2026-10-27T10:27:04Z | CREATED | Author: windows_extension
import json
import re
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path
import numpy as np
from PIL import Image
from alpha_optimizer import apply_vector_alpha
ROOT=Path(__file__).resolve().parent

def verify_alpha_runs() -> dict:
    """Reconstruct all 256 alpha levels and boundary cases from serialized paths."""
    matrices={'all_levels':np.arange(256,dtype='uint8').reshape(16,16),
              'all_transparent':np.zeros((16,16),dtype='uint8'),
              'all_opaque':np.full((16,16),255,dtype='uint8'),
              'checker':np.indices((16,16)).sum(axis=0).astype('uint8')%2*255}
    results={}
    with tempfile.TemporaryDirectory() as directory:
        folder=Path(directory)
        source=folder/'rgb.svg'
        source.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"><rect width="16" height="16" fill="red"/></svg>',encoding='utf-8')
        for name,expected in matrices.items():
            Image.fromarray(expected).save(folder/'alpha.png')
            stats=apply_vector_alpha(source,folder/'alpha.png',folder/'output.svg')
            reconstructed=np.zeros_like(expected)
            root=ET.parse(folder/'output.svg').getroot()
            mask=next(e for e in root.iter() if e.tag.endswith('}mask'))
            for path in mask:
                alpha=int(round(float(path.get('fill-opacity'))*255))
                for match in re.finditer(r'M(\d+) (\d+)H(\d+)V(\d+)H(\d+)Z',path.get('d')):
                    x,y,end,next_y,back=map(int,match.groups())
                    if back!=x or next_y!=y+1: raise AssertionError('Malformed horizontal run')
                    reconstructed[y:next_y,x:end]=alpha
            equal=np.array_equal(expected,reconstructed)
            results[name]={'exact_array_reconstruction':equal,'raster_free':stats['structure']['raster_free'],
                           'alpha_run_count':stats['alpha_run_count']}
            if not equal or not stats['structure']['raster_free']: raise AssertionError(results)
    report={'passed':True,'cases':results,'scope':'serialized vector geometry only; actual renderer alpha correctness requires separate evaluate_alpha run'}
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports'/'alpha_geometry_tests.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return report

if __name__=='__main__': print(json.dumps(verify_alpha_runs(),indent=2))
# END CHANGE AGD-CODEX-ALPHA-GEOMETRY-QA | 2026-10-27T10:27:04Z | CREATED | Author: windows_extension
