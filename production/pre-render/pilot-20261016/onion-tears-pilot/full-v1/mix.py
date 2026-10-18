from pathlib import Path
import json,subprocess,math,hashlib,numpy as np
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).parent;repo=r.parents[4];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr);rng=np.random.default_rng(61422)
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
beat=.6;mel=[587.33,659.255,698.456,880,783.991,698.456,659.255,523.251];roots=[146.832,110,116.541,130.813]
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
('cut_match',.12,.27,.30,'cut lands at onion / first physical fact','primary'),
('marker_bold.mp3',E['eye_question']+.10,.24,.28,'eye location question selected','generated'),
('camera_move.mp3',sc[1]['start']+.04,.45,.32,'enter same cut surface','generated'),
('paper.mp3',sc[1]['start']+.55,.40,.31,'tissue inset opens at source selection','generated'),
('pencil.mp3',sc[1]['start']+1.05,.44,.29,'cut tissue boundary traced','generated'),
('paper.mp3',sc[2]['start']+.12,.36,.30,'same origin becomes reaction strip','generated'),
('marker_bold.mp3',E['lfs']-.18,.45,.34,'select LFS-assisted conversion on spoken name','generated'),
('ink.mp3',sc[3]['start']+.32,.22,.29,'LF emerges from cut as one category','generated'),
('camera_move.mp3',sc[4]['start']+.03,.48,.32,'follow LF through shared air space','generated'),
('pencil.mp3',sc[4]['start']+.26,.55,.29,'source-to-eye path extends','generated'),
('camera_move.mp3',sc[5]['start']+.03,.45,.30,'attention arrives at same eye','generated'),
('marker_bold.mp3',sc[5]['start']+.86,.28,.31,'irritation consequence selected','generated'),
('paper.mp3',sc[6]['start']+.10,.30,.28,'full relationship reopens','generated'),
('pencil.mp3',sc[6]['start']+2.8,.58,.28,'retrace airborne connection','generated'),
('camera_move.mp3',sc[6]['start']+6.5,.42,.31,'inspect knife remaining at onion','generated'),
('causal_reveal',sc[6]['start']+9.0,1.0,.27,'reaction reaches eye / final answer','primary'),
('paper.mp3',tl['ending_start'],.26,.22,'exact shared ending arrival','generated')]
import csv
catalog={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())}
fx=np.zeros_like(vo);en=np.sqrt(np.convolve(np.mean(vo*vo,axis=1),np.ones(960)/960,mode='same'));act=np.clip(en/.05,0,1);sheet=[]
for name,at,dur,peak,event,kind in cues:
 p=repo/(catalog[name]['path']if kind=='primary'else 'audio/generated-editorial-v1/'+name);a=load(p);energy=np.sqrt(np.mean(a*a,axis=1));ix=np.where(energy>max(.0005,np.max(energy)*.03))[0];off=max(0,int(ix[0])-240)if len(ix)else 0;a=a[off:off+round(dur*sr)];a=sosfilt(butter(2,6800,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);a=a[:n-i];a*=(1-.22*act[i:i+len(a)])[:,None];fx[i:i+len(a)]+=a;mu[max(0,i-1200):min(n,i+len(a)+2400)]*=.72;sheet.append({'sound_id':name,'asset_file':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset_time':at,'duration':len(a)/sr,'peak_target':peak,'purpose':event,'animation_event_id':event,'narrative_word_id':min(range(len(tl['words'])),key=lambda k:abs(tl['words'][k]['start']-at)),'mix_bus':'PHYSICAL/EDITORIAL SFX','rights':'Existing original Curio designed sound; not authentic recorded onion Foley','edit':'high-cut6800Hz,10ms edges, speech duck22%, music duck28%'})
mu*=(1-.20*act)[:,None]
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,np.int16(np.clip(a,-1,1)*32767))
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8,alimiter=limit=0.85:level=false:latency=true','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/mix.wav'),'-c:a','flac','-compression_level','8',str(r/'Onion-Mix-v1.flac')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n');(r/'MUSIC_DIRECTION.json').write_text(json.dumps({'method':'Original local composition, deterministic source in mix.py','runway_generation':'Blocked by current plan; no music task created','tempo':100,'form':'curious two-note hook, tactile marimba investigation, sparse high-register airborne passage, warm harmonic answer, exact ending arrival','instruments':['inharmonic mallet/plucks','upright-like bass','filtered brush percussion','slow chamber triads'],'licensed_inputs':'No external music samples','listening':'Complete encoded owner review pending'},indent=2)+'\n')
print(json.dumps({'duration':tl['duration'],'cues':len(sheet),'voice_end':len(a)/sr if False else tl['voice_edited_duration'],'original_tail_retained':True,'master_peak':float(np.max(abs(load(r/'audio/mix.wav'))))}))
