from pathlib import Path
import subprocess,json,hashlib,sys
B=Path(sys.argv[1]).resolve();SRC=B/'segments.txt';MIX=B/'project/assets/preflight_mix.wav';D=1172/30;reports={}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
assert digest(MIX)=='12f6260a92de4e7999cf42e93e465c5287444f449cea7bc7f965f6a9e45c5f68'
# Remux recovered readable prefixes into fully closed, video-only containers.
segments=json.loads((B/'SEGMENT_QA.json').read_text())
for seg in segments:
 if seg['status']=='verified native prefix':
  dest=Path(seg['path']).with_name(Path(seg['path']).stem+'_closed.mkv');subprocess.run(['ffmpeg','-y','-v','error','-i',seg['path'],'-map','0:v:0','-c:v','copy',str(dest)],check=True);seg['path']=str(dest);seg['status']='closed, recovered native prefix'
SRC.write_text('\n'.join("file '"+s['path']+"'" for s in segments)+'\n');(B/'SEGMENT_QA.json').write_text(json.dumps(segments,indent=2))
for kind,name in [('master','Astronaut_Height_4K_Master.mp4'),('webm','Astronaut_Height_4K.webm'),('upload','Astronaut_Height_4K_Upload.mp4')]:
 p=B/name;args=['ffmpeg','-y','-v','error','-filter_threads','2','-threads','2','-f','concat','-safe','0','-i',str(SRC),'-i',str(MIX),'-map','0:v:0','-map','1:a:0','-vf','setpts=N/(30*TB)','-r','30','-t',str(D),'-color_primaries','bt709','-color_trc','iec61966-2-1']
 if kind=='webm':args+=['-c:v','libvpx-vp9','-deadline','realtime','-cpu-used','6','-threads','2','-row-mt','1','-crf','22','-b:v','0','-pix_fmt','yuv420p','-c:a','libopus','-b:a','256k','-ar','48000','-ac','2']
 else:
  args+=['-c:v','libx264','-preset','fast','-threads','4','-rc-lookahead','10','-x264-params','sync-lookahead=0','-crf','15' if kind=='master' else '20','-pix_fmt','yuv420p']
  if kind=='upload':args+=['-maxrate','48000k','-bufsize','96000k']
  args+=['-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-moov_size','65536']
 print('Encoding',name,flush=True);subprocess.run(args+[str(p)],check=True)
 print('Verifying',name,flush=True);probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));v=next(x for x in probe['streams'] if x['codec_type']=='video');a=next(x for x in probe['streams'] if x['codec_type']=='audio');assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']),int(a['sample_rate']),a['channels'])==(2160,3840,'30/1',1172,48000,2);assert abs(float(probe['format']['duration'])-D)<.08
 assert v['codec_name']==('vp9' if kind=='webm' else 'h264');assert a['codec_name']==('opus' if kind=='webm' else 'aac')
 subprocess.run(['ffmpeg','-v','error','-xerror','-threads','2','-i',str(p),'-f','null','-'],check=True)
 meter=subprocess.run(['ffmpeg','-hide_banner','-threads','2','-i',str(p),'-vn','-af','loudnorm=I=-13:TP=-1.5:LRA=8:print_format=json','-f','null','-'],capture_output=True,text=True,check=True);stats=json.loads(meter.stderr[meter.stderr.rfind('{'):]);assert float(stats['input_tp'])<=-1;assert abs(float(stats['input_i'])-(-14.46))<.35
 if kind=='upload':assert p.stat().st_size<512*1024*1024
 reports[name]={'resolution':[2160,3840],'fps':30,'frames':1172,'duration':float(probe['format']['duration']),'codecs':[v['codec_name'],a['codec_name']],'audio':[48000,2],'full_decode':'PASS','LUFS':float(stats['input_i']),'true_peak_dBTP':float(stats['input_tp']),'size':p.stat().st_size,'sha256':digest(p)}
 (B/'Native_QA.json').write_text(json.dumps({'status':'Owner-approved R2 picture/sound; native technical outputs passed','outputs':reports,'native_source':'Actual 2160x3840 Canvas, exact one-to-one lossless screenshot parity at three states, lossless RGB intermediates; no 1080p upscale','approved_mix_sha256':digest(MIX),'audio_note':'Owner-approved R2 level (~-14.46 LUFS) preserved on resolution-only delivery, slightly below the nominal -14 LUFS target. Both delivery codecs measured independently.','caption_basis':'Approved R2 actual-audio ASR phrases retained; not newly independent word-listening certified.'},indent=2)+'\n');print('PASS',name,p.stat().st_size,flush=True)
print('Native MP4, WebM and upload MP4 complete',flush=True)
