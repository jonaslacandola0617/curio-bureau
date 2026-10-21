from pathlib import Path
import json,hashlib,urllib.request
P=Path(__file__).resolve().parent;A=P/'assets';A.mkdir(exist_ok=True)
for r in json.loads((P/'SOURCE_DOWNLOADS.json').read_text()):
 p=A/r['path']
 if not p.exists():
  with urllib.request.urlopen(r['url'],timeout=60)as src,open(p,'wb')as out:
   while b:=src.read(1048576):out.write(b)
 assert hashlib.sha256(p.read_bytes()).hexdigest()==r['sha256'],str(p)+' source hash mismatch'
print('All three original public source objects verified')
