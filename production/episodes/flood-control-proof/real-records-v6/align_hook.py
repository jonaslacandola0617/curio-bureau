from pathlib import Path
import subprocess,numpy as np,json
from faster_whisper import WhisperModel
P=Path(__file__).resolve().parent
x=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(P/'audio/hook-original.mp3'),'-ar','16000','-ac','1','-f','f32le','-']),np.float32)
m=WhisperModel('base.en',device='cpu',compute_type='int8',local_files_only=True)
ss,info=m.transcribe(x,word_timestamps=True,language='en',beam_size=5)
w=[];segments=[]
for s in ss:
 segments.append({'start':s.start,'end':s.end,'text':s.text})
 for a in s.words:w.append({'word':a.word.strip(),'start':a.start,'end':a.end,'probability':a.probability})
(P/'audio/HOOK_ASR.json').write_text(json.dumps({'segments':segments,'words':w},indent=2))
print(json.dumps(segments))
