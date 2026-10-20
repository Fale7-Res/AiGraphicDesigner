<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "CREATED", "last_change_id": "TASK-MULTI-VER-01", "last_edited_at_utc": "2026-10-17T08:58:05Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# معادلات ومقاييس القياس المعياري الدقيقة (`Benchmark Metrics & Mathematical Formulations`)

**الحالة:** معتمدة رسمياً كمرجعية قياسية (`OFFICIAL_BENCHMARK_METRICS_SPEC`)  
**سياق الحوكمة:** `benchmarks/METRICS.md` ضمن نظام التجارب متعدد الإصدارات.

---

## 1. مقاييس دقة التفكيك والرؤية الحاسوبية (`Vision & Decomposition Metrics`)

### أ. نسبة التقاطع لشريط الحواف (`Trimap Boundary IoU — 8px Band`)
تتجاوز هذه المعادلة مقياس التقاطع التقليدي الساذج (`Global Mask IoU`) الذي يعطي نتائج مضللة مرتفعة بسبب المساحات الداخلية الكبيرة، وتركز حصرياً على شريط الحواف الحرجة:
$$\text{Boundary-IoU}(A, B; d) = \frac{|(A \cap B) \cap T_d(A \cup B)|}{|(A \cup B) \cap T_d(A \cup B)|}$$
حيث:
- $A$: القناع المستخرج من النموذج.
- $B$: القناع المرجعي الحقيقي (`Ground Truth`).
- $T_d$: شريط التقليم الشريطي بعرض $d = 8$ بكسلات عند دقة $2048 \times 2048$.
- **عتبة النجاح الصارمة:** $\ge 0.90$.

---

### ب. النقاء الإدراكي للبصريات (`LPIPS — Learned Perceptual Image Patch Similarity`)
يقيس الفرق البصري الحقيقي بين الصورة الأصلية وإعادة تصيير الـ SVG المولّد في فضاء استجابات الشبكات العميقة (AlexNet/VGG):
$$d_{\text{LPIPS}}(x, x_0) = \sum_l \frac{1}{H_l W_l} \sum_{h,w} \left\| w_l \odot \left(\hat{y}_{hw}^l - \hat{y}_{0,hw}^l\right) \right\|_2^2$$
- **عتبة النجاح الصارمة:** $\le 0.12$.

---

### ج. التشابه الهيكلي للطبقات (`SSIM — Structural Similarity Index`)
يقيس الحفاظ على التباين والسطوع والهيكل الداخلي لكل طبقة مفككة مقارنة بالأصل:
$$\text{SSIM}(x, y) = \frac{(2\mu_x\mu_y + c_1)(2\sigma_{xy} + c_2)}{(\mu_x^2 + \mu_y^2 + c_1)(\sigma_x^2 + \sigma_y^2 + c_2)}$$
- **عتبة النجاح الصارمة:** $\ge 0.92$.

---

## 2. مقاييس جودة الفيكتور والمنحنيات (`Vector & Geometry Quality Metrics`)

### أ. ميزانية العقد القصوى لمسار بيزييه (`Maximum Bézier Node Budget`)
تضمن أن المنحنيات المتجهة تمثل "فيكتور نظيفاً" (`Clean SVG`) قابلاً للتعديل بواسطة مصمم محترف بأداة القلم (`Pen Tool`)، وليست مصفوفة مجهرية من آلاف النقاط:
$$N_{\text{nodes}}(\text{Path}_k) \le 36 \quad \forall k \in \text{Semantic Layers}$$
- **عتبة النجاح الصارمة:** لا يزيد عدد نقاط التحكم عن 36 نقطة للمسار الدلالي الأساسي، مع منع ظهور مسارات فرعية يقل طولها عن 4 بكسلات (`No Micro-Fragments`).

---

### ب. استمرارية الانحناء والانسيابية (`C1 Curvature Continuity Ratio`)
تقيس نسبة نقاط الاتصال بين مقاطع بيزييه التي تحقق استمرارية المماس والانحناء ($C^1$ Continuity) لمنع الانكسارات البصرية غير المقصودة:
$$\text{Ratio}_{C^1} = \frac{\sum_{i=1}^{M} \mathbb{I}\left(\|\mathbf{t}_{i}^- - \mathbf{t}_{i}^+\| < \epsilon\right)}{M} \ge 0.95$$
- **عتبة النجاح الصارمة:** $\ge 0.95$.

---

## 3. مقاييس الأداء واستهلاك العتاد والتكلفة (`Performance, Telemetry & Cost`)

| المقياس (`Metric`) | المعادلة / طريقة الرصد | العتبة المقبولة (`Target`) | الحد الأقصى الحرج (`Max Bound`) |
| :--- | :--- | :--- | :--- |
| **زمن الاستجابة الإجمالي (`Latency`)** | $T_{\text{total}} = T_{\text{seg}} + T_{\text{inpaint}} + T_{\text{vec}} + T_{\text{group}}$ | $\le 5.0\text{ s}$ | $\le 8.0\text{ s}$ |
| **ذروة ذاكرة الفيديو (`Peak VRAM`)** | $\max_t \text{torch.cuda.memory_allocated}(t)$ | $\le 12.0\text{ GB}$ | $\le 16.0\text{ GB}$ |
| **التكلفة التشغيلية لكل تصميم (`Cost`)** | $\text{Cost} = \text{GPU\_Rate\_Per\_Second} \times T_{\text{total}}$ | $\le \$0.02$ | $\le \$0.04$ |
