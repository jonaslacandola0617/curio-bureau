from pathlib import Path
import json,subprocess,hashlib,re,math
r=Path(__file__).parent
raw=json.loads((r/'TRANSCRIPT_ORIGINAL.json').read_text());words=[w.copy()for w in raw['words']if re.search('[A-Za-z]',w['text'])]
# Interior silence only; no word, sample rate or speaking-speed edits.
edits=[{'start':5.05,'end':5.62,'basis':'inside measured4.82220–5.89828 silence; outside ASR word bounds'},{'start':10.42,'end':10.66,'basis':'inside measured10.2025–10.9501 silence; outside word bounds'},{'start':27.25,'end':27.40,'basis':'inside measured27.0998–28.0232 silence; ends before uncertain So timestamp27.54'}]
for e in edits:
 assert all(e['end']<=w['start']or e['start']>=w['end']for w in words)
def tr(t):return round(t-sum(max(0,min(t,e['end'])-e['start'])for e in edits),6)
for w in words:w['original_start']=w['start'];w['original_end']=w['end'];w['start']=tr(w['start']);w['end']=tr(w['end'])
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_format','-of','json',str(r/'audio/voice-original.mp3')]))
# Decoded length is authoritative, not container padding.
a=subprocess.check_output(['ffmpeg','-v','error','-i',str(r/'audio/voice-original.mp3'),'-ar','48000','-ac','2','-f','f32le','-']);origlen=len(a)/8/48000
vo_end=tr(origlen);duration=math.ceil((vo_end+.8+1.1)*30)/30
starts=[0]+[max(0,words[i]['start']-.10)for i in [12,24,33,43,50,61]]
scenes=[{'id':f'S{i+1:02}','start':starts[i],'end':starts[i+1]if i<6 else duration,'operation':['connect','reveal damaged tissue','select LFS conversion','produce LF','transfer through air','locate irritation','resolve'][i]}for i in range(7)]
# Caption phrases use recognized word events; never character-proportional timing.
caps=[];group=[]
for i,w in enumerate(words):
 group.append(w)
 nextw=words[i+1]if i+1<len(words)else None
 stop=(len(group)>=6 or re.search('[.!?,]$',w['text']) or (nextw and nextw['start']-w['end']>.4))
 if stop or nextw is None:
  caps.append({'start':group[0]['start'],'end':min((nextw['start']-.025)if nextw else vo_end+.45,max(w['end']+.12,group[0]['start']+.3)),'text':' '.join(x['text']for x in group),'word_start':i-len(group)+1,'word_end':i});group=[]
# Specific spellings checked against the intended science script; transcript already matches.
expected="Cut here Tear up here How does an onion reach your eyes The knife damages the onion’s tissue starting a chain of chemical reactions One step uses an enzyme called lachrymatory factor synthase It helps make a volatile compound called the lachrymatory factor Volatile means it can enter the air That compound causes the familiar eye irritation associated with chopping onions So the slice and the irritation happen in different places connected by an airborne chemical The knife never touched your eye It started a reaction that could reach it"
norm=lambda x:re.findall('[a-z]+',x.lower().replace('’',"'"))
assert norm(expected)==norm(' '.join(w['text']for w in words)), 'Script reconciliation failed'
tl={'width':1080,'height':1920,'fps':30,'frames':round(duration*30),'duration':duration,'voice_original_duration':origlen,'voice_edited_duration':vo_end,'voice_silence_edits':edits,'scenes':scenes,'captions':caps,'words':words,'ending_start':duration-1.1,'protected_tail':duration-1.1-vo_end,'word_alignment':'Local faster-whisper/base.en actual audio transcription; ASR boundaries, not a human forced-alignment certification','events':{'cut':.12,'eye_question':words[2]['start'],'tissue':starts[1],'lfs':words[30]['start'],'lf':words[41]['start'],'air':starts[4],'eye':starts[5],'resolve':starts[6]}}
(r/'timeline.json').write_text(json.dumps(tl,indent=2)+'\n')
(r/'NARRATION_SOURCE.json').write_text(json.dumps({'provider':'Runway','voice':'Bernard','voice_id':'QMJTqaMXmGnG8TCm8WQG','task_id':'03ae4496-d54e-44ee-9c6a-a8c746dfc5ad','model':'eleven_v3','original':'audio/voice-original.mp3','sha256':hashlib.sha256((r/'audio/voice-original.mp3').read_bytes()).hexdigest(),'decoded_duration':origlen,'edited_duration':vo_end,'speed':1,'time_stretch':False,'silence_edits':edits,'transcription':'local inference only; external ElevenLabs transfer was blocked and not performed','script_reconciliation':'90 lexical words match intended script; punctuation-only tail hallucination excluded'} ,indent=2)+'\n')
(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'final_phrase':'It started a reaction that could reach it.','final_word':'it','final_word_asr_end':words[-1]['end'],'complete_decoded_narration_end':vo_end,'endcard_start':duration-1.1,'protected_tail':tl['protected_tail'],'complete_original_retained':True,'last_audio_samples_retained':True,'voice_fade':False,'encoded_tail_listening':'PENDING actual output','asr_reconciliation':'PASS, independent listening still required'},indent=2)+'\n')
def stamp(t):
 n=round(t*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
(r/'captions.srt').write_text('\n'.join(f'{i+1}\n{stamp(c["start"])} --> {stamp(c["end"])}\n{c["text"]}\n'for i,c in enumerate(caps)))
print(json.dumps({'duration':duration,'frames':tl['frames'],'scenes':scenes,'word_count':len(words),'protected_tail':tl['protected_tail']}))
