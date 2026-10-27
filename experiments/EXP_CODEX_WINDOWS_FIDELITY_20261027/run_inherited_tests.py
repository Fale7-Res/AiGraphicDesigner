"""Run historical tests unchanged, explicitly against the Windows derived optimizer."""
# START CHANGE AGD-CODEX-WIN-TESTS | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
import hashlib
import importlib.util
import json
import sys
import unittest
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
import optimizer
HISTORY=ROOT.parent/'EXP_ADAPTIVE_VTRACER_20261027'/'test_optimizer.py'

def run_tests() -> bool:
    """Load exact historical bytes, keeping unittest patch target optimizer local."""
    spec=importlib.util.spec_from_file_location('historical_optimizer_tests_unchanged',HISTORY)
    tests=importlib.util.module_from_spec(spec);spec.loader.exec_module(tests)
    suite=unittest.defaultTestLoader.loadTestsFromModule(tests)
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    # START CHANGE AGD-CODEX-WIN-TEST-EVIDENCE | 2026-10-27T10:27:57Z | EDITED | Author: windows_extension
    report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),
            'python_executable':sys.executable,'python_version':sys.version,'vtracer_version':version('vtracer'),
            'test_source':str(HISTORY),'test_source_sha256':hashlib.sha256(HISTORY.read_bytes()).hexdigest(),
            'optimizer_under_test':str(Path(optimizer.__file__).resolve()),
            'scope':'unchanged four historical tests against Windows-derived optimizer; historical direct Windows import remains unsupported',
            'tests_run':result.testsRun,'errors':len(result.errors),'failures':len(result.failures),
            'passed':result.wasSuccessful(),
            'error_details':[(str(test),traceback) for test,traceback in result.errors],
            'failure_details':[(str(test),traceback) for test,traceback in result.failures]}
    # END CHANGE AGD-CODEX-WIN-TEST-EVIDENCE | 2026-10-27T10:27:57Z | EDITED | Author: windows_extension
    (ROOT/'reports').mkdir(exist_ok=True)
    (ROOT/'reports'/'inherited_tests.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    return result.wasSuccessful()

if __name__=='__main__': raise SystemExit(0 if run_tests() else 1)
# END CHANGE AGD-CODEX-WIN-TESTS | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
