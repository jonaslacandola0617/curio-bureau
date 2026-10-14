import json
from scipy.io import wavfile
import numpy as np
def load(assets):
 t=json.loads((assets/"timing.json").read_text());sr,v=wavfile.read(assets/"voice_full.wav");v=v.mean(axis=1).astype(float);n=160;parts=np.array_split(v,n);w=[float(np.max(np.abs(x))) for x in parts];m=max(w) or 1
 return {"timing":t,"waveform":[x/m for x in w]}
