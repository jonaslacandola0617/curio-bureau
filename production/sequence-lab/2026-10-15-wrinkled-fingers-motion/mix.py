from pathlib import Path
import json,subprocess,hashlib
import numpy as np
from scipy.io import wavfile
r=Path(__file__).parent;sr=48000;duration=12;n=round(sr*duration)
def load(p):
 b=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar','48000','-ac','2','-']);return np.frombuffer(b,np.float32).reshape(-1,2).copy()
voice=load(r/'audio/voice_source.wav');source_duration=len(voice)/sr;voice*=.58/max(np.max(np.abs(voice)),.001);vo=np.zeros((n,2));start=round(.35*sr);assert start+len(voice)<n-round(.75*sr);vo[start:start+len(voice)]=voice
mu=np.zeros((n,2));t=np.arange(n)/sr
# Reuse the approved study-score construction; original harmony/motif, no stock audio.
for i,notes in enumerate([[146.832,220,261.626],[130.813,196,246.942],[164.814,220,293.665]]):
 onset=i*3.8;tt=t-onset;env=np.where(tt>=0,np.minimum(np.maximum(tt,0)/.7,1)*np.exp(-np.maximum(tt,0)/3.7),0)
 for f in notes:mu[:,0]+=.008*np.sin(2*np.pi*f*t)*env;mu[:,1]+=.008*np.sin(2*np.pi*f*t+.1)*env
for k,f in enumerate([587.33,440,523.25,659.25,587.33,440,392,523.25]):
 at=.18+k*1.34;tt=t-at;env=np.where(tt>=0,np.exp(-np.maximum(tt,0)*3.6)*np.minimum(np.maximum(tt,0)/.015,1),0);v=(np.sin(2*np.pi*f*tt)+.25*np.sin(2*np.pi*2*f*tt))*.031*env;mu[:,0]+=v;mu[:,1]+=v*.88
mu*=np.minimum(t/.18,1)[:,None]*np.minimum((duration-t)/.7,1)[:,None];fx=np.zeros_like(mu);sheet=[]
cues=[('camera_move.mp3',0,.65,.20,'intro_approach','Photo and heading establish'),('paper.mp3',.60,.95,.32,'photo_comparison','Source A/B comparison reveal'),('micro_emphasis.flac',2.245,.60,.27,'vessel_narrowing','Editorial accent on represented narrowing'),('paper_turn.flac',6.5,.85,.29,'volume_change','Printed mechanism shifts'),('marker_bold.mp3',8.95,.65,.35,'crease_selection','Printed crease marks and surface fold'),('resolution.flac',10.4,.65,.21,'fold_settle','Resolved explanatory hold')]
for name,on,dur,peak,event,purpose in cues:
 p=r/'audio'/name;raw=load(p);energy=np.sqrt(np.mean(raw*raw,axis=1));active=np.where(energy>max(.0005,np.max(energy)*.03))[0];offset=max(0,int(active[0]) - round(.01*sr)) if len(active) else 0;v=raw[offset:offset+round(dur*sr)].copy();v*=peak/max(np.max(np.abs(v)),.001);fade=min(round(.018*sr),len(v)//3);v[:fade]*=np.linspace(0,1,fade)[:,None];v[-fade:]*=np.linspace(1,0,fade)[:,None];at=round(on*sr);fx[at:at+len(v)]+=v;mu[max(0,at-2400):min(n,at+len(v)+6000)]*=.65;sheet.append({'sound_id':name,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_offset_seconds':offset/sr,'onset_time':on,'duration':len(v)/sr,'peak_target':peak,'animation_event_id':event,'narrative_word_id':'phrase-estimate; not word-aligned','purpose':purpose,'mix_bus':'physical/editorial','provenance':'Existing Curio designed cue, reused. Not an authentic body or field recording.'})
for name,a in [('voice_study.wav',vo),('music_study.wav',mu),('sfx_study.wav',fx),('raw.wav',vo+mu+fx)]:wavfile.write(r/'audio'/name,sr,np.int16(np.clip(a,-1,1)*32767))
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8','-ar','48000','-ac','2','-c:a','pcm_s24le',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/mix.wav'),'-c:a','libopus','-b:a','192k',str(r/'audio/mix.ogg')],check=True)
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n');(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'source_sha256':hashlib.sha256((r/'audio/voice_source.wav').read_bytes()).hexdigest(),'source_duration':source_duration,'onset_time':.35,'all_source_samples_preserved':True,'voice_fade':False,'decoded_source_end_on_timeline':.35+source_duration,'closing_word':'folds','final_caption_end':11.7,'duration':12,'endcard':'not part of this isolated moving study','listening_approval':'pending owner review; no independent word verification claimed','caption_timing':'estimated phrases; source sentence pause at 4.361–4.895s used'} ,indent=2)+'\n');print('Mix ready; source voice',source_duration,'seconds, complete and unfaded')
