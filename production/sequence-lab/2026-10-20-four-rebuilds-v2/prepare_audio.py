from pathlib import Path
import json,subprocess,hashlib,csv,sys,math,re
import numpy as np
from scipy.io import wavfile
r=Path(__file__).resolve().parent;repo=r.parents[2];id=sys.argv[1];out=r/id;out.mkdir(exist_ok=True);sr=48000;n=12*sr;ix=['01-concrete','02-diomede','03-shrimp','04-brine'].index(id);tl=json.loads((out/'timeline.json').read_text())
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar','48000','-ac','2','-']),np.float32).reshape(-1,2).copy()
vo=np.zeros((n,2),np.float32);src=load(r.parent/'2026-10-20-four-original-tests/assets'/f'{id}-voice.mp3');start=round(tl['voice_offset']*sr);assert start+len(src)<round(10*sr), 'Voice must leave full tail before ending';vo[start:start+len(src)]=src;vo*=.59/max(abs(vo).max(),.001)
mu=np.zeros_like(vo);fx=np.zeros_like(vo);base=[130.813,164.814,146.832,110.0][ix]
# Four independently keyed original short scores: sparse question, active mechanism, earned cadence.
for k,at in enumerate(np.arange(.1,10.9,.55 if ix!=1 else .65)):
 phase=0 if at<3.5 else 1 if at<8.5 else 2;steps=[[0,3,7,10,7,3],[0,7,12,4,7,11],[0,3,10,7,3,12],[0,7,3,10,12,7]][ix];degree=steps[k%len(steps)];f=base*2**((degree+(12 if phase==1 else 0))/12);length=1.5;t=np.arange(round(length*sr))/sr;env=np.minimum(t/.012,1)*np.exp(-t*(3.0 if ix in [0,1] else 2.0));tone=(np.sin(2*np.pi*f*t)+.32*np.sin(2*np.pi*f*2.001*t)*np.exp(-1.7*t)+.17*np.sin(2*np.pi*f*3.003*t)*np.exp(-3.1*t)+.09*np.sin(2*np.pi*f*5.01*t)*np.exp(-5*t))*env*(.075 if phase!=2 else .09);a=round(at*sr);l=min(len(tone),n-a);pan=.28*math.sin(k*2.4);mu[a:a+l,0]+=tone[:l]*(1-pan);mu[a:a+l,1]+=tone[:l]*(1+pan)
for delay,gain in [(0.113,.19),(0.237,.10)]:
 lag=round(delay*sr);mu[lag:,0]+=mu[:-lag,1].copy()*gain;mu[lag:,1]+=mu[:-lag,0].copy()*gain
# Low sustained chord turns as the mechanism resolves; no reused finished soundtrack.
t=np.arange(n)/sr
for f in [base/2,base*2**(3/12)/2,base*1.5]:mu[:,0]+=.012*np.sin(2*np.pi*f*t)*np.minimum(t/.4,1);mu[:,1]+=.012*np.sin(2*np.pi*f*1.001*t)*np.minimum(t/.4,1)
voice_energy=np.convolve(np.max(abs(vo),axis=1),np.ones(2400)/2400,mode='same');duck=np.clip(1-voice_energy*9,.30,1);mu*=duck[:,None];mu[-round(1.0*sr):]*=np.linspace(1,0,round(sr))[:,None]
cat={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())}
sets=[[('wood_stress', 0.25, 0.2), ('document_focus', 1.9, 0.16), ('map_route_draw', 2.75, 0.18), ('data_pulse', 4.2, 0.14), ('tiny_mask_reveal', 6.7, 0.2), ('quiet_resolution', 8.8, 0.22)], [('photo_slide', 0.4, 0.18), ('evidence_lock', 1.6, 0.15), ('pencil_marks', 3.35, 0.18), ('tiny_mask_reveal', 4.5, 0.16), ('map_route_draw', 5.3, 0.18), ('typewriter_cluster', 6.65, 0.23), ('quiet_resolution', 8.8, 0.18)], [('doubt_tick', 0.1, 0.14), ('document_focus', 1.8, 0.17), ('cut_match', 2.25, 0.17), ('steel_latch', 5.05, 0.21), ('map_route_draw', 5.27, 0.18), ('tiny_mask_reveal', 6.35, 0.18), ('hard_fact_punctuate', 8.38, 0.34), ('restrained_boom', 8.38, 0.13), ('quiet_resolution', 9.4, 0.18)], [('cavern_lowwind', 0.1, 0.1), ('pencil_marks', 0.4, 0.17), ('soft_depth_pass', 2.4, 0.18), ('tiny_mask_reveal', 3, 0.16), ('heavy_hinge', 5.4, 0.15), ('soft_depth_pass', 6.6, 0.17), ('map_route_draw', 7, 0.18), ('warm_resolution', 9.1, 0.18)]];cues=[]
for name,at,g in sets[ix]:
 row=cat[name];p=repo/row['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'];v=load(p)*g;i=round(at*sr);l=min(len(v),n-i);fx[i:i+l]+=v[:l];cues.append({'id':name,'time':at,'gain':g,'sha256':row['sha256'],'note':'Original synthesized editorial cue, not an authentic recording of the depicted event'})
raw=vo+mu+fx;raw*=.80/max(abs(raw).max(),.001)
for name,data in [('voice',vo),('music',mu),('sfx',fx),('raw',raw)]:wavfile.write(out/f'{name}.wav',sr,data.astype(np.float32))
# Measured two-pass normalization; preserve natural speech time and complete source tail.
a=subprocess.run(['ffmpeg','-hide_banner','-i',str(out/'raw.wav'),'-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True,check=True);m=json.loads(re.findall(r'\{[^{}]*\}',a.stderr)[-1]);f=f"loudnorm=I=-14:TP=-1.5:LRA=8:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true:print_format=json"
subprocess.run(['ffmpeg','-v','error','-y','-i',str(out/'raw.wav'),'-af',f,'-ar','48000','-ac','2','-c:a','pcm_f32le',str(out/'mix.wav')],check=True)
(out/'AUDIO_RECEIPT.json').write_text(json.dumps({'source_mp3_sha256':hashlib.sha256((r.parent/'2026-10-20-four-original-tests/assets'/f'{id}-voice.mp3').read_bytes()).hexdigest(),'source_duration':len(src)/sr,'voice_offset':tl['voice_offset'],'speed':1,'legacy_repository_voice_label':'Bernard','provider_voice_name':'Clyde - Vintage Male Radio Announcer','voice_id':'QMJTqaMXmGnG8TCm8WQG','voice_identity':'Exact legacy voice ID retained; provider name differs from repository alias','score':'New original three-phase plucked harmonic score; independent six-note topic motifs, decaying overtones, stereo room taps and voice-envelope ducking','cues':cues,'normalization_measurements':m,'mix_sha256':hashlib.sha256((out/'mix.wav').read_bytes()).hexdigest(),'independent_listening':'NOT CLAIMED'},indent=2))
print(id,'audio ready',len(src)/sr)
