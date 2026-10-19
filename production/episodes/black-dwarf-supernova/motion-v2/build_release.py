from pathlib import Path
import subprocess,os,json,hashlib,math,zipfile
r=Path(__file__).resolve().parent; repo=r.parents[3]; tag='black-dwarf-motion-v2-review-20261019'; target=os.environ['GITHUB_SHA']
def run(a,**kw):return subprocess.run(a,check=True,**kw)
def read(a):return subprocess.check_output(a,text=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def upload(files):
 if files:run(['gh','release','upload',tag,*map(str,files),'--repo',os.environ['GH_REPO']])
def record(p,role):return {'name':p.name,'role':role,'bytes':p.stat().st_size,'sha256':digest(p),'source_commit':target}
for item in json.loads((r/'SOURCE_FINGERPRINT.json').read_text())['files']:
 assert digest(r/item['path'])==item['sha256'], 'Frozen source changed: '+item['path']
run(['python',str(r/'prepare.py')]);tl=json.loads((r/'timeline.json').read_text());run(['node',str(r/'qa.cjs')]);run(['node',str(r/'effect-proof.cjs')]);run(['python',str(r/'make_coverage.py')]);run(['python',str(r/'preflight.py')]);run(['node',str(r/'render.cjs'),'stills'])
run(['gh','release','create',tag,'--repo',os.environ['GH_REPO'],'--target',target,'--prerelease','--latest=false','--title','Black Dwarf — mechanism motion/sound review v2','--notes','Owner-approved static artwork developed into an isolated difficult mechanism preflight. Native 1080×1920/30fps, 12fps scene states, natural Bernard excerpt, original developing score and existing Curio action cues. Strong source-local materials and active optical/grain overlays. Moving/listening review PENDING; this is not a complete film. Source commit: '+target])
chunks=r/'chunks';chunks.mkdir(exist_ok=True);pending=[];records=[];closed=[]
try:
 for i,start in enumerate(range(0,tl['frames'],150)):
  end=min(start+150,tl['frames']);p=chunks/f'Black-Dwarf-v2-RGB-{i:02d}-{start:04d}-{end-1:04d}.mkv'
  run(['node',str(r/'render.cjs'),'chunk',str(start),str(end),str(p)])
  probe=json.loads(read(['ffprobe','-v','error','-count_frames','-show_entries','stream=width,height,nb_read_frames,pix_fmt','-of','json',str(p)]))['streams'][0]
  assert (probe['width'],probe['height'],int(probe['nb_read_frames']))==(1080,1920,end-start)
  records.append(dict(record(p,'lossless RGB recovery'),start_frame=start,end_frame_exclusive=end,decoded_frames=end-start));pending.append(p);closed.append(p)
  if len(pending)==2:upload(pending);pending=[]
finally:
 if pending:upload(pending)
(r/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':records,'format':'libx264rgb CRF0/rgb24; native lossless RGB recovery'},indent=2)+'\n');upload([r/'RECOVERY.json'])
concat=r/'concat.txt';concat.write_text(''.join("file '"+str(p)+"'\n" for p in closed))
movie=r/'Black-Dwarf-Motion-v2-1080p.mp4'
run(['ffmpeg','-nostdin','-v','error','-y','-f','concat','-safe','0','-i',str(concat),'-i',str(r/'audio/mix.wav'),'-map','0:v','-map','1:a','-frames:v',str(tl['frames']),'-r','30','-c:v','libx264','-preset','slow','-profile:v','high','-pix_fmt','yuv420p','-b:v','12M','-maxrate','16M','-bufsize','24M','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(movie)])
probe=json.loads(read(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(movie)]));v=next(s for s in probe['streams']if s['codec_type']=='video');assert(v['width'],v['height'],int(v['nb_read_frames']))==(1080,1920,tl['frames'])
assert v['pix_fmt']=='yuv420p' and v['r_frame_rate']=='30/1'
# Archive the closed movie immediately after basic integrity checks, before extended review.
upload([movie]);receipt=record(movie,'ARCHIVED_UNREVIEWED mechanism preflight');receipt['tag']=tag
(r/'OUTPUT_PROBE.json').write_text(json.dumps(probe,indent=2)+'\n')
run(['ffmpeg','-nostdin','-v','error','-i',str(movie),'-f','null','-'])
run(['ffmpeg','-nostdin','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-f','null','-'],stderr=(r/'qa/ENCODED_LOUDNESS.log').open('w'))
for i,t in enumerate([.5,4.8,8,9.75,12.75,15.9,20.5,22.5,24.8]):run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(r/'qa'/f'encoded-{i:02d}.jpg')])
assets=json.loads(read(['gh','api','repos/'+os.environ['GH_REPO']+'/releases/tags/'+tag]))['assets'];remote=next(x for x in assets if x['name']==movie.name);assert remote['size']==receipt['bytes'];assert remote.get('digest')=='sha256:'+receipt['sha256'];receipt.update({'asset_id':remote['id'],'download_url':remote['browser_download_url'],'provider_digest':remote['digest'],'uploaded_size':remote['size'],'status':'ARCHIVED_UNREVIEWED','owner_motion_review':'PENDING','human_listening':'NOT CLAIMED','caption_alignment':'actual-audio ASR estimates; independent verification pending'})
(r/'ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
for name in ['voice','music','sfx','mix']:run(['ffmpeg','-nostdin','-v','error','-y','-i',str(r/'audio'/f'{name}.wav'),'-c:a','flac',str(r/f'Black-Dwarf-{name}-v2.flac')])
z=r/'Black-Dwarf-Motion-v2-QA.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED)as f:
 for p in list((r/'qa').glob('*'))+list(r.glob('*.json'))+list(r.glob('*.md')):f.write(p,p.relative_to(r))
upload([r/'ARCHIVE_RECEIPT.json',r/'OUTPUT_PROBE.json',r/'FINISHING_RUNTIME_PROOF.json',r/'AUDIO_RECEIPT.json',r/'SFX_CUE_SHEET.json',r/'timeline.json',z,*r.glob('Black-Dwarf-*-v2.flac')])
print(json.dumps(receipt,indent=2))
