from pathlib import Path
import numpy as np,json,subprocess,hashlib,math
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).parent;repo=r.parents[4];sr=48000
load=lambda p:np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
voice=load(r/'audio/voice_original.mp3');on=.18;duration=math.ceil((on+len(voice)/sr+.92)*30)/30;n=round(sr*duration);vo=np.zeros((n,2));voice*=.62/max(np.max(abs(voice)),.001);start=round(on*sr);vo[start:start+len(voice)]=voice;t=np.arange(n)/sr
mu=np.zeros_like(vo)
for i,notes in enumerate([[146.832,220,261.626],[174.614,261.626,349.228],[196,246.942,293.665],[130.813,196,261.626]]):
 tt=t-i*3.4;u=np.maximum(tt,0);env=np.where(tt>=0,np.minimum(u/.35,1)*np.exp(-u/3.4),0)
 for f in notes:
  v=(np.sin(2*np.pi*f*t)+.23*np.sin(2*np.pi*2*f*t))*.012*env;mu[:,0]+=v;mu[:,1]+=v*.92
for k,f in enumerate([587.33,440,523.25,659.25,587.33,523.25,392,523.25,659.25,523.25]):
 tt=t-(.3+k*1.26);u=np.maximum(tt,0);env=np.where(tt>=0,np.minimum(u/.012,1)*np.exp(-u*3.8),0);v=(np.sin(2*np.pi*f*tt)+.21*np.sin(2*np.pi*2*f*tt)+.08*np.sin(2*np.pi*3*f*tt))*.042*env;mu[:,0]+=v;mu[:,1]+=v*.87
mu*=np.minimum(t/.22,1)[:,None]*np.clip((duration-t)/.65,0,1)[:,None]
fx=np.zeros_like(vo);sheet=[]
# One action cue at a time in the first reveal; contact and paper land before speech.
cues=[('camera_move.mp3',0,.50,.24,'photographic approach'),('ink.mp3',2.64,.12,.16,'contact ring closure'),('paper.mp3',2.80,.34,.29,'printed inspection launch and settle'),('pencil.mp3',3.88,.94,.24,'three continuous qualitative heat-flow strokes'),('camera_move.mp3',6.43,.40,.25,'registered comparison cut'),('marker_bold.mp3',7.00,.40,.27,'faster metal transfer'),('pencil.mp3',8.04,.46,.25,'slower wood transfer'),('paper.mp3',9.74,.24,.22,'same-starting-condition tag')]
# Speech activity has fast attack and 80ms release; protects consonants without hiding Foley.
voice_env=np.sqrt(np.convolve(np.mean(vo*vo,axis=1),np.ones(480)/480,mode='same'))
activity=np.clip(voice_env/.025,0,1)
release=np.exp(-1/(sr*.08));held=0.
for j in range(n):held=max(activity[j],held*release);activity[j]=held

for name,at,dur,peak,event in cues:
 p=repo/'audio/generated-editorial-v1'/name;a=load(p);energy=np.sqrt(np.mean(a*a,axis=1));idx=np.where(energy>max(.0005,np.max(energy)*.03))[0];offset=max(0,int(idx[0])-480)if len(idx)else 0;a=a[offset:offset+round(dur*sr)];a=sosfilt(butter(2,6500,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(960,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);a*= (1-.56*activity[i:i+len(a)])[:,None];fx[i:i+len(a)]+=a;mu[max(0,i-1500):min(n,i+len(a)+4000)]*=.64;sheet.append(dict(source=str(p.relative_to(repo)),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),onset=at,duration=len(a)/sr,event=event,peak_target=peak,speech_duck_max_db=-7.13,lowpass_hz=6500,provenance='Existing Curio designed cue; not sound of heat or an actual experiment'))
for name,a in [('voice.wav',vo),('music.wav',mu),('sfx.wav',fx),('raw.wav',vo+mu+fx)]:wavfile.write(r/'audio'/name,sr,np.int16(np.clip(a,-1,1)*32767))
normalized=np.frombuffer(subprocess.check_output(['ffmpeg','-nostdin','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8,volume=0.6dB,alimiter=limit=0.85:level=false:latency=true','-ar','48000','-ac','2','-f','f32le','-']),np.float32).reshape(-1,2)
assert len(normalized)==n,(len(normalized),n)
wavfile.write(r/'audio/mix.wav',sr,np.int16(np.clip(normalized,-1,1)*32767))
# Phrase boundaries use measured pauses and script; not claimed independently word-aligned.
caps=[(.26,2.75,['Your hand is warmer','than the spoon.']),(3.23,6.15,['Touch it, and heat flows','out of your skin.']),(6.50,9.45,['Metal carries that energy','away faster than wood.']),(10.02,11.48,['Same starting temperature.']),(11.68,duration-.15,['Different heat transfer.'])]
(r/'timeline.json').write_text(json.dumps({'duration':duration,'fps':30,'frames':round(duration*30),'captions':[dict(start=a,end=b,lines=s)for a,b,s in caps],'caption_status':'phrase estimates informed by source silence; not word-verified','events':sheet},indent=2)+'\n');(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n')
(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'voice':'Bernard','task_id':'37575f5f-aea2-44d1-9e10-46cbe82388d2','source_sha256':hashlib.sha256((r/'audio/voice_original.mp3').read_bytes()).hexdigest(),'decoded_samples':len(voice),'sample_rate':sr,'source_onset':on,'source_end':on+len(voice)/sr,'duration':duration,'preserved_all_decoded_samples':True,'voice_fade':False,'protected_tail':duration-on-len(voice)/sr,'closing_phrase':'Different heat transfer.','final_word':'transfer','endcard':'Not included in isolated passage','encoded_ending_listening':'OWNER REVIEW PENDING'},indent=2)+'\n');print('Mixed',duration,'seconds; original narration preserved; existing SFX only.')
