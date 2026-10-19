from pathlib import Path
import json,subprocess,hashlib,csv
import numpy as np
from scipy.io import wavfile
r=Path(__file__).resolve().parent;repo=r.parents[2];sr=48000;tl=json.loads((r/'timeline.json').read_text());n=round(tl['duration']*sr)
def load(p):return np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p),'-f','f32le','-ar','48000','-ac','2','-']),np.float32).reshape(-1,2).copy()
voice=load(r/'audio/source-voice.flac');music=load(r/'audio/source-music.flac');vo=np.zeros((n,2),np.float32)
pins=json.loads((r/'INPUTS.json').read_text())
for name in ['voice','music']:assert hashlib.sha256((r/'audio'/f'source-{name}.flac').read_bytes()).hexdigest()==pins['source_audio_flac_sha256'][name], 'Source audio drift: '+name
for item in pins['files']:assert hashlib.sha256((repo/item['path']).read_bytes()).hexdigest()==item['sha256'], item['path']
for a,b,at in tl['parts']:
 v=voice[round(a*sr):round(b*sr)].copy();fade=round(.008*sr);v[:fade]*=np.linspace(0,1,fade)[:,None];v[-fade:]*=np.linspace(1,0,fade)[:,None];i=round(at*sr);vo[i:i+len(v)]+=v
# Reuse the original Black Dwarf score, taking its developing mechanism-to-payoff section.
mu=music[round(27*sr):round(46.5*sr)].copy();mu[:round(.18*sr)]*=np.linspace(0,1,round(.18*sr))[:,None];mu[-round(1.3*sr):]*=np.linspace(1,0,round(1.3*sr))[:,None]
fx=np.zeros_like(vo);cat={x['name']:x for x in csv.DictReader((repo/'audio/curio_sfx_v1/CATALOG.csv').open())};cues=[]
for id,t,g,event in [('map_route_draw',1.4,.22,'mass reference appears'),('doubt_tick',2.25,.20,'support alternative'),('document_focus',3.75,.18,'inspect comparison'),('evidence_lock',5.95,.20,'fixed-mass lock'),('map_route_draw',7.5,.22,'first limit descent'),('cable_tension',11.25,.13,'limit crosses mass'),('causal_reveal',13.65,.22,'conditional contraction')]:
 row=cat[id];p=repo/row['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'];v=load(p)*g;i=round(t*sr);l=min(len(v),n-i);fx[i:i+l]+=v[:l];cues.append({'id':id,'time':t,'event':event,'gain':g,'source_sha256':row['sha256'],'rights':'Original designed Curio cue; not recorded stellar sound'})
raw=vo+mu+fx
# A single measured master gain preserves voice dynamics; no speed changes or new TTS.
gain=min(.91/max(abs(raw).max(),.001),1.35);mix=raw*gain
for name,data in [('voice',vo),('music',mu),('sfx',fx),('mix',mix)]:wavfile.write(r/'audio'/f'{name}.wav',sr,data.astype(np.float32))
(r/'AUDIO_RECEIPT.json').write_text(json.dumps({'parts':tl['parts'],'voice_pcm_sha256':hashlib.sha256(voice.tobytes()).hexdigest(),'music_pcm_sha256':hashlib.sha256(music.tobytes()).hexdigest(),'cues':cues,'peak':float(abs(mix).max()),'master_gain':gain,'retained_natural_speed':True,'independent_listening':'not claimed','source':'Black Dwarf full-v2 original Bernard and score stems'},indent=2))
