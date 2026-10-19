from pathlib import Path
import json,re,subprocess,hashlib,math
import numpy as np
from scipy.io import wavfile
r=Path(__file__).resolve().parent;ep=r.parent;repo=r.parents[3];sr=48000
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']),np.float32).reshape(-1,2).copy()
original=load(ep/'audio/voice-original-v1.mp3');log=(ep/'audio/SILENCE_V1.log').read_text();cuts=[(a+.25,b-.25)for a,b in zip(map(float,re.findall(r'silence_start: ([\d.]+)',log)),map(float,re.findall(r'silence_end: ([\d.]+)',log)))if b-a>.85]
def mapped(t):return t-sum(max(0,min(t,b)-a)for a,b in cuts if t>a)
parts=[];cursor=0
for a,b in cuts:parts.append(original[cursor:round(a*sr)]);cursor=round(b*sr)
parts.append(original[cursor:]);edited=np.concatenate(parts);duration=math.ceil((len(edited)/sr+.85+1.1)*30)/30;ending=duration-1.1;n=round(duration*sr)
vo=np.zeros((n,2),np.float32);vo[:len(edited)]=edited;vo*=.64/max(abs(vo).max(),.001)
# Read actual-audio phrases from approved mechanism, extend around the complete retained source.
caps=[{'text':x,'start':a,'end':b}for x,a,b in [('This star could explode',0,1.18),('long after it has stopped shining.',1.18,3.35),('The trigger is not a growing mass.',4.08,6.2),('It is a falling limit.',6.2,8.12),("It’s a black dwarf:",8.78,10.25),('the cold remnant a white dwarf',10.25,12.16),('could become in the far future.',12.16,14.38),('Inside, pressure from electrons',15.18,17.1),('resists gravity.',17.1,18.5)]]
mid=json.loads((ep/'motion-v2/timeline.json').read_text())
caps += [dict(c,start=19+c['start'],end=min(44.1666666667,19+c['end']))for c in mid['captions']]
caps += [{'text':x,'start':mapped(a),'end':mapped(b)}for x,a,b in [('The earliest might wait',45.06,46.48),('ten to the power of',46.48,47.84),('eleven hundred years.',47.84,49.12),("But only if protons",49.76,51.26),("don’t decay first.",51.26,52.5),('A dead star,',53.44,54.22),('with one more possible ending.',54.22,56.8)]]
caps[-1]['end']=ending
before=[(0,'Isolate the cold illustrative remnant','Dead-looking does not establish a finished fate.'),(1.6,'Introduce inward force marks on the body','An apparently inert remnant can change.'),(3.2,'Pull back the same body and reveal unfinished keyword','The question concerns a future outcome.'),(4.8,'Attach nearly-fixed mass register to the body','Large mass growth is not the trigger.'),(6.4,'Reveal a separately descending support marker','A falling support limit can trigger failure.'),(8,'Bring in the native Sirius evidence plate','White dwarfs are observed; black dwarfs are hypothetical.'),(9.6,'Circle the actual faint Sirius B point','Identify the remnant, not the bright companion.'),(11.2,'Draw the source-attached identity leader','The observation establishes a stellar-remnant class.'),(12.8,'Register the hypothetical future illustration below','Observation and extrapolation are distinct.'),(14.5,'Select the interior of the same illustrative remnant','The next question is its internal support.'),(16,'Extend outward pressure against inward gravity','Electron pressure resists gravity.'),(17.6,'Register the printed composition-detail window','Internal composition is the next changing variable.')]
events=[{'t':t,'operation':op,'understanding':u}for t,op,u in before]
events += [{'t':19+e['t'],'operation':e['operation'],'understanding':e['understanding']}for e in json.loads((ep/'motion-v2/MOTION_REVIEW_TARGETS.json').read_text())['events']]
after=[(44.1666666667,'Return same remnant beneath the timescale field','This is a far-future conditional model.'),(45.8,'Establish base ten as a physical printed notation','Time is expressed with an exponent.'),(47.4,'Complete the 1100 exponent and years qualification','Earliest model estimate is roughly ten to the eleven hundred years.'),(49,'Reveal proton-stability condition','The scenario requires protons to survive.'),(50.6,'Underline conditional requirement','Proton decay could prevent this path.'),(52.2,'Reconnect the condition to the same remnant','This remains one possible fate of a dead star.'),(53.8,'Close inward marks on the illustrated body','The opening question has a conditional ending.'),(55.4,'Resolve the possible-ending keyword on the same body','Possible, not a confirmed future event.')]
events += [{'t':t,'operation':op,'understanding':u}for t,op,u in after]
tl={'duration':duration,'frames':round(duration*30),'ending_start':ending,'scene_fps':12,'fps':30,'width':1080,'height':1920,'mechanism_start':19,'mechanism_end':44.1666666667,'voice_duration':len(edited)/sr,'captions':caps,'events':events,'caption_status':'Local actual-audio ASR estimates; script-correct phrases; independent forced alignment pending'}
(r/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n');(r/'MOTION_REVIEW_TARGETS.json').write_text(json.dumps({'duration':duration,'events':events,'exceptions':[]},indent=2)+'\n')
# Five-section original score, preserving the approved mechanism's harmonic sequence at its absolute placement.
mu=np.zeros((n,2),np.float32);fx=np.zeros_like(mu)
def put(at,v,pan=0):
 i=round(at*sr);a=max(0,-i);i=max(0,i);l=min(len(v)-a,n-i)
 if l>0:mu[i:i+l,0]+=v[a:a+l]*math.sqrt((1-pan)/2);mu[i:i+l,1]+=v[a:a+l]*math.sqrt((1+pan)/2)
def note(at,f,amp,length=1.4,pan=0):
 t=np.arange(round(length*sr))/sr;v=(np.sin(2*np.pi*f*t)+.22*np.sin(2*np.pi*f*2.003*t)+.075*np.sin(2*np.pi*f*3*t))*np.minimum(t/.008,1)*np.exp(-t*3.8)*amp;put(at,v,pan)
for k,at in enumerate(np.arange(.08,ending,.625)):
 section=0 if at<8 else 1 if at<19 else 2 if at<28.5 else 3 if at<39 else 4
 melody=[[146.832,220,293.665,329.628],[164.814,220,329.628,293.665],[146.832,220,293.665,329.628],[164.814,174.614,246.942,220],[146.832,220,293.665,440]][section]
 note(float(at),melody[k%4],.052 if section<4 else .06,pan=(-.28 if k%2 else .28))
 if k%4==0:note(float(at),[73.416,82.407,73.416,82.407,73.416][section],.06,2.1)
for at,f in [(0,146.832),(8,164.814),(19,146.832),(28.5,164.814),(34.5,174.614),(39,73.416),(44.1667,146.832),(49,164.814),(53.8,146.832)]:
 t=np.arange(3*sr)/sr
 for j,ratio in enumerate([1,1.5,2]):put(at,np.sin(2*np.pi*f*ratio*t)*np.minimum(t/.25,1)*np.exp(-t/1.2)*.018,-.3+j*.3)
# Reuse every approved mechanism cue at its actual full-film timestamp; add physical opening/evidence/closing cues.
cues=[dict(c,onset=c['onset']+19)for c in json.loads((ep/'motion-v2/SFX_CUE_SHEET.json').read_text())]
choices=['camera_move','ink','camera_move','marker_bold','pencil','paper','marker_bold','pencil','paper','camera_move','pencil','paper']
for e,name in zip(events[:12],choices):cues.append({'asset':'audio/generated-editorial-v1/'+name+'.mp3','onset':e['t'],'duration':.6,'peak_target':.23,'event':e['operation']})
for e,name in zip(events[-8:],['camera_move','marker_bold','pencil','paper','ink','camera_move','paper','marker_bold']):cues.append({'asset':'audio/generated-editorial-v1/'+name+'.mp3','onset':e['t'],'duration':.65,'peak_target':.22,'event':e['operation']})
for c in cues:
 p=repo/c['asset'];a=load(p)[:round(c['duration']*sr)];a*=c['peak_target']/max(abs(a).max(),.001);fade=min(480,len(a)//3);a[:fade]*=np.linspace(0,1,fade)[:,None];a[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(c['onset']*sr);l=min(len(a),n-i);fx[i:i+l]+=a[:l];mu[max(0,i-960):min(n,i+l+1920)]*=.72;c['sha256']=h(p);c['rights']='Existing original Curio synthesized editorial sound; not authentic space audio';c['listening']='Owner full-film review pending'
t=np.arange(n)/sr;mu*=np.minimum(t/.1,1)[:,None]*np.clip((duration-t)/1,0,1)[:,None]
(r/'audio').mkdir(exist_ok=True)
for name,a in [('voice',vo),('music',mu),('sfx',fx),('raw',vo+mu+fx)]:wavfile.write(r/'audio'/f'{name}.wav',sr,(np.clip(a,-1,1)*32767).astype(np.int16))
subprocess.run(['ffmpeg','-v','error','-y','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8','-ar','48000','-ac','2',str(r/'audio/mix.wav')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sorted(cues,key=lambda c:c['onset']),indent=2)+'\n')
(r/'AUDIO_RECEIPT.json').write_text(json.dumps({'voice':'Bernard','voice_id':'QMJTqaMXmGnG8TCm8WQG','speed':1,'source_sha256':h(ep/'audio/voice-original-v1.mp3'),'original_samples':len(original),'edited_samples':len(edited),'measured_silence_cuts':cuts,'cues':len(cues),'score_sections':5,'raw_clipped_samples':int(np.sum(abs(vo+mu+fx)>=1)),'mix_sha256':h(r/'audio/mix.wav'),'human_listening':'PENDING'},indent=2)+'\n')
(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'original_sha256':h(ep/'audio/voice-original-v1.mp3'),'decoded_original_duration':len(original)/sr,'retained_edited_duration':len(edited)/sr,'final_word':'ending','final_word_end_asr_estimate':mapped(56.8),'caption_end':ending,'endcard_start':ending,'movie_duration':duration,'protected_tail_after_all_retained_source':ending-len(edited)/sr,'voice_fade':False,'listening':'PENDING; measurements do not certify pronunciation/tail audibility'},indent=2)+'\n')
def stamp(x):
 ms=round(x*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(r/'captions.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}'for i,c in enumerate(caps))+'\n')
print(json.dumps({'duration':duration,'frames':tl['frames'],'tail':ending-len(edited)/sr,'cues':len(cues)}))
