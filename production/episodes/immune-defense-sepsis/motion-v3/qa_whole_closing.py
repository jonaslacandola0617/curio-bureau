from pathlib import Path
import subprocess,json,numpy as np
P=Path(__file__).resolve().parent;movie=P/'Curio-Immune-Defense-Full-Review-v3.mp4';start=31.6;duration=13.0
b=subprocess.check_output(['ffmpeg','-v','error','-ss',str(start),'-i',str(movie),'-t',str(duration),'-vf','crop=1080:240:0:690,scale=540:120','-an','-f','rawvideo','-pix_fmt','rgb24','-']);a=np.frombuffer(b,dtype=np.uint8).reshape(-1,120,540,3).astype(np.float32)
mask=(a[:,:,:,0]>a[:,:,:,1]*1.08)&(a[:,:,:,1]>a[:,:,:,2]*1.08)&(a[:,:,:,0]>120)&(a[:,:,:,1]>65);edges=[]
for frame in mask:
 cols=np.where(frame.sum(axis=0)>5)[0];assert len(cols)>10;edges.append(int(cols[0]))
displacement=2*(max(edges)-min(edges));jump=int(2*max(abs(np.diff(edges))));assert len(edges)==390;assert displacement<=4,displacement
report={'scope':'Every delivered frame of the entire held closing composition after its original entrance settles, before the exact ending begins','start':31.6,'end_exclusive':44.6,'frames_checked':len(edges),'fps':30,'max_hand_displacement_native_pixels':displacement,'max_adjacent_jump_native_pixels':jump,'verdict':'NO_REPEATED_HAND_ENTRANCE_DURING_ENTIRE_CLOSING_HOLD','excluded':'The original motivated entrance31–31.6s and exact endcard crossfade44.6–45.7s are inspected in picture boards, not treated as erroneous motion','sound':'Unchanged AAC; no independent audition claim'}
(P/'review/encoded/WHOLE_CLOSING_FRAME_CHECK.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
