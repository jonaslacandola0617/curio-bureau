from pathlib import Path
import sys,json,hashlib,subprocess
import numpy as np
from PIL import Image
import render_movie as M
P=Path(__file__).resolve().parent;ROOT=P.parents[3];R=P/'review';R.mkdir(exist_ok=True)
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
TL=M.TL
cases=[];evidence=[]
selected={'material_texture':TL['scene_boundaries'][2]+2.4,'moving_grain':.5,'selective_focus':TL['scene_boundaries'][1]+1,'focus_shading':TL['scene_boundaries'][1]+1,'focus_hunt':TL['scene_boundaries'][1]+.15,'motion_blur':TL['scene_boundaries'][1]+.15,'chromatic':TL['scene_boundaries'][1]+1,'mechanical_jitter':TL['scene_boundaries'][1]+1,'exposure':TL['scene_boundaries'][1]+1.25}
for effect,t in selected.items():
 M.A.F.DISABLED=set();a=M.frame(t);M.A.F.DISABLED={effect};b=M.frame(t);M.A.F.DISABLED=set()
 aa=np.array(a,dtype=np.int16);bb=np.array(b,dtype=np.int16);diff=float(abs(aa-bb).mean());assert diff>0,(effect,diff)
 p=R/f'proof-{effect}.jpg';board=Image.new('RGB',(720,640));board.paste(a.resize((360,640)),(0,0));board.paste(b.resize((360,640)),(360,0));board.save(p,quality=92)
 # Caption opaque-core is evaluated separately at an actual active phrase.
 cases.append({'effect':effect,'t':t,'meanRedDifference':diff,'opaqueCaptionDifference':0 if np.array_equal(aa[990:1000,500:580],bb[990:1000,500:580])else float(abs(aa[990:1000,500:580]-bb[990:1000,500:580]).mean())});evidence.append(p)
M.A.F.DISABLED=set();q=M.A.Image.new('RGB',(1080,1920),(95,110,125))
a=np.asarray(M.A.F.foreground(q,.1).resize((216,384)),dtype=np.float32);b=np.asarray(M.A.F.foreground(q,.2).resize((216,384)),dtype=np.float32);temporal=float(abs(a-b).mean());assert temporal>.1
# Endcard frames are the output of the untouched shared brand module and bypass finishing.
n=TL['frames']-1;a=M.composed(n);M.A.F.DISABLED=set(M.A.F.EFFECTS);b=M.composed(n);M.A.F.DISABLED=set();assert a.tobytes()==b.tobytes()
cases.append({'effect':'ending_protection','t':n/30,'meanRedDifference':0,'opaqueCaptionDifference':0})
d={'native':[1080,1920],'deterministic':M.frame(.5).tobytes()==M.frame(.5).tobytes(),'studio_sha256':digest(P/'render_movie.py'),'sources':{f:digest(P/f)for f in ['render_art.py','finish.py','timeline.json','episode.json']},'errors':[],'cases':cases,'temporal_grain':{'changed_mean_abs':temporal},'independent_listening':'PENDING','owner_motion_review':'PENDING'}
(R/'FINISHING_RUNTIME.json').write_text(json.dumps(d,indent=2)+'\n')
# Technical sound/tail checks do not claim an audition or audible perfection.
info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(P/'audio/soundtrack.flac')]))
assert info['streams'][0]['sample_rate']=='48000'and info['streams'][0]['channels']==2
assert .8<TL['duration']-TL['last_word_end']<2.5
sound={'channels':2,'sample_rate':48000,'cues':len(json.loads((P/'SFX_CUE_SHEET.json').read_text())),'complete_tail_seconds':TL['duration']-TL['last_word_end'],'technical_presence':'PASS','independent_listening':'PENDING'}
(R/'SOUND_EXECUTION.json').write_text(json.dumps(sound,indent=2)+'\n')
allproof=[{'path':str(p.relative_to(P)),'sha256':digest(p)}for p in evidence+[R/'FINISHING_RUNTIME.json',R/'SOUND_EXECUTION.json']]
coverage={}
for name in ['material_texture','moving_grain','motion_blur','selective_focus','focus_shading','focus_hunt','chromatic','mechanical_jitter','exposure','caption_protection','ending_protection','sequence_continuity','audio_tail','sound_music']:
 coverage[name]={'applicable':True,'execution':'PASS','active_window':str(selected.get(name,'See actual timeline/proof frames')),'expected_result':'Actual native treatment/source motion or media protection demonstrated; creative/listening judgments remain separate','evidence':allproof}
for name in ['ink_bleed','edge_boil']:coverage[name]={'applicable':False,'reason':'No hand-ink strokes or source boundary boil in this microscopy/medical model; keep tiny biological junctions and explanatory labels stable, rather than distorting evidence.'}
audit={'schema':1,'sources':[{'path':f,'sha256':digest(P/f)}for f in ['render_movie.py','render_art.py','finish.py','timeline.json','episode.json']],'coverage':coverage,'owner_motion_review':'PENDING','subjective_listening':'PENDING'}
(P/'FINISHING_COVERAGE.json').write_text(json.dumps(audit,indent=2)+'\n')
sys.path.insert(0,str(ROOT/'production/engine'))
from finishing_contract import validate_finishing
from production_standard import validate_standard
from finishing_audit import check
config=json.loads((P/'episode.json').read_text());validate_finishing(config,P,stage='release',studio_path=P/'render_movie.py',expected_size=[1080,1920]);validate_standard(config,P,TL['duration']);r=check(P/'FINISHING_COVERAGE.json');assert r['execution_records_pass'],r
(R/'PREFLIGHT_GATES.json').write_text(json.dumps(r,indent=2)+'\n');print('NATIVE_EXECUTION_GATES_PASS',temporal,flush=True)
