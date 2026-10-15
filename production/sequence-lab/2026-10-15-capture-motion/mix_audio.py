from pathlib import Path
import json,subprocess,hashlib
import numpy as np
from scipy.io import wavfile
r=Path(__file__).parent;sr=48000;duration=13.2;n=round(sr*duration)
def load(p):
 b=subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar',str(sr),'-ac','2','-']);return np.frombuffer(b,np.float32).reshape(-1,2).copy()
voice=load(r/'audio/voice_source.wav');voice=voice[round(17.60*sr):round(29.22*sr)];voice*=.58/max(np.max(np.abs(voice)),.001)
vo=np.zeros((n,2));start=round(.45*sr);vo[start:start+len(voice)]=voice
# Original harmonic miniature: damped felt-like partials, answered motif, soft sustained harmony.
mu=np.zeros((n,2));t=np.arange(n)/sr
for i,notes in enumerate([[146.832,220,261.626],[130.813,196,246.942],[164.814,220,293.665]]):
 onset=i*4.2;tt=t-onset;env=np.where(tt>=0,np.minimum(np.maximum(tt,0)/.7,1)*np.exp(-np.maximum(tt,0)/3.7),0)
 for f in notes:mu[:,0]+=.008*np.sin(2*np.pi*f*t)*env;mu[:,1]+=.008*np.sin(2*np.pi*f*t+.1)*env
for k,f in enumerate([587.33,440,523.25,659.25,587.33,440,392,523.25]):
 at=.25+k*1.45;tt=t-at;env=np.where(tt>=0,np.exp(-np.maximum(tt,0)*3.6)*np.minimum(np.maximum(tt,0)/.015,1),0);s=(np.sin(2*np.pi*f*tt)+.25*np.sin(2*np.pi*2*f*tt))*.028*env;mu[:,0]+=s;mu[:,1]+=s*.88
mu*=np.minimum(t/.25,1)[:,None]*np.minimum((duration-t)/.7,1)[:,None]
fx=np.zeros_like(mu);sheet=[]
cues=[('camera_move.mp3',0,1.1,.17,'camera approach'),('marker_bold.mp3',2.35,.55,.29,'selection border'),('paper.mp3',2.8,.9,.36,'record arrival'),('paper_turn.flac',3.65,.9,.32,'material extraction'),('pencil.mp3',5.35,1.5,.27,'signal trace'),('resolution.flac',6.1,.9,.20,'captured category resolution')]
for name,on,dur,peak,purpose in cues:
 p=r/'audio'/name;v=load(p)[:round(dur*sr)];v*=peak/max(np.max(np.abs(v)),.001);f=min(round(.025*sr),len(v)//3);v[:f]*=np.linspace(0,1,f)[:,None];v[-f:]*=np.linspace(1,0,f)[:,None];at=round(on*sr);fx[at:at+len(v)]+=v;mu[max(0,at-2400):min(n,at+len(v)+6000)]*=.60;sheet.append({'asset':name,'onset':on,'duration':len(v)/sr,'peak_target':peak,'purpose':purpose,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'provenance':'Existing Curio designed cue; not authentic field recording'})
raw=vo+mu+fx;wavfile.write(r/'audio/raw.wav',sr,np.int16(np.clip(raw,-1,1)*32767));wavfile.write(r/'audio/voice_excerpt.wav',sr,np.int16(vo*32767));wavfile.write(r/'audio/music_study.wav',sr,np.int16(mu*32767));wavfile.write(r/'audio/sfx_study.wav',sr,np.int16(fx*32767));(r/'SFX_CUE_SHEET.json').write_text(json.dumps(sheet,indent=2)+'\n')
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8','-ar','48000','-ac','2','-c:a','pcm_s24le',str(r/'audio/mix.wav')],check=True)
subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/mix.wav'),'-c:a','aac','-b:a','256k',str(r/'audio/mix.m4a')],check=True)
print('13.2s mix with original intact 17.60–29.22s Bernard passage; no new voice or SFX generated')

subprocess.run(['ffmpeg','-y','-v','error','-i',str(r/'audio/mix.wav'),'-c:a','libopus','-b:a','192k',str(r/'audio/mix.ogg')],check=True)
