from pathlib import Path
import sys,json,subprocess,hashlib,re
import numpy as np
from faster_whisper import WhisperModel
r=Path(__file__).resolve().parent;sys.path.insert(0,str(r/'engine'));from curio import verify
names=['Recorded_Voice_4K_Master.mp4','Recorded_Voice_4K_Upload.mp4','Recorded_Voice_4K.webm'];result={}
model=WhisperModel('tiny.en',device='cpu',compute_type='int8');norm=lambda s:re.sub('[^a-z0-9]','',s.lower());closing="Both versions are you. You're hearing them through different routes."
for name in names:
 p=r/name;check=verify(p,2,1058,1058/30)
 if 'Upload' in name and p.stat().st_size>=512*1024*1024:raise ValueError('Posting copy exceeds download size limit')
 measure=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','loudnorm=I=-13:TP=-1.5:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True,check=True);levels=json.loads(measure.stderr[measure.stderr.rfind('{'):])
 if not -14<=float(levels['input_i'])<=-12 or float(levels['input_tp'])>-1:raise ValueError('Encoded sound outside target: '+name)
 raw=subprocess.check_output(['ffmpeg','-v','error','-ss','23.2','-i',str(p),'-f','f32le','-ar','16000','-ac','1','pipe:1']);segments,info=model.transcribe(np.frombuffer(raw,dtype=np.float32).copy(),language='en',beam_size=5,condition_on_previous_text=False,vad_filter=False);transcript=' '.join(s.text.strip() for s in segments)
 if norm(closing) not in norm(transcript):raise ValueError('Closing sentence recognition mismatch: '+name+' '+transcript)
 check.update(sha256=hashlib.sha256(p.read_bytes()).hexdigest(),audio_levels=levels,encoded_tail_transcript=transcript,complete_closing_sentence_ASR=True);result[name]=check;print(name,check['width'],check['height'],check['frames'],levels['input_i'],levels['input_tp'],'tail complete',flush=True)
q={'status':'NATIVE DELIVERY — OWNER-APPROVED PICTURE AND MIX; ENCODED TECHNICAL QA PASSED','outputs':result,'source_mix_sha256':hashlib.sha256((r/'project/assets/preflight_mix.wav').read_bytes()).hexdigest(),'render_method':'Native2160×3840 RGBA at frameN/30 into H264 CRF15/CRF20 and VP9 CRF22 video-only sections; packet-copy assembly with continuous original mix; no upscale or video re-encode','owner_review':'Approved 1080p picture/audio15October2026; resolution-only export','phonetic_check_scope':'Encoded closing sentence ASR passes, complete original source held0.7667seconds before ending; no additional independent human listening certificate asserted','visual_checks':'Native encoded opening inspected; final native representative states pending inspection','posts':'Recorded_Voice_Posts.txt includes platform copy and source/image-license credits'}
(r/'Recorded_Voice_4K_QA.json').write_text(json.dumps(q,indent=2));print('All native encoded outputs passed',flush=True)
