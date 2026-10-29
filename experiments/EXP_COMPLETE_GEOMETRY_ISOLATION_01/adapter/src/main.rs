// START CHANGE AGD-GEOMETRY-ADAPTER | 2026-10-28T14:17:00Z | CREATED | Author: /root/appearance_fit
//! Research-only geometry bridge for VTracer 1.0.0-alpha.4.
//! Upstream: visioncortex/vtracer commit2500df76b5aea0ac22d15296b22722442f825c5b,
//! MIT OR Apache-2.0. Uses public graph/fitter APIs; no Arena source is copied.
//! Face-reference traversal below is newly authored against the public graph
//! contract and follows its documented right-turn/left-region convention.
use serde::Deserialize;
use serde_json::{json, Value};
use std::{collections::{BTreeMap, BTreeSet}, env, fs, time::Instant};
use vtracer::{Color, ColorImage};
use vtracer::frontend::WatershedHierarchy;
use vtracer::ir::Paint;
use vtracer::mosaic::{BoundaryGraph, FittedGeom, LabelMap, SegmentFitter, SplineSegmentFitter, OUTSIDE};

const SOURCE_COMMIT: &str = "2500df76b5aea0ac22d15296b22722442f825c5b";

#[derive(Deserialize)]
struct Request {
    width: u32,
    height: u32,
    #[serde(default)] labels: Vec<u32>,
    #[serde(default)] rgba: Vec<u8>,
    #[serde(default="default_detail")] detail: u32,
    #[serde(default)] min_area: usize,
}
fn default_detail() -> u32 {192}
fn region(value:u32) -> u32 {if value==OUTSIDE {0} else {value}}
fn point(value: vtracer::PointI32) -> [i32;2] {[value.x,value.y]}
fn reference(chain:usize,forward:bool) -> Value {json!({"chain":chain,"forward":forward})}
fn label_fingerprint(labels:&[u32]) -> String {
    let mut hash=0xcbf29ce484222325u64;
    for value in labels {for byte in value.to_le_bytes() {hash^=byte as u64;hash=hash.wrapping_mul(0x100000001b3);}}
    format!("{hash:016x}")
}

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

fn direction(a:vtracer::PointI32,b:vtracer::PointI32) -> Result<usize,String> {
    match (b.x-a.x,b.y-a.y) {(0,-1)=>Ok(0),(1,0)=>Ok(1),(0,1)=>Ok(2),(-1,0)=>Ok(3),_=>Err("Non-unit lattice step".into())}
}

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

#[cfg(test)]
mod tests {
    use super::*;
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
    #[test] fn uniform_domain(){case(vec![1;16],4,4)}
    #[test] fn shared_junction(){case(vec![1,1,2,2,1,1,2,2,3,3,2,2,3,3,2,2],4,4)}
    #[test] fn hole_and_islands(){case(vec![1,1,1,1,1,1,2,2,2,1,1,2,3,2,1,1,2,2,2,1,1,1,1,1,1],5,5)}
    #[test] fn diagonal_pinches(){case(vec![1,2,2,1],2,2)}
    #[test] fn all_small_three_label_maps(){for value in 0..81 {let mut rest=value;let mut labels=Vec::new();for _ in 0..4 {labels.push(rest%3+1);rest/=3;}case(labels,2,2)}}
    #[test] fn opaque_input_required(){let r=Request {width:1,height:1,rgba:vec![0,0,0,0],labels:vec![],detail:192,min_area:0};assert!(segment(&r).is_err())}
}
// END CHANGE AGD-GEOMETRY-ADAPTER | 2026-10-28T14:17:00Z | CREATED
