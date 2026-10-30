# START CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
"""Monitor owned worker process trees, including Windows venv launchers."""
from pathlib import Path
import subprocess,time,psutil,json

def supervise(args,log,wall_seconds=300,memory_mib=768,reserve_mib=700,interval=.1):
    started=time.monotonic();peak=0;root_peak=0;seen={};status='COMPLETED';samples=0;cpu_peak=0.
    with Path(log).open('w',encoding='utf-8') as stream:
        job=subprocess.Popen(list(map(str,args)),stdout=stream,stderr=subprocess.STDOUT)
        while job.poll() is None:
            try:
                root=psutil.Process(job.pid);members=[root]+root.children(recursive=True)
                rss=0;cpu=0.
                for p in members:
                    try:
                        mem=p.memory_info().rss;rss+=mem;seen[p.pid]=max(seen.get(p.pid,0),mem)
                        times=p.cpu_times();cpu+=times.user+times.system
                        if p.pid==job.pid:root_peak=max(root_peak,mem)
                    except psutil.Error:pass
                peak=max(peak,rss);cpu_peak=max(cpu_peak,cpu);samples+=1
            except psutil.Error:pass
            if time.monotonic()-started>wall_seconds:status='STOPPED_TIME'
            elif peak>memory_mib*2**20:status='STOPPED_MEMORY'
            elif psutil.virtual_memory().available<reserve_mib*2**20:status='STOPPED_AVAILABLE_RAM'
            if status!='COMPLETED':
                try:
                    root=psutil.Process(job.pid)
                    for p in root.children(recursive=True)[::-1]:
                        try:p.kill()
                        except psutil.Error:pass
                    root.kill()
                except psutil.Error:pass
                break
            time.sleep(interval)
        code=job.wait()
    return {'status':status if code==0 or status!='COMPLETED' else 'FAILED','exit_code':code,'wall_seconds':time.monotonic()-started,'sampled_tree_RSS_peak_mib':peak/2**20,'sampled_root_RSS_peak_mib':root_peak/2**20,'observed_pid_peak_bytes':seen,'sample_count':samples,'sample_interval_seconds':interval,'sampled_tree_cpu_seconds_highwater':cpu_peak,'memory_limit_mib':memory_mib,'limitations':'SummedworkingRSSmaydoublecountsharedpages; samplingcanmisspeaks; notexactmaximum. AllchildPIDsownedbythisworker.'}

# END CHANGE AGD-CONTOUR-CONSTRUCTION | 2026-10-30T08:44:39Z | CREATED | Author: root
