"""Batch source integrity checks; cannot certify art, motion or listening."""
from pathlib import Path
import hashlib,json,re,sys
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'engine'))
from sequence import validate_contract
from pre_render import validate_package
B=Path(__file__).resolve().parent
reports=[]
for slug in ['mint-cold-pilot','onion-tears-pilot','knuckle-pop-pilot','recorded-voice-pilot']:
 p=B/slug;c=json.loads((p/'sequence_contract.json').read_text());art=validate_contract(c,'artwork')
 try:validate_contract(c,'motion');blocked=False
 except ValueError:blocked=True
 m=json.loads((p/'package.json').read_text())
 changed=[i['path'] for i in m['inputs'] if hashlib.sha256((p/i['path']).read_bytes()).hexdigest()!=i['sha256']]
 n=(p/'NARRATION.md').read_text().split('\n\n')[2]
 norm=lambda s:re.sub(r'\W+','',s).lower()
 coverage=norm(' '.join(s['narration_phrase'] for s in c['shots']))==norm(n)
 ready=validate_package(p/'package.json')['ready']
 report={'episode':slug,'artwork_contract':art,'narration_coverage':coverage,'stale_input_hashes':changed,'unapproved_motion_blocked':blocked,'render_ready':ready}
 reports.append(report)
 if changed or not coverage or not blocked or ready:raise SystemExit(json.dumps(report))
r={'scope':'Text/source integrity only; not artistic approval','episodes':reports,'all_pass':True,'complete_new_movies':0}
(B/'REVISION_VERIFICATION_20261017.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r))
