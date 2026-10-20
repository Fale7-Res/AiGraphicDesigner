---
trigger: model_decision
description: "Mandatory rules for maintaining PROJECT_FILE_CATALOG.md and FILE_RELATIONSHIPS_GRAPH.md whenever files or responsibilities change."
---
<!-- DOC_PROVENANCE
{"created_at_utc": null, "last_action": "EDITED", "last_change_id": "GOV-FINAL-20261017", "last_edited_at_utc": "2026-10-17T06:58:37Z", "last_editor": "governance-maintainer", "tracking_started_at_utc": "2026-10-17T06:52:16Z"}
END_DOC_PROVENANCE -->
# قواعد فهرس ملفات المشروع وخريطة العلاقات (`Project File Catalog & Relationship Rules`)

`PROJECT_FILE_CATALOG.md` و`memory/FILE_RELATIONSHIPS_GRAPH.md` هما وثيقتان حيتان إلزاميتان. يجب على كل Agent أو Sub-Agent يعمل على هذا المستودع تحديثهما في **نفس المهمة (Same Task)** عند إنشاء أو حذف أو نقل أي ملف أو تعديل مسؤوليته.

## 1. شمولية الفهرس (`100% First-Party File Coverage`)

1. يجب فهرسة **كل ملف مملوك للمشروع (First-Party File)** بشكل فردي داخل `PROJECT_FILE_CATALOG.md`.
2. يُستثنى فقط مجلدات المكتبات الخارجية والكاش المؤقت المتفق عليها (`.git/`, `node_modules/`, `__pycache__/`, `.venv/`).
3. إذا اختلف الواقع الفعلي للملفات على القرص مع `PROJECT_FILE_CATALOG.md`، فإن شجرة الملفات الفعلية هي الحقيقة التقنية ويجب تحديث الفهرس فوراً وتشغيل `python tools/project_catalog/verify_catalog.py` للتأكد من `0 uncataloged files` و`0 stale paths`.

## 2. الحقول الإلزامية لكل ملف في الفهرس (`Required Catalog Fields`)

لكل ملف في `PROJECT_FILE_CATALOG.md` يجب تسجيل:
- **Path:** المسار النسبي من جذر المشروع.
- **Type:** نوع الملف (`Rule / Memory-Brain / Domain-Code / AI-Pipeline / Vector-Engine / API / UI-Canvas / Tooling / Spec`).
- **Purpose:** الغرض الهندسي المباشر من الملف.
- **Contents summary:** ملخص دقيق لمحتوياته (وللملفات البرمجية: رابط مباشر لملف المرآة الخاص به في `memory/code_mirrors/`).
- **Why it exists:** المشكلة التي يحلها في معمارية المشروع.
- **Current status:** حالته الحالية (`ACTIVE`, `BASELINE`, `IN_PROGRESS`, `VERIFIED`).
- **Source of truth / authority:** مرجعيته في النظام.
- **Update trigger:** متى يجب تحديث هذا الملف.
- **Related Files (`Yes / No`):**
  - إذا كان له ملفات مرتبطة، يجب ذكر كل ملف مرتبط مع:
    - **Relationship & Data Flow (`بياخد منين وبيرمي فين`):** هل يقرأ منه، يكتب إليه، يستدعي دواله، أو يتحقق منه؟
    - **Direction:** اتجاه العلاقة (`Upstream -> This` أو `This -> Downstream` أو `Bidirectional`).
    - **Change Impact:** ماذا يجب مراجعته أو تحديثه إذا تغير أحد الطرفين.
