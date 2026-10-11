#!/usr/bin/env python3
"""Native 4K lossless-PNG-stream deterministic rendering, separate codecs and actual encoded QA."""
import os,sys,json,base64,time,math,zipfile,shutil,subprocess,pathlib
from PIL import Image,ImageOps,ImageDraw,ImageFont
from playwright.sync_api import sync_playwright
ROOT=pathlib.Path(__file__).resolve().parents[1];A=ROOT/'audio';SRC=ROOT/'src';DIST=ROOT/'dist';AS=ROOT/'assets';DIST.mkdir(exist_ok=True);AS.mkdir(exist_ok=True)
manifest=json.loads((A/'timeline.json').read_text());duration=float(manifest['duration']);frames=round(duration*30)
font_style=''
for css,path in [('Playfair Display',AS/'PlayfairDisplay.ttf'),('Manrope',AS/'Manrope.ttf')]:
 if not path.exists():raise RuntimeError('Mandatory font absent: '+str(path))
 bin=base64.b64encode(path.read_bytes()).decode()
 font_style+='@font-face{font-family:"'+css+'";src:url(data:font/truetype;base64,'+bin+') format("truetype");font-weight:100 900;}'
html=(SRC/'studio_template.html').read_text()
html=html.replace('/*LOCAL_RENDER_FONTS*/',font_style)
html=html.replace('/*TIMELINE_JSON*/',json.dumps(manifest,separators=(',',':')))
(DIST/'studio_renderer_PRIVATE.html').write_text(html)
# Clean end-user studio deliberately excludes font binaries and raw inline fonts.
clean=(SRC/'studio_template.html').read_text().replace('/*LOCAL_RENDER_FONTS*/','')
clean=clean.replace('/*TIMELINE_JSON*/',json.dumps(manifest,separators=(',',':')))
(DIST/'CURIO_EP009_MOTION_STUDIO.html').write_text(clean)

shutil.copy(A/'final_mix.mp3',DIST/'final_mix.mp3')
shutil.copy(A/'captions.srt',DIST/'captions.srt')
(DIST/'READ_ME.txt').write_text('Curio Bureau Episode 009 — RENDER CANDIDATE. Open CURIO_EP009_MOTION_STUDIO.html in a browser; keep final_mix.mp3 alongside it. Online Playfair and Manrope will load via Google Fonts. Every visible WWII battlefield illustration is originally drawn Canvas art, an explicitly labelled reconstruction, not an archival photograph or battlefield recording. This candidate requires human artistic, caption and listening review before FINAL MASTER. No font binaries distributed.\n')
mp4=DIST/'CURIO_BUREAU_EP009_NATIVE4K_MP4_REVIEW.mp4';webm=DIST/'CURIO_BUREAU_EP009_NATIVE4K_WEBM_REVIEW.webm'
cmd=['ffmpeg','-y','-loglevel','error','-threads','4','-f','image2pipe','-framerate','30','-vcodec','png','-i','pipe:0','-i',str(A/'master_24bit.wav'),'-map','0:v','-map','1:a','-c:v','libx264','-preset','ultrafast','-crf','14','-pix_fmt','yuv420p','-tune','animation','-r','30','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart','-frames:v',str(frames),str(mp4)]
print('RENDERING',frames,'native-4K frames for',round(duration,3),'seconds',flush=True)
times=[];contact=[];first5=DIST/'first_5_seconds_4K_preview.mp4'
with sync_playwright() as pw:
 browser=pw.chromium.launch(headless=True,args=['--disable-dev-shm-usage','--no-sandbox','--disable-gpu-sandbox'])
 context=browser.new_context(viewport={'width':1080,'height':1920},device_scale_factor=2)
 page=context.new_page()
 page.goto((DIST/'studio_renderer_PRIVATE.html').as_uri(),wait_until='domcontentloaded',timeout=180000)
 page.add_style_tag(content='body{margin:0!important;padding:0!important;display:block!important}canvas{width:1080px!important;height:1920px!important}#controls{display:none!important}')
 page.evaluate('window.readyPromise')
 check=page.evaluate("({playfair:document.fonts.check('600 32px Playfair Display'),manrope:document.fonts.check('700 32px Manrope'),nativeCanvas:document.querySelector('canvas').width})")
 print('ASSETS_CHECK',check,flush=True)
 if not(check['playfair'] and check['manrope'] and check['nativeCanvas']==2160):raise RuntimeError('Critical font or native canvas failed')
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
 for i in range(frames):
  page.evaluate('(n)=>window.renderFrame(n)',i)
  pic=page.locator('#film').screenshot(type='png',scale='device')
  proc.stdin.write(pic)
  if i==0:
   from io import BytesIO
   im=Image.open(BytesIO(pic))
   if im.size!=(2160,3840):raise RuntimeError('NOT native 4k screenshot: '+str(im.size))
  if i in [round(j*(frames-1)/12) for j in range(13)] or (i%200==0):
   from io import BytesIO
   thumb=Image.open(BytesIO(pic)).convert('RGB')
   thumb.thumbnail((270,480))
   if i in [round(j*(frames-1)/12) for j in range(13)]:contact.append((i,thumb))
  if i%180==0:print('FRAME',i,'of',frames,'elapsed',round(time.time()-os.stat(mp4).st_mtime) if mp4.exists() else 0,flush=True)
 proc.stdin.close()
 if proc.wait()!=0:raise RuntimeError('FFmpeg H264 encoder failed with '+str(proc.returncode))
 context.close();browser.close()
print('MP4 COMPLETE',mp4.stat().st_size,flush=True)
# Encode 4K WebM without changing dimensions, fps or captions.
vc=['ffmpeg','-y','-loglevel','error','-i',str(mp4),'-c:v','libvpx-vp9','-deadline','realtime','-cpu-used','5','-row-mt','1','-threads','4','-b:v','0','-crf','24','-pix_fmt','yuv420p','-c:a','libopus','-b:a','256k','-ar','48000','-ac','2',str(webm)]
subprocess.run(vc,check=True);print('WEBM COMPLETE',webm.stat().st_size,flush=True)
# Contact montage actually extracted from original rendered PNG images, plus stream validation.
if contact:
 cols=3;rows=math.ceil(len(contact)/cols);sheet=Image.new('RGB',(cols*290,rows*520),(7,16,27));draw=ImageDraw.Draw(sheet)
 for j,(ix,pic) in enumerate(contact):
  x=(j%cols)*290+10;y=(j//cols)*520+27
  sheet.paste(pic,(x,y));draw.text((x,y-20),'T=%0.2fs'%(ix/30),fill=(234,222,198))
 sheet.save(DIST/'EP009_NATIVE4K_CONTACT_SHEET.jpg',quality=94)
qa={'native4k_expected':[2160,3840,30],'frames_expected':frames,'duration_timeline':duration,'streams':{},'release_status':'RENDER CANDIDATE','creative_release_blockers':['Requires complete subjective full-speed playback on consumer phone/headphones','Caption phrase boundaries tied to actual TTS clips; word-level alignment unavailable','No independent human external art-director approval of all moving mechanisms','Expressive narrator human listening A/B comparisons open']}
for fn in [mp4,webm]:
 p=subprocess.run(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(fn)],capture_output=True,text=True,check=True)
 obj=json.loads(p.stdout)
 va=next(z for z in obj['streams'] if z['codec_type']=='video');au=next(z for z in obj['streams'] if z['codec_type']=='audio')
 inf={'width':va['width'],'height':va['height'],'fps':va['r_frame_rate'],'codec':va['codec_name'],'audio_codec':au['codec_name'],'audio_rate':au['sample_rate'],'duration':obj['format'].get('duration')}
 if inf['width']!=2160 or inf['height']!=3840 or inf['fps']!='30/1':raise RuntimeError('Encoded stream failed 4k: '+str(inf))
 if int(au['sample_rate'])!=48000:raise RuntimeError('Audio rate wrong')
 qa['streams'][fn.name]=inf
 subprocess.run(['ffmpeg','-v','error','-sseof','-1','-i',str(fn),'-frames:v','1','-f','null','-'],check=True)
(DIST/'ENCODE_QA.json').write_text(json.dumps(qa,indent=2))
# Distributable source zip. Excludes raw fonts and private renderer HTML.
with zipfile.ZipFile(DIST/'CURIO_BUREAU_EP009_SOURCE_REVIEW.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in [DIST/'CURIO_EP009_MOTION_STUDIO.html',DIST/'final_mix.mp3',DIST/'captions.srt',DIST/'READ_ME.txt',DIST/'ENCODE_QA.json']:
  z.write(p,p.name)
 for p in [SRC/'studio_template.html',SRC/'build_audio.py',SRC/'render.py']:
  z.write(p,'src/'+p.name)
 for p in (ROOT/'docs').rglob('*'):
  if p.is_file():z.write(p,'docs/'+p.name)
 for p in [A/'timeline.json',A/'voice_gap_QA.json',A/'audio_cue_sheet.csv',A/'VOICE_AB_QA.md',A/'AUDIO_HUMAN_CREATIVE_GATE.md']:
  z.write(p,'audio/'+p.name)
print('EP009 RENDER CANDIDATE DELIVERED',qa['streams'],flush=True)
