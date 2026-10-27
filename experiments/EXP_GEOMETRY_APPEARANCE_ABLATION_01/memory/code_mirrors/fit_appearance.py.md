# مرآة الكود التفصيلية: `fit_appearance.py`

> **تنبيه مرجعية الكود (`AUTO-GENERATED MIRROR — DO NOT HAND-EDIT CODE SNIPPETS`):**
> الملف البرمجي الأصلي `fit_appearance.py` هو **المرجع التنفيذي الوحيد (`Sole Implementation Authority`)**. تم توليد هذه المرآة آلياً عبر `tools/memory_guard/sync_code_mirrors.py`؛ أي تعديل في الكود الأصلي يستلزم إعادة تشغيل أداة المزامنة فوراً لمنع تحول المرآة إلى نسخة قديمة (`Stale Copy`).

## 1. بطاقة تعريف الملف (`File Overview`)
- **المسار الفعلي (`Source File`):** `fit_appearance.py`
- **الدور المعماري (`Architectural Role`):** Isolated Windows fidelity validation experiment
- **إجمالي عدد الأسطر (`Total Lines`):** `339` (`Lines 1–339`)
- **بصمة الملف (`SHA-256`):** `3ae12b40fb67746e393745fac5340429a05d9be69129bbbf3e362b887b7e528f`
- **الوصف التفصيلي:** # START CHANGE EXP-GEOMETRY-APPEARANCE-01 | 2026-10-27T14:37:00Z | CREATED | Author: /root/appearance_fit

## 2. خريطة العلاقات وتدفق البيانات (`File Relationships — بياخد منين وبيرمي فين`)

| الاتجاه (`Direction`) | الملف أو المكوّن المرتبط (`Related Target / Source`) | البيانات أو الاستدعاء (`Payload / Call`) | تأثير التعديل (`Change Impact`) |
| :--- | :--- | :--- | :--- |
| **يأخذ من (`Takes From`)** | `historical adaptive optimizer and fidelity evaluator` | source images, candidate configurations, metric arrays | preserve baseline behavior; native execution only |
| **يرمي إلى (`Throws To`)** | `isolated experiment reports and SVG/render trial directories` | generated vectors, PNGs, metrics, process measurements | research evidence only; architecture NOT_APPROVED |

## 3. فهرس الدوال والكلاسات والرموز الداخلية (`Symbols, Methods & Nested Functions Table`)

| الاسم (`Symbol Name`) | النوع (`Kind`) | نطاق الأسطر (`Exact Lines`) | التوقيع (`Signature`) | الوظيفة التفصيلية (`Purpose`) |
| :--- | :--- | :--- | :--- | :--- |
| `_matrix` | `function` | `Lines 28–54` | `def _matrix(transform):` | Parse affine SVG transforms; reject unknown transforms explicitly. |
| `_paths` | `function` | `Lines 57–67` | `def _paths(root):` | رمز برمجي موثق. |
| `_paths.walk` | `nested_function` | `Lines 59–65` | `def walk(node, parent):` | رمز برمجي موثق. |
| `_ownership` | `function` | `Lines 70–106` | `def _ownership(root, width, height, directory, timeout):` | Render unique pseudo-random RGB IDs; reject seams with local consensus. |
| `_basis` | `function` | `Lines 109–116` | `def _basis(t, stops):` | رمز برمجي موثق. |
| `_predict` | `function` | `Lines 119–127` | `def _predict(model, xy):` | رمز برمجي موثق. |
| `_fit_region` | `function` | `Lines 130–220` | `def _fit_region(xy, rgb, train, selection, test, deadline, weights):` | رمز برمجي موثق. |
| `_fit_region.fit_model` | `nested_function` | `Lines 141–166` | `def fit_model(kind, params, stops):` | رمز برمجي موثق. |
| `_paint` | `function` | `Lines 223–246` | `def _paint(root, models):` | رمز برمجي موثق. |
| `fit_svg` | `function` | `Lines 249–338` | `def fit_svg(source_png, baseline_svg, flat_svg, gradient_svg, diagnostics_path, deadline_seconds=600):` | Write C/D SVGs with identical geometry; return region fit diagnostics. |

## 4. التوثيق بالسطر والمقتطفات الفعلية للكود (`Exact Line Numbers & Verbatim Code Snippets`)

### `_matrix` — `Lines 28–54`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `28` إلى السطر `54` (`Lines 28–54`)
- **الوظيفة:** Parse affine SVG transforms; reject unknown transforms explicitly.
- **الكود الفعلي (`Lines 28–54`):**
```python
def _matrix(transform):
    """Parse affine SVG transforms; reject unknown transforms explicitly."""
    result = np.eye(3)
    consumed = ""
    for match in re.finditer(r"([A-Za-z]+)\s*\(([^)]*)\)", transform or ""):
        name, values = match.groups()
        a = [float(x) for x in re.findall(r"[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?", values)]
        m = np.eye(3)
        if name == "translate" and len(a) in (1, 2):
            m[:2, 2] = [a[0], a[1] if len(a) == 2 else 0]
        elif name == "scale" and len(a) in (1, 2):
            m[0, 0], m[1, 1] = a[0], a[-1]
        elif name == "matrix" and len(a) == 6:
            m = np.array([[a[0], a[2], a[4]], [a[1], a[3], a[5]], [0, 0, 1.]])
        elif name == "rotate" and len(a) in (1, 3):
            c, s = math.cos(math.radians(a[0])), math.sin(math.radians(a[0]))
            m[:2, :2] = [[c, -s], [s, c]]
            if len(a) == 3:
                p = np.array(a[1:])
                m[:2, 2] = p - m[:2, :2] @ p
        else:
            raise ValueError(f"Unsupported transform {name}: {values}")
        result = result @ m
        consumed += match.group(0)
    if re.sub(r"[\s,]", "", transform or "") != re.sub(r"[\s,]", "", consumed):
        raise ValueError(f"Invalid transform: {transform}")
    return result
```

### `_paths` — `Lines 57–67`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `57` إلى السطر `67` (`Lines 57–67`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 57–67`):**
```python
def _paths(root):
    found = []
    def walk(node, parent):
        matrix = parent @ _matrix(node.get("transform"))
        if node.tag == f"{{{SVG}}}path":
            found.append((node, matrix))
        for child in node:
            if child.tag not in (f"{{{SVG}}}defs", f"{{{SVG}}}mask", f"{{{SVG}}}clipPath"):
                walk(child, matrix)
    walk(root, np.eye(3))
    return found
```

### `_paths.walk` — `Lines 59–65`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `59` إلى السطر `65` (`Lines 59–65`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 59–65`):**
```python
    def walk(node, parent):
        matrix = parent @ _matrix(node.get("transform"))
        if node.tag == f"{{{SVG}}}path":
            found.append((node, matrix))
        for child in node:
            if child.tag not in (f"{{{SVG}}}defs", f"{{{SVG}}}mask", f"{{{SVG}}}clipPath"):
                walk(child, matrix)
```

### `_ownership` — `Lines 70–106`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `70` إلى السطر `106` (`Lines 70–106`)
- **الوظيفة:** Render unique pseudo-random RGB IDs; reject seams with local consensus.
- **الكود الفعلي (`Lines 70–106`):**
```python
def _ownership(root, width, height, directory, timeout):
    """Render unique pseudo-random RGB IDs; reject seams with local consensus."""
    work = copy.deepcopy(root)
    entries = _paths(work)
    if len(entries) >= 2**24 - 1:
        raise ValueError("Too many paths for RGB ownership IDs")
    codes = ((np.arange(1, len(entries) + 1, dtype=np.int64) * 104729) % (2**24)).astype(np.int64)
    for (path, _), code in zip(entries, codes):
        path.set("fill", f"#{int(code):06x}")
        path.attrib.pop("style", None)
        path.set("fill-opacity", "1")
        path.set("opacity", "1")
        path.set("stroke", "none")
    svg, png = directory / "ownership.svg", directory / "ownership.png"
    ET.ElementTree(work).write(svg, encoding="utf-8", xml_declaration=True)
    subprocess.run([os.environ["AGD_RENDERER_EXE"], str(svg), str(png)], check=True,
                   capture_output=True, timeout=max(1, timeout))
    rgba = np.array(Image.open(png).convert("RGBA"))
    if rgba.shape[:2] != (height, width):
        raise ValueError("Source and ownership render dimensions differ")
    rgb = rgba[:, :, :3].astype(np.int64)
    actual = (rgb[:, :, 0] << 16) | (rgb[:, :, 1] << 8) | rgb[:, :, 2]
    order = np.argsort(codes)
    sorted_codes = codes[order]
    position = np.searchsorted(sorted_codes, actual)
    safe = np.minimum(position, max(0, len(codes) - 1))
    labels = np.full((height, width), -1, dtype=np.int32)
    valid = (position < len(codes)) & (sorted_codes[safe] == actual) & (rgba[:, :, 3] == 255)
    labels[valid] = order[safe[valid]]
    interior = valid.copy()
    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        shifted = np.roll(labels, (dy, dx), (0, 1))
        interior &= labels == shifted
    interior[[0, -1], :] = False
    interior[:, [0, -1]] = False
    labels[~interior] = -1
    return labels
```

### `_basis` — `Lines 109–116`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `109` إلى السطر `116` (`Lines 109–116`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 109–116`):**
```python
def _basis(t, stops):
    t = np.clip(t, 0, 1) * (stops - 1)
    left = np.minimum(t.astype(int), stops - 2)
    fraction = t - left
    basis = np.zeros((len(t), stops))
    basis[np.arange(len(t)), left] = 1 - fraction
    basis[np.arange(len(t)), left + 1] = fraction
    return basis
```

### `_predict` — `Lines 119–127`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `119` إلى السطر `127` (`Lines 119–127`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 119–127`):**
```python
def _predict(model, xy):
    if model["kind"] == "flat":
        return np.broadcast_to(model["colors"][0], (len(xy), 3))
    if model["kind"] == "linear":
        delta = np.array(model["end"]) - model["start"]
        t = (xy - model["start"]) @ delta / (delta @ delta)
    else:
        t = np.linalg.norm(xy - model["center"], axis=1) / model["radius"]
    return _basis(t, len(model["colors"])) @ model["colors"]
```

### `_fit_region` — `Lines 130–220`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `130` إلى السطر `220` (`Lines 130–220`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 130–220`):**
```python
def _fit_region(xy, rgb, train, selection, test, deadline, weights):
    flat = {"kind": "flat", "colors": [np.average(rgb[train], axis=0, weights=weights[train]).tolist()]}
    best = flat
    weighted_error = lambda m, ids: float(np.average(np.mean((_predict(m, xy[ids]) - rgb[ids]) ** 2, axis=1), weights=weights[ids]))
    selection_error = lambda m: weighted_error(m, selection)
    best_error = selection_error(flat)
    center, span = xy.mean(axis=0), np.maximum(np.ptp(xy, axis=0), 1.)
    scale = float(np.linalg.norm(span))
    # All optimizer evaluations count against one regional 100-evaluation cap.
    evaluations = 0
    candidates = []
    def fit_model(kind, params, stops):
        nonlocal evaluations
        if evaluations >= 100 or time.monotonic() >= deadline:
            raise TimeoutError
        evaluations += 1
        if kind == "linear":
            direction = np.array([math.cos(params[0]), math.sin(params[0])])
            projection = xy @ direction
            lo, hi = float(projection.min()), float(projection.max())
            if hi - lo < 1e-7:
                hi = lo + 1
            model = {"kind": kind, "start": (direction * lo).tolist(), "end": (direction * hi).tolist()}
            t = (projection - lo) / (hi - lo)
        else:
            point = center + np.array(params) * span
            radius = max(float(np.linalg.norm(xy - point, axis=1).max()), 1.)
            model = {"kind": kind, "center": point.tolist(), "radius": radius}
            t = np.linalg.norm(xy - point, axis=1) / radius
        basis = _basis(t, stops)
        # Bounded stop RGBs; clipping LS coefficients can be suboptimal but keeps
        # both the scoring model and exported SVG in the same representable range.
        w = np.sqrt(weights[train, None])
        colors = np.clip(np.linalg.lstsq(basis[train] * w, rgb[train] * w, rcond=None)[0], 0, 255)
        model["colors"] = colors.tolist()
        loss = weighted_error(model, train)
        return loss, model
    if len(train) >= 16 and len(selection) >= 6 and best_error > .25:
        try:
            for stops in (2, 3, 4):
                for angle in (0., math.pi / 4, math.pi / 2, 3 * math.pi / 4):
                    candidates.append(fit_model("linear", [angle], stops))
                for origin in ((0., 0.), (-.4, -.4), (.4, .4)):
                    candidates.append(fit_model("radial", origin, stops))
            # Refine each model family from its strongest training initialization.
            for kind in ("linear", "radial"):
                seed = min((v for v in candidates if v[1]["kind"] == kind), key=lambda v: v[0])[1]
                count = len(seed["colors"])
                if kind == "linear":
                    direction = np.array(seed["end"]) - seed["start"]
                    initial = [math.atan2(direction[1], direction[0])]
                    bounds = [(-math.pi * 2, math.pi * 2)]
                else:
                    initial = (np.array(seed["center"]) - center) / span
                    bounds = [(-1.5, 1.5), (-1.5, 1.5)]
                point = np.array(initial, dtype=float)
                step = .2 if kind == "linear" else .15
                current = fit_model(kind, point, count)
                # Small deterministic pattern search avoids a heavyweight native
                # optimizer import; cap refinement at 25 objective evaluations.
                local_calls = 1
                while local_calls < 25 and step >= .005:
                    changed = False
                    for axis in range(len(point)):
                        for sign in (-1, 1):
                            if local_calls >= 25:
                                break
                            trial = point.copy()
                            trial[axis] = np.clip(trial[axis] + sign * step, *bounds[axis])
                            fitted = fit_model(kind, trial, count)
                            local_calls += 1
                            if fitted[0] < current[0]:
                                point, current, changed = trial, fitted, True
                    if not changed:
                        step *= .5
                candidates.append(current)
        except TimeoutError:
            pass
        # Selection never looks at diagnostic test pixels. Prefer simpler models
        # unless improvement exceeds both quantization noise and a 1% margin.
        for _, candidate in sorted(candidates, key=lambda x: (len(x[1]["colors"]), x[1]["kind"])):
            error = selection_error(candidate)
            if error < best_error - max(.0625, best_error * .01):
                best, best_error = candidate, error
    return flat, best, {
        "model": best["kind"], "stops": len(best["colors"]), "optimizer_evaluations": evaluations,
        "train_count": len(train), "selection_count": len(selection), "test_count": len(test),
        "flat_selection_mse": selection_error(flat), "selected_selection_mse": best_error,
        "flat_test_mse": weighted_error(flat, test) if len(test) else None,
        "selected_test_mse": weighted_error(best, test) if len(test) else None,
    }
```

### `_fit_region.fit_model` — `Lines 141–166`
- **النوع:** `nested_function`
- **نطاق الأسطر الدقيق:** من السطر `141` إلى السطر `166` (`Lines 141–166`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 141–166`):**
```python
    def fit_model(kind, params, stops):
        nonlocal evaluations
        if evaluations >= 100 or time.monotonic() >= deadline:
            raise TimeoutError
        evaluations += 1
        if kind == "linear":
            direction = np.array([math.cos(params[0]), math.sin(params[0])])
            projection = xy @ direction
            lo, hi = float(projection.min()), float(projection.max())
            if hi - lo < 1e-7:
                hi = lo + 1
            model = {"kind": kind, "start": (direction * lo).tolist(), "end": (direction * hi).tolist()}
            t = (projection - lo) / (hi - lo)
        else:
            point = center + np.array(params) * span
            radius = max(float(np.linalg.norm(xy - point, axis=1).max()), 1.)
            model = {"kind": kind, "center": point.tolist(), "radius": radius}
            t = np.linalg.norm(xy - point, axis=1) / radius
        basis = _basis(t, stops)
        # Bounded stop RGBs; clipping LS coefficients can be suboptimal but keeps
        # both the scoring model and exported SVG in the same representable range.
        w = np.sqrt(weights[train, None])
        colors = np.clip(np.linalg.lstsq(basis[train] * w, rgb[train] * w, rcond=None)[0], 0, 255)
        model["colors"] = colors.tolist()
        loss = weighted_error(model, train)
        return loss, model
```

### `_paint` — `Lines 223–246`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `223` إلى السطر `246` (`Lines 223–246`)
- **الوظيفة:** رمز برمجي موثق.
- **الكود الفعلي (`Lines 223–246`):**
```python
def _paint(root, models):
    defs = ET.Element(f"{{{SVG}}}defs")
    for i, ((path, matrix), model) in enumerate(zip(_paths(root), models)):
        path.attrib.pop("style", None)
        if model["kind"] == "flat":
            path.set("fill", "rgb(" + ",".join(f"{v:.5f}" for v in model["colors"][0]) + ")")
            continue
        kind = model["kind"]
        gradient = ET.SubElement(defs, f"{{{SVG}}}{kind}Gradient", {"id": f"agd_fit_{i}", "gradientUnits": "userSpaceOnUse", "color-interpolation": "sRGB"})
        # Coordinates were fitted in root image space. Inverse accumulated path
        # transform maps that space into local path user coordinates, including
        # rotations/nonuniform scaling; radial gradients remain correct ellipses.
        inv = np.linalg.inv(matrix)
        gradient.set("gradientTransform", "matrix(" + " ".join(f"{v:.12g}" for v in (inv[0, 0], inv[1, 0], inv[0, 1], inv[1, 1], inv[0, 2], inv[1, 2])) + ")")
        if kind == "linear":
            for name, v in zip(("x1", "y1", "x2", "y2"), model["start"] + model["end"]):
                gradient.set(name, f"{v:.9g}")
        else:
            for name, v in zip(("cx", "cy", "r"), model["center"] + [model["radius"]]):
                gradient.set(name, f"{v:.9g}")
        for j, color in enumerate(model["colors"]):
            ET.SubElement(gradient, f"{{{SVG}}}stop", {"offset": f"{j / (len(model['colors']) - 1):.9g}", "stop-color": "rgb(" + ",".join(f"{v:.5f}" for v in color) + ")"})
        path.set("fill", f"url(#agd_fit_{i})")
    root.insert(0, defs)
```

### `fit_svg` — `Lines 249–338`
- **النوع:** `function`
- **نطاق الأسطر الدقيق:** من السطر `249` إلى السطر `338` (`Lines 249–338`)
- **الوظيفة:** Write C/D SVGs with identical geometry; return region fit diagnostics.
- **الكود الفعلي (`Lines 249–338`):**
```python
def fit_svg(source_png, baseline_svg, flat_svg, gradient_svg, diagnostics_path, deadline_seconds=600):
    """Write C/D SVGs with identical geometry; return region fit diagnostics.

    Inputs must be opaque RGB geometry with a pixel-sized root viewport and no
    inherited fills/styles on groups. Alpha masks are applied by the caller.
    """
    started = time.monotonic()
    deadline = started + deadline_seconds
    root = ET.parse(baseline_svg).getroot()
    if root.get("viewBox"):
        box = [float(x) for x in root.get("viewBox").replace(",", " ").split()]
        image = Image.open(source_png).convert("RGB")
        if box != [0., 0., float(image.width), float(image.height)]:
            raise ValueError("Only image-aligned viewBox supported")
    else:
        image = Image.open(source_png).convert("RGB")
    entries = _paths(root)
    if not entries:
        raise ValueError("No visible path geometry")
    for node in root.iter():
        if node.tag in (f"{{{SVG}}}mask", f"{{{SVG}}}clipPath", f"{{{SVG}}}image", f"{{{SVG}}}filter"):
            raise ValueError("Fit input must be unmasked RGB geometry without raster/filter content")
        for key in ("style", "clip-path", "mask", "filter"):
            if node.get(key):
                raise ValueError(f"Unsupported inherited appearance attribute: {key}")
        for key in ("opacity", "fill-opacity"):
            if float(node.get(key, "1")) != 1:
                raise ValueError("Fit input must have opaque region appearance")
        if node.get("stroke", "none") != "none":
            raise ValueError("Fit input must have filled paths without visible strokes")
    rgb_image = np.asarray(image).astype(float)
    alpha = np.asarray(Image.open(source_png).convert("RGBA"))[:, :, 3].astype(float) / 255
    with tempfile.TemporaryDirectory(prefix="agd-fit-") as temporary:
        labels = _ownership(root, image.width, image.height, Path(temporary), deadline_seconds)
    labels[alpha == 0] = -1
    ys, xs = np.nonzero(labels >= 0)
    order = np.argsort(labels[ys, xs], kind="stable")
    ys, xs = ys[order], xs[order]
    counts = np.bincount(labels[ys, xs], minlength=len(entries))
    offsets = np.r_[0, np.cumsum(counts)]
    flats, models, records = [], [], []
    for i, (path, _) in enumerate(entries):
        y, x = ys[offsets[i]:offsets[i + 1]], xs[offsets[i]:offsets[i + 1]]
        if len(x) == 0 or time.monotonic() >= deadline:
            fill = path.get("fill", "#000000")
            try:
                from PIL import ImageColor
                color = list(ImageColor.getrgb(fill))[:3]
            except ValueError as error:
                raise ValueError(f"Unsupported baseline flat fill {fill}") from error
            flat = best = {"kind": "flat", "colors": [color]}
            record = {"model": "flat", "stops": 1, "reason": "no_interior_samples" if not len(x) else "deadline", "interior_count": len(x)}
        else:
            xy = np.column_stack((x + .5, y + .5))
            rgb = rgb_image[y, x]
            weights = alpha[y, x] ** 2
            split = (x + 3 * y) % 5
            train, selection, test = np.flatnonzero(split < 3), np.flatnonzero(split == 3), np.flatnonzero(split == 4)
            if len(train) == 0:
                # An isolated tiny region has no independent split: use its
                # interior mean, and disclose that it cannot validate a gradient.
                train = np.arange(len(x))
                selection = test = np.array([], dtype=int)
            train = train[np.linspace(0, len(train) - 1, min(512, len(train))).astype(int)]
            if len(selection) == 0:
                flat = best = {"kind": "flat", "colors": [np.average(rgb[train], axis=0, weights=weights[train]).tolist()]}
                record = {"model": "flat", "stops": 1, "reason": "insufficient_selection_samples", "interior_count": len(x)}
            else:
                selection = selection[np.linspace(0, len(selection) - 1, min(256, len(selection))).astype(int)]
                test = test[np.linspace(0, len(test) - 1, min(256, len(test))).astype(int)]
                flat, best, record = _fit_region(xy, rgb, train, selection, test, deadline, weights)
                record["interior_count"] = len(x)
        flats.append(flat)
        models.append(best)
        records.append(dict(path_index=i, **record))
    c, d = copy.deepcopy(root), copy.deepcopy(root)
    _paint(c, flats)
    _paint(d, models)
    for target, tree in ((flat_svg, c), (gradient_svg, d)):
        Path(target).parent.mkdir(parents=True, exist_ok=True)
        ET.ElementTree(tree).write(target, encoding="utf-8", xml_declaration=True)
    diagnostic = {"schema": 1, "wall_seconds": time.monotonic() - started,
                  "deadline_seconds": deadline_seconds, "path_count": len(entries),
                  "split": "(x+3*y)%5: train 0,1,2; selection 3; untouched test 4",
                  "alpha_fitting": "Zero-alpha pixels excluded; all fit/selection/test residuals weighted by source alpha squared (premultiplied appearance objective); source alpha mask reconstructed separately",
                  "max_optimizer_evaluations_per_region": 100,
                  "limitations": ["Interior-only fitting excludes antialiased boundaries", "At most four equally spaced stops", "Periodic pixel split tests interpolation, not spatial-block extrapolation", "Radial focal point equals center and radius follows visible interior sample extent", "Train least squares stop colors clipped to RGB gamut, not a constrained optimum", "Tiny regions retain flat models", "No geometry or alpha optimization"],
                  "regions": records}
    Path(diagnostics_path).write_text(json.dumps(diagnostic, indent=2), encoding="utf-8")
    return diagnostic
```
