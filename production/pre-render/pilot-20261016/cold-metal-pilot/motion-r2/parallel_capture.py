"""Capture at most two native lossless chunks concurrently with isolated frame workers.
Preserves the frozen picture fingerprint used by native_capture.cjs. No picture code is changed.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,os
r=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
recovery=json.loads((r/'RECOVERY.json').read_text());total=recovery['total_frames']
assert sum(x['storage_status']!='DURABLE' for x in recovery['chunks'])==0,'Save pending chunks before more capture'
sources=['render.cjs','scene-core.cjs','editorial-finish.cjs','native_capture.cjs','native_worker.cjs','timeline.json','audio/mix.wav']
# Match the frozen JS identity byte-for-byte, including compact JSON serialization.
fingerprint=hashlib.sha256(json.dumps([[p,h(r/p)]for p in sources],separators=(',',':')).encode()).hexdigest()
assert fingerprint==recovery['source_fingerprint'],'Picture/capture input drift'
proof=json.loads((r/'NATIVE_PROOF.json').read_text())
for p,digest in proof['source_fingerprints'].items():assert h(r/p)==digest,p
subprocess.run(['python3',str(r/'preflight.py')],check=True)
existing={x['start_frame']:x for x in recovery['chunks']}
jobs=[(start,min(30,total-start))for start in range(0,total,30)if start not in existing][:2]
assert jobs,'All native frames already captured'
def capture(job):
 start,count=job;name=f'chunk_{start:04d}_{count}.mkv';dest=r/'chunks'/name;temp=dest.with_suffix('.partial.mkv')
 ff=subprocess.Popen(['ffmpeg','-nostdin','-y','-v','error','-f','rawvideo','-pixel_format','rgba','-video_size','2160x3840','-framerate','30','-i','pipe:0','-an','-c:v','ffv1','-level','3','-coder','1','-context','1','-g','1','-threads','2','-pix_fmt','gbrp',str(temp)],stdin=subprocess.PIPE)
 try:
  for frame in range(start,start+count,3):
   n=min(3,start+count-frame)
   subprocess.run([os.environ['CODEX_PRIMARY_RUNTIME_NODE'],'--expose-gc',str(r/'native_worker.cjs'),str(frame),str(n)],stdout=ff.stdin,check=True)
   print('FRAME',frame+n,'/',total,flush=True)
  ff.stdin.close();assert ff.wait()==0,'FFV1 failed'
 except:
  ff.kill();raise
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,nb_read_frames','-of','json',str(temp)]))['streams'][0]
 assert(probe['width'],probe['height'],int(probe['nb_read_frames']))==(2160,3840,count)
 os.replace(temp,dest)
 return dict(file='chunks/'+name,start_frame=start,frame_count=count,sha256=h(dest),bytes=dest.stat().st_size,decode='PASS',storage_status='LOCAL_VERIFIED',source_fingerprint=fingerprint,runner_sha256=h(Path(__file__)))
with ThreadPoolExecutor(max_workers=2)as pool:
 for record in pool.map(capture,jobs):
  recovery['chunks'].append(record);(r/'RECOVERY.json').write_text(json.dumps(recovery,indent=2)+'\n');print('CHUNK_VERIFIED',record['file'],record['bytes'],flush=True)
