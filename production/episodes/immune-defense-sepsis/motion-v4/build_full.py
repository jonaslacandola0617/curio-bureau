from pathlib import Path
import subprocess,os,json,hashlib,urllib.request,zipfile
P=Path(__file__).resolve().parent;V3=P.parent/'motion-v3';repo=os.environ['GH_REPO'];target=os.environ['SOURCE_COMMIT'];tag='immune-defense-motion-v4-20261021'
def run(a):subprocess.run(list(map(str,a)),check=True)
def out(a):return subprocess.check_output(list(map(str,a))).decode()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def rec(f):return {'file':f.name,'bytes':f.stat().st_size,'sha256':sha(f)}
freeze=json.loads((P/'SOURCE_FREEZE.json').read_text())
for x in freeze['inputs']:assert sha(P/x['path'])==x['sha256'],x['path']
for f in ['render_art.py','render_movie.py','finish.py','episode.json','FINISHING_CONTRACT.json']:assert (P/f).read_bytes()==(V3/f).read_bytes(),f
run(['python',P/'download_assets.py']);run(['python',P/'prepare_timeline.py']);assert sha(P/'timeline.json')==next(x['sha256']for x in freeze['inputs']if x['path']=='timeline.json')
tl=json.loads((P/'timeline.json').read_text());original=json.loads((P/'V3_RECOVERY.json').read_text())['chunks'][-1];native=P/'original-ending-native.mkv';tmp=native.with_suffix('.part');h=hashlib.sha256();n=0
with urllib.request.urlopen(original['download_url'],timeout=120)as src,tmp.open('wb')as dst:
 while True:
  b=src.read(1024*1024)
  if not b:break
  dst.write(b);h.update(b);n+=len(b)
 dst.flush();os.fsync(dst.fileno())
assert n==original['bytes']and h.hexdigest()==original['sha256'];tmp.replace(native)
ending=P/'ending';ending.mkdir(exist_ok=True);run(['ffmpeg','-v','error','-y','-i',native,'-vf',r'select=gte(n\,138)','-vsync','0','-start_number','0',ending/'%03d.png']);assert len(list(ending.glob('*.png')))==33
run(['python',P/'prove_runtime.py']);run(['python',P/'qa_native_closing.py'])
voicecheck=subprocess.run(['ffmpeg','-hide_banner','-i',P/'audio/voice.wav','-af','silencedetect=noise=-37dB:d=0.85','-f','null','-'],capture_output=True,text=True);(P/'review/VOICE_GAP_LOG.txt').write_text(voicecheck.stderr)
if subprocess.run(['gh','release','view',tag,'--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:
 run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Curio Bureau — Immune defense restored speech V4','--notes','V1–V3 audio was defective: estimated ASR quiet cuts entered speech. V4 restores original Bernard samples and trims only measured near-silence; captions/scenes/cues retimed. Approved art/finishing and exact33 ending frames preserved. Review export, no social publication. Frozen source: '+target])
def upload(fs):run(['gh','release','upload',tag,'--repo',repo,*fs])
proofzip=P/'NATIVE_EXECUTION_EVIDENCE.zip'
with zipfile.ZipFile(proofzip,'w',zipfile.ZIP_DEFLATED)as z:
 for f in (P/'review').glob('*'):
  if f.is_file():z.write(f,str(f.relative_to(P)))
upload([P/'audio/bernard-restored-float.wav',P/'audio/soundtrack.flac',P/'audio/VOICE_EDITS.json',proofzip])
chunks=P/'chunks';chunks.mkdir(exist_ok=True);records=[];pending=[]
for start in range(0,tl['frames'],300):
 end=min(tl['frames'],start+300);f=chunks/f'frames-{start:05}-{end:05}.mkv';run(['python',P/'render_movie.py','--chunk',start,end,f]);count=int(out(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=nb_read_frames','-of','csv=p=0',f]).strip());assert count==end-start;pending.append(f)
 if len(pending)==2 or end==tl['frames']:
  upload(pending)
  for q in pending:
   r=rec(q);parts=q.stem.split('-');r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{q.name}','start_frame':int(parts[1]),'end_frame_exclusive':int(parts[2]),'role':'lossless native RGB recovery'});records.append(r)
  progress=P/f'RECOVERY-through-{end:05}.json';progress.write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':records},indent=2)+'\n');upload([progress]);pending=[]
(P/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':records},indent=2)+'\n')
def hashes(f,select):
 s=out(['ffmpeg','-v','error','-i',f,'-vf',select,'-an','-pix_fmt','rgb24','-f','framemd5','-']);return [x.rsplit(',',1)[1].strip()for x in s.splitlines()if x and not x.startswith('#')]
lastchunk=chunks/records[-1]['file'];offset=round(tl['ending_start']*30)-records[-1]['start_frame'];assert hashes(native,r'select=gte(n\,138)')==hashes(lastchunk,f'select=gte(n\\,{offset})')
audio=json.loads((P/'audio/VOICE_EDITS.json').read_text());proof={'audio_restoration':audio,'artwork_renderer':'BYTE_IDENTICAL toV3','render_movie_continuity_clock':'BYTE_IDENTICAL toV3; no repeated closing entrance','finishing':'BYTE_IDENTICAL toV3; separate paper and foreground grain','old_AAC':'NOT REUSED; defective prior cut mix retained historically','original33_native_ending_frames':'DECODED_RGB_IDENTICAL, relocated after complete restored narration','scene_and_caption_timing':'Rebuilt from complete acoustic utterance spans plus qualified ASR word estimates','independent_listening':'NOT PERFORMED; automated source/mix/encoded speech checks recorded separately'};(P/'REPAIR_PROOF.json').write_text(json.dumps(proof,indent=2)+'\n')
manifest=chunks/'concat.txt';manifest.write_text(''.join("file '"+str((chunks/r['file']).resolve())+"'\n"for r in records));movie=P/'Curio-Immune-Defense-Full-Review-v4.mp4'
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-i',P/'audio/soundtrack.flac','-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart',movie]);upload([movie])
r=rec(movie);r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{movie.name}','source_commit':target,'status':'ARCHIVED_RESTORED_SPEECH_FULL_REVIEW','duration_seconds':tl['duration'],'native':[1080,1920],'delivery_fps':30,'scene_fps':12,'owner_art_approval':'APPROVED; unchanged source art with vivid accents','owner_motion_full_film_approval':'PENDING','independent_listening':'PENDING; no audition claim','exact_caption_boundaries':'Measured acoustic phrase anchors plus internal ASR estimates; independent verification pending','clinical_wording_human_review':'PENDING','publication':'NOT AUTHORIZED / NOT PERFORMED','repair':'Restored all original Bernard speech samples; only sample-verified near-silence trimmed; all scene/caption/SFX timings rebuilt; exact33 native ending frames preserved'})
(P/'DELIVERY.json').write_text(json.dumps(r,indent=2)+'\n');run(['ffmpeg','-v','error','-xerror','-i',movie,'-f','null','-']);(P/'TECHNICAL_PROBE.json').write_text(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
upload([P/f for f in ['DELIVERY.json','RECOVERY.json','REPAIR_PROOF.json','TECHNICAL_PROBE.json','SOURCE_FREEZE.json','OWNER_APPROVAL.md','review/FINISHING_RUNTIME.json','review/PREFLIGHT_GATES.json','review/NATIVE_CLOSING_CONTINUITY.json','FINISHING_COVERAGE.json','audio/ASR_WORDS.json','timeline.json','README.md']]);print('DELIVERY_ARCHIVED',json.dumps(r),flush=True)
