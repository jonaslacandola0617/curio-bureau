"""Reassemble the approved prepared stems without regenerating voice or stock Foley."""
import os,sys
from pathlib import Path
sys.path.insert(0,os.environ['CURIO_ENGINE_ROOT']);import audio as shared
assets=Path(os.environ['CURIO_PROJECT_ROOT'])/'assets'
voice,music,fx=[shared.load(assets/n) for n in ['voice_full.wav','music_full.wav','sfx_full.wav']]
shared.save(assets/'mix_raw.wav',voice*.85+music+fx)
shared.normalize_two_pass(assets/'mix_raw.wav',assets/'mix_loud.wav')
shared.canonical_pcm(assets/'mix_loud.wav',assets/'preflight_mix.wav')
