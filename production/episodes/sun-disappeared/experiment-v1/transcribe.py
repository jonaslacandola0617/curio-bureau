from pathlib import Path
import sys,json,subprocess
sys.path.insert(0,'/workspace/scratch/292e697b57ab/curio-tools')
from faster_whisper import WhisperModel
import numpy as np
r=Path(__file__).parent
m=WhisperModel('base.en',device='cpu',compute_type='int8',cpu_threads=4,download_root='/workspace/scratch/292e697b57ab/curio-models')
pcm=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'audio/voice-original.mp3'),'-ar','16000','-ac','1','-f','f32le','-']),dtype=np.float32)
segments,info=m.transcribe(pcm,language='en',word_timestamps=True,beam_size=5,vad_filter=False)
words=[];ss=[]
for s in segments:
 print(s.start,s.end,s.text,flush=True)
 ss.append({'start':s.start,'end':s.end,'text':s.text})
 for w in s.words:words.append({'start':w.start,'end':w.end,'text':w.word.strip(),'probability':w.probability})
(r/'TRANSCRIPT_ORIGINAL.json').write_text(json.dumps({'method':'Local faster-whisper/base.en; actual-audio ASR word events, not independently verified forced alignment','words':words,'segments':ss},indent=2)+'\n')
