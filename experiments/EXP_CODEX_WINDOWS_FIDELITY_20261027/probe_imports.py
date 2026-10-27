"""Print immediate progress for dependency imports on native Windows."""
# START CHANGE AGD-CODEX-WIN-PROBE | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
import importlib
import faulthandler
import sys
import time
print(sys.executable,flush=True)
faulthandler.dump_traceback_later(15)
for name in ('PIL','numpy','psutil','scipy.ndimage','skimage.color','skimage.feature','skimage.metrics','vtracer','windows_search','optimizer'):
    start=time.perf_counter();print('Importing '+name,flush=True)
    module=importlib.import_module(name)
    print(name,str(getattr(module,'__version__','unknown')),time.perf_counter()-start,flush=True)
faulthandler.cancel_dump_traceback_later()
# END CHANGE AGD-CODEX-WIN-PROBE | 2026-10-27T10:19:50Z | CREATED | Author: windows_extension
