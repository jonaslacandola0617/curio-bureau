from pathlib import Path
import subprocess,json,hashlib,os,shutil
r=Path(__file__).resolve().parent;out=r/'native';out.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args):subprocess.run([str(x) for x in args],check=True)
def save(files):
 p=subprocess.run(['python3',r/'native_save_helpers/library_upload.py'],input=json.dumps({'uploads':files}),capture_output=True,text=True)
 if p.returncode:raise RuntimeError('Persistent checkpoint save failed: '+p.stderr[-1200:])
 lines=[l for l in p.stdout.splitlines() if l.startswith('{"results"')]
 if not lines:raise RuntimeError('Missing upload receipt')
 result=json.loads(lines[-1])['results']
 if len(result)!=len(files) or any(x['status']!='succeeded' for x in result):raise RuntimeError('Some checkpoint saves failed: '+str(result))
 return result
inputs={str(p.relative_to(r)):digest(p) for p in [r/'build/Studio.html',r/'project/assets/preflight_mix.wav',r/'native_chunk_render.cjs']}
manifest=out/'Recorded_Voice_Native_Recovery.json'
if manifest.exists():
 state=json.loads(manifest.read_text())
 if state['inputs']!=inputs:raise ValueError('Inputs changed; do not reuse stale native chunks')
else:state={'status':'NATIVE RENDER IN PROGRESS','owner_approval':'15 October 2026 Asia/Manila: alright, render 4K and write posts','source_bundle_id':'libfile_06b39caebf8c8191b08f220647920aed','inputs':inputs,'width':2160,'height':3840,'fps':30,'total_frames':1058,'chunks':[]}
def record():
 manifest.write_text(json.dumps(state,indent=2));ref=state.get('manifest_identity');job={'local_path':str(manifest),'purpose':'replace_library_file' if ref else 'create_library_file'}
 if ref:job.update(library_file_id=ref['library_file_id'],expected_current_version=ref['current_version_number'],version_reason='Completed native frame ranges and saved recovery identities')
 else:job['library_artifact_type']='other'
 result=save([job])[0];state['manifest_identity']={k:result[k] for k in ['library_file_id','file_id','current_version_number']};manifest.write_text(json.dumps(state,indent=2));print('Checkpoint manifest saved',flush=True)
if not state.get('manifest_identity'):record()
for start in range(0,1058,80):
 count=min(80,1058-start);old=next((c for c in state['chunks'] if c['start_frame']==start),None)
 if old and all((out/x['name']).exists() and digest(out/x['name'])==x['sha256'] for x in old['outputs']):print('Reusing verified range',start,flush=True);continue
 outputs=[{'kind':k,'path':str(out/f'Recorded_Voice_Native_{start:04}_{k}{ext}')} for k,ext in [('master','.mp4'),('webm','.webm'),('download','.mp4')]]
 cfg={'studio':str(r/'build/Studio.html'),'chrome':str(r/'runtime/chrome-headless-shell-linux64/chrome-headless-shell'),'scale':2,'start':start/30,'frames':count,'outputs':outputs,'progress':str(out/'capture_progress.json')}
 req=out/'chunk_request.json';req.write_text(json.dumps(cfg));run([os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node'),r/'native_chunk_render.cjs',req])
 info=[]
 for x in outputs:
  p=Path(x['path']);v=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-of','json',p]))['streams'][0]
  if (v['width'],v['height'],int(v['nb_read_frames']),v['r_frame_rate'])!=(2160,3840,count,'30/1'):raise ValueError('Bad native range')
  info.append({'name':p.name,'kind':x['kind'],'size':p.stat().st_size,'sha256':digest(p),'frames':count})
 receipts=save([{'local_path':x['path'],'purpose':'create_library_file','library_artifact_type':'other'} for x in outputs])
 for item,receipt in zip(info,receipts):item.update({k:receipt[k] for k in ['library_file_id','file_id']})
 state['chunks']=[c for c in state['chunks'] if c['start_frame']!=start]+[{'start_frame':start,'frame_count':count,'outputs':info}];record();print('DURABLE RANGE',start,'to',start+count-1,'/',1058,flush=True)
state['status']='ALL NATIVE RANGES SAVED — ASSEMBLING';record()
for kind,name,codec,rate in [('master','Recorded_Voice_4K_Master.mp4','aac','320k'),('webm','Recorded_Voice_4K.webm','libopus','256k'),('download','Recorded_Voice_4K_Upload.mp4','aac','320k')]:
 parts=[out/next(x['name'] for x in c['outputs'] if x['kind']==kind) for c in sorted(state['chunks'],key=lambda c:c['start_frame'])]
 listing=out/(kind+'_concat.txt');listing.write_text(''.join("file '"+str(p)+"'\n" for p in parts))
 target=r/name
 args=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',listing,'-i',r/'project/assets/preflight_mix.wav','-map','0:v','-map','1:a','-c:v','copy','-c:a',codec,'-b:a',rate,'-ar','48000','-ac','2','-t',str(1058/30)]
 if codec=='aac':args+=['-movflags','+faststart']
 run(args+[target]);print('Assembled',target.name,flush=True)
state['status']='ASSEMBLED — FINAL ENCODED QA PENDING';record()
