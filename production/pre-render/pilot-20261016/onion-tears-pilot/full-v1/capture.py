from pathlib import Path
import subprocess,json,sys,os,hashlib,concurrent.futures
r=Path(__file__).parent;tl=json.loads((r/'timeline.json').read_text());finger=json.loads((r/'SOURCE_FINGERPRINT.json').read_text())
assert finger.get('source_commit') and finger['source_commit']!='PENDING'
for f in finger['files']:assert hashlib.sha256((r/f['path']).read_bytes()).hexdigest()==f['sha256'],f['path']
manifest=r/'RECOVERY.json';d=json.loads(manifest.read_text()) if manifest.exists()else {'schema':1,'source_commit':finger['source_commit'],'total_frames':tl['frames'],'chunk_size':240,'format':'FFV1 lossless BGRA native1080x1920/30','chunks':[]}
existing={c['start_frame']:c for c in d['chunks']};starts=list(range(0,tl['frames'],240));pending=[s for s in starts if s not in existing or existing[s]['archive_status']!='DURABLE'];pending=pending[:2]
# Native streams retain one frame per pipe; two workers capped, no browser frame accumulation.
(r/'chunks').mkdir(exist_ok=True)
def work(start):
 end=min(start+240,tl['frames']);name=f'Onion-lossless-{start:05d}-{end-1:05d}.mkv';p=r/'chunks'/name
 with (r/'chunks'/f'{start:05d}.log').open('w')as log:subprocess.run([os.environ['CODEX_PRIMARY_RUNTIME_NODE'],str(r/'render.cjs'),'worker',str(start),str(end),str(p)],check=True,stdout=log,stderr=subprocess.STDOUT)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',str(p)]));v=probe['streams'][0];assert int(v['nb_read_frames'])==end-start and(v['width'],v['height'])==(1080,1920)
 return {'file':name,'start_frame':start,'count':end-start,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'archive_status':'LOCALLY_VERIFIED','source_commit':finger['source_commit']}
with concurrent.futures.ThreadPoolExecutor(max_workers=2)as pool:
 for c in pool.map(work,pending):
  d['chunks']=[x for x in d['chunks']if x['start_frame']!=c['start_frame']]+[c];manifest.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(c),flush=True)
print('BATCH CLOSED — archive these actual chunks before the next capture batch',flush=True)
