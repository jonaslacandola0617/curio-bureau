from pathlib import Path
import subprocess,json,hashlib,numpy as np,re
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;p=r/'00-Sun-Last-Light-Motion-Preflight-v1.mp4';q=r/'qa'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));(q/'FFPROBE.json').write_text(json.dumps(probe,indent=2)+'\n')
subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json','-vn','-f','null','-'],stderr=subprocess.PIPE,text=True).stderr
m=json.loads(loud[loud.rfind('{'):loud.rfind('}')+1]);(q/'ENCODED_AUDIO_LOUDNESS.json').write_text(json.dumps(m,indent=2)+'\n')
md5=subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'Passage-lossless.mkv'),'-f','framemd5','-'],text=True);hashes=[line.split(',')[-1].strip()for line in md5.splitlines()if line and not line.startswith('#')]
violations=[i for i in range(1,len(hashes))if i*12//30==(i-1)*12//30 and hashes[i]!=hashes[i-1]]
runs=[];current=1
for a,b in zip(hashes,hashes[1:]):
 if a==b:current+=1
 else:runs.append(current);current=1
runs.append(current)
def audio(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','-']),np.float32).reshape(-1,2)
a=audio(p);b=audio(r/'Passage-Mix-v1.flac');n=min(len(a),len(b));tail_a=a[max(0,n-3*48000):n];tail_b=b[max(0,n-3*48000):n];corr=float(np.corrcoef(tail_a.flatten(),tail_b.flatten())[0,1])
times=[0,1.75,3.5,5.25,6.9,8.6,9.85,11.3];sheet=Image.new('RGB',(1200,1110),'#eee9df');d=ImageDraw.Draw(sheet)
for i,t in enumerate(times):
 f=q/f'encoded-{t}.jpg';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(p),'-frames:v','1','-q:v','2',str(f)],check=True);im=Image.open(f);im.thumbnail((285,507));x=10+(i%4)*300;y=30+(i//4)*550;sheet.paste(im,(x,y));d.text((x,y-20),f'{t}s',fill='#0d1c2b')
sheet.save(q/'ENCODED_CONTACT_SHEET.jpg',quality=94)
record={'role':'Representative passage only; owner moving review pending','duration':float(probe['format']['duration']),'width':probe['streams'][0]['width'],'height':probe['streams'][0]['height'],'frames':int(probe['streams'][0]['nb_read_frames']),'scene_fps':12,'full_decode':'PASS','within_12fps_state_changes':violations,'hold_run_lengths':sorted(set(runs)),'unique_source_states':len(set(hashes)),'source_lossless_frames':len(hashes),'encoded_audio_lufs':m['input_i'],'encoded_audio_dbtp':m['input_tp'],'encoded_tail_mix_correlation':corr,'selected_voice_closing_phrase':'Then, daylight ends.','source_voice_selection':[14.55,26.15],'last_selected_spoken_end':25.44-14.55,'protected_selected_tail':11.6-(25.44-14.55),'independent_listening':'Not claimed; owner review pending','mp4_sha256':hashlib.sha256(p.read_bytes()).hexdigest()};(q/'OUTPUT_QA.json').write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(record,indent=2));assert record['frames']==348 and not violations
