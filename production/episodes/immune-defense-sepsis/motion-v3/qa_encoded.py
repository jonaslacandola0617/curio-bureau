from pathlib import Path
import subprocess,json,hashlib,re
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;R=P/'review/encoded';R.mkdir(parents=True,exist_ok=True);movie=P/'Curio-Immune-Defense-Full-Review-v3.mp4';tl=json.loads((P/'timeline.json').read_text());receipt=json.loads((P/'DELIVERY.json').read_text())
def out(a):return subprocess.check_output(list(map(str,a))).decode()
sha=hashlib.sha256(movie.read_bytes()).hexdigest();assert sha==receipt['sha256']and movie.stat().st_size==receipt['bytes']
subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(movie),'-f','null','-'],check=True)
probe=json.loads(out(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',movie]));v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio');assert(v['width'],v['height'])==(1080,1920)and int(v['nb_read_frames'])==tl['frames'];assert v['avg_frame_rate']=='30/1';assert a['sample_rate']=='48000'and a['channels']==2
b=tl['scene_boundaries'];times=[.3,1.7,b[1]+.15,b[1]+1,b[2]+.3,b[2]+2.5,b[3]+1.5,b[3]+2.8,b[4]+1,b[6]+1,tl['ending_start']+.4,tl['duration']-.05]
board=Image.new('RGB',(1440,1992),(13,28,43))
for k,t in enumerate(times):
 f=R/f'{k:02}-{t:.2f}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(f)],check=True);im=Image.open(f).convert('RGB').resize((360,640));x=k%4*360;y=k//4*664;board.paste(im,(x,y));ImageDraw.Draw(board).text((x+8,y+643),f'{t:.2f}s',fill=(245,240,231))
board.save(R/'whole-film-phone-review.jpg',quality=94,subsampling=0)
l=subprocess.run(['ffmpeg','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json','-f','null','-'],capture_output=True,text=True);(R/'loudness.log').write_text(l.stderr);m=re.search(r'\{\s*"input_i".*?\}',l.stderr,re.S);loud=json.loads(m.group())if m else None
report={'status':'ENCODED_REVIEW_TECHNICAL_PASS; picture inspection recorded separately','movie':movie.name,'bytes':movie.stat().st_size,'sha256':sha,'public_download_hash':'MATCH','duration':float(probe['format']['duration']),'native':[1080,1920],'delivery_fps':30,'authored_scene_fps':12,'frames':int(v['nb_read_frames']),'strict_complete_decode':'PASS','audio':{'sample_rate':48000,'channels':2,'loudness':loud},'checkpoints':times,'owner_art_approval':'APPROVED with vibrant yellow/red correction','owner_motion_full_film_approval':'PENDING','independent_listening':'PENDING; no audition claim','caption_boundaries':'Actual-audio ASR; script reconciled, independent check pending','clinical_wording_human_review':'PENDING','publication':'NOT AUTHORIZED / NOT PERFORMED'}
(R/'ENCODED_QA.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
