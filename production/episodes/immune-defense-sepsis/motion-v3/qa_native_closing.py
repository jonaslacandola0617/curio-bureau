from pathlib import Path
import json
import render_movie as M
P=Path(__file__).resolve().parent;R=P/'review';R.mkdir(exist_ok=True)
M.A.F.DISABLED=set(M.A.F.EFFECTS)
times=[37.9,38.25,38.3333333333,38.5,39.1,41.1666666667,41.25,41.5,42.1,44.3]
ref=M.frame(times[0],False).tobytes()
for t in times:assert M.frame(t,False).tobytes()==ref,('Closing artwork re-entered or changed',t)
M.A.F.DISABLED=set()
(R/'NATIVE_CLOSING_CONTINUITY.json').write_text(json.dumps({'times':times,'caption_and_finishing_disabled_for_geometry_test':True,'closing_artwork_held_identically_across_both_narration_boundaries':'PASS','finishing_source':'unchanged and tested independently by prove_runtime.py','audio_listening':'NOT CLAIMED'},indent=2)+'\n');print('NATIVE_CLOSING_CONTINUITY_PASS',flush=True)
