from pathlib import Path
import subprocess,json,hashlib
r=Path(__file__).parent;tl=json.loads((r/'timeline.json').read_text());d=json.loads((r/'RECOVERY.json').read_text());chunks=sorted(d['chunks'],key=lambda c:c['start_frame']);pos=0
for c in chunks:
 assert c['start_frame']==pos and c['archive_status']=='DURABLE';pos+=c['count']
assert pos==tl['frames']
fingerprint=json.loads((r/'SOURCE_FINGERPRINT.json').read_text())
for f in fingerprint['files']:
 p=r/f['path'];assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f['path']
(r/'concat.txt').write_text(''.join("file '"+str((r/'chunks'/c['file']).resolve())+"'\n"for c in chunks))
out=r/'00-Mint-1080p-Review-v2.mp4'
args=['ffmpeg','-nostdin','-y','-hide_banner','-loglevel','warning','-threads','2','-f','concat','-safe','0','-i',str(r/'concat.txt'),'-i',str(r/'audio/mix.wav'),'-map','0:v:0','-map','1:a:0','-vf','format=gbrpf32le,zscale=pin=bt709:tin=iec61966-2-1:min=gbr:rin=full:p=bt709:t=bt709:m=bt709:r=limited,format=yuv420p','-r','30','-c:v','libx264','-preset','medium','-threads','2','-profile:v','high','-b:v','12M','-maxrate','16M','-bufsize','24M','-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart','-t',str(tl['duration']),str(out)]
(r/'ENCODE_COMMAND.json').write_text(json.dumps({'source_commit':fingerprint['source_commit'],'argv':args,'colour':'Explicit sRGB full-range RGB to BT709 SDR limited-range YUV conversion; no HDR'},indent=2)+'\n');subprocess.run(args,check=True)
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(out)]));v=next(x for x in probe['streams']if x['codec_type']=='video');a=next(x for x in probe['streams']if x['codec_type']=='audio');assert(v['width'],v['height'],v['r_frame_rate'],int(v['nb_frames']))==(1080,1920,'30/1',tl['frames']);assert a['sample_rate']=='48000'and a['channels']==2
receipt={'status':'ENCODED_ARCHIVE_PENDING','file':out.name,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'source_commit':fingerprint['source_commit'],'frames':int(v['nb_frames']),'duration':probe['format']['duration'],'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'native':[1080,1920],'fps':30,'owner_motion_review':'PENDING','owner_whole_film_review':'PENDING'};(r/'OUTPUT.json').write_text(json.dumps(receipt,indent=2)+'\n');(r/'FFPROBE.json').write_text(json.dumps(probe,indent=2)+'\n');print(json.dumps(receipt),flush=True)
