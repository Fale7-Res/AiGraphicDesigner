<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "CREATED", "last_change_id": "TASK-MULTI-VER-01", "last_edited_at_utc": "2026-10-17T08:58:05Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# Architecture Version 03: Diffusion Latent Decomposition & Dual-Path Typography (`versions/version-03/`)

**معرف الإصدار:** `version-03`  
**الفرضية المعمارية:** تفكيك الطبقات في الفضاء الكامن لشبكات الانتشار مع مسار مزدوج للخط العربي يجمع بين مسارات المنحنيات ومطابقة عائلة الخط والوزن.  
**حالة الاعتماد:** هيكل تجريبي مقترح (`PROPOSED_EXPERIMENTAL_SKELETON — NOT_APPROVED`)  
**الوكيل المنفذ المسؤول:** `scene-and-vision-agent` & `vector-and-typography-agent`

---

## 1. هيكل المجلد (`Version Tree`)

```
versions/version-03/
├── README.md                           # هذه الوثيقة
├── PROJECT_FILE_CATALOG.md             # الفهرس الحي لملفات الإصدار وعلاقاتها
├── dependencies/
│   └── requirements.txt                # الاعتماديات الخاصة بهذا الإصدار
├── docs/
│   ├── ARCHITECTURE.md                 # التوصيف المعماري التفصيلي
│   ├── FUNCTION_REGISTRY.md            # سجل الدوال المعزول الخاص بالإصدار
│   └── CODE_MIRRORS/                   # مرايا الكود المعزولة 1:1
│       └── src/
│           ├── geometry/
│           │   └── bezier.py.md
│           └── pipeline.py.md
├── experiments/
│   ├── EXPERIMENT_CONFIG.json          # إعدادات التجارب القياسية
│   └── EXPERIMENT_LOG.md               # سجل الملاحظات والنتائج التجريبية
├── src/
│   ├── geometry/
│   │   └── bezier.py                   # استخراج المنحنيات الدقيقة للأحرف والشعارات
│   └── pipeline.py                     # خط الأنابيب الكامن والتيبوجرافي ثنائي المسار
└── tests/
    └── test_version.py                 # اختبارات التحقق من صحة الإصدار
```

---

## 2. تعليمات التشغيل والاختبار (`Verification Guide`)

- توليد وتحديث المرايا وسجل الدوال الخاص بالإصدار:
  `python tools/memory_guard/sync_code_mirrors.py --version version-03 --write`
- توليد وتحديث فهرس الملفات الخاص بالإصدار:
  `python tools/project_catalog/build_catalog.py --version version-03 --write`
- تشغيل اختبارات الإصدار:
  `python -m unittest versions/version-03/tests/test_version.py`
