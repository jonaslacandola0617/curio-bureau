from pathlib import Path
import subprocess,os,json,hashlib,zipfile,sys
r=Path(__file__).resolve().parent;repo=r.parents[2];id=sys.argv[1];out=r/id;target=os.environ['GITHUB_SHA'];ghrepo=os.environ['GH_REPO'];mapnames={'01-concrete':('roman-concrete','Roman-Concrete'),'02-diomede':('diomede-date-line','Diomede-Date-Line'),'03-shrimp':('pistol-shrimp','Pistol-Shrimp'),'04-brine':('underwater-brine-lake','Underwater-Brine-Lake')};slug,name=mapnames[id];tag='visual-test-'+slug+'-v1-20261020'
def run(a):subprocess.run(a,check=True)
def get(a):return subprocess.check_output(a,text=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def upload(ps):run(['gh','release','upload',tag,*map(str,ps),'--repo',ghrepo])
for x in json.loads((r/'SOURCE_LOCK.json').read_text())['files']:assert sha(repo/x['path'])==x['sha256'], 'Changed source '+x['path']
run(['python',str(r/'prepare_audio.py'),id]);run(['node',str(r/'render.cjs'),'stills',id])
run(['gh','release','create',tag,'--repo',ghrepo,'--target',target,'--prerelease','--latest=false','--title',name.replace('-',' ')+' — original 12-second visual test v1','--notes','Owner-requested new-topic visual proof. Exactly360 native1080×1920 frames at30fps;12fps explanatory scene states and exact shared ending. Original subject-specific art/sequence, natural narration, new short score, existing designed action sounds, source-local focus and material overlays. Internal review does not imply owner approval. Source commit: '+target])
chunks=[];records=[]
for start in range(0,360,120):
 end=start+120;p=out/f'{name}-RGB-{start:03d}-{end-1:03d}.mkv';run(['node',str(r/'render.cjs'),'chunk',id,str(start),str(end),str(p)]);v=json.loads(get(['ffprobe','-v','error','-count_frames','-show_entries','stream=width,height,nb_read_frames','-of','json',str(p)]))['streams'][0];assert (v['width'],v['height'],int(v['nb_read_frames']))==(1080,1920,120);upload([p]);records.append({'name':p.name,'start_frame':start,'end_exclusive':end,'bytes':p.stat().st_size,'sha256':sha(p)});chunks.append(p)
(out/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':360,'chunks':records,'format':'Native lossless RGB libx264rgb CRF0'},indent=2));upload([out/'RECOVERY.json'])
(out/'concat.txt').write_text(''.join("file '"+str(p)+"'\n" for p in chunks));movie=out/f'Curio-Test-{id[:2]}-{name}-12s-v1.mp4'
run(['ffmpeg','-nostdin','-y','-v','error','-f','concat','-safe','0','-i',str(out/'concat.txt'),'-i',str(out/'mix.wav'),'-map','0:v','-map','1:a','-frames:v','360','-t','12','-r','30','-c:v','libx264','-preset','slow','-profile:v','high','-pix_fmt','yuv420p','-b:v','12M','-maxrate','16M','-bufsize','24M','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(movie)])
probe=json.loads(get(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(movie)]));v=next(s for s in probe['streams']if s['codec_type']=='video');assert(v['width'],v['height'],int(v['nb_read_frames']),v['r_frame_rate'])==(1080,1920,360,'30/1');assert abs(float(probe['format']['duration'])-12)<.05
upload([movie])
remote=next(a for a in json.loads(get(['gh','api','repos/'+ghrepo+'/releases/tags/'+tag]))['assets']if a['name']==movie.name);assert remote['size']==movie.stat().st_size and remote['digest']=='sha256:'+sha(movie)
receipt={'topic':id,'tag':tag,'source_commit':target,'status':'ARCHIVED_UNREVIEWED','name':movie.name,'bytes':movie.stat().st_size,'sha256':sha(movie),'asset_id':remote['id'],'provider_digest':remote['digest'],'download_url':remote['browser_download_url'],'probe':probe};(out/'ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2));upload([out/'ARCHIVE_RECEIPT.json',out/'AUDIO_RECEIPT.json'])
run(['ffmpeg','-v','error','-i',str(movie),'-f','null','-'])
for t in [0,1.6,2.8,3.8,4.8,5.8,6.8,7.8,8.5,9.4,10.5,11.8]:run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(out/'qa'/f'encoded-{t}.jpg')])
with zipfile.ZipFile(out/'QA.zip','w',zipfile.ZIP_DEFLATED)as z:
 for p in (out/'qa').glob('*.jpg'):z.write(p,'qa/'+p.name)
 for p in list(out.glob('*.json'))+[r/'SOURCE_LOCK.json',r/'README.md',r/'CASE_CONTRACTS.json',r/'ASSETS.json']:z.write(p,p.name)
upload([out/'QA.zip']);print(json.dumps(receipt,indent=2))
