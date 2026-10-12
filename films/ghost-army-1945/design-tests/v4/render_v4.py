#!/usr/bin/env python3
"""Curio Bureau Ghost Army V4. Distinct real frames at 1080x1920 24fps, source-grounded images.
V4 is an art-direction review, not the v1.3 required 2160x3840 30fps final episode."""
import base64,io,json,math,os,pathlib,random,subprocess,time,wave,zipfile
import numpy as np, requests
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright

ROOT=pathlib.Path(__file__).resolve().parent
ASSETS=ROOT/'assets';ASSETS.mkdir(exist_ok=True)
OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
DUR,FPS=16,24
SOURCES={
 'tank':('Ghost Army dummy tank, International Spy Museum.jpg','https://commons.wikimedia.org/wiki/File:Ghost_Army_dummy_tank,_International_Spy_Museum.jpg','CC0, ArtemisiaGentileschiFan, October 2025. This is a museum display, NOT a 1940s operational photo.'),
 'halftrack':('M3A1 Halftrack.jpg','https://commons.wikimedia.org/wiki/File:M3A1_Halftrack.jpg','U.S. Army 1944 technical manual, public domain. Vehicle-type reference, NOT a photo of the Ghost Army sonic equipment.'),
 'radio':('SCR-610.jpg','https://commons.wikimedia.org/wiki/File:SCR-610.jpg','U.S. Army technical manual TM 11-487, October 1944, public domain. Period radio-type reference, NOT verified as 23rd inventory.')
}
session=requests.Session()
session.headers.update({'User-Agent':'CurioBureauEditorialResearch/1.0 (noncommercial sourcing; GitHub Actions; original direct-attribution video)'})
for name,(filename,url,license_text) in SOURCES.items():
 dest=ASSETS/(name+'.jpg')
 # Retrieve author-provided Commons file by its exact file name; don't rely on unverified URL paths.
 api='https://commons.wikimedia.org/w/api.php'
 q={'action':'query','format':'json','prop':'imageinfo','iiprop':'url','titles':'File:'+filename}
 errors=[]
 candidates=[]
 try:
  v=session.get(api,params=q,timeout=45);v.raise_for_status()
  pages=v.json()['query']['pages']
  obj=next(iter(pages.values()))
  candidates.append(obj['imageinfo'][0]['url'])
 except Exception as e:errors.append(str(e))
 from urllib.parse import quote
 candidates.append('https://commons.wikimedia.org/wiki/Special:Redirect/file/'+quote(filename))
 for remote in candidates:
  try:
   print('SOURCE',name,remote,flush=True)
   resp=session.get(remote,timeout=80);resp.raise_for_status()
   im=Image.open(io.BytesIO(resp.content));im.load()
   assert im.width>400 and im.height>230,(im.width,im.height)
   im.convert('RGB').save(dest,'JPEG',quality=93,subsampling=0,optimize=True)
   print('SOURCE OK',name,im.size,dest.stat().st_size,flush=True)
   break
  except Exception as e:errors.append(str(e))
 else: raise RuntimeError('Unable to obtain attribution-checked image '+name+' failures='+str(errors))

sources_text='# Curio Bureau V4 — sourced imagery and factual caveats\n\n'
for name,(fn,url,lic) in SOURCES.items():sources_text+=f'- **{name}** [{fn}]({url}): {lic}\n'
sources_text+="""
- All three files were fetched by exact Wikimedia Commons filename at render time. Output JPGs have lossless-subject editing only through re-encoding; cropping, grading and typography are original Curio decisions.
- **Important:** The 2025 museum photo is a modern exhibition photo. The War Department half-track and radio photos are generic equipment references. These three images must not be relabeled as genuine photographs of Ghost Army operations.
- The map is an **original schematic** and makes no claims about exact deployment or troop movement. Düsseldorf/Cologne region positioning is merely geographic context.
- Unit comparison: a rounded ∼1,100 real Ghost Army members and ∼30,000-person force that could be simulated. National WWII Museum: https://www.nationalww2museum.org/visit/museum-campus-guide/hall-democracy/senator-john-alario-jr-special-exhibition-hall/ghost-army ; https://www.nationalww2museum.org/media/press-releases/national-wwii-museum-unveils-new-special-exhibit-ghost-army-combat-con-artists
- The "observer" and radio ticks in the video are explanatory symbols, not depicted historical intercepted traffic.
- Reference films/tutorials were studied for transferable visual grammar. No original Vox frames, audio, animations, logo, or graphical designs were inserted.
"""
(ROOT/'SOURCES.md').write_text(sources_text,encoding='utf8')

src=(ROOT/'visual_match.html').read_text(encoding='utf8')
fdir=ROOT.parent.parent/'assets'
css=''
for family,fn in [('Playfair Display','PlayfairDisplay.ttf'),('Manrope','Manrope.ttf')]:
 f=fdir/fn
 if f.exists():
  b64=base64.b64encode(f.read_bytes()).decode()
  css+=f'@font-face{{font-family:"{family}";src:url(data:font/ttf;base64,{b64}) format("truetype");font-weight:100 900;}}\n'
browser_source=src.replace('/*LOCAL_FONTS*/',css)
(OUT/'renderer_private.html').write_text(browser_source,encoding='utf8')
editable_source=src.replace('/*LOCAL_FONTS*/','@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Playfair+Display:wght@500;600;700&display=swap");')
(OUT/'CURIO_GHOST_ARMY_V4_EDITABLE.html').write_text(editable_source,encoding='utf8')

rate=48000
tt=np.arange(DUR*rate)/rate
snd=.004*np.sin(2*np.pi*51*tt)+.003*np.sin(2*np.pi*81*tt)
snd+=.002*np.sin(2*np.pi*137*tt)*np.sin(2*np.pi*.23*tt)
rng=np.random.default_rng(20261012)
def transient(at,base=100,amp=.07,l=.32):
 global snd
 n=int(l*rate);ix=int(at*rate)
 if ix+n>len(snd):n=len(snd)-ix
 if n<=0:return
 q=np.arange(n)/rate
 snd[ix:ix+n]+=amp*np.exp(-q*15)*np.sin(2*np.pi*(base*q+70*q*q))
def broadband(at,duration=.25,amp=.012):
 ix=int(at*rate);nn=min(len(snd)-ix,int(rate*duration))
 if nn<=0:return
 white=rng.normal(0,1,nn)
 # A soft textured paper accent, NOT the sound of the historic operation
 white=np.convolve(white,np.ones(23)/23,mode='same')
 enve=np.sin(np.linspace(0,np.pi,nn))**1.3
 snd[ix:ix+nn]+=white*enve*amp
for ev in [(1.22,171,.032,.2),(3.2,85,.070,.28),(4.3,62,.055,.4),(6.2,103,.070,.3),(7.12,370,.024,.18),(9.2,65,.06,.35),(10.55,185,.038,.22),(12.8,95,.065,.3),(13.35,166,.034,.24)]:
 transient(*ev)
for x in [1.25,3.25,6.4,9.24,12.83]:broadband(x,.22,.05)
# Clearly synthetic sonic-deception hint; not an authentic historical recording.
m=(tt>3.6)&(tt<4.8)
snd[m]+=.013*np.sin(2*np.pi*(76+7*np.sin(3*tt[m]))*tt[m])*np.sin(np.pi*(tt[m]-3.6)/1.2)**2
m=(tt>6.52)&(tt<7.65)
snd[m]+=.014*rng.normal(0,1,np.sum(m))*np.sin(np.pi*(tt[m]-6.52)/1.13)**2
snd=np.tanh(snd*1.5)*.76
audio=OUT/'CURIO_GHOST_ARMY_V4_SOUND_DESIGN.wav'
with wave.open(str(audio),'wb') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(rate)
 a=np.stack((snd,snd*.98),axis=-1)
 w.writeframes((a*32767).astype('<i2').tobytes())
print('SOUND READY',flush=True)
start=time.time()
cmd=['ffmpeg','-y','-nostdin','-loglevel','error','-f','image2pipe','-framerate',str(FPS),'-vcodec','png','-i','pipe:0',
 '-an','-c:v','libx264','-preset','veryfast','-crf','18','-pix_fmt','yuv420p','-movflags','+faststart','-r',str(FPS),
 '-frames:v',str(DUR*FPS),str(OUT/'silent.mp4')]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
contact=[]
checks=[8,25,51,75,88,105,127,156,174,195,215,235,254,272,301,326,350,381]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu-sandbox'])
 page=browser.new_page(viewport={'width':650,'height':2040},device_scale_factor=2)
 page.goto((OUT/'renderer_private.html').as_uri(),wait_until='domcontentloaded',timeout=120000)
 page.wait_for_function('window.renderReady === true',timeout=120000)
 page.add_style_tag(content='main{margin:0!important;padding:0!important}#film{width:540px!important;height:960px!important}main>div,main>p{display:none!important}')
 for n in range(DUR*FPS):
  page.evaluate('(t)=>window.renderAt(t)',n/FPS)
  snap=page.locator('#film').screenshot(type='png',animations='disabled',timeout=120000)
  if n==0:
   img=Image.open(io.BytesIO(snap))
   assert img.size==(1080,1920),('Wrong screenshot size',img.size)
  proc.stdin.write(snap)
  if n in checks:
   thumb=Image.open(io.BytesIO(snap)).convert('RGB');thumb.thumbnail((270,480))
   contact.append((n/FPS,thumb.copy()))
  if n%24==0:print('FRAME',n,'/',DUR*FPS,'wallsec',round(time.time()-start),flush=True)
 browser.close()
proc.stdin.close()
if proc.wait()!=0:raise RuntimeError('ffmpeg silent render failed')
mp4=OUT/'CURIO_GHOST_ARMY_VISUAL_MATCH_V4_WITH_AUDIO.mp4'
webm=OUT/'CURIO_GHOST_ARMY_VISUAL_MATCH_V4_WITH_AUDIO.webm'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(OUT/'silent.mp4'),'-i',str(audio),
 '-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',str(mp4)],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(mp4),'-c:v','libvpx-vp9',
 '-deadline','realtime','-cpu-used','5','-b:v','0','-crf','32','-row-mt','1','-threads','4',
 '-c:a','libopus','-b:a','128k',str(webm)],check=True)
contact_sheet=Image.new('RGB',(4*286,5*526),'#17272b');d=ImageDraw.Draw(contact_sheet)
for i,(t,thumb) in enumerate(contact):
 x=(i%4)*286+8;y=(i//4)*526+24;contact_sheet.paste(thumb,(x,y))
 d.text((x,y-20),f'{t:.2f}s',fill='white')
contact_sheet.save(OUT/'CURIO_GHOST_ARMY_V4_FRAME_REVIEW.jpg',quality=89)
qa={'status':'ART_DIRECTION_REVIEW_NOT_MASTER','requested_duration_seconds':16,'rendered_distinct_frames':DUR*FPS,
 'screen_scale':'1080x1920','fps':FPS,'no_voiceover':True,
 'image_attribution':'See SOURCES.md (museum photo and two Army equipment type references)',
 'timeline_shots':[[0,3.2],[3.2,6.2],[6.2,9.2],[9.2,12.8],[12.8,16]],
 'final_data_unit_counts':{'actual_filled':11,'simulated_outlined':300,'people_per_unit':100},
 'files':{}}
for f in [mp4,webm]:
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(f)],text=True))
 vs=next(s for s in info['streams'] if s['codec_type']=='video')
 au=next(s for s in info['streams'] if s['codec_type']=='audio')
 assert (vs['width'],vs['height'],vs['r_frame_rate'])==(1080,1920,'24/1')
 duration=float(info['format']['duration']);assert abs(duration-16)<.15
 qa['files'][f.name]={'bytes':f.stat().st_size,'codec':vs['codec_name'],'audio':au['codec_name'],'duration':duration,'width':1080,'height':1920,'fps':vs['r_frame_rate']}
 subprocess.run(['ffmpeg','-v','error','-sseof','-0.2','-i',str(f),'-frames:v','1','-f','null','-'],check=True)
(OUT/'CURIO_GHOST_ARMY_V4_QA.json').write_text(json.dumps(qa,indent=2),encoding='utf8')
readme="""CURIO BUREAU — GHOST ARMY V4 / 16-SECOND VISUAL MATCH REVIEW
1080x1920, 24 native independently rendered frames/sec, H264/AAC MP4 plus VP9/Opus WebM.
Five deliberate distinct visual treatments: photo recognition / sonic mechanism / radio communication / schematic map / equal-unit force comparison.
Review only, not official 4K 30fps master. Original sound accents only, no voiceover (V3 reference had no narration).
Sources and truth/rights distinctions in SOURCES.md, supplied with editable HTML and separate source images.
The source images were obtained from Wikimedia Commons and not from Vox reference footage.
"""
(OUT/'README.txt').write_text(readme)
with zipfile.ZipFile(OUT/'CURIO_GHOST_ARMY_V4_EDITABLE_SOURCE.zip','w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
 z.write(OUT/'CURIO_GHOST_ARMY_V4_EDITABLE.html','visual_match.html')
 for name in SOURCES:z.write(ASSETS/(name+'.jpg'),'assets/'+name+'.jpg')
 z.write(ROOT/'SOURCES.md','SOURCES.md')
 z.write(ROOT/'render_v4.py','render_v4.py')
 z.write(OUT/'README.txt','README.txt')
 z.write(OUT/'CURIO_GHOST_ARMY_V4_QA.json','QA.json')
print('RENDER COMPLETE',json.dumps(qa['files']), 'wallsec',round(time.time()-start),flush=True)
