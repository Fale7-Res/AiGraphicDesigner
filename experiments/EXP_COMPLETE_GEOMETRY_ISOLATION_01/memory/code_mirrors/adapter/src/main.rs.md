# Native adapter source mirror

Exact source: adapter/src/main.rs. Inputs: frozen labels or common RGBA. Outputs: raw watershed labels, canonical graph and native spline JSON. Research only; no Arena code copied.

```rust
1: // START CHANGE AGD-GEOMETRY-ADAPTER | 2026-10-28T14:17:00Z | CREATED | Author: /root/appearance_fit
2: //! Research-only geometry bridge for VTracer 1.0.0-alpha.4.
3: //! Upstream: visioncortex/vtracer commit2500df76b5aea0ac22d15296b22722442f825c5b,
4: //! MIT OR Apache-2.0. Uses public graph/fitter APIs; no Arena source is copied.
5: //! Face-reference traversal below is newly authored against the public graph
6: //! contract and follows its documented right-turn/left-region convention.
7: use serde::Deserialize;
8: use serde_json::{json, Value};
9: use std::{collections::{BTreeMap, BTreeSet}, env, fs, time::Instant};
10: use vtracer::{Color, ColorImage};
11: use vtracer::frontend::WatershedHierarchy;
12: use vtracer::ir::Paint;
13: use vtracer::mosaic::{BoundaryGraph, FittedGeom, LabelMap, SegmentFitter, SplineSegmentFitter, OUTSIDE};
14: 
15: const SOURCE_COMMIT: &str = "2500df76b5aea0ac22d15296b22722442f825c5b";
16: 
17: #[derive(Deserialize)]
18: struct Request {
19:     width: u32,
20:     height: u32,
21:     #[serde(default)] labels: Vec<u32>,
22:     #[serde(default)] rgba: Vec<u8>,
23:     #[serde(default="default_detail")] detail: u32,
24:     #[serde(default)] min_area: usize,
25: }
26: fn default_detail() -> u32 {192}
27: fn region(value:u32) -> u32 {if value==OUTSIDE {0} else {value}}
28: fn point(value: vtracer::PointI32) -> [i32;2] {[value.x,value.y]}
29: fn reference(chain:usize,forward:bool) -> Value {json!({"chain":chain,"forward":forward})}
30: fn label_fingerprint(labels:&[u32]) -> String {
31:     let mut hash=0xcbf29ce484222325u64;
32:     for value in labels {for byte in value.to_le_bytes() {hash^=byte as u64;hash=hash.wrapping_mul(0x100000001b3);}}
33:     format!("{hash:016x}")
34: }
35: 
36: fn segment(request: &Request) -> Result<Value,String> {
37:     let pixels=request.width as usize*request.height as usize;
38:     if request.rgba.len()!=pixels*4 {return Err("RGBA size differs from dimensions".into())}
39:     if request.rgba.chunks_exact(4).any(|p|p[3]!=255) {return Err("Segmentation requires frozen opaque working RGBA".into())}
40:     let image=ColorImage {pixels:request.rgba.clone(),width:request.width as usize,height:request.height as usize};
41:     let hierarchy=WatershedHierarchy::build(&image).map_err(|e|e.to_string())?;
42:     let segmentation=hierarchy.cut(&image,request.detail,request.min_area);
43:     let map=LabelMap::from_segmentation(&segmentation);
44:     if map.labels.contains(&OUTSIDE) {return Err("Opaque watershed unexpectedly leaves uncovered pixels".into())}
45:     let unique:BTreeSet<_>=map.labels.iter().copied().collect();
46:     let mapping:BTreeMap<_,_>=unique.iter().enumerate().map(|(i,&v)|(v,i as u32+1)).collect();
47:     let labels:Vec<_>=map.labels.iter().map(|v|mapping[v]).collect();
48:     Ok(json!({"schema":1,"operation":"segment","width":map.width,"height":map.height,"labels":labels,
49:         "regions":mapping.len(),"outside_label":0,"source_commit":SOURCE_COMMIT,"vtracer_version":"1.0.0-alpha.4","labels_fnv1a64_u32le":label_fingerprint(&labels),
50:         "detail":request.detail,"min_area":request.min_area,"merges_disabled":true,
51:         "policy":"RAW watershed partition; dense1-based labels, full opaque domain; no compositor color-similarity merge"}))
52: }
53: 
54: fn direction(a:vtracer::PointI32,b:vtracer::PointI32) -> Result<usize,String> {
55:     match (b.x-a.x,b.y-a.y) {(0,-1)=>Ok(0),(1,0)=>Ok(1),(0,1)=>Ok(2),(-1,0)=>Ok(3),_=>Err("Non-unit lattice step".into())}
56: }
57: 
58: fn islands(map:&LabelMap) -> Vec<u32> {
59:     let mut ids=vec![u32::MAX;map.labels.len()];let mut next=0;
60:     for start in 0..ids.len() {
61:         if ids[start]!=u32::MAX||map.labels[start]==OUTSIDE {continue}
62:         let mut stack=vec![start];ids[start]=next;
63:         while let Some(index)=stack.pop() {
64:             let x=index as i32%map.width as i32;let y=index as i32/map.width as i32;
65:             for dy in -1..=1 {for dx in -1..=1 {
66:                 let xx=x+dx;let yy=y+dy;
67:                 if xx<0||yy<0||xx>=map.width as i32||yy>=map.height as i32 {continue}
68:                 let neighbor=yy as usize*map.width as usize+xx as usize;
69:                 if ids[neighbor]==u32::MAX&&map.labels[neighbor]==map.labels[start] {ids[neighbor]=next;stack.push(neighbor)}
70:             }}
71:         }
72:         next+=1;
73:     }
74:     ids
75: }
76: 
77: fn validate_graph_labels(graph:&BoundaryGraph,map:&LabelMap) -> Result<usize,String> {
78:     let mut edges=BTreeSet::new();
79:     for chain in &graph.segments {for pair in chain.points.windows(2) {
80:         let a=pair[0];let b=pair[1];let dir=direction(a,b)?;
81:         let (lx,ly,rx,ry)=match dir {0=>(a.x-1,a.y-1,a.x,a.y-1),1=>(a.x,a.y-1,a.x,a.y),2=>(a.x,a.y,a.x-1,a.y),_=>(a.x-1,a.y,a.x-1,a.y-1)};
82:         if map.label(lx,ly)!=chain.left||map.label(rx,ry)!=chain.right {return Err("Graph left/right adjacency differs from exact input labels".into())}
83:         let aa=point(a);let bb=point(b);let key=if aa<bb {(aa,bb)} else {(bb,aa)};
84:         if !edges.insert(key) {return Err("Duplicate canonical unit edge".into())}
85:     }}
86:     let mut expected=0;
87:     for y in 0..map.height as i32 {for x in 0..=map.width as i32 {expected+=usize::from(map.label(x-1,y)!=map.label(x,y));}}
88:     for y in 0..=map.height as i32 {for x in 0..map.width as i32 {expected+=usize::from(map.label(x,y-1)!=map.label(x,y));}}
89:     if edges.len()!=expected {return Err("Canonical graph does not cover every label boundary".into())}
90:     Ok(expected)
91: }
92: 
93: fn face_references(graph:&BoundaryGraph,map:&LabelMap) -> Result<Vec<Value>,String> {
94:     let island_ids=islands(map);
95:     let mut used=vec![[false;2];graph.segments.len()];
96:     let mut loops:BTreeMap<(u32,u32),Vec<Vec<Value>>>=BTreeMap::new();
97:     for start in 0..graph.segments.len() {for initial_forward in [true,false] {
98:         let initial=&graph.segments[start];
99:         let side=if initial_forward {initial.left} else {initial.right};
100:         if side==OUTSIDE||used[start][initial_forward as usize] {continue}
101:         let (a,b)=if initial_forward {(initial.points[0],initial.points[1])} else {let n=initial.points.len();(initial.points[n-1],initial.points[n-2])};
102:         let first_direction=direction(a,b)?;
103:         let (x,y)=match first_direction {0=>(a.x-1,a.y-1),1=>(a.x,a.y-1),2=>(a.x,a.y),_=>(a.x-1,a.y)};
104:         if x<0||y<0||x>=map.width as i32||y>=map.height as i32 {return Err("Region-side pixel outside domain".into())}
105:         let pixel=y as usize*map.width as usize+x as usize;
106:         if map.labels[pixel]!=side {return Err("Face side label disagreement".into())}
107:         let mut contour=Vec::new();let mut current=(start,initial_forward);
108:         loop {
109:             if used[current.0][current.1 as usize] {return Err("Face walker hit a previously used oriented chain before closure".into())}
110:             used[current.0][current.1 as usize]=true;contour.push(reference(current.0,current.1));
111:             let chain=&graph.segments[current.0];
112:             if chain.is_ring() {break}
113:             let endpoint=if current.1 {chain.end} else {chain.start}.ok_or("Missing junction endpoint")?;
114:             let incoming=if current.1 {chain.last_dir as usize} else {(chain.first_dir as usize+2)%4};
115:             let mut successor=None;
116:             for outgoing in [(incoming+1)%4,incoming,(incoming+3)%4] {
117:                 if let Some(candidate)=graph.nodes[endpoint as usize].out[outgoing] {
118:                     let neighbor=&graph.segments[candidate.seg as usize];
119:                     let candidate_side=if candidate.forward {neighbor.left} else {neighbor.right};
120:                     if candidate_side==side {successor=Some((candidate.seg as usize,candidate.forward));break}
121:                 }
122:             }
123:             current=successor.ok_or("No successor preserving left region")?;
124:             if current==(start,initial_forward) {break}
125:             if contour.len()>graph.segments.len()*2 {return Err("Face walk failed to close".into())}
126:         }
127:         loops.entry((side,island_ids[pixel])).or_default().push(contour);
128:     }}
129:     Ok(loops.into_iter().map(|((r,island),contours)|json!({"region":region(r),"island":island,"loops":contours})).collect())
130: }
131: 
132: fn fit(request:&Request) -> Result<Value,String> {
133:     if request.labels.len()!=request.width as usize*request.height as usize {return Err("Label size differs from dimensions".into())}
134:     let max=*request.labels.iter().max().ok_or("Empty labels")?;
135:     if max>request.labels.len() as u32 {return Err("Labels must be dense with zero reserved outside".into())}
136:     let map=LabelMap {width:request.width,height:request.height,
137:         labels:request.labels.iter().map(|&x|if x==0 {OUTSIDE} else {x}).collect(),
138:         paints:(0..=max).map(|_|Paint::Solid(Color::new(0,0,0))).collect()};
139:     let graph=BoundaryGraph::extract(&map);let crack_edges=validate_graph_labels(&graph,&map)?;let fitter=SplineSegmentFitter::default();
140:     let nodes:Vec<_>=graph.nodes.iter().enumerate().map(|(id,node)|json!({"id":id,"point":point(node.corner),"out":node.out.iter().map(|r|r.map(|v|reference(v.seg as usize,v.forward))).collect::<Vec<_>>()})).collect();
141:     let mut chains=Vec::new();
142:     for (id,chain) in graph.segments.iter().enumerate() {
143:         let fitted=if chain.is_ring() {fitter.fit_ring(chain)} else {fitter.fit_open(chain)};
144:         let (geometry,segments)=match fitted.geom {
145:             FittedGeom::Polyline(points)=>{
146:                 let segments=points.windows(2).map(|p|json!({"type":"L","p0":[p[0].x,p[0].y],"p3":[p[1].x,p[1].y]})).collect::<Vec<_>>();
147:                 (json!({"kind":"polyline","points":points.iter().map(|p|[p.x,p.y]).collect::<Vec<_>>()}),segments)
148:             },
149:             FittedGeom::Beziers(curves)=>{
150:                 let segments=curves.iter().map(|p|json!({"type":"C","p0":[p[0].x,p[0].y],"p1":[p[1].x,p[1].y],"p2":[p[2].x,p[2].y],"p3":[p[3].x,p[3].y]})).collect::<Vec<_>>();
151:                 (json!({"kind":"beziers","curves":curves.iter().map(|curve|curve.iter().map(|p|[p.x,p.y]).collect::<Vec<_>>()).collect::<Vec<_>>()}),segments)
152:             }
153:         };
154:         chains.push(json!({"id":id,"left":region(chain.left),"right":region(chain.right),"adjacent_face_labels":[region(chain.left),region(chain.right)],"start":chain.start,"end":chain.end,"ring":chain.is_ring(),"closed":chain.is_ring(),"pixel_crack_vertices":chain.points.iter().map(|p|point(*p)).collect::<Vec<_>>(),"segments":segments,"geometry":geometry}));
155:     }
156:     let patches=face_references(&graph,&map)?;
157:     let mut faces:BTreeMap<String,Vec<Value>>=BTreeMap::new();
158:     for patch in &patches {
159:         faces.entry(patch["region"].to_string()).or_default().extend(patch["loops"].as_array().unwrap().iter().cloned());
160:     }
161:     let mut edges=BTreeSet::new();let mut degrees:BTreeMap<[i32;2],usize>=BTreeMap::new();
162:     for chain in &graph.segments {for pair in chain.points.windows(2) {
163:         let a=point(pair[0]);let b=point(pair[1]);let key=if a<b {(a,b)} else {(b,a)};
164:         if edges.insert(key) {*degrees.entry(a).or_default()+=1;*degrees.entry(b).or_default()+=1;}
165:     }}
166:     let incidence:Vec<_>=degrees.into_iter().map(|(xy,degree)|json!({"xy":xy,"degree":degree})).collect();
167:     Ok(json!({"schema":1,"operation":"fit","width":request.width,"height":request.height,"outside_label":0,
168:         "nodes":nodes,"chains":chains,"faces":faces,"patches":patches,"incidence":incidence,"source_commit":SOURCE_COMMIT,"vtracer_version":"1.0.0-alpha.4",
169:         "labels":request.labels,"labels_fnv1a64_u32le":label_fingerprint(&request.labels),"input_label_boundary_unit_edges":crack_edges,"graph_matches_exact_labels":true,
170:         "merges_disabled":true,"simplify":false,"curve_passes":0,
171:         "face_policy":"new adapter traversal of public graph, right-turn/left-region successor,8-connected same-label islands; canonical shared chain referenced in reverse",
172:         "geometry_policy":"Unmodified SplineSegmentFitter::default; no refinement, no custom fallback, all native polyline outputs explicitly identified"}))
173: }
174: 
175: fn main() {
176:     let start=Instant::now();
177:     let args:Vec<_>=env::args().collect();
178:     if args.len()!=4 {eprintln!("Usage: agd_geometry segment|fit request.json output.json");std::process::exit(2)}
179:     let result=(||->Result<Value,String>{
180:         let input=fs::read(&args[2]).map_err(|e|e.to_string())?;
181:         let request:Request=serde_json::from_slice(&input).map_err(|e|e.to_string())?;
182:         if request.width==0||request.height==0 {return Err("Empty dimensions".into())}
183:         match args[1].as_str() {"segment"=>segment(&request),"fit"=>fit(&request),_=>Err("Unknown operation".into())}
184:     })();
185:     match result {
186:         Ok(mut result)=>{result["wall_seconds"]=json!(start.elapsed().as_secs_f64());let encoded=serde_json::to_vec(&result).unwrap();if let Err(error)=fs::write(&args[3],encoded) {eprintln!("{error}");std::process::exit(1)}},
187:         Err(error)=>{eprintln!("{error}");std::process::exit(1)}
188:     }
189: }
190: 
191: #[cfg(test)]
192: mod tests {
193:     use super::*;
194:     fn case(labels:Vec<u32>,width:u32,height:u32) {
195:         let request=Request {width,height,labels,rgba:vec![],detail:192,min_area:0};
196:         let output=fit(&request).unwrap();
197:         let mut incidence:BTreeMap<usize,Vec<bool>>=BTreeMap::new();
198:         for loops in output["faces"].as_object().unwrap().values() {for contour in loops.as_array().unwrap() {for r in contour.as_array().unwrap() {incidence.entry(r["chain"].as_u64().unwrap() as usize).or_default().push(r["forward"].as_bool().unwrap());}}}
199:         for chain in output["chains"].as_array().unwrap() {
200:             let id=chain["id"].as_u64().unwrap() as usize;
201:             let expected=usize::from(chain["left"]!=0)+usize::from(chain["right"]!=0);
202:             assert_eq!(incidence[&id].len(),expected);
203:             if expected==2 {assert_ne!(incidence[&id][0],incidence[&id][1]);}
204:         }
205:     }
206:     #[test] fn uniform_domain(){case(vec![1;16],4,4)}
207:     #[test] fn shared_junction(){case(vec![1,1,2,2,1,1,2,2,3,3,2,2,3,3,2,2],4,4)}
208:     #[test] fn hole_and_islands(){case(vec![1,1,1,1,1,1,2,2,2,1,1,2,3,2,1,1,2,2,2,1,1,1,1,1,1],5,5)}
209:     #[test] fn diagonal_pinches(){case(vec![1,2,2,1],2,2)}
210:     #[test] fn all_small_three_label_maps(){for value in 0..81 {let mut rest=value;let mut labels=Vec::new();for _ in 0..4 {labels.push(rest%3+1);rest/=3;}case(labels,2,2)}}
211:     #[test] fn opaque_input_required(){let r=Request {width:1,height:1,rgba:vec![0,0,0,0],labels:vec![],detail:192,min_area:0};assert!(segment(&r).is_err())}
212: }
213: // END CHANGE AGD-GEOMETRY-ADAPTER | 2026-10-28T14:17:00Z | CREATED
```
