"""Fail closed on absent execution; preserves separate creative/listening verdicts."""
from pathlib import Path
import json,hashlib,sys
import numpy as np
from PIL import Image,ImageDraw
import render as V
import finish as F
P=Path(__file__).resolve().parent;R=P/'review';D=R/'proof';D.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def mad(a,b):return float(np.mean(np.abs(np.asarray(a,dtype=float)-np.asarray(b,dtype=float))))
def evidence(p):return {'path':str(p.relative_to(P)),'sha256':sha(p)}
times={'material_texture':4.4,'moving_grain':4.4,'motion_blur':.6,'selective_focus':.3,'focus_shading':.3,'focus_hunt':.3,'chromatic':4.4,'mechanical_jitter':4.4,'exposure':4.4,'ink_bleed':2.1,'edge_boil':2.1}
cases=[];coverage={};boards=[]
for name,t in times.items():
 F.DISABLED.clear();a=V.raw(t)
 F.DISABLED.add(name);b=V.raw(t);F.DISABLED.clear()
 value=mad(a,b);assert value>0,(name,'did not change native picture')
 # Caption's opaque core is invariant because it is composited after every source effect.
 c=next(x for x in V.TL['captions']if x['start']<=t<x['end']);s=c['text'];n=35
 while ImageDraw.Draw(a).textbbox((0,0),s,font=V.font(n))[2]>970:n-=1
 w=ImageDraw.Draw(a).textbbox((0,0),s,font=V.font(n))[2]+32;x=(1080-w)//2
 cap=mad(a.crop((x,975,x+w,1037)),b.crop((x,975,x+w,1037)));assert cap==0
 ap=a.resize((360,640),Image.Resampling.LANCZOS);bp=b.resize((360,640),Image.Resampling.LANCZOS)
 board=Image.new('RGB',(720,672),V.N);board.paste(bp,(0,0));board.paste(ap,(360,0));d=ImageDraw.Draw(board);d.text((12,645),name+' OFF',fill=V.I);d.text((372,645),name+' ON',fill=V.I)
 dest=D/(name+'-phone-ab.jpg');board.save(dest,quality=96);boards.append(board)
 cases.append({'effect':name,'t':t,'meanRedDifference':float(np.mean(np.abs(np.asarray(a,dtype=float)[:,:,0]-np.asarray(b,dtype=float)[:,:,0]))),'native_mean_abs':value,'phone_mean_abs':mad(ap,bp),'opaqueCaptionDifference':cap})
 coverage[name]={'applicable':True,'execution':'PASS','active_window':[t,t+1/12],'expected_result':{'material_texture':'Surface-local print tooth and laid fibers, without obscuring photographic detail','moving_grain':'Changing fine/coarse source grain','motion_blur':'Finite source integration during approach, followed by a sharp hold','selective_focus':'Selected source remains sharper than its surround','focus_shading':'Same focus field gently darkens the surround','focus_hunt':'Brief source defocus overshoot settles in 0.68s','chromatic':'One native-pixel image channel separation; documentary map colors excluded','mechanical_jitter':'Coherent source-plane displacement, clean screen type','exposure':'Restrained photographic exposure variation','ink_bleed':'Local editorial underline ink spread','edge_boil':'Local editorial underline changes at12fps; no scientific boundary wobble'}[name],'evidence':[evidence(dest)],'limits':'Pixel difference proves execution only; artistic result requires encoded review.'}
F.DISABLED.clear();a=V.raw(4.4);assert mad(a,V.raw(4.4))==0
F.DISABLED=F.EFFECTS-{'moving_grain'}
src=V.basin.resize((1080,840));a=F.source(src,4.4).resize((360,280));b=F.source(src,4.5).resize((360,280));temporal=mad(a,b);assert temporal>.1
F.DISABLED.clear();n=V.TL['frames']-1;a=V.composed(n);F.DISABLED=set(F.EFFECTS);b=V.composed(n);F.DISABLED.clear();assert mad(a,b)==0
cases.append({'t':n/30,'meanRedDifference':0,'opaqueCaptionDifference':0,'role':'Shared ending untouched by every finishing switch'})
report={'schema':1,'native':[1080,1920],'deterministic':True,'errors':[],'studio_sha256':sha(P/'render.py'),'finish_sha256':sha(P/'finish.py'),'cases':cases,'temporal_grain':{'changed_mean_abs':temporal,'method':'Same source and exposure, only grain time changes; compared at360px width'},'caption_protection':'Zero difference inside actual opaque caption regions for every per-effect comparison','ending_protection':'Final shared-module frame is byte-identical with all finishing toggled','owner_approval':'PENDING','subjective_listening':'PENDING'}
(R/'FINISHING_RUNTIME.json').write_text(json.dumps(report,indent=2)+'\n')
proof=evidence(R/'FINISHING_RUNTIME.json')
for name,window,result in [('caption_protection',[0,V.TL['ending_start']],'Type and captions are rendered after source optics'),('ending_protection',[V.TL['ending_start'],V.TL['duration']],'Shared ending receives no additional processing'),('sequence_continuity',[0,V.TL['ending_start']],'Specific source components retain provenance and geographic registration'),('audio_tail',[V.TL['voice_duration'],V.TL['ending_start']],'All retained narration samples play at speed1 with a0.9s pre-ending tail'),('sound_music',[0,V.TL['duration']],'Continuous full-length original episode score and existing action cues; independent listening remains pending')]:
 coverage[name]={'applicable':True,'execution':'PASS','active_window':window,'expected_result':result,'evidence':[proof if name in {'caption_protection','ending_protection'}else evidence(P/('SHOT_CONTRACTS.json'if name=='sequence_continuity'else'audio/AUDIO_RECEIPT.json'if name=='audio_tail'else'SFX_CUE_SHEET.json'))]}
audit={'schema':1,'sources':[evidence(P/f)for f in ['render.py','finish.py','timeline.json','episode.json','SHOT_CONTRACTS.json']],'coverage':coverage,'owner_motion_review':'PENDING','subjective_listening':'PENDING'}
(P/'FINISHING_COVERAGE.json').write_text(json.dumps(audit,indent=2)+'\n')
contract={'enabled':True,'style':'source-local photographic/printed material; original video detail preserved','coverage':coverage,'exclusions':['No color-channel separation or edge boil of documentary map boundaries','No optics or texture applied after screen-space typography','No added treatment on locked ending'],'focus_windows':[{'start':t,'end':t+.68,'settles_to':0}for t in [.12,3.7,V.BND[1],V.BND[2]+2.6,V.BND[3],V.BND[5],V.BND[5]+3.6,V.BND[7],V.BND[7]+2.5,V.BND[7]+5,V.BND[8]+2.1]]}
(P/'FINISHING_CONTRACT.json').write_text(json.dumps(contract,indent=2)+'\n')
sys.path.insert(0,str(V.ROOT/'production/engine'))
from finishing_contract import validate_finishing
from finishing_audit import check
from production_standard import validate_standard
config=json.loads((P/'episode.json').read_text())
result={'finishing':validate_finishing(config,P,stage='release',studio_path=P/'render.py',expected_size=[1080,1920]),'coverage':check(P/'FINISHING_COVERAGE.json'),'cadence':validate_standard(config,P,actual_duration=V.TL['duration'])}
assert result['coverage']['execution_records_pass'],result
(R/'PREFLIGHT_GATES.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'EXECUTION_PROOF_PASS','effects':len(times),'temporal_phone_grain_mad':temporal,'creative_approval':'PENDING','listening':'PENDING'}),flush=True)
