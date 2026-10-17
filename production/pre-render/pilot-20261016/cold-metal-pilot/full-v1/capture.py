from pathlib import Path
import subprocess,json,hashlib,os
r=Path(__file__).parent;t=json.loads((r/'timeline.json').read_text());chunk=r/'preview-chunks';chunk.mkdir(exist_ok=True);w=int(os.environ.get('CURIO_PREVIEW_WIDTH','720'));sig=hashlib.sha256(b''.join((r/f).read_bytes()for f in ['render.cjs','scene-core.cjs','timeline.json'])+str(w).encode()).hexdigest();receipts=[]
for start in range(0,t['frames'],45):
 end=min(start+45,t['frames']);p=chunk/f'{start:04}-{end:04}-{w}.mp4';receipt=p.with_suffix('.json');valid=False
 if p.exists()and receipt.exists():
  old=json.loads(receipt.read_text());valid=old.get('source')==sig and old.get('sha256')==hashlib.sha256(p.read_bytes()).hexdigest()
 if not valid:
  subprocess.run(['node',str(r/'render.cjs'),'worker',str(start),str(end),str(w),str(p)],check=True)
  receipt.write_text(json.dumps({'start':start,'end_exclusive':end,'source':sig,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}))
 receipts.append(json.loads(receipt.read_text()));(r/'PREVIEW_PROGRESS.json').write_text(json.dumps({'frames_done':end,'frames_total':t['frames'],'preview_width':w,'full_movie_complete':end==t['frames'],'source':sig,'chunks':receipts},indent=2))
 print(f'Complete preview: {end}/{t["frames"]} frames',flush=True)
concat=chunk/'concat.txt';concat.write_text(''.join("file '"+str((chunk/f'{a:04}-{min(a+45,t["frames"]):04}-{w}.mp4').resolve())+"'\n"for a in range(0,t['frames'],45)))
output=r/f'Cold_Metal_Full_Review_{w}.mp4';subprocess.run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',str(concat),'-i',str(r/'audio/mix.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','256k','-ar','48000','-t',str(t['duration']),'-movflags','+faststart',str(output)],check=True);print(output,flush=True)
