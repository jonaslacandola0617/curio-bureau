from pathlib import Path
import json,hashlib,zipfile,os,subprocess,shutil
repo=Path(__file__).resolve().parents[5];r=Path(__file__).resolve().parent;project=r.parent;files=set()
for p in r.rglob('*'):
 if not p.is_file()or p.name.startswith('.')or '__pycache__'in p.parts or 'chunks'in p.parts or p.suffix in {'.mp4','.webm','.zip','.log'}or p.name in {'DELIVERY_MANIFEST.json','DOWNLOADS.md','CHECKSUMS.sha256','RESTORE_QA.json','RENDER_PROGRESS.json','native-preview.png'}:continue
 files.add(p)
for p in (project/'art-v1').iterdir():
 if p.suffix in {'.md','.json','.cjs'}:files.add(p)
for p in (project/'art-v1/assets').iterdir():files.add(p)
for name in ['OWNER_ART_APPROVAL.md','sequence_contract.json','RESEARCH.md','NARRATION.md','package.json']:files.add(project/name)
for name in ['sequence.py','finishing_contract.py','finishing_audit.py','FINISHING_CHECKLIST.md','FINISHING_OUTPUT_CONTRACT.md','NATIVE_RENDER_RECOVERY.md','NARRATION_TAIL_QA.md','requirements.lock.json']:files.add(repo/'production/engine'/name)
files.add(repo/'production/engine/browser/finishing.js')
for name in ['camera_move.mp3','ink.mp3','marker_bold.mp3','paper.mp3','pencil.mp3','CATALOG.json','README.md']:files.add(repo/'audio/generated-editorial-v1'/name)
for name in ['AGENTS.md','production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md','production/approved-benchmarks/IMAGE_LED_OWNER_DIRECTION.md','production/audio-sfx-v1/SOUND_DIRECTION_GUIDE.md']:files.add(repo/name)
manifest={str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(files)}
archive=r/'Cold_Metal_R2_Source.zip';tmp=archive.with_suffix('.partial.zip')
with zipfile.ZipFile(tmp,'w',zipfile.ZIP_DEFLATED,compresslevel=5)as z:
 for p in sorted(files):z.write(p,str(p.relative_to(repo)))
 z.writestr('PACKAGE_HASHES.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(tmp)as z:assert z.testzip()is None
os.replace(tmp,archive)
restore=Path('/tmp/curio-r2-clean-restore');restore.mkdir(exist_ok=True)
with zipfile.ZipFile(archive)as z:z.extractall(restore)
for name,digest in manifest.items():assert hashlib.sha256((restore/name).read_bytes()).hexdigest()==digest,name
subprocess.run(['python3',str(restore/r.relative_to(repo)/'preflight.py')],check=True)
report={'zip_crc':'PASS','file_hashes':'PASS','files':len(manifest),'clean_extracted_preflight':'PASS','bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'movie_and_lossless_chunk_assets':'Archived separately in the same GitHub Release, referenced by durable GitHub asset IDs in RECOVERY.json'}
(r/'RESTORE_QA.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report),flush=True)
