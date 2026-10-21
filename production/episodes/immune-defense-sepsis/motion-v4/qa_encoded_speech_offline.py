# Offline-only analysis: no ONNX VAD; process-level network syscalls denied before model imports.
import os,ctypes,ctypes.util,errno
os.environ['HF_HUB_OFFLINE']='1';os.environ['HF_HUB_DISABLE_TELEMETRY']='1';os.environ['DO_NOT_TRACK']='1'
libpath=ctypes.util.find_library('seccomp')
if not libpath:raise RuntimeError('No network-denial filter available; refuse to run inference')
lib=ctypes.CDLL(libpath);lib.seccomp_init.argtypes=[ctypes.c_uint32];lib.seccomp_init.restype=ctypes.c_void_p;lib.seccomp_syscall_resolve_name.argtypes=[ctypes.c_char_p];lib.seccomp_syscall_resolve_name.restype=ctypes.c_int;lib.seccomp_rule_add.argtypes=[ctypes.c_void_p,ctypes.c_uint32,ctypes.c_int,ctypes.c_uint];lib.seccomp_load.argtypes=[ctypes.c_void_p]
ctx=lib.seccomp_init(0x7fff0000)
if not ctx:raise RuntimeError('Cannot create network denial filter')
for name in ['socket','connect','sendto','sendmsg','sendmmsg','accept','accept4','bind','listen']:
 n=lib.seccomp_syscall_resolve_name(name.encode())
 if n>=0 and lib.seccomp_rule_add(ctx,0x00050000|errno.EPERM,n,0)!=0:raise RuntimeError('Cannot deny network syscall '+name)
if lib.seccomp_load(ctx)!=0:raise RuntimeError('Cannot activate network denial filter')
from pathlib import Path
import json,subprocess,numpy as np,re
from faster_whisper import WhisperModel
p=Path(__file__).resolve().parent;alignment=json.loads((p/'audio/UTTERANCE_ALIGNMENT.json').read_text());x=np.frombuffer(subprocess.check_output(['ffmpeg','-v','error','-i',str(p/'Curio-Immune-Defense-Full-Review-v4.mp4'),'-f','f32le','-ar','16000','-ac','1','-']),dtype=np.float32);model=WhisperModel('base.en',device='cpu',compute_type='int8',local_files_only=True,cpu_threads=4);reports=[]
norm=lambda t:re.sub('[^a-z0-9 ]','',t.lower()).split()
for u in alignment['units']:
 if u['index']<13:continue
 a,b=u['repaired_nonquiet_span'];start=max(0,a-.12);end=b+.12;segments,_=model.transcribe(x[round(start*16000):round(end*16000)].copy(),language='en',beam_size=5,vad_filter=False,condition_on_previous_text=False);text=' '.join(s.text.strip()for s in segments);expected=' '.join(w['word']for w in u['words']);row={'unit':u['index'],'span':[start,end],'expected':expected,'observed':text,'normalised_word_sequence_match':norm(expected)==norm(text)};reports.append(row);print(json.dumps(row),flush=True)
(p/'review/encoded/ENCODED_CLOSING_SPEECH_CHECK.json').write_text(json.dumps({'source':'Actually decoded new full mix, original Bernard; no ASR prompt','offline':'No ONNX VAD, cached local model, process network syscalls denied','checks':reports,'limits':'Automated speech recognition evidence, not independent human sound audition'},indent=2)+'\n')
