from pathlib import Path
import subprocess,json,sys,time,hashlib
r=Path(__file__).parent.resolve();node=__import__('os').environ['CODEX_PRIMARY_RUNTIME_NODE'];batch=int(sys.argv[1])
while not(r/'chunks/batch_0.json').exists():time.sleep(2)
for i in range(batch,7):
 if i:
  with (r/f'chunks/batch_{i}.log').open('w')as log:subprocess.run([node,str(r/'render_chunks.cjs'),str(i)],stdout=log,stderr=subprocess.STDOUT,check=True)
 receipt=r/f'chunks/receipt_{i}.json'
 if not receipt.exists():
  with (r/f'chunks/upload_{i}.json').open('rb')as src,receipt.open('wb')as out:subprocess.run(['python3',str(r/'helpers/library_upload.py')],stdin=src,stdout=out,check=True)
 d=json.loads(receipt.read_text());assert all(x['status']=='succeeded'and x['local_metadata_applied'] for x in d['results']),d
 subprocess.run(['python3',str(r/'checkpoint.py')],check=True)
 print('DURABLE_BATCH',i,flush=True)
