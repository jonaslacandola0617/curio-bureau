from pathlib import Path
import json,hashlib,sys
r=Path(__file__).resolve().parent;sys.path.insert(0,str(r.parents[2]/'engine'))
from production_standard import validate_standard
from finishing_contract import validate_finishing
from finishing_audit import check
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def run():
 for f in json.loads((r/'SOURCE_FINGERPRINT.json').read_text())['files']:assert h(r/f['path'])==f['sha256'],'Frozen input changed: '+f['path']
 c=json.loads((r/'episode.json').read_text());tl=json.loads((r/'timeline.json').read_text());p=json.loads((r/'FINISHING_RUNTIME_PROOF.json').read_text())
 assert p['renderer_inputs']=={'scenes':h(r/'scenes.cjs'),'approved_source':h(r/'../motion-v2/render.cjs'),'brand':h(r/'../../../engine/browser/brand.js')}
 assert not p['errors'] and len(p['effects'])==11 and all(e['execution']=='PASS' for e in p['effects'])
 assert all(e['equal']for e in p['approved_passage_identity']) and p['ending']['fully_shown_pixel_identical']
 tail=json.loads((r/'NARRATION_TAIL_QA.json').read_text());assert tail['protected_tail_after_all_retained_source']>=.75 and not tail['voice_fade']
 result={'standard':validate_standard(c,r,tl['duration']),'finishing':validate_finishing(c,r,stage='release',studio_path=r/'render.cjs',expected_size=[1080,1920]),'coverage':check(r/'FINISHING_COVERAGE.json')}
 assert result['coverage']['execution_records_pass'],result
 result['decision']='FULL_FILM_CAPTURE_ALLOWED_FOR_OWNER_REVIEW';(r/'PRECAPTURE_GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':run()
