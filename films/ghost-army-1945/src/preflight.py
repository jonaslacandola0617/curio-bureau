#!/usr/bin/env python3
"""Native-4K styleframe motion preflight. Uses the actual spoken timing and Canvas renderer."""
import pathlib,json,base64,math,sys
from io import BytesIO
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
R=pathlib.Path(__file__).resolve().parents[1]; A=R/'audio';S=R/'src';T=R/'review';F=R/'assets';T.mkdir(exist_ok=True)
d=json.loads((A/'timeline.json').read_text());s=(S/'studio_template.html').read_text()
style=''
for fam,fname in [('Manrope','Manrope.ttf'),('Playfair Display','PlayfairDisplay.ttf')]:
 f=F/fname
 if not f.exists():raise RuntimeError('missing render font '+str(f))
 style+='@font-face{font-family:"'+fam+'";src:url(data:font/truetype;base64,'+base64.b64encode(f.read_bytes()).decode()+') format("truetype");font-weight:100 900;}'
s=s.replace('/*LOCAL_RENDER_FONTS*/',style).replace('/*TIMELINE_JSON*/',json.dumps(d,separators=(',',':')))
private=T/'preflight_INTERNAL_RENDERER.html';private.write_text(s)
frames=[];errors=[]
with sync_playwright() as p:
 browser=p.chromium.launch(headless=True,args=['--disable-dev-shm-usage','--no-sandbox','--disable-gpu-sandbox'])
 ctx=browser.new_context(viewport={'width':1080,'height':1920},device_scale_factor=2)
 page=ctx.new_page()
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(private.as_uri(),wait_until='domcontentloaded',timeout=180000)
 page.add_style_tag(content='body{margin:0!important;padding:0!important;display:block!important}canvas{width:1080px!important;height:1920px!important}#controls{display:none!important}')
 page.evaluate('window.readyPromise')
 checks=page.evaluate("({playfair:document.fonts.check('600 64px Playfair Display'),manrope:document.fonts.check('700 32px Manrope'),canvas:[document.querySelector('canvas').width,document.querySelector('canvas').height]})")
 assert checks['playfair'] and checks['manrope'] and checks['canvas']==[2160,3840],checks
 for k in range(9):
  sc=d['scenes'][str(k)]
  for frac in [.05,.37,.71]:
   tt=sc['start']+(sc['end']-sc['start'])*frac
   page.evaluate('(t)=>window.setTime(t)',tt)
   raw=page.locator('#film').screenshot(type='png',scale='device')
   im=Image.open(BytesIO(raw)).convert('RGB')
   if im.size!=(2160,3840):raise RuntimeError('Not native-4K '+str(im.size))
   if frac==.37:im.save(T/f'scene_{k}_2160x3840.png',optimize=True)
   im.thumbnail((225,400))
   frames.append((k,frac,im))
 if errors:raise RuntimeError('Browser errors: '+str(errors))
 browser.close()
sheet=Image.new('RGB',(27//3*239,3*427),(11,21,32)) # 9 columns x 3 rows
draw=ImageDraw.Draw(sheet)
for i,(k,u,img) in enumerate(frames):
 col=i//3;row=i%3
 x=col*239+7;y=row*427+20
 sheet.paste(img,(x,y));draw.text((x,y-16),f'S{k} at {int(u*100)}%',fill=(242,218,166))
sheet.save(T/'EP009_9_SCENES_27_FRAME_MOTION_XRAY.jpg',quality=87)
# Small version for real human remote GitHub quick review, only committed artwork is original.
size=Image.new('RGB',(9*181,3*324),(12,22,33));dw=ImageDraw.Draw(size)
for i,(k,u,img) in enumerate(frames):
 col=i//3;row=i%3
 pic=img.copy();pic.thumbnail((171,304));x=col*181+5;y=row*324+19
 size.paste(pic,(x,y));dw.text((x,y-17),f'S{k} {round(u,2)}',fill='#dbc6a6')
size.save(T/'EP009_SHOT_PREFLIGHT_CONTACT.jpg',quality=80)
report={"native4k":True,"fps":30,"scenes":9,"timeline_seconds":d['duration'],
        "frame_samples":27,"scene_midframes_native_saved":9,
        "motion_validation":"27 samples over 9 scenes at 5/37/71 percent, not continuous human playback",
        "font_checks":checks,"page_errors":errors,
        "release":"ART PREFLIGHT / motion only; no actual video release approval",
        "limitations":["No human full-speed sound audit","Original layered objects reviewed by sampled frames, not subjective animation audit","Captions phrase-timed; true word-level align still open"]}
(T/'EP009_PREFLIGHT_QA.json').write_text(json.dumps(report,indent=2))
print('EP009_PREFLIGHT_PASS',json.dumps(report),flush=True)
