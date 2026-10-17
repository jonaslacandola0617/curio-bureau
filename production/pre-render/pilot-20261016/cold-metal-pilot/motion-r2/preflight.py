from pathlib import Path
import importlib.util,json
r=Path(__file__).resolve().parent;e=r.parents[3]/'engine'
def module(name):
 s=importlib.util.spec_from_file_location('cold_'+name,e/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
module('sequence').validate_contract(json.loads((r.parent/'sequence_contract.json').read_text()),'motion')
module('finishing_contract').validate_finishing(json.loads((r/'preview-config.json').read_text()),r,'artwork')
import hashlib
proof=json.loads((r/'RUNTIME_PROOF.json').read_text())
assert proof.get('execution_complete')is True,'Incomplete runtime proof'
assert proof.get('deterministic')is True and proof.get('min_alpha')==255
assert proof.get('hidden_panel_mean_difference')==0,'Unrevealed panel leak'
assert proof.get('source_fingerprints'),'Runtime proof lacks source bindings'
for name,digest in proof['source_fingerprints'].items():
 assert hashlib.sha256((r/name).read_bytes()).hexdigest()==digest,'Stale runtime picture proof: '+name
a=module('finishing_audit').check(r/'FINISHING_COVERAGE.json')
if not a['execution_records_pass']:raise ValueError('Finishing audit blocked: '+'; '.join(a['errors']))
print('Pre-capture: owner art record, finishing declaration, actual proof and current source hashes PASS; motion/listening owner review pending.')

# Validate actual complete canonical mixed-audio bytes, not just their existence/hash.
import wave
timeline=json.loads((r/"timeline.json").read_text())
with wave.open(str(r/"audio/mix.wav")) as w:
 assert (w.getnchannels(),w.getsampwidth(),w.getframerate())==(2,2,48000)
 assert abs(w.getnframes()/48000-timeline["duration"])<.005,"Mixed audio duration mismatch"
 assert len(w.readframes(w.getnframes()))==w.getnframes()*4,"Truncated mixed audio data"
