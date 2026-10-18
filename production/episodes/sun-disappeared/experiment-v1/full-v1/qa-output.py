from pathlib import Path
import subprocess,json,hashlib,numpy as np
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;q=r/'qa';p=r/'00-Sun-Disappeared-1080p-Full-Review-v1.mp4';tl=json.loads((r/'timeline.json').read_text())
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));(q/'FFPROBE.json').write_text(json.dumps(probe,indent=2)+'\n')
subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-vn','-f','null','-'],stderr=subprocess.PIPE,text=True).stderr;m=json.loads(loud[loud.rfind('{'):loud.rfind('}')+1]);(q/'ENCODED_AUDIO_LOUDNESS.json').write_text(json.dumps(m,indent=2)+'\n')
hashes=[]
for c in sorted((r/'chunks').glob('*.mkv')):
 md5=subprocess.check_output(['ffmpeg','-v','error','-i',str(c),'-f','framemd5','-'],text=True);hashes.extend(line.split(',')[-1].strip()for line in md5.splitlines()if line and not line.startswith('#'))
violations=[i for i in range(1,len(hashes))if i/30<tl['ending_start'] and i*12//30==(i-1)*12//30 and hashes[i]!=hashes[i-1]]
def audio(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','-']),np.float32).reshape(-1,2)
a=audio(p);b=audio(r/'Sun-Full-Mix-v1.flac');n=min(len(a),len(b));corr=float(np.corrcoef(a[40*48000:n].flatten(),b[40*48000:n].flatten())[0,1])
times=[0,1.7,3.4,6.4,9.6,12.3,14.7,18.1,21.4,24.9,27.8,30.7,33.8,36.5,38.6,40.9,43.1,46.4,48.0,49.3];sheet=Image.new('RGB',(1200,2770),'#eee9df');d=ImageDraw.Draw(sheet)
for i,t in enumerate(times):
 f=q/f'encoded-{t}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(p),'-frames:v','1','-q:v','2',str(f)],check=True);im=Image.open(f);im.thumbnail((285,507));x=10+i%4*300;y=30+i//4*550;sheet.paste(im,(x,y));d.text((x,y-20),f'{t}s',fill='#0d1c2b')
sheet.save(q/'ENCODED_FULL_CONTACT_SHEET.jpg',quality=94)
# Sample actual joins at first/intermediate/resolved states, including source removal and brand handoff.
joins=[6.1,10.45,14.55,26.15,32.3,36.1,40.45,48.4];joinSheet=Image.new('RGB',(960,8*610),'#eee9df');jd=ImageDraw.Draw(joinSheet)
for row,t in enumerate(joins):
 for col,off in enumerate([-.10,.04,.24]):
  f=q/f'join-{t}-{col}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t+off),'-i',str(p),'-frames:v','1','-q:v','2',str(f)],check=True);im=Image.open(f);im.thumbnail((300,534));x=10+col*320;y=30+row*610;joinSheet.paste(im,(x,y));jd.text((x,y-20),f'{t+off:.2f}s',fill='#0d1c2b')
joinSheet.save(q/'ENCODED_JOINS.jpg',quality=92)
record={'role':'COMPLETE FULL-FILM REVIEW; owner approval pending','duration':float(probe['format']['duration']),'frames':int(probe['streams'][0]['nb_read_frames']),'native':[probe['streams'][0]['width'],probe['streams'][0]['height']],'source_lossless_frames':len(hashes),'full_decode':'PASS','scene_fps':12,'within12fps_state_changes':violations,'ending30fps_exception':[48.4,49.5],'audio_lufs':m['input_i'],'audio_dbtp':m['input_tp'],'closing_audio_mix_correlation':corr,'whole_closing_clause':"We'd spend those final minutes living in the sun's past.",'decoded_voice_end':47.59,'endcard_start':48.4,'protected_voice_tail':.81,'independent_listening':'Owner full playback pending; ASR/correlation are not independent listening','sha256':hashlib.sha256(p.read_bytes()).hexdigest()};(q/'OUTPUT_QA.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2));assert record['frames']==1485 and not violations
