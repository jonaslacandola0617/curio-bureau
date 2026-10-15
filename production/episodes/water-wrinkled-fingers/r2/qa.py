from pathlib import Path
import subprocess,json,hashlib,re
r=Path(__file__).parent.resolve();qa={'profile':{'width':2160,'height':3840,'fps':30,'frames':1089,'duration':36.3},'files':[],'narration':json.loads((r/'NARRATION_TAIL_QA.json').read_text()),'scope':'Technical checks do not substitute for owner listening or artistic judgment. R2 finishing correction explicitly ordered; original audio preserved. R1 finishing rejected; new R2 not yet owner-reviewed.'}
for p in (r/'delivered').iterdir():
 if p.suffix not in ['.mp4','.webm']:continue
 d=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]));v=next(s for s in d['streams']if s['codec_type']=='video');a=next(s for s in d['streams']if s['codec_type']=='audio');assert(v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']))==(2160,3840,'30/1',1089);assert a['sample_rate']=='48000'and a['channels']==2
 subprocess.run(['ffmpeg','-v','error','-i',str(p),'-f','null','-'],check=True)
 loud=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-vn','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True,check=True).stderr;(r/'checks'/('loudness_'+p.name+'.txt')).write_text(loud);summary=loud.split('Summary:')[-1];lufs=float(re.search(r'I:\s+(-?[\d.]+) LUFS',summary).group(1));peak=float(re.search(r'Peak:\s+(-?[\d.]+) dBFS',summary).group(1));assert -14.0<=lufs<=-12 and peak<=-1
 qa['files'].append({'name':p.name,'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'video_codec':v['codec_name'],'audio_codec':a['codec_name'],'decoded_frames':1089,'full_decode':'passed','lufs':lufs,'true_peak_dbfs':peak,'duration':d['format']['duration']});print(qa['files'][-1],flush=True)
(r/'delivered/Wrinkled_Fingers_QA.json').write_text(json.dumps(qa,indent=2))
