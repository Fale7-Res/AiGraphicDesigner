# START CHANGE DELIVERY-INSTALL | 2026-10-25T15:01:53Z | CREATED | Author: parent
"""Verify staged files and install without overwriting existing project paths."""
from pathlib import Path, PurePosixPath
import argparse,copy,datetime,hashlib,json,shutil
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
MANIFEST=HERE/'DELIVERY_MANIFEST.json'
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def canonical_manifest_hash(record):
    clean=copy.deepcopy(record)
    for row in clean['files']:
        if row.get('hash_scheme')=='canonical_manifest_self_v1':row['size_bytes']=0;row['sha256']=None
    return hashlib.sha256(json.dumps(clean,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def verify():
    record=json.loads(MANIFEST.read_text());errors=[]
    for row in record['files']:
        rel=PurePosixPath(row['path'])
        if rel.is_absolute() or '..' in rel.parts:raise ValueError('Unsafe manifest path')
        path=ROOT.joinpath(*rel.parts)
        if path.is_symlink() or not path.is_file():errors.append(row['path']);continue
        actual=canonical_manifest_hash(record) if row.get('hash_scheme')=='canonical_manifest_self_v1' else digest(path)
        if actual!=row['sha256'] or path.stat().st_size!=row['size_bytes']:errors.append(row['path'])
    if errors:raise ValueError('Missing/tampered files: '+json.dumps(errors))
    return record
def install(record,destination):
    destination=destination.resolve()
    if destination==ROOT:raise ValueError('Install from staging into a separate directory')
    review=destination/'updates'/('REVIEW_COLLISIONS_VTRACER_'+datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%fZ'))
    result={'copied':[],'identical_skipped':[],'conflicts':[],'review_directory':str(review)}
    for row in record['files']:
        source=ROOT/row['path'];target=destination/row['path']
        if target.is_symlink() or any(p.is_symlink() for p in target.parents):raise ValueError('Symlink destination refused')
        if target.exists():
            if target.is_file() and digest(target)==digest(source):result['identical_skipped'].append(row['path']);continue
            target=review/row['path'];result['conflicts'].append(row['path'])
        else:result['copied'].append(row['path'])
        target.parent.mkdir(parents=True,exist_ok=True)
        with source.open('rb') as src,target.open('xb') as dst:shutil.copyfileobj(src,dst)
    return result
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--destination',type=Path);args=parser.parse_args();record=verify()
    print(json.dumps(install(record,args.destination) if args.destination else {'status':'PASS','verified_files':len(record['files'])},indent=2))
# END CHANGE DELIVERY-INSTALL | 2026-10-25T15:01:53Z | CREATED | Author: parent
