from pathlib import Path
import json,math,subprocess,numpy as np
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent;R=P/'review/encoded';R.mkdir(parents=True,exist_ok=True);tl=json.loads((P/'timeline.json').read_text());movie=P/'Curio-Immune-Defense-Full-Review-v4.mp4';bound=tl['scene_boundaries'];start=math.ceil((bound[6]+.85)*30);end=round(tl['ending_start']*30);count=end-start
raw=subprocess.check_output(['ffmpeg','-v','error','-ss',str(start/30),'-i',str(movie),'-frames:v',str(count),'-vf','crop=1080:240:0:690,scale=540:120','-an','-f','rawvideo','-pix_fmt','rgb24','-']);a=np.frombuffer(raw,dtype=np.uint8).reshape(-1,120,540,3).astype(np.float32);assert len(a)==count
mask=(a[:,:,:,0]>a[:,:,:,1]*1.08)&(a[:,:,:,1]>a[:,:,:,2]*1.08)&(a[:,:,:,0]>120)&(a[:,:,:,1]>65);edges=[]
for frame in mask:
 cols=np.where(frame.sum(axis=0)>5)[0];assert len(cols)>10;edges.append(int(cols[0]))
displacement=2*(max(edges)-min(edges));jump=int(2*max(abs(np.diff(edges))));assert displacement<=4
report={'scope':'Every actual decoded held-closing frame of retimedV4; original entrance and exact endcard fade excluded from zero-motion expectation','start':start/30,'end':end/30,'frames':count,'max_hand_displacement_native_pixels':displacement,'max_adjacent_jump_native_pixels':jump,'verdict':'NO_REPEATED_CLOSING_ENTRANCE','retimed_narration_beats':bound[7:9],'audio':'Verified separately from new speech; defective V3 AAC not reused'};(R/'CLOSING_FRAME_CHECK.json').write_text(json.dumps(report,indent=2)+'\n')
times=[bound[6]+.3,bound[6]+1,bound[7]-.1,bound[7]+.1,bound[7]+.4,bound[7]+.8,bound[8]-.1,bound[8]+.1,bound[8]+.4,bound[8]+.8,tl['voice_duration']-.15,tl['voice_duration']+.15,tl['ending_start'],tl['ending_start']+.3,tl['duration']-.05];board=Image.new('RGB',(1500,1665),(13,28,43))
for i,t in enumerate(times):
 f=R/f'close-{t:.2f}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(f)],check=True);x=i%5*300;y=i//5*555;board.paste(Image.open(f).convert('RGB').resize((300,533)),(x,y));ImageDraw.Draw(board).text((x+8,y+535),f'{t:.2f}s',fill='white')
board.save(R/'closing-restored-encoded.jpg',quality=94,subsampling=0);print(json.dumps(report),flush=True)
