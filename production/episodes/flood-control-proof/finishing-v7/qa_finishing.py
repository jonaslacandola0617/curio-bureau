"""Inspect the actual finishing-only MP4; source/word timing remains locked."""
from pathlib import Path
import json,hashlib,subprocess
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;D=P/'review/encoded-v7';D.mkdir(exist_ok=True)
movie=P/'Curio-Flood-Proof-Finishing-v7.mp4'
def run(cmd):subprocess.run(list(map(str,cmd)),check=True)
def out(cmd):return subprocess.check_output(list(map(str,cmd))).decode()
probe=json.loads(out(['ffprobe','-v','error','-show_streams','-show_format','-of','json',movie]))
v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1080,1920,'30/1',1822)
assert a['sample_rate']=='48000'and a['channels']==2
original=json.loads((P/'V6_TECHNICAL_PROBE.json').read_text());oa=next(s for s in original['streams']if s['codec_type']=='audio')
audio_keys=['codec_name','sample_rate','channels','channel_layout','time_base','start_pts','duration_ts']
for key in audio_keys:assert a.get(key)==oa.get(key),(key,a.get(key),oa.get(key))
run(['ffmpeg','-v','error','-xerror','-i',movie,'-f','null','-'])
receipt=json.loads((P/'DELIVERY_V7.json').read_text());digest=hashlib.sha256(movie.read_bytes()).hexdigest();assert digest==receipt['sha256']
audio=out(['ffmpeg','-v','error','-i',movie,'-map','0:a:0','-c','copy','-f','hash','-hash','sha256','-']).strip();assert audio==receipt['audio_packet_payload_hash']
times=[4.4,7.04,16.5,24.2,29.6,40.52,45.06,50.6,53.4,57.5,59.8,60.7]
board=Image.new('RGB',(1440,1992),(13,28,43))
for i,t in enumerate(times):
 dest=D/f'{t:.2f}.png';run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',movie,'-frames:v','1',dest])
 im=Image.open(dest);board.paste(im.resize((360,640)),((i%4)*360,(i//4)*664));ImageDraw.Draw(board).text(((i%4)*360+10,(i//4)*664+643),f'{t:.2f}s',fill='white')
board.save(D/'finishing-whole-film-review.jpg',quality=96)
encoded=np.asarray(Image.open(D/'60.70.png').convert('RGB'),dtype=float);expected=np.asarray(Image.open(P/'ending/032.png').convert('RGB'),dtype=float)
ending={'native_ending_source':'Original V6 lossless ending frame','encoded_mean_absolute_rgb_error':float(np.mean(abs(encoded-expected))),'encoded_rmse':float(np.sqrt(np.mean((encoded-expected)**2))),'note':'Lossy H264 difference; original33 native ending frames preserved by hash on runner'}
with(D/'loudness.log').open('w')as log:
 subprocess.run(['ffmpeg','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json','-f','null','-'],stdout=subprocess.DEVNULL,stderr=log,check=True)
log=(D/'loudness.log').read_text();loud=json.loads(log[log.rfind('{'):])
report={'schema':1,'movie':movie.name,'sha256':digest,'bytes':movie.stat().st_size,'duration_seconds':float(probe['format']['duration']),'frames':int(v['nb_frames']),'native_size':[1080,1920],'delivery_fps':30,'authored_fps':12,'strict_full_decode':'PASS','public_download_hash':'MATCH','artwork_owner_approved':True,'artwork_lock':'Same art code except one overlay hook;19 no-paper/no-grain states pixel-equal on runner; all source/timeline/optics inputs unchanged','audio_packet_hash':audio,'audio_packet_payload_identical_to_v6':True,'audio_timing_and_format_unchanged':{key:a.get(key)for key in audio_keys},'audio_loudness':{'integrated_lufs':loud['input_i'],'true_peak_dbtp':loud['input_tp'],'lra_lu':loud['input_lra']},'ending_comparison':ending,'encoded_checkpoints':times,'new_finishing_owner_approval':'PENDING','independent_listening':'Unchanged pending status; no new audition claimed','exact_caption_boundaries':'Unchanged V6 actual-audio ASR/script reconciliation; independent check pending','publication':'NOT AUTHORIZED / NOT PERFORMED'}
(D/'FINISHING_ENCODED_QA.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
