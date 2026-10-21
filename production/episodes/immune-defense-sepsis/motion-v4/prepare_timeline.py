from pathlib import Path
import json,re,math,subprocess,hashlib,numpy as np
from scipy.io import wavfile
P=Path(__file__).resolve().parent;ROOT=P.parents[3];SR=48000
voice_original=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(P/'audio/bernard-original.mp3'),'-f','f32le','-ar',str(SR),'-ac','2','-']),dtype=np.float32).reshape(-1,2).copy()
edit=json.loads((P/'audio/SAFE_QUIET_CUTS.json').read_text());cuts=edit['cuts'];parts=[];cursor=0;keeps=[]
for cut in cuts:
 a=round(cut['start']*SR);b=round(cut['end']*SR);z=voice_original[a:b]
 # This is a sample-level gate, not a guess based on ASR inter-word timestamps.
 assert abs(z).max()<10**(-55/20),('Cut enters nonquiet audio',cut)
 assert cut['start']-cut['actual_quiet'][0]>=.1999 and cut['actual_quiet'][1]-cut['end']>=.1999
 parts.append(voice_original[cursor:a]);keeps.append([cursor,a]);cursor=b
parts.append(voice_original[cursor:]);keeps.append([cursor,len(voice_original)]);voice=np.concatenate(parts);unscaled=voice.copy();offset=0
for a,b in keeps:
 assert np.array_equal(unscaled[offset:offset+b-a],voice_original[a:b]);offset+=b-a
assert offset==len(unscaled)
wavfile.write(P/'audio/bernard-restored-float.wav',SR,unscaled)
(P/'audio/VOICE_EDITS.json').write_text(json.dumps({'method':edit['method'],'cuts':cuts,'speed':1,'pitch_change':False,'all_removed_samples_below_stereo_peak_dbfs':-55,'quiet_guard_each_side_seconds':.2,'all_retained_samples':'BIT_IDENTICAL before gain/mixing','source_decoded_pcm_sha256':hashlib.sha256(voice_original.tobytes()).hexdigest(),'retained_decoded_pcm_sha256':hashlib.sha256(unscaled.tobytes()).hexdigest(),'voice_duration':len(unscaled)/SR,'ASR_timestamps_used_to_cut_audio':False},indent=2)+'\n')
alignment=json.loads((P/'audio/UTTERANCE_ALIGNMENT.json').read_text());reference=json.loads((P/'audio/ORIGINAL_REFERENCE_WORDS.json').read_text())['words']
def norm(s):return re.sub(r'[^a-z0-9]','',s.lower())
words=[dict(w)for u in alignment['units']for w in u['words']];assert [norm(w['word'])for w in words]==[norm(w['word'])for w in reference]
for w,c in zip(words,reference):w['word']=c['word']
# Anchor complete phrase boundaries to measured acoustic spans, not unreliable zero-duration word alignments.
caps=[];pos=0
for u in alignment['units']:
 count=len(u['words']);ww=words[pos:pos+count];pos+=count;a,b=u['repaired_nonquiet_span'];ww[0]['start']=max(0,a-.04);ww[-1]['end']=max(ww[-1]['end'],b)
 for j,w in enumerate(ww):
  w['start']=max(a-.04,min(b,w['start']));w['end']=max(w['start'],min(b,w['end']))
 groups=[ww[j:j+7]for j in range(0,len(ww),7)]
 for j,g in enumerate(groups):caps.append({'text':' '.join(w['word']for w in g),'start':g[0]['start'],'end':groups[j+1][0]['start']if j+1<len(groups)else b+.10,'timing':'Acoustic utterance anchor; internal ASR estimates'})
plain=[norm(w['word'])for w in words]
def find(phrase,default=None):
 a=[norm(s)for s in phrase.split()]
 for k in range(len(plain)-len(a)+1):
  if plain[k:k+len(a)]==a:return words[k]['start']
 if default is not None:return default
 raise ValueError('ASR phrase not found: '+phrase)
bound=[0,find('your immune system'),find('look at the lining'),find('at the same time'),find('that can disrupt'),find('the infection matters'),find('sepsis is more complicated'),find('it is a medical emergency'),find('protection depends')]
last=words[-1]['end'];ending=math.ceil((max(last,len(voice)/SR)+.50)*30)/30;duration=ending+1.1;frames=round(duration*30)
for a,b in zip(caps,caps[1:]):a['end']=min(a['end'],b['start'])
tl={'duration':duration,'frames':frames,'ending_start':ending,'voice_duration':len(voice)/SR,'last_word_end':last,'scene_boundaries':bound+[ending],'scene_art':[0,1,2,3,4,1,5,5,5],'captions':caps,'words':words,'caption_status':'Source-script reconciled116words; measured complete acoustic phrase anchors with internal ASR estimates. Independent exact word-boundary listening pending.','scene_fps':12,'delivery_fps':30}
(P/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n');(P/'audio/ASR_WORDS.json').write_text(json.dumps({'status':tl['caption_status'],'words':words},indent=2)+'\n')
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
 if i<7 and b+.7<(bound[i+1]if i+1<len(bound)else ending):ops.append({'t':b+.7,'operation':'Independent source plane settles; selected feature remains clear','understanding':'Read source/model relationship after arrival'})
 if i in [2,3,4] and b+2<(bound[i+1]if i+1<len(bound)else ending):ops.append({'t':b+2,'operation':['','','Lining gap and fluid tracers develop','Clot components accumulate','Reduced downstream delivery remains distinct'][i],'understanding':'Visible physical model state change'})

for o in ops:
 if o['t']in bound[7:]:o.update(operation='Narration/caption context changes; closing artwork holds without a new entrance',understanding='Not counted as new object animation')
ops.sort(key=lambda x:x['t']);ex=[]
for a,b in zip([o['t']for o in ops],[o['t']for o in ops][1:]+[ending]):
 if b-a>2:ex.append({'start':a,'end':b,'reason':'Source/model reading and spoken qualification hold; blood-cell/tracer motion continues where relevant. No caption or grain counted as a new explanatory event.'})
(P/'MOTION_REVIEW_TARGETS.json').write_text(json.dumps({'duration':duration,'events':ops,'exceptions':ex},indent=2)+'\n')
print(json.dumps({'duration':duration,'boundaries':bound,'captions':len(caps),'last_word_end':last}))
