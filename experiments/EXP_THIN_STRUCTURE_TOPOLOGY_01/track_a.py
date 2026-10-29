"""Source-supported local reconnection of frozen labels; no truth or case-name input."""
# START CHANGE AGD-THIN-TRACK-A | 2026-10-29T11:31:15Z | EDITED | Author: package_generalization
from __future__ import annotations
import heapq,math,time
import numpy as np
from scipy import ndimage
from scipy.spatial import cKDTree
from skimage.color import rgb2lab
from skimage.morphology import skeletonize

DEFAULT_CONFIG={
 'version':'endpoint_color_geodesic_v1','skeleton_connectivity':8,'endpoint_degree':1,
 'endpoint_tangent_steps':3,'max_endpoint_radius_px':2.0,'max_pair_distance_px':12.0,
 'max_path_steps':12,'max_new_connector_pixels':12,'max_bridges':32,
 'max_label_lab_distance':12.0,'min_facing_cosine':.75,'max_endpoint_width_ratio':2.5,
 'radius_floor_px':.5,'corridor_radius_px':1.5,'min_fg_bg_lab_contrast':15.0,
 'min_mixture_fraction':.15,'max_mixture_residual_lab':8.0,'min_mean_mixture_fraction':.35,
 'background_flank_min_px':1.5,'background_flank_max_px':3.5,'background_min_samples':3,
 'common_gap_label_required':True,'original_adjacent_pair_forbidden':True,'max_endpoint_pairs':512}

def _region_endpoints(labels):
    """Find short-radius skeleton endpoints and inward/outward local directions."""
    # Dense row-major IDs prevent huge allocations for sparse arbitrary label IDs.
    ids,dense=np.unique(labels,return_inverse=True);dense=dense.reshape(labels.shape)+1
    boxes=ndimage.find_objects(dense);endpoints=[]
    for code,box in enumerate(boxes,1):
        if box is None:continue
        local=dense[box]==code
        # Pad explicitly: tight bounding boxes must not be treated as foreground
        # continuing outside the array by either thinning or distance transform.
        padded=np.pad(local,1,constant_values=False)
        skel=skeletonize(padded)[1:-1,1:-1];radius=ndimage.distance_transform_edt(padded)[1:-1,1:-1]
        degree=ndimage.convolve(skel.astype(np.uint8),np.ones((3,3),np.uint8),mode='constant')-skel
        for y,x in np.argwhere(skel&(degree==1)):
            start=(int(y),int(x));previous=None;point=start
            for _ in range(3):
                neighbors=[]
                for dy in (-1,0,1):
                    for dx in (-1,0,1):
                        q=(point[0]+dy,point[1]+dx)
                        if (dy or dx) and 0<=q[0]<skel.shape[0] and 0<=q[1]<skel.shape[1] and skel[q] and q!=previous:neighbors.append(q)
                if len(neighbors)!=1:break
                previous,point=point,neighbors[0]
            delta=np.array([start[1]-point[1],start[0]-point[0]],float);length=float(np.linalg.norm(delta))
            if length<1e-9:continue
            endpoints.append({'label':int(ids[code-1]),'y':start[0]+box[0].start,'x':start[1]+box[1].start,'radius':float(radius[start]),'outward':delta/length})
    return endpoints

def _adjacent_pairs(labels):
    pairs=set()
    for a,b in ((labels[:-1],labels[1:]),(labels[:,:-1],labels[:,1:])):
        mask=a!=b
        if mask.any():pairs.update(map(tuple,np.unique(np.sort(np.column_stack((a[mask],b[mask])),axis=1),axis=0)))
    return pairs

def _neighbor_labels(labels,endpoint):
    y,x=endpoint['y'],endpoint['x'];h,w=labels.shape
    return {int(labels[yy,xx]) for yy,xx in ((y-1,x),(y+1,x),(y,x-1),(y,x+1)) if 0<=yy<h and 0<=xx<w}

def _segment_distance(xx,yy,a,b):
    vx,vy=b['x']-a['x'],b['y']-a['y'];den=vx*vx+vy*vy
    t=np.clip(((xx-a['x'])*vx+(yy-a['y'])*vy)/den,0,1)
    return np.hypot(xx-(a['x']+t*vx),yy-(a['y']+t*vy))

def _path_for_pair(rgb_lab,labels,a,b,gap,fg,cfg):
    """Bounded four-neighbor Dijkstra with a source-color mixture support gate."""
    h,w=labels.shape;margin=4
    x0=max(0,min(a['x'],b['x'])-margin);x1=min(w,max(a['x'],b['x'])+margin+1)
    y0=max(0,min(a['y'],b['y'])-margin);y1=min(h,max(a['y'],b['y'])+margin+1)
    yy,xx=np.mgrid[y0:y1,x0:x1];distance=_segment_distance(xx,yy,a,b);region=labels[y0:y1,x0:x1]
    flank=(region==gap)&(distance>=cfg['background_flank_min_px'])&(distance<=cfg['background_flank_max_px'])
    if int(flank.sum())<cfg['background_min_samples']:return None,'background_support'
    bg=np.median(rgb_lab[y0:y1,x0:x1][flank],axis=0);axis=fg-bg;contrast=float(np.linalg.norm(axis))
    if contrast<cfg['min_fg_bg_lab_contrast']:return None,'low_contrast'
    colors=rgb_lab[y0:y1,x0:x1]
    raw_fraction=np.sum((colors-bg)*axis,axis=2)/(contrast*contrast)
    fraction=np.clip(raw_fraction,0.,1.)
    residual=np.linalg.norm(colors-(bg+fraction[...,None]*axis),axis=2)
    valid=(distance<=cfg['corridor_radius_px'])&np.isin(region,[a['label'],b['label'],gap])
    valid&=(fraction>=cfg['min_mixture_fraction'])&(residual<=cfg['max_mixture_residual_lab'])
    start=(a['y']-y0,a['x']-x0);end=(b['y']-y0,b['x']-x0)
    if not valid[start] or not valid[end]:return None,'unsupported_endpoint'
    cost=1+2*(1-np.clip(fraction,0,1))+residual/cfg['max_mixture_residual_lab']
    queue=[(0.,0,start[0],start[1])];best={(start[0],start[1],0):0.};parents={};found=None
    while queue:
        score,steps,y,x=heapq.heappop(queue);state=(y,x,steps)
        if score!=best.get(state):continue
        if (y,x)==end:found=state;break
        if steps>=cfg['max_path_steps']:continue
        for dy,dx in ((-1,0),(0,-1),(0,1),(1,0)):
            ny,nx=y+dy,x+dx
            if not(0<=ny<valid.shape[0] and 0<=nx<valid.shape[1] and valid[ny,nx]):continue
            nxt=(ny,nx,steps+1);candidate=score+float(cost[ny,nx])
            if candidate<best.get(nxt,float('inf')):
                best[nxt]=candidate;parents[nxt]=state;heapq.heappush(queue,(candidate,steps+1,ny,nx))
    if found is None:return None,'no_source_supported_path'
    cells=[];state=found
    while True:
        cells.append((state[0]+y0,state[1]+x0))
        if state==(start[0],start[1],0):break
        state=parents[state]
    cells.reverse();new=[(y,x) for y,x in cells if labels[y,x]==gap]
    if not new or len(new)>cfg['max_new_connector_pixels']:return None,'connector_budget'
    mean=float(np.mean([fraction[y-y0,x-x0] for y,x in new]))
    if mean<cfg['min_mean_mixture_fraction']:return None,'weak_mean_support'
    return {'path':cells,'connector':new,'cost':best[found],'mean_mixture_fraction':mean,
       'min_mixture_fraction':float(min(fraction[y-y0,x-x0] for y,x in new)),
       'max_mixture_residual_lab':float(max(residual[y-y0,x-x0] for y,x in new)),'gap_label':int(gap),
       'foreground_lab':fg.tolist(),'background_lab':bg.tolist(),'endpoint_a':[a['x'],a['y']],'endpoint_b':[b['x'],b['y']],
       'labels':[a['label'],b['label']]},None

def discover(rgb,labels,config=None):
    """Return repaired labels/audit/evidence; absent source confidence is unchanged.

    No reference, image ID, annotation, geometric initializer or fallback is read.
    All topology changes are explicit label merges with narrow connector pixels.
    """
    started=time.perf_counter();cfg=dict(DEFAULT_CONFIG)
    if config:
        unknown=set(config)-set(cfg)
        if unknown:raise ValueError('Unknown Track A config fields: '+str(sorted(unknown)))
        cfg.update(config)
    if cfg['endpoint_tangent_steps']!=3 or cfg['skeleton_connectivity']!=8 or cfg['endpoint_degree']!=1:raise ValueError('Unsupported algorithm variant; fixed v1 endpoint definition')
    rgb=np.asarray(rgb);labels=np.asarray(labels)
    if rgb.ndim!=3 or rgb.shape[2]!=3 or labels.shape!=rgb.shape[:2] or labels.ndim!=2 or not np.issubdtype(labels.dtype,np.integer) or labels.min()<1:raise ValueError('Require RGB HxWx3 and positive integer HxW labels')
    lab=rgb2lab(rgb.astype(float)/255.);ids,inverse=np.unique(labels,return_inverse=True)
    inverse=inverse.ravel();count=np.bincount(inverse);means=np.column_stack([np.bincount(inverse,weights=lab[:,:,i].ravel())/count for i in range(3)])
    prototypes={int(key):mean for key,mean in zip(ids,means)}
    endpoints=[e for e in _region_endpoints(labels) if e['radius']<=cfg['max_endpoint_radius_px']]
    adjacency=_adjacent_pairs(labels);reject={};proposals=[];tested=0
    def rejected(reason):reject[reason]=reject.get(reason,0)+1
    pairs=[];pairs_available=0
    if len(endpoints)>=2:
        points=np.array([[p['x'],p['y']] for p in endpoints]);pairs=list(cKDTree(points).query_pairs(cfg['max_pair_distance_px']))
        pairs.sort(key=lambda ij:(float(np.linalg.norm(points[ij[0]]-points[ij[1]])),min(endpoints[ij[0]]['label'],endpoints[ij[1]]['label']),max(endpoints[ij[0]]['label'],endpoints[ij[1]]['label']),endpoints[ij[0]]['y'],endpoints[ij[0]]['x'],endpoints[ij[1]]['y'],endpoints[ij[1]]['x']))
        pairs_available=len(pairs);pairs=pairs[:cfg['max_endpoint_pairs']]
    for i,j in pairs:
        a,b=endpoints[i],endpoints[j];tested+=1
        if a['label']==b['label']:rejected('same_label');continue
        key=tuple(sorted((a['label'],b['label'])))
        if key in adjacency:rejected('already_four_adjacent');continue
        if np.linalg.norm(prototypes[a['label']]-prototypes[b['label']])>cfg['max_label_lab_distance']:rejected('incompatible_color');continue
        vector=np.array([b['x']-a['x'],b['y']-a['y']],float);length=float(np.linalg.norm(vector))
        if not length:rejected('same_point');continue
        direction=vector/length
        if min(float(a['outward']@direction),float(b['outward']@(-direction)))<cfg['min_facing_cosine']:rejected('tangent');continue
        widths=[max(e['radius'],cfg['radius_floor_px']) for e in (a,b)]
        if max(widths)/min(widths)>cfg['max_endpoint_width_ratio']:rejected('width');continue
        gaps=(_neighbor_labels(labels,a)&_neighbor_labels(labels,b))-{a['label'],b['label']}
        if not gaps:rejected('no_common_gap_label');continue
        for gap in sorted(gaps):
            proposal,reason=_path_for_pair(lab,labels,a,b,gap,(prototypes[a['label']]+prototypes[b['label']])/2,cfg)
            if reason:rejected(reason)
            else:proposals.append(proposal)
    proposals.sort(key=lambda p:(p['cost'],len(p['connector']),min(p['labels']),max(p['labels']),p['endpoint_a'][1],p['endpoint_a'][0],p['endpoint_b'][1],p['endpoint_b'][0]))
    parent={int(i):int(i) for i in ids};output=labels.copy();connector_mask=np.zeros(labels.shape,bool);accepted=[]
    def representative(a):
        while parent[a]!=a:a=parent[a]
        return a
    for proposal in proposals:
        if len(accepted)>=cfg['max_bridges']:break
        a,b=map(representative,proposal['labels']);gap=representative(proposal['gap_label'])
        if a==b or gap in (a,b):rejected('merge_conflict');continue
        if any(connector_mask[y,x] or representative(int(labels[y,x]))!=gap for y,x in proposal['connector']):rejected('connector_conflict');continue
        # A newly adjacent pair no longer needs a connection; never globally erase
        # an existing interface merely to reduce label count.
        neighbors=_adjacent_pairs(output)
        if tuple(sorted((a,b))) in neighbors:rejected('became_adjacent');continue
        target=min(a,b);other=max(a,b);parent[other]=target
        output[output==other]=target
        for y,x in proposal['connector']:output[y,x]=target;connector_mask[y,x]=True
        accepted.append(proposal|{'merged_to':target,'merged_from':other})
    # Relabel IDs without changing membership; number of regions can only fall.
    if accepted:
        _,dense=np.unique(output,return_inverse=True);output=dense.reshape(labels.shape).astype(np.uint32)+1
    audit={'config':cfg,'algorithm':'source-supported endpoint color geodesic bridge','endpoints':len(endpoints),'endpoint_pairs_tested':tested,
      'source_supported_proposals':len(proposals),'accepted_bridges':len(accepted),'connector_pixels':int(connector_mask.sum()),
      'input_regions':len(ids),'output_regions':len(np.unique(output)),'rejections':reject,'bridges':accepted,
      'endpoint_pairs_available':pairs_available,'endpoint_pairs_truncated':max(0,pairs_available-len(pairs)),
      'status':'LOCAL_SOURCE_SUPPORTED_EDITS' if accepted else 'UNCHANGED_NO_CONFIDENT_PROPOSAL','wall_seconds':time.perf_counter()-started,
      'limitations':['Convex Lab two-color mixture (projection clipped0..1) is heuristic evidence, not physical boundary truth.','Only joins existing nonadjacent compatible regions; cannot discover a wholly absent region/band.','One-pixel connector ownership can introduce width error; unchanged inherited initializer may still collapse geometry.','Merging region identities can falsely join distinct same-colored structures; source/tangent/width gates are controls, not proof.','No claim of correct semantics, topology, fidelity, or generalization.'],
      'reference_or_case_name_used':False,'initializer_changed':False,'new_region_ids_added':False}
    return output,audit,{'connector_mask':connector_mask.astype(np.uint8),'endpoint_coordinates_xy':np.array([[e['x'],e['y']] for e in endpoints],dtype=np.int32).reshape(-1,2)}
# END CHANGE AGD-THIN-TRACK-A | 2026-10-29T11:31:15Z | EDITED | Author: package_generalization
