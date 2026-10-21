from pathlib import Path
import json,subprocess,re,math,hashlib,os
import numpy as np
from scipy.io import wavfile
P=Path(__file__).resolve().parent;ROOT=Path(os.getenv('CURIO_REPO_ROOT',str(P.parents[3])));SR=48000
# Keep natural speech samples; edit the unsupported qualification and only proven inter-word silence.
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-ar',str(SR),'-ac','2','-f','f32le','-']),np.float32).reshape(-1,2).copy()
a=load(P/'audio/bernard-original.mp3');raw=json.loads((P/'audio/ASR_ORIGINAL.json').read_text());words=raw['words']
cuts=[(35.37,39.11),(52.7059,52.79)]
log=(P/'audio/SILENCE_ORIGINAL.log').read_text();starts=list(map(float,re.findall('silence_start: ([0-9.]+)',log)));ends=list(map(float,re.findall('silence_end: ([0-9.]+)',log)))
for st,en in zip(starts,ends):
 if en-st<.85 or(st<39.11 and en>35.37):continue
 x,y=st+.25,en-.25
 if not any(w['start']-.08<y and w['end']+.08>x for w in words):cuts.append((x,y))
cuts.sort()
def mapped(t):return t-sum(max(0,min(t,y)-x)for x,y in cuts if t>x)
parts=[];cur=0
for x,y in cuts:parts.append(a[cur:round(x*SR)]);cur=round(y*SR)
parts.append(a[cur:]);v=np.concatenate(parts);voice_duration=len(v)/SR;duration=math.ceil((voice_duration+.9+1.1)*30)/30;ending=duration-1.1
wavfile.write(P/'audio/voice-edited.wav',SR,(np.clip(v,-1,1)*32767).astype(np.int16))
ww=[]
for w in words:
 if any(x<=w['start']<y for x,y in cuts):continue
 z=dict(w,start=round(mapped(w['start']),4),end=round(mapped(w['end']),4));z['word']=z['word'].replace('IMIS','Imus')
 if z['word']=='analysis,':z['word']='analysis.'
 ww.append(z)
# Script reconciliation is explicit; timestamps remain actual-audio ASR estimates.
caps=[];group=[]
for w in ww:
 group.append(w)
 text=' '.join(x['word']for x in group)
 if len(text)>36 or len(group)>=6 or text.endswith(('.', '?','!')):
  caps.append({'text':text,'start':group[0]['start'],'end':group[-1]['end']+.1});group=[]
if group:caps.append({'text':' '.join(x['word']for x in group),'start':group[0]['start'],'end':group[-1]['end']+.1})
for c,nxt in zip(caps,caps[1:]):c['end']=min(c['end'],nxt['start']-.025)
caps[-1]['end']=min(ending,voice_duration+.65)
# Scene boundaries follow decoded speech, not fixed-duration guesses.
bound=[0,mapped(7.64),mapped(13.28),mapped(22.7),mapped(26.92),mapped(39.16),mapped(49.8),mapped(52.88),mapped(61.12),ending]
TL={'production_standard':'sun-disappeared-v1','scene_fps':12,'delivery_fps':30,'width':1080,'height':1920,'duration':duration,'frames':round(duration*30),'voice_duration':voice_duration,'ending_start':ending,'scene_boundaries':bound,'captions':caps,'words':ww,'voice_edits_seconds_original':cuts,'caption_status':'Script-reconciled actual-audio ASR estimates; independent word-boundary listening pending','owner_direction':'Use real records then render; no generated flood scenery','sources':{'footage_date':'2025-02-16','map_publication':'2025-03-11','analysis_publication':'2025-03-12','jica_study':'2023-08 through 2024-11'}}
(P/'timeline.json').write_text(json.dumps(TL,indent=2)+'\n')
n=round(duration*SR);voice=np.zeros((n,2),np.float32);voice[:len(v)]=v;voice*=.67/max(abs(voice).max(),.001);music=np.zeros_like(voice);fx=np.zeros_like(voice)
def put(at,arr,pan=0):
 i=round(at*SR);l=min(len(arr),n-i)
 if l>0:music[i:i+l,0]+=arr[:l]*math.sqrt((1-pan)/2);music[i:i+l,1]+=arr[:l]*math.sqrt((1+pan)/2)
def note(at,hz,amp,length=1.4,pan=0):
 t=np.arange(round(length*SR))/SR;arr=(np.sin(2*np.pi*hz*t)+.18*np.sin(2*np.pi*hz*2.001*t))*np.minimum(t/.012,1)*np.exp(-t/0.48)*amp;put(at,arr,pan)
for k,at in enumerate(np.arange(.12,duration-.5,.625)):
 section=0 if at<bound[2] else 1 if at<bound[5] else 2 if at<bound[7] else 3
 notes=[[146.832,220,293.665,329.628],[146.832,174.614,220,261.626],[164.814,220,246.942,293.665],[146.832,220,293.665,440]][section]
 note(float(at),notes[k%4],.035,pan=(-.32 if k%2 else .32))
 if k%4==0:note(float(at),notes[0]/2,.045,2.0)
for at in [0,bound[2],bound[5],bound[7]]:
 t=np.arange(round(4*SR))/SR
 for j,hz in enumerate([73.416,110,146.832]):put(at,np.sin(2*np.pi*hz*t)*np.minimum(t/.3,1)*np.exp(-t/1.5)*.018,-.35+j*.35)
cuefiles=['editorial/CB_EDITORIAL_doubt_tick_v1.flac','archive/CB_ARCHIVE_paper_light_turn_v1.flac','editorial/CB_EDITORIAL_evidence_lock_v1.flac','editorial/CB_EDITORIAL_causal_reveal_v1.flac','editorial/CB_EDITORIAL_quiet_resolution_v1.flac']
events=[(0,0,'Opening question'),(bound[2],1,'Published map enters'),(mapped(15.88),2,'With-project color identified'),(mapped(19.52),3,'Counterfactual color identified'),(bound[3],0,'Model-estimate qualification'),(bound[4],2,'Attributed estimate'),(bound[5],1,'Distinct Philippine record'),(mapped(45.24),0,'Measurement gap'),(bound[6],3,'Missing is not zero'),(bound[7],1,'Request event evidence'),(bound[8],4,'Closing question')]
cue=[]
for at,index,operation in events:
 file=ROOT/'audio/curio_sfx_v1'/cuefiles[index];z=load(file)[:round(.75*SR)];z*=.13/max(abs(z).max(),.001);fade=min(480,len(z)//3);z[:fade]*=np.linspace(0,1,fade)[:,None];z[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*SR);l=min(len(z),n-i);fx[i:i+l]+=z[:l];music[max(0,i-1200):min(n,i+l+2400)]*=.65;cue.append({'time':at,'source':str(file.relative_to(ROOT)),'operation':operation,'kind':'designed editorial cue, not authentic field sound'})
# Preserve all voice samples; only music/effects receive a closing fade.
t=np.arange(n)/SR;music*=np.clip((duration-t)/1.1,0,1)[:,None];premix=voice+music+fx;wavfile.write(P/'audio/premix.wav',SR,(np.clip(premix,-1,1)*32767).astype(np.int16))
(P/'SFX_CUE_SHEET.json').write_text(json.dumps(cue,indent=2)+'\n')
(P/'audio/AUDIO_RECEIPT.json').write_text(json.dumps({'voice':'Bernard','voice_id':'QMJTqaMXmGnG8TCm8WQG','speed':1,'source_sha256':hashlib.sha256((P/'audio/bernard-original.mp3').read_bytes()).hexdigest(),'source_samples':len(a),'retained_samples':len(v),'edits':cuts,'voice_duration':voice_duration,'duration':duration,'tail_before_ending':ending-voice_duration,'peak_before_normalization':float(abs(premix).max()),'score':'Original deterministic four-section score, no reused Sun soundtrack','independent_listening':'PENDING','caption_alignment':'ASR estimates, script reconciled; independent boundary verification PENDING'},indent=2)+'\n')
print(json.dumps({'duration':duration,'boundaries':bound,'cuts':cuts,'captions':len(caps)}))
