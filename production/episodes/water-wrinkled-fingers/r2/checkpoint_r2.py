from pathlib import Path
import json,hashlib,shutil,subprocess
r=Path(__file__).parent.resolve();repo=r.parent/'curio_r2';pub=repo/'production/episodes/water-wrinkled-fingers/r2';pub.mkdir(parents=True,exist_ok=True)
for n in ['film.js','animate.js','static_scene.js','build.py','render_chunks.cjs','encode.py','qa.py','check_finishing.cjs','checkpoint_r2.py','run_r2.py','episode.json','FINISHING_AUDIT.md']:
 if(r/n).exists():shutil.copy(r/n,pub/n)
for n in ['editorial-finish.js','finishing.js']:shutil.copy(r/'shared'/n,pub/n)
shutil.copy(r/'checks/finishing_verification.json',pub/'FINISHING_VERIFICATION.json')
src=json.loads((r/'r2_source_receipt.json').read_text())['results'][0];assert src['status']=='succeeded'and src['local_metadata_applied'];chunks=[]
for p in sorted((r/'chunks').glob('batch_*_manifest.json')):
 ds=json.loads(p.read_text());receipt=json.loads((r/'chunks'/('receipt_'+p.name.split('_')[1]+'.json')).read_text())['results'];byname={Path(x['local_path']).name:x for x in receipt};
 for d in ds:
  d['path']=Path(d['path']).name;d['status']='durable'
  for part in d['parts']:
   x=byname[part['name']];assert x['status']=='succeeded'and x['local_metadata_applied'];part.update(library_file_id=x['library_file_id'],file_id=x['file_id'])
  chunks.append(d)
d={'revision':'R2','status':'NATIVE CAPTURE / FINISHING CORRECTION','width':2160,'height':3840,'fps':30,'frames':1089,'duration':36.3,'studio_sha256':hashlib.sha256((r/'studio.html').read_bytes()).hexdigest(),'mix_sha256':hashlib.sha256((r/'audio/full_mix.wav').read_bytes()).hexdigest(),'audio':'Exact R1 full mix, no regeneration','source':{'library_file_id':src['library_file_id'],'file_id':src['file_id'],'sha256':hashlib.sha256((r/'Wrinkled_Fingers_R2_Checkpoint.zip').read_bytes()).hexdigest()},'chunks':chunks,'durable_frames':sum(c['count']for c in chunks)}
if d['durable_frames']==1089:d['status']='NATIVE CAPTURE COMPLETE / FINAL ENCODE PENDING'
(r/'recovery.json').write_text(json.dumps(d,indent=2));(pub/'RECOVERY.json').write_text(json.dumps(d,indent=2));print('DURABLE_FRAMES',d['durable_frames'],flush=True)
paths=subprocess.check_output(['git','-C',str(repo),'diff','--name-only'],text=True).splitlines()+subprocess.check_output(['git','-C',str(repo),'ls-files','--others','--exclude-standard'],text=True).splitlines();(r/'git_changes.json').write_text(json.dumps([{'path':p,'mode':'100644','type':'blob','content':(repo/p).read_text()}for p in paths if p.startswith(('production/episodes/water-wrinkled-fingers/r2/','production/engine/')) and Path(p).suffix in {'.py','.js','.cjs','.md','.json','.txt'}]))
