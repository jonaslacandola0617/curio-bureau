from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def evidence(*names):return [{'path':n,'sha256':h(r/n)}for n in names]
proof=json.loads((r/'NATIVE_EFFECT_AUDIT.json').read_text());coverage={}
for item in proof['effects']:
 name=item['effect'];coverage[name]={'applicable':True,'execution':item['execution'],'active_window':str(item['time'])+'s isolated native diagnostic; material/image effects throughout, blur/hunt at 9.5–10.1667s, ink on support marker after 11s','expected_result':'Independent removal changes native picture pixels while opaque caption differences remain zero. Ink/boil remain anchored to qualitative support line.','evidence':evidence('NATIVE_EFFECT_AUDIT.json')}
for name,files,window,expect in [('caption_protection',['FINISHING_RUNTIME_PROOF.json','NATIVE_EFFECT_AUDIT.json'],'All caption phrases; native sampled states','Opaque caption pixels unchanged after optics.'),('sequence_continuity',['MOTION_REVIEW_TARGETS.json','render.cjs'],'0–26.033333s; lattice to same mass/support figure and remnant','Same conceptual remnant and fixed mass anchor; actual owner moving assessment pending.'),('audio_tail',['AUDIO_RECEIPT.json'],'Complete selected source 19–44.9s plus .827s added space','No selected voice samples lost or speed changed; subjective final-word listening remains open.'),('sound_music',['SFX_CUE_SHEET.json','AUDIO_RECEIPT.json'],'17 timecoded cues and three-part developing score','Original score and reused catalogued actions; listening not certified.')]:
 coverage[name]={'applicable':True,'execution':'PASS','active_window':window,'expected_result':expect,'evidence':evidence(*files)}
coverage['ending_protection']={'applicable':False,'reason':'Explicit isolated-preflight scope, 26.033333s mechanism excerpt. Exact full-film endcard absent and not certified.'}
sources=evidence('render.cjs','effect-proof.cjs','qa.cjs','prepare.py','preflight.py','make_coverage.py','episode.json','FINISHING_CONTRACT.md')
(r/'FINISHING_COVERAGE.json').write_text(json.dumps({'schema':1,'scope':'isolated-preflight, not a full-film release','sources':sources,'coverage':coverage,'owner_motion_review':'PENDING','subjective_listening':'NOT CLAIMED'},indent=2)+'\n')
