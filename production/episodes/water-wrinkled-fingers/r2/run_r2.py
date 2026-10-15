from pathlib import Path
import subprocess,json,hashlib,os,sys
r=Path(__file__).parent.resolve();node=os.environ['CODEX_PRIMARY_RUNTIME_NODE'];limit=240*1024*1024
for i in range(int(sys.argv[1]) if len(sys.argv)>1 else 0,7):
 with(r/f'chunks/batch_{i}.log').open('w')as log:subprocess.run([node,str(r/'render_chunks.cjs'),str(i)],stdout=log,stderr=subprocess.STDOUT,check=True)
 ds=json.loads((r/f'chunks/batch_{i}.json').read_text());uploads=[]
 for d in ds:
  p=Path(d['path']);d['parts']=[]
  if p.stat().st_size<=480*1024*1024:parts=[p]
  else:
   parts=[]
   with p.open('rb')as f:
    j=0
    while True:
     data=f.read(limit)
     if not data:break
     part=p.with_suffix(p.suffix+f'.part{j:03}');part.write_bytes(data);parts.append(part);j+=1
  for part in parts:
   d['parts'].append({'name':part.name,'bytes':part.stat().st_size,'sha256':hashlib.sha256(part.read_bytes()).hexdigest()});uploads.append({'local_path':str(part),'purpose':'create_library_file','library_artifact_type':'other'})
 (r/f'chunks/batch_{i}_manifest.json').write_text(json.dumps(ds,indent=2));req=r/f'chunks/parts_upload_{i}.json';req.write_text(json.dumps({'uploads':uploads}))
 with req.open('rb')as src,(r/f'chunks/receipt_{i}.json').open('wb')as out:subprocess.run(['python3',str(r.parent/'r2_helpers_current/library_upload.py')],stdin=src,stdout=out,check=True)
 receipt=json.loads((r/f'chunks/receipt_{i}.json').read_text());assert all(x['status']=='succeeded'and x['local_metadata_applied']for x in receipt['results'])
 subprocess.run(['python3',str(r/'checkpoint_r2.py')],check=True)
 for d in ds:
  for part in d['parts']:
   if '.part' in part['name']:(r/'chunks'/part['name']).unlink()
 print('SAVED_BATCH',i,flush=True)
