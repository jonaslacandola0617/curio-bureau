from pathlib import Path
import json,sys,hashlib,subprocess,re
r=Path(__file__).resolve().parent;repo=r.parents[4];sys.path.insert(0,str(repo/'production/engine'));from finishing_contract import validate_finishing
tl=json.loads((r/'timeline.json').read_text());proof=json.loads((r/'FINISHING_RUNTIME_PROOF.json').read_text());config={'id':'sun-disappeared','revision':'full-v1','visual_style':'image-led','material_profile':'image-led-v1','brand_ending':'london-bridge-v1','finishing':{'enabled':True,'implementation':'render.cjs / finish','contract':'FINISHING_CONTRACT.md','runtime_proof':'FINISHING_RUNTIME_PROOF.json','studio':'render.cjs'}}
(r/'FINISHING_CONFIG.json').write_text(json.dumps(config,indent=2)+'\n');result=validate_finishing(config,r,stage='release',studio_path=r/'render.cjs',expected_size=[1080,1920]);(r/'FINISHING_GATE.json').write_text(json.dumps(result,indent=2)+'\n')
errors=[]
for i,c in enumerate(tl['captions']):
 if c['end']<=c['start']:errors.append(['invalid',i])
 if i and c['start']<tl['captions'][i-1]['end']-.001:errors.append(['overlap',i])
assert not errors,errors
(r/'qa/CAPTION_QA.json').write_text(json.dumps({'interval_errors':errors,'phrases':len(tl['captions']),'method':tl['caption_method'],'screen_band':'all captions at875–993px,45.6–51.7% of frame','word_coverage':'all local actual-audio ASR words grouped in order; independent acoustic verification not claimed'},indent=2)+'\n')
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(r/'captions.srt').write_text(''.join(f"{i+1}\n{stamp(c['start'])} --> {stamp(c['end'])}\n{c['text']}\n\n"for i,c in enumerate(tl['captions'])))
files=['scene.cjs','approved-passage.cjs','render.cjs','timeline.json','mix.py','FINISHING_CONTRACT.md','FINISHING_CONFIG.json','FINISHING_RUNTIME_PROOF.json','Sun-Full-Mix-v1.flac','SFX_CUE_SHEET.json','captions.srt']
(r/'SOURCE_FINGERPRINT.json').write_text(json.dumps({'artwork_source':'30259142d60749478f80c304277231250dc59d3e','motion_source':'c9ca6af4f2a58c242421ca6bbdff78001f0204b1','motion_approval':'61b1954c831859a0a31ca3eb898bb74f3fe28fc3','duration':tl['duration'],'frames':tl['frames'],'native':[1080,1920],'fps':30,'scene_fps':12,'ending_exception':'original brand.js,30fps curve','inputs':[{'path':p,'sha256':hashlib.sha256((r/p).read_bytes()).hexdigest()}for p in files]},indent=2)+'\n')
(r/'NARRATION_TAIL_QA.json').write_text(json.dumps({'original_narration_sha256':hashlib.sha256((r.parent/'audio/voice-original.mp3').read_bytes()).hexdigest(),'edited_narration_decoded_duration':47.59,'final_clause':"We'd spend those final minutes living in the sun's past.",'final_word':'past','ASR_final_word_end':tl['words'][-1]['end'],'ending_start':48.4,'protected_after_decoded_voice':.81,'film_duration':49.5,'voice_faded':False,'independent_encoded_listening':'OWNER REVIEW PENDING; machine checks are separate'},indent=2)+'\n')
(r/'.gitignore').write_text('audio/*.wav\nchunks/*.mkv\n*.mp4\n')
(r/'README.md').write_text('''# Complete Sun-disappearance experiment — full v1 review
Complete49.5-second,1485-frame native1080×1920/30fps episode. Scene/camera/ink/grain states evaluated at12fps; exact established endcard remains30fps. Full natural-speed narration, original evolving score and31 existing SFX cues. The owner-approved11.6s passage is inherited with a full-film footer and phrase captions; composition and sound-stem timing are retained.
This is a complete owner review, not an assertion of human final approval. Source and native finishing checks precede capture; verified lossless RGB recovery chunks are archived at most two at a time. Final MP4 gets its own version and public byte/hash verification.
No shadow-like type/graphic backdrops. Crisp solid caption supports remain as in approved preflight. The impossible mass-removal premise, approximate8m20 travel time, NASA composite/assigned-color imagery and simplified Sun–Earth orbital figure remain explicitly qualified.
''')
print(json.dumps({'finishing_gate':result,'caption_errors':errors,'caption_phrases':len(tl['captions']),'tail_after_decoded_voice':.81}))
