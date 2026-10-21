from pathlib import Path
import subprocess,os,json,hashlib,urllib.request,concurrent.futures,zipfile
P=Path(__file__).resolve().parent;V2=P.parent/'motion-v2';repo=os.environ['GH_REPO'];target=os.environ['SOURCE_COMMIT'];tag='immune-defense-motion-v3-20261021'
def run(a):subprocess.run(list(map(str,a)),check=True)
def out(a):return subprocess.check_output(list(map(str,a))).decode()
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def rec(f):return {'file':f.name,'bytes':f.stat().st_size,'sha256':sha(f)}
freeze=json.loads((P/'SOURCE_FREEZE.json').read_text())
for x in freeze['inputs']:assert sha(P/x['path'])==x['sha256'],x['path']
scope=json.loads((P/'REPAIR_SCOPE.json').read_text());assert (P/'render_movie.py').read_text().replace(scope['new_expression'],scope['old_expression'])==(V2/'render_movie.py').read_text()
for f in ['render_art.py','finish.py','episode.json','timeline.json','FINISHING_CONTRACT.json','prepare_timeline.py']:
 assert (P/f).read_bytes()==(V2/f).read_bytes(),f
chunks=P/'chunks';chunks.mkdir(exist_ok=True);old=json.loads((P/'V2_RECOVERY.json').read_text());delivery=json.loads((P/'V2_DELIVERY.json').read_text())
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
run(['python',P/'download_assets.py']);run(['python',P/'prepare_timeline.py']);assert (P/'timeline.json').read_bytes()==(V2/'timeline.json').read_bytes()
ending=P/'ending';ending.mkdir(exist_ok=True)
run(['ffmpeg','-v','error','-y','-i',chunks/old['chunks'][-1]['file'],'-vf',r'select=gte(n\,138)','-vsync','0','-start_number','0',ending/'%03d.png']);assert len(list(ending.glob('*.png')))==33
run(['python',P/'prove_runtime.py']);run(['python',P/'qa_native_closing.py'])
window=chunks/'repair-01150-01260.mkv';run(['python',P/'render_movie.py','--chunk',1150,1260,window])
def segment(src,start,end,name):
 f=chunks/name;run(['ffmpeg','-v','error','-y','-i',src,'-vf',f'select=gte(n\\,{start})*lt(n\\,{end}),setpts=N/(30*TB)','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',f]);return f
def join(parts,name):
 m=chunks/(name+'.txt');m.write_text(''.join("file '"+str(f.resolve())+"'\n"for f in parts));f=chunks/name;run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',m,'-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',f]);return f
orig3=chunks/old['chunks'][3]['file'];orig4=chunks/old['chunks'][4]['file']
f3=join([segment(orig3,0,250,'prefix-00900-01150.mkv'),segment(window,0,50,'patch-01150-01200.mkv')],'frames-00900-01200-v3.mkv')
f4=join([segment(window,50,110,'patch-01200-01260.mkv'),segment(orig4,60,171,'tail-01260-01371.mkv')],'frames-01200-01371-v3.mkv')
def hashes(f):
 s=out(['ffmpeg','-v','error','-i',f,'-an','-pix_fmt','rgb24','-f','framemd5','-']);return [x.rsplit(',',1)[1].strip()for x in s.splitlines()if x and not x.startswith('#')]
a=hashes(orig3)+hashes(orig4);b=hashes(f3)+hashes(f4);assert len(a)==len(b)==471;changed=[900+i for i in range(471)if a[i]!=b[i]]
assert changed and all(1150<=n<1260 for n in changed);assert any(n<1200 for n in changed)and any(n>=1238 for n in changed)
proof={'only_changed_native_frames':changed,'frames_0_through_899':'ORIGINAL_VERIFIED_LOSSLESS_FILES_REUSED','frames_900_through_1149':'DECODED_RGB_IDENTICAL','frames_1260_through_1370':'DECODED_RGB_IDENTICAL','original33_ending_frames':'DECODED_RGB_IDENTICAL','approved_artwork_renderer_sha256':sha(P/'render_art.py'),'timeline':'BYTE_IDENTICAL','finishing':'BYTE_IDENTICAL','captions':'BYTE_IDENTICAL; independent exact-boundary audition pending','scope':'One continuous closing animation clock across narration beats; no new geometry, assets or audio'}
if subprocess.run(['gh','release','view',tag,'--repo',repo],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL).returncode:
 run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Curio Bureau — Immune defense corrected closing V3','--notes','Repairs repeated closing hand entrances confirmed by owner. Approved art, original AAC and exact native ending preserved. Review export; no social publication. Frozen source: '+target])
def upload(fs):run(['gh','release','upload',tag,'--repo',repo,*fs])
upload([f3,f4]);records=[]
for f,start,end in [(f3,900,1200),(f4,1200,1371)]:
 r=rec(f);r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{f.name}','start_frame':start,'end_frame_exclusive':end,'role':'lossless native RGB recovery'});records.append(r)
recovery={'source_commit':target,'frames':1371,'chunks':old['chunks'][:3]+records};(P/'RECOVERY.json').write_text(json.dumps(recovery,indent=2)+'\n')
manifest=chunks/'concat.txt';files=[chunks/r['file']for r in old['chunks'][:3]]+[f3,f4];manifest.write_text(''.join("file '"+str(f.resolve())+"'\n"for f in files))
movie=P/'Curio-Immune-Defense-Full-Review-v3.mp4';v2movie=chunks/delivery['file']
run(['ffmpeg','-v','error','-y','-f','concat','-safe','0','-i',manifest,'-i',v2movie,'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','copy','-movflags','+faststart',movie]);upload([movie])
def audiohash(f):return out(['ffmpeg','-v','error','-i',f,'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).strip()
assert audiohash(v2movie)==audiohash(movie);proof['aac_packet_payload_hash']=audiohash(movie);(P/'REPAIR_PROOF.json').write_text(json.dumps(proof,indent=2)+'\n')
r=rec(movie);r.update({k:v for k,v in delivery.items()if k not in ['file','bytes','sha256','download_url','source_commit','repair']});r.update({'download_url':f'https://github.com/{repo}/releases/download/{tag}/{movie.name}','source_commit':target,'repair':'Closing animation clock continues across38.3s and41.2s narration beats; all native frames outside1150–1259 and original AAC preserved'})
(P/'DELIVERY.json').write_text(json.dumps(r,indent=2)+'\n');run(['ffmpeg','-v','error','-xerror','-i',movie,'-f','null','-']);(P/'TECHNICAL_PROBE.json').write_text(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
proofzip=P/'NATIVE_EXECUTION_EVIDENCE.zip'
with zipfile.ZipFile(proofzip,'w',zipfile.ZIP_DEFLATED)as z:
 for f in (P/'review').glob('*'):
  if f.is_file():z.write(f,str(f.relative_to(P)))
upload([P/f for f in ['DELIVERY.json','RECOVERY.json','REPAIR_PROOF.json','REPAIR_SCOPE.json','TECHNICAL_PROBE.json','SOURCE_FREEZE.json','OWNER_APPROVAL.md','review/FINISHING_RUNTIME.json','review/PREFLIGHT_GATES.json','review/NATIVE_CLOSING_CONTINUITY.json','FINISHING_COVERAGE.json','audio/VOICE_EDITS.json','timeline.json','NATIVE_EXECUTION_EVIDENCE.zip']]);print('DELIVERY_ARCHIVED',json.dumps(r),flush=True)
