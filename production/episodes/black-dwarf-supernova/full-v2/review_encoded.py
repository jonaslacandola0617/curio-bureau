"""Build a contact sheet and preserve actual runner evidence after public download."""
from pathlib import Path
import json,zipfile,hashlib,re
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent
with zipfile.ZipFile(r/'Black-Dwarf-Full-v2-QA.zip')as z:
 for name in ['FINISHING_RUNTIME_PROOF.json','PRECAPTURE_GATE.json','AUDIO_RECEIPT.json','NARRATION_TAIL_QA.json','ACCEPTANCE_LOOKBACK.json','RECOVERY.json']:
  b=z.read(name);p=r/'qa'/('CI_'+name);p.write_bytes(b)
 gate=json.loads(z.read('PRECAPTURE_GATE.json'));assert gate['decision']=='FULL_FILM_CAPTURE_ALLOWED_FOR_OWNER_REVIEW'
 recovery=json.loads(z.read('RECOVERY.json'));assert recovery['frames']==1747 and len(recovery['chunks'])==12
 assert recovery['chunks'][0]['start_frame']==0 and recovery['chunks'][-1]['end_frame_exclusive']==1747
 for a,b in zip(recovery['chunks'],recovery['chunks'][1:]):assert a['end_frame_exclusive']==b['start_frame']
 frames=sorted((r/'qa').glob('encoded-*.jpg'));assert len(frames)==29
 times=[0,1.8,3.4,5.2,6.8,8.6,9.8,11.5,13.2,14.6,16.3,17.9,19.5,23.8,28.7,31.9,34.9,39.5,42.8,44.5,46,47.8,49.5,51,52.6,54.2,55.8,57.433333,58.033333]
 for start in [0,15]:
  selected=frames[start:start+15];out=Image.new('RGB',(5*216,3*420),'#0D1C2B');d=ImageDraw.Draw(out)
  for j,p in enumerate(selected):
   x=j%5*216;y=j//5*420;im=Image.open(p).resize((216,384));out.paste(im,(x,y));d.text((x+8,y+393),str(round(times[start+j],3))+'s',fill='white')
  out.save(r/'qa'/f'ENCODED_CONTACT_{start//15+1}.jpg',quality=94)
 d=json.loads((r/'PUBLIC_DOWNLOAD_QA.json').read_text());log=(r/'qa/ENCODED_LOUDNESS.log').read_text();m=re.search(r'\{\s*"input_i".*?\}',log,re.S);levels=json.loads(m.group(0));d['encoded_audio_levels']={k:levels[k]for k in ['input_i','input_tp','input_lra']};d['source_commit']=recovery['source_commit'];d['recovery_chunks']=12;d['runner_gate']='PASS';d['encoded_visual_inspection']='29 checkpoints prepared; actual inspection pending';(r/'PUBLIC_DOWNLOAD_QA.json').write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'levels':d['encoded_audio_levels'],'frames':len(frames),'source':recovery['source_commit']}))
