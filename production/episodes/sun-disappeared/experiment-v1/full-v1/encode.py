from pathlib import Path
import json,subprocess,hashlib
r=Path(__file__).resolve().parent;records=[json.loads(p.read_text())for p in sorted((r/'chunks').glob('*.mkv.json'))];at=0
for c in records:
 assert c['start_frame']==at,(c['file'],at);assert c['archive_status']=='DURABLE',c['file'];at=c['end_frame']+1
assert at==1485,at
(r/'concat.txt').write_text(''.join("file 'chunks/"+c['file']+"'\n"for c in records))
cmd=['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',str(r/'concat.txt'),'-i',str(r/'Sun-Full-Mix-v1.flac'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-profile:v','high','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','320k','-movflags','+faststart',str(r/'00-Sun-Disappeared-1080p-Full-Review-v1.mp4')]
(r/'ENCODE_COMMAND.json').write_text(json.dumps(cmd,indent=2)+'\n');subprocess.run(cmd,check=True)
p=r/'00-Sun-Disappeared-1080p-Full-Review-v1.mp4';subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True);(r/'OUTPUT_LOCAL.json').write_text(json.dumps({'status':'ENCODED_ARCHIVE_PENDING','file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'source_commit':'30cea6213c2d5a6005c8595ce1e8ddb21aaccdf2','frames':1485,'duration':49.5},indent=2)+'\n');print((r/'OUTPUT_LOCAL.json').read_text())
