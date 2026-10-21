from pathlib import Path
import os,sys,json,math,subprocess
from functools import lru_cache
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter
import finish as F
P=Path(__file__).resolve().parent;ROOT=Path(os.getenv('CURIO_REPO_ROOT',str(P.parents[3])));A=P/'assets';R=P/'review';R.mkdir(exist_ok=True)
TL=json.loads((P/'timeline.json').read_text());W,H=1080,1920;N=(13,28,43);I=(245,240,231);G=(200,162,107);C=(213,120,100);B=(88,191,229)
FP=ROOT/'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets'
@lru_cache(80)
def font(s,serif=False):
 f=ImageFont.truetype(str(FP/('Playfair900.ttf'if serif else'Manrope.ttf')),s)
 if not serif:f.set_variation_by_axes([700])
 return f
def txt(im,x,y,s,n=30,c=I,serif=False,anchor=None):ImageDraw.Draw(im).text((x,y),s,font=font(n,serif),fill=c,anchor=anchor)
def lines(im,x,y,ss,n=70,c=I,serif=True):
 for k,s in enumerate(ss):txt(im,x,y+k*n*1.12,s,n,c,serif)
def tag(im,x,y,s,c=G,n=25):
 d=ImageDraw.Draw(im);ww=d.textbbox((0,0),s,font=font(n))[2]+28;d.rectangle((round(x),round(y),round(x+ww),round(y+n+20)),fill=c);txt(im,x+14,y+5,s,n,N)
def S(v):v=max(0,min(1,v));return v*v*(3-2*v)
def L(a,b,v):return a+(b-a)*v
@lru_cache(22)
def frame(kind,tick):
 fs=sorted((P/'frames'/kind).glob('*.jpg'));return Image.open(fs[max(0,min(len(fs)-1,tick))]).convert('RGB')
mp=Image.open(A/'official-comparison.jpg').convert('RGB');basin=Image.open(A/'imus-basin.jpeg').convert('RGB');marker=Image.open(A/'imus-marker.jpeg').convert('RGB');excerpt=Image.open(A/'jica-excerpt.png').convert('RGB')
BND=TL['scene_boundaries'];OFFSET=TL['body_offset_from_v5']
def oldtime(t):return t-OFFSET
def photo(im,src,box,t,kind='photo',focus=None,hunt=0,moving=0,contain=False,border=0):
 x,y,w,h=map(round,box);dx,dy=F.jitter(t);x+=dx;y+=dy
 if contain:
  q=Image.new('RGB',(w,h),I);z=src.copy();z.thumbnail((w,h),Image.Resampling.LANCZOS);q.paste(z,((w-z.width)//2,(h-z.height)//2))
 else:q=ImageOps.fit(src,(w,h),method=Image.Resampling.LANCZOS)
 q=F.source(q,t,kind,focus,hunt,moving)
 if border:
  b=F.backing(w+border*2,h+border*2,True,F.active('material_texture')).copy();b.paste(q,(border,border));im.paste(b,(x-border,y-border))
 else:im.paste(q,(x,y))
 return x,y,w,h
def ink(im,pts,t,c=G,width=5):
 # Only editorial selection marks boil; documentary map boundaries never do.
 wobble=.8*math.sin(math.floor(t*12)*2.2)if F.active('edge_boil')else 0
 pts=[(x,y+wobble)for x,y in pts];d=ImageDraw.Draw(im)
 if F.active('ink_bleed'):
  under=tuple(round(z*.55)for z in c);d.line([(x,y+1)for x,y in pts],fill=under,width=width+2)
 d.line(pts,fill=c,width=width)
def caption(im,t):
 c=next((x for x in TL['captions']if x['start']<=t<x['end']),None)
 if c:
  s=c['text'];n=35;d=ImageDraw.Draw(im)
  while d.textbbox((0,0),s,font=font(n))[2]>970:n-=1
  w=d.textbbox((0,0),s,font=font(n))[2]+32;x=(W-w)//2
  d.rectangle((x,975,x+w,1037),fill=N);txt(im,540,982,s,n,I,anchor='ma')
def foot(im,s,light=False):
 c=N if light else I
 # Crisp source footnotes on a clean material lane, never blurred shadows.
 ImageDraw.Draw(im).rectangle((0,1742,W,H),fill=I if light else N)
 txt(im,48,1763,s,23,c);txt(im,48,1810,'Sources: USACE / DVIDS; JICA evaluation',21,c)
 txt(im,48,1850,'U.S. government imagery does not imply endorsement.',19,c)
@lru_cache(3)
def emphasized(mode):
 a=np.asarray(mp).copy();f=a.astype(np.float32);grey=np.mean(f,axis=2);base=f*.20+grey[:,:,None]*.80
 blue=(f[:,:,2]>f[:,:,0]*1.25)&(f[:,:,2]>105)&(f[:,:,2]>f[:,:,1]*1.2)
 red=(f[:,:,0]>f[:,:,1]*1.3)&(f[:,:,0]>f[:,:,2]*1.16)&(f[:,:,0]>100)
 mask=blue if mode=='blue'else red if mode=='red'else blue|red
 base[mask]=f[mask];return Image.fromarray(np.uint8(base))
def raw(t,headings=True,caps=True):
 qt=math.floor((t+1e-8)*12)/12;k=min(8,max(i for i,b in enumerate(BND)if qt>=b));u=qt-BND[k];ot=oldtime(qt)
 im=F.backing(W,H,k==5,F.active('material_texture')).copy()
 if k==0:
  # Three independent source planes: background project, street print, question.
  v=S((u-.25)/1.55);p=S((u-2.65)/1.0)
  photo(im,basin,(-110-18*v,470-55*v,1290+80*v,870+90*v),qt,focus=(.5,.5),hunt=F.hunt_envelope(u-.12),moving=1-v)
  if headings:
   lines(im,52,125,['Can flood control','actually work?'],82)
   tag(im,54,334,'IN THE PHILIPPINES?',n=31)
  if u>1.75:ink(im,[(55,410),(L(55,715,S((u-1.75)/.45)),410)],qt,width=6)
  if u>2.65:
   x=L(1120,425,p)-60*S((u-3.6)/1.7);y=L(1020,1135,p)
   photo(im,marker,(x,y,650,500),qt,focus=(.63,.5),hunt=F.hunt_envelope(u-3.7),moving=1-p,border=14)
   if headings and u>3.2:tag(im,58,1450,'HOW WOULD YOU PROVE',n=27);tag(im,58,1510,'YOUR STREET IS SAFER?',n=31)
  foot(im,'Imus project photographs · JICA / DPWH · FY2023 evaluation')
 elif k==1:
  # Documentary footage owns the scene; the camera reveals its operating structure.
  v=S(u/1.05);q=frame('hickory',round((10+u)*12))
  photo(im,q,(L(-155,-45,v),0,1235,1742),qt,'video',focus=(.5,.38),hunt=F.hunt_envelope(u+.08),moving=1-v)
  if headings:
   ImageDraw.Draw(im).rectangle((36,110,935,335),fill=N)
   lines(im,54,125,['Start with','a recorded event.'],77)
  tag(im,54,365,'TENNESSEE, USA · FEBRUARY 2025',n=26)
  if u>1.8:
   # Widen to the actual context in a separate, nearer evidence print.
   v2=S((u-1.8)/.65);photo(im,frame('cordell',round((12+u)*12)),(L(1100,420,v2),1195,610,440),qt,'video',moving=1-v2,border=10)
  if u>3.7:tag(im,54,1640,'USACE · ORIGINAL EVENT RECORD',n=25)
  foot(im,'Old Hickory / Cordell Hull · USACE · 16 February 2025')
 elif k==2:
  # A single geography is retained while its published categories become readable.
  mode='blue'if ot<19.12232 else'both';source=mp if ot<15.48232 else emphasized(mode)
  v=S((u-.2)/.85);mw=1160-80*v
  mx,my,mw,mh=photo(im,source,(-80+80*v,420,mw,mw*mp.height/mp.width),qt,'print',moving=1-v,border=8)
  if headings:txt(im,54,140,'What changed?',91,I,True)
  tag(im,54,292,'PUBLISHED WITH / WITHOUT COMPARISON',n=24)
  if ot>=15.48232:
   # The crop is the original map's pixels, not an invented flood drawing.
   z=S((ot-15.48232)/.75);detail=S((ot-17.0)/.6)
   rw=L(700,570,detail);rh=L(380,310,detail);roi=(900-rw/2,490-rh/2,900+rw/2,490+rh/2)
   x,y,w,h=photo(im,source.crop(roi),(L(700,80,z),1145,920,500),qt,'print',focus=(.5,.48),hunt=F.hunt_envelope(ot-15.48232),moving=1-z,border=12)
   if ot>=16.3:tag(im,80,1080,'BLUE: WITH PROJECTS',B,27)
   if ot>=19.12232:tag(im,80,1660,'RED: ESTIMATED WITHOUT',C,27)
   d=ImageDraw.Draw(im);sx=mw/mp.width;sy=mh/mp.height
   d.rectangle((mx+roi[0]*sx,my+roi[1]*sy,mx+roi[2]*sx,my+roi[3]*sy),outline=G,width=4)
  foot(im,'USACE graphic 8910491 · original source colors emphasized')
 elif k==3:
  # Same map is inspected; blue and red meanings remain attached to their source.
  v=S(u/.8);roi=(690,260,1390,1000)
  photo(im,emphasized('blue').crop(roi),(-170+100*v,420,1000,1057),qt,'print',focus=(.52,.45),hunt=F.hunt_envelope(u),moving=1-v)
  x=L(1120,510,S((u-.7)/.8));photo(im,emphasized('red').crop(roi),(x,620,640,677),qt,'print',moving=1-S((u-.7)/.8),border=12)
  if headings:lines(im,54,125,['Not another flood.'],79)
  tag(im,54,318,'A MODELLED ALTERNATIVE',C,29)
  if u>1.4:tag(im,555,1527,'SAME MAP',n=26)
  foot(im,'Counterfactual: USACE estimated without-project extent')
 elif k==4:
  photo(im,frame('hickory',round((30+u)*12)),(0,320,1080,1400),qt,'video')
  if headings:
   tag(im,54,120,'HOW MUCH DAMAGE AVOIDED?',n=29)
   y=L(440,330,S(u/.75));ImageDraw.Draw(im).rectangle((36,y-7,666,y+300),fill=N)
   txt(im,54,y,'$734',142,I,True);txt(im,54,y+156,'million',118,I,True)
  tag(im,55,660,'USACE ESTIMATE',n=30)
  if u>2.1:
   v=S((u-2.1)/.5);ImageDraw.Draw(im).rectangle((54,L(1200,1120,v),1026,1390),fill=N)
   lines(im,82,L(1230,1155,v),['Across the Cumberland','River Basin'],44,I,False)
  if u>5.4:tag(im,55,1520,'PRELIMINARY ANALYSIS',C,29)
  foot(im,'USACE preliminary analysis · published 12 March 2025')
 elif k==5:
  # Return to the opening's actual Philippine source; a report advances, not a new noun card.
  v=S(u/1.0);photo(im,basin,(-45-70*v,420-25*v,1170,840),qt,focus=(.5,.42),hunt=F.hunt_envelope(u),moving=1-v)
  if headings:lines(im,54,105,['Now check Imus.'],82,N)
  tag(im,54,277,'PHILIPPINES · DISTINCT PROJECT RECORD',n=24)
  if u>1.75:tag(im,54,1100,'INTERVIEWS: IMPROVEMENT REPORTED',n=25)
  if u>3.5:
   z=S((u-3.5)/.7);photo(im,marker,(L(1110,600,z),1240,480,450),qt,focus=(.63,.5),hunt=F.hunt_envelope(u-3.6),moving=1-z,border=12)
  if u>5.2:
   z=S((u-5.2)/.65);y=L(1800,1320,z)
   photo(im,excerpt,(50,y,950,138),qt,'print',contain=True,moving=1-z,border=14)
   if u>5.9:tag(im,54,1500,'COMPARABLE ACTUAL VALUES: UNAVAILABLE',C,24)
  txt(im,54,1660,'Overall evaluation: satisfactory.',30,N)
  foot(im,'JICA FY2023 evaluation · printed pp.1, 14–15',True)
 elif k==6:
  photo(im,basin,(-90,400,1250,850),qt)
  z=S(u/.7);photo(im,marker,(L(610,510,z),1180,610,490),qt,border=12,moving=1-z)
  if headings:
   txt(im,54,150,'Unknown',109,I,True);tag(im,54,300,'DOES NOT MEAN ZERO BENEFIT',n=30)
  # Two honest categories, not a false numeric counter.
  tag(im,54,1330,'MISSING MEASUREMENTS',C,25)
  if u>1.3:tag(im,54,1400,'PROJECT STILL EXISTS',G,25)
  foot(im,'Unavailable comparable values ≠ zero measured benefit')
 elif k==7:
  # Three separately authored evidence planes navigate front to back.
  n=0 if u<2.5 else 1 if u<5 else 2;v=S((u-[0,2.5,5][n])/.65)
  sources=[frame('hickory',round((14+u)*12)),mp,marker]
  # Receding evidence remains context, never a new coordinate interpretation.
  if n>0:photo(im,sources[n-1],(-130,350,800,530),qt,'print',focus=(.45,.45),border=10)
  photo(im,sources[n],(L(1120,80,v),570,960,1000 if n!=1 else 650),qt,'video'if n==0 else'print',hunt=F.hunt_envelope(u-[0,2.5,5][n]),moving=1-v,border=14)
  if headings:txt(im,54,125,'Ask for the proof.',82,I,True)
  tag(im,54,315,['1  THE EVENT RECORD','2  THE WITH / WITHOUT MODEL','3  CHECKS AGAINST OBSERVATIONS'][n],n=27)
  if n==1:tag(im,80,1380,'SAME EVENT · TWO CONDITIONS',n=28)
  if n==2:photo(im,excerpt,(54,1480,970,145),qt,'print',contain=True,border=8)
  foot(im,'Keep recorded events, estimates and field checks distinct')
 else:
  photo(im,frame('hickory',round((49+u)*12)),(0,0,1080,1742),qt,'video')
  if headings:
   ImageDraw.Draw(im).rectangle((36,115,1044,255),fill=N)
   txt(im,54,125,'How much safer?',86,I,True)
  if u>1.15:tag(im,54,310,'FOR WHOM?',n=31)
  if u>2.05:
   v=S((u-2.05)/.55);photo(im,marker,(L(1120,550,v),1155,550,495),qt,hunt=F.hunt_envelope(u-2.1),moving=1-v,border=12)
   tag(im,54,1500,'HOW DO YOU KNOW?',n=30)
  foot(im,'Can flood control actually work in the Philippines?')
 if caps:caption(im,t)
 txt(im,48,42,'CURIO BUREAU',22,N if k==5 else G)
 return im

def stills():
 times=[.3,2.1,4.4]+[b+.8 for b in BND[1:-1]]+[BND[2]+6.9,BND[5]+6.5,TL['ending_start']-.4]
 for i,t in enumerate(times):raw(t).save(R/f'{i:02}-{t:.2f}.jpg',quality=96,subsampling=0)
 board=Image.new('RGB',(1440,math.ceil(len(times)/4)*664),N)
 for i,t in enumerate(times):
  board.paste(raw(t).resize((360,640)),((i%4)*360,(i//4)*664));txt(board,(i%4)*360+8,(i//4)*664+642,f'{t:.2f}s',14)
 board.save(R/'v6-source-board.jpg',quality=95)
 raw(BND[2]+5,False,False).save(R/'heading-hidden-map.jpg')
 raw(TL['ending_start']-.04).save(P/'ending-base.png')
def chunk(start,end,file):
 # Every native capture entry point rechecks actual proof freshness. A wrapper cannot
 # accidentally bypass finishing by invoking this renderer directly.
 sys.path.insert(0,str(ROOT/'production/engine'))
 from finishing_contract import validate_finishing
 from finishing_audit import check
 from production_standard import validate_standard
 config=json.loads((P/'episode.json').read_text())
 validate_finishing(config,P,stage='release',studio_path=P/'render.py',expected_size=[1080,1920])
 validate_standard(config,P,actual_duration=TL['duration'])
 audit=check(P/'FINISHING_COVERAGE.json');assert audit['execution_records_pass'],audit
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pixel_format','rgb24','-s','1080x1920','-r','30','-i','-','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',str(file)]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE);last=-1;buf=None;endstart=round(TL['ending_start']*30)
 for n in range(start,end):
  if n>=endstart:buf=composed(n).tobytes()
  else:
   tick=math.floor((n/30+1e-8)*12)
   if tick!=last:buf=raw(tick/12).tobytes();last=tick
  proc.stdin.write(buf)
 proc.stdin.close();assert proc.wait()==0;print('CLOSED_CHUNK',start,end,flush=True)
def composed(n):
 endstart=round(TL['ending_start']*30)
 if n>=endstart:return Image.open(P/'ending'/f'{n-endstart:03}.png').convert('RGB')
 return raw(math.floor((n/30+1e-8)*12)/12)
if __name__=='__main__':
 if '--chunk'in sys.argv:chunk(int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
 else:stills()
