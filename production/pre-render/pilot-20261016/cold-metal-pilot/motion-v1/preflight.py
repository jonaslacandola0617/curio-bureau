from pathlib import Path
import importlib.util,json
r=Path(__file__).resolve().parent;e=r.parents[3]/'engine'
def module(name):
 s=importlib.util.spec_from_file_location('cold_'+name,e/(name+'.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
module('sequence').validate_contract(json.loads((r.parent/'sequence_contract.json').read_text()),'motion')
module('finishing_contract').validate_finishing(json.loads((r/'preview-config.json').read_text()),r,'artwork')
a=module('finishing_audit').check(r/'FINISHING_COVERAGE.json')
if not a['execution_records_pass']:raise ValueError('Finishing audit blocked: '+'; '.join(a['errors']))
print('Pre-capture: owner art record, finishing declaration, actual proof and current source hashes PASS; motion/listening owner review pending.')
