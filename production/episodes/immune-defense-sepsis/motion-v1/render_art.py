"""Native scene-specific artwork; still review only. No motion/listening approval implied."""
from pathlib import Path
from functools import lru_cache
import math,json
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageOps
import finish as F
P=Path(__file__).resolve().parent;A=P/'assets';R=P/'review';R.mkdir(exist_ok=True)
MOTION=False; U=2.4; CL=1.0
def S(v):
 v=max(0,min(1,v));return v*v*(3-2*v)
def entry(delay=0):return S((U-delay)/.7) if MOTION else 1
W,H=1080,1920;N=(13,28,43);I=(245,240,231);G=(255,227,55);C=(255,64,48);TEAL=(91,151,153)
@lru_cache(90)
def font(n,serif=False):
 f=ImageFont.truetype(str(A/('Playfair900.ttf' if serif else 'Manrope.ttf')),n)
 if not serif:f.set_variation_by_axes([700])
 return f
def txt(im,x,y,s,n=30,c=I,serif=False,anchor=None):ImageDraw.Draw(im).text((x,y),s,font=font(n,serif),fill=c,anchor=anchor)
def lines(im,x,y,ss,n=78,c=I):
 for i,s in enumerate(ss):txt(im,x,y+i*n*1.10,s,n,c,True)
def tag(im,x,y,s,n=25,c=G):
 d=ImageDraw.Draw(im);box=d.textbbox((0,0),s,font=font(n));ww=box[2]+28;d.rectangle((x,y,x+ww,y+n+20),fill=c);txt(im,x+14,y+5,s,n,N)
def line(im,pts,c=G,w=3):ImageDraw.Draw(im).line(pts,fill=c,width=w,joint='curve')
def arrow(im,pts,c=G,w=4):
 line(im,pts,c,w);x,y=pts[-1];xx,yy=pts[-2];a=math.atan2(y-yy,x-xx);d=ImageDraw.Draw(im);d.polygon([(x,y),(x-18*math.cos(a-.42),y-18*math.sin(a-.42)),(x-18*math.cos(a+.42),y-18*math.sin(a+.42))],fill=c)
def cap(im,s,light=False):
 n=37
 while font(n).getlength(s)>960:n-=1
 ww=font(n).getlength(s);d=ImageDraw.Draw(im);d.rectangle((540-ww/2-15,973,540+ww/2+15,1037),fill=N);txt(im,540,982,s,n,I,anchor='ma')
def footer(im,ss,light=False):
 c=N if light else I;ImageDraw.Draw(im).rectangle((0,1720,W,H),fill=I if light else N)
 for j,s in enumerate(ss):txt(im,48,1740+j*36,s,22,c)
def paste(im,q,xy):
 if q.mode=='RGBA':im.paste(q,tuple(map(round,xy)),q)
 else:im.paste(q,tuple(map(round,xy)))
def photo(im,q,box,t,focus=(.5,.5),kind='photo',blur=0):
 x,y,w,h=map(round,box);q=ImageOps.fit(q.convert('RGB'),(w,h),method=Image.Resampling.LANCZOS)
 q=F.source(q,t,kind,focus,hunt=F.hunt_envelope(U) if MOTION else blur,moving=1-entry());dx,dy=F.jitter(t);paste(im,q,(x+dx,y+dy))
@lru_cache(50)
def rbc(w=130,h=80,angle=0):
 # Biconcave illustrative disc: center depression, rim, directional light, surface tooth.
 yy,xx=np.mgrid[-1:1:complex(h),-1:1:complex(w)];r=np.sqrt(xx*xx+yy*yy);z=np.sqrt(np.clip(1-r*r,0,1))*(.24+.76*(1-np.exp(-r*r*7)))
 gy,gx=np.gradient(z);shade=np.clip(.65-gx*23-gy*15+z*.5,0,1.35);noise=np.random.default_rng(w*19+h).normal(0,.022,(h,w))
 a=np.clip(np.array([235,48,36])[None,None,:]*(shade+noise)[:,:,None],0,255)
 rgba=np.dstack((a,np.uint8(np.clip((1-r)*35,0,1)*255))).astype(np.uint8)
 return Image.fromarray(rgba).rotate(angle,Image.Resampling.BICUBIC,expand=True)
@lru_cache(100)
def lining_cell(w,h,seed=1):
 # Organic, microtextured endothelial tile: shaded material and irregular membrane.
 rng=np.random.default_rng(seed);yy,xx=np.mgrid[:h,:w];x=(xx-w*.5)/(w*.51);y=(yy-h*.5)/(h*.51)
 theta=np.arctan2(y,x);r=(np.abs(x)**3+np.abs(y)**3)**(1/3);edge=1+.025*np.sin(theta*7+seed)+.012*np.sin(theta*19)
 z=np.sqrt(np.clip(1-(r/edge)**4,0,1));shade=np.clip(.55+.44*z-.18*x-.16*y,0,1.25)
 fibers=np.sin(xx*.19+yy*.12+3*np.sin(yy*.035))*1.8+np.sin(xx*.071-yy*.15)*1.1
 noise=rng.normal(0,2.3,(h,w));col=np.array([126,153,143]);a=np.clip(col[None,None,:]*shade[:,:,None]+noise[:,:,None]+fibers[:,:,None],0,255)
 # Local ellipsoidal nucleus is a sculpted depression, not flat oval graphic.
 nr=((x+.02)/.30)**2+((y+.04)/.44)**2;nm=np.clip((1-nr)*8,0,1)
 nuc=np.array([73,101,108])[None,None,:]*(.6+.55*np.sqrt(np.clip(1-nr,0,1)))[:,:,None]
 a=a*(1-nm[:,:,None]*.8)+nuc*nm[:,:,None]*.8
 edgeglint=np.exp(-((r/edge-.92)/.022)**2)*18
 a+=edgeglint[:,:,None];alpha=np.uint8(np.clip((edge-r)*45,0,1)*255)
 return Image.fromarray(np.dstack((np.uint8(np.clip(a,0,255)),alpha)))

@lru_cache(3)
def tissue(w,h,light=False):
 # Dense organic material with separate cells and coherent low-relief lighting.
 rng=np.random.default_rng(322);bg=(214,205,186)if light else(29,49,59);q=Image.new('RGB',(w,h),bg)
 for row in range(-1,h//110+2):
  for col in range(-1,w//190+2):
   x=int(col*185+(row%2)*90+rng.uniform(-13,13));y=int(row*105+rng.uniform(-8,8))
   cell=lining_cell(200,125,100+row*31+col)
   if light:
    a=np.array(cell).copy();rgb=a[:,:,:3].astype(float);rgb=rgb*.4+np.array([145,131,108])[None,None,:];a[:,:,:3]=np.uint8(np.clip(rgb,0,255));cell=Image.fromarray(a)
   else:
    a=np.array(cell).copy();a[:,:,:3]=np.uint8(a[:,:,:3].astype(float)*.58);cell=Image.fromarray(a)
   paste(q,cell,(x,y))
 return q

def vessel(im,box,leak=0,t=0,clot=False,light=False):
 """Declared longitudinal section; RBCs stay intravascular, fluid tracers cross gap."""
 x,y,w,h=box;pw,ph=round(w),round(h);q=Image.new('RGB',(pw,ph),N)
 yy=np.arange(ph)[:,None];base=np.array([45,45,50])[None,None,:]+np.sin(np.arange(ph)[:,None,None]/ph*np.pi)*np.array([34,8,7])[None,None,:]
 a=np.tile(base,(1,pw,1));q=Image.fromarray(np.uint8(a));d=ImageDraw.Draw(q)
 d.rectangle((0,0,pw,ph*.22),fill=(24,51,61));d.rectangle((0,ph*.81,pw,ph),fill=(25,48,57))
 # Separate top and bottom lining tiles preserve visible junctions.
 count=6;cw=math.ceil(pw/count);ch=round(ph*.19)
 for row,cy in [(0,round(ph*.08)),(1,round(ph*.72))]:
  for k in range(count):
   offset=round(leak*23)if row==1 and k>=3 else 0
   paste(q,lining_cell(cw-4,ch,k+row*20+1),(k*cw+offset,cy+(round(leak*9)if row==1 and k==3 else 0)))
 for k in range(7):
  xx=(k*pw/6+t*43)%(pw+110)-80;cy=ph*.47+math.sin(k*2)*ph*.12
  if clot and CL>.55 and xx>pw*.66:continue
  paste(q,rbc(round(ph*.28),round(ph*.16),int(-14+k*7)),(xx,cy))
 if clot:
  rng=np.random.default_rng(41)
  for j in range(max(0,round(34*CL))):
   xx=pw*.65+rng.normal(0,pw*.055);cy=ph*.50+rng.normal(0,ph*.13);rr=rng.uniform(8,16)
   d.ellipse((xx-rr,cy-rr,xx+rr,cy+rr),fill=(255,220,43),outline=(255,241,133),width=2)
  for j in range(max(0,round(35*CL))):
   xx=pw*.65+rng.normal(0,pw*.055);cy=ph*.5+rng.normal(0,ph*.17);d.line((xx,cy,xx+rng.normal(0,55),cy+rng.normal(0,48)),fill=(255,229,80),width=2)
 q=F.source(q,t,'print',focus=(.5,.65),hunt=F.hunt_envelope(U-1.2)if MOTION else 0,moving=1-entry())
 paste(im,q,(x,y))
 if leak:
  d=ImageDraw.Draw(im);cx=x+pw*.50
  for k in range(18):
   u=(k/18+t*.11)%1;px=cx+math.sin(k*2.5)*18+u*math.sin(k)*80;py=y+ph*.80+u*125
   rr=3+(k%3);d.ellipse((px-rr,py-rr,px+rr,py+rr),fill=G)
 return x+pw*.5,y+ph*.85

def raw(scene,t=2,captions=True,headings=True):
 light=scene in [2,5];im=Image.new('RGB',(W,H),I if light else N);tc=N if light else I
 if scene==0:
  if headings:lines(im,54,130,['Could your body’s','defense system','hurt you?'],78)
  tag(im,58,432,'PROTECTION HAS A HIDDEN LIMIT',n=24)
  hand=Image.open(A/'hand-original.png').convert('RGBA');hand.thumbnail((1330,1000));paste(im,hand,(40+220*(1-entry()),640+32*(1-entry())))
  # Separate photographic circular microscope inspection; physical depth is editorial.
  m=Image.open(A/'neutrophil-mrsa.jpg').convert('RGB');m=ImageOps.fit(m,(430,430));mask=Image.new('L',(430,430));ImageDraw.Draw(mask).ellipse((2,2,428,428),fill=255)
  rim=Image.new('RGBA',(450,450));dr=ImageDraw.Draw(rim);dr.ellipse((0,0,449,449),fill=G);rim.paste(m,(10,10),mask);paste(im,rim,(54-260*(1-entry(.6)),1190+45*(1-entry(.6))))
  line(im,[(495,1385),(680,1305),(775,1275)],G,3);txt(im,540,1480,'Your cells.',38);txt(im,540,1532,'Your defenses.',38)
  footer(im,['NIH / NIAID: false-colored electron microscopy','Hand: original illustrative photographic asset','No patient or sepsis diagnosis is depicted.'])
  phrase='Could your body’s defense system hurt you?'
 elif scene==1:
  src=Image.open(A/'neutrophil-mrsa.jpg');photo(im,src,(0,0,1080,1720),t,focus=(.51,.42))
  d=ImageDraw.Draw(im);d.rectangle((35,100,1045,340),fill=N)
  if headings:lines(im,56,116,['Built to protect.'],78)
  txt(im,58,235,'A REAL IMMUNE CELL AT WORK',27,G)
  tag(im,60,540,'BACTERIA',n=30,c=C);line(im,[(280,590),(510,590),(680,590)],I,3)
  tag(im,55,1210,'NEUTROPHIL',n=30);line(im,[(335,1230),(230,1310),(125,1360)],I,3)
  
  if not MOTION or U>1.2:tag(im,470,1470,'THE CASE: SEPSIS',n=28)
  footer(im,['Human neutrophil ingesting MRSA · NIH / NIAID','False-colored SEM; still record, not time-lapse','This image shows defense, not a sepsis diagnosis.'])
  phrase='In sepsis, that response can harm your own organs.'
 elif scene==2:
  if headings:lines(im,56,110,['One failing','boundary.'],87,tc)
  tag(im,58,330,'VESSEL LINING · CONCEPTUAL SECTION',n=23)
  paste(im,tissue(1080,500,True),(0,1130))
  vessel(im,(-55,470,1190,400),leak=.65*(S((U-1.2)/2)if MOTION else 1),t=t,light=True)
  txt(im,56,412,'INSIDE THE BLOOD VESSEL',24,N)
  tag(im,620,879,'FLUID ESCAPES',n=26,c=C)
  # Enlarged junction is a separate, purpose-built component inspection below captions.
  paste(im,lining_cell(440,170,3),(45+35*(1-entry(1.2)),1200));paste(im,lining_cell(440,170,4),(570-35*(1-entry(1.2)),1220))
  for k in range(16 if not MOTION else round(16*S((U-1.2)/2))):
   x=518+math.sin(k*2)*20;y=1240+k*18;ImageDraw.Draw(im).ellipse((x-4,y-4,x+4,y+4),fill=(235,166,0))
  arrow(im,[(515,1140),(515,1190)],C,5);txt(im,60,1475,'Between neighboring lining cells',29,N)
  txt(im,60,1535,'Fluid crosses. Red cells remain inside.',27,N)
  footer(im,['Original conceptual model · geometry/colors not to scale','Barrier pathway: Brabenec et al., Nature Communications2026','One pathway in sepsis; not its complete mechanism.'],True)
  phrase='Inflammatory signals can make this barrier leaky.'
 elif scene==3:
  if headings:lines(im,56,110,['A blockage at','the wrong scale.'],80)
  tag(im,60,320,'CLOTTING CAN OBSTRUCT SMALL VESSELS',n=23,c=C)
  # Longitudinal obstruction with readable arrival and downstream outcome.
  paste(im,tissue(1080,490),(0,1190));vessel(im,(-65,425,1210,480),t=t,clot=True)
  tag(im,580,780,'CLOT',n=28,c=G);line(im,[(710,780),(725,730)],G,3)
  arrow(im,[(160,408),(360,408)],G,6);txt(im,60,365,'FLOW',26)
  # Registered normal-vs-obstructed comparison; same width/orientation, no faux quantitative scale.
  txt(im,54,1115,'Same vessel, two schematic conditions',30)
  vessel(im,(50,1190,980,210),t=t)
  vessel(im,(50,1440,980,210),t=t,clot=True)
  tag(im,70,1200,'OPEN',n=23);tag(im,70,1450,'OBSTRUCTED',n=23,c=C)
  footer(im,['Original conceptual model · no measured flow rate','Clotting and perfusion: NIH / NIGMS; WHO','Not every sepsis case has the same vascular changes.'])
  phrase='Clotting can also obstruct small vessels.'
 elif scene==4:
  if headings:lines(im,56,110,['The organ pays','the price.'],83)
  tag(im,58,330,'WHEN OXYGEN DELIVERY IS DISRUPTED',n=23,c=C)
  vessel(im,(-30,455,1150,300),t=t,clot=True)
  paste(im,tissue(1080,730),(0,1090))
  # Nonquantitative oxygen delivery symbols: lower density beyond selected obstruction.
  d=ImageDraw.Draw(im)
  for k in range(23):
   x=85+(k%6)*90;y=805+(k//6)*37;d.ellipse((x-5,y-5,x+5,y+5),fill=G)
  for x,y in [(120,1150),(200,1250),(290,1340),(350,1450)]:
   d.ellipse((x-7,y-7,x+7,y+7),fill=G)
  arrow(im,[(220,880),(220,940)],G,4)
  txt(im,60,1510,'Less delivery.',50,I,True)
  txt(im,60,1585,'Organ function can suffer.',34)
  footer(im,['Original model · gold dots symbolize oxygen delivery','No oxygen concentration, rate or patient outcome measured','Sepsis involves multiple interacting injury pathways.'])
  phrase='Organs can struggle to get the oxygen they need.'
 else:
  if headings:lines(im,56,120,['Protection needs','control.'],86,N)
  tag(im,58,348,'SEPSIS IS MORE THAN “TOO MUCH” IMMUNITY',n=23)
  hand=Image.open(A/'hand-original.png');hand.thumbnail((1250,900));paste(im,hand,(50+170*(1-entry()),650))
  tag(im,55,570,'DYSREGULATED INFLAMMATION',n=24,c=C)
  tag(im,210,1280,'SOME DEFENSES CAN BE SUPPRESSED',n=24,c=G)
  ImageDraw.Draw(im).rectangle((45,1425,1035,1625),fill=N)
  txt(im,70,1445,'SEPSIS IS A MEDICAL EMERGENCY',33,I)
  txt(im,70,1510,'Early treatment matters.',40,I,True)
  footer(im,['Mechanism context: WHO / CDC / NIH; Brabenec et al.2026','Original illustration is not a patient record','Exact Curio ending follows the complete spoken tail.'],True)
  phrase='Protection depends on control—not just force.'
 im=F.foreground(im,t)
 if captions:cap(im,phrase,light)
 txt(im,48,42,'CURIO BUREAU',22,N if light else G)
 return im

def main():
 labels=['01 · BODY / QUESTION','02 · REAL CELL / DEFENSE','03 · BARRIER / DIFFICULT STATE','04 · CLOT / COMPARISON','05 · DELIVERY / CONSEQUENCE','06 · CONTEXT / PAYOFF']
 board=Image.new('RGB',(1620,2000),N)
 for k,label in enumerate(labels):
  im=raw(k,2.4);im.save(R/f'{k+1:02}-art-review.jpg',quality=95,subsampling=0)
  x=k%3*540;y=k//3*1000;board.paste(im.resize((540,960),Image.Resampling.LANCZOS),(x,y));txt(board,x+12,y+966,label,16)
  raw(k,2.4,False,False).save(R/f'{k+1:02}-heading-hidden.jpg',quality=91)
 board.save(R/'whole-story-art-review.jpg',quality=95,subsampling=0)
 # Direct implementation proof for static effects only; temporal/moving evidence is pending.
 base=raw(2,2.4);F.DISABLED={'material_texture'};no_paper=raw(2,2.4);F.DISABLED={'moving_grain'};no_grain=raw(2,2.4);F.DISABLED=set()
 b=np.asarray(base,dtype=np.int16);npap=np.asarray(no_paper,dtype=np.int16);ng=np.asarray(no_grain,dtype=np.int16)
 proof={'status':'NATIVE_STATIC_ART_REVIEW_ONLY','size':[1080,1920],'paper_mean_absolute_rgb_difference':float(np.abs(b-npap).mean()),'foreground_grain_mean_absolute_rgb_difference':float(np.abs(b-ng).mean()),'caption_opaque_core_changed_pixels':int(np.any(b[990:1010,450:630]!=ng[990:1010,450:630],axis=2).sum()),'motion_focus_hunt_parallax':'PLANNED / NOT YET ENCODED','independent_listening':'NOT PERFORMED','owner_art_approval':'PENDING','actual_voice_timing':'NOT RECORDED; provisional planning only'}
 (R/'STATIC_FINISHING_PROOF.json').write_text(json.dumps(proof,indent=2)+'\n')
 print(json.dumps(proof))
if __name__=='__main__':main()
