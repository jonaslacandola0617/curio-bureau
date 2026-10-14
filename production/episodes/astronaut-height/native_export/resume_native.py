from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,json,os,sys,hashlib
B=Path(sys.argv[1]).resolve()
RENDER=str(Path(__file__).with_name('render-capture.cjs'))
def task(start):
 count=min(80,1172-start);out=B/f'frames_{start:04d}.mkv';config=B/f'request_{start:04d}.json'
 if out.exists():
  v=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,nb_read_frames','-of','json',str(out)]))['streams'][0]
  if (v['width'],v['height'],int(v.get('nb_read_frames',0)))==(2160,3840,count):return dict(start_frame=start,count=count,path=str(out),status='closed native frames')
  raise RuntimeError('Existing incomplete output: preserve it and inspect before rendering this range')
 cfg=dict(studio=str(B/'Studio.html'),mix=str(B/'project/assets/preflight_mix.wav'),chrome=str(B/'chrome-headless-shell-linux64/chrome-headless-shell'),scale=2,start_frame=start,start=start/30,frames=count,outputs=[dict(kind='lossless',path=str(out))],progress=str(B/f'progress_{start:04d}.json'))
 config.write_text(json.dumps(cfg))
 with (B/f'capture_{start:04d}.log').open('w') as log:subprocess.run(['node','--expose-gc',RENDER,str(config)],stdout=log,stderr=log,check=True)
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v:0','-show_entries','stream=width,height,nb_read_frames','-of','json',str(out)]))['streams'][0]
 assert (probe['width'],probe['height'],int(probe['nb_read_frames']))==(2160,3840,count)
 fd=os.open(out,os.O_RDONLY);os.fsync(fd);os.posix_fadvise(fd,0,0,os.POSIX_FADV_DONTNEED);os.close(fd)
 print('Verified native range',start,count,flush=True)
 return dict(start_frame=start,count=count,path=str(out),status='closed native frames')
assert hashlib.sha256((B/'project/assets/preflight_mix.wav').read_bytes()).hexdigest()=='12f6260a92de4e7999cf42e93e465c5287444f449cea7bc7f965f6a9e45c5f68'
with ThreadPoolExecutor(max_workers=2) as pool:segments=list(pool.map(task,range(0,1172,80)))
assert sum(s['count'] for s in segments)==1172
(B/'SEGMENT_QA.json').write_text(json.dumps(segments,indent=2))
print('All 1172 native frames verified',flush=True)
subprocess.run(['python',str(Path(__file__).with_name('finish_native.py')),str(B)],check=True)
