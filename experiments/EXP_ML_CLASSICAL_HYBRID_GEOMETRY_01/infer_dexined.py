# START CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
"""CPU-only OpenCV ONNX inference. No evaluator/reference inputs or training."""
import os
os.environ['OMP_NUM_THREADS']='2'
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import sys,time,json,hashlib
import cv2
import numpy as np
from PIL import Image
from scipy.special import expit

def infer(source,weights,out):
    out=Path(out);out.mkdir(parents=True,exist_ok=False)
    cv2.setNumThreads(2)
    rgb=np.asarray(Image.open(source).convert('RGB'));h,w=rgb.shape[:2]
    started=time.perf_counter();net=cv2.dnn.readNetFromONNX(str(weights))
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV);net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
    load=time.perf_counter()-started
    blob=cv2.dnn.blobFromImage(rgb[...,::-1].copy(),1.,(256,256),(103.5,116.2,123.6),swapRB=False,crop=False)
    net.setInput(blob);started=time.perf_counter();outputs=net.forward();elapsed=time.perf_counter()-started
    logits=np.asarray(outputs,dtype=np.float32)
    # Published OpenCV wrapper treats last first-axis prediction as fused.
    fuse=np.squeeze(logits[-1]);assert fuse.ndim==2,fuse.shape
    probability=cv2.resize(expit(fuse),(w,h),interpolation=cv2.INTER_LINEAR)
    np.savez_compressed(out/'predictions.npz',raw_outputs=logits,native_sigmoid=probability)
    Image.fromarray(np.rint(probability*255).astype('uint8')).save(out/'sigmoid.png')
    report={'opencv':cv2.__version__,'model_load_seconds':load,'inference_seconds':elapsed,'output_shape':list(logits.shape),'native_size':[w,h],'sigmoid_min':float(probability.min()),'sigmoid_max':float(probability.max()),'model_sha256':hashlib.sha256(Path(weights).read_bytes()).hexdigest(),'source_sha256':hashlib.sha256(Path(source).read_bytes()).hexdigest(),'device':'CPU','threads':2,'inference_shape':[256,256],'resource_fallback':True,'normalization':'sigmoid only, no per-image minmax','training':False}
    (out/'inference.json').write_text(json.dumps(report,indent=2));print(json.dumps(report),flush=True)

if __name__=='__main__':infer(*sys.argv[1:])

# END CHANGE AGD-ML-PACKAGE | 2026-10-30T08:17:45Z | CREATED | Author: root
