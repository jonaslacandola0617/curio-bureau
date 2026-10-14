"""Reassemble R2 prepared stems; no voice or stock regeneration."""
import os,sys,subprocess
from pathlib import Path
import numpy as np
sys.path.insert(0,os.environ['CURIO_ENGINE_ROOT']);import audio as shared
a=Path(os.environ['CURIO_PROJECT_ROOT'])/'assets'
v,m,f=[shared.load(a/n) for n in ['voice_full.wav','music_ducked_r2.wav','sfx_full.wav']]
mix=v*.85+m+f;mix*=min(1,.94/max(.001,float(np.max(np.abs(mix)))))
shared.save(a/'mix_raw_r2.wav',mix)
shared.normalize_two_pass(a/'mix_raw_r2.wav',a/'mix_loud_r2.wav')
subprocess.run(['ffmpeg','-y','-v','error','-i',str(a/'mix_loud_r2.wav'),'-af','aresample=192000,alimiter=limit=0.78:attack=5:release=80:level=false,aresample=48000','-ar','48000','-ac','2','-c:a','pcm_s16le',str(a/'mix_limit_r2.wav')],check=True)
shared.canonical_pcm(a/'mix_limit_r2.wav',a/'preflight_mix.wav')

# Reserve AAC reconstruction headroom; measured on the delivered codec.
shared.save(a/'preflight_mix.wav',shared.load(a/'preflight_mix.wav')*.9)
