# السجل المركزي الموحد للدوال والكلاسات والرموز (`memory/FUNCTION_REGISTRY.md`)

> **مرجعية الكود ومستويات منع التكرار (`Source Authority & 3-Tier Deduplication Policy`):**
> 1. **المستوى الأول — تكرار الاسم المطابق (`Exact-Name Duplication`):** فحص حتمي آلي 100% يمنع وجود دالتين بنفس الاسم عبر الملفات.
> 2. **المستوى الثاني — التشابه الهيكلي للـ AST (`Structural AST Similarity`):** فحص آلي تحذيري يرصد الدوال ذات البنية الهيكلية المتطابقة للمراجعة.
> 3. **المستوى الثالث — التكرار الدلالي (`Semantic Duplication`):** **ليس آلياً بالكامل**؛ يتطلب من كل Agent قراءة عمود الوظيفة (`Purpose`) أدناه قبل كتابة أي دالة جديدة، ويخضع لتدقيق الـ Sub-Agent المراجع (`qa-reviewer-auditor`).

- **إجمالي الملفات البرمجية المفحوصة:** `13`
- **إجمالي الرموز المسجلة بالسطر (شاملة Methods وNested وArrow):** `48`
- **عدد الدوال المتطابقة الاسم غير المسموحة (`Exact-Name Duplicates`):** `0`
- **مرشحات التشابه الهيكلي (`Structural Similarity Candidates`):** `1`

## جدول جميع الدوال والكلاسات والرموز في المشروع (`Master Symbol Index`)

| اسم الرمز (`Symbol`) | النوع (`Kind`) | الملف المالك (`Owner File`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة (`Purpose`) | مرآة الكود التفصيلية (`Code Mirror`) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `render` | `function` | `analyze_matrix.py` | `Lines 15–18` | `def render(svg,png):` | رمز برمجي موثق. | [analyze_matrix.py.md](code_mirrors/analyze_matrix.py.md) |
| `edge_dictionary` | `function` | `analyze_matrix.py` | `Lines 20–29` | `def edge_dictionary(g):` | رمز برمجي موثق. | [analyze_matrix.py.md](code_mirrors/analyze_matrix.py.md) |
| `region_center_check` | `function` | `analyze_matrix.py` | `Lines 31–37` | `def region_center_check(svg,labels,target):` | رمز برمجي موثق. | [analyze_matrix.py.md](code_mirrors/analyze_matrix.py.md) |
| `analyze` | `function` | `analyze_matrix.py` | `Lines 39–86` | `def analyze():` | رمز برمجي موثق. | [analyze_matrix.py.md](code_mirrors/analyze_matrix.py.md) |
| `signature` | `function` | `common_geometry.py` | `Lines 6–9` | `def signature(ch):` | رمز برمجي موثق. | [common_geometry.py.md](code_mirrors/common_geometry.py.md) |
| `normalize_to_common_faces` | `function` | `common_geometry.py` | `Lines 11–33` | `def normalize_to_common_faces(common,candidate):` | رمز برمجي موثق. | [common_geometry.py.md](code_mirrors/common_geometry.py.md) |
| `segment_area` | `function` | `exact_area_check.py` | `Lines 7–13` | `def segment_area(s):` | رمز برمجي موثق. | [exact_area_check.py.md](code_mirrors/exact_area_check.py.md) |
| `coverage_geometry` | `function` | `final_diagnostics.py` | `Lines 14–29` | `def coverage_geometry(g):` | رمز برمجي موثق. | [final_diagnostics.py.md](code_mirrors/final_diagnostics.py.md) |
| `visible_micro` | `function` | `final_diagnostics.py` | `Lines 31–50` | `def visible_micro(g,m,out,name):` | رمز برمجي موثق. | [final_diagnostics.py.md](code_mirrors/final_diagnostics.py.md) |
| `failure_example` | `function` | `final_diagnostics.py` | `Lines 52–66` | `def failure_example():` | رمز برمجي موثق. | [final_diagnostics.py.md](code_mirrors/final_diagnostics.py.md) |
| `failure_example.make` | `nested_function` | `final_diagnostics.py` | `Lines 56–61` | `def make(source,raw,color):` | رمز برمجي موثق. | [final_diagnostics.py.md](code_mirrors/final_diagnostics.py.md) |
| `label_rgb` | `function` | `geometry_eval.py` | `Lines 14–16` | `def label_rgb(label):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `flatten_cubic` | `function` | `geometry_eval.py` | `Lines 18–27` | `def flatten_cubic(points,epsilon=.01,depth=0):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `chain_points` | `function` | `geometry_eval.py` | `Lines 29–40` | `def chain_points(ch,raw=False):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `uniform_points` | `function` | `geometry_eval.py` | `Lines 42–48` | `def uniform_points(points,step=.25):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `signed_area` | `function` | `geometry_eval.py` | `Lines 50–51` | `def signed_area(points):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `ring_points` | `function` | `geometry_eval.py` | `Lines 53–63` | `def ring_points(refs,chains):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `compare_samples` | `function` | `geometry_eval.py` | `Lines 65–70` | `def compare_samples(a,b):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `svg_graph` | `function` | `geometry_eval.py` | `Lines 72–107` | `def svg_graph(graph,raw=False,regions=False,foreground=None):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `svg_graph.data` | `nested_function` | `geometry_eval.py` | `Lines 74–87` | `def data(ch,forward=True):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `evaluate` | `function` | `geometry_eval.py` | `Lines 109–179` | `def evaluate(graph,reference=None):` | رمز برمجي موثق. | [geometry_eval.py.md](code_mirrors/geometry_eval.py.md) |
| `digest` | `function` | `isolation.py` | `Lines 27–28` | `def digest(path):` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `dump` | `function` | `isolation.py` | `Lines 30–32` | `def dump(path, obj):` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `case_dir` | `function` | `isolation.py` | `Lines 34–36` | `def case_dir(case):` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `prepare` | `function` | `isolation.py` | `Lines 38–51` | `def prepare():` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `arena_modules` | `function` | `isolation.py` | `Lines 53–66` | `def arena_modules():` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `arena_modules.denied` | `nested_function` | `isolation.py` | `Lines 58–58` | `def denied(*a,**k): raise RuntimeError('Appearance/rendering forbidden in external geometry worker')` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `worker` | `function` | `isolation.py` | `Lines 68–91` | `def worker(case,stage,segmentation):` | رمز برمجي موثق. | [isolation.py.md](code_mirrors/isolation.py.md) |
| `pixel_path` | `function` | `package_evidence.py` | `Lines 11–15` | `def pixel_path(case):` | رمز برمجي موثق. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `img` | `function` | `package_evidence.py` | `Lines 17–19` | `def img(path,label,svg=None):` | رمز برمجي موثق. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `main` | `function` | `package_evidence.py` | `Lines 21–92` | `def main():` | رمز برمجي موثق. | [package_evidence.py.md](code_mirrors/package_evidence.py.md) |
| `verify_resume_inputs` | `function` | `run_matrix.py` | `Lines 16–28` | `def verify_resume_inputs():` | رمز برمجي موثق. | [run_matrix.py.md](code_mirrors/run_matrix.py.md) |
| `launch` | `function` | `run_matrix.py` | `Lines 30–35` | `def launch(command,name):` | رمز برمجي موثق. | [run_matrix.py.md](code_mirrors/run_matrix.py.md) |
| `vt_segment` | `function` | `run_matrix.py` | `Lines 37–47` | `def vt_segment(case):` | رمز برمجي موثق. | [run_matrix.py.md](code_mirrors/run_matrix.py.md) |
| `vt_fit` | `function` | `run_matrix.py` | `Lines 49–59` | `def vt_fit(case,seg):` | رمز برمجي موثق. | [run_matrix.py.md](code_mirrors/run_matrix.py.md) |
| `GeometryIsolationTests` | `class` | `test_isolation.py` | `Lines 7–65` | `class GeometryIsolationTests(unittest.TestCase):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_cubic_flattening_analytic_parabola` | `method` | `test_isolation.py` | `Lines 8–13` | `def test_cubic_flattening_analytic_parabola(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_ring_area_detects_collapsed_cell` | `method` | `test_isolation.py` | `Lines 15–17` | `def test_ring_area_detects_collapsed_cell(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_distance_is_symmetric_and_exposes_missing_detail` | `method` | `test_isolation.py` | `Lines 19–23` | `def test_distance_is_symmetric_and_exposes_missing_detail(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_svg_preserves_shared_reversal_hole` | `method` | `test_isolation.py` | `Lines 25–43` | `def test_svg_preserves_shared_reversal_hole(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_common_face_mapping_rejects_changed_boundaries` | `method` | `test_isolation.py` | `Lines 45–52` | `def test_common_face_mapping_rejects_changed_boundaries(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_only_closed_rings_gain_svg_closure` | `method` | `test_isolation.py` | `Lines 54–58` | `def test_only_closed_rings_gain_svg_closure(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `GeometryIsolationTests.test_protocol_prevents_truth_selection` | `method` | `test_isolation.py` | `Lines 60–65` | `def test_protocol_prevents_truth_selection(self):` | رمز برمجي موثق. | [test_isolation.py.md](code_mirrors/test_isolation.py.md) |
| `mask_topology` | `function` | `validate_geometry.py` | `Lines 15–18` | `def mask_topology(mask):` | رمز برمجي موثق. | [validate_geometry.py.md](code_mirrors/validate_geometry.py.md) |
| `mask_boundary` | `function` | `validate_geometry.py` | `Lines 20–23` | `def mask_boundary(mask,scale=8):` | رمز برمجي موثق. | [validate_geometry.py.md](code_mirrors/validate_geometry.py.md) |
| `known_mask_evaluation` | `function` | `validate_geometry.py` | `Lines 25–51` | `def known_mask_evaluation(case,g,labels,reference,out,name):` | رمز برمجي موثق. | [validate_geometry.py.md](code_mirrors/validate_geometry.py.md) |
| `visible_microgeometry` | `function` | `validate_geometry.py` | `Lines 53–69` | `def visible_microgeometry(g,labels):` | رمز برمجي موثق. | [validate_geometry.py.md](code_mirrors/validate_geometry.py.md) |
| `run` | `function` | `validate_geometry.py` | `Lines 71–93` | `def run():` | رمز برمجي موثق. | [validate_geometry.py.md](code_mirrors/validate_geometry.py.md) |

## Native Rust bridge symbols

Input: frozen RGBA/labels. Output: canonical graph/native curves; no appearance. All full source lines in adapter/src/main.rs mirror.

### adapter/src/main.rs::default_detail — Lines26–26

```rust
fn default_detail() -> u32 {192}
```

### adapter/src/main.rs::region — Lines27–27

```rust
fn region(value:u32) -> u32 {if value==OUTSIDE {0} else {value}}
```

### adapter/src/main.rs::point — Lines28–28

```rust
fn point(value: vtracer::PointI32) -> [i32;2] {[value.x,value.y]}
```

### adapter/src/main.rs::reference — Lines29–29

```rust
fn reference(chain:usize,forward:bool) -> Value {json!({"chain":chain,"forward":forward})}
```

### adapter/src/main.rs::label_fingerprint — Lines30–34

```rust
fn label_fingerprint(labels:&[u32]) -> String {
    let mut hash=0xcbf29ce484222325u64;
    for value in labels {for byte in value.to_le_bytes() {hash^=byte as u64;hash=hash.wrapping_mul(0x100000001b3);}}
    format!("{hash:016x}")
}
```

### adapter/src/main.rs::segment — Lines36–52

```rust
fn segment(request: &Request) -> Result<Value,String> {
    let pixels=request.width as usize*request.height as usize;
    if request.rgba.len()!=pixels*4 {return Err("RGBA size differs from dimensions".into())}
    if request.rgba.chunks_exact(4).any(|p|p[3]!=255) {return Err("Segmentation requires frozen opaque working RGBA".into())}
    let image=ColorImage {pixels:request.rgba.clone(),width:request.width as usize,height:request.height as usize};
    let hierarchy=WatershedHierarchy::build(&image).map_err(|e|e.to_string())?;
    let segmentation=hierarchy.cut(&image,request.detail,request.min_area);
    let map=LabelMap::from_segmentation(&segmentation);
    if map.labels.contains(&OUTSIDE) {return Err("Opaque watershed unexpectedly leaves uncovered pixels".into())}
    let unique:BTreeSet<_>=map.labels.iter().copied().collect();
    let mapping:BTreeMap<_,_>=unique.iter().enumerate().map(|(i,&v)|(v,i as u32+1)).collect();
    let labels:Vec<_>=map.labels.iter().map(|v|mapping[v]).collect();
    Ok(json!({"schema":1,"operation":"segment","width":map.width,"height":map.height,"labels":labels,
        "regions":mapping.len(),"outside_label":0,"source_commit":SOURCE_COMMIT,"vtracer_version":"1.0.0-alpha.4","labels_fnv1a64_u32le":label_fingerprint(&labels),
        "detail":request.detail,"min_area":request.min_area,"merges_disabled":true,
        "policy":"RAW watershed partition; dense1-based labels, full opaque domain; no compositor color-similarity merge"}))
}
```

### adapter/src/main.rs::direction — Lines54–56

```rust
fn direction(a:vtracer::PointI32,b:vtracer::PointI32) -> Result<usize,String> {
    match (b.x-a.x,b.y-a.y) {(0,-1)=>Ok(0),(1,0)=>Ok(1),(0,1)=>Ok(2),(-1,0)=>Ok(3),_=>Err("Non-unit lattice step".into())}
}
```

### adapter/src/main.rs::islands — Lines58–75

```rust
fn islands(map:&LabelMap) -> Vec<u32> {
    let mut ids=vec![u32::MAX;map.labels.len()];let mut next=0;
    for start in 0..ids.len() {
        if ids[start]!=u32::MAX||map.labels[start]==OUTSIDE {continue}
        let mut stack=vec![start];ids[start]=next;
        while let Some(index)=stack.pop() {
            let x=index as i32%map.width as i32;let y=index as i32/map.width as i32;
            for dy in -1..=1 {for dx in -1..=1 {
                let xx=x+dx;let yy=y+dy;
                if xx<0||yy<0||xx>=map.width as i32||yy>=map.height as i32 {continue}
                let neighbor=yy as usize*map.width as usize+xx as usize;
                if ids[neighbor]==u32::MAX&&map.labels[neighbor]==map.labels[start] {ids[neighbor]=next;stack.push(neighbor)}
            }}
        }
        next+=1;
    }
    ids
}
```

### adapter/src/main.rs::validate_graph_labels — Lines77–91

```rust
fn validate_graph_labels(graph:&BoundaryGraph,map:&LabelMap) -> Result<usize,String> {
    let mut edges=BTreeSet::new();
    for chain in &graph.segments {for pair in chain.points.windows(2) {
        let a=pair[0];let b=pair[1];let dir=direction(a,b)?;
        let (lx,ly,rx,ry)=match dir {0=>(a.x-1,a.y-1,a.x,a.y-1),1=>(a.x,a.y-1,a.x,a.y),2=>(a.x,a.y,a.x-1,a.y),_=>(a.x-1,a.y,a.x-1,a.y-1)};
        if map.label(lx,ly)!=chain.left||map.label(rx,ry)!=chain.right {return Err("Graph left/right adjacency differs from exact input labels".into())}
        let aa=point(a);let bb=point(b);let key=if aa<bb {(aa,bb)} else {(bb,aa)};
        if !edges.insert(key) {return Err("Duplicate canonical unit edge".into())}
    }}
    let mut expected=0;
    for y in 0..map.height as i32 {for x in 0..=map.width as i32 {expected+=usize::from(map.label(x-1,y)!=map.label(x,y));}}
    for y in 0..=map.height as i32 {for x in 0..map.width as i32 {expected+=usize::from(map.label(x,y-1)!=map.label(x,y));}}
    if edges.len()!=expected {return Err("Canonical graph does not cover every label boundary".into())}
    Ok(expected)
}
```

### adapter/src/main.rs::face_references — Lines93–130

```rust
fn face_references(graph:&BoundaryGraph,map:&LabelMap) -> Result<Vec<Value>,String> {
    let island_ids=islands(map);
    let mut used=vec![[false;2];graph.segments.len()];
    let mut loops:BTreeMap<(u32,u32),Vec<Vec<Value>>>=BTreeMap::new();
    for start in 0..graph.segments.len() {for initial_forward in [true,false] {
        let initial=&graph.segments[start];
        let side=if initial_forward {initial.left} else {initial.right};
        if side==OUTSIDE||used[start][initial_forward as usize] {continue}
        let (a,b)=if initial_forward {(initial.points[0],initial.points[1])} else {let n=initial.points.len();(initial.points[n-1],initial.points[n-2])};
        let first_direction=direction(a,b)?;
        let (x,y)=match first_direction {0=>(a.x-1,a.y-1),1=>(a.x,a.y-1),2=>(a.x,a.y),_=>(a.x-1,a.y)};
        if x<0||y<0||x>=map.width as i32||y>=map.height as i32 {return Err("Region-side pixel outside domain".into())}
        let pixel=y as usize*map.width as usize+x as usize;
        if map.labels[pixel]!=side {return Err("Face side label disagreement".into())}
        let mut contour=Vec::new();let mut current=(start,initial_forward);
        loop {
            if used[current.0][current.1 as usize] {return Err("Face walker hit a previously used oriented chain before closure".into())}
            used[current.0][current.1 as usize]=true;contour.push(reference(current.0,current.1));
            let chain=&graph.segments[current.0];
            if chain.is_ring() {break}
            let endpoint=if current.1 {chain.end} else {chain.start}.ok_or("Missing junction endpoint")?;
            let incoming=if current.1 {chain.last_dir as usize} else {(chain.first_dir as usize+2)%4};
            let mut successor=None;
            for outgoing in [(incoming+1)%4,incoming,(incoming+3)%4] {
                if let Some(candidate)=graph.nodes[endpoint as usize].out[outgoing] {
                    let neighbor=&graph.segments[candidate.seg as usize];
                    let candidate_side=if candidate.forward {neighbor.left} else {neighbor.right};
                    if candidate_side==side {successor=Some((candidate.seg as usize,candidate.forward));break}
                }
            }
            current=successor.ok_or("No successor preserving left region")?;
            if current==(start,initial_forward) {break}
            if contour.len()>graph.segments.len()*2 {return Err("Face walk failed to close".into())}
        }
        loops.entry((side,island_ids[pixel])).or_default().push(contour);
    }}
    Ok(loops.into_iter().map(|((r,island),contours)|json!({"region":region(r),"island":island,"loops":contours})).collect())
}
```

### adapter/src/main.rs::fit — Lines132–173

```rust
fn fit(request:&Request) -> Result<Value,String> {
    if request.labels.len()!=request.width as usize*request.height as usize {return Err("Label size differs from dimensions".into())}
    let max=*request.labels.iter().max().ok_or("Empty labels")?;
    if max>request.labels.len() as u32 {return Err("Labels must be dense with zero reserved outside".into())}
    let map=LabelMap {width:request.width,height:request.height,
        labels:request.labels.iter().map(|&x|if x==0 {OUTSIDE} else {x}).collect(),
        paints:(0..=max).map(|_|Paint::Solid(Color::new(0,0,0))).collect()};
    let graph=BoundaryGraph::extract(&map);let crack_edges=validate_graph_labels(&graph,&map)?;let fitter=SplineSegmentFitter::default();
    let nodes:Vec<_>=graph.nodes.iter().enumerate().map(|(id,node)|json!({"id":id,"point":point(node.corner),"out":node.out.iter().map(|r|r.map(|v|reference(v.seg as usize,v.forward))).collect::<Vec<_>>()})).collect();
    let mut chains=Vec::new();
    for (id,chain) in graph.segments.iter().enumerate() {
        let fitted=if chain.is_ring() {fitter.fit_ring(chain)} else {fitter.fit_open(chain)};
        let (geometry,segments)=match fitted.geom {
            FittedGeom::Polyline(points)=>{
                let segments=points.windows(2).map(|p|json!({"type":"L","p0":[p[0].x,p[0].y],"p3":[p[1].x,p[1].y]})).collect::<Vec<_>>();
                (json!({"kind":"polyline","points":points.iter().map(|p|[p.x,p.y]).collect::<Vec<_>>()}),segments)
            },
            FittedGeom::Beziers(curves)=>{
                let segments=curves.iter().map(|p|json!({"type":"C","p0":[p[0].x,p[0].y],"p1":[p[1].x,p[1].y],"p2":[p[2].x,p[2].y],"p3":[p[3].x,p[3].y]})).collect::<Vec<_>>();
                (json!({"kind":"beziers","curves":curves.iter().map(|curve|curve.iter().map(|p|[p.x,p.y]).collect::<Vec<_>>()).collect::<Vec<_>>()}),segments)
            }
        };
        chains.push(json!({"id":id,"left":region(chain.left),"right":region(chain.right),"adjacent_face_labels":[region(chain.left),region(chain.right)],"start":chain.start,"end":chain.end,"ring":chain.is_ring(),"closed":chain.is_ring(),"pixel_crack_vertices":chain.points.iter().map(|p|point(*p)).collect::<Vec<_>>(),"segments":segments,"geometry":geometry}));
    }
    let patches=face_references(&graph,&map)?;
    let mut faces:BTreeMap<String,Vec<Value>>=BTreeMap::new();
    for patch in &patches {
        faces.entry(patch["region"].to_string()).or_default().extend(patch["loops"].as_array().unwrap().iter().cloned());
    }
    let mut edges=BTreeSet::new();let mut degrees:BTreeMap<[i32;2],usize>=BTreeMap::new();
    for chain in &graph.segments {for pair in chain.points.windows(2) {
        let a=point(pair[0]);let b=point(pair[1]);let key=if a<b {(a,b)} else {(b,a)};
        if edges.insert(key) {*degrees.entry(a).or_default()+=1;*degrees.entry(b).or_default()+=1;}
    }}
    let incidence:Vec<_>=degrees.into_iter().map(|(xy,degree)|json!({"xy":xy,"degree":degree})).collect();
    Ok(json!({"schema":1,"operation":"fit","width":request.width,"height":request.height,"outside_label":0,
        "nodes":nodes,"chains":chains,"faces":faces,"patches":patches,"incidence":incidence,"source_commit":SOURCE_COMMIT,"vtracer_version":"1.0.0-alpha.4",
        "labels":request.labels,"labels_fnv1a64_u32le":label_fingerprint(&request.labels),"input_label_boundary_unit_edges":crack_edges,"graph_matches_exact_labels":true,
        "merges_disabled":true,"simplify":false,"curve_passes":0,
        "face_policy":"new adapter traversal of public graph, right-turn/left-region successor,8-connected same-label islands; canonical shared chain referenced in reverse",
        "geometry_policy":"Unmodified SplineSegmentFitter::default; no refinement, no custom fallback, all native polyline outputs explicitly identified"}))
}
```

### adapter/src/main.rs::main — Lines175–189

```rust
fn main() {
    let start=Instant::now();
    let args:Vec<_>=env::args().collect();
    if args.len()!=4 {eprintln!("Usage: agd_geometry segment|fit request.json output.json");std::process::exit(2)}
    let result=(||->Result<Value,String>{
        let input=fs::read(&args[2]).map_err(|e|e.to_string())?;
        let request:Request=serde_json::from_slice(&input).map_err(|e|e.to_string())?;
        if request.width==0||request.height==0 {return Err("Empty dimensions".into())}
        match args[1].as_str() {"segment"=>segment(&request),"fit"=>fit(&request),_=>Err("Unknown operation".into())}
    })();
    match result {
        Ok(mut result)=>{result["wall_seconds"]=json!(start.elapsed().as_secs_f64());let encoded=serde_json::to_vec(&result).unwrap();if let Err(error)=fs::write(&args[3],encoded) {eprintln!("{error}");std::process::exit(1)}},
        Err(error)=>{eprintln!("{error}");std::process::exit(1)}
    }
}
```

### adapter/src/main.rs::case — Lines194–205

```rust
    fn case(labels:Vec<u32>,width:u32,height:u32) {
        let request=Request {width,height,labels,rgba:vec![],detail:192,min_area:0};
        let output=fit(&request).unwrap();
        let mut incidence:BTreeMap<usize,Vec<bool>>=BTreeMap::new();
        for loops in output["faces"].as_object().unwrap().values() {for contour in loops.as_array().unwrap() {for r in contour.as_array().unwrap() {incidence.entry(r["chain"].as_u64().unwrap() as usize).or_default().push(r["forward"].as_bool().unwrap());}}}
        for chain in output["chains"].as_array().unwrap() {
            let id=chain["id"].as_u64().unwrap() as usize;
            let expected=usize::from(chain["left"]!=0)+usize::from(chain["right"]!=0);
            assert_eq!(incidence[&id].len(),expected);
            if expected==2 {assert_ne!(incidence[&id][0],incidence[&id][1]);}
        }
    }
```

### adapter/src/main.rs::uniform_domain — Lines206–206

```rust
    #[test] fn uniform_domain(){case(vec![1;16],4,4)}
```

### adapter/src/main.rs::shared_junction — Lines207–207

```rust
    #[test] fn shared_junction(){case(vec![1,1,2,2,1,1,2,2,3,3,2,2,3,3,2,2],4,4)}
```

### adapter/src/main.rs::hole_and_islands — Lines208–208

```rust
    #[test] fn hole_and_islands(){case(vec![1,1,1,1,1,1,2,2,2,1,1,2,3,2,1,1,2,2,2,1,1,1,1,1,1],5,5)}
```

### adapter/src/main.rs::diagonal_pinches — Lines209–209

```rust
    #[test] fn diagonal_pinches(){case(vec![1,2,2,1],2,2)}
```

### adapter/src/main.rs::all_small_three_label_maps — Lines210–210

```rust
    #[test] fn all_small_three_label_maps(){for value in 0..81 {let mut rest=value;let mut labels=Vec::new();for _ in 0..4 {labels.push(rest%3+1);rest/=3;}case(labels,2,2)}}
```

### adapter/src/main.rs::opaque_input_required — Lines211–211

```rust
    #[test] fn opaque_input_required(){let r=Request {width:1,height:1,rgba:vec![0,0,0,0],labels:vec![],detail:192,min_area:0};assert!(segment(&r).is_err())}
```

