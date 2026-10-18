from pathlib import Path
import json,subprocess,math,csv,hashlib,numpy as np
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).resolve().parent;ep=r.parent;repo=ep.parents[3];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr);rng=np.random.default_rng(19981)
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
a=load(ep/'audio/voice-edit.wav');a=a[round(tl['start_in_voice']*sr):round(tl['end_in_voice']*sr)];vo=np.zeros((n,2));vo[:len(a)]=a*.62/max(np.max(abs(a)),.001);mu=np.zeros_like(vo);fx=np.zeros_like(vo)
def put(at,v,pan=0):
 i=round(at*sr);l=min(len(v),n-i)
 if i<0 or l<=0:return
 mu[i:i+l,0]+=v[:l]*math.sqrt((1-pan)/2);mu[i:i+l,1]+=v[:l]*math.sqrt((1+pan)/2)
def pluck(at,f,amp,pan=0):
 u=np.arange(round(1.6*sr))/sr;v=(np.sin(2*np.pi*f*u)*np.exp(-u*4.0)+.3*np.sin(2*np.pi*f*2.01*u)*np.exp(-u*10))*np.minimum(u/.004,1)*amp;put(at,v,pan)
mel=[329.628,493.883,369.994,440,329.628,246.942,293.665,369.994]
for k in range(19):
 at=.08+k*.5
 if at>9.3:break
 pluck(at,mel[k%len(mel)],.083 if k<10 else .060,(-.32 if k%2 else .32))
 if k%4==0:
  u=np.arange(round(1.6*sr))/sr;put(at,np.sin(2*np.pi*[82.407,73.416,61.735][(k//4)%3]*u)*np.minimum(u/.02,1)*np.exp(-u*2.8)*.07)
for at,ch in [(0,[164.814,196,246.942]),(3.6,[146.832,184.997,220]),(6.5,[123.471,164.814,196])]:
 u=np.arange(round(4*sr))/sr
 for j,f in enumerate(ch):put(at,np.sin(2*np.pi*f*u)*np.minimum(u/.25,1)*np.exp(-u/2)*.018,(-.4+j*.4))
# Remove upper musical voices at daylight loss, retaining a gentle decaying low motif.
mu[round(9.45*sr):]*=.25
for at,f in [(9.50,82.407),(10.25,164.814)]:pluck(at,f,.045,0)
t=np.arange(n)/sr;mu*=np.minimum(t/.08,1)[:,None]*np.clip((tl['duration']-t)/.4,0,1)[:,None]
cat={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())}
cues=[('doubt_tick',.08,.45,.25,'light marks begin moving'),('pencil_marks',1.70,.5,.29,'emission-time keyword revealed'),('parallax_swish',3.40,.65,.32,'camera follows same travel path'),('photo_slide',5.05,.6,.36,'Sun photographic layer wipes away'),('pencil_marks',6.80,.55,.28,'absence boundary advances; empty path revealed'),('soft_depth_pass',8.50,.7,.30,'remaining distance inspection'),('micro_emphasis',9.55,.5,.34,'last sunlight reaches Earth; daylight clears')]
sheet=[]
for name,at,dur,peak,event in cues:
 p=repo/cat[name]['path'];a=load(p)[:round(dur*sr)];a=sosfilt(butter(2,7000,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);l=min(len(a),n-i);fx[i:i+l]+=a[:l];mu[max(0,i-960):min(n,i+l+1920)]*=.7
 sheet.append({'sound_id':name,'asset_file':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset_time':at,'duration':l/sr,'purpose':event,'animation_event_id':event,'narrative_word_id':min(range(len(tl['words'])),key=lambda k:abs(tl['words'][k]['start']-at)),'mix_bus':'EDITORIAL/PHYSICAL','peak_target':peak,'rights':'Original Curio synthesized library; editorial effects, not sounds transmitted through vacuum'})
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,np.int16(np.clip(a,-1,1)*32767))
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=7','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'audio/mix.wav'),'-c:a','flac','-compression_level','8',str(r/'Passage-Mix-v1.flac')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n')
(r/'MUSIC_DIRECTION.json').write_text(json.dumps({'method':'Original deterministic local composition; no reused music track or outside samples','key':'E minor / suspended modal changes','instruments':['inharmonic glass plucks','restrained sine/wood-like bass','three evolving chamber triads'],'story':'Already-emitted-light motif, reduced texture after source removal, high voices stop when daylight ends','subjective_listening':'Owner moving review pending; not claimed'},indent=2)+'\n')
print('Mixed complete three-phrase excerpt, original score and 7 existing cues. Duration',n/sr)
