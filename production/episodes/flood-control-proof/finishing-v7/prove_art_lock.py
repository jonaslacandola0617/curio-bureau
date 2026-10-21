"""Guard the owner's artwork lock independently from the new overlay proof."""
from pathlib import Path
import importlib.util,sys,json,hashlib
import numpy as np
from PIL import Image,ImageDraw
import render as V
import finish as F
P=Path(__file__).resolve().parent;B=P/'baseline'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(B/'render.py')=='383fb08d96428713b1354686082db08e6ec891f3e84ccfadf5e7d3bae6eef767'
assert sha(B/'finish.py')=='8eea423f1207a2381df6f34cffa11f83e70ffef9206428d703b6f50db4cb673b'
assert (P/'render.py').read_text().replace(' im=F.foreground(im,qt)\n','')==(B/'render.py').read_text()
original=json.loads((P/'BASELINE_INPUTS.json').read_text());unchanged=[]
allowed={'render.py','finish.py','prove_finishing.py','build_release.py','SOURCES_AND_SCOPE.md'}
for x in original['inputs']:
 if 'path'in x and x['path']not in allowed:
  assert sha(P/x['path'])==x['sha256'],x['path'];unchanged.append(x['path'])
for name in ['assets','frames']:
 if not(B/name).exists():(B/name).symlink_to((P/name).resolve())
spec=importlib.util.spec_from_file_location('original_finish',B/'finish.py');old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
sys.modules['finish']=old
spec=importlib.util.spec_from_file_location('original_art',B/'render.py');orig=importlib.util.module_from_spec(spec);spec.loader.exec_module(orig);sys.modules['finish']=F
times=[0,.3,2.1,4.4,7.04,10.5,12.68,16.5,20.6,24.2,26.32,32.8,34.82,40.52,45.06,50.6,53.4,57.5,59.23]
rows=[]
for t in times:
 old.DISABLED={'material_texture','moving_grain'};F.DISABLED={'material_texture','moving_grain'}
 a=orig.raw(t);b=V.raw(t);assert np.array_equal(np.asarray(a),np.asarray(b)),t
 rows.append({'t':t,'mean_absolute_difference':0,'artwork_pixels_equal_with_finishing_disabled':True})
old.DISABLED.clear();F.DISABLED.clear()
media=json.loads((P/'locked/LOCKED_MEDIA_RECEIPT.json').read_text())
for x in media['ending_native_frames']:assert sha(P/'ending'/x['file'])==x['sha256']
# Foreground proof must exercise photographs as well as navy negative space.
a=V.raw(4.4);F.DISABLED={'moving_grain'};b=V.raw(4.4);F.DISABLED.clear()
metrics={}
for name,rect in {'photograph':[80,500,980,880],'background':[60,110,1000,350]}.items():
 delta=float(np.mean(np.abs(np.asarray(a.crop(rect),dtype=float)-np.asarray(b.crop(rect),dtype=float))));assert delta>.2,(name,delta);metrics[name]=delta
report={'schema':1,'owner_artwork_approved':True,'finishing_only':True,'renderer_diff':'Exactly one foreground finishing call; all scene code otherwise byte-identical','unchanged_inputs':unchanged,'sampled_art_equality':rows,'all33_ending_frames_reused_and_hash_equal':True,'approved_audio_packet_hash':media['audio_packet_payload_hash'],'foreground_grain_native_mean_abs_by_region':metrics,'owner_new_finishing_approval':'PENDING'}
(P/'review/ARTWORK_PRESERVATION.json').write_text(json.dumps(report,indent=2)+'\n')
print('Locked artwork equality PASS at19 demanding states; all33 ending frames preserved',flush=True)
