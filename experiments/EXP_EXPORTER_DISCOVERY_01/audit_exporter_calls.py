# START CHANGE AGD-EXPORTER-AUDIT | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness
"""Read-only repository source audit; output JSON in caller-selected location."""
import argparse
import ast
import json
from pathlib import Path


def audit(root):
    hits=[];definitions=[];other=[]
    for path in sorted(root.rglob('*')):
        if path.suffix not in {'.py','.rs','.js','.ts'}:continue
        if any(x in {'.git','node_modules','.venv','venv','__pycache__','target','build','memory'} for x in path.parts):continue
        try:text=path.read_text(encoding='utf-8')
        except (UnicodeError,OSError):continue
        relative=path.relative_to(root).as_posix()
        for number,line in enumerate(text.splitlines(),1):
            if 'svg_graph(' in line:
                hits.append({'file':relative,'line':number,'text':line.strip()})
            if 'def svg_graph(' in line:definitions.append({'file':relative,'line':number})
            if any(token in line for token in ('def export_svg','def to_svg','fn to_svg','fn write_svg')):
                other.append({'file':relative,'line':number,'text':line.strip()})
    return {'scope':'Source inspection, not exhaustive dynamic dependency proof','svg_graph_mentions':hits,'svg_graph_definitions':definitions,'other_exporter_definitions':other}


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('repository');parser.add_argument('output');args=parser.parse_args()
    result=audit(Path(args.repository));Path(args.output).write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({'mentions':len(result['svg_graph_mentions']),'definitions':result['svg_graph_definitions'],'other_exporters':result['other_exporter_definitions']},indent=2))
# END CHANGE AGD-EXPORTER-AUDIT | 2026-10-29T21:55:44Z | CREATED | Author: exporter_correctness
