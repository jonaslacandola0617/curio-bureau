"""Reuse the exact approved audio and native ending; never regenerate either."""
from pathlib import Path
import json,hashlib,subprocess,urllib.request,shutil
P=Path(__file__).resolve().parent;D=P/'locked';D.mkdir(exist_ok=True);tag='flood-proof-real-records-v6-20261021'
base='https://github.com/jonaslacandola0617/curio-bureau/releases/download/'+tag+'/'
def get(name):
 p=D/name
 if not p.exists():
  with urllib.request.urlopen(base+name,timeout=60)as r,p.open('wb')as f:
   while b:=r.read(1048576):f.write(b)
 return p
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
movie=get('Curio-Flood-Proof-Real-Records-v6.mp4')
assert sha(movie)=='6e95da904de634bcd2dd30e7a91f40ecd9fa2042f525eb09180a8fd1cb516aab'
records=json.loads(get('RECOVERY.json').read_text());ending=P/'ending';ending.mkdir(exist_ok=True)
start=1789;last=1822;n=0;receipts=[]
for item in records['chunks']:
 a,b=item['start_frame'],item['end_frame_exclusive']
 if b<=start or a>=last:continue
 f=get(item['file']);assert sha(f)==item['sha256'];offset=max(start,a)-a;count=min(last,b)-max(start,a)
 subprocess.run(['ffmpeg','-v','error','-y','-i',str(f),'-vf',f'trim=start_frame={offset},setpts=PTS-STARTPTS','-vsync','0','-frames:v',str(count),'-start_number',str(n),str(ending/'%03d.png')],check=True)
 receipts.append({'chunk':f.name,'source_sha256':item['sha256'],'source_frame_offset':offset,'frames':count});n+=count
assert n==33
original=D/'ending';original.mkdir(exist_ok=True)
frames=[]
for f in sorted(ending.glob('*.png')):shutil.copy2(f,original/f.name);frames.append({'file':f.name,'sha256':sha(f)})
audio=subprocess.check_output(['ffmpeg','-v','error','-i',str(movie),'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).decode().strip()
(D/'LOCKED_MEDIA_RECEIPT.json').write_text(json.dumps({'approved_movie_sha256':sha(movie),'audio_packet_payload_hash':audio,'ending_chunks':receipts,'ending_native_frames':frames},indent=2)+'\n')
print('Recovered33 original native ending frames; V6 AAC will be stream-copied',flush=True)
