from pathlib import Path
import os,sys,json
import numpy as np
sys.path.insert(0,os.environ['CURIO_ENGINE_ROOT'])
import audio as engine
r=Path(os.environ['CURIO_PROJECT_ROOT']);a=r/'assets';rate=48000;n=round(12.8*rate)
voice=engine.load(a/'voice_full.wav');music=engine.load(a/'music_full.wav')[:n].copy();fx=np.zeros((n,2))
plan=[
('projector.mp3',0,6,.04,'film mechanism bed'),
('projector.mp3',6,6,.035,'film mechanism bed'),
('garden_foley.mp3',0,2.2,.22,'pig rooting'),
('marker_bold.mp3',.9,.65,.32,'PIG highlight'),
('camera_move.mp3',3.03,.7,.32,'pig focus approach'),
('paper.mp3',5.03,.85,.36,'document entrance'),
('camera_move.mp3',5.13,.5,.14,'document focus settle'),
('paper.mp3',6.35,.55,.24,'treaty title'),
('camera_move.mp3',8.17,1.1,.32,'source approach'),
('camera_move.mp3',9.22,.7,.25,'peak-velocity macro'),
('marker_bold.mp3',9.6,1,.40,'source highlight'),
('paper.mp3',9.92,.65,.24,'source to transcription cut'),
('camera_move.mp3',10.9,.9,.31,'document exit'),
('marker_bold.mp3',11.1,.8,.32,'Haro trace'),
('marker_bold.mp3',11.55,.65,.27,'Rosario trace')]
cues=[]
for name,t,dur,gain,event in plan:
 actual=engine.place_cue(fx,engine.load(a/name),t,dur,gain,rate=rate)
 cues.append(dict(file=name,onset=t,duration=actual,peak_before_master_dbfs=round(float(20*np.log10(gain)),2),event=event,source_path='audio/generated-editorial-v1/'+name,provenance='Reused designed sound, not archival recording'))
fade=round(.35*rate);music[-fade:]*=np.linspace(1,0,fade)[:,None]
master=voice+music+fx;master*=.86/max(.86,float(np.max(np.abs(master))))
engine.save(a/'mix_pre.wav',master);engine.save(a/'sfx_full.wav',fx)
engine.normalize_two_pass(a/'mix_pre.wav',a/'master_full.wav')
engine.canonical_pcm(a/'master_full.wav',a/'preflight_mix.wav')
(r/'SFX_CUE_SHEET.json').write_text(json.dumps(cues,indent=2))
print('Mixed 15 reused cues; two-pass loudness normalization')
