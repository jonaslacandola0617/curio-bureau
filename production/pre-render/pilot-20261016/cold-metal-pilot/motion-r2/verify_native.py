from pathlib import Path
import subprocess,json,hashlib,re,wave,math,os
import numpy as np
from PIL import Image,ImageFilter
r=Path(__file__).resolve().parent;report={'scope':'R2 13.9-second native4K sequence, not a full episode','files':{},'owner_motion_review':'R2 correction requested; revised result pending owner review','subjective_listening':'Owner R1 feedback addressed through cue separation and ducking; independent human phone/headphone listening not claimed','full_film_ending':'Not present in isolated sequence; not certified'}
for name in ['Cold_Metal_R2_4K.mp4','Cold_Metal_R2_4K.webm','Cold_Metal_R2_Posting.mp4']:
 p=r/name;probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
 assert(v['width'],v['height'],v['avg_frame_rate'],int(v['nb_read_frames']))==(2160,3840,'30/1',417)
 assert a['sample_rate']=='48000' and a['channels']==2
 assert(v['codec_name'],a['codec_name'])==(('vp9','opus')if name.endswith('.webm')else('h264','aac'))
 assert v.get('color_primaries')=='bt709' and v.get('color_transfer')=='iec61966-2-1' and v.get('color_space')=='bt709'
 if 'Posting'in name:assert p.stat().st_size<512*1024*1024,'Posting copy exceeds512MiB'
 assert abs(float(probe['format']['duration'])-13.9)<.08
 subprocess.run(['ffmpeg','-nostdin','-v','error','-xerror','-i',str(p),'-f','null','-'],check=True,capture_output=True)
 loud=subprocess.run(['ffmpeg','-nostdin','-hide_banner','-i',str(p),'-vn','-sn','-af','loudnorm=I=-14:TP=-1:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True,check=True).stderr
 metrics=json.loads(re.search(r'\{\s*"input_i".*?\}',loud,re.S).group())
 assert -14<=float(metrics['input_i'])<=-12,(name,metrics)
 assert float(metrics['input_tp'])<=-1,(name,metrics)
 pcm=np.frombuffer(subprocess.check_output(['ffmpeg','-nostdin','-v','error','-i',str(p),'-map','0:a:0','-f','f32le','-ar','48000','-ac','2','-']),np.float32).reshape(-1,2)
 assert abs(len(pcm)/48000-13.9)<.08
 from scipy.io import wavfile
 sr,mix=wavfile.read(r/'audio/mix.wav');ref=mix.astype(float)/32768;n=min(len(ref),len(pcm));corr=float(np.corrcoef(ref[:n].mean(axis=1),pcm[:n].mean(axis=1))[0,1]);assert corr>.97,(name,corr)
 tail=slice(int(11.65*48000),int(13.05*48000));tailcorr=float(np.corrcoef(ref[tail].mean(axis=1),pcm[tail].mean(axis=1))[0,1]);assert tailcorr>.95,(name,tailcorr)
 report['files'][name]={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'dimensions':[2160,3840],'fps':30,'frames':417,'duration':float(probe['format']['duration']),'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'audio_rate':48000,'audio_channels':2,'decoded_audio_duration':len(pcm)/48000,'loudness_lufs':float(metrics['input_i']),'true_peak_dbtp':float(metrics['input_tp']),'mix_correlation':corr,'closing_phrase_correlation':tailcorr,'full_decode':'PASS'}
 print('VERIFIED',name,metrics['input_i'],metrics['input_tp'],flush=True)
(r/'proof').mkdir(exist_ok=True)
times=[2.5,2.7,2.9,3.16,3.4,3.88,4.2,4.9,5.1,6.45,6.6,6.9,7.4,8.4,10.3,12.2,13.6]
indices=[math.ceil(t*30-1e-6)for t in times]
selector="select='"+'+'.join(f'eq(n,{n})'for n in indices)+"',scale=270:480"
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-i',str(r/'Cold_Metal_R2_4K.mp4'),'-an','-sn','-vf',selector,'-fps_mode','vfr',str(r/'proof/selected_%02d.png')],check=True)
for i,t in enumerate(times,1):os.replace(r/'proof'/f'selected_{i:02d}.png',r/'proof'/f'encoded_{t}.png')
report['encoded_phone_review_frame_indices']=indices
im=Image.open(r/'proof/encoded_7.4.png').convert('L').crop((8,112,60,155));hp=np.asarray(im,dtype=float)-np.asarray(im.filter(ImageFilter.GaussianBlur(1)),dtype=float);report['phone_texture_mean_abs_highpass']=float(np.mean(abs(hp)));assert report['phone_texture_mean_abs_highpass']>.15
# Compare delivered settled frame with native rendered proof, allowing codec/JPEG error.
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-ss','4.9','-i',str(r/'Cold_Metal_R2_4K.mp4'),'-frames:v','1',str(r/'proof/encoded_native_4.9.png')],check=True)
a=np.asarray(Image.open(r/'proof/native_4.9.jpg').convert('RGB').resize((540,960)),dtype=float);b=np.asarray(Image.open(r/'proof/encoded_native_4.9.png').convert('RGB').resize((540,960)),dtype=float);delta=float(np.mean(abs(a-b)));assert delta<6,('Source/encoded mismatch',delta)
report['settled_native_source_to_encoded_mean_rgb_difference']=delta
subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-ss','4.9','-i',str(r/'Cold_Metal_R2_4K.webm'),'-frames:v','1','-vf','scale=540:960',str(r/'proof/webm_native_4.9.png')],check=True)
w=np.asarray(Image.open(r/'proof/webm_native_4.9.png').convert('RGB'),dtype=float);wd=float(np.mean(abs(a-w)));assert wd<7,('WebM source mismatch',wd)
report['webm_native_source_mean_rgb_difference']=wd
webphone=Image.open(r/'proof/webm_native_4.9.png').convert('L').resize((270,480)).crop((8,112,60,155));wh=np.asarray(webphone,dtype=float)-np.asarray(webphone.filter(ImageFilter.GaussianBlur(1)),dtype=float);report['webm_phone_texture_mean_abs_highpass']=float(np.mean(abs(wh)));assert report['webm_phone_texture_mean_abs_highpass']>.15
(r/'OUTPUT_QA.json').write_text(json.dumps(report,indent=2)+'\n');print('All output checks PASS')
