from pathlib import Path
import json,re,math,subprocess,hashlib
r=Path(__file__).parent
raw=json.loads((r/'TRANSCRIPT_ORIGINAL.json').read_text());words=raw['words']
script=(r.parent/'NARRATION.md').read_text().split('\n\n',1)[1].split('\n\nDirection:')[0].strip()
norm=lambda s:re.findall('[a-z]+',s.lower().replace('’',"'"))
assert norm(script)==norm(' '.join(w['text'] for w in words)), 'Actual narration differs from script'
edits=[{'start':12.80,'end':13.20,'basis':'Inside measured12.5666–13.6345 quiet interval, outside ASR spoken words; remove400ms of silence only'}]
for e in edits:assert all(e['end']<=w['start'] or e['start']>=w['end'] for w in words)
def tr(t):return round(t-sum(max(0,min(t,e['end'])-e['start']) for e in edits),6)
for w in words:w['original_start']=w['start'];w['original_end']=w['end'];w['start']=tr(w['start']);w['end']=tr(w['end'])
a=subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'audio/voice-original.mp3'),'-ar','48000','-ac','2','-f','f32le','-']);original=len(a)/8/48000;vo=tr(original);duration=math.ceil((vo+1.9)*30)/30
def find(phrase,start=0):
 target=norm(phrase)
 for i in range(start,len(words)):
  if norm(' '.join(w['text'] for w in words[i:i+len(phrase.split())]))==target:return i
 raise ValueError(phrase)
ids=[0,find('You checked it'),find('That experience'),find('One proposed'),find('Pressure from'),find('But researchers'),find('So a convincing')]
starts=[0]+[max(0,words[i]['start']-.10) for i in ids[1:]]
scenes=[{'id':f'S{i+1:02}','start':v,'end':starts[i+1] if i<6 else duration,'source_state':['hook','check','name','candidate','interpretation','evidence','payoff'][i]} for i,v in enumerate(starts)]
caps=[];g=[]
for i,w in enumerate(words):
 g.append(w);nx=words[i+1] if i+1<len(words) else None
 if len(g)>=6 or re.search('[.!?,]$',w['text']) or nx is None:
  caps.append({'start':g[0]['start'],'end':min(nx['start']-.025 if nx else vo+.45,max(w['end']+.13,g[0]['start']+.3)),'text':' '.join(z['text'] for z in g),'word_start':i-len(g)+1,'word_end':i});g=[]
events={key:words[find(phrase)]['start'] for key,phrase in [('felt','felt your'),('nothing','Nothing'),('question','So what'),('expect',"When you're"),('interpret','your brain'),('buzz','as the familiar'),('pressure','Pressure from'),('muscle','small muscle'),('survey','Surveys document'),('not_proven',"They don't prove"),('final','The sensation')]}
tl={'width':1080,'height':1920,'fps':30,'frames':round(duration*30),'duration':duration,'voice_original_duration':original,'voice_edited_duration':vo,'voice_silence_edits':edits,'scenes':scenes,'captions':caps,'words':words,'events':events,'ending_start':duration-1.1,'protected_tail':duration-1.1-vo,'word_alignment':raw['method']}
(r/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n')
(r/'NARRATION_SOURCE.json').write_text(json.dumps({'provider':'Runway','voice':'Bernard','voice_id':'QMJTqaMXmGnG8TCm8WQG','task_id':'afc524ea-9219-4ce2-b68b-4af2fd38de8c','model':'eleven_v3','speed':1,'time_stretch':False,'original':'audio/voice-original.mp3','sha256':hashlib.sha256((r/'audio/voice-original.mp3').read_bytes()).hexdigest(),'decoded_duration':original,'edited_duration':vo,'silence_edits':edits,'script_reconciliation':'All lexical words match including complete closing clause','external_transcription':False},indent=2)+'\n')
(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'final_word':"wasn't",'final_phrase':"The sensation can feel real even when the alert wasn't.",'asr_final_word_end':words[-1]['end'],'complete_decoded_voice_end':vo,'endcard_start':duration-1.1,'protected_tail':tl['protected_tail'],'untouched_original_preserved':True,'voice_fade':False,'encoded_tail_listening':'PENDING owner full-review audition'},indent=2)+'\n')
def stamp(t):
 n=round(t*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
(r/'captions.srt').write_text('\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}\n' for i,c in enumerate(caps)))
print(json.dumps({'duration':duration,'frames':tl['frames'],'scenes':scenes,'events':events,'protected_tail':tl['protected_tail']}))
