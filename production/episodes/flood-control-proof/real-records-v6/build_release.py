from pathlib import Path
import os,subprocess,json,hashlib
P=Path(__file__).resolve().parent;repo=os.environ['GH_REPO'];target=os.environ['SOURCE_COMMIT'];tag='flood-proof-real-records-v6-20261021'
def run(a):subprocess.run(list(map(str,a)),check=True)
def out(a):return subprocess.check_output(list(map(str,a))).decode()
def rec(p):
 r={'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
 if p.suffix=='.mkv':
  z=p.stem.split('-');r.update({'start_frame':int(z[1]),'end_frame_exclusive':int(z[2]),'role':'lossless native RGB recovery chunk'})
 else:r['role']='completed review movie'
 return r
freeze=json.loads((P/'SOURCE_FREEZE.json').read_text())
for item in freeze['inputs']:
 path=(Path(os.environ['CURIO_REPO_ROOT'])/item['repository_path'])if item.get('repository_path')else P/item['path']
 assert hashlib.sha256(path.read_bytes()).hexdigest()==item['sha256'],str(path)
run(['ffmpeg','-v','error','-xerror','-i',P/'audio/soundtrack.flac','-f','null','-'])
audio_duration=float(out(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',P/'audio/soundtrack.flac']).strip())
assert abs(audio_duration-json.loads((P/'timeline.json').read_text())['duration'])<.001
if subprocess.run(['gh','release','view',tag,'--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:
 run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Flood-control proof — real records v6 review','--notes','Owner-commissioned render using actual USACE flood-event footage, published comparison and JICA evaluation. Review export; no social publication or owner approval implied. Source: '+target])
run(['python',P/'recover_sources.py'])
for kind,name in [('hickory','old-hickory.mp4'),('cordell','cordell-hull.mp4')]:
 dest=P/'frames'/kind;dest.mkdir(parents=True,exist_ok=True)
 run(['ffmpeg','-v','error','-y','-i',P/'assets'/name,'-vf','fps=12,scale=1080:-2','-q:v','3',dest/'%04d.jpg'])
run(['python',P/'render.py']);run(['node',P/'ending.cjs'])
# Custom capture cannot bypass the existing production/finishing gates.
run(['python',P/'prove_finishing.py'])
tl=json.loads((P/'timeline.json').read_text());chunks=P/'chunks';chunks.mkdir(exist_ok=True);records=[];pending=[]
def upload(files):
 run(['gh','release','upload',tag,'--repo',repo,*files])
 for p in files:
  r=rec(p);r['download_url']=f'https://github.com/{repo}/releases/download/{tag}/{p.name}';records.append(r)
 (P/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':[r for r in records if r['file'].endswith('.mkv')]},indent=2)+'\n')
release=json.loads(out(['gh','api',f'repos/{repo}/releases/tags/{tag}']))
existing={a['name']:a for a in release['assets']}
if existing and release.get('target_commitish')!=target:raise RuntimeError('Existing release binds another source commit; preserve it and version the changed render')
for start in range(0,tl['frames'],300):
 end=min(start+300,tl['frames']);f=chunks/f'frames-{start:05}-{end:05}.mkv'
 if f.name in existing:
  run(['gh','release','download',tag,'--repo',repo,'--pattern',f.name,'--dir',chunks,'--clobber'])
  expected=existing[f.name].get('digest')
  if expected:assert 'sha256:'+hashlib.sha256(f.read_bytes()).hexdigest()==expected
 else:run(['python',P/'render.py','--chunk',start,end,f])
 count=int(out(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',f]).strip());assert count==end-start
 if f.name in existing:
  r=rec(f);r['download_url']=existing[f.name]['browser_download_url'];records.append(r)
 else:pending.append(f)
 if len(pending)==2:upload(pending);pending=[]
if pending:upload(pending)
manifest=P/'chunks/concat.txt';manifest.write_text(''.join("file '"+str(p.resolve())+"'\n"for p in sorted(chunks.glob('*.mkv'))))
movie=P/'Curio-Flood-Proof-Real-Records-v6.mp4'
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-i',P/'audio/soundtrack.flac','-c:v','libx264','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',movie])
# Archive the completed movie before extended review.
upload([movie])
receipt=rec(movie);receipt.update({'source_commit':target,'release_tag':tag,'download_url':f'https://github.com/{repo}/releases/download/{tag}/{movie.name}','status':'ARCHIVED_FOR_REVIEW','owner_full_approval':'PENDING','independent_listening':'PENDING','caption_boundaries':'actual-audio ASR estimates, script reconciled; independent verification pending'})
(P/'DELIVERY.json').write_text(json.dumps(receipt,indent=2)+'\n')
run(['ffmpeg','-v','error','-i',movie,'-f','null','-'])
(P/'TECHNICAL_PROBE.json').write_text(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
run(['ffmpeg','-v','info','-i',movie,'-af','loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json','-f','null','-'])
run(['gh','release','upload',tag,'--repo',repo,P/'DELIVERY.json',P/'RECOVERY.json',P/'TECHNICAL_PROBE.json',P/'SOURCES_AND_SCOPE.md',P/'SOURCE_FREEZE.json',P/'review/v6-source-board.jpg',P/'review/FINISHING_RUNTIME.json',P/'review/PREFLIGHT_GATES.json',P/'FINISHING_COVERAGE.json',P/'MOTION_REVIEW_TARGETS.json'])
print(json.dumps(receipt),flush=True)
