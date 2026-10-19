from pathlib import Path
import subprocess,os,json,hashlib,math,zipfile
r=Path(__file__).resolve().parent; repo=r.parents[3]; tag='black-dwarf-full-v1-review-20261019'; target=os.environ['GITHUB_SHA']
def run(a,**kw):return subprocess.run(a,check=True,**kw)
def read(a):return subprocess.check_output(a,text=True)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def upload(files):
 if files:run(['gh','release','upload',tag,*map(str,files),'--repo',os.environ['GH_REPO']])
def record(p,role):return {'name':p.name,'role':role,'bytes':p.stat().st_size,'sha256':digest(p),'source_commit':target}
for item in json.loads((r/'SOURCE_FINGERPRINT.json').read_text())['files']:
 assert digest(r/item['path'])==item['sha256'], 'Frozen source changed: '+item['path']
run(['python',str(r/'prepare.py')]);tl=json.loads((r/'timeline.json').read_text());run(['node',str(r/'qa.cjs')]);run(['python',str(r/'make_coverage.py')]);run(['python',str(r/'preflight.py')]);run(['node',str(r/'render.cjs'),'stills'])
run(['gh','release','create',tag,'--repo',os.environ['GH_REPO'],'--target',target,'--prerelease','--latest=false','--title','Black Dwarf — complete film review v1','--notes','Complete original black-dwarf episode, integrating owner-approved art and motion v2. Native 1080×1920/30fps, 12fps scene states, complete natural Bernard narration, original developing score and existing Curio action cues. Strong source-local materials and active optical/grain overlays. Full-film owner review and independent listening/caption alignment PENDING; no social publication. Source commit: '+target])
chunks=r/'chunks';chunks.mkdir(exist_ok=True);pending=[];records=[];closed=[]
try:
 for i,start in enumerate(range(0,tl['frames'],150)):
  end=min(start+150,tl['frames']);p=chunks/f'Black-Dwarf-Full-v1-RGB-{i:02d}-{start:04d}-{end-1:04d}.mkv'
  run(['node',str(r/'render.cjs'),'chunk',str(start),str(end),str(p)])
  probe=json.loads(read(['ffprobe','-v','error','-count_frames','-show_entries','stream=width,height,nb_read_frames,pix_fmt','-of','json',str(p)]))['streams'][0]
  assert (probe['width'],probe['height'],int(probe['nb_read_frames']))==(1080,1920,end-start)
  records.append(dict(record(p,'lossless RGB recovery'),start_frame=start,end_frame_exclusive=end,decoded_frames=end-start));pending.append(p);closed.append(p)
  if len(pending)==2:upload(pending);pending=[]
finally:
 if pending:upload(pending)
(r/'RECOVERY.json').write_text(json.dumps({'source_commit':target,'frames':tl['frames'],'chunks':records,'format':'libx264rgb CRF0/rgb24; native lossless RGB recovery'},indent=2)+'\n');upload([r/'RECOVERY.json'])
concat=r/'concat.txt';concat.write_text(''.join("file '"+str(p)+"'\n" for p in closed))
movie=r/'Black-Dwarf-Full-v1-1080p.mp4'
run(['ffmpeg','-nostdin','-v','error','-y','-f','concat','-safe','0','-i',str(concat),'-i',str(r/'audio/mix.wav'),'-map','0:v','-map','1:a','-frames:v',str(tl['frames']),'-r','30','-c:v','libx264','-preset','slow','-profile:v','high','-pix_fmt','yuv420p','-b:v','12M','-maxrate','16M','-bufsize','24M','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(movie)])
probe=json.loads(read(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(movie)]));v=next(s for s in probe['streams']if s['codec_type']=='video');assert(v['width'],v['height'],int(v['nb_read_frames']))==(1080,1920,tl['frames'])
assert v['pix_fmt']=='yuv420p' and v['r_frame_rate']=='30/1'
# Archive the closed movie immediately after basic integrity checks, before extended review.
upload([movie]);receipt=record(movie,'ARCHIVED_UNREVIEWED complete film');receipt['tag']=tag
(r/'OUTPUT_PROBE.json').write_text(json.dumps(probe,indent=2)+'\n')
run(['ffmpeg','-nostdin','-v','error','-i',str(movie),'-f','null','-'])
run(['ffmpeg','-nostdin','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-f','null','-'],stderr=(r/'qa/ENCODED_LOUDNESS.log').open('w'))
for i,t in enumerate([0,1.8,3.4,5.2,6.8,8.6,9.8,11.5,13.2,14.6,16.3,17.9,19.5,23.8,28.7,31.9,34.9,39.5,42.8,44.5,46,47.8,49.5,51,52.6,54.2,55.8,tl['duration']-.8,tl['duration']-.2]):run(['ffmpeg','-nostdin','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(r/'qa'/f'encoded-{i:02d}.jpg')])
assets=json.loads(read(['gh','api','repos/'+os.environ['GH_REPO']+'/releases/tags/'+tag]))['assets'];remote=next(x for x in assets if x['name']==movie.name);assert remote['size']==receipt['bytes'];assert remote.get('digest')=='sha256:'+receipt['sha256'];receipt.update({'asset_id':remote['id'],'download_url':remote['browser_download_url'],'provider_digest':remote['digest'],'uploaded_size':remote['size'],'status':'ARCHIVED_UNREVIEWED','owner_motion_review':'APPROVED v2','owner_full_review':'PENDING','human_listening':'NOT CLAIMED','caption_alignment':'actual-audio ASR estimates; independent verification pending'})
(r/'ARCHIVE_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
for name in ['voice','music','sfx','mix']:run(['ffmpeg','-nostdin','-v','error','-y','-i',str(r/'audio'/f'{name}.wav'),'-c:a','flac',str(r/f'Black-Dwarf-{name}-full-v1.flac')])
run(['python',str(r/'lookback.py')]);z=r/'Black-Dwarf-Full-v1-QA.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED)as f:
 for p in list((r/'qa').glob('*'))+list(r.glob('*.json'))+list(r.glob('*.md')):f.write(p,p.relative_to(r))
upload([r/'ARCHIVE_RECEIPT.json',r/'OUTPUT_PROBE.json',r/'FINISHING_RUNTIME_PROOF.json',r/'AUDIO_RECEIPT.json',r/'SFX_CUE_SHEET.json',r/'timeline.json',z,*r.glob('Black-Dwarf-*-full-v1.flac')])
print(json.dumps(receipt,indent=2))
