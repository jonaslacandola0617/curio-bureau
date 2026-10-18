from pathlib import Path
import subprocess,json,hashlib,re
import numpy as np
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;tl=json.loads((r/'timeline.json').read_text());p=r/'00-Phantom-Vibration-1080p-Review-v1.mp4';out=r/'encoded-review';out.mkdir(exist_ok=True)
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));(r/'FFPROBE.json').write_text(json.dumps(probe,indent=2)+'\n')
v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']))==(1080,1920,'30/1',tl['frames'])
assert v['codec_name']=='h264' and a['codec_name']=='aac' and a['channels']==2 and a['sample_rate']=='48000'
dec=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],capture_output=True,text=True);assert dec.returncode==0 and not dec.stderr.strip(),dec.stderr
met=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-vn','-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True).stderr
m=json.loads(met[met.rfind('{'):met.rfind('}')+1]);(r/'ENCODED_AUDIO_LOUDNESS.json').write_text(json.dumps(m,indent=2)+'\n');assert -15.5<float(m['input_i'])<-11 and float(m['input_tp'])<=-1
def pcm(path):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(path),'-ar','48000','-ac','2','-f','f32le','-']),dtype=np.float32).reshape(-1,2)
reference=pcm(r/'Phantom-Mix-v1.flac');actual=pcm(p);end=min(len(reference),len(actual),round(tl['voice_edited_duration']*48000));start=round((tl['voice_edited_duration']-8)*48000);corr=float(np.corrcoef(reference[start:end,0],actual[start:end,0])[0,1]);assert corr>.99
times=[.15,.6,1.8,1.9,3.8,5.9,9.6,12,13.1,16.7,18.4,20.3,22.4,24.2,27,31.2,33.6,35.8,40.2,43.9,45.6]
sheet=Image.new('RGB',(1080,7*662),'#e9e4da');draw=ImageDraw.Draw(sheet)
for i,t in enumerate(times):
 f=out/f'frame-{t}.png';subprocess.run(['ffmpeg','-y','-v','error','-ss',str(t),'-i',str(p),'-frames:v','1',str(f)],check=True)
 im=Image.open(f);assert im.size==(1080,1920);im=im.resize((350,622));x=(i%3)*360+5;y=(i//3)*662+30;sheet.paste(im,(x,y));draw.text((x,y-20),f'{t:.2f}s',fill='#0d1c2b')
sheet.save(out/'ENCODED_CONTACT_SHEET.jpg',quality=94)
qa={'status':'TECHNICAL_CHECKS_PASS; OWNER_FULL_REVIEW_PENDING','native':[1080,1920],'fps':30,'decoded_frames':int(v['nb_read_frames']),'duration':float(v['duration']),'complete_decode_errors':[],'audio':m,'last8sec_mix_correlation':corr,'voice_end':tl['voice_edited_duration'],'endcard_start':tl['ending_start'],'protected_tail':tl['protected_tail'],'checkpoint_frames':times,'text_shadow_backdrop':'absent by source construction and pre-capture runtime inspection','caption_timing':'actual-audio local ASR; independent listening approval pending','owner_motion':'PENDING','owner_whole_film':'PENDING','subjective_listening':'PENDING owner full-video audition','sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(r/'OUTPUT_QA.json').write_text(json.dumps(qa,indent=2)+'\n');print(json.dumps({k:qa[k] for k in ['status','decoded_frames','duration','last8sec_mix_correlation','protected_tail']}))
