from pathlib import Path
import json,re,math,subprocess,numpy as np
from scipy.io import wavfile
P=Path(__file__).resolve().parent;ROOT=P.parents[3];SR=48000
words=json.loads((P/'audio/ASR_WORDS.json').read_text())['words']
original_words=[dict(w)for w in words]
cuts=[]
for a,b in zip(words,words[1:]):
 if b['start']-a['end']>.60:cuts.append([a['end']+.12,b['start']-.16])
def ripple(t):return t-sum(max(0,min(t,b)-a)for a,b in cuts if t>a)
for w in words:w['start']=ripple(w['start']);w['end']=ripple(w['end'])
(P/'audio/VOICE_EDITS.json').write_text(json.dumps({'cuts_original_seconds':cuts,'preserved_word_guards_seconds':[.12,.16],'speed':1,'reason':'Remove only discretionary inter-phrase quiet; no speech speed change or omitted words'},indent=2)+'\n')
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
plain=[norm(w['word'])for w in words]
def find(phrase,default=None):
 a=[norm(s)for s in phrase.split()]
 for k in range(len(plain)-len(a)+1):
  if plain[k:k+len(a)]==a:return words[k]['start']
 if default is not None:return default
 raise ValueError('ASR phrase not found: '+phrase)
# Real speech defines scene events; no fixed scene padding/time stretching.
bound=[0,find('your immune system'),find('look at the lining'),find('at the same time'),find('that can disrupt'),find('the infection matters'),find('sepsis is more complicated'),find('it is a medical emergency'),find('protection depends')]
voice=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(P/'audio/bernard-original.mp3'),'-f','f32le','-ar',str(SR),'-ac','2','-']),dtype=np.float32).reshape(-1,2).copy()
if cuts:
 parts=[];cursor=0
 for a,b in cuts:parts.append(voice[cursor:round(a*SR)]);cursor=round(b*SR)
 parts.append(voice[cursor:]);voice=np.concatenate(parts)
last=words[-1]['end'];ending=math.ceil((max(last+.50,len(voice)/SR)+.05)*30)/30;duration=ending+1.1;frames=round(duration*30)
caps=[];group=[]
for i,w in enumerate(words):
 group.append(w)
 if len(group)>=7 or re.search(r'[.?!,]$',w['word']) or i==len(words)-1:
  caps.append({'text':' '.join(x['word']for x in group),'start':group[0]['start'],'end':min(group[-1]['end']+.12,words[i+1]['start']-.025)if i+1<len(words)else last+.15});group=[]
tl={'duration':duration,'frames':frames,'ending_start':ending,'voice_duration':len(voice)/SR,'last_word_end':last,'scene_boundaries':bound+[ending],'scene_art':[0,1,2,3,4,1,5,5,5],'captions':caps,'words':words,'caption_status':'Actual decoded-audio ASR; script-reconciled spelling, independent word-boundary listening pending','scene_fps':12,'delivery_fps':30}
(P/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n')
# Original four-part cue-led score; perceptual listening remains separate.
n=round(duration*SR);v=np.zeros((n,2),np.float32);v[:len(voice)]=voice;v*=.68/max(.001,abs(v).max());music=np.zeros_like(v);fx=np.zeros_like(v)
def put(at,a,pan=0):
 i=round(at*SR);l=min(len(a),n-i)
 if l>0:music[i:i+l,0]+=a[:l]*math.sqrt((1-pan)/2);music[i:i+l,1]+=a[:l]*math.sqrt((1+pan)/2)
for k,at in enumerate(np.arange(.1,ending,.61)):
 sec=0 if at<bound[2]else 1 if at<bound[4]else 2 if at<bound[6]else 3
 notes=[[146.83,220,293.66,349.23],[146.83,174.61,220,261.63],[130.81,196,261.63,293.66],[146.83,220,293.66,440]][sec]
 hz=notes[k%4];t=np.arange(int(SR*1.6))/SR;z=(np.sin(2*np.pi*hz*t)+.22*np.sin(2*np.pi*hz*2.001*t))*np.minimum(t/.008,1)*np.exp(-t/.55)*.032
 put(float(at),z,-.3 if k%2 else .3)
 if k%4==0:put(float(at),np.sin(2*np.pi*notes[0]/2*t)*np.minimum(t/.12,1)*np.exp(-t/.9)*.03)
for at in [0,bound[2],bound[4],bound[6]]:
 t=np.arange(SR*4)/SR
 for j,hz in enumerate([73.416,110,146.83]):put(at,np.sin(2*np.pi*hz*t)*np.minimum(t/.35,1)*np.exp(-t/1.5)*.014,-.35+j*.35)
cuefiles=['editorial/CB_EDITORIAL_doubt_tick_v1.flac','archive/CB_ARCHIVE_photo_slide_v1.flac','editorial/CB_EDITORIAL_causal_reveal_v1.flac','editorial/CB_EDITORIAL_turn_of_story_v1.flac','editorial/CB_EDITORIAL_quiet_resolution_v1.flac']
events=[(0,0,'Protection question'),(.65,1,'Microscopy lens advances'),(bound[1],1,'Real cell record selected'),(bound[2],2,'Vessel lining selected'),(find('inflammatory signals'),0,'Leak mechanism begins'),(bound[3],3,'Clotting pathway'),(bound[4],2,'Perfusion consequence'),(bound[5],0,'Infection and host response distinguished'),(bound[6],1,'Immune complexity'),(bound[7],0,'Emergency context'),(bound[8],4,'Control takeaway')]
cues=[]
for at,k,meaning in events:
 f=ROOT/'audio/curio_sfx_v1'/cuefiles[k];z=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(f),'-f','f32le','-ar',str(SR),'-ac','2','-']),dtype=np.float32).reshape(-1,2).copy()[:int(SR*.9)]
 z*=.105/max(.001,abs(z).max());fade=min(600,len(z)//4);z[:fade]*=np.linspace(0,1,fade)[:,None];z[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*SR);l=min(len(z),n-i);fx[i:i+l]+=z[:l];music[max(0,i-1000):min(n,i+l+3000)]*=.65;cues.append({'t':at,'source':str(f.relative_to(ROOT)),'operation':meaning,'kind':'Original designed sound, not authentic biological recording'})
t=np.arange(n)/SR;music*=np.clip((duration-t)/1.1,0,1)[:,None];mix=v+music+fx
wavfile.write(P/'audio/voice.wav',SR,v);wavfile.write(P/'audio/premix.wav',SR,mix)
subprocess.run(['ffmpeg','-v','error','-y','-i',str(P/'audio/premix.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=7','-ar',str(SR),'-c:a','flac',str(P/'audio/soundtrack.flac')],check=True)
(P/'SFX_CUE_SHEET.json').write_text(json.dumps(cues,indent=2)+'\n')
# Declare real operations and explicitly qualified reading holds. This isn't artistic certification.
ops=[]
for i,b in enumerate(bound):
 ops.append({'t':b,'operation':['Independent hand/lens establishes question','Select real immune-cell record','Inspect lining boundary','Introduce local obstruction','Follow oxygen delivery consequence','Revisit actual source and response distinction','Separate inflammation/suppressed defenses','Present urgent-care context','Resolve protection question'][i],'understanding':'Next source-supported proposition; see scene contract'})
 if b+.7<(bound[i+1]if i+1<len(bound)else ending):ops.append({'t':b+.7,'operation':'Independent source plane settles; selected feature remains clear','understanding':'Read source/model relationship after arrival'})
 if i in [2,3,4] and b+2<(bound[i+1]if i+1<len(bound)else ending):ops.append({'t':b+2,'operation':['','','Lining gap and fluid tracers develop','Clot components accumulate','Reduced downstream delivery remains distinct'][i],'understanding':'Visible physical model state change'})
ops.sort(key=lambda x:x['t']);ex=[]
for a,b in zip([o['t']for o in ops],[o['t']for o in ops][1:]+[ending]):
 if b-a>2:ex.append({'start':a,'end':b,'reason':'Source/model reading and spoken qualification hold; blood-cell/tracer motion continues where relevant. No caption or grain counted as a new explanatory event.'})
(P/'MOTION_REVIEW_TARGETS.json').write_text(json.dumps({'duration':duration,'events':ops,'exceptions':ex},indent=2)+'\n')
print(json.dumps({'duration':duration,'boundaries':bound,'captions':len(caps),'last_word_end':last}))
