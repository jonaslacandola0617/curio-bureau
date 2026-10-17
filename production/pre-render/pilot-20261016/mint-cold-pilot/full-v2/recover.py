from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,hashlib,json,sys
r=Path(__file__).parent
pairs=[tuple(map(int,s.split(':')))for s in sys.argv[1:]]
def run(ab):
 a,b=ab;p=r/'chunks'/f'Mint-v2-lossless-{a:04}-{b-1:04}.mkv';d=json.loads(subprocess.check_output(['ffprobe','-v','error','-threads','2','-count_frames','-show_entries','stream=width,height,nb_read_frames','-of','json',str(p)]))['streams'][0];assert(d['width'],d['height'],int(d['nb_read_frames']))==(1080,1920,b-a);h=hashlib.sha256()
 with p.open('rb')as f:
  for z in iter(lambda:f.read(8388608),b''):h.update(z)
 return {'file':p.name,'start_frame':a,'count':b-a,'codec':'ffv1','lossless':True,'bytes':p.stat().st_size,'sha256':h.hexdigest(),'archive_status':'VERIFIED_LOCAL_ARCHIVE_PENDING'}
with ThreadPoolExecutor(2)as ex:rows=list(ex.map(run,pairs))
p=r/'RECOVERY.json';d=json.loads(p.read_text())if p.exists()else{'source_commit':'0f897eccd22931966f31b3f371608a0945266992','total_frames':1201,'chunks':[]};d['chunks']=[c for c in d['chunks']if c['start_frame']not in [x[0]for x in pairs]]+rows;p.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps(rows))
