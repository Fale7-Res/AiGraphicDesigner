# START CHANGE VTRACER-TEST-ISOLATION | 2026-10-24T23:42:36Z | EDITED | Author: vtracer_sources
"""Native synthetic alpha/color audit; diagnostic raw-alpha failures are retained."""
# START CHANGE VTRACER-COLOR-CONTRACT | 2026-10-24T09:55:59Z | CREATED | Author: vtracer_sources
from pathlib import Path
import argparse,json,subprocess,sys,unittest,tempfile
import numpy as np
from PIL import Image
from evaluate import load_rgb,render_svg,compare

ROOT=Path(__file__).resolve().parents[1]

def audit_color_contract(destination):
    """Compare raw alpha and explicit white composition through native SVG rendering."""
    destination=Path(destination);destination.mkdir(parents=True,exist_ok=True)
    fixtures={}
    a=np.zeros((16,16,4),np.uint8);a[:]=[255,0,0,128];fixtures['partial_red']=a
    a=a.copy();a[:,:,3]=np.arange(16,dtype=np.uint8)[None,:]*17;fixtures['alpha_ramp']=a
    a=a.copy();a[:,:,3]=0;fixtures['fully_transparent']=a
    a=np.zeros((16,16,4),np.uint8);a[:8,:8]=[255,0,0,255];a[:8,8:]=[0,255,0,255];a[8:,:8]=[0,0,255,255];a[8:,8:]=[128,128,128,255];fixtures['srgb_patches']=a
    records=[]
    for name,rgba in fixtures.items():
        source=destination/(name+'.png');Image.fromarray(rgba).save(source)
        white=load_rgb(source);prepared=destination/(name+'_white.png');Image.fromarray(white).save(prepared)
        for clustering in ['color-cluster','watershed']:
            for route,input_path in [('raw',source),('white',prepared)]:
                stem=name+'_'+clustering+'_'+route;svg=destination/(stem+'.svg');png=destination/(stem+'.png')
                config={'clustering':clustering,'filter_speckle':0,'color_precision':8,'layer_difference':0,'mode':'pixel','path_precision':3,'watershed_detail':512}
                code='import vtracer,json,sys;vtracer.Config(**json.loads(sys.argv[3])).convert_file(sys.argv[1],sys.argv[2])'
                proc=subprocess.run([sys.executable,'-c',code,str(input_path),str(svg),json.dumps(config)],capture_output=True,text=True,timeout=30)
                row={'fixture':name,'clustering':clustering,'route':route,'config':config,'returncode':proc.returncode,'stderr':proc.stderr}
                if proc.returncode==0:
                    render_svg(svg,png,16,16)
                    with Image.open(png) as im:im.verify()
                    pred=load_rgb(png);row['white_composited_metrics']=compare(white,pred)
                    with Image.open(png) as im:row['rendered_alpha_range']=[int(np.array(im.convert('RGBA'))[:,:,3].min()),int(np.array(im.convert('RGBA'))[:,:,3].max())]
                records.append(row)
    report={'contract':'RGB sRGB numeric values; explicit white composition before tracing. Raw arbitrary alpha is diagnostic only, not supported contract. No ICC conversion tested here.','records':records}
    (destination/'audit.json').write_text(json.dumps(report,indent=2));return report

class ColorContractTests(unittest.TestCase):
    def test_explicit_white_contract_and_raw_alpha_diagnostic(self):
        """Opaque canonical fixtures retain colors; raw partial alpha is not silently approved."""
        with tempfile.TemporaryDirectory() as temporary:
            report=audit_color_contract(temporary)
        for row in report['records']:
            if row['route']=='white':
                self.assertEqual(row['returncode'],0,row)
                self.assertLessEqual(row['white_composited_metrics']['rmse'],1,row)
        raw=[r for r in report['records'] if r['fixture']=='partial_red' and r['route']=='raw']
        self.assertTrue(any(r['returncode'] or r['white_composited_metrics']['rmse']>10 for r in raw))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args,other=parser.parse_known_args()
    if args.output:audit_color_contract(args.output)
    else:unittest.main(argv=[sys.argv[0]]+other)
# END CHANGE VTRACER-COLOR-CONTRACT | 2026-10-24T09:55:59Z | CREATED | Author: vtracer_sources

# END CHANGE VTRACER-TEST-ISOLATION | 2026-10-24T23:42:36Z | EDITED | Author: vtracer_sources
