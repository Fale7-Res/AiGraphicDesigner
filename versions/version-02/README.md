<!-- DOC_PROVENANCE
{"created_at_utc": "2026-10-17T08:58:05Z", "last_action": "CREATED", "last_change_id": "TASK-MULTI-VER-01", "last_edited_at_utc": "2026-10-17T08:58:05Z", "last_editor": "orchestrator-planner", "tracking_started_at_utc": "2026-10-17T08:58:05Z"}
END_DOC_PROVENANCE -->
# Architecture Version 02: Hierarchical Scene Graph & Vector Optimization (`versions/version-02/`)

**معرف الإصدار:** `version-02`  
**الفرضية المعمارية:** تمثيل التصميم عبر `Design IR` المنفصل مع توحيد المسارات بالاتحاد البوليني ومسارات القص `<clipPath>` لحصر الظلال دون تفتيت مع تمكين مقابض أداة القلم التفاعلية.  
**حالة الاعتماد:** هيكل تجريبي مقترح (`PROPOSED_EXPERIMENTAL_SKELETON — NOT_APPROVED`)  
**الوكيل المنفذ المسؤول:** `vector-and-typography-agent` & `fullstack-canvas-agent`

---

## 1. هيكل المجلد (`Version Tree`)

```
versions/version-02/
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
│   │   └── bezier.py                   # خوارزمية بيزييه مع الاتحاد البوليني ومسارات القص
│   └── pipeline.py                     # خط الأنابيب الهرمي وشجرة المشهد (Design IR)
└── tests/
    └── test_version.py                 # اختبارات التحقق من صحة الإصدار
```

---

## 2. تعليمات التشغيل والاختبار (`Verification Guide`)

- توليد وتحديث المرايا وسجل الدوال الخاص بالإصدار:
  `python tools/memory_guard/sync_code_mirrors.py --version version-02 --write`
- توليد وتحديث فهرس الملفات الخاص بالإصدار:
  `python tools/project_catalog/build_catalog.py --version version-02 --write`
- تشغيل اختبارات الإصدار:
  `python -m unittest versions/version-02/tests/test_version.py`
