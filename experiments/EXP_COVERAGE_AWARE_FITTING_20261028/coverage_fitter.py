# START CHANGE AGD-COVERAGE-FITTER | 2026-10-28T05:16:21Z | EDITED | Author: /root/appearance_fit
"""Experimental fixed-geometry fitting using measured full-scene coverage weights.

Straight SVG colors are approximated by a linear sRGB premultiplied mixture.
Quantization/renderer mismatch is measured, never assumed away. No alpha,
geometry, topology, stop-spacing or model-capacity optimization is performed.
"""
from __future__ import annotations
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET
import numpy as np
from PIL import Image, ImageColor

SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def _historical():
    path = os.environ.get("AGD_INHERITED_FITTER")
    if not path:
        for ancestor in Path(__file__).resolve().parents:
            candidate = ancestor / "EXP_GEOMETRY_APPEARANCE_ABLATION_01/fit_appearance.py"
            if candidate.exists():
                path = str(candidate)
                break
    if not path:
        raise RuntimeError("Set AGD_INHERITED_FITTER to preserved fit_appearance.py")
    spec = importlib.util.spec_from_file_location("coverage_inherited_appearance", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _json(path, data):
    Path(path).write_text(json.dumps(data, indent=2, allow_nan=False), encoding="utf-8")


def _hash(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def _shape_signature(root):
    """Ignore only visible-path RGB paint and gradient definitions; retain masks."""
    excluded=_visible_gradient_ids(root)
    def visit(node, inside_mask=False):
        local = node.tag.rsplit("}", 1)[-1]
        if local in ("linearGradient", "radialGradient") and node.get("id") in excluded:
            return None
        inside_mask = inside_mask or local in ("mask", "clipPath")
        attrs = dict(node.attrib)
        if local == "path" and not inside_mask:
            attrs.pop("fill", None)
        children = [result for child in node if (result := visit(child, inside_mask)) is not None]
        if local == "defs" and not children:
            return None
        return [node.tag, attrs, children]
    return hashlib.sha256(json.dumps(visit(root), sort_keys=True).encode()).hexdigest()


def _visible_gradient_ids(root):
    ids=set()
    def visit(node):
        if node.tag.rsplit("}",1)[-1] in ("defs","mask","clipPath"):return
        if node.tag.rsplit("}",1)[-1]=="path" and node.get("fill","").startswith("url(#"):
            ids.add(node.get("fill")[5:-1])
        for child in node:visit(child)
    visit(root)
    # Gradient definitions that also drive alpha cannot be treated as mutable RGB.
    dependencies=set()
    for mask in root.iter(f"{{{SVG}}}mask"):
        for node in mask.iter():
            for value in node.attrib.values():dependencies.update(re.findall(r"url\(#([^)]*)\)",value))
    definitions={node.get("id"):node for node in root.iter() if node.get("id")}
    pending=list(dependencies)
    while pending:
        key=pending.pop();node=definitions.get(key)
        if node is None:continue
        for descendant in node.iter():
            for attr,value in descendant.attrib.items():
                refs=re.findall(r"url\(#([^)]*)\)",value)
                if attr.endswith("href") and value.startswith("#"):refs.append(value[1:])
                for ref in refs:
                    if ref not in dependencies:dependencies.add(ref);pending.append(ref)
    if ids&dependencies:raise ValueError("RGB gradient is also a fixed alpha dependency")
    return ids


def _render(root, svg, png):
    ET.ElementTree(root).write(svg, encoding="utf-8", xml_declaration=True)
    subprocess.run([os.environ["AGD_RENDERER_EXE"], str(svg), str(png)], check=True,
                   capture_output=True, timeout=15)
    rgba = np.asarray(Image.open(png).convert("RGBA"), dtype=np.float32)
    return rgba[:, :, :3] * (rgba[:, :, 3:4] / 255.)


def _paint_probe(root, colors, old):
    result = copy.deepcopy(root)
    paths = old._paths(result)
    for (path, _), color in zip(paths, colors):
        if path.get("style"):
            raise ValueError("Style-bound RGB paint unsupported; preserve explicit attrs")
        if path.get("stroke", "none") != "none":
            raise ValueError("Visible strokes unsupported")
        path.set("fill", "rgb(" + ",".join(str(int(v)) for v in color) + ")")
    return result


def build_maps(baseline_svg, folder):
    """Measure per-path effective visibility; preserve full-scene opacity and masks."""
    old = _historical()
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    metadata_path = folder / "maps.json"
    if metadata_path.exists():
        metadata = json.loads(metadata_path.read_text())
        if metadata["baseline_sha256"] != _hash(baseline_svg):
            raise ValueError("Coverage map source drift")
        if metadata.get("maps_npz_sha256")!=_hash(folder/"maps.npz"):
            raise ValueError("Coverage NPZ cache drift")
        return metadata
    started = time.monotonic()
    root = ET.parse(baseline_svg).getroot()
    for node in root.iter():
        if node.tag.rsplit("}",1)[-1] in ("image","filter","foreignObject","use","style"):
            raise ValueError("Coverage fitter requires explicit paths without raster/filter/use/CSS")
        style=node.get("style","")
        allowed_mask_style=node.tag==f"{{{SVG}}}mask" and style.replace(" ","").rstrip(";")=="mask-type:alpha"
        if (style and not allowed_mask_style) or any(node.get(key) for key in ("filter","mix-blend-mode")):
            raise ValueError("CSS/filter/blend composition unsupported")
        if node.get("stroke","none") != "none":
            raise ValueError("Stroke composition unsupported")
    entries = old._paths(root)
    if not entries:
        raise ValueError("No visible RGB paths")
    n = len(entries)
    colors = np.zeros((n, 3), dtype=np.uint8)
    black = _render(_paint_probe(root, colors, old), folder / "probe.svg", folder / "black.png")
    height, width = black.shape[:2]
    byte_size = n * height * width * 4
    if byte_size > 200 * 1024 * 1024:
        raise MemoryError(f"Coverage maps need {byte_size} bytes, cap200MiB")
    weights = np.empty((n, height * width), dtype=np.float32)
    for i in range(n):
        colors[i] = 255
        rendered = _render(_paint_probe(root, colors, old), folder / "probe.svg", folder / "probe.png")
        if i in {0, n//2, n-1}:
            shutil_path = folder / f"representative_{i:04d}.png"
            shutil_path.write_bytes((folder / "probe.png").read_bytes())
        weights[i] = ((rendered - black).mean(axis=2) / 255.).reshape(-1)
        colors[i] = 0
    white = _render(_paint_probe(root, np.full((n, 3), 255, dtype=np.uint8), old), folder / "probe.svg", folder / "white.png")
    black_alpha=np.asarray(Image.open(folder/"black.png").convert("RGBA"))[:,:,3].astype(int)
    white_alpha=np.asarray(Image.open(folder/"white.png").convert("RGBA"))[:,:,3].astype(int)
    expected = (white - black).mean(axis=2).reshape(-1) / 255.
    closure = weights.sum(axis=0) - expected
    random = np.random.default_rng(20261028).integers(0, 256, (n, 3), dtype=np.uint8)
    actual = _render(_paint_probe(root, random, old), folder / "probe.svg", folder / "random_actual.png")
    predicted = black.reshape(-1, 3) + weights.T @ random.astype(np.float32)
    error = predicted - actual.reshape(-1, 3)
    Image.fromarray(np.clip(np.rint(predicted.reshape(height, width, 3)), 0, 255).astype(np.uint8)).save(folder / "random_predicted_premult.png")
    energy = np.einsum("ij,ij->i", weights, weights)
    gram = weights @ weights.T
    norm = np.sqrt(np.maximum(energy, 1e-30))
    correlation = gram / norm[:, None] / norm[None, :]
    np.fill_diagonal(correlation, 0)
    eigen = np.linalg.eigvalsh(gram.astype(np.float64))
    positive = eigen[eigen > max(float(eigen.max()), 1.) * 1e-9]
    np.savez_compressed(folder / "maps.npz", weights=weights, black=black.reshape(-1, 3), total=expected, width=width, height=height)
    metadata = {"baseline_sha256": _hash(baseline_svg), "geometry_signature": _shape_signature(root),
                "maps_npz_sha256":_hash(folder/"maps.npz"),
                "regions": n, "width": width, "height": height, "uncompressed_map_bytes": byte_size,
                "wall_seconds": time.monotonic()-started, "probe_count": n+3,
                "closure_mae": float(np.mean(np.abs(closure))), "closure_max": float(np.max(np.abs(closure))),
                "black_vs_white_alpha_max_change_bytes":int(np.abs(black_alpha-white_alpha).max()),
                "random_forward_rmse_bytes": float(np.sqrt(np.mean(error**2))), "random_forward_max_error_bytes": float(np.max(np.abs(error))),
                "unobservable_regions": np.flatnonzero(energy < 1e-10).tolist(),
                "weak_regions_energy_lt_flat_ridge":np.flatnonzero(energy<1e-4).tolist(),
                "nearly_correlated_region_pairs_gt_0_995": np.argwhere(np.triu(correlation > .995, 1)).tolist(),
                "positive_gram_condition_ratio": float(positive.max()/positive.min()) if len(positive) else None,
                "gram_rank_threshold_1e9": int(len(positive)),
                "limitations": ["Renderer probe quantization makes weights approximate", "Linear sRGB-byte premultiplied model may differ from actual SVG composition", "Visible RGB paths only; no strokes/filter/raster inputs", "Coefficients already contain alpha and overlap; never apply source alpha weighting again"]}
    _json(metadata_path, metadata)
    for name in ("probe.svg", "probe.png"):
        (folder / name).unlink(missing_ok=True)
    return metadata


def _color(value):
    if value.startswith("rgb("):
        return np.array([float(v) for v in value[4:-1].split(",")])
    return np.array(ImageColor.getrgb(value)[:3], dtype=float)


def _models(root, old):
    definitions = {node.get("id"): node for node in root.iter() if node.tag.rsplit("}",1)[-1] in ("linearGradient", "radialGradient")}
    models = []
    for path, matrix in old._paths(root):
        fill = path.get("fill", "#000000")
        if not fill.startswith("url("):
            models.append({"kind": "flat", "colors": [_color(fill).tolist()]})
            continue
        gradient = definitions[fill[5:-1]]
        if gradient.get("gradientUnits")!="userSpaceOnUse" or gradient.get("spreadMethod","pad")!="pad" or gradient.get("color-interpolation","sRGB")!="sRGB":
            raise ValueError("Seed gradient outside inherited SVG appearance family")
        if any(float(stop.get("stop-opacity","1"))!=1 for stop in gradient):
            raise ValueError("Seed stop alpha is not a fitted RGB parameter")
        if gradient.tag.endswith("radialGradient") and (gradient.get("fx",gradient.get("cx"))!=gradient.get("cx") or gradient.get("fy",gradient.get("cy"))!=gradient.get("cy")):
            raise ValueError("Off-center radial focus outside inherited family")
        if not np.allclose(matrix @ old._matrix(gradient.get("gradientTransform")), np.eye(3), atol=1e-6):
            raise ValueError("Seed gradients must use inherited global coordinates")
        colors = [_color(stop.get("stop-color")).tolist() for stop in gradient]
        offsets = [float(stop.get("offset")) for stop in gradient]
        if len(colors) > 4 or not np.allclose(offsets, np.linspace(0,1,len(colors))):
            raise ValueError("Seed gradient outside inherited equal-stop model capacity")
        if gradient.tag.endswith("linearGradient"):
            model = {"kind":"linear", "start":[float(gradient.get("x1")),float(gradient.get("y1"))], "end":[float(gradient.get("x2")),float(gradient.get("y2"))]}
        else:
            model = {"kind":"radial", "center":[float(gradient.get("cx")),float(gradient.get("cy"))], "radius":float(gradient.get("r"))}
        model["colors"] = colors
        models.append(model)
    return models


def _write_models(root, models, target, old):
    painted = copy.deepcopy(root)
    excluded=_visible_gradient_ids(painted)
    for parent in painted.iter():
        for child in list(parent):
            if child.tag.rsplit("}",1)[-1] in ("linearGradient","radialGradient") and child.get("id") in excluded:
                parent.remove(child)
    existing={node.get("id") for node in painted.iter() if node.get("id")}
    for i,model in enumerate(models):
        if model["kind"]!="flat" and f"agd_fit_{i}" in existing:
            raise ValueError("Inherited RGB gradient ID collides with fixed mask dependency")
    old._paint(painted, models)
    if _shape_signature(painted) != _shape_signature(root):
        raise AssertionError("Fixed geometry/mask changed")
    ET.ElementTree(painted).write(target, encoding="utf-8", xml_declaration=True)


def fit_case(source_png, baseline_flat_svg, baseline_gradient_svg, maps_folder,
             out_flat_svg, out_gradient_svg, diagnostics_path, max_seconds=300):
    """Fit flat and same-capacity gradient paint using full-scene linear coefficients."""
    started=time.monotonic(); deadline=started+max_seconds
    old=_historical(); root=ET.parse(baseline_flat_svg).getroot(); droot=ET.parse(baseline_gradient_svg).getroot()
    meta=json.loads((Path(maps_folder)/"maps.json").read_text())
    if meta.get("maps_npz_sha256")!=_hash(Path(maps_folder)/"maps.npz"):
        raise ValueError("Coverage NPZ cache drift")
    if _shape_signature(root)!=meta["geometry_signature"] or _shape_signature(droot)!=meta["geometry_signature"]:
        raise ValueError("Map/input geometry drift")
    with np.load(Path(maps_folder)/"maps.npz") as saved:
        w=saved["weights"]; black=saved["black"].astype(float); total=saved["total"].astype(float); width=int(saved["width"]);height=int(saved["height"])
    source=np.asarray(Image.open(source_png).convert("RGBA"),dtype=float)
    if source.shape[:2]!=(height,width):raise ValueError("Source dimensions differ")
    source_alpha=(source[:,:,3]/255.).reshape(-1)
    premult=(source[:,:,:3]*(source[:,:,3:4]/255.)).reshape(-1,3)
    background_mean=np.mean([[255.,255.,255.],[0.,0.,0.],[40.,80.,120.]],axis=0)
    target=premult+(total-source_alpha)[:,None]*background_mean
    yy,xx=np.indices((height,width));xy=np.column_stack((xx.reshape(-1)+.5,yy.reshape(-1)+.5));partition=(xx.reshape(-1)+3*yy.reshape(-1))%5
    train=partition<3;selection=partition==3;test=partition==4
    def error(pred, mask):return float(np.mean((pred[mask]-target[mask])**2))
    flatmodels=_models(root,old)
    if any(m["kind"]!="flat" for m in flatmodels):raise ValueError("Flat seed must use flat colors")
    colors=np.array([m["colors"][0] for m in flatmodels],dtype=float)
    seedcolors=colors.copy();regularization=1e-4
    prediction=black+w.T@colors
    best=colors.copy();bestloss=error(prediction,selection);flat_history=[{"sweep":-1,"train_mse":error(prediction,train),"selection_mse":bestloss}]
    for sweep in range(20):
        if time.monotonic()>=deadline:break
        movement=0.
        for i in range(len(w)):
            support=np.flatnonzero(w[i]>1e-8);ids=support[train[support]]
            denom=float(w[i,ids]@w[i,ids])
            if denom<1e-12:continue
            delta=(w[i,ids]@(target[ids]-prediction[ids])-regularization*(colors[i]-seedcolors[i]))/(denom+regularization)
            updated=np.clip(colors[i]+delta,0,255);change=updated-colors[i]
            prediction[support]+=w[i,support,None]*change;colors[i]=updated;movement=max(movement,float(np.max(np.abs(change))))
        loss=error(prediction,selection)
        flat_history.append({"sweep":sweep,"train_mse":error(prediction,train),"selection_mse":loss})
        if loss<bestloss:best,bestloss=colors.copy(),loss
        if movement<1e-4:break
    bmodels=[{"kind":"flat","colors":[color.tolist()]} for color in best]
    flatpred=black+w.T@best
    dmodels=_models(droot,old)
    def predict_models(models):
        result=black.copy()
        for i,m in enumerate(models):
            support=np.flatnonzero(w[i]>1e-8)
            if len(support):result[support]+=w[i,support,None]*old._predict(m,xy[support])
        return result
    dpred=predict_models(dmodels)
    if error(dpred,selection)<error(flatpred,selection):models=copy.deepcopy(dmodels);prediction=dpred;initialization="inherited_gradient_seed"
    else:models=copy.deepcopy(bmodels);prediction=flatpred.copy();initialization="coverage_flat_seed"
    bestmodels=copy.deepcopy(models);gradientloss=error(prediction,selection);gradient_history=[];regional=[]
    for sweep in range(2):
        for i in range(len(w)):
            if time.monotonic()>=deadline:break
            support=np.flatnonzero(w[i]>1e-8)
            ids=[np.flatnonzero(partition[support]<3),np.flatnonzero(partition[support]==3),np.flatnonzero(partition[support]==4)]
            if not len(ids[0]) or not len(ids[1]):
                regional.append({"pass":sweep,"region":i,"reason":"unobservable_or_split_empty","support":len(support)})
                continue
            ids=[a[np.linspace(0,len(a)-1,min(cap,len(a))).astype(int)] if len(a) else a for a,cap in zip(ids,(512,256,256))]
            before=old._predict(models[i],xy[support]);partial=target[support]-prediction[support]+w[i,support,None]*before
            pseudo=partial/w[i,support,None]
            flat,candidate,diag=old._fit_region(xy[support],pseudo,*ids,deadline,w[i,support]**2)
            localbest=models[i];localprediction=before;localloss=error(prediction,selection)
            for proposed in (flat,candidate):
                proposed["colors"]=np.clip(proposed["colors"],0,255).tolist()
                proposedpaint=old._predict(proposed,xy[support]);delta=w[i,support,None]*(proposedpaint-before)
                valid=selection[support]
                # Compare exact global selection objective affected by this region.
                change=float(np.sum((prediction[support][valid]+delta[valid]-target[support][valid])**2)-np.sum((prediction[support][valid]-target[support][valid])**2))/(int(selection.sum())*3)
                if error(prediction,selection)+change<localloss-1e-10:
                    localbest=copy.deepcopy(proposed);localprediction=proposedpaint;localloss=error(prediction,selection)+change
            prediction[support]+=w[i,support,None]*(localprediction-before);models[i]=localbest
            regional.append({"proposal_fit_diagnostics":diag,"pass":sweep,"region":i,"support":len(support),"selection_global_mse":localloss,"effective_weight_sum":float(w[i].sum()),"effective_weight_energy":float(w[i]@w[i]),"accepted_model":localbest["kind"],"note":"Proposal test metrics do not necessarily describe accepted/global-final model; final heldout metrics reported only at global checkpoint"})
            if localloss<gradientloss:gradientloss=localloss;bestmodels=copy.deepcopy(models)
        gradient_history.append({"pass":sweep,"train_mse":error(prediction,train),"selection_mse":error(prediction,selection)})
        if time.monotonic()>=deadline:break
    gradientpred=predict_models(bestmodels)
    for dest in (out_flat_svg,out_gradient_svg,diagnostics_path):Path(dest).parent.mkdir(parents=True,exist_ok=True)
    _write_models(root,bmodels,out_flat_svg,old);_write_models(root,bestmodels,out_gradient_svg,old)
    actual_forward={}
    with tempfile.TemporaryDirectory(prefix="agd-coverage-final-") as temporary:
        for name,path,pred in (("flat",out_flat_svg,flatpred),("gradient",out_gradient_svg,gradientpred)):
            png=Path(diagnostics_path).parent/f"coverage_{name}_actual.png"
            actual=_render(ET.parse(path).getroot(),Path(temporary)/f"{name}.svg",png).reshape(-1,3)
            alpha=np.asarray(Image.open(png).convert("RGBA"))[:,:,3].reshape(-1)/255.
            mismatch=pred-actual
            errors=[]
            for background in ([255.,255.,255.],[0.,0.,0.],[40.,80.,120.]):
                bg=np.array(background)
                errors.append(float(np.mean((actual+(1-alpha)[:,None]*bg-premult-(1-source_alpha)[:,None]*bg)**2)))
            actual_forward[name]={"premult_surrogate_vs_actual_rmse_bytes":float(np.sqrt(np.mean(mismatch**2))),"premult_surrogate_vs_actual_max_error_bytes":float(np.max(np.abs(mismatch))),"actual_three_background_float_mse":float(np.mean(errors)),"actual_per_background_float_mse":dict(zip(("white","black","bluegray"),errors)),"note":"Float byte compositing diagnostic; final parent evaluator renders/quantizes backgrounds independently"}
    diagnostic={"map_metadata":meta,"wall_seconds":time.monotonic()-started,"deadline_seconds":max_seconds,"deadline_reached":time.monotonic()>=deadline,
        "split":"(x+3y)%5 train0,1,2; selection3; untouched test4; interpolation not spatial extrapolation",
        "objective":"Equal-mean squared error over white/black/bluegray backgrounds: effective target Ps+(Atotal-As)*mean(backgrounds). Wi already includes SVG opacity/alpha, no second alpha weighting",
        "flat_regularization":{"lambda":regularization,"policy":"Tiny train-only ridge toward inherited flat colors; unobservable regions retain seed; validation uses unregularized data loss"},
        "gradient_initialization":initialization,"initialization_note":"Selection chooses inherited D or new flat B; this is warm-started same-capacity fitting, not isolation from initialization",
        "flat_history":flat_history,"gradient_history":gradient_history,"regions":regional,
        "forward_model_validation":actual_forward,
        "flat_surrogate":{"train_mse":error(flatpred,train),"selection_mse":error(flatpred,selection),"untouched_test_mse":error(flatpred,test)},
        "gradient_surrogate":{"train_mse":error(gradientpred,train),"selection_mse":error(gradientpred,selection),"untouched_test_mse":error(gradientpred,test)},
        "limits":["Linear measured sRGB surrogate is approximate; actual exported SVG rendering is decisive", "Inherited interior fitter applied to Wi-weighted partial residual; <=100 objective calls per region per pass", "Same flat/linear/radial family with <=4 equally spaced stops; no geometry/alpha/stop-position changes", "Selection loss chooses checkpoints/models; untouched test split never used for decisions"]}
    _json(diagnostics_path,diagnostic)
    return diagnostic
# END CHANGE AGD-COVERAGE-FITTER | 2026-10-28T05:16:21Z | EDITED
