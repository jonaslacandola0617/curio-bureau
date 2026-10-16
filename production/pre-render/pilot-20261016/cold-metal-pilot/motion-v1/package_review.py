from pathlib import Path
import zipfile,json,hashlib,shutil,subprocess,os
repo=Path(__file__).resolve().parents[5];r=Path(__file__).resolve().parent;project=r.parent
# Whole repo-relative layout preserves engine/assets/cue references on restoration.
files=set()
for p in r.rglob('*'):
 if not p.is_file()or '__pycache__'in p.parts or p.name.startswith('debug_')or p.suffix in {'.zip','.mp4','.webm','.partial'}or p.name in {'RENDER_PROGRESS.json','DELIVERY_MANIFEST.json','CHECKSUMS.sha256','RESTORE_QA.json'}:continue
 files.add(p)
for p in (project/'art-v1/assets').iterdir():files.add(p)
for name in ['art.cjs','ASSETS.json','GENERATION_PROMPTS.json','README.md']:
 files.add(project/'art-v1'/name)
for name in ['sequence_contract.json','OWNER_ART_APPROVAL.md','RESEARCH.md','NARRATION.md','package.json']:files.add(project/name)
for name in ['sequence.py','finishing_contract.py','finishing_audit.py','FINISHING_CHECKLIST.md']:
 files.add(repo/'production/engine'/name)
files.add(repo/'production/engine/browser/finishing.js')
files.add(repo/'production/engine/FINISHING_OUTPUT_CONTRACT.md')
for name in ['camera_move.mp3','marker_bold.mp3','paper.mp3','pencil.mp3','CATALOG.json','README.md']:
 files.add(repo/'audio/generated-editorial-v1'/name)
files.add(repo/'AGENTS.md');files.add(repo/'production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md')
manifest={str(p.relative_to(repo)):hashlib.sha256(p.read_bytes()).hexdigest()for p in sorted(files)}
archive=r/'Cold_Metal_Source_Package.zip'
temp=r/'Cold_Metal_Source_Package.partial'
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED,compresslevel=5)as z:
 for p in sorted(files):z.write(p,str(p.relative_to(repo)))
 z.writestr('PACKAGE_HASHES.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(temp)as z:assert z.testzip()is None
os.replace(temp,archive)
check=repo.parent/'cold_metal_source_restore_check';check.mkdir(exist_ok=True)
with zipfile.ZipFile(archive)as z:
 assert z.testzip()is None;z.extractall(check)
for name,digest in manifest.items():assert hashlib.sha256((check/name).read_bytes()).hexdigest()==digest,name
restored=check/r.relative_to(repo);subprocess.run(['python3',str(restored/'preflight.py')],check=True)
(r/'RESTORE_QA.json').write_text(json.dumps({'zip_integrity':'PASS','files_verified':len(manifest),'all_file_hashes_match':True,'clean_extracted_preflight':'PASS','new_voice_or_sfx_generation':False,'path_layout':'repo-relative, preserving source references','movies_in_archive':False,'movie_exports_archived_separately':True,'zip_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'zip_bytes':archive.stat().st_size},indent=2)+'\n')
shutil.copyfile(r/'Encoded_Review.jpg',r/'Cold_Metal_Review.jpg')
for name in ['Cold_Metal_Sequence.mp4','Cold_Metal_Sequence.webm','Cold_Metal_Source_Package.zip','Cold_Metal_Review.jpg','Review.html']:assert(r/name).is_file()
(r/'CHECKSUMS.sha256').write_text(''.join(hashlib.sha256((r/name).read_bytes()).hexdigest()+'  '+name+'\n'for name in ['Cold_Metal_Sequence.mp4','Cold_Metal_Sequence.webm','Cold_Metal_Source_Package.zip','Cold_Metal_Review.jpg','Review.html']))
print('Review package restored and verified:',len(manifest),'files;',archive.stat().st_size,'bytes')
