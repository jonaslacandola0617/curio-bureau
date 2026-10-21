from pathlib import Path
import subprocess,os,json,hashlib,urllib.request,concurrent.futures
P=Path(__file__).resolve().parent;V1=P.parent/'motion-v1';repo=os.environ['GH_REPO'];target=os.environ['SOURCE_COMMIT'];tag='immune-defense-motion-v2-20261021'
def run(a):subprocess.run(list(map(str,a)),check=True)
def out(a):return subprocess.check_output(list(map(str,a))).decode()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def rec(f):return {'file':f.name,'bytes':f.stat().st_size,'sha256':sha(f)}
freeze=json.loads((P/'SOURCE_FREEZE.json').read_text())
for x in freeze['inputs']:assert sha(P/x['path'])==x['sha256'],x['path']
scope=json.loads((P/'REPAIR_SCOPE.json').read_text());assert (P/'render_art.py').read_text().replace(scope['new_line'],scope['old_line'])==(V1/'render_art.py').read_text()
for f in ['render_movie.py','finish.py','episode.json','timeline.json','FINISHING_CONTRACT.json','prepare_timeline.py']:
 assert (P/f).read_bytes()==(V1/f).read_bytes(),f
chunks=P/'chunks';chunks.mkdir(exist_ok=True);old=json.loads((P/'V1_RECOVERY.json').read_text());delivery=json.loads((P/'V1_DELIVERY.json').read_text())
def download(r):
 f=chunks/r['file'];tmp=f.with_suffix('.part');h=hashlib.sha256();n=0
 with urllib.request.urlopen(r['download_url'],timeout=120)as src,tmp.open('wb')as dst:
  while True:
   b=src.read(1024*1024)
   if not b:break
   dst.write(b);h.update(b);n+=len(b)
  dst.flush();os.fsync(dst.fileno())
 assert n==r['bytes']and h.hexdigest()==r['sha256'],r['file'];tmp.replace(f);print('VERIFIED_RECOVERY',f.name,flush=True);return f
with concurrent.futures.ThreadPoolExecutor(max_workers=4)as ex:list(ex.map(download,old['chunks']+[delivery]))
run(['python',P/'download_assets.py']);run(['python',P/'prepare_timeline.py'])
assert (P/'timeline.json').read_bytes()==(V1/'timeline.json').read_bytes()
ending=P/'ending';ending.mkdir(exist_ok=True)
run(['ffmpeg','-v','error','-y','-i',chunks/old['chunks'][-1]['file'],'-vf','select=gte(n\,138)','-vsync','0','-start_number','0',ending/'%03d.png'])
assert len(list(ending.glob('*.png')))==33
run(['python',P/'prove_runtime.py'])
start=chunks/'repair-00000-00040.mkv';run(['python',P/'render_movie.py','--chunk',0,40,start])
orig=chunks/old['chunks'][0]['file'];tail=chunks/'tail-00040-00300.mkv'
run(['ffmpeg','-v','error','-y','-i',orig,'-vf','select=gte(n\,40),setpts=N/(30*TB)','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',tail])
manifest=chunks/'repair.txt';manifest.write_text(''.join("file '"+str(f.resolve())+"'\n"for f in [start,tail]))
patched=chunks/'frames-00000-00300-v2.mkv';run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',patched])
def hashes(f):
 s=out(['ffmpeg','-v','error','-i',f,'-an','-pix_fmt','rgb24','-f','framemd5','-']);return [x.rsplit(',',1)[1].strip()for x in s.splitlines()if x and not x.startswith('#')]
a=hashes(orig);b=hashes(patched);assert len(a)==len(b)==300 and a[40:]==b[40:];assert a[:40]!=b[:40]
proof={'only_changed_native_frames':[i for i in range(300)if a[i]!=b[i]],'frames_40_through_299':'DECODED_RGB_IDENTICAL','frames_300_through_1370':'ORIGINAL_LOSSLESS_FILES_REUSED_WITH_VERIFIED_SHA256','ending':'ORIGINAL_33_NATIVE_FRAMES_REUSED','audio':'Original V1 AAC payload, no regeneration'}
if subprocess.run(['gh','release','view',tag,'--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:
 run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Curio Bureau — Immune defense full review v2','--notes','Owner-approved artwork and vibrant colors. Opening connector tracking repaired; all subsequent native frames and original audio preserved. Full review export; independent listening/caption and owner full-film review remain pending. Source: '+target])
def upload(fs):run(['gh','release','upload',tag,'--repo',repo,*fs])
upload([patched]);r=rec(patched);r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{patched.name}','start_frame':0,'end_frame_exclusive':300,'role':'lossless native RGB recovery'})
recovery={'source_commit':target,'frames':1371,'chunks':[r]+old['chunks'][1:]};(P/'RECOVERY.json').write_text(json.dumps(recovery,indent=2)+'\n')
manifest=chunks/'concat.txt';files=[patched]+[chunks/r['file']for r in old['chunks'][1:]];manifest.write_text(''.join("file '"+str(f.resolve())+"'\n"for f in files))
movie=P/'Curio-Immune-Defense-Full-Review-v2.mp4';v1movie=chunks/delivery['file']
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-i',v1movie,'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',movie])
upload([movie])
def audiohash(f):return out(['ffmpeg','-v','error','-i',f,'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).strip()
assert audiohash(v1movie)==audiohash(movie);proof['aac_packet_payload_hash']=audiohash(movie);(P/'REPAIR_PROOF.json').write_text(json.dumps(proof,indent=2)+'\n')
r=rec(movie);r.update({k:v for k,v in delivery.items()if k not in ['file','bytes','sha256','download_url','source_commit']});r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{movie.name}','source_commit':target,'repair':'Opening connector follows existing moving source planes; native frames40 onward unchanged; AAC identical'})
(P/'DELIVERY.json').write_text(json.dumps(r,indent=2)+'\n')
run(['ffmpeg','-v','error','-xerror','-i',movie,'-f','null','-']);(P/'TECHNICAL_PROBE.json').write_text(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
upload([P/f for f in ['DELIVERY.json','RECOVERY.json','REPAIR_PROOF.json','REPAIR_SCOPE.json','TECHNICAL_PROBE.json','SOURCE_FREEZE.json','OWNER_APPROVAL.md','review/FINISHING_RUNTIME.json','review/PREFLIGHT_GATES.json','FINISHING_COVERAGE.json','audio/VOICE_EDITS.json','timeline.json']]);print('DELIVERY_ARCHIVED',json.dumps(r),flush=True)
