from pathlib import Path
import os,json,hashlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont
from scipy.ndimage import binary_propagation
HERE=Path(__file__).resolve().parent
ROOT=Path(os.environ.get('CURIO_REPO_ROOT',str(HERE.parents[3])))
FP=ROOT/'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets'
OUT=HERE/'review';OUT.mkdir(exist_ok=True)
N='#0D1C2B';I='#F5F0E7';G='#C8A26B';C='#D57864';B='#A9CFD6'
def f(size,serif=False):
 x=ImageFont.truetype(str(FP/('Playfair900.ttf' if serif else 'Manrope.ttf')),size)
 if not serif:x.set_variation_by_axes([600])
 return x
def t(im,xy,s,size=30,col=I,serif=False,anchor=None):ImageDraw.Draw(im).text(xy,s,font=f(size,serif),fill=col,anchor=anchor)
def lines(im,xy,ss,size=68,col=I,serif=True,step=None):
 for k,s in enumerate(ss):t(im,(xy[0],xy[1]+k*(step or size+10)),s,size,col,serif)
def tag(im,x,y,s,col=G,size=28):
 d=ImageDraw.Draw(im);w=d.textbbox((0,0),s,font=f(size))[2]+24;d.rectangle((x,y,x+w,y+size+19),fill=col);t(im,(x+12,y+6),s,size,N)
def base(kind):
 im=Image.new('RGB',(1080,1920),N);d=ImageDraw.Draw(im)
 for y in range(270,1860,112):d.line((0,y,1080,y-28),fill='#122332',width=1)
 t(im,(64,59),'CURIO BUREAU',23,G);t(im,(1016,59),kind,19,I,anchor='ra');d.line((64,106,1016,106),fill=G,width=2)
 t(im,(1016,119),'EDITORIAL SOURCE EXCERPT' if 'EVIDENCE' in kind else 'ILLUSTRATIVE MODEL',22,G,anchor='ra')
 t(im,(64,1830),'CONCEPTUAL MODEL · NOT A REAL PROJECT',22,G);t(im,(64,1868),'STATIC ART REVIEW v1 / NOT A HYDRAULIC RESULT',19)
 return im
def cap(im,s):
 d=ImageDraw.Draw(im);w=d.textbbox((0,0),s,font=f(34))[2]+36;x=(1080-w)//2;d.rectangle((x,989,x+w,1044),fill='#09141F');t(im,(540,995),s,34,anchor='ma')
src=Image.open(HERE/'assets/neighborhood-concept-v1.png').convert('RGB');a=np.array(src).astype(float)
possible=(a[:,:,2]>a[:,:,0]*1.15)&(a[:,:,2]>a[:,:,1]*1.03)&(a.max(2)<105)
seed=np.zeros(possible.shape,bool);seed[0]=possible[0];seed[:,0]=possible[:,0];seed[:,-1]=possible[:,-1]
plate=src.convert('RGBA');plate.putalpha(Image.fromarray(np.uint8(~binary_propagation(seed,mask=possible))*255))
wall=Image.new('RGBA',src.size);mask=Image.new('L',src.size);ImageDraw.Draw(mask).polygon([(323,166),(994,652),(994,553),(323,143)],fill=255)
rng=np.random.default_rng(20261020);noise=rng.normal(0,7,(src.height,src.width));yy,xx=np.indices(noise.shape);noise+=3*np.sin(xx*.07)+3*np.sin(yy*.15)
tex=Image.fromarray(np.clip(np.array([156,157,151])[None,None,:]+1.65*noise[:,:,None],0,255).astype('uint8')).convert('RGBA');tex.putalpha(mask);wall.alpha_composite(tex)
d=ImageDraw.Draw(wall);d.polygon([(323,143),(994,553),(1010,544),(332,140)],fill='#C4C5BC');d.polygon([(994,652),(1010,641),(1010,544),(994,553)],fill='#777D79');d.line([(323,143),(994,553)],fill='#D4D2C6',width=2)
for q in [.12,.3,.48,.66,.83]:
 x=323+671*q;y=166+486*q;h=23+76*q;d.line((x,y,x,y-h),fill='#666F6C',width=2);d.ellipse((x+4,y-h+9,x+7,y-h+12),fill='#545F5B')
def model(im,x,y,w,haswall=True,probe=False):
 p=plate.copy();sc=w/src.width
 if haswall:p.alpha_composite(wall)
 p=p.resize((w,round(src.height*sc)),Image.Resampling.LANCZOS);im.paste(p,(x,y),p)
 if probe:
  tx=x+round(1184*sc);ty=y+round(428*sc);d=ImageDraw.Draw(im);d.ellipse((tx-17,ty-17,tx+17,ty+17),outline=B,width=3);d.line((tx,ty,tx-92,ty+116,tx-225,ty+116),fill=B,width=3);tag(im,tx-225,ty+128,'DEPTH: ?',B,27)
def save(im,name):im.save(OUT/(name+'.png'))
for stage in ['initial','intermediate','resolved']:
 im=base('02 / CONTROLLED COMPARISON')
 if stage=='initial':
  lines(im,(64,158),['Start with','one place.'],71,step=78);model(im,-10,470,1100);tag(im,64,1255,'PROJECT PRESENT',size=23);t(im,(64,1340),'Keep the river, street and homes recognizable.',30);cap(im,'Start with the same neighborhood.')
 else:
  lines(im,(64,145),['Change the project.'],57);t(im,(64,223),'MATCH THE STORM / MATCH THE EXPOSED HOMES',24,G)
  tag(im,64,281,'WITH PROJECT');model(im,45,330,990,True,stage=='resolved');tag(im,64,1108,'WITHOUT PROJECT',C);model(im,45,1157,990,False,stage=='resolved')
  d=ImageDraw.Draw(im);sc=990/1536
  for k in range(0,16,2):
   q=k/16;r=(k+1)/16;d.line((45+(323+671*q)*sc,1157+(166+486*q)*sc,45+(323+671*r)*sc,1157+(166+486*r)*sc),fill=C,width=4)
  cap(im,'Same conditions. Remove the project.' if stage=='intermediate' else 'Then estimate the difference. Don’t assume it.')
 save(im,'02-'+stage)
 if stage=='resolved':
  ImageDraw.Draw(im).rectangle((55,154,1040,218),fill=N);save(im,'02-resolved-heading-hidden')
im=base('03 / EVIDENCE');lines(im,(64,151),['What could the','evaluation verify?'],67,step=77)
paper=np.array(Image.new('RGB',(952,660),I)).astype(float);paper=np.clip(paper+rng.normal(0,1.6,(660,952,1)),0,255).astype('uint8');im.paste(Image.fromarray(paper),(64,400));d=ImageDraw.Draw(im)
t(im,(94,434),'JICA / FY2023 EX-POST EVALUATION',24,N);d.line((94,484,985,484),fill=N,width=2);t(im,(94,510),'IMUS RIVER COMPONENT',30,N)
lines(im,(94,580),['“Therefore, the actual','values could not','be reviewed.”'],44,N,False,61);d.rectangle((94,780,973,837),fill='#E7CA64');t(im,(110,792),'Comparable flood-area / household data unavailable',25,N)
t(im,(94,865),'Interviews separately reported reduced flood damage.',25,N);t(im,(94,925),'Editorial excerpt · §3.3.1.1 · printed pp14–15',22,N);cap(im,'Missing measurements are not zero flooding.')
lines(im,(64,1180),['Two kinds','of evidence.'],73,step=83);t(im,(64,1410),'DATA COMPARISON',25,G);t(im,(64,1460),'Unknown for these indicators.',34);t(im,(64,1540),'INTERVIEWS',25,G);t(im,(64,1590),'Reported improvement.',34);t(im,(64,1710),'Overall project evaluation: satisfactory.',26);save(im,'03-evidence')
im=base('04 / RETURN TO THE HOMES');lines(im,(64,154),['For whom?'],97);p=src.convert('RGBA');p.alpha_composite(wall);im.paste(p.crop((386,0,1536,920)).convert('RGB').resize((1080,864),Image.Resampling.LANCZOS),(0,470));cap(im,'How much risk was reduced—and for whom?')
d=ImageDraw.Draw(im);d.ellipse((735,845,783,893),outline=G,width=4);d.line((760,892,691,1390,570,1390),fill=G,width=3);lines(im,(64,1450),['Ask for the evidence','behind the protection.'],50,step=68);t(im,(64,1660),'Scenario comparison → observed checks → limits',27,B);save(im,'04-payoff')
if (OUT/'01-opening.png').exists():
 board=Image.new('RGB',(1080,1360),N)
 for i,name in enumerate(['01-opening','02-initial','02-intermediate','02-resolved','03-evidence','04-payoff']):
  board.paste(Image.open(OUT/(name+'.png')).resize((360,640),Image.Resampling.LANCZOS),((i%3)*360,(i//3)*680));t(board,((i%3)*360+12,(i//3)*680+646),name,17)
 board.save(OUT/'review-board.jpg',quality=95)
receipt={p.name:{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'size':Image.open(p).size}for p in sorted(OUT.glob('*'))};(HERE/'RENDER_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print('Rendered',len(receipt),'review files; motion and voice NOT STARTED.')
