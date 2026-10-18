from pathlib import Path
import urllib.request,json,hashlib,sys
r=Path(__file__).resolve().parent
u='https://api.github.com/repos/jonaslacandola0617/curio-bureau/releases/tags/sun-disappeared-full-v1-review-20261018'
req=urllib.request.Request(u,headers={'Accept':'application/vnd.github+json','User-Agent':'Curio-Bureau-archive-verifier'})
d=json.loads(urllib.request.urlopen(req,timeout=25).read());assets={a['name']:a for a in d['assets']};receipts=[]
for name in sys.argv[1:]:
 a=assets.get(name);assert a is not None,(name,'not present');p=r/'chunks'/name if name.endswith('.mkv')else r/name if (r/name).is_file()else r/'audio'/name;digest=hashlib.sha256(p.read_bytes()).hexdigest();assert a['state']=='uploaded' and a['size']==p.stat().st_size and a.get('digest')=='sha256:'+digest,(name,a)
 record={'name':name,'asset_id':a['id'],'bytes':a['size'],'sha256':digest,'download_url':a['browser_download_url'],'observed_provider_digest':a['digest'],'state':a['state']};receipts.append(record)
 if name.endswith('.mkv'):
  fp=r/'chunks'/(name+'.json');c=json.loads(fp.read_text());c.update(archive_status='DURABLE',archive_receipt=record);fp.write_text(json.dumps(c,indent=2)+'\n')
all_chunks=[json.loads(p.read_text())for p in sorted((r/'chunks').glob('*.mkv.json'))];(r/'RECOVERY.json').write_text(json.dumps({'source_commit':'30cea6213c2d5a6005c8595ce1e8ddb21aaccdf2','release_id':d['id'],'release_url':d['html_url'],'total_frames':1485,'durable_frames':sum(c['count']for c in all_chunks if c['archive_status']=='DURABLE'),'status':'CAPTURING' if sum(c['count']for c in all_chunks if c['archive_status']=='DURABLE')<1485 else 'ALL_FRAMES_DURABLE','chunks':all_chunks},indent=2)+'\n')
(r/'qa/ARCHIVE_ASSETS_LATEST.json').write_text(json.dumps({'release_id':d['id'],'url':d['html_url'],'checked':receipts},indent=2)+'\n');print(json.dumps({'verified':[x['name']for x in receipts],'durable_frames':sum(c['count']for c in all_chunks if c['archive_status']=='DURABLE')},indent=2))
