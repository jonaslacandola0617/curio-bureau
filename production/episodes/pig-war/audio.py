from pathlib import Path
import numpy as np,json,subprocess,shutil
from scipy.io import wavfile
from scipy.signal import lfilter
import os,sys
sys.path.insert(0,os.environ['CURIO_ENGINE_ROOT'])
import audio as audio_engine
r=Path(os.environ['CURIO_PROJECT_ROOT']);rate=48000;m=json.loads((r/'assets/timing.json').read_text());E=m['events'];n=round(m['duration']*rate)
def load(name):return audio_engine.load(r/'assets'/name,rate)
def save(name,a):audio_engine.save(r/'assets'/name,a,rate)
voice=load('voice_full.wav');score=np.zeros((n,2));fx=np.zeros((n,2));intro=round(E['trigger']*rate)
for name,dest in [('score_r2_stem.wav',score),('sfx_r2_stem.wav',fx)]:
 a=load(name);dest[:intro]=a[:intro]
# Existing library cues supply later material/evidence accents, no new SFX generation.
repo=Path('curio-bureau');sources={'wood_stress.flac':'audio/curio_sfx_v1/mechanical/CB_MECHANICAL_wood_stress_v1.flac','evidence_lock.flac':'audio/curio_sfx_v1/editorial/CB_EDITORIAL_evidence_lock_v1.flac','quiet_resolution.flac':'audio/curio_sfx_v1/editorial/CB_EDITORIAL_quiet_resolution_v1.flac','page_heavy.flac':'audio/curio_sfx_v1/archive/CB_ARCHIVE_paper_heavy_turn_v1.flac','doubt_tick.flac':'audio/curio_sfx_v1/editorial/CB_EDITORIAL_doubt_tick_v1.flac'}
for dest,src in sources.items():
 if (r/'assets'/dest).is_file():continue
 if (repo/src).is_file():shutil.copy2(repo/src,r/'assets'/dest)
 elif not (r/'assets'/dest).is_file():raise FileNotFoundError(src)
cues=json.loads((r/'baseline/SFX_CUE_SHEET_R2.json').read_text())
def cue(name,t,dur,peak,event,pan=0,off=0):
 duration=audio_engine.place_cue(fx,load(name),t,dur,peak,pan,off,rate);cues.append({'file':name,'onset':round(t,3),'duration':duration,'peak_before_master_dbfs':round(20*np.log10(peak),2),'event':event,'source_path':sources.get(name,'audio/generated-editorial-v1/'+name),'provenance':'Designed sound, not historical recording'})
for t in np.arange(E['trigger'],m['duration'],5.95):cue('projector.mp3',float(t),min(6,m['duration']-t),.045,'film mechanism bed')
for a in [('paper.mp3',E['trigger'],.8,.38,'garden returns from map'),('garden_foley.mp3',E['trigger']+.3,1.6,.24,'pig rooting close approach'),('paper.mp3',E['pig_property'],.6,.30,'company property tag'),('marker_bold.mp3',E['arrest'],.8,.40,'ARREST highlight'),('paper.mp3',E['protection'],.7,.36,'PROTECTION title and agency turn'),('camera_move.mp3',E['soldiers']-.15,.85,.36,'garden panel clears to troops'),('evidence_lock.flac',E['soldiers'],.7,.27,'troop marker'),('camera_move.mp3',E['ships'],1.5,.35,'frigate foreground entrance'),('wood_stress.flac',E['ships']+.6,1.4,.24,'ship timber material'),('marker_bold.mp3',E['crisis']+.4,.8,.38,'international crisis emphasis'),('camera_move.mp3',E['restraint'],1.2,.32,'ship retreats from composition'),('quiet_resolution.flac',E['diplomacy'],1.4,.25,'tension release with diplomacy'),('paper.mp3',E['camps'],1.3,.36,'English Camp source arrives'),('page_heavy.flac',E['camps']+2.2,1.2,.30,'American Camp source arrives'),('camera_move.mp3',E['joint'],1.0,.22,'joint occupation source reframe'),('marker_bold.mp3',E['joint']+.15,1.8,.30,'occupation timeline grows'),('paper.mp3',E['arbitration'],1.1,.38,'award transcription arrival'),('camera_move.mp3',E['arbitration']+1.8,1.25,.30,'award macro approach'),('marker_bold.mp3',E['selected'],1.1,.43,'Haro selected in source'),('paper.mp3',E['settlement']+.2,1.2,.38,'award exits into settled interpretation'),('evidence_lock.flac',E['settlement']+.65,.8,.28,'Haro result title'),('camera_move.mp3',E['payoff'],.85,.32,'pig foreground return'),('garden_foley.mp3',E['payoff']+.2,1.2,.20,'pig reminder texture'),('marker_bold.mp3',E['payoff']+.55,.7,.35,'one casualty title'),('paper.mp3',E['border'],1.2,.38,'pig clears to underlying border'),('marker_bold.mp3',E['border']+1.05,.8,.38,'THE BORDER emphasis'),('quiet_resolution.flac',E['brand'],1.1,.24,'integrated brand resolution')]:cue(*a)
# Reuse the approved plucked-string language; develop harmony/instrument density by story state.
rng=np.random.default_rng(441);notes=[]
def pluck(midi,length=1.8):
 hz=440*2**((midi-69)/12);N=int(rate/hz);noise=rng.normal(0,.28,N);size=int(length*rate);z=np.zeros(size);z[:N]=noise;den=np.zeros(N+2);den[0]=1;den[N]=-.495;den[N+1]=-.495;y=lfilter([1],den,z);y*=np.exp(-np.arange(size)/rate/1.35);return y/max(.01,np.max(np.abs(y)))
beat=60/92;chords=[[50,57,62,65],[46,53,58,62],[48,55,60,64],[45,52,57,61]]
for i,t in enumerate(np.arange(E['trigger'],m['duration']-.15,beat)):
 if t<E['restraint']:ch=chords[(i//8)%4];gain=.047
 elif t<E['arbitration']:ch=[50,57,62,66] if i//8%2==0 else [55,59,62,67];gain=.042
 else:ch=[50,57,62,66] if i//8%2==0 else [55,59,62,67];gain=.051
 midi=ch[(i*3)%4]+(12 if i%4==3 else 0);p=round(t*rate);a=pluck(midi)[:n-p];pan=.16 if i%2 else -.16;score[p:p+len(a),0]+=a*gain*(1-pan);score[p:p+len(a),1]+=a*gain*(1+pan);notes.append({'t':float(t),'midi':midi})
 if i%4==0:
  a=pluck(ch[0]-12,2.4)[:n-p];score[p:p+len(a)]+=a[:,None]*.032
# Soft harmonically evolving bowed layer follows danger then relief, not a fixed drone.
for t in np.arange(E['ships'],m['duration']-2,beat*4):
 ch=chords[int((t-E['ships'])/(beat*8))%4] if t<E['restraint'] else [50,57,62,66];length=min(beat*4+1,m['duration']-t);ts=np.arange(round(length*rate))/rate;env=np.minimum(ts/.7,1)*np.minimum((length-ts)/1.1,1);a=np.zeros(len(ts))
 for midi in ch[1:]:
  hz=440*2**((midi+12-69)/12);a+=(np.sin(2*np.pi*hz*ts+.004*np.sin(ts*6))+np.sin(2*np.pi*(hz+.6)*ts))*.0022
 p=round(t*rate);score[p:p+len(a)]+=a[:n-p,None]*env[:n-p,None]
# Speech/FX ducking preserves a clearly audible musical bed.
v=np.max(np.abs(voice),axis=1);sm=np.convolve(v[::480],np.ones(20)/20,mode='same');duck=np.interp(np.arange(n),np.arange(len(sm))*480,1-.32*np.clip(sm*8,0,1));score[intro:]*=duck[intro:,None];score[-round(.6*rate):]*=np.linspace(1,0,round(.6*rate))[:,None]
master=voice+score+fx;master*=.86/max(.86,float(np.max(np.abs(master))));save('mix_pre.wav',master);save('music_full.wav',score);save('sfx_full.wav',fx)
audio_engine.normalize(r/'assets/mix_pre.wav',r/'assets/master_full.wav',rate)
audio_engine.canonical_pcm(r/'assets/master_full.wav',r/'assets/preflight_mix.wav',rate)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(cues,indent=2));(r/'MUSIC_NOTES.json').write_text(json.dumps(notes,indent=2));print('Full mix:',m['duration'],'seconds;',len(cues),'cues; all effects reused')
