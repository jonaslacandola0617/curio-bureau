from pathlib import Path
import subprocess,json,hashlib
r=Path(__file__).parent.resolve();out=r/'delivered';metas=sorted((r/'chunks').glob('frames_*.mkv.json'),key=lambda p:json.loads(p.read_text())['start_frame']);end=0;lines=[]
for p in metas:
 d=json.loads(p.read_text());assert d['start_frame']==end;end+=d['count'];v=Path(d['path']);assert hashlib.sha256(v.read_bytes()).hexdigest()==d['sha256'];lines.append("file '"+str(v)+"'")
assert end==1089;assert json.loads((r/'recovery.json').read_text())['locally_verified_frames']==1089
(r/'chunks/concat.txt').write_text('\n'.join(lines)+'\n')
common=['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(r/'chunks/concat.txt'),'-i',str(r/'audio/full_mix.wav'),'-map','0:v','-map','1:a','-frames:v','1089','-t','36.3','-vf','setpts=N/(30*TB),scale=in_range=pc:out_range=tv:out_color_matrix=bt709,format=yuv420p','-color_range','tv','-colorspace','bt709','-color_primaries','bt709','-color_trc','iec61966-2-1','-r','30','-fps_mode','cfr','-ar','48000','-ac','2']
for name,opts in [
 ('Wrinkled_Fingers_4K_Master.mp4',['-c:v','libx264','-preset','fast','-threads','4','-crf','15','-c:a','aac','-b:a','320k','-movflags','+faststart']),
 ('Wrinkled_Fingers_4K_Posting.mp4',['-c:v','libx264','-preset','fast','-threads','4','-crf','18','-maxrate','60M','-bufsize','120M','-c:a','aac','-b:a','320k','-movflags','+faststart']),
 ('Wrinkled_Fingers_4K.webm',['-c:v','libvpx-vp9','-deadline','realtime','-cpu-used','6','-threads','4','-row-mt','1','-crf','22','-b:v','0','-c:a','libopus','-b:a','256k'])]:
 p=out/name;print('ENCODING',name,flush=True);subprocess.run(common+opts+[str(p)],check=True);print('ENCODED',name,p.stat().st_size,flush=True)
