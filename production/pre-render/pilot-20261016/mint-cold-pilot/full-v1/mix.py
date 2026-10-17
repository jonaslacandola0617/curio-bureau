from pathlib import Path
import json,subprocess,math,hashlib,numpy as np
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).parent;repo=r.parents[4];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr)
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
a=load(r/'audio/voice-original.mp3');a=np.concatenate([a[:round(4.24*sr)],a[round(4.89*sr):]])
vo=np.zeros((n,2));vo[:len(a)]=a*.60/max(np.max(abs(a)),.001)
t=np.arange(n)/sr;mu=np.zeros_like(vo)
# Original Mint score: curious glassy/plucked motif and a gently evolving harmonic bed.
chords=[[164.814,246.942,329.628],[146.832,220,293.665],[130.813,196,261.626],[174.614,261.626,349.228]]
for k in range(math.ceil(tl['duration']/4)):
 tt=t-k*4;u=np.maximum(tt,0);env=np.where(tt>=0,np.minimum(u/.22,1)*np.exp(-u/3.0),0)
 for f in chords[k%4]:
  v=(np.sin(2*np.pi*f*t)+.17*np.sin(4*np.pi*f*t))*.014*env;mu[:,0]+=v;mu[:,1]+=v*.9
notes=[659.25,493.88,587.33,739.99,659.25,587.33,440,587.33]
for k in range(math.ceil(tl['duration']/1.15)):
 at=.12+k*1.15;f=notes[k%8];tt=t-at;u=np.maximum(tt,0);env=np.where(tt>=0,np.minimum(u/.008,1)*np.exp(-u*4.5),0);v=(np.sin(2*np.pi*f*tt)+.23*np.sin(2*np.pi*2.01*f*tt)+.06*np.sin(2*np.pi*3.99*f*tt))*.045*env;mu[:,k%2]+=v;mu[:,1-k%2]+=v*.65
mu*=np.minimum(t/.18,1)[:,None]*np.clip((tl['duration']-t)/.7,0,1)[:,None]
# One primary cue per action. No pile of paper/marker sounds over the hook.
cues=[('camera_move.mp3',.02,.45,.25,'mint enters foreground / mouth depth'),('marker_bold.mp3',1.70,.24,.25,'not chilled label'),('camera_move.mp3',4.15,.40,.27,'inspect same mint leaf'),('paper.mp3',5.1,.38,.26,'menthol identification print'),('paper.mp3',7.16,.38,.27,'channel print establishes comparison'),('pencil.mp3',11.95,.68,.29,'cooling route draws toward channel'),('ink.mp3',13.05,.20,.24,'cooling route arrives'),('marker_bold.mp3',17.5,.55,.30,'chemical input joins same channel'),('ink.mp3',18.65,.22,.27,'shared channel activation selected'),('camera_move.mp3',22.0,.45,.27,'return to sensation in mouth'),('marker_bold.mp3',23.6,.32,.28,'sensation is not temperature'),('camera_move.mp3',28.25,.42,.27,'mint and ice remain distinct'),('pencil.mp3',31.9,.55,.28,'another route recalled'),('ink.mp3',35.1,.22,.26,'different input resolves'),('paper.mp3',tl['ending_start'],.28,.20,'locked brand arrival')]
fx=np.zeros_like(vo);en=np.sqrt(np.convolve(np.mean(vo*vo,axis=1),np.ones(960)/960,mode='same'));act=np.clip(en/.04,0,1);sheet=[]
for name,at,dur,peak,event in cues:
 p=repo/'audio/generated-editorial-v1'/name;a=load(p);energy=np.sqrt(np.mean(a*a,axis=1));ix=np.where(energy>max(.0005,np.max(energy)*.03))[0];off=max(0,int(ix[0])-240)if len(ix)else 0;a=a[off:off+round(dur*sr)];a=sosfilt(butter(2,7000,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);a*=(1-.30*act[i:i+len(a)])[:,None];fx[i:i+len(a)]+=a;mu[max(0,i-1200):min(n,i+len(a)+3600)]*=.68;sheet.append({'source':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset':at,'duration':len(a)/sr,'peak_target':peak,'event':event})
mu*=(1-.22*act)[:,None]
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,np.int16(np.clip(a,-1,1)*32767))
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8,alimiter=limit=0.85:level=false:latency=true','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n')
print(json.dumps({'duration':tl['duration'],'voice_samples':len(vo),'cues':len(sheet),'protected_tail':tl['protected_tail'],'original_retained':True,'listening_status':'Owner full encoded review pending; no human listening certification claimed'}))
