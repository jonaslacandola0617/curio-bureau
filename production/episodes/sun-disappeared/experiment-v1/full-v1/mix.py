from pathlib import Path
import json,subprocess,math,csv,hashlib,numpy as np
from scipy.io import wavfile
from scipy.signal import butter,sosfilt
r=Path(__file__).resolve().parent;ep=r.parent;repo=ep.parents[3];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr);rng=np.random.default_rng(19981)
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
a=load(ep/'audio/voice-edit.wav');vo=np.zeros((n,2));vo[:len(a)]=a*.62/max(np.max(abs(a)),.001);mu=np.zeros_like(vo);fx=np.zeros_like(vo)
def put(at,v,pan=0):
 i=round(at*sr);l=min(len(v),n-i)
 if i<0 or l<=0:return
 mu[i:i+l,0]+=v[:l]*math.sqrt((1-pan)/2);mu[i:i+l,1]+=v[:l]*math.sqrt((1+pan)/2)
def pluck(at,f,amp,pan=0):
 u=np.arange(round(1.6*sr))/sr;v=(np.sin(2*np.pi*f*u)*np.exp(-u*4.0)+.3*np.sin(2*np.pi*f*2.01*u)*np.exp(-u*10))*np.minimum(u/.004,1)*amp;put(at,v,pan)
mel=[329.628,493.883,369.994,440,329.628,246.942,293.665,369.994]
for k in range(98):
 at=.08+k*.5;section=next((i for i,s in enumerate(tl['scenes'])if s['start']<=at<s['end']),7)
 if 14.35<=at<26.3:continue
 amp=.075 if section in [0,2,5]else .058;f=mel[(k+2*section)%len(mel)]
 if section==6:f*=.5;amp=.085
 if section==7:f*=1.0;amp=.065
 pluck(at,f,amp,(-.32 if k%2 else .32))
 if k%4==0:
  u=np.arange(round(1.6*sr))/sr;put(at,np.sin(2*np.pi*[82.407,73.416,61.735,98][(k//8)%4]*u)*np.minimum(u/.02,1)*np.exp(-u*2.8)*.062)
for j,at in enumerate([0,3.6,7.2,10.8,26.3,29.9,33.5,37.1,40.7,44.3]):
 root=[164.814,146.832,123.471,196][j%4];ch=[root,root*2**((4 if j>7 else 3)/12),root*1.5];u=np.arange(round(4*sr))/sr
 for k,f in enumerate(ch):put(at,np.sin(2*np.pi*f*u)*np.minimum(u/.25,1)*np.exp(-u/2)*.017,(-.4+k*.4))
# A new lower pulse accompanies delayed gravity; brighter harmonic return supports the final insight.
for at in np.arange(27,40,.85):
 u=np.arange(round(.12*sr))/sr;v=sosfilt(butter(2,[1400,5200],fs=sr,btype='bandpass',output='sos'),rng.normal(0,1,len(u)))*np.exp(-u*35)*.022;put(float(at),v,.12)
for j,f in enumerate([164.814,207.652,246.942,329.628]):pluck(tl['ending_start']+.025*j,f,.050,-.25+j*.17)
t=np.arange(n)/sr;mu*=np.minimum(t/.08,1)[:,None]*np.clip((tl['duration']-t)/.4,0,1)[:,None]
cat={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())}
cues=[('photo_slide',.05,.6,.35,'Sun photographic layer removal'),('parallax_swish',1.7,.6,.30,'city foreground reveals persistent daylight'),('pencil_marks',3.4,.5,.29,'approximate delay stamp'),('soft_depth_pass',5.05,.65,.29,'city inspection before premise distinction'),('document_stamp',6.5,.5,.30,'impossible premise marked'),('doubt_tick',7.8,.45,.26,'real delay separated from impossible event'),('pencil_marks',9.2,.5,.28,'measurement is the real part'),('perspective_whip',10.5,.7,.30,'distance opens between Sun and Earth'),('pencil_marks',11.9,.7,.32,'travel ruler builds'),('hard_fact_punctuate',13.6,.5,.32,'eight minutes twenty seconds resolves'),('turn_of_story',26.4,.8,.32,'gravity twist'),('photo_slide',27.8,.6,.29,'Earth and old solar orbit selected'),('pencil_marks',29.5,.5,.29,'orbit continues after hypothetical source removal'),('doubt_tick',31.2,.45,.29,'gravitational change has not arrived'),('paper_light_turn',32.4,.6,.30,'shared propagation comparison'),('pencil_marks',34.1,.6,.29,'two change boundaries advance together'),('evidence_lock',35.8,.55,.31,'same causal speed resolves'),('micro_emphasis',37.3,.5,.34,'delayed change reaches orbit'),('parallax_swish',38.6,.6,.31,'Earth follows its tangent'),('pencil_marks',39.8,.5,.29,'radial-flight misconception crossed out'),('photo_slide',40.6,.65,.32,'return to original daylight photo'),('doubt_tick',42.3,.4,.27,'first warning is delayed'),('pencil_marks',44.1,.55,.28,'emission time revealed'),('quiet_resolution',46.15,1.8,.22,'Sun past payoff')]
sheet=[]
for name,at,dur,peak,event in cues:
 p=repo/cat[name]['path'];a=load(p)[:round(dur*sr)];a=sosfilt(butter(2,7000,fs=sr,output='sos'),a,axis=0);a*=peak/max(np.max(abs(a)),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);l=min(len(a),n-i);fx[i:i+l]+=a[:l];mu[max(0,i-960):min(n,i+l+1920)]*=.7
 sheet.append({'sound_id':name,'asset_file':str(p.relative_to(repo)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset_time':at,'duration':l/sr,'purpose':event,'animation_event_id':event,'mix_bus':'EDITORIAL/PHYSICAL','peak_target':peak,'rights':'Existing original synthesized Curio cue; not authentic NASA/space sound'})
# Carry the exact approved performance, score and effects stems into the representative passage.
start=round(14.55*sr);end=round(26.15*sr);pre=ep/'motion-preflight-v1/audio'
for target,name in [(vo,'voice'),(mu,'music'),(fx,'sfx')]:
 aa=load(pre/f'{name}.wav');l=min(len(aa),end-start);target[start:start+l]=aa[:l]
for c in json.loads((ep/'motion-preflight-v1/SFX_CUE_SHEET.json').read_text()):
 c=dict(c);c['onset_time']=round(c['onset_time']+14.55,4);c['inherited_owner_approved_passage']=True;sheet.append(c)
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:
 wavfile.write(r/'audio'/f'{name}.wav',sr,np.int16(np.clip(a,-1,1)*32767))
 if name!='raw':subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'audio'/f'{name}.wav'),'-c:a','flac','-compression_level','8',str(r/'audio'/f'{name}.flac')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'audio/mix.wav'),'-c:a','flac','-compression_level','8',str(r/'Sun-Full-Mix-v1.flac')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sorted(sheet,key=lambda x:x['onset_time']),indent=2)+'\n')
(r/'MUSIC_DIRECTION.json').write_text(json.dumps({'method':'Original deterministic score; approved passage stems inherited without time stretching','key':'E minor / suspended changes; brighter resolution','instruments':['glass plucks','restrained bass','evolving chamber triads','gravity-passage brush pulse'],'form':'strange opening, measurable journey, approved transit, lower gravity discovery, tangent release, warm return and brand resolution','independent_listening':'NOT CLAIMED; complete-film owner playback review pending'},indent=2)+'\n')
print(json.dumps({'duration':tl['duration'],'cues':len(sheet),'voice_samples_preserved':len(load(ep/'audio/voice-edit.wav')),'music_development_sections':5,'raw_clipped_samples':int(np.sum(np.abs(vo+mu+fx)>=1))}))
