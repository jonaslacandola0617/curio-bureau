"""Verify the public archived bytes; do not treat checks as owner creative/listening approval."""
from pathlib import Path
import urllib.request,json,hashlib,subprocess,zipfile
r=Path(__file__).resolve().parent;tag='black-dwarf-motion-v2-review-20261019'
with urllib.request.urlopen('https://api.github.com/repos/jonaslacandola0617/curio-bureau/releases/tags/'+tag,timeout=45)as f:release=json.load(f)
required=['Black-Dwarf-Motion-v2-1080p.mp4','ARCHIVE_RECEIPT.json','Black-Dwarf-Motion-v2-QA.zip']
receipt=[]
for name in required:
 a=next(x for x in release['assets']if x['name']==name)
 p=r/name
 if not p.is_file() or p.stat().st_size!=a['size']:
  with urllib.request.urlopen(a['browser_download_url'],timeout=120)as f:p.write_bytes(f.read())
 sha=hashlib.sha256(p.read_bytes()).hexdigest()
 assert p.stat().st_size==a['size'] and a['digest']=='sha256:'+sha
 receipt.append({'name':name,'asset_id':a['id'],'bytes':a['size'],'sha256':sha,'provider_digest':a['digest'],'public_download_verified':True,'url':a['browser_download_url']})
q=r/'qa/encoded';q.mkdir(parents=True,exist_ok=True)
with zipfile.ZipFile(r/'Black-Dwarf-Motion-v2-QA.zip')as z:
 for name in z.namelist():
  if name.startswith('qa/') and '..' not in Path(name).parts:
   p=r/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(z.read(name))
p=r/required[0]
probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(p)]))
v=next(s for s in probe['streams']if s['codec_type']=='video');a=next(s for s in probe['streams']if s['codec_type']=='audio')
assert(v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']),v['pix_fmt'])==(1080,1920,'30/1',781,'yuv420p')
assert a['codec_name']=='aac' and a['sample_rate']=='48000' and a['channels']==2
subprocess.run(['ffmpeg','-nostdin','-v','error','-i',str(p),'-f','null','-'],check=True)
data={'status':'ARCHIVED_UNREVIEWED','download_verification':receipt,'video':{'width':v['width'],'height':v['height'],'fps':v['r_frame_rate'],'frames':int(v['nb_read_frames']),'codec':v['codec_name'],'profile':v['profile'],'pixel_format':v['pix_fmt'],'duration':v['duration']},'audio':{'codec':a['codec_name'],'sample_rate':a['sample_rate'],'channels':a['channels'],'duration':a['duration']},'full_decode':'PASS','encoded_visual_inspection':'PENDING','owner_motion_review':'PENDING','independent_listening':'NOT CLAIMED','word_alignment':'actual-audio ASR estimates, independently verified alignment PENDING'}
(r/'PUBLIC_DOWNLOAD_QA.json').write_text(json.dumps(data,indent=2)+'\n');print(json.dumps(data,indent=2))
