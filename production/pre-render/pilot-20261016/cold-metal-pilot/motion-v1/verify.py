from pathlib import Path
import subprocess,json,hashlib,io
from PIL import Image,ImageFilter,ImageChops
import numpy as np
r=Path(__file__).resolve().parent;report={'scope':'13.9s 1080p review passage; not a native 4K release','files':{},'subjective_listening':'OWNER REVIEW PENDING','owner_motion_review':'NOT REVIEWED'}
for name in ['Cold_Metal_Sequence.mp4','Cold_Metal_Sequence.webm']:
 p=r/name
 if not p.exists()or p.stat().st_size<1000:continue
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
 assert(v['width'],v['height'])==(1080,1920);assert v['avg_frame_rate']=='30/1';assert int(v['nb_read_frames'])==417;assert abs(float(probe['format']['duration'])-13.9)<.08
 subprocess.run(['ffmpeg','-nostdin','-v','error','-xerror','-i',str(p),'-f','null','-'],check=True,capture_output=True)
 decoded=subprocess.check_output(['ffmpeg','-nostdin','-v','error','-i',str(p),'-map','0:a:0','-ar','48000','-ac','2','-f','f32le','-']);n=len(decoded)//8;assert abs(n/48000-13.9)<.08
 report['files'][name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'dimensions':[1080,1920],'fps':30,'frames':417,'duration':float(probe['format']['duration']),'decoded_audio_duration':n/48000,'full_decode':'PASS'}
print(json.dumps(report,indent=2));(r/'OUTPUT_QA.json').write_text(json.dumps(report,indent=2)+'\n')
# Actual encoded phone frames, not source-only screenshots.
for t in [.6,3.4,4.9,6.6,7.5,11.7]:
 data=subprocess.check_output(['ffmpeg','-nostdin','-v','error','-ss',str(t),'-i',str(r/'Cold_Metal_Sequence.mp4'),'-frames:v','1','-vf','scale=270:480','-f','image2pipe','-vcodec','png','-']);(r/'proof'/f'encoded_phone_{t}.png').write_bytes(data)
# Texture high-pass on a calm decoded comparison background.
im=Image.open(r/'proof/encoded_phone_7.5.png').convert('L').crop((8,112,60,155));hp=np.asarray(im,dtype=float)-np.asarray(im.filter(ImageFilter.GaussianBlur(1)),dtype=float);strength=float(np.mean(np.abs(hp)));assert strength>.15,strength
report['encoded_phone_texture_mean_abs_highpass']=strength;report['encoded_phone_texture_scope']='Visible high-frequency texture survives MP4 phone downsample; not an isolated proof of artistic quality or grain alone.'
(r/'OUTPUT_QA.json').write_text(json.dumps(report,indent=2)+'\n')
