from pathlib import Path
import sys,json,numpy as np
root=Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'engine'));import audio as shared
a=root/'project/assets';timing=json.loads((a/'timing.json').read_text());duration=timing['duration'];n=round(duration*48000)
voice=shared.load(a/'voice_full.wav');voice*=.60/max(.001,float(np.max(np.abs(voice))))
music=shared.load(a/'music_full.wav')[:n].copy();music*=.043/max(.001,float(np.sqrt(np.mean(music**2))))
if len(music)<n:music=np.pad(music,((0,n-len(music)),(0,0)))
music[-52800:]*=np.linspace(1,0,52800)[:,None];music[round(29.2*48000):]*=.62
fx=np.zeros_like(voice);spec=[('013',.04,.20,'record click'),('041',.48,.80,'close approach'),('001',2.98,.8,'photo handoff'),('002',3.55,.40,'skull photo arrival'),('023',3.95,.55,'two-route reveal'),('021',6.55,.7,'air route stroke'),('044',8.60,.68,'skull inspection'),('001',9.30,.8,'model source arrival'),('021',10.05,.7,'body path annotation'),('035',14.14,.45,'extra route emphasis'),('047',17.42,.75,'microphone closeup'),('049',18.35,.6,'air recording cue'),('023',20.04,.4,'missing component reveal'),('002',22.46,.40,'playback print'),('013',23.03,.20,'play click'),('021',23.35,.65,'actual waveform reveal'),('044',26.46,.55,'recording conditions'),('035',29.26,.45,'both versions resolve')]
voiced=np.sqrt(np.mean(voice[np.max(np.abs(voice),axis=1)>.05]**2));sheet=[]
for i,(id,t,d,why) in enumerate(spec):
 p=root/'sfx_private'/('CB_FREE_'+id+'.wav');raw=shared.load(p);piece=raw[:round(d*48000)];rms=np.sqrt(np.mean(piece**2));peak=float(np.max(np.abs(piece)));wanted=min(.57,voiced*.84*peak/max(.001,rms));actual=shared.place_cue(fx,raw,t,d,wanted,pan=(-.18 if i%2 else .18));music[max(0,round((t-.08)*48000)):min(n,round((t+actual+.14)*48000))]*=.60;sheet.append({'sound_id':'CB_FREE_'+id,'onset_time':t,'duration':actual,'purpose':why,'peak_target':wanted,'source_file':str(p.relative_to(root))})
shared.save(a/'music_review.wav',music);shared.save(root/'mix_raw.wav',voice+music+fx);shared.normalize_two_pass(root/'mix_raw.wav',root/'mix_mastered.wav');shared.canonical_pcm(root/'mix_mastered.wav',a/'preflight_mix.wav')
(root/'episode/SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2));print('Mix ready',duration,'seconds / complete unfaded narration',flush=True)
