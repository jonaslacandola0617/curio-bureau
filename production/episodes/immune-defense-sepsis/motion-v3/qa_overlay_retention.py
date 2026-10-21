from pathlib import Path
import math,json,subprocess
import numpy as np
from PIL import Image
import render_movie as M
P=Path(__file__).resolve().parent;R=P/'review/encoded';R.mkdir(parents=True,exist_ok=True);movie=P/'Curio-Immune-Defense-Full-Review-v3.mp4'
cases=[('moving_grain',3.8,(60,600,950,920),'Microscopy source, foreground grain'),('material_texture',12.6,(80,1080,980,1640),'Light vessel/junction material, independent paper')]
out=[]
for effect,t,roi,label in cases:
 tick=math.floor((round(t*30)/30+1e-8)*12)/12
 M.A.F.DISABLED=set();on=np.asarray(M.frame(tick).crop(roi),dtype=np.float32)
 M.A.F.DISABLED={effect};off=np.asarray(M.frame(tick).crop(roi),dtype=np.float32);M.A.F.DISABLED=set()
 f=R/f'retention-{effect}.png';subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(f)],check=True);enc=np.asarray(Image.open(f).convert('RGB').crop(roi),dtype=np.float32)
 weights=np.array([.2126,.7152,.0722]);native=((on-off)*weights).sum(axis=2).ravel();encoded=((enc-off)*weights).sum(axis=2).ravel();corr=float(np.corrcoef(native,encoded)[0,1])
 out.append({'effect':effect,'time':t,'ROI':roi,'subject':label,'native_mean_abs_luma_difference':float(np.abs(native).mean()),'encoded_residual_correlation':corr})
(R/'OVERLAY_RETENTION.json').write_text(json.dumps({'method':'Same-time native effect-on minus off, correlated with decoded MP4 minus same off baseline; no perceptual pass threshold or artistic score inferred','cases':out},indent=2)+'\n');print(json.dumps(out))
