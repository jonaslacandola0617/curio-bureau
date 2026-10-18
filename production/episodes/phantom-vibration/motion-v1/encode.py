from pathlib import Path
import json,subprocess,hashlib
r=Path(__file__).resolve().parent;tl=json.loads((r/'timeline.json').read_text());rec=json.loads((r/'RECOVERY.json').read_text());chunks=sorted(rec['chunks'],key=lambda x:x['start']);cursor=0
for c in chunks:
 assert c['start']==cursor and c['archive_status']=='DURABLE', 'Capture coverage or archive incomplete'
 p=r/c['file'];assert hashlib.sha256(p.read_bytes()).hexdigest()==c['sha256'];cursor=c['end']
assert cursor==tl['frames']
(r/'concat.txt').write_text(''.join("file '"+str((r/c['file']).resolve())+"'\n" for c in chunks))
out=r/'00-Phantom-Vibration-1080p-Review-v1.mp4'
cmd=['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',str(r/'concat.txt'),'-i',str(r/'Phantom-Mix-v1.flac'),'-map','0:v:0','-map','1:a:0','-c:v','libx264','-preset','slow','-crf','18','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-r','30','-frames:v',str(tl['frames']),'-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(out)]
(r/'ENCODE_COMMAND.json').write_text(json.dumps({'command':cmd,'source_mix_sha256':hashlib.sha256((r/'Phantom-Mix-v1.flac').read_bytes()).hexdigest(),'role':'complete owner-review candidate; unchanged approved bytes may become posting copy'},indent=2)+'\n');subprocess.run(cmd,check=True)
(r/'OUTPUT.json').write_text(json.dumps({'file':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'frames':tl['frames'],'duration':tl['duration'],'width':1080,'height':1920,'fps':30,'archive_status':'ENCODED_ARCHIVE_PENDING','owner_full_review':'PENDING'},indent=2)+'\n');print((r/'OUTPUT.json').read_text())
