from pathlib import Path
import json,subprocess,math,hashlib,numpy as np
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).parent;repo=r.parents[3];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr);rng=np.random.default_rng(61422)
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
a=load(r/'audio/voice-original.mp3');pieces=[];last=0
for e in tl['voice_silence_edits']:
 pieces.append(a[last:round(e['start']*sr)]);last=round(e['end']*sr)
pieces.append(a[last:]);a=np.concatenate(pieces)
vo=np.zeros((n,2));vo[:len(a)]=a*.62/max(np.max(abs(a)),.001)
mu=np.zeros_like(vo);t=np.arange(n)/sr
# Original subject-specific chamber groove. Voice remains centered; plucks and brushes spread gently.
def put(at,x,pan=0):
 i=round(at*sr);l=min(len(x),n-i)
 if i<0 or l<=0:return
 mu[i:i+l,0]+=x[:l]*math.sqrt((1-pan)/2);mu[i:i+l,1]+=x[:l]*math.sqrt((1+pan)/2)
def mallet(at,f,amp=.07,pan=0):
 u=np.arange(round(1.9*sr))/sr;v=(np.sin(2*np.pi*f*u)*np.exp(-u*4.2)+.38*np.sin(2*np.pi*f*2.015*u)*np.exp(-u*9)+.10*np.sin(2*np.pi*f*3.97*u)*np.exp(-u*16));v*=np.minimum(u/.004,1)*amp;put(at,v,pan);put(at+.14,v*.15,-pan)
def bass(at,f,amp=.045):
 u=np.arange(round(.75*sr))/sr;v=(np.sin(2*np.pi*f*u)+.22*np.sin(2*np.pi*f*2*u))*np.minimum(u/.016,1)*np.exp(-u*4.2)*amp;put(at,v,0)
beat=60/108;mel=[587.33,698.456,659.255,880,783.991,698.456,659.255,587.33];roots=[146.832,116.541,98,110]
for k in range(math.ceil(tl['duration']/beat)):
 at=.05+k*beat;section=next((i for i,s in enumerate(tl['scenes'])if s['start']<=at<s['end']),6);root=roots[(k//8)%4]
 if k%2==0:
  f=mel[(k//2+section)%len(mel)];amp=.074 if section in [2,3]else .058
  if section==4:amp=.045;f*=2
  mallet(at+(.035 if k%4==2 else 0),f,amp,(-.32 if k%4==0 else .32))
 if k%4==0:bass(at,root/2,.06)
 if section in [1,2,3,6] and k%2==1:
  u=np.arange(round(.11*sr))/sr;noise=rng.normal(0,1,len(u));noise=sosfilt(butter(2,[2200,6500],fs=sr,btype='bandpass',output='sos'),noise);put(at,noise*np.exp(-u*42)*.025,.18)
 if section in [2,6] and k%4==3:mallet(at+.31,mel[(k+3)%8]/2,.032,-.25)
# Evolving warm triads; sparse in the airborne passage, brighter at the answer.
for k in range(math.ceil(tl['duration']/4.8)):
 at=k*4.8;root=roots[k%4];third=root*(2**(3/12)if k<6 else 2**(4/12));ch=[root,third,root*1.5]
 u=np.arange(round(5.3*sr))/sr;env=np.minimum(u/.5,1)*np.exp(-u/2.8)
 for j,f in enumerate(ch):put(at,np.sin(2*np.pi*f*u+0.04*np.sin(u*3.1))*env*.013,(-.45+j*.45))
# Final measured harmonic arrival supports the locked endcard.
for j,f in enumerate([293.665,369.994,440,587.33]):mallet(tl['ending_start']+.02+j*.025,f,.045,(-.2+j*.13))
mu*=np.minimum(t/.10,1)[:,None]*np.clip((tl['duration']-t)/.5,0,1)[:,None]
E=tl['events'];sc=tl['scenes'];cues=[
('micro_emphasis',E['felt']+.02,.20,.30,'subjective felt-buzz annotation, not a physical phone recording','primary'),
('camera_move.mp3',sc[1]['start']+.04,.42,.40,'hand-held phone inspection begins','generated'),
('doubt_tick',E['nothing']+.02,.24,.32,'empty screen contradiction','primary'),
('paper.mp3',sc[2]['start']+.04,.35,.34,'two image states compare felt and device','generated'),
('marker_bold.mp3',sc[2]['start']+.48,.32,.38,'felt versus device-still labels resolve','generated'),
('camera_move.mp3',sc[3]['start']+.04,.42,.39,'enter the same pocket detail','generated'),
('pencil.mp3',sc[3]['start']+.35,.60,.36,'candidate sensation selection draws','generated'),
('marker_bold.mp3',E['expect']+.06,.38,.39,'expectation state becomes readable','generated'),
('ink.mp3',E['buzz']+.03,.22,.36,'interpretation changes to phone buzz question','generated'),
('camera_move.mp3',sc[4]['start']+.04,.38,.37,'candidate comparison settles','generated'),
('paper.mp3',sc[5]['start']+.04,.40,.35,'original research summary enters','generated'),
('evidence_lock',E['survey']+.03,.65,.30,'self-reported study evidence selected','primary'),
('marker_bold.mp3',E['not_proven']+.04,.40,.38,'cause not established is emphasized','generated'),
('paper.mp3',sc[6]['start']+.04,.35,.34,'return to opening pocket with revised understanding','generated'),
('micro_emphasis',E['final']+.03,.20,.28,'felt sensation contrasted with device','primary'),
('warm_resolution',tl['voice_edited_duration']-.85,2.45,.20,'earned resolution after final explanation','primary')
]
import csv
catalog={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())}
fx=np.zeros_like(vo);en=np.sqrt(np.convolve(np.mean(vo*vo,axis=1),np.ones(960)/960,mode='same'));act=np.clip(en/.05,0,1);sheet=[]
for name,at,dur,peak,event,kind in cues:
 p=repo/(catalog[name]['path']if kind=='primary'else 'audio/generated-editorial-v1/'+name);a=load(p);energy=np.sqrt(np.mean(a*a,axis=1));ix=np.where(energy>max(.0005,np.max(energy)*.03))[0];off=max(0,int(ix[0])-240)if len(ix)else 0;a=a[off:off+round(dur*sr)];a=sosfilt(butter(2,6800,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);a=a[:n-i];a*=(1-.22*act[i:i+len(a)])[:,None];fx[i:i+len(a)]+=a;mu[max(0,i-1200):min(n,i+len(a)+2400)]*=.72;sheet.append({'sound_id':name,'asset_file':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset_time':at,'duration':len(a)/sr,'peak_target':peak,'purpose':event,'animation_event_id':event,'narrative_word_id':min(range(len(tl['words'])),key=lambda k:abs(tl['words'][k]['start']-at)),'mix_bus':'PHYSICAL/EDITORIAL SFX','rights':'Existing original Curio designed cue, not a real recording of a phantom sensation','edit':'high-cut6800Hz,10ms edges, speech duck22%, music duck28%'})
mu*=(1-.20*act)[:,None]
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,np.int16(np.clip(a,-1,1)*32767))
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8,alimiter=limit=0.85:level=false:latency=true','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/mix.wav'),'-c:a','flac','-compression_level','8',str(r/'Phantom-Mix-v1.flac')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n');(r/'MUSIC_DIRECTION.json').write_text(json.dumps({'method':'Original local composition, deterministic source in mix.py','runway_generation':'No music generation requested; original score composed locally','tempo':108,'form':'familiar two-note motif, tactile pluck investigation, reduced score during evidence qualification, warm answer and exact ending arrival','instruments':['inharmonic mallet/plucks','upright-like bass','filtered brush percussion','slow chamber triads'],'licensed_inputs':'No external music samples','listening':'Complete encoded owner review pending'},indent=2)+'\n')
print(json.dumps({'duration':tl['duration'],'cues':len(sheet),'voice_end':len(a)/sr if False else tl['voice_edited_duration'],'original_tail_retained':True,'master_peak':float(np.max(abs(load(r/'audio/mix.wav'))))}))
