from pathlib import Path
import json,sys,subprocess,hashlib
r=Path(__file__).resolve().parent;repo=r.parents[3];sys.path.insert(0,str(repo/'production/engine'))
from finishing_contract import validate_finishing
tl=json.loads((r/'timeline.json').read_text());config=json.loads((r/'FINISHING_CONFIG.json').read_text())
print(validate_finishing(config,r,stage='release',expected_size=[1080,1920]),flush=True)
source=json.loads((r/'SOURCE_FINGERPRINT.json').read_text())
for f in source['inputs']:
 p=(r/f['path']).resolve();assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f['path']
record=r/'RECOVERY.json';data=json.loads(record.read_text()) if record.exists() else {'fps':30,'width':1080,'height':1920,'total_frames':tl['frames'],'chunks':[]}
start=int(sys.argv[1]);stop=min(int(sys.argv[2]),tl['frames'])
for a in range(start,stop,240):
 b=min(a+240,stop);p=r/'chunks'/f'Phantom-lossless-{a:05}-{b-1:05}.mkv'
 old=next((x for x in data['chunks'] if x['start']==a and x['end']==b),None)
 if old and p.exists() and hashlib.sha256(p.read_bytes()).hexdigest()==old['sha256']:print('Reuse verified',p.name,flush=True);continue
 subprocess.run(['node',str(r/'render.cjs'),'worker',str(a),str(b),str(p)],check=True)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(p)]))['streams'][0]
 assert int(probe['nb_read_frames'])==b-a and probe['width']==1080 and probe['height']==1920
 entry={'file':'chunks/'+p.name,'start':a,'end':b,'frames':b-a,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_fingerprint_sha256':hashlib.sha256((r/'SOURCE_FINGERPRINT.json').read_bytes()).hexdigest(),'archive_status':'LOCALLY_VERIFIED_ARCHIVE_PENDING'}
 data['chunks']=[x for x in data['chunks'] if x['start']!=a]+[entry];data['chunks'].sort(key=lambda x:x['start']);record.write_text(json.dumps(data,indent=2)+'\n');print('CLOSED_VERIFIED',json.dumps(entry),flush=True)
print('PAUSED: archive these closed chunks before another pair.',flush=True)
