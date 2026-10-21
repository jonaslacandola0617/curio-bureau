from pathlib import Path
import subprocess,os,json,hashlib
P=Path(__file__).resolve().parent;repo=os.environ['GH_REPO'];target=os.environ['SOURCE_COMMIT'];tag='immune-defense-motion-v1-20261021'
def run(a):subprocess.run(list(map(str,a)),check=True)
def out(a):return subprocess.check_output(list(map(str,a))).decode()
def rec(f):return {'file':f.name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
freeze=json.loads((P/'SOURCE_FREEZE.json').read_text())
for x in freeze['inputs']:assert hashlib.sha256((P/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
run(['python',P/'download_assets.py']);run(['python',P/'prepare_timeline.py']);run(['python',P/'render_movie.py']);run(['node',P/'ending.cjs']);run(['python',P/'prove_runtime.py'])
tl=json.loads((P/'timeline.json').read_text());chunks=P/'chunks';chunks.mkdir(exist_ok=True);records=[];pending=[]
if subprocess.run(['gh','release','view',tag,'--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:
 run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Curio Bureau — Immune defense full motion review v1','--notes','Owner-approved artwork with requested saturated yellow/red. Natural Bernard; scientific context remains source-qualified. Review export, not social publication or final listening/caption/clinical approval. Frozen source: '+target])
def upload(fs):
 run(['gh','release','upload',tag,'--repo',repo,*fs])
 for f in fs:
  r=rec(f);r['download_url']=f'https://github.com/{repo}/releases/download/{tag}/{f.name}'
  if f.suffix=='.mkv':
   z=f.stem.split('-');r.update({'start_frame':int(z[1]),'end_frame_exclusive':int(z[2]),'role':'lossless native RGB recovery'})
  records.append(r)
 (P/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':[r for r in records if r['file'].endswith('.mkv')]},indent=2)+'\n')
for start in range(0,tl['frames'],300):
 end=min(tl['frames'],start+300);f=chunks/f'frames-{start:05}-{end:05}.mkv';run(['python',P/'render_movie.py','--chunk',start,end,f])
 count=int(out(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',f]).strip());assert count==end-start
 pending.append(f)
 if len(pending)==2:upload(pending);pending=[]
if pending:upload(pending)
manifest=chunks/'concat.txt';manifest.write_text(''.join("file '"+str(f.resolve())+"'\n"for f in sorted(chunks.glob('*.mkv'))))
movie=P/'Curio-Immune-Defense-Full-Review-v1.mp4'
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-i',P/'audio/soundtrack.flac','-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart',movie])
upload([movie])
r=rec(movie);r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{movie.name}','source_commit':target,'status':'ARCHIVED_FULL_MOTION_REVIEW','duration_seconds':tl['duration'],'native':[1080,1920],'delivery_fps':30,'scene_fps':12,'owner_art_approval':'APPROVED with saturated yellow/red correction','owner_motion_full_film_approval':'PENDING','independent_listening':'PENDING','exact_caption_boundaries':'Actual audio ASR; independent verification pending','clinical_wording_human_review':'PENDING','publication':'NOT AUTHORIZED / NOT PERFORMED'})
(P/'DELIVERY.json').write_text(json.dumps(r,indent=2)+'\n')
run(['ffmpeg','-v','error','-xerror','-i',movie,'-f','null','-']);(P/'TECHNICAL_PROBE.json').write_text(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
run(['gh','release','upload',tag,'--repo',repo,P/'DELIVERY.json',P/'RECOVERY.json',P/'TECHNICAL_PROBE.json',P/'SOURCE_FREEZE.json',P/'OWNER_APPROVAL.md',P/'review/FINISHING_RUNTIME.json',P/'review/PREFLIGHT_GATES.json',P/'FINISHING_COVERAGE.json',P/'audio/VOICE_EDITS.json',P/'timeline.json'])
print('DELIVERY_ARCHIVED',json.dumps(r),flush=True)
