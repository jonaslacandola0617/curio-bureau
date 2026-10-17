from pathlib import Path
import subprocess,json,hashlib,os
from concurrent.futures import ThreadPoolExecutor
r=Path(__file__).resolve().parent;d=json.loads((r/'RECOVERY.json').read_text());pos=0
for c in sorted(d['chunks'],key=lambda x:x['start_frame']):
 assert c['start_frame']==pos and c['storage_status']=='DURABLE',c
 assert hashlib.sha256((r/c['file']).read_bytes()).hexdigest()==c['sha256'];pos+=c['frame_count']
assert pos==417
playlist=r/'chunks'/'native.ffconcat';playlist.write_text('ffconcat version 1.0\n'+''.join("file '"+str((r/c['file']).resolve())+"'\n"for c in sorted(d['chunks'],key=lambda x:x['start_frame'])))
common=['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-threads','2','-i',str(playlist),'-i',str(r/'audio/mix.wav'),'-map','0:v:0','-map','1:a:0','-r','30','-t','13.9','-vf','scale=in_range=full:out_range=tv:out_color_matrix=bt709','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','iec61966-2-1','-colorspace','bt709']
profiles=[('Cold_Metal_R2_4K.mp4',['-c:v','libx264','-preset','medium','-crf','15','-threads','3','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart']),('Cold_Metal_R2_4K.webm',['-c:v','libvpx-vp9','-crf','22','-b:v','0','-deadline','good','-cpu-used','4','-row-mt','1','-threads','3','-c:a','libopus','-b:a','256k','-ar','48000'])]
def encode(profile):
 name,args=profile
 out=r/name;temp=out.with_name(out.stem+'.partial'+out.suffix);subprocess.run(common+args+[str(temp)],check=True);os.replace(temp,out);print('ENCODED',name,out.stat().st_size,flush=True)
with ThreadPoolExecutor(max_workers=2)as pool:list(pool.map(encode,profiles))
# Posting copy is derived from the native lossless timeline, independently of either delivery codec.
name='Cold_Metal_R2_Posting.mp4';out=r/name;temp=out.with_name(out.stem+'.partial.mp4')
subprocess.run(common+['-c:v','libx264','-preset','fast','-crf','20','-threads','3','-c:a','aac','-b:a','256k','-movflags','+faststart',str(temp)],check=True);os.replace(temp,out);print('ENCODED',name,out.stat().st_size,flush=True)
