"""Independent native encodes, with picture/audio/profile-bound reuse."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,hashlib,os,threading
r=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
d=json.loads((r/'RECOVERY.json').read_text());chunks=sorted(d['chunks'],key=lambda x:x['start_frame']);pos=0
for c in chunks:
 assert c['start_frame']==pos and c['storage_status']=='DURABLE',c
 assert h(r/c['file'])==c['sha256'];pos+=c['frame_count']
assert pos==417
playlist=r/'chunks/native.ffconcat';playlist.write_text('ffconcat version 1.0\n'+''.join("file '"+str((r/c['file']).resolve())+"'\n"for c in chunks))
common=['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-threads','2','-i',str(playlist),'-i',str(r/'audio/mix.wav'),'-map','0:v:0','-map','1:a:0','-r','30','-t','13.9','-vf','scale=in_range=full:out_range=tv:out_color_matrix=bt709','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','iec61966-2-1','-colorspace','bt709']
profiles=[('Cold_Metal_R2_4K.mp4',['-c:v','libx264','-preset','veryfast','-crf','15','-threads','6','-c:a','aac','-b:a','320k','-ar','48000','-movflags','+faststart']),('Cold_Metal_R2_4K.webm',['-c:v','libvpx-vp9','-crf','22','-b:v','0','-deadline','realtime','-cpu-used','8','-row-mt','1','-tile-columns','2','-lag-in-frames','0','-threads','6','-c:a','libopus','-b:a','256k','-ar','48000']),('Cold_Metal_R2_Posting.mp4',['-c:v','libx264','-preset','veryfast','-crf','20','-threads','6','-c:a','aac','-b:a','256k','-movflags','+faststart'])]
cache_path=r/'ENCODE_CACHE.json';cache=json.loads(cache_path.read_text())if cache_path.exists()else{};lock=threading.Lock()
def fingerprint(args):
 material={'native_chunk_hashes':[x['sha256']for x in chunks],'mix_sha256':h(r/'audio/mix.wav'),'frames':417,'native':[2160,3840],'fps':30,'duration':13.9,'colors':'BT709 matrix/primaries, sRGB transfer, full RGB to limited YUV420','profile':args}
 if args==profiles[2][1]:material['posting_picture_input_master_sha256']=h(r/'Cold_Metal_R2_4K.mp4')
 return hashlib.sha256(json.dumps(material,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def record_complete(profile,basis='completed by this encoder'):
 name,args=profile;out=r/name;q=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,nb_read_frames','-of','json',str(out)]))['streams'][0]
 assert(q['width'],q['height'],int(q['nb_read_frames']))==(2160,3840,417)
 with lock:
  cache[name]={'input_fingerprint':fingerprint(args),'file_sha256':h(out),'bytes':out.stat().st_size,'profile':args,'basis':basis}
  tmp=cache_path.with_suffix('.partial.json');tmp.write_text(json.dumps(cache,indent=2)+'\n');os.replace(tmp,cache_path)
def encode(profile):
 name,args=profile;out=r/name;expected=fingerprint(args)
 if out.exists():
  old=cache.get(name,{})
  assert old.get('input_fingerprint')==expected and old.get('file_sha256')==h(out),'Existing movie has missing/stale source/profile binding: '+name
  print('REUSE verified native encode',name,flush=True);return
 temp=out.with_name(out.stem+'.partial'+out.suffix)
 command=common
 if args==profiles[2][1]:
  command=['ffmpeg','-nostdin','-y','-v','error','-i',str(r/'Cold_Metal_R2_4K.mp4'),'-i',str(r/'audio/mix.wav'),'-map','0:v:0','-map','1:a:0','-r','30','-t','13.9','-pix_fmt','yuv420p','-color_primaries','bt709','-color_trc','iec61966-2-1','-colorspace','bt709']
 subprocess.run(command+args+[str(temp)],check=True);os.replace(temp,out);record_complete(profile);print('ENCODED',name,out.stat().st_size,flush=True)
if __name__=='__main__':
 with ThreadPoolExecutor(max_workers=2)as pool:list(pool.map(encode,profiles[:2]))
 encode(profiles[2])
