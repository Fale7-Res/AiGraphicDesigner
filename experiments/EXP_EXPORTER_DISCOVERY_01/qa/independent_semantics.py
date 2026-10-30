# START CHANGE AGD-EXPORT-QA-INDEPENDENT-SEMANTICS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
"""Independent third-party SVG parser tests; no candidate generation or fitting."""
import importlib.util,json,sys,random,xml.etree.ElementTree as ET
from pathlib import Path
from fontTools.pens.recordingPen import RecordingPen
from fontTools.svgLib.path import parse_path

HERE=Path(__file__).resolve().parent
SER=HERE.parent/'exporter_stage'/'svg_exporter.py'
spec=importlib.util.spec_from_file_location('independent_exporter_under_test',SER)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

def interpreted(text):
    pen=RecordingPen();parse_path(text,pen)
    current=start=None;segments=[]
    for op,args in pen.value:
        if op=='moveTo':current=start=args[0]
        elif op=='lineTo':segments.append(('L',current,args[0]));current=args[0]
        elif op=='curveTo':segments.append(('C',current,*args));current=args[-1]
        elif op=='closePath':
            if current!=start:segments.append(('L',current,start))
            current=start
        elif op!='endPath':raise AssertionError(op)
    return segments

rng=random.Random(79123);passed=0
for test in range(100):
    a=tuple(rng.uniform(3,8) for _ in range(2))
    b=tuple(rng.uniform(12,18) for _ in range(2))
    c=tuple(rng.uniform(20,30) for _ in range(2))
    p1=tuple(rng.uniform(8,15) for _ in range(2));p2=tuple(rng.uniform(15,22) for _ in range(2))
    chain={'id':0,'closed':True,'adjacent_face_labels':[0,1],
      'pixel_crack_vertices':[list(a),list(b),list(c)],
      'segments':[{'type':'L','p0':list(a),'p3':list(b)},
      {'type':'C','p0':list(b),'p1':list(p1),'p2':list(p2),'p3':list(c)}]}
    for reverse in (False,True):
        for raw in (False,True):
            graph={'width':64,'height':64,'chains':[chain],
              'faces':{'1':[[{'chain':0,'forward':not reverse}]]}}
            text=module.svg_graph(graph,raw=raw,regions=True)
            paths=ET.fromstring(text);assert len(paths)==1
            observed=interpreted(paths[0].attrib['d'])
            middle=('L',b,c) if raw else ('C',b,p1,p2,c)
            expected=[('L',a,b),middle,('L',c,a)]
            if reverse:expected=[(seg[0],*reversed(seg[1:])) for seg in reversed(expected)]
            assert observed==expected,(test,reverse,raw,observed,expected)
            passed+=1
report={'test':'100 deterministic random closed L/C walks, both directions, raw and fitted',
 'parser':'fontTools.svgLib.path.parse_path via RecordingPen; independent of project parser',
 'semantic_checks_passed':passed,'geometry_benchmarks_run':0,
 'limitations':'Abstract command semantics, not certified global topology, renderer or crown truth.'}
(HERE/'independent_semantics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report))

# END CHANGE AGD-EXPORT-QA-INDEPENDENT-SEMANTICS | 2026-10-29T22:12:25Z | CREATED | Author: export_discovery_qa
