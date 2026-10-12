#!/usr/bin/env python3
"""Render genuine 24-fps distinct frames from browser-openable Curio collage source.
This is a REVIEW proof at 540x960, not a native-4K episode master."""
import base64,io,json,math,os,pathlib,shutil,subprocess,time,wave,zipfile
import numpy as np
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright

HERE=pathlib.Path(__file__).resolve().parent
FILM=HERE.parents[1]
OUT=HERE/'output'
OUT.mkdir(exist_ok=True)
TEMPLATE=(HERE/'motion_template.html').read_text(encoding='utf8')
ORIGINAL=(FILM/'src'/'studio_template.html').read_text(encoding='utf8')
assert 'const W=1080,H=1920' in ORIGINAL
legacy=ORIGINAL[ORIGINAL.index('const W=1080,H=1920'):ORIGINAL.index('function scene0')]
assert 'function ww2Tank' in legacy and 'function speakerVehicle' in legacy and 'function radioBox' in legacy
source=TEMPLATE.replace('/*LEGACY_FUNCTIONS*/',legacy)
(OUT/'CURIO_GHOST_ARMY_V3_EDITABLE.html').write_text(source,encoding='utf8')
fontcss=''
for family,fname in [('Playfair Display','PlayfairDisplay.ttf'),('Manrope','Manrope.ttf')]:
 f=FILM/'assets'/fname
 if f.exists():
  data=base64.b64encode(f.read_bytes()).decode()
  fontcss+='@font-face{font-family:"'+family+'";src:url(data:font/truetype;base64,'+data+') format("truetype");font-weight:100 900;}\n'
renderer=source.replace('/*INLINE_RENDER_FONTS*/',fontcss)
(OUT/'renderer_private.html').write_text(renderer,encoding='utf8')

rate=48000;dur=16;sr=np.arange(rate*dur)/rate
# Original synthesized room-tone, warm signal swells, selective textured thumps.
a=.014*np.sin(2*np.pi*59*sr)+.009*np.sin(2*np.pi*91*sr)
a+=.006*np.sin(2*np.pi*180*sr)*np.sin(sr*.77)
def hit(at,base=85,amp=.12):
 global a
 dt=sr-at;mask=(dt>=0)&(dt<.55)
 part=np.zeros(len(sr),dtype=np.float64)
 part[mask]=amp*np.exp(-dt[mask]*11)*np.sin(2*np.pi*(base*dt[mask]+(base*.28)*dt[mask]**2))
 a+=part
for t,base,amp in [(1.33,230,.065),(2.91,78,.20),(3.58,64,.17),(5.05,130,.075),(7.35,110,.19),(8.75,210,.065),(11.2,83,.19),(12.78,145,.065),(13.65,105,.12)]:
 hit(t,base,amp)
# broadband tactile paper rustle at select physical actions, no SFX blanket.
rng=np.random.default_rng(3341)
for at,amp,length in [(1.4,.05,.2),(3.58,.04,.12),(7.38,.045,.2),(11.24,.06,.32)]:
 start=int(at*rate);size=int(length*rate)
 n=rng.normal(0,1,size)
 # short noisy scratch band with no external recordings
 n=np.convolve(n,np.ones(25)/25,mode='same')
 end=min(len(a),start+size)
 a[start:end]+=amp*n[:end-start]*np.linspace(0,1,end-start)**.25*np.linspace(1,0,end-start)**.5
a=np.tanh(a*1.6)*.78
audio=OUT/'CURIO_GHOST_ARMY_V3_ORIGINAL_AUDIO.wav'
with wave.open(str(audio),'wb') as w:
 w.setnchannels(2);w.setsampwidth(2);w.setframerate(rate)
 stereo=np.stack([a,a*.98],axis=1)
 w.writeframes((stereo*32767).astype('<i2').tobytes())

start=time.time()
frames=dur*24
silent=OUT/'frames_no_audio.mp4'
cmd=['ffmpeg','-y','-nostdin','-loglevel','error','-f','image2pipe','-framerate','24','-vcodec','png','-i','pipe:0',
 '-an','-c:v','libx264','-preset','veryfast','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart','-r','24',
 '-frames:v',str(frames),str(silent)]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
contact=[]
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu-sandbox'])
 page=browser.new_page(viewport={'width':750,'height':1300},device_scale_factor=1)
 page.goto((OUT/'renderer_private.html').as_uri(),wait_until='domcontentloaded',timeout=120000)
 page.wait_for_function('window.renderReady === true',timeout=120000)
 page.add_style_tag(content="main{padding:0!important;margin:0!important}#film{width:540px!important;height:960px!important}main>div,main>small{display:none!important}")
 for i in range(frames):
  page.evaluate('(n)=>window.renderAt(n/24)',i)
  png=page.locator('#film').screenshot(type='png',animations='disabled')
  proc.stdin.write(png)
  if i in [round((frames-1)*j/11) for j in range(12)]:
   thumb=Image.open(io.BytesIO(png)).convert('RGB');thumb.thumbnail((180,320))
   contact.append((i,thumb.copy()))
  if i%48==0:
   print('Rendered moving frame',i,'/',frames,'elapsed sec',round(time.time()-start),flush=True)
  if page.locator('#film').count()!=1: raise RuntimeError('Canvas lost')
 browser.close()
proc.stdin.close()
if proc.wait()!=0:raise RuntimeError('ffmpeg video render failed')

mp4=OUT/'CURIO_GHOST_ARMY_EDITORIAL_COLLAGE_V3_WITH_AUDIO.mp4'
webm=OUT/'CURIO_GHOST_ARMY_EDITORIAL_COLLAGE_V3_WITH_AUDIO.webm'
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(silent),'-i',str(audio),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',str(mp4)],check=True)
subprocess.run(['ffmpeg','-y','-loglevel','error','-i',str(mp4),'-c:v','libvpx-vp9','-deadline','realtime','-cpu-used','5','-b:v','0','-crf','31','-row-mt','1','-threads','4','-c:a','libopus','-b:a','128k',str(webm)],check=True)
contact_sheet=Image.new('RGB',(3*190,4*354),'#162b30')
d=ImageDraw.Draw(contact_sheet)
for idx,(i,img) in enumerate(contact):
 x=(idx%3)*190+5;y=(idx//3)*354+20
 contact_sheet.paste(img,(x,y));d.text((x,y-15),f'T={i/24:.2f}s',fill='#f3eee4')
contact_sheet.save(OUT/'CURIO_GHOST_ARMY_V3_FRAME_REVIEW.jpg',quality=90)
qa={'review_not_master':True,'duration_requested':dur,'frames_rendered':frames,'render_cadence':'24 independently rendered frames per second','audio':'original synthetic sound bed and designed accents; NO narration','source':'HTML Canvas + editable layered illustration; reused EP009 illustrative object functions','files':{}}
for filename in (mp4,webm):
 info=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(filename)],text=True))
 video=next(s for s in info['streams'] if s['codec_type']=='video')
 aud=next(s for s in info['streams'] if s['codec_type']=='audio')
 assert (video['width'],video['height'],video['r_frame_rate'])==(540,960,'24/1')
 qa['files'][filename.name]={'size':filename.stat().st_size,'video_codec':video['codec_name'],'audio_codec':aud['codec_name'],'width':540,'height':960,'frame_rate':'24/1','duration':info['format']['duration']}
 subprocess.run(['ffmpeg','-v','error','-sseof','-0.3','-i',str(filename),'-frames:v','1','-f','null','-'],check=True)
(OUT/'CURIO_GHOST_ARMY_V3_QA.json').write_text(json.dumps(qa,indent=2))
readme="""CURIO BUREAU — GHOST ARMY / EXPERIMENTAL EDITORIAL COLLAGE PROOF V3
16 seconds, native 24 distinct illustrated frames/sec at 540x960 REVIEW size, H264/AAC MP4 and VP9/Opus WebM.
Original synthetic sound cues; no narration. Not a native-4K final master, not 100% independent photographs, and not an approved public episode.
This V3 attempts varied transformations: short 2.5D reveal, circle-to-horn match, sound trace to radio, cable to conceptual map, selective map emphasis.
Source HTML editable; open in browser (uses online fonts). No copyrighted Vox frames or audio bundled.
Reuse of programmatic tank/speaker/radio illustration functions from current Curio EP009 means their mechanical detail remains a quality ceiling: these are paper-composited vector-like illustrations, not new professionally sourced photographs. Owner should reject if this looks too simplistic.
Caution: Map is expressly illustrative; '1,100' and '~30,000' represent period contextual approximate Ghost Army size and possible simulated force size; not a precise plotted order of battle.
"""
(OUT/'README.txt').write_text(readme)
with zipfile.ZipFile(OUT/'CURIO_GHOST_ARMY_V3_EDITABLE_SOURCE.zip','w',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
 for f in [OUT/'CURIO_GHOST_ARMY_V3_EDITABLE.html',OUT/'README.txt',OUT/'CURIO_GHOST_ARMY_V3_QA.json']:
  z.write(f,f.name)
 z.write(HERE/'motion_template.html','source/motion_template.html')
 z.write(HERE/'render_preview.py','source/render_preview.py')
 print('SOURCE_ARCHIVED',flush=True)
print('ALL_CHECKS_PASS',json.dumps(qa['files']), 'wallsec',round(time.time()-start),flush=True)
