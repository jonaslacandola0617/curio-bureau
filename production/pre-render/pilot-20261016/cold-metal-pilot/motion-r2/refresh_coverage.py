from pathlib import Path
import json,hashlib
r=Path(__file__).resolve().parent;p=r/'FINISHING_COVERAGE.json';d=json.loads(p.read_text())
for item in d['sources']:
 item['sha256']=hashlib.sha256((r/item['path']).read_bytes()).hexdigest()
for item in d['coverage'].values():
 for e in item.get('evidence',[]):e['sha256']=hashlib.sha256((r/e['path']).read_bytes()).hexdigest()
d['scope']='R2 representative sequence; native execution checked separately by native_proof.cjs, not a completed full-film release'
d['owner_motion_review']='Owner requested R2 correction and 4K; revised motion awaiting review'
d['coverage']['focus_hunt']['active_window']='2.78–3.12s; resolves before Touch it'
d['coverage']['sequence_continuity']['active_window']='contact settles 2.64s → paper 2.78–3.16s → continuous heat strokes 3.88s → comparison 6.60s'
p.write_text(json.dumps(d,indent=2)+'\n')
