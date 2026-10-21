from pathlib import Path
import json,subprocess,numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;R=P/'review/encoded';R.mkdir(parents=True,exist_ok=True)
def track(movie):
 # Read EVERY delivered frame of both formerly broken joins; source skin hue isolates hand from ivory paper.
 b=subprocess.check_output(['ffmpeg','-v','error','-ss','37.8','-i',str(movie),'-t','4.6','-vf','crop=1080:240:0:690,scale=540:120','-an','-f','rawvideo','-pix_fmt','rgb24','-'])
 a=np.frombuffer(b,dtype=np.uint8).reshape(-1,120,540,3).astype(np.float32);mask=(a[:,:,:,0]>a[:,:,:,1]*1.08)&(a[:,:,:,1]>a[:,:,:,2]*1.08)&(a[:,:,:,0]>120)&(a[:,:,:,1]>65)
 edges=[]
 for frame in mask:
  cols=np.where(frame.sum(axis=0)>5)[0];assert len(cols)>10;edges.append(int(cols[0]))
 return {'start':37.8,'frames_checked':len(edges),'sample_fps':30,'hand_left_edge_half_resolution':edges,'max_displacement_native_pixels':2*(max(edges)-min(edges)),'max_adjacent_jump_native_pixels':int(2*max(abs(np.diff(edges))))}
if __name__=='__main__':
 import sys
 new=P/'Curio-Immune-Defense-Full-Review-v3.mp4';old=P.parent/'motion-v2/Curio-Immune-Defense-Full-Review-v2.mp4'
 if '--control-only'in sys.argv:
  report=track(old);(R/'V2_FAILURE_CONTROL.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items()if 'edge'not in k}));assert report['max_displacement_native_pixels']>100
 else:
  v2=track(old);v3=track(new);assert v2['max_displacement_native_pixels']>100;assert v3['max_displacement_native_pixels']<=4,v3
  times=[31.3,37.9,38.2,38.3,38.4,38.6,38.9,39.1,40.9,41.2,41.3,41.5,41.8,42,44.3,44.6,44.9,45.3];board=Image.new('RGB',(1440,1350),(13,28,43))
  for i,t in enumerate(times):
   f=R/f'close-{t:.2f}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(new),'-frames:v','1',str(f)],check=True);x=i%6*240;y=i//6*450;board.paste(Image.open(f).convert('RGB').resize((240,426)),(x,y));ImageDraw.Draw(board).text((x+8,y+430),f'{t:.2f}s',fill='white')
  board.save(R/'closing-continuity-encoded.jpg',quality=94,subsampling=0)
  report={'defect':'Repeated same-art narration boundaries restarted hand entrance','V2_failure_control':v2,'V3_corrected':v3,'verdict':'NO_REPEATED_HAND_ENTRANCE_ACROSS_BOTH_JOINS','scope':'All138 delivered frames across37.8–42.4s checked; board covers closing entry, both joins, final word hold and original logo transition. This is not independent listening or full-film owner approval.'};(R/'CLOSING_CONTINUITY_QA.json').write_text(json.dumps(report,indent=2)+'\n');print('ENCODED_CLOSING_CONTINUITY_PASS',flush=True)
