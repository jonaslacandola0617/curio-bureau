from pathlib import Path
import sys,json,math,subprocess,hashlib
import numpy as np
from PIL import Image,ImageDraw
import render_art as A
P=Path(__file__).resolve().parent;ROOT=P.parents[3];TL=json.loads((P/'timeline.json').read_text());W,H=1080,1920

def frame(t,caption=True):
 qt=math.floor((t+1e-8)*12)/12
 k=min(len(TL['scene_art'])-1,max(i for i,b in enumerate(TL['scene_boundaries'][:-1])if qt>=b));u=qt-TL['scene_boundaries'][k];scene=TL['scene_art'][k]
 A.MOTION=True;A.U=u;A.CL=A.S((u-.6)/2)if scene==3 else 1
 im=A.raw(scene,qt,False)
 if caption:
  c=next((c for c in TL['captions']if c['start']<=t<c['end']),None)
  if c:A.cap(im,c['text'])
 return im

def composed(n,caption=True):
 if n>=round(TL['ending_start']*30):return Image.open(P/'ending'/f'{n-round(TL["ending_start"]*30):03}.png').convert('RGB')
 return frame(math.floor((n/30+1e-8)*12)/12,caption)

def capture(start,end,file):
 sys.path.insert(0,str(ROOT/'production/engine'))
 from finishing_contract import validate_finishing
 from production_standard import validate_standard
 from finishing_audit import check
 config=json.loads((P/'episode.json').read_text())
 validate_finishing(config,P,stage='release',studio_path=P/'render_movie.py',expected_size=[1080,1920]);validate_standard(config,P,TL['duration'])
 result=check(P/'FINISHING_COVERAGE.json');assert result['execution_records_pass'],result
 proc=subprocess.Popen(['ffmpeg','-v','error','-y','-f','rawvideo','-pixel_format','rgb24','-s','1080x1920','-r','30','-i','-','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',str(file)],stdin=subprocess.PIPE)
 last=-1;buf=None
 for n in range(start,end):
  tick=math.floor((n/30+1e-8)*12)
  if n>=round(TL['ending_start']*30)or tick!=last:buf=composed(n).tobytes();last=tick
  proc.stdin.write(buf)
 proc.stdin.close();assert proc.wait()==0
 print('CLOSED_NATIVE_CHUNK',start,end,flush=True)
if __name__=='__main__':
 if '--chunk'in sys.argv:capture(int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
 else:
  R=P/'review';R.mkdir(exist_ok=True)
  ts=[.3,1.7]+[b+.4 for b in TL['scene_boundaries'][1:-1]]+[TL['scene_boundaries'][2]+2.5,TL['scene_boundaries'][3]+1.5,TL['ending_start']-.2]
  for j,t in enumerate(ts):frame(t).save(R/f'frame-{j:02}-{t:.2f}.jpg',quality=94,subsampling=0)
  frame(TL['ending_start']-.04).save(P/'ending-base.png')
  print('Native demanding states',len(ts))
