"""V04 repair: boundary-aware superpixels, smooth cubic contours, local SVG gradients.

This implementation deliberately does not emit source-edge pixel runs or embed a
source raster. It models each SLIC region as one compound vector path and chooses
between a solid fill and a local multi-stop linear gradient from measured RGB data.
"""
from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import html, time, xml.etree.ElementTree as ET
import cv2
import numpy as np
from PIL import Image
from skimage.segmentation import slic

@dataclass
class Config:
    initial_segments: int = 850
    target_regions: int = 180
    compactness: float = 8.0
    sigma: float = 0.65
    boundary_weight: float = 0.018
    merge_threshold: float = 0.0015
    contour_epsilon_px: float = 1.8
    min_region_area_px: int = 3
    min_gradient_pixels: int = 30
    min_gradient_r2: float = 0.28
    min_gradient_gain: float = 0.20
    gradient_stops: int = 5
    seam_stroke_px: float = 0.0
    seam_stroke_opacity: float = 0.0
    corner_turn_degrees: float = 86.0
    max_dimension: int = 4096


def _rgb_hex(rgb) -> str:
    vals = np.clip(np.rint(np.asarray(rgb, dtype=float)), 0, 255).astype(int)
    return '#%02x%02x%02x' % tuple(vals.tolist())


def _escape(s: str) -> str:
    return html.escape(s, quote=True)


def _curve_path(points: np.ndarray, turn_degrees: float) -> tuple[str, int]:
    """Convert a closed contour into cubic segments; retain strong corners.

    Points have already been simplified with approxPolyDP. Catmull-Rom-like cubic
    handles provide smooth arcs; at vertices exceeding the turn threshold the
    handles are clamped to the vertex to preserve corners instead of rounding them.
    """
    p = np.asarray(points, dtype=np.float64).reshape(-1, 2)
    if len(p) < 3:
        return '', 0
    # Remove adjacent duplicate points that make ill-defined tangents.
    keep = [p[0]]
    for q in p[1:]:
        if np.linalg.norm(q - keep[-1]) > 1e-6:
            keep.append(q)
    p = np.asarray(keep, dtype=np.float64)
    if len(p) > 2 and np.linalg.norm(p[0] - p[-1]) < 1e-6:
        p = p[:-1]
    n = len(p)
    if n < 3:
        return '', 0
    corners = np.zeros(n, dtype=bool)
    threshold = np.deg2rad(turn_degrees)
    for i in range(n):
        incoming = p[i] - p[(i - 1) % n]
        outgoing = p[(i + 1) % n] - p[i]
        ni, no = np.linalg.norm(incoming), np.linalg.norm(outgoing)
        if ni < 1e-7 or no < 1e-7:
            corners[i] = True
            continue
        cosang = float(np.clip(np.dot(incoming, outgoing) / (ni * no), -1, 1))
        turn = np.pi - np.arccos(cosang)
        corners[i] = turn >= threshold
    # For non-corners, cubic controls approximate a centripetal Catmull-Rom tangent.
    tangents = np.zeros_like(p)
    for i in range(n):
        if corners[i]:
            tangents[i] = 0
        else:
            prev = p[(i - 1) % n]
            curr = p[i]
            nxt = p[(i + 1) % n]
            # Weighted secant reduces overshoot when segment lengths differ.
            a = np.linalg.norm(curr - prev); b = np.linalg.norm(nxt - curr)
            if a + b > 1e-8:
                tangents[i] = (nxt - prev) * (min(a, b) / (a + b)) / 3.0
    chunks = [f'M {p[0,0]:.3f} {p[0,1]:.3f}']
    for i in range(n):
        j = (i + 1) % n
        p0, p1 = p[i], p[j]
        c1 = p0 + tangents[i]
        c2 = p1 - tangents[j]
        chunks.append(f'C {c1[0]:.3f} {c1[1]:.3f} {c2[0]:.3f} {c2[1]:.3f} {p1[0]:.3f} {p1[1]:.3f}')
    chunks.append('Z')
    return ' '.join(chunks), n


def _binned_surface(colors: np.ndarray, t: np.ndarray, stop_count: int):
    """Fit a compact multi-stop gradient from mean RGB per position bin."""
    t=np.clip(t.astype(np.float64),0,1)
    stops=[]; offsets=(np.arange(stop_count,dtype=float)+0.5)/stop_count
    fitted=np.zeros_like(colors,dtype=np.float64)
    edges=np.linspace(0,1,stop_count+1)
    for i in range(stop_count):
        select=(t>=edges[i]) & ((t<edges[i+1]) if i<stop_count-1 else (t<=edges[i+1]))
        stops.append(colors[select].mean(axis=0) if np.any(select) else colors.mean(axis=0))
    stops_arr=np.asarray(stops)
    for ch in range(3): fitted[:,ch]=np.interp(t,offsets,stops_arr[:,ch])
    residual=float(np.sum((colors-fitted)**2))
    return [(float(o),_rgb_hex(c)) for o,c in zip(offsets,stops_arr)],residual


def _fit_region_gradient(rgb: np.ndarray, mask: np.ndarray, cfg: Config):
    """Compare local linear and radial multi-stop gradients against a flat fill."""
    ys,xs=np.where(mask); n=len(xs)
    if n<cfg.min_gradient_pixels: return None
    colors=rgb[ys,xs].astype(np.float64); mean=colors.mean(axis=0); total=float(np.sum((colors-mean)**2))
    if total<1e-6:return None
    xy=np.column_stack((xs.astype(float),ys.astype(float))); xy0=xy.mean(axis=0); centered_xy=xy-xy0; centered_color=colors-mean
    candidates=[]
    # Candidate 1: a direction fitted by RGB spatial regression, followed by 5 stop colors.
    try:
        coef,*_=np.linalg.lstsq(centered_xy,centered_color,rcond=None)
        u,_,_=np.linalg.svd(coef,full_matrices=False); direction=u[:,0]
        proj=centered_xy@direction; pmin=float(proj.min()); pmax=float(proj.max())
        if pmax-pmin>=4:
            norm=(proj-pmin)/(pmax-pmin); stops,res=_binned_surface(colors,norm,cfg.gradient_stops)
            gain=(total-res)/max(total,1e-9)
            if gain>=cfg.min_gradient_gain:
                a=xy[int(np.argmin(proj))]; b=xy[int(np.argmax(proj))]
                candidates.append((res,{'kind':'linear','x1':float(a[0]),'y1':float(a[1]),'x2':float(b[0]),'y2':float(b[1]),'stops':stops,'gain':gain}))
    except np.linalg.LinAlgError: pass
    # Candidate 2: radial illumination centered on mean, bright focus, or dark focus.
    # Radial is used only if it lowers actual within-region RGB error sufficiently.
    if n>=max(60,cfg.min_gradient_pixels*2) and min(xs.max()-xs.min(),ys.max()-ys.min())>=8:
        luminance=colors@np.array([0.2126,0.7152,0.0722])
        rx=max(2.0,(float(xs.max())-float(xs.min()))/2.0); ry=max(2.0,(float(ys.max())-float(ys.min()))/2.0)
        centers=[xy0]
        for which in ['bright','dark']:
            q=np.quantile(luminance,0.72 if which=='bright' else 0.28)
            weights=np.maximum(luminance-q,0) if which=='bright' else np.maximum(q-luminance,0)
            if weights.sum()>1e-8: centers.append(np.average(xy,axis=0,weights=weights))
        # Separate brighter and darker lobes can sometimes center on the wrong object;
        # a few data-derived candidates are evaluated rather than assuming semantics.
        centers.extend([xy[np.argmax(luminance)],xy[np.argmin(luminance)]])
        unique=[]
        for center in centers:
            if all(np.linalg.norm(center-u)>1.0 for u in unique): unique.append(center)
        for center in unique:
            rad=np.sqrt(((xs-center[0])/rx)**2+((ys-center[1])/ry)**2)
            rmax=max(float(rad.max()),1e-6); t=rad/rmax
            stops,res=_binned_surface(colors,t,cfg.gradient_stops)
            gain=(total-res)/max(total,1e-9)
            if gain>=cfg.min_gradient_gain:
                spec={'kind':'radial','cx':float(center[0]),'cy':float(center[1]),'rx':rx*rmax,'ry':ry*rmax,'stops':stops,'gain':gain}
                candidates.append((res,spec))
    if not candidates:return None
    # Prefer a simple linear ramp when residuals are nearly tied; radial is selected
    # only when it has a meaningful fit advantage and region spans enough pixels.
    candidates.sort(key=lambda x:x[0]); best_error,best=candidates[0]
    linear=next((item for err,item in candidates if item['kind']=='linear'),None)
    if best['kind']=='radial' and linear is not None:
        linerr=next(err for err,item in candidates if item['kind']=='linear')
        if best_error >= linerr*0.92: best=linear
    return best


def _cell_edge_paths(labels: np.ndarray, label_id: int):
    """Trace contours on shared pixel-cell edges (integer coordinates), not pixel centers.

    Every border between two labels is the same geometric edge traversed in opposite
    directions. This prevents cracks when neighboring shapes are rendered without strokes.
    """
    h,w=labels.shape
    ys,xs=np.where(labels==label_id)
    if len(xs)==0:return [],0
    edges=[]
    for y,x in zip(ys.tolist(),xs.tolist()):
        if y==0 or labels[y-1,x]!=label_id: edges.append(((x,y),(x+1,y)))
        if x==w-1 or labels[y,x+1]!=label_id: edges.append(((x+1,y),(x+1,y+1)))
        if y==h-1 or labels[y+1,x]!=label_id: edges.append(((x+1,y+1),(x,y+1)))
        if x==0 or labels[y,x-1]!=label_id: edges.append(((x,y+1),(x,y)))
    outgoing={}
    for idx,(a,b) in enumerate(edges):outgoing.setdefault(a,[]).append(idx)
    unused=set(range(len(edges))); paths=[]
    # In image coordinates, E,S,W,N order is clockwise; keep the region on the right
    # at ambiguous diagonal-touch vertices by preferring right turn, straight, left, back.
    dir_code={(1,0):0,(0,1):1,(-1,0):2,(0,-1):3}
    while unused:
        first=min(unused); a,b=edges[first]; start=a; current=first; vertices=[a]
        guard=0
        while current in unused and guard<=len(edges)+4:
            unused.remove(current); edge_start,edge_end=edges[current]; vertices.append(edge_end)
            if edge_end==start:break
            candidates=[j for j in outgoing.get(edge_end,[]) if j in unused]
            if not candidates:break
            prev=(edge_end[0]-edge_start[0],edge_end[1]-edge_start[1]); pd=dir_code[prev]
            def rank(j):
                nxt=edges[j][1]; dv=(nxt[0]-edge_end[0],nxt[1]-edge_end[1]); nd=dir_code[dv]
                turn=(nd-pd)%4
                preference={1:0,0:1,3:2,2:3}
                return (preference[turn],nxt[1],nxt[0])
            current=min(candidates,key=rank);guard+=1
        if len(vertices)>=4 and vertices[-1]==vertices[0]:
            pts=vertices[:-1]
            # Remove collinear intermediate vertices to keep output compact without changing edges.
            compact=[]
            for i,pnt in enumerate(pts):
                prev=pts[(i-1)%len(pts)];nxt=pts[(i+1)%len(pts)]
                if (pnt[0]-prev[0])*(nxt[1]-pnt[1]) != (pnt[1]-prev[1])*(nxt[0]-pnt[0]):
                    compact.append(pnt)
            if len(compact)>=3:
                d=[f'M {compact[0][0]} {compact[0][1]}']
                d.extend(f'L {x} {y}' for x,y in compact[1:]);d.append('Z')
                paths.append(' '.join(d))
    return paths,len(edges)


def _contours_for_label(labels: np.ndarray, label_id: int, cfg: Config):
    # Internal boundaries remain exact/shared. The composite GrabCut silhouette is the
    # only boundary deliberately smoothed in this iteration.
    return _cell_edge_paths(labels,label_id)


def _region_moments(labels: np.ndarray, rgb: np.ndarray):
    """Additive moments for a quadratic RGB surface model in normalized image coordinates."""
    h, w = labels.shape
    ids = labels.ravel().astype(np.int64)
    nregions = int(ids.max()) + 1
    x = np.tile((np.arange(w, dtype=np.float64) - (w - 1) / 2.0) / max(1.0, w / 2.0), h)
    y = np.repeat((np.arange(h, dtype=np.float64) - (h - 1) / 2.0) / max(1.0, h / 2.0), w)
    cols = rgb.reshape(-1, 3).astype(np.float64)
    basis = np.column_stack([np.ones_like(x), x, y, x*x, x*y, y*y])
    counts = np.bincount(ids, minlength=nregions).astype(np.int64)
    stats = [{'n': int(counts[i]), 'gram': np.zeros((6,6),dtype=np.float64),
              'cross': np.zeros((6,3),dtype=np.float64), 'sum_sq': 0.0} for i in range(nregions)]
    def bc(v): return np.bincount(ids, weights=v, minlength=nregions).astype(np.float64)
    for i in range(6):
        for j in range(i,6):
            values=bc(basis[:,i]*basis[:,j])
            for k in range(nregions):
                stats[k]['gram'][i,j]=values[k]; stats[k]['gram'][j,i]=values[k]
        for c in range(3):
            values=bc(basis[:,i]*cols[:,c])
            for k in range(nregions): stats[k]['cross'][i,c]=values[k]
    sumsquares=bc(np.sum(cols*cols,axis=1))
    for k in range(nregions): stats[k]['sum_sq']=float(sumsquares[k])
    return stats


def _smooth_model_sse(st):
    """Residual SSE of a regularized 2D quadratic RGB surface fit for merge decisions."""
    if st['n'] <= 0: return 0.0
    gram=st['gram'].copy(); gram[1:,1:]+=np.eye(5)*1e-5
    try: coef=np.linalg.solve(gram,st['cross'])
    except np.linalg.LinAlgError: coef=np.linalg.pinv(gram)@st['cross']
    explained=float(np.sum(coef*st['cross']))
    return max(0.0,float(st['sum_sq'])-explained)


def _merge_superpixels(labels: np.ndarray, rgb: np.ndarray, lab: np.ndarray, target: int, boundary_weight: float, merge_threshold: float):
    """Agglomerate adjacent SLIC cells by model error + observed boundary strength.

    Region planes capture coherent shading. Boundary contrast protects likely object
    edges. The merge cost is normalized, deterministic, and only merges adjacent cells.
    """
    labels=np.asarray(labels,dtype=np.int32); nregions=int(labels.max())+1
    if nregions<=target: return labels, {'initial_regions':nregions,'final_regions':nregions,'merges':0}
    h,w=labels.shape
    adj=[{} for _ in range(nregions)]
    # Gather pixel-neighbor region pairs and their local perceptual edge difference.
    pairs_all=[]; delta_all=[]
    for a,b,la,lb in [(labels[:,:-1],labels[:,1:],lab[:,:-1],lab[:,1:]), (labels[:-1,:],labels[1:,:],lab[:-1,:],lab[1:,:])]:
        mask=a!=b
        if not np.any(mask): continue
        aa=a[mask].astype(np.int64); bb=b[mask].astype(np.int64)
        lo=np.minimum(aa,bb); hi=np.maximum(aa,bb)
        pairs_all.append(np.column_stack([lo,hi]))
        delta_all.append(np.linalg.norm(la[mask].astype(np.float32)-lb[mask].astype(np.float32),axis=1).astype(np.float64))
    if pairs_all:
        pairs=np.vstack(pairs_all); deltas=np.concatenate(delta_all)
        uniq, inv=np.unique(pairs,axis=0,return_inverse=True)
        lengths=np.bincount(inv,minlength=len(uniq)).astype(np.int64)
        sums=np.bincount(inv,weights=deltas,minlength=len(uniq)).astype(np.float64)
        for (a,b),length,total in zip(uniq,lengths,sums):
            a=int(a);b=int(b); value=(int(length),float(total))
            adj[a][b]=value; adj[b][a]=value
    stats=_region_moments(labels,rgb)
    active=set(range(nregions)); parent=list(range(nregions)); versions=[0]*nregions
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def cost(a,b,edge):
        merged_n=stats[a]['n']+stats[b]['n']
        combined={'n':merged_n,'gram':stats[a]['gram']+stats[b]['gram'],
                  'cross':stats[a]['cross']+stats[b]['cross'],'sum_sq':stats[a]['sum_sq']+stats[b]['sum_sq']}
        inc=max(0.0,_smooth_model_sse(combined)-_smooth_model_sse(stats[a])-_smooth_model_sse(stats[b]))
        model=inc/max(1,merged_n*3*255.0*255.0)
        edge_mean=edge[1]/max(1,edge[0])
        edge_cost=boundary_weight*(min(edge_mean,180.0)/100.0)**2
        # Small regions get merged slightly earlier unless their boundary is very strong.
        size_bias=0.00015/max(1.0,np.sqrt(merged_n))
        return model+edge_cost+size_bias
    import heapq
    heap=[]
    def push(a,b):
        if a==b or a not in active or b not in active or b not in adj[a]: return
        if a>b:a,b=b,a
        heapq.heappush(heap,(cost(a,b,adj[a][b]),a,b,versions[a],versions[b]))
    for a in range(nregions):
        for b in adj[a]:
            if a<b: push(a,b)
    merges=0
    while len(active)>max(1,target) and heap:
        c,a,b,va,vb=heapq.heappop(heap)
        if a not in active or b not in active or versions[a]!=va or versions[b]!=vb or b not in adj[a]: continue
        if c > merge_threshold:
            break
        # Stable lower ID remains the merged region identity.
        root,other=(a,b) if a<b else (b,a)
        parent[other]=root
        active.remove(other); merges+=1
        # Merge sufficient statistics and adjacency evidence.
        stats[root]['n'] += stats[other]['n']
        stats[root]['gram'] += stats[other]['gram']
        stats[root]['cross'] += stats[other]['cross']
        stats[root]['sum_sq'] += stats[other]['sum_sq']
        neighbors=set(adj[root])|set(adj[other]); neighbors.discard(root); neighbors.discard(other)
        adj[root].pop(other,None); adj[other].pop(root,None)
        for nb in list(neighbors):
            ev1=adj[root].pop(nb,None); ev2=adj[other].pop(nb,None)
            adj[nb].pop(root,None); adj[nb].pop(other,None)
            if ev1 and ev2: edge=(ev1[0]+ev2[0],ev1[1]+ev2[1])
            elif ev1: edge=ev1
            else: edge=ev2
            if edge:
                adj[root][nb]=edge; adj[nb][root]=edge
        adj[other].clear(); versions[root]+=1
        # Neighbor-region colors/statistics did not change, so their other heap costs remain valid.
        # Only costs touching root need a refreshed entry because root statistics changed.
        for nb in adj[root]: push(root,nb)
    remap={}
    for i in range(nregions):
        r=find(i)
        if r in active and r not in remap: remap[r]=len(remap)
    lut=np.zeros(nregions,dtype=np.int32)
    for i in range(nregions): lut[i]=remap[find(i)]
    final=lut[labels]
    return final, {'initial_regions':nregions,'final_regions':len(active),'merges':merges}


def _foreground_silhouette(rgb: np.ndarray, cfg: Config):
    """Estimate a coarse composite foreground mask, then smooth only its outer boundary.

    GrabCut is used as a lightweight CPU segmentation prior, not as a semantic layer model.
    Its mask clips region fills to a coherent outer silhouette; internal region boundaries
    stay as the region model because independently smoothing every boundary makes gaps.
    """
    h,w=rgb.shape[:2]
    bgr=cv2.cvtColor(rgb,cv2.COLOR_RGB2BGR)
    mask=np.zeros((h,w),dtype=np.uint8)
    x=max(1,int(w*0.025)); y=max(1,int(h*0.025))
    rect=(x,y,max(2,w-2*x),max(2,h-2*y))
    bg_model=np.zeros((1,65),dtype=np.float64); fg_model=np.zeros((1,65),dtype=np.float64)
    try:
        cv2.setRNGSeed(0)  # reproducible GrabCut GMM initialization
        cv2.grabCut(bgr,mask,rect,bg_model,fg_model,3,cv2.GC_INIT_WITH_RECT)
        fg=((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD)).astype(np.uint8)
        # Close only one-pixel breaks in the overall silhouette; do not blur its color layers.
        fg=cv2.morphologyEx(fg,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8),iterations=1)
        # Keep small detached foreground details (e.g. letters/sparks), but eliminate isolated noise.
        count,lab,stats,_=cv2.connectedComponentsWithStats(fg,8)
        cleaned=np.zeros_like(fg)
        min_area=max(2,int(h*w*0.00001))
        for i in range(1,count):
            if stats[i,cv2.CC_STAT_AREA]>=min_area: cleaned[lab==i]=1
        if int(cleaned.sum())<h*w*0.005 or int(cleaned.sum())>h*w*0.97:
            return None, {'grabcut_used':False,'reason':'foreground mask degenerate'}
        fg=cleaned
    except cv2.error as exc:
        return None, {'grabcut_used':False,'reason':f'GrabCut failed: {exc}'}
    contours,hierarchy=cv2.findContours(fg,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)
    if hierarchy is None:return None, {'grabcut_used':False,'reason':'no foreground contours'}
    paths=[]; segcount=0
    for cont in contours:
        if abs(cv2.contourArea(cont))<2:continue
        perimeter=cv2.arcLength(cont,True)
        eps=max(1.0,min(cfg.contour_epsilon_px*2.0,perimeter*0.02))
        approx=cv2.approxPolyDP(cont,eps,True).reshape(-1,2)
        d,nseg=_curve_path(approx,turn_degrees=cfg.corner_turn_degrees)
        if d:paths.append(d);segcount+=nseg
    if not paths:return None, {'grabcut_used':False,'reason':'all contours degenerate'}
    return ' '.join(paths), {'grabcut_used':True,'foreground_pixels':int(fg.sum()),'foreground_fraction':float(fg.mean()),'silhouette_contours':len(paths),'silhouette_cubic_segments':segcount}


def estimate_target_regions(rgb: np.ndarray, min_regions: int = 220, max_regions: int = 560) -> tuple[int, dict]:
    """Allocate more regions to spatially distributed texture than to flat/logo artwork.

    A grid-coverage term avoids interpreting a small block of high-contrast calligraphy
    as photographic texture. This is a complexity heuristic, not a semantic classifier.
    """
    gray=cv2.cvtColor(rgb,cv2.COLOR_RGB2GRAY)
    edge=(cv2.Canny(gray,80,160)>0)
    h,w=gray.shape; edge_density=float(edge.mean())
    cell=32; cover=[]
    for y in range(0,h,cell):
        for x in range(0,w,cell):
            tile=edge[y:min(h,y+cell),x:min(w,x+cell)]
            cover.append(float(tile.mean()) if tile.size else 0.0)
    grid_coverage=float(np.mean(np.asarray(cover)>0.02)) if cover else 0.0
    # Dense edges spread throughout the frame indicate textured photographic material.
    score=edge_density*grid_coverage
    lo,hi=0.035,0.18
    factor=float(np.clip((score-lo)/(hi-lo),0,1))
    target=int(round(min_regions+factor*(max_regions-min_regions)))
    return target, {'edge_density':edge_density,'edge_grid_coverage':grid_coverage,'texture_complexity_score':score,'adaptive_target_regions':target}


class Challenger:
    def __init__(self, config: Config | None = None):
        self.config = config or Config()

    def vectorize(self, source: str | Path | np.ndarray):
        start = time.perf_counter()
        if isinstance(source, (str, Path)):
            rgb = np.asarray(Image.open(source).convert('RGB'), dtype=np.uint8)
            source_name = Path(source).name
        else:
            rgb = np.asarray(source, dtype=np.uint8)
            source_name = '<array>'
        if rgb.ndim != 3 or rgb.shape[2] != 3 or min(rgb.shape[:2]) < 2:
            raise ValueError('source must be an RGB image with at least 2x2 pixels')
        h, w = rgb.shape[:2]
        if max(h, w) > self.config.max_dimension:
            raise ValueError(f'image dimension exceeds configured limit {self.config.max_dimension}')
        # SLIC on a lightly edge-preserving source: avoid smoothing away small meaningful contours.
        bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
        filtered = cv2.bilateralFilter(bgr, d=5, sigmaColor=14, sigmaSpace=3)
        filtered = cv2.cvtColor(filtered, cv2.COLOR_BGR2RGB)
        slic_labels = slic(filtered.astype(np.float32) / 255.0,
                           n_segments=self.config.initial_segments,
                           compactness=self.config.compactness,
                           sigma=self.config.sigma,
                           convert2lab=True,
                           enforce_connectivity=True,
                           start_label=0,
                           channel_axis=2).astype(np.int32)
        lab_img = cv2.cvtColor(rgb, cv2.COLOR_RGB2LAB)
        labels, merge_info = _merge_superpixels(slic_labels, rgb, lab_img, self.config.target_regions, self.config.boundary_weight, self.config.merge_threshold)
        label_ids, counts = np.unique(labels, return_counts=True)
        # Coherent coarse foreground contour used for clipping. Region boundaries themselves
        # are NOT individually clipped into their own smoothed silhouette, preventing the
        # old edge-stencil behavior and reducing cracks along the outside shape.
        silhouette_d, silhouette_meta = _foreground_silhouette(rgb, self.config)
        # Large regions go first, small details last; this reduces holes/seams when curves simplify.
        order = sorted([(int(n), int(i)) for i, n in zip(label_ids, counts)], reverse=True)
        defs, body = [], []
        gradient_count = 0; path_count = 0; region_boundary_segments = 0; dropped = 0
        total_regions = len(order)
        for region_order, (pixel_count, label_id) in enumerate(order):
            region_mask = labels == label_id
            paths, segment_count = _contours_for_label(labels, label_id, self.config)
            if not paths:
                dropped += 1; continue
            # SLIC labels are usually connected; if there are multiple loops, use evenodd.
            d = ' '.join(paths)
            grad = _fit_region_gradient(rgb, region_mask, self.config)
            fill_attr = _rgb_hex(rgb[region_mask].mean(axis=0))
            if grad is not None:
                gid = f'grad_{label_id}'
                stops = ''.join(f'<stop offset="{off*100:.2f}%" stop-color="{color}"/>' for off, color in grad['stops'])
                if grad['kind']=='radial':
                    transform=f'matrix({grad["rx"]:.3f} 0 0 {grad["ry"]:.3f} {grad["cx"]:.3f} {grad["cy"]:.3f})'
                    defs.append(f'<radialGradient id="{gid}" gradientUnits="userSpaceOnUse" cx="0" cy="0" r="1" gradientTransform="{transform}">{stops}</radialGradient>')
                else:
                    defs.append(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{grad["x1"]:.3f}" y1="{grad["y1"]:.3f}" x2="{grad["x2"]:.3f}" y2="{grad["y2"]:.3f}">{stops}</linearGradient>')
                fill_attr = f'url(#{gid})'; gradient_count += 1
            # Use the region's representative color for the tiny seam-hiding stroke.
            # Stroking with a transformed radial gradient can create pale/transparent halos.
            stroke_color=_rgb_hex(rgb[region_mask].mean(axis=0))
            stroke = f' stroke="{stroke_color}" stroke-opacity="{self.config.seam_stroke_opacity:.3f}" stroke-width="{self.config.seam_stroke_px:.2f}" stroke-linejoin="round"' if self.config.seam_stroke_px > 0 else ''
            fillrule = ' fill-rule="evenodd"' if len(paths) > 1 else ''
            body.append(f'<path id="region_{label_id}" data-region-size="{pixel_count}" fill="{fill_attr}"{fillrule}{stroke} d="{d}"/>')
            path_count += 1; region_boundary_segments += segment_count
        # Reuse the same region/color model under complementary foreground/background clip paths.
        # This gives the composite a smooth coherent outer silhouette while maintaining a full
        # vector background and preserving the source's broad shadow/background variation.
        clip_defs=''
        region_markup=''.join(body)
        if silhouette_d is not None:
            clip_defs=(f'<clipPath id="foregroundClip"><path fill-rule="evenodd" d="{silhouette_d}"/></clipPath>'
                       f'<clipPath id="backgroundClip"><path fill-rule="evenodd" d="M0 0H{w}V{h}H0Z {silhouette_d}"/></clipPath>')
            bg_markup=region_markup.replace('id="region_','id="bg_region_')
            fg_markup=region_markup.replace('id="region_','id="fg_region_')
            scene=(f'<g id="background-appearance" clip-path="url(#backgroundClip)" shape-rendering="geometricPrecision">{bg_markup}</g>'
                   f'<g id="foreground-base-and-lighting" clip-path="url(#foregroundClip)" shape-rendering="geometricPrecision">{fg_markup}</g>')
        else:
            scene=f'<g id="reconstructed-regions" shape-rendering="geometricPrecision">{region_markup}</g>'
        defs_str = '<defs>' + ''.join(defs) + clip_defs + '</defs>' if defs or clip_defs else ''
        border_rgb=np.concatenate([rgb[0],rgb[-1],rgb[:,0],rgb[:,-1]],axis=0).mean(axis=0)
        background=f'<rect id="fallback-background" x="0" y="0" width="{w}" height="{h}" fill="{_rgb_hex(border_rgb)}"/>'
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" version="1.1">'
               '<title>V04 smooth region reconstruction</title>'
               '<desc>Boundary-aware merged regions with cubic contours and local linear/radial gradients. A coarse GrabCut silhouette clip separates composite foreground appearance from background. Pure vector output; no embedded raster or source-edge pixel stencil. Not semantic object/shadow/highlight recovery.</desc>'
               + defs_str + background + scene + '</svg>')
        root = ET.fromstring(svg)
        ns = {'s': 'http://www.w3.org/2000/svg'}
        metrics = {
            'source': source_name, 'width': w, 'height': h,
            'initial_slic_segments': self.config.initial_segments,
            'target_regions': self.config.target_regions,
            'initial_regions': merge_info['initial_regions'], 'merge_count': merge_info['merges'],
            'actual_regions': total_regions, 'emitted_paths': path_count,
            'region_boundary_segments': region_boundary_segments, 'gradient_count': gradient_count, 'linear_gradient_count':sum(1 for d in defs if '<linearGradient' in d), 'radial_gradient_count':sum(1 for d in defs if '<radialGradient' in d), 'silhouette_cubic_segments':silhouette_meta.get('silhouette_cubic_segments',0),
            'dropped_tiny_or_invalid_regions': dropped, 'silhouette':silhouette_meta,
            'embedded_raster_images': len(root.findall('.//s:image', ns)),
            'svg_bytes': len(svg.encode('utf-8')),
            'generation_ms': round((time.perf_counter() - start) * 1000, 3),
            'method': 'SLIC regions + simplified closed contours + cubic curves + local multi-stop gradients; no edge pixel stencil',
            'config': asdict(self.config),
        }
        return svg, metrics


def render_svg(svg_path: str | Path, png_path: str | Path, width: int, height: int, inkscape: str='inkscape') -> float:
    import subprocess
    start = time.perf_counter()
    args = [inkscape, str(svg_path), '--export-type=png', f'--export-filename={png_path}', f'--export-width={width}', f'--export-height={height}']
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=90)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f'Inkscape render timeout: {svg_path}') from exc
    if proc.returncode:
        raise RuntimeError(f'Inkscape failed for {svg_path}: {proc.stderr[-1000:]}')
    im = Image.open(png_path)
    if im.size != (width, height):
        raise RuntimeError(f'Wrong render dimensions for {png_path}: {im.size}, expected {(width, height)}')
    return (time.perf_counter() - start) * 1000
