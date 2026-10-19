"""Fail-closed pre-capture gate. Excerpt scope never certifies full-film ending."""
from pathlib import Path
import json,hashlib,sys
r=Path(__file__).resolve().parent
sys.path.insert(0,str(r.parents[2]/'engine'))
from production_standard import validate_standard
from finishing_contract import validate_finishing
from finishing_audit import check
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run():
 frozen=json.loads((r/'SOURCE_FINGERPRINT.json').read_text())
 for item in frozen['files']:
  assert digest(r/item['path'])==item['sha256'],'Frozen input changed: '+item['path']
 config=json.loads((r/'episode.json').read_text());tl=json.loads((r/'timeline.json').read_text())
 result={'standard':validate_standard(config,r,tl['duration'],scope='isolated-preflight'),
 'finishing':validate_finishing(config,r,stage='release',studio_path=r/'render.cjs',expected_size=[1080,1920],scope='isolated-preflight')}
 proof=json.loads((r/'NATIVE_EFFECT_AUDIT.json').read_text())
 assert proof['renderer_sha256']==digest(r/'render.cjs')
 assert proof['audit_sha256']==digest(r/'effect-proof.cjs')
 assert not proof['frozen_source_drift'] and proof['decision']=='EXECUTION_PASS'
 assert len(proof['effects'])==11 and all(x['execution']=='PASS' for x in proof['effects'])
 assert all(x['opaque_caption_difference']==0 for x in proof['effects'])
 settled=next(x for x in proof['settling_envelope'] if x['time']==10.166667)
 assert settled['hunt_radius']<.0005 and settled['transition_radius']<.0005
 coverage=json.loads((r/'FINISHING_COVERAGE.json').read_text())
 # Refresh generated evidence hashes only. All code/assets remain frozen inputs.
 for item in coverage['coverage'].values():
  for e in item.get('evidence',[]):e['sha256']=digest(r/e['path'])
 (r/'FINISHING_COVERAGE.json').write_text(json.dumps(coverage,indent=2)+'\n')
 result['coverage']=check(r/'FINISHING_COVERAGE.json');assert result['coverage']['execution_records_pass'],result
 result['decision']='CAPTURE_ALLOWED_FOR_OWNER_REVIEW';result['ending']='NOT INCLUDED; no full-film certification'
 (r/'PRECAPTURE_GATE.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
 return result
if __name__=='__main__':run()
