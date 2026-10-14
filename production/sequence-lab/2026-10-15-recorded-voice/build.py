from pathlib import Path
import base64,json,mimetypes,shutil
from PIL import Image
r=Path(__file__).parent
for n in ['ear_source.webp','paper_material.webp','fiber_browser.webp','plastic_browser.webp','photocopy_browser.webp','Manrope.ttf','PlayfairDisplay.ttf']:
 if not (r/'browser_assets'/n).exists():shutil.copy(Path('design_lab/browser_assets')/n,r/'browser_assets'/n)
# Reuse an already-cleared source model; resize/compress for the review only.
if not (r/'browser_assets/skull.webp').exists():
 im=Image.open('rebuild_voice/project/assets/skull_source.jpg');im.thumbnail((2000,2000));im.save(r/'browser_assets/skull.webp',quality=93)
if not (r/'browser_assets/microphone.jpg').exists():shutil.copy('rebuild_voice/project/assets/microphone_source.jpg',r/'browser_assets/microphone.jpg')
A={p.name:'data:'+(mimetypes.guess_type(p.name)[0] or 'application/octet-stream')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in (r/'browser_assets').iterdir()}
def image(n,x,y,w,h,extra=''):
 fit='' if 'preserveAspectRatio' in extra else 'preserveAspectRatio="xMidYMid slice"'
 tag=f'<image data-asset="{n}" x="{x}" y="{y}" width="{w}" height="{h}" {fit} {extra}/>'
 if 'url(#photo)' in extra:return tag.replace('url(#photo)','url(#mono)')+tag.replace('/>',' mask="url(#fringe-mask)"/>')
 return tag
def text(s,x,y,size=32,fill='#152032',font='Manrope',weight=800,extra=''):return f'<text x="{x}" y="{y}" fill="{fill}" font-family="{font}" font-weight="{weight}" font-size="{size}" {extra}>{s}</text>'
def lines(ss,x,y,size=100,fill='#152032',font='Playfair'):
 return ''.join(text(s,x,y+i*size*1.07,size,fill,font,900) for i,s in enumerate(ss))
def paper(x,y,w,h,extra=''):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#f5f0e7" {extra}/>'+image('paper_material.webp',x,y,w,h,'opacity=".56" style="mix-blend-mode:multiply"')
def ear(x,y,w,h,id='ear'):
 return f'<g data-role="{id}" clip-path="url(#ear-mask)">'+image('ear_source.webp',x,y,w,h,'filter="url(#photo)"')+'</g>'
def source_model():return '<g transform="rotate(-5 250 650)" data-role="body-context">'+paper(65,405,395,390,'filter="url(#shadow)"')+image('skull.webp',80,420,365,300,'filter="url(#mono)"')+text('SKULL MODEL',91,763,24)+'</g>'
def photoear():return '<g data-role="listener-print" transform="rotate(4 813 1420)">'+paper(590,1185,430,442,'filter="url(#shadow)"')+image('ear_source.webp',603,1198,404,416,'filter="url(#photo)"')+'</g>'
def routes(body=True,capture=False,playback=False):
 s='<g data-role="conceptual-paths" fill="none" stroke-linecap="round" stroke-linejoin="round">'
 s+='<path d="M130 1360 L130 1155 L945 1155 L945 1700 L840 1700" stroke="#f7c928" stroke-width="12" marker-end="url(#arrow-air)"/>'
 if body:s+='<path d="M130 1360 C130 1630 270 1730 460 1730 C620 1730 715 1700 830 1700" stroke="#d57864" stroke-width="14" marker-end="url(#arrow-body)"/>'
 else:s+='<path d="M130 1360 C130 1630 270 1730 460 1730 C620 1730 715 1700 830 1700" stroke="#d57864" stroke-width="8" stroke-dasharray="13 16" opacity=".2"/><rect x="605" y="1697" width="86" height="60" fill="#f5f0e7" stroke="none"/><path d="M626 1705L667 1748M666 1705L626 1748" stroke="#d57864" stroke-width="7"/>'
 if capture:s+='<path d="M420 1155 L420 710 L670 710" stroke="#f7c928" stroke-width="12" marker-end="url(#arrow-air)"/>'
 s+='</g>'
 s+= '<rect x="73" y="1295" width="274" height="111" fill="#152032"/>'+text('PLAYBACK' if playback else 'YOUR VOICE',93,1368,37,'#f5f0e7')
 s+= '<rect x="531" y="1109" width="117" height="57" fill="#f7c928"/>'+text('AIR',548,1152,36)
 s+= '<rect x="295" y="1612" width="167" height="62" fill="#d57864"/>'+text('BODY',311,1656,37)
 s+='<circle cx="830" cy="1700" r="34" fill="#152032"/>'+text('HEARING',735,1792,31)
 return s
css='''*{box-sizing:border-box}body{margin:0;background:#101319;color:#eee9df;font-family:Manrope}header{max-width:1160px;margin:36px auto 20px;padding:0 24px}h1{font-size:30px;letter-spacing:-1px;margin:12px 0}header p{font-size:14px;line-height:1.6;color:#b9babb;max-width:820px}.tools{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0}button{background:#eee9df;color:#152032;border:0;font:800 13px Manrope;padding:12px 18px;cursor:pointer}button[aria-pressed=true]{background:#f7c928}.gallery{max-width:1160px;margin:auto;display:grid;grid-template-columns:repeat(3,1fr);gap:24px;padding:0 24px 50px}.item{min-width:0}.art{display:block;width:100%;height:auto;background:#f5f0e7}.brief{font-size:13px;line-height:1.6;padding:14px 0;color:#c3c1bc}.brief b{display:block;font-size:16px;color:#fff}.single .gallery{grid-template-columns:1fr;max-width:640px}.single .item{display:none}.single .item.active{display:block}.safe{display:none}.show-safe .safe{display:block}.hide-headings .editorial-title{visibility:hidden}footer{max-width:1100px;margin:0 auto 40px;padding:24px;font-size:12px;color:#bbb;line-height:1.7}a{color:inherit}@media(max-width:700px){.gallery{grid-template-columns:1fr;max-width:480px}}'''
fontcss=''.join(f'@font-face{{font-family:{name};src:url("{A[f]}");font-weight:100 900;font-display:block}}' for name,f in [('Manrope','Manrope.ttf'),('Playfair','PlayfairDisplay.ttf')])
def defs():return '''<defs><radialGradient id="fringe-gradient"><stop offset="0" stop-color="black"/><stop offset=".55" stop-color="black"/><stop offset="1" stop-color="white"/></radialGradient><mask id="fringe-mask" maskUnits="objectBoundingBox" maskContentUnits="objectBoundingBox" x="0" y="0" width="1" height="1"><rect x="0" y="0" width="1" height="1" fill="url(#fringe-gradient)"/></mask><filter id="mono"><feColorMatrix type="saturate" values="0"/></filter><filter id="photo" color-interpolation-filters="sRGB"><feColorMatrix type="saturate" values="0" result="gray"/><feColorMatrix in="gray" values="1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0" result="r"/><feOffset in="r" dx="1.8" result="rr"/><feColorMatrix in="gray" values="0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 1 0" result="c"/><feOffset in="c" dx="-1.5" result="cc"/><feBlend in="rr" in2="cc" mode="screen"/></filter><filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".66" numOctaves="3" seed="17" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><filter id="ink"><feTurbulence baseFrequency=".04 .09" numOctaves="2" seed="7" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale=".6"/><feGaussianBlur stdDeviation=".13"/></filter><filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="8" dy="16" stdDeviation="8" flood-opacity=".25"/></filter><clipPath id="ear-mask"><path d="M320 625 L880 585 L1080 780 L1110 1390 L894 1602 L370 1652 L217 1420 L174 973Z"/></clipPath><marker id="arrow-air" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="2.4" markerHeight="2.4" orient="auto-start-reverse"><path d="M0 0L10 5L0 10" fill="#f7c928"/></marker><marker id="arrow-body" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="2.4" markerHeight="2.4" orient="auto"><path d="M0 0L10 5L0 10" fill="#d57864"/></marker></defs>'''
def wrap(content,i):return '<svg class="art" viewBox="0 0 1080 1920" xmlns="http://www.w3.org/2000/svg">'+defs()+paper(0,0,1080,1920)+text('CURIO BUREAU / VISUAL SEQUENCE',75,120,22,extra='letter-spacing="3"')+text('0'+str(i),965,120,26)+content+'<rect x="0" y="0" width="1080" height="1920" filter="url(#grain)" opacity=".13" style="mix-blend-mode:soft-light" pointer-events="none"/>'+text('Conceptual routes · not an anatomical map or measured signal',75,1866,21,weight=650)+'<g class="safe"><rect x="0" y="806" width="1080" height="307" fill="#00cda526" stroke="#00aa86" stroke-width="3" stroke-dasharray="15 12"/>'+text('42–58% caption review guide',30,847,27)+'</g></svg>'
frames=[]
# Recognition: the listener is the first eye target; a question relates it to recording.
f='<g class="editorial-title" filter="url(#ink)">'+lines(['Same voice.','Why different?'],75,270,118)+'</g>'+ear(160,580,1020,1040)+ '<g transform="rotate(-7 350 1540)" data-role="microphone">'+paper(-80,1480,870,225,'filter="url(#shadow)"')+image('mic-cutout',-90,1485,920,220,'preserveAspectRatio="xMidYMid meet"')+'</g>'+text('SPEAKING',95,1760,35)+text('RECORDING',665,1760,35)
frames.append(wrap(f,1))
# Relationship: two source categories converge on one conceptual hearing endpoint.
f='<g class="editorial-title" filter="url(#ink)">'+lines(['Two routes,','one listener.'],75,267,109)+'</g>'+source_model()+lines(['Body route:','skull +','other tissues'],510,512,37,font='Manrope')+photoear()+routes()
frames.append(wrap(f,2))
# Capture: retain the baseline and add a fork into a physical microphone, not a new postcard.
f='<g class="editorial-title" filter="url(#ink)">'+lines(['What the mic','captures.'],75,267,105)+'</g><g data-role="capture-device" transform="rotate(-6 615 580)">'+image('mic-cutout',235,466,900,275,'preserveAspectRatio="xMidYMid meet"')+'</g>'+text('AIRBORNE SOUND',492,784,31)+photoear()+routes(capture=True)
frames.append(wrap(f,3))
# Reveal: an actual recorded-narration strip replaces the source and the internal route terminates.
from scipy.io import wavfile
import numpy as np
voice_path=r/'source_audio/voice_full.wav'
if not voice_path.exists():voice_path=Path('rebuild_voice/project/assets/voice_full.wav')
sr,a=wavfile.read(voice_path)
if a.ndim>1:a=a.mean(axis=1)
a=a[int(3.38*sr):int(6.66*sr)].astype(float)
v=np.array([np.sqrt(np.mean(c*c)) for c in np.array_split(a,100)]);v=v/max(v.max(),1)
points=' '.join(f'{140+i*7.65:.1f},{625-z*58:.1f}' for i,z in enumerate(v))
wave_line=f'<polyline points="{points}" fill="none" stroke="#152032" stroke-width="4"/>'
# Actual source waveform is supplied by data.py elsewhere; no invented waveform is used here.
f='<g class="editorial-title" filter="url(#ink)">'+lines(['Playback leaves','a route out.'],75,267,108)+'</g>'+paper(100,475,865,245,'filter="url(#shadow)"')+text('RECORDED NARRATION',140,541,30)+wave_line+text('Approved voice / signal envelope',140,691,22,weight=650)+photoear()+routes(body=False,playback=True)+text('ABSENT',596,1671,26,'#a14d3e')
frames.append(wrap(f,4))
# Resolution: stable equal-scale comparison; absence is space rather than a fabricated metric.
f='<g class="editorial-title" filter="url(#ink)">'+lines(['Same voice.','Different routes.'],75,267,107)+'</g>'
for x,lab in [(70,'SPEAKING'),(572,'PLAYBACK')]:
 f+=text(lab,x+20,477,34)+paper(x,526,430,475,'filter="url(#shadow)"')+image('ear_source.webp',x+12,538,406,451,'filter="url(#photo)"')
 f+='<rect x="'+str(x)+'" y="1245" width="430" height="116" fill="#f7c928"/>'+text('AIR',x+28,1322,54)
f+='<rect x="70" y="1422" width="430" height="143" fill="#d57864"/>'+text('BODY',100,1510,55)
f+='<rect x="572" y="1422" width="430" height="143" fill="none" stroke="#d57864" stroke-width="4" stroke-dasharray="12 10"/>'+lines(['Original internal','route absent'],597,1477,29,font='Manrope')
f+=text('The microphone + room can also affect playback.',75,1764,29,weight=650)
frames.append(wrap(f,5))
briefs=[('01 / Recognize','The same voice is heard while speaking and on a recording. Establish the listener and question.'),('02 / Connect','Reveal two routes converging on one hearing destination. Routes are conceptual, not a physical anatomy trace.'),('03 / Capture','Keep the routes recognizable; add the microphone as a branch from airborne sound. The body route continues while speaking.'),('04 / Remove','Switch the source to playback. The original internal route stops before the hearing destination; its faint trace preserves the comparison.'),('05 / Resolve','Equal-scale listener images and aligned route rows show what persists and what is absent. No invented amplitude or pitch data.')]
items=''.join(f'<section class="item" data-board="{i+1}">{v}<div class="brief"><b>{briefs[i][0]}</b>{briefs[i][1]}</div></section>' for i,v in enumerate(frames))
# Sources are embedded once; SVG references are filled synchronously before capture.
js='const A='+json.dumps(A)+';'+'''async function setup(){let source=new Image();source.src=A['microphone.jpg'];await source.decode();const c=document.createElement('canvas');c.width=1876;c.height=640;const q=c.getContext('2d');q.drawImage(source,1900,775,1876,640,0,0,1876,640);let d=q.getImageData(0,0,c.width,c.height),p=d.data,seen=new Uint8Array(c.width*c.height),queue=new Int32Array(c.width*c.height),head=0,tail=0;const add=i=>{if(i<0||i>=seen.length||seen[i])return;seen[i]=1;if(p[i*4]*.2126+p[i*4+1]*.7152+p[i*4+2]*.0722>=165){queue[tail++]=i;p[i*4+3]=0}};for(let j=0;j<c.width;j++){add(j);add((c.height-1)*c.width+j)}for(let j=0;j<c.height;j++){add(j*c.width);add(j*c.width+c.width-1)}while(head<tail){let i=queue[head++],x=i%c.width;add(i-c.width);add(i+c.width);if(x)add(i-1);if(x<c.width-1)add(i+1)}q.putImageData(d,0,0);A['mic-cutout']=c.toDataURL();for(const im of document.querySelectorAll('image[data-asset]'))im.setAttribute('href',A[im.dataset.asset]);await document.fonts.ready;await Promise.all(Object.values(A).filter(u=>u.startsWith('data:image/')).map(async u=>{const im=new Image();im.src=u;await im.decode()}));window.artReady=true}const items=[...document.querySelectorAll('.item')];function choose(n){document.body.classList.toggle('single',n>0);items.forEach((e,i)=>e.classList.toggle('active',i===n-1));document.querySelectorAll('[data-select]').forEach(b=>b.setAttribute('aria-pressed',Number(b.dataset.select)===n))}document.querySelectorAll('[data-select]').forEach(b=>b.onclick=()=>choose(Number(b.dataset.select)));document.querySelector('#safe').onclick=()=>document.body.classList.toggle('show-safe');document.querySelector('#hide').onclick=()=>document.body.classList.toggle('hide-headings');setup();choose(0);'''
header='<header><p>CURIO BUREAU / CONNECTED VISUAL STATES</p><h1>How a recording leaves a route out.</h1><p>Five states of one explanation. Follow the yellow airborne route and coral internal route. Compare the unchanged hearing destination with the microphone branch and playback gap. Finished static beatboard; owner sequence review precedes animation.</p><nav class="tools">'+''.join(f'<button data-select="{n}" aria-pressed="false">{s}</button>' for n,s in [(0,'All five'),(1,'Recognize'),(2,'Connect'),(3,'Capture'),(4,'Remove'),(5,'Resolve')])+'<button id="safe">Caption guide</button><button id="hide">Hide headings</button></nav></header>'
credits='<footer><details><summary>Sources, rights and scientific limits</summary><p>Ear: Travis Isaacs / CC BY 2.0. Skull teaching model: John Campbell / CC BY 2.0. Microphone: Anonimski / CC0. Changes: crop, grayscale, source-preserving microphone matte, print composition and conceptual annotations. Owner materials and pinned fonts reused. No endorsement implied.</p><p>Air/body paths illustrate source-supported categories; they do not trace anatomy, measure vibration strength or claim equal contributions. The skull is a teaching model. Playback omits the original self-generated internal route; microphone and room also influence the recording.</p><p><a href="https://commons.wikimedia.org/wiki/File:Blond_Female_Ear.jpg">Ear source</a> / <a href="https://commons.wikimedia.org/wiki/File:Skull_model_1.jpg">Skull source</a> / <a href="https://commons.wikimedia.org/wiki/File:Microphone_and_cover.JPG">Mic source</a> / <a href="https://creativecommons.org/licenses/by/2.0/">CC BY 2.0</a> / <a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0</a></p><p><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC9929504/">Orepic et al.</a> / <a href="https://doi.org/10.1038/s41598-020-80095-6">Hosaka et al.</a> / <a href="https://www.nidcd.nih.gov/health/how-do-we-hear">NIDCD</a></p></details></footer>'
notices=''.join('<h3>'+p.name+'</h3><pre style="white-space:pre-wrap">'+__import__('html').escape(p.read_text())+'</pre>' for p in (r/'font_notices').glob('*.txt'))
html='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Curio Bureau / Recorded Voice sequence</title><style>'+fontcss+css+'</style>'+header+'<main class="gallery">'+items+'</main>'+credits+'<footer><details><summary>Font licenses</summary>'+notices+'</details></footer><script>'+js+'</script></html>'
(r/'deliverables/Recorded_Voice_Sequence_Review.html').write_text(html)
(r/'states.json').write_text(json.dumps({'status':'OWNER_SEQUENCE_REVIEW_PENDING','frames':[{'id':i+1,'job':b[0],'operation':b[1]} for i,b in enumerate(briefs)],'visual_style':'image-led','movement_implemented':False,'sequence_invariant':'AIR yellow; BODY coral; same listening subject; hearing endpoint common in states 2–4','captions_review':'Guide only; phrase-specific test pending'},indent=2))
print('built HTML',len(html))
