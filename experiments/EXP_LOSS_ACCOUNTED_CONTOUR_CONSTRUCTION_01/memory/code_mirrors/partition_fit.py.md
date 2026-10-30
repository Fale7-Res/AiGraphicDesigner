# مرآة الكود التفصيلية: `partition_fit.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `partition_fit.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `partition_fit.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `186` (`Lines 1–186`)
- **بصمة الملف (`SHA-256`):** `b87073967a8ebcaa6e969e1ad34f751660fcdd5009519593b0fc289909be8fbb`
- **الوصف التفصيلي:** # START CHANGE AGD-LOSS-CONTOUR-PARTITION | 2026-10-30T08:37:34Z | CREATED | Author: contour_partition

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `signed_area` | `function` | `Lines 21–23` | `def signed_area(points):` | رمز برمجي موثق. |
| `flattened` | `function` | `Lines 26–27` | `def flattened(curves):` | رمز برمجي موثق. |
| `source_partitions` | `function` | `Lines 30–62` | `def source_partitions(points):` | Source-index cuts preserve anchors, with disjoint edge intervals [lo, hi). |
| `periodic_handles` | `function` | `Lines 65–94` | `def periodic_handles(points, intervals, candidates, corners):` | Closed raw loop: match directional tangents at smooth partition junctions. |
| `construct` | `function` | `Lines 97–180` | `def construct(points, condition="Q", deadline=None, maximum_trace_cubics=TRACE_CUBICS):` | Return accepted chains + exhaustive original-edge ledger for one trace. |
| `construct.rejected_all` | `nested_function` | `Lines 108–109` | `def rejected_all(reason):` | رمز برمجي موثق. |
| `fit_trace` | `function` | `Lines 183–185` | `def fit_trace(points, periodic=False, deadline=None, maximum_trace_cubics=TRACE_CUBICS):` | Caller-facing alias: periodic False=P and True=Q; no case/image inputs. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `signed_area` — `Lines 21–23`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `21` إلى السطر `23` (`Lines 21–23`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 21–23`):**
```python
def signed_area(points):
    p = np.asarray(points, float)
    return float(np.sum(p[:-1, 0]*p[1:, 1]-p[1:, 0]*p[:-1, 1])/2)
```

### `flattened` — `Lines 26–27`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `26` إلى السطر `27` (`Lines 26–27`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 26–27`):**
```python
def flattened(curves):
    return np.concatenate([flatten(c)[:-1] for c in curves]+[curves[-1, -1:]])
```

### `source_partitions` — `Lines 30–62`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `30` إلى السطر `62` (`Lines 30–62`)
- **الوظيفة:** Source-index cuts preserve anchors, with disjoint edge intervals [lo, hi).
- **الكود الفعلي (`Lines 30–62`):**
```python
def source_partitions(points):
    """Source-index cuts preserve anchors, with disjoint edge intervals [lo, hi)."""
    p = np.asarray(points, float)
    lengths = np.linalg.norm(np.diff(p, axis=0), axis=1)
    units = np.diff(p, axis=0)/lengths[:, None]
    turns = np.zeros(len(p))
    if len(units)>1:
        turns[1:-1] = np.degrees(np.arccos(np.clip(np.sum(units[:-1]*units[1:], axis=1), -1, 1)))
    # Apply curvature to a source-only RDP support, avoiding skeleton stair-step
    # oscillations acting as one-pixel corner anchors. Raw vertices remain ledger.
    import cv2
    support = cv2.approxPolyDP(p.astype(np.float32).reshape(-1,1,2), .35, False).reshape(-1,2)
    ids=[]; prior=-1
    for v in support:
        remain=np.arange(prior+1,len(p))
        idx=int(remain[np.argmin(np.linalg.norm(p[remain]-v,axis=1))]);ids.append(idx);prior=idx
    significant={}
    for j in range(1,len(ids)-1):
        a,b,c=p[ids[j-1]],p[ids[j]],p[ids[j+1]]
        u,v=b-a,c-b
        angle=math.degrees(math.acos(float(np.clip(u@v/(np.linalg.norm(u)*np.linalg.norm(v)), -1,1))))
        significant[ids[j]]=angle
    cuts=[0];arc=0.;turn=0.
    for i in range(1,len(p)):
        # Cut before an edge would exceed arc budget, keeping source endpoints.
        if arc+lengths[i-1]>MAX_ARC and i-1>cuts[-1]:
            cuts.append(i-1);arc=0.;turn=0.
        arc+=lengths[i-1]
        turn+=significant.get(i,0.)
        if i<len(p)-1 and (significant.get(i,0.)>=CORNER or turn>=TURN_BUDGET):
            cuts.append(i);arc=0.;turn=0.
    if cuts[-1]!=len(p)-1:cuts.append(len(p)-1)
    return [(a,b) for a,b in zip(cuts[:-1],cuts[1:])], significant
```

### `periodic_handles` — `Lines 65–94`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `65` إلى السطر `94` (`Lines 65–94`)
- **الوظيفة:** Closed raw loop: match directional tangents at smooth partition junctions.
- **الكود الفعلي (`Lines 65–94`):**
```python
def periodic_handles(points, intervals, candidates, corners):
    """Closed raw loop: match directional tangents at smooth partition junctions.

    Exact corners >=60deg retain independent one-sided handles. Endpoint locations
    remain identical. Each resulting partition is revalidated before acceptance.
    """
    p=np.asarray(points,float);n=len(p)-1
    joins=[]
    for j in range(len(intervals)):
        previous=(j-1)%len(intervals);k=intervals[j][0]
        row=dict(source_index=k,previous_partition=previous,next_partition=j)
        joins.append(row)
        if candidates[j] is None or candidates[previous] is None:
            row['status']='unavailable_partition';continue
        if corners.get(k,0.)>=CORNER:
            row['status']='intentional_corner_preserved';continue
        # Tangents from immediate source chords. Sharp raster turns preserved;
        # no image-specific smoothing, guessed seam or invented closure.
        left=p[k]-p[(k-1)%n];right=p[(k+1)%n]-p[k]
        left/=np.linalg.norm(left);right/=np.linalg.norm(right)
        angle=math.degrees(math.acos(float(np.clip(left@right,-1,1))))
        if angle>=CORNER:
            row.update(status='source_local_corner_preserved',source_turn_degrees=angle);continue
        direction=left+right;direction/=np.linalg.norm(direction)
        before,after=candidates[previous],candidates[j]
        span=min(np.linalg.norm(before[-1,3]-before[-1,0]),np.linalg.norm(after[0,3]-after[0,0]))/3
        before[-1,2]=p[k]-direction*span
        after[0,1]=p[k]+direction*span
        row.update(status='periodic_handles_proposed',source_turn_degrees=angle,handle_length_px=float(span))
    return joins
```

### `construct` — `Lines 97–180`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `97` إلى السطر `180` (`Lines 97–180`)
- **الوظيفة:** Return accepted chains + exhaustive original-edge ledger for one trace.
- **الكود الفعلي (`Lines 97–180`):**
```python
def construct(points, condition="Q", deadline=None, maximum_trace_cubics=TRACE_CUBICS):
    """Return accepted chains + exhaustive original-edge ledger for one trace.

    deadline is caller's absolute monotonic arm budget. No proposal-count cap.
    Source edge >32px is reported, never silently interpolated into grid geometry.
    """
    started=time.monotonic();p=np.asarray(points,float)
    if condition not in ("P","Q"):raise ValueError("condition must be P or Q")
    if p.ndim!=2 or p.shape[1]!=2 or len(p)<2 or not np.isfinite(p).all():
        return {"chains":[],"ledger":[],"reason":"invalid_input","total_length_px":0.,"accepted_length_px":0.,"rejected_length_px":0.}
    edge=np.linalg.norm(np.diff(p,axis=0),axis=1);total=float(edge.sum())
    def rejected_all(reason):
        return {"chains":[],"ledger":[dict(lo=0,hi=len(p)-1,length_px=total,status="rejected",reason=reason)],"reason":reason,"closed_source":bool(np.array_equal(p[0],p[-1])),"total_length_px":total,"accepted_length_px":0.,"rejected_length_px":total}
    if np.any(edge<=1e-12):return rejected_all("duplicate_adjacent_points")
    if total<6:return rejected_all("short_chain")
    intervals,corners=source_partitions(p);closed=bool(np.array_equal(p[0],p[-1]))
    candidates=[];metas=[]
    for lo,hi in intervals:
        if deadline is not None and time.monotonic()>=deadline:
            curves,meta=None,{"reason":"arm_wall_budget"}
        elif float(edge[lo:hi].sum())>MAX_ARC+1e-8:
            curves,meta=None,{"reason":"source_edge_exceeds_partition_arc"}
        else:
            curves,meta=fit(p[lo:hi+1],maximum_deviation=DEVIATION,maximum_segments=64)
        candidates.append(curves);metas.append(meta)
    joins=periodic_handles(p,intervals,candidates,corners) if condition=="Q" and closed else []
    ledger=[];accepted=[];cubics=0
    for i,((lo,hi),curves,meta) in enumerate(zip(intervals,candidates,metas)):
        row=dict(partition_id=i,lo=lo,hi=hi,length_px=float(edge[lo:hi].sum()),status="rejected",reason=meta['reason'],initial_fit=meta)
        if curves is not None:
            m=measure(p[lo:hi+1],curves);row['final_fit']=m
            reason=None
            if m['numerical_upper_envelope_px']>DEVIATION:reason='periodic_deviation_gate'
            elif not np.array_equal(curves[0,0],p[lo]) or not np.array_equal(curves[-1,-1],p[hi]):reason='endpoint_moved'
            elif cubics+len(curves)>maximum_trace_cubics:reason='original_trace_cubic_budget'
            else:
                line=LineString(flattened(curves));raw=LineString(p[lo:hi+1])
                if raw.is_simple and not line.is_simple:reason='new_partition_selfintersection'
                for old_i,old_curve in accepted:
                    if reason:break
                    oldlo,oldhi=intervals[old_i]
                    oldraw=LineString(p[oldlo:oldhi+1]);oldline=LineString(flattened(old_curve))
                    crossing=line.intersection(oldline)
                    if not crossing.is_empty:
                        expected=raw.intersection(oldraw)
                        if expected.is_empty or not crossing.difference(expected.buffer(DEVIATION)).is_empty:
                            reason='new_partition_crossing'
            if reason:row['reason']=reason
            else:
                row.update(status='accepted',reason='accepted',cubics=len(curves));accepted.append((i,curves));cubics+=len(curves)
        ledger.append(row)
    # A closed loop must preserve source winding/nondegeneracy. Rejection is
    # conservative whole-loop rollback; open subsets do not masquerade as holes.
    allok=len(accepted)==len(intervals)
    if closed and allok:
        assembled=np.concatenate([v for _,v in accepted])
        rawarea=signed_area(p);area=signed_area(flattened(assembled))
        if abs(rawarea)>1e-9 and (abs(area)<=1e-9 or rawarea*area<=0):
            for row in ledger:row.update(status='rejected',reason='closed_winding_or_area')
            accepted=[];allok=False
    chains=[];runs=[]
    for i,c in accepted:
        if runs and i==runs[-1][-1][0]+1:runs[-1].append((i,c))
        else:runs.append([(i,c)])
    # Rejoin accepted runs across source seam, preserving original orientation.
    if closed and len(runs)>1 and runs[0][0][0]==0 and runs[-1][-1][0]==len(intervals)-1:
        runs=[runs[-1]+runs[0]]+runs[1:-1]
    for run in runs:
        c=np.concatenate([v for _,v in run]);chains.append(dict(curves=c.tolist(),closed=bool(closed and allok),partition_ids=[i for i,_ in run]))
    retained_ids={row['partition_id'] for row in ledger if row['status']=='accepted'}
    for join in joins:
        a,b=join['previous_partition'],join['next_partition']
        join['both_partitions_retained']=a in retained_ids and b in retained_ids
        if join['status']=='periodic_handles_proposed' and join['both_partitions_retained']:
            va=candidates[a][-1,3]-candidates[a][-1,2];vb=candidates[b][0,1]-candidates[b][0,0]
            norm=float(np.linalg.norm(va)*np.linalg.norm(vb))
            join['retained_tangent_angle_degrees']=math.degrees(math.acos(float(np.clip(va@vb/norm,-1,1)))) if norm else None
    retained=sum(x['length_px'] for x in ledger if x['status']=='accepted')
    return dict(chains=chains,ledger=ledger,condition=condition,closed_source=closed,closed_retained=bool(closed and allok),
                total_length_px=total,accepted_length_px=retained,rejected_length_px=sum(x['length_px'] for x in ledger if x['status']=='rejected'),
                edge_accounting_error_px=float(sum(x['length_px'] for x in ledger)-total),
                intentional_corner_source_indices=[i for i,a in corners.items() if a>=CORNER],
                periodic_joins=joins,
                wall_seconds=time.monotonic()-started,reason='completed',continuous_exact_certification=False)
```

### `construct.rejected_all` — `Lines 108–109`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `108` إلى السطر `109` (`Lines 108–109`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 108–109`):**
```python
    def rejected_all(reason):
        return {"chains":[],"ledger":[dict(lo=0,hi=len(p)-1,length_px=total,status="rejected",reason=reason)],"reason":reason,"closed_source":bool(np.array_equal(p[0],p[-1])),"total_length_px":total,"accepted_length_px":0.,"rejected_length_px":total}
```

### `fit_trace` — `Lines 183–185`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `183` إلى السطر `185` (`Lines 183–185`)
- **الوظيفة:** Caller-facing alias: periodic False=P and True=Q; no case/image inputs.
- **الكود الفعلي (`Lines 183–185`):**
```python
def fit_trace(points, periodic=False, deadline=None, maximum_trace_cubics=TRACE_CUBICS):
    """Caller-facing alias: periodic False=P and True=Q; no case/image inputs."""
    return construct(points, 'Q' if periodic else 'P', deadline, maximum_trace_cubics)
```
