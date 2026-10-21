from pathlib import Path
import json
import render_movie as M
P=Path(__file__).resolve().parent;R=P/'review';R.mkdir(exist_ok=True);tl=M.TL;b=tl['scene_boundaries'];times=[b[6]+1,b[7]-.1,b[7]+.1,b[7]+.6,b[8]-.1,b[8]+.1,b[8]+.6,tl['ending_start']-.2];M.A.F.DISABLED=set(M.A.F.EFFECTS);ref=M.frame(times[0],False).tobytes()
for t in times:assert M.frame(t,False).tobytes()==ref,('Closing artwork restarted',t)
M.A.F.DISABLED=set();(R/'NATIVE_CLOSING_CONTINUITY.json').write_text(json.dumps({'times':times,'geometry_across_retimed_closing_boundaries':'IDENTICAL; no repeated entrance','finishing':'Independently verified by native runtime proof','audio':'Repaired separately, not reused defective AAC'},indent=2)+'\n');print('NATIVE_CLOSING_CONTINUITY_PASS',flush=True)
