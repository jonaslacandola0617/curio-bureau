from pathlib import Path
import json,base64,mimetypes
r=Path(__file__).parent
assets={p.name:'data:'+(mimetypes.guess_type(p.name)[0]or'application/octet-stream')+';base64,'+base64.b64encode(p.read_bytes()).decode() for p in (r/'assets').iterdir()}
base=(r/'static_scene.js').read_text().split('function render(state)')[0]
base=base.replace('const u=state/2;', 'const u=motion.vessel;').replace('amp=3+u*25,drop=u*34,contract=u*48','amp=3+motion.fold*25,drop=motion.volume*34,contract=motion.volume*48')
start=base.index('let seed=3108;');end=base.index('q.restore();',start);base=base[:start]+"q.drawImage(printStipple,-450,-60);"+base[end:]
base=base.replace('if(state===1){ // A lifted inspection corner','if(motion.corner>0){ // A lifted inspection corner').replace('q.save();q.translate(373,-213);','q.save();q.globalAlpha=motion.corner;q.translate(373,-213);')
anim=(r/'animate.js').read_text().split('function setupPlayer()')[0].replace('const DURATION=12;', 'const PASSAGE_DURATION=12;').replace('function renderAt(t)', 'function renderMechanism(t)')
fonts=''.join('@font-face{font-family:"'+f+'";src:url('+assets[n]+');font-weight:100 900;}' for f,n in [('Playfair','PlayfairDisplay.ttf'),('Playfair Display','PlayfairDisplay.ttf'),('Manrope','Manrope.ttf')])
html='<!doctype html><html><meta charset="utf-8"><style>'+fonts+'body{margin:0;background:#0d1c2b}canvas{display:block;height:100vh;width:auto;margin:auto}</style><canvas></canvas><script>const ASSETS='+json.dumps(assets)+';'+base+anim+((r/'shared/brand.js') if (r/'shared/brand.js').exists() else (r.parent/'curio_wrinkle_full/production/engine/browser/brand.js')).read_text()+(r/'film.js').read_text()+'</script></html>'
(r/'studio.html').write_text(html);print('Studio built',len(html))
