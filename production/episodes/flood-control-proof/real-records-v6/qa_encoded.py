from pathlib import Path
import subprocess,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent
movie=P/'Curio-Flood-Proof-Real-Records-v6.mp4'
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(movie)]))
v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1080,1920,'30/1',1822)
assert a['sample_rate']=='48000'and a['channels']==2
subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(movie),'-f','null','-'],check=True)
D=P/'review/encoded';D.mkdir(exist_ok=True)
times=[.3,2.1,4.4,7.04,10.5,12.68,14.7,16.5,18.8,20.6,22.1,24.2,26.32,29.6,32.8,34.82,38,40.52,42.5,45.06,47.9,50.6,53.4,55.93,57.5,59.23,59.8,60.7]
board=Image.new('RGB',(1440,4648),(13,28,43));d=ImageDraw.Draw(board)
for i,t in enumerate(times):
 dest=D/f'{t:05.1f}.png'
 subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(dest)],check=True)
 im=Image.open(dest);board.paste(im.resize((360,640)),((i%4)*360,(i//4)*664));d.text(((i%4)*360+10,(i//4)*664+643),f'{t:.1f} seconds',fill=(245,240,231))
board.save(D/'encoded-review-board.jpg',quality=96)
for j in range(3):
 chunk=Image.new('RGB',(1440,1992),(13,28,43))
 for i,t in enumerate(times[j*12:(j+1)*12]):
  im=Image.open(D/f'{t:05.1f}.png');chunk.paste(im.resize((360,640)),((i%4)*360,(i//4)*664));ImageDraw.Draw(chunk).text(((i%4)*360+10,(i//4)*664+643),f'{t:.2f} seconds',fill=(245,240,231))
 chunk.save(D/f'encoded-board-{j+1}.jpg',quality=96)
last=np.asarray(Image.open(D/'060.7.png').convert('RGB'),dtype=float)
expected=np.asarray(Image.open(P/'ending/032.png').convert('RGB'),dtype=float)
ending={'mean_absolute_rgb_error':float(np.mean(np.abs(last-expected))),'rmse':float(np.sqrt(np.mean((last-expected)**2)))}
subprocess.run(['ffmpeg','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=7:print_format=json','-f','null','-'],stdout=subprocess.DEVNULL,stderr=(D/'loudness.log').open('w'),check=True)
log=(D/'loudness.log').read_text();loud=json.loads(log[log.rfind('{'):])
receipt={'file':movie.name,'sha256':hashlib.sha256(movie.read_bytes()).hexdigest(),'bytes':movie.stat().st_size,'duration_seconds':float(probe['format']['duration']),'video':{'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'frames':int(v['nb_frames']),'codec':v['codec_name'],'pixel_format':v['pix_fmt']},'audio':{'codec':a['codec_name'],'sample_rate':a['sample_rate'],'channels':a['channels'],'measured_integrated_lufs':loud['input_i'],'measured_true_peak_dbtp':loud['input_tp'],'measured_lra':loud['input_lra']},'full_decode':'PASS','ending_comparison_to_shared_module_png':ending,'contact_sheet_timestamps':times,'independent_listening':'PENDING; not claimed','caption_boundaries':'script reconciled actual-audio ASR; independent listening pending','owner_approval':'PENDING','publication':'NOT PERFORMED','authored_state_cadence':'12fps verified in current source, not inferred from encoded30fps','runtime_finishing_proof':'11 effect on/off cases + phone temporal grain + protected captions/ending; artistic quality separate'}
(D/'ENCODED_QA.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
