from pathlib import Path
import json,hashlib,subprocess,re,concurrent.futures
from PIL import Image,ImageDraw
r=Path(__file__).resolve().parent;rows=json.loads((r/'PUBLIC_ASSETS.json').read_text());ts=[0,1.6,2.8,3.8,4.8,5.8,6.8,7.8,8.5,9.6,10.5,11.8]
def review(row):
 out=r/row['id'];movie=out/row['name'];assert hashlib.sha256(movie.read_bytes()).hexdigest()==row['digest'][7:];assert movie.stat().st_size==row['bytes'];receipt=json.loads((out/'ARCHIVE_RECEIPT.json').read_text());assert receipt['sha256']==row['digest'][7:] and receipt['source_commit']=='cd566912c93eba1e529e20f9d45e8962acf94b72'
 probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-count_frames','-show_streams','-show_format','-of','json',str(movie)]));v=next(x for x in probe['streams']if x['codec_type']=='video');a=next(x for x in probe['streams']if x['codec_type']=='audio');assert (v['width'],v['height'],v['r_frame_rate'],int(v['nb_read_frames']))==(1080,1920,'30/1',360);assert abs(float(probe['format']['duration'])-12)<.001;assert a['sample_rate']=='48000'and a['channels']==2
 subprocess.run(['ffmpeg','-v','error','-i',str(movie),'-f','null','-'],check=True)
 dest=out/'encoded-review';dest.mkdir(exist_ok=True)
 for t in ts:subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(dest/f'{t:g}.jpg')],check=True)
 # Dense joins inspect source-to-model changes; selected seek times are requested times, not inferred edit boundaries.
 dense=[2.8,3.1,3.4,3.7,4.0,4.3]if row['id']=='03-shrimp'else[4.2,4.5,4.8,5.1,5.4,5.7]if row['id']=='04-brine'else[6.8,7.1,7.4,7.7,8.0,8.3]if row['id']=='01-concrete'else[5.6,5.9,6.2,6.5,6.8,7.1]
 for t in dense:subprocess.run(['ffmpeg','-v','error','-y','-ss',str(t),'-i',str(movie),'-frames:v','1',str(dest/f'dense-{t:g}.jpg')],check=True)
 sheet=Image.new('RGB',(1080,1230),'#111b25');dr=ImageDraw.Draw(sheet)
 for i,t in enumerate(ts):
  im=Image.open(dest/f'{t:g}.jpg').resize((216,384));xx=i%5*216;yy=i//5*410;sheet.paste(im,(xx,yy));dr.text((xx+5,yy+385),str(t),fill='white')
 sheet.save(out/'ENCODED_CONTACT.jpg',quality=90)
 sheet=Image.new('RGB',(1296,410),'#111b25');dr=ImageDraw.Draw(sheet)
 for i,t in enumerate(dense):sheet.paste(Image.open(dest/f'dense-{t:g}.jpg').resize((216,384)),(i*216,0));dr.text((i*216+5,385),str(t),fill='white')
 sheet.save(out/'ENCODED_JOIN.jpg',quality=90)
 log=subprocess.run(['ffmpeg','-hide_banner','-i',str(movie),'-af','loudnorm=I=-14:TP=-1.5:LRA=8:print_format=json','-f','null','-'],text=True,capture_output=True,check=True);m=json.loads(re.findall(r'\{[^{}]*\}',log.stderr)[-1]);(out/'ENCODED_LOUDNESS.json').write_text(json.dumps(m,indent=2))
 report={'topic':row['id'],'download_url':row['url'],'public_download_verified':True,'bytes':row['bytes'],'sha256':row['digest'][7:],'provider_digest':row['digest'],'source_commit':receipt['source_commit'],'native_dimensions':[1080,1920],'fps':'30/1','decoded_frames':360,'duration_seconds':float(probe['format']['duration']),'complete_decode':'PASS','codecs':{'video':v['codec_name'],'pixel_format':v['pix_fmt'],'audio':a['codec_name'],'sample_rate':a['sample_rate'],'channels':a['channels']},'encoded_loudness':m,'encoded_review_times':ts,'dense_join_requested_times':dense,'scene_fps_implementation':12,'ending':'Exact shared brand source, real30fps; sampled at11.8s','caption_timing':'Scribe actual-audio words, no independent forced alignment claim','owner_creative_approval':'PENDING','independent_phone_headphone_listening':'NOT CLAIMED'};(out/'PUBLIC_DOWNLOAD_QA.json').write_text(json.dumps(report,indent=2));print(row['id'],'12.000s /360frames /full decode /public SHA matched',flush=True);return report
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(2)as ex:reports=list(ex.map(review,rows))
 (r/'PUBLIC_DOWNLOAD_QA.json').write_text(json.dumps({'tests':reports},indent=2))
