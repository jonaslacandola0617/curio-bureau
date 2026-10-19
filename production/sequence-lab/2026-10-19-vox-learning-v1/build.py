from pathlib import Path
import subprocess,os,json,hashlib,zipfile
r=Path(__file__).resolve().parent;tag='vox-learning-black-dwarf-test-v1-20261019';target=os.environ['GITHUB_SHA'];repo=os.environ['GH_REPO']
def run(a):subprocess.run(a,check=True)
def get(a):return subprocess.check_output(a,text=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def upload(ps):run(['gh','release','upload',tag,*map(str,ps),'--repo',repo])
(r/'audio').mkdir(exist_ok=True)
for s in ['voice','music']:
 run(['gh','release','download','black-dwarf-full-v2-review-20261019','--repo',repo,'--pattern',f'Black-Dwarf-{s}-full-v2.flac','--dir',str(r/'audio')]);p=r/'audio'/f'Black-Dwarf-{s}-full-v2.flac';p.rename(r/'audio'/f'source-{s}.flac')
run(['python',str(r/'prepare.py')]);run(['node',str(r/'render.cjs'),'stills'])
run(['gh','release','create',tag,'--repo',repo,'--target',target,'--prerelease','--latest=false','--title','Vox learning — Black Dwarf visual test v1','--notes','Owner-requested 19.5-second visual proof, not a new complete episode or an approved release. Same specimen, dominant support comparison, fixed mass and descending limit, conditional contraction. Native1080×1920/30fps with12fps scene cadence, retained Bernard/score, existing designed SFX, textures, source-local focus and locked ending. Source: '+target])
chunks=[];records=[]
for start in range(0,585,150):
 end=min(start+150,585);p=r/f'Recovery-RGB-{start:04d}-{end-1:04d}.mkv';run(['node',str(r/'render.cjs'),'chunk',str(start),str(end),str(p)]);v=json.loads(get(['ffprobe','-v','error','-count_frames','-show_entries','stream=width,height,nb_read_frames','-of','json',str(p)]))['streams'][0];assert(v['width'],v['height'],int(v['nb_read_frames']))==(1080,1920,end-start);upload([p]);chunks.append(p);records.append({'name':p.name,'start':start,'end_exclusive':end,'sha256':sha(p),'bytes':p.stat().st_size})
(r/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'chunks':records},indent=2));upload([r/'RECOVERY.json'])
(r/'concat.txt').write_text(''.join("file '"+str(p)+"'\n" for p in chunks));movie=r/'Vox-Learning-Black-Dwarf-Test-v1-1080p.mp4'
run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',str(r/'concat.txt'),'-i',str(r/'audio/mix.wav'),'-map','0:v','-map','1:a','-frames:v','585','-r','30','-c:v','libx264','-preset','slow','-profile:v','high','-pix_fmt','yuv420p','-b:v','12M','-maxrate','16M','-bufsize','24M','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(movie)])
probe=json.loads(get(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(movie)]));v=next(x for x in probe['streams']if x['codec_type']=='video');assert(v['width'],v['height'],int(v['nb_read_frames']))==(1080,1920,585);upload([movie])
asset=next(x for x in json.loads(get(['gh','api','repos/'+repo+'/releases/tags/'+tag]))['assets']if x['name']==movie.name);assert asset['size']==movie.stat().st_size and asset['digest']=='sha256:'+sha(movie)
receipt={'source_commit':target,'status':'ARCHIVED_UNREVIEWED','tag':tag,'name':movie.name,'sha256':sha(movie),'bytes':movie.stat().st_size,'asset_id':asset['id'],'download_url':asset['browser_download_url'],'provider_digest':asset['digest'],'probe':probe}
(r/'ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2));upload([r/'ARCHIVE_RECEIPT.json',r/'AUDIO_RECEIPT.json'])
run(['ffmpeg','-nostdin','-v','error','-i',str(movie),'-f','null','-'])
with zipfile.ZipFile(r/'Visual-Test-QA.zip','w',zipfile.ZIP_DEFLATED)as z:
 for p in (r/'qa').glob('*.jpg'):z.write(p,'qa/'+p.name)
 for p in r.glob('*.json'):z.write(p,p.name)
upload([r/'Visual-Test-QA.zip']);print(json.dumps(receipt,indent=2))
