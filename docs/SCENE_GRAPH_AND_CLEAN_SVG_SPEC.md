# المواصفات الهندسية للـ Scene Graph وخوارزميات الـ Clean SVG (`SCENE_GRAPH_AND_CLEAN_SVG_SPEC.md`)

## 1. عقد بيانات الـ Scene Graph الموحد (`Canonical SceneGraph JSON Schema`)

يمثل كائن `SceneGraph` العقد المشترك بين جميع الـ Sub-Agents والموديولات:

```json
{
  "scene_id": "scene_sandwich_001",
  "canvas": {
    "width_px": 1024,
    "height_px": 1024,
    "view_box": "0 0 1024 1024",
    "background_color": "#FFFFFF"
  },
  "language": "ar",
  "groups": [
    {
      "group_id": "grp_bread_bottom",
      "display_name": "العيش السفلي",
      "semantic_class": "bread",
      "z_index": 1,
      "bbox_px": {"x_min": 140, "y_min": 520, "x_max": 880, "y_max": 860},
      "layers": [
        {
          "layer_id": "lyr_bread_base",
          "role": "base_shape",
          "fill_hex": "#E6B87A",
          "amodal_completed": true,
          "bezier_node_count": 18,
          "svg_path_d": "M 140.00 620.00 C ...",
          "qa_metrics": {"iou": 0.964, "ssim": 0.951, "opacity_50_verified": true}
        },
        {
          "layer_id": "lyr_bread_shadow",
          "role": "shadow_shape",
          "fill_hex": "#C49252",
          "opacity": 0.85,
          "clipped_to_layer_id": "lyr_bread_base",
          "bezier_node_count": 12,
          "svg_path_d": "M 160.00 710.00 C ...",
          "qa_metrics": {"iou": 0.948, "ssim": 0.942, "opacity_50_verified": true}
        }
      ]
    },
    {
      "group_id": "grp_potato",
      "display_name": "بطاطس",
      "semantic_class": "potato_fries",
      "z_index": 2,
      "bbox_px": {"x_min": 210, "y_min": 310, "x_max": 790, "y_max": 640},
      "layers": [
        {
          "layer_id": "lyr_potato_base",
          "role": "base_shape",
          "fill_hex": "#F4C430",
          "amodal_completed": false,
          "bezier_node_count": 22,
          "svg_path_d": "M 210.00 350.00 C ...",
          "qa_metrics": {"iou": 0.958, "ssim": 0.949, "opacity_50_verified": true}
        },
        {
          "layer_id": "lyr_potato_shadow",
          "role": "shadow_shape",
          "fill_hex": "#D49B1A",
          "opacity": 0.9,
          "clipped_to_layer_id": "lyr_potato_base",
          "bezier_node_count": 14,
          "svg_path_d": "M 230.00 480.00 C ...",
          "qa_metrics": {"iou": 0.941, "ssim": 0.938, "opacity_50_verified": true}
        }
      ]
    }
  ]
}
```

## 2. خوارزمية منع تشظي الألوان وتجميع الـ Clean Design (`Anti-Fragmentation Algorithm`)

لضمان عدم تفتت العناصر مثل الفلافل أو البطاطس إلى عشرات الأجزاء الصغيرة:
1. **العزل الدلالي (`Step 1: Semantic Instance Masking`):**
   - يتم تمرير الصورة على مصنف الكيانات لفصل قناع البكسلات (`Mask M_k`) لكل عنصر (`Bread`, `Potato`, `Falafel`, `Shield`).
   - يُحظر تماماً لأي عملية تجميع لوني أن تدمج بكسلات من `M_potato` مع بكسلات من `M_bread`.
2. **التبسيط اللوني الوظيفي داخل العنصر الواحد (`Step 2: Intra-Object Functional Color Quantization`):**
   - بدلاً من تحويل كل درجة لونية صغيرة إلى مسار مستقل، يتم تجميع ألوان العنصر الواحد في 2 إلى 4 مستويات وظيفية فقط:
     - `Base Color`: اللون الأساسي الذي يملأ كامل مساحة العنصر (`Silhouette`).
     - `Shadow Color`: المناطق الأغمق التي تمثل الظل الداخلي.
     - `Highlight / Accent Color`: مناطق الإضاءة أو التفاصيل البارزة.
3. **الدمج الهندسي للمناطق المتجاورة (`Step 3: Morphological Closing & Topology Union`):**
   - إذا كانت منطقة الظل تحتوي على فجوات ميكروسكوبية أو قطع صغيرة متجاورة ضمن مسافة أقل من `tolerance_px`، يتم تطبيق `Morphological Closing` ثم `Polygon Boolean Union` لدمجها في قطعة هندسية واحدة متصلة قبل تحويلها لمنحنيات Bézier.
4. **قص الزوائد وضمان النظافة (`Step 4: Z-Clean Boundary Clipping`):**
   - يتم تطبيق تقاطع هندسي `Shadow_Clean = Intersection(Shadow_Raw, Base_Shape)` لضمان عدم خروج أي حافة ظل خارج إطار العنصر الأساسي.
