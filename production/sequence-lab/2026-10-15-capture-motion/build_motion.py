from pathlib import Path
import json,base64,mimetypes
r=Path(__file__).parent;out=r.parent/'delivered';out.mkdir(exist_ok=True)
a={p.name:'data:'+(mimetypes.guess_type(p.name)[0]or'application/octet-stream')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in (r/'assets').iterdir()}
fonts=''.join('@font-face{font-family:'+f+';src:url('+a[n]+');font-weight:100 900}' for f,n in [('Playfair','PlayfairDisplay.ttf'),('Manrope','Manrope.ttf')])
base=(r/'scene.js').read_text().split('function record(')[0]
js='const ASSETS='+json.dumps(a)+';const envelope='+ (r/'envelope.json').read_text()+';'+base+(r/'motion.js').read_text()
audio=base64.b64encode((r/'audio/mix.ogg').read_bytes()).decode()
html='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Curio / Moving capture passage</title><style>'''+fonts+'''body{margin:0;background:#111923;color:#f5f0e7;font:15px Manrope}main{max-width:540px;margin:auto;padding:20px}h1{font:900 25px Playfair}p{font-size:13px;line-height:1.6;color:#bbc2cb}canvas{width:100%;height:auto}nav{display:flex;gap:8px;flex-wrap:wrap;margin:15px 0}button{font:800 12px Manrope;padding:12px;background:#f0cd29;border:0;cursor:pointer}input{width:100%}</style><main><h1>Recorded Voice / moving passage</h1><p>13.2-second motion study of the approved composition. Original Bernard recording, reused action sounds, original study score. Artwork approved; motion awaits review. Gold/coral are conceptual categories; portrait is an illustration.</p><nav><button id="play">Play / pause</button><button id="restart">Restart</button><button id="export">Export full WebM</button></nav><input aria-label="Scrub passage" type="range" min="0" max="13.2" step=".033333" value="0"><canvas width="1080" height="1920"></canvas><audio preload="auto" src="data:audio/ogg;base64,'''+audio+'''"></audio><p>Lab captions use the upper quiet area to preserve the approved art. Full-film caption safe-zone and platform review remain pending. Microphone: Anonimski, CC0. Owner materials reused privately; font notices and detailed sources in the source package.</p></main><script>'''+js+'</script></html>'
cached=out/'Capture_Motion_Review.webm'
if cached.exists():
 data='data:video/webm;base64,'+base64.b64encode(cached.read_bytes()).decode()
 html=html.replace('</script></html>','</script><script>const VERIFIED_WEBM='+json.dumps(data)+';'+(r/'verified_player.js').read_text()+'</script></html>')
(out/'Capture_Motion_Review.html').write_text(html);print('Built motion HTML',len(html))
