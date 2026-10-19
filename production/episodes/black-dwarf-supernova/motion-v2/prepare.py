from pathlib import Path
import json,re,subprocess,hashlib,math
import numpy as np
from scipy.io import wavfile
r=Path(__file__).resolve().parent; ep=r.parent; sr=48000
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
source=load(ep/'audio/voice-original-v1.mp3')
log=(ep/'audio/SILENCE_V1.log').read_text(); starts=re.findall(r'silence_start: ([\d.]+)',log); ends=re.findall(r'silence_end: ([\d.]+)',log)
# Remove only central portions of measured discretionary long silence, preserving .25s at each edge.
cuts=[]
for a,b in zip(map(float,starts),map(float,ends)):
 if b-a>.85: cuts.append((a+.25,b-.25))
def mapped(t):return t-sum(max(0,min(t,b)-a) for a,b in cuts if t>a)
parts=[];cursor=0
for a,b in cuts:parts.append(source[cursor:round(a*sr)]);cursor=round(b*sr)
parts.append(source[cursor:]);edited=np.concatenate(parts)
wavfile.write(ep/'audio/voice-edit-v1.wav',sr,(np.clip(edited,-1,1)*32767).astype(np.int16))
words=json.loads((ep/'audio/TRANSCRIPT_ASR_V1.json').read_text())['words']
start,end=19.0,44.90; begin=mapped(start);stop=mapped(end)
voice=edited[round(begin*sr):round(stop*sr)];duration=math.ceil((len(voice)/sr+.8)*30)/30
n=round(duration*sr);vo=np.zeros((n,2),np.float32);vo[:len(voice)]=voice
vo*=.64/max(abs(vo).max(),.001)
pw=[dict(w,start=round(mapped(w['start'])-begin,4),end=round(mapped(w['end'])-begin,4)) for w in words if start<=w['start']<end]
# Script-correct phrases; boundaries remain actual-audio ASR estimates, openly labeled.
phrases=[('In a theoretical model,',19.42,20.82),('quantum tunneling allows',20.82,22.32),('extremely slow fusion,',22.32,24.4),('gradually making the core',24.58,26.18),('richer in iron.',26.18,27.15),('That changes how much mass',28.06,29.8),('the remnant can support.',29.8,31.10),('Its mass barely changes.',32.16,34.20),('Its limit falls.',34.90,35.95),('For some of the heaviest remnants,',36.86,38.50),('gravity could finally win:',38.94,40.90),('collapse,',41.48,42.25),('and a possible supernova.',42.64,44.35)]
caps=[{'text':s,'start':round(mapped(a)-begin,4),'end':round(mapped(b)-begin,4)}for s,a,b in phrases]
events=[(0,'Open the conceptual cutaway'),(1.6,'Establish electron support against inward gravity'),(3.2,'Select the lattice detail'),(4.8,'Begin conceptual composition replacement'),(6.4,'Advance the iron-rich selection'),(8.0,'Resolve the more-iron state'),(9.5,'Replace lattice detail with the mass/support comparison'),(11.0,'Establish support capacity above mass'),(12.75,'Lock and emphasize the nearly fixed mass reference'),(14.4,'Reveal the independent falling-limit keyword'),(15.5,'Lower the support limit without changing the mass reference'),(17.0,'Extend the source-attached downward comparison'),(18.5,'Restrict the consequence to some massive remnants'),(20.0,'Cross the support limit below the mass reference'),(21.5,'Return inward gravity marks to the same remnant'),(22.2,'Contract the same illustrative body'),(23.8,'Resolve possible collapse, not an exact transient prediction')]
tl={'production_standard':'sun-disappeared-v1','scene_fps':12,'width':1080,'height':1920,'fps':30,'visual_style':'image-led','material_profile':'image-led-v1','duration':duration,'frames':round(duration*30),'excerpt_source_seconds':[start,end],'excerpt_edited_start':begin,'voice_duration':len(voice)/sr,'captions':caps,'words':pw,'caption_status':'Actual-audio ASR estimates, script-correct phrases; independent word alignment pending','events':[{'time':t,'operation':s}for t,s in events],'ending':'isolated mechanism preflight; no brand ending or full-film claim','motion_review_targets':'MOTION_REVIEW_TARGETS.json'}
caps[-1]['end']=round(duration-.1,4)
(r/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n')
(r/'MOTION_REVIEW_TARGETS.json').write_text(json.dumps({'duration':duration,'events':[{'t':e['time'],'operation':e['operation'],'understanding':e['operation']}for e in tl['events']],'exceptions':[{'start':23.8,'end':duration,'reason':'Read possible-collapse qualification and retain the complete supernova word plus source tail.'}]},indent=2)+'\n')
mu=np.zeros((n,2),np.float32);fx=np.zeros_like(mu);rng=np.random.default_rng(191026)
def put(at,v,pan=0):
 i=round(at*sr);l=min(len(v),n-i)
 if i<0 or l<=0:return
 mu[i:i+l,0]+=v[:l]*math.sqrt((1-pan)/2);mu[i:i+l,1]+=v[:l]*math.sqrt((1+pan)/2)
def note(at,f,amp,length=1.4,pan=0):
 t=np.arange(round(length*sr))/sr
 v=(np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2.003*t)+.075*np.sin(2*np.pi*f*3*t))*np.minimum(t/.008,1)*np.exp(-t*3.8)*amp
 put(at,v,pan)
# New original three-part score: sparse suspended fifths, a narrowing interval, then low resolved release.
for k,at in enumerate(np.arange(.08,duration-.3,.625)):
 section=0 if at<9.5 else 1 if at<20 else 2
 melody=[[146.832,220,293.665,329.628],[164.814,174.614,246.942,220],[146.832,220,293.665,440]][section]
 note(float(at),melody[k%4],.052 if section<2 else .063,pan=(-.28 if k%2 else .28))
 if k%4==0:note(float(at),[73.416,82.407,73.416][section],.065,2.1)
for at,root in [(0,146.832),(5,164.814),(9.5,164.814),(14.5,174.614),(20.0,73.416),(23.8,146.832)]:
 u=np.arange(round(3*sr))/sr
 for j,ratio in enumerate([1,1.5,2]):put(at,np.sin(2*np.pi*root*ratio*u)*np.minimum(u/.25,1)*np.exp(-u/1.2)*.018,-.3+j*.3)
t=np.arange(n)/sr;mu*=np.minimum(t/.1,1)[:,None]*np.clip((duration-t)/.5,0,1)[:,None]
repo=ep.parents[2]
cues=[('audio/generated-editorial-v1/paper.mp3',.05,.65,.23,'Cutaway inspection'),('audio/curio_sfx_v1/editorial/CB_EDITORIAL_causal_reveal_v1.flac',1.6,.6,.23,'Electron-support relationship'),('audio/generated-editorial-v1/camera_move.mp3',3.2,.65,.22,'Selected lattice macro'),('audio/generated-editorial-v1/ink.mp3',4.8,.55,.25,'Composition replacement begins'),('audio/generated-editorial-v1/pencil.mp3',6.4,.55,.24,'Iron-rich region advances'),('audio/curio_sfx_v1/editorial/CB_EDITORIAL_evidence_lock_v1.flac',8.0,.5,.23,'Iron-rich state resolves'),('audio/generated-editorial-v1/paper.mp3',9.5,.7,.26,'Mass/support figure handoff'),('audio/generated-editorial-v1/marker_bold.mp3',11,.6,.25,'Support limit established'),('audio/curio_sfx_v1/editorial/CB_EDITORIAL_doubt_tick_v1.flac',12.75,.45,.25,'Mass reference locks'),('audio/generated-editorial-v1/ink.mp3',14.4,.5,.23,'Limit keyword reveals'),('audio/generated-editorial-v1/pencil.mp3',15.5,.65,.27,'Limit falls'),('audio/curio_sfx_v1/motion/CB_MOTION_tiny_mask_reveal_v1.flac',17,.5,.23,'Downward relation extends'),('audio/curio_sfx_v1/editorial/CB_EDITORIAL_causal_reveal_v1.flac',18.5,.6,.22,'Massive-remnant qualification'),('audio/curio_sfx_v1/cinematic/CB_CINEMATIC_micro_emphasis_v1.flac',20,.55,.28,'Support crossing'),('audio/curio_sfx_v1/motion/CB_MOTION_soft_depth_pass_v1.flac',21.5,.7,.23,'Return to remnant'),('audio/curio_sfx_v1/cinematic/CB_CINEMATIC_low_cinematic_hit_v1.flac',22.2,.9,.26,'Possible collapse'),('audio/curio_sfx_v1/editorial/CB_EDITORIAL_quiet_resolution_v1.flac',23.8,1.2,.21,'Qualified landing')]
sheet=[]
for file,at,dur,peak,event in cues:
 p=repo/file;a=load(p)[:round(dur*sr)];a*=peak/max(abs(a).max(),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);l=min(len(a),n-i);fx[i:i+l]+=a[:l];mu[max(0,i-960):min(n,i+l+1920)]*=.72
 sheet.append({'asset':file,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'onset':at,'duration':l/sr,'peak_target':peak,'event':event,'rights':'Existing original Curio synthesized design, not authentic space audio','listening':'OWNER REVIEW PENDING'})
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n')
(r/'audio').mkdir(exist_ok=True)
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,(np.clip(a,-1,1)*32767).astype(np.int16))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
(r/'AUDIO_RECEIPT.json').write_text(json.dumps({'source_task':'29a2145d-831b-4d82-8f79-5485a8895ae5','voice':'Bernard','voice_id':'QMJTqaMXmGnG8TCm8WQG','model':'eleven_v3','speed':1,'original_sha256':hashlib.sha256((ep/'audio/voice-original-v1.mp3').read_bytes()).hexdigest(),'source_samples':len(source),'edited_samples':len(edited),'removed_only_measured_silence':cuts,'source_excerpt':[start,end],'excerpt_voice_duration':len(voice)/sr,'movie_duration':duration,'cues':len(cues),'raw_clipped_samples':int(np.sum(abs(vo+mu+fx)>=1)),'caption_status':tl['caption_status'],'score':'Original deterministic score, three developing sections; no reused Sun music','human_listening':'PENDING'},indent=2)+'\n')
print(json.dumps({'duration':duration,'frames':tl['frames'],'cues':len(cues),'silence_cuts':cuts}))
