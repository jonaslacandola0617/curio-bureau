from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import base64,json,hashlib,html,io
root=Path(__file__).resolve().parent
names=['01_hook','02_check','03_name','04_candidate','05_interpretation','06_evidence','07_payoff']
labels=['1 / Felt buzz','2 / Checking the phone','3 / Naming the experience','4 / Possible input','5 / Proposed interpretation','6 / Evidence boundary','7 / Payoff']
sheet=Image.new('RGB',(960,1836),'#e9e4da');d=ImageDraw.Draw(sheet)
for i,(n,label) in enumerate(zip(names,labels)):
 im=Image.open(root/'rendered'/f'{n}.jpg').resize((300,533))
 x=10+(i%3)*320;y=40+(i//3)*610
 sheet.paste(im,(x,y));d.text((x,y-23),label,fill='#0d1c2b')
sheet.save(root/'CONTACT_SHEET.jpg',quality=94)
strip=Image.new('RGB',(960,590),'#e9e4da');d=ImageDraw.Draw(strip)
for i in range(3):
 im=Image.open(root/'rendered'/f'passage_{i}.jpg').resize((300,533));strip.paste(im,(10+i*320,40));d.text((10+i*320,16),['Initial / sensation','Intermediate / expectation','Resolved / interpretation'][i],fill='#0d1c2b')
strip.save(root/'HARDEST_PASSAGE.jpg',quality=94)
def uri(p):
 im=Image.open(p);im.thumbnail((540,960));b=io.BytesIO();im.save(b,format='JPEG',quality=84);return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
items=[]
for n,label in zip(names,labels):
 items.append('<figure><figcaption>'+html.escape(label)+'</figcaption><img class="normal" src="'+uri(root/'rendered'/f'{n}.jpg')+'"><img class="hidden" src="'+uri(root/'rendered'/f'{n}_no_heading.jpg')+'"></figure>')
passage=''.join('<figure><figcaption>'+label+'</figcaption><img class="normal" src="'+uri(root/'rendered'/f'passage_{i}.jpg')+'"><img class="hidden" src="'+uri(root/'rendered'/f'passage_{i}_no_heading.jpg')+'"></figure>' for i,label in enumerate(['Initial','Intermediate','Resolved']))
page='''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Curio Bureau / Phantom Vibration / Art v1</title><style>*{box-sizing:border-box}body{margin:0;background:#e9e4da;color:#0d1c2b;font:16px system-ui}header,section{max-width:1200px;margin:auto;padding:24px}h1{font-size:32px}button{background:#0d1c2b;color:#f5f0e7;border:0;padding:14px;cursor:pointer}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px}figure{margin:0}figcaption{padding:12px 0;font-weight:700}img{width:100%;display:block}.hidden{display:none}body.nohead .normal{display:none}body.nohead .hidden{display:block}.note{max-width:850px;line-height:1.5}@media(max-width:700px){.grid{grid-template-columns:1fr}header,section{padding:16px}}</style><header><h1>Phantom Vibration — complete-story artwork</h1><p class="note">STATIC ART REVIEW v1. Lightweight540px previews; the separate rendered/ folder retains all native1080px frames. Seven story beats and the hardest three-state passage. No animation, voice recording or final duration is claimed. Proposed explanations remain explicitly qualified. Clean text and graphics: no blurred backdrop, glow or added soft shadow. The established brand ending will be inserted unchanged after the complete final spoken word.</p><button onclick="document.body.classList.toggle('nohead')">Show / hide decorative headlines</button></header><section><h2>All seven beats</h2><div class="grid">'''+''.join(items)+'''</div></section><section><h2>Hardest passage: source stays fixed, interpretation changes</h2><p class="note">The cloth/phone photograph is an illustrative candidate cue, not an experimentally demonstrated trigger. The question mark and proposed-explanation label must remain. The visual does not depict measured brain activity.</p><div class="grid">'''+passage+'''</div></section></html>'''
(root/'REVIEW.html').write_text(page)
print('Built self-contained REVIEW.html and two contact sheets.')
