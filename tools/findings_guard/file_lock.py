#!/usr/bin/env python3
"""Cross-platform advisory inter-process locking for repository governance transactions.

No lock artifacts are written into the repository. OS releases locks on process death.
The lock guards cooperative CLI processes, not malicious filesystem writers.
"""
# START CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | CREATED | Author: Governance maintainer
from contextlib import contextmanager
from hashlib import sha256
from pathlib import Path
import os
import tempfile
import time


@contextmanager
def repository_lock(repository_root: Path, purpose: str, timeout_seconds: float = 90):
    """Hold a named OS lock across processes, supporting Windows and POSIX."""
    identifier = sha256(str(repository_root.resolve()).casefold().encode("utf-8")).hexdigest()[:22]
    lockfile = Path(tempfile.gettempdir()) / f"agd-{purpose}-{identifier}.lock"
    handle = open(lockfile, "a+b")
    acquired = False
    try:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        end = time.monotonic() + timeout_seconds
        if os.name == "nt":
            import msvcrt
            while not acquired:
                try:
                    handle.seek(0)
                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                    acquired = True
                except OSError:
                    if time.monotonic() >= end:
                        raise TimeoutError(f"Timed out acquiring {purpose} lock")
                    time.sleep(0.05)
        else:
            import fcntl
            while not acquired:
                try:
                    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                    acquired = True
                except BlockingIOError:
                    if time.monotonic() >= end:
                        raise TimeoutError(f"Timed out acquiring {purpose} lock")
                    time.sleep(0.05)
        yield
    finally:
        if acquired:
            if os.name == "nt":
                import msvcrt
                handle.seek(0)
                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()
# END CHANGE GOV-FINAL-20261017 | 2026-10-17T06:49:23Z | CREATED
