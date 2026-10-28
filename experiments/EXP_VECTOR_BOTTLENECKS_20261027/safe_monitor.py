"""Bounded isolated Windows research workers; PID reuse guarded, no history edits."""
# START CHANGE AGD-BOTTLENECK-MONITOR | 2026-10-28T03:34:28Z | EDITED | Author: root
import subprocess,time,os
from pathlib import Path
import psutil

def monitor(command,log,timeout=900,memory_mib=4096):
    start=time.monotonic();peak=0;samples=0;reason=None;identities={}
    with Path(log).open('w',encoding='utf-8') as stream:
        p=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        root=psutil.Process(p.pid)
        while p.poll() is None:
            try:members=[root]+root.children(recursive=True)
            except psutil.Error:members=[]
            rss=0
            for child in members:
                try:identities[(child.pid,child.create_time())]=None;rss+=child.memory_info().rss
                except psutil.Error:pass
            peak=max(peak,rss);samples+=1
            if time.monotonic()-start>timeout:reason='timeout';break
            if rss>memory_mib*1024**2:reason='sampled_memory_limit';break
            time.sleep(.05)
        if reason:
            for pid,birth in identities:
                try:
                    child=psutil.Process(pid)
                    if child.create_time()==birth:child.kill()
                except psutil.Error:pass
            if p.poll() is None:p.kill()
        code=p.wait(timeout=15)
        remaining=[]
        if reason:
            deadline=time.monotonic()+2
            while True:
                remaining=[]
                for pid,birth in identities:
                    try:
                        child=psutil.Process(pid)
                        if child.create_time()==birth and child.is_running():remaining.append(pid)
                    except psutil.NoSuchProcess:pass
                    except psutil.Error:remaining.append(pid)
                if not remaining or time.monotonic()>=deadline:break
                time.sleep(.05)
    return {'returncode':code,'termination_reason':reason,'wall_seconds':time.monotonic()-start,'sampled_tree_peak_mib':peak/1024**2,'samples':samples,'cleanup_unverified_pids':remaining,'note':'50ms requested sampling plus enumeration overhead; PID/create-time identity checked before killing only owned observed workers; bounded2s descendant drain ontimeout, errors reported not hidden; short peaks or unobserved descendants may be missed'}
# END CHANGE AGD-BOTTLENECK-MONITOR | 2026-10-28T03:34:28Z | EDITED | Author: root
