"""Recover byte-pinned source micrographs/fonts; hand is committed original artwork."""
from pathlib import Path
import urllib.request,hashlib,json
P=Path(__file__).resolve().parent;A=P/'assets';A.mkdir(exist_ok=True)
urls={'neutrophil-mrsa.jpg':'https://upload.wikimedia.org/wikipedia/commons/0/01/Human_neutrophil_ingesting_MRSA.jpg','neutrophil-detail.jpg':'https://upload.wikimedia.org/wikipedia/commons/8/8f/Neutrophil_MRSA_II.jpg','Playfair900.ttf':'https://raw.githubusercontent.com/jonaslacandola0617/curio-bureau/cddd2f4d7acb42ea1562684e00fcc56eda5d199b/production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets/Playfair900.ttf','Manrope.ttf':'https://raw.githubusercontent.com/jonaslacandola0617/curio-bureau/cddd2f4d7acb42ea1562684e00fcc56eda5d199b/production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets/Manrope.ttf'}
for item in json.loads((P/'ASSETS.json').read_text())['assets']:
 q=A/item['file']
 if not q.exists():
  if item['file']not in urls:raise RuntimeError('Missing committed original asset: '+item['file'])
  req=urllib.request.Request(urls[item['file']],headers={'User-Agent':'CurioBureauResearch/1.0 (educational source review)'});q.write_bytes(urllib.request.urlopen(req,timeout=60).read())
 assert q.stat().st_size==item['bytes'],q
 assert hashlib.sha256(q.read_bytes()).hexdigest()==item['sha256'],q
 print('VERIFIED',q.name)
