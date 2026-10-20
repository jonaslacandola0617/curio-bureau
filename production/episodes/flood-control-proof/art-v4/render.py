from pathlib import Path
import math,os,json,hashlib,subprocess,sys
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops,ImageOps,ImageEnhance
P=Path(__file__).resolve().parent;A=P/'assets';O=P/'review';O.mkdir(exist_ok=True)
ROOT=Path(os.getenv('CURIO_REPO_ROOT',str(P.parents[3])))
F=ROOT/'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets'
FOCUS=0
W,H=1080,1920;NAVY=(13,28,43);IVORY=(245,240,231);GOLD=(200,162,107);CORAL=(211,120,99);BLUE=(129,194,204)
def f(n,serif=False):
 a=ImageFont.truetype(str(F/('Playfair900.ttf'if serif else'Manrope.ttf')),n)
 if not serif:a.set_variation_by_axes([650])
 return a
FONT={}
def tx(im,xy,s,n=30,c=IVORY,serif=False,anchor=None):
 key=(n,serif)
 if key not in FONT:FONT[key]=f(n,serif)
 ImageDraw.Draw(im).text(xy,s,font=FONT[key],fill=c,anchor=anchor)
def lines(im,xy,ss,n=76,c=IVORY,serif=True,gap=1.16):
 for j,s in enumerate(ss):tx(im,(xy[0],xy[1]+j*n*gap),s,n,c,serif)
def ease(x):x=max(0,min(1,x));return x*x*(3-2*x)
def tag(im,xy,s,c=GOLD,n=23):
 font=f(n);d=ImageDraw.Draw(im);b=d.textbbox((0,0),s,font=font);w=b[2]+24;d.rectangle((xy[0],xy[1],xy[0]+w,xy[1]+n+18),fill=c);tx(im,(xy[0]+12,xy[1]+5),s,n,NAVY)
def caption(im,s):
 d=ImageDraw.Draw(im);bb=d.textbbox((0,0),s,font=f(33));ww=bb[2]+34;d.rectangle(((W-ww)//2,978,(W+ww)//2,1035),fill=NAVY);tx(im,(540,983),s,33,IVORY,anchor='ma')
def base(light=False):
 im=Image.new('RGB',(W,H),IVORY if light else NAVY)
 tx(im,(58,44),'CURIO BUREAU',22,GOLD)
 return im
hero=Image.open(A/'crest-crossing.webp').convert('RGB');terrain=Image.open(A/'terrain.webp').convert('RGB').resize((1000,1000))
water=Image.open(A/'real-water.jpg').convert('RGB');field=Image.open(A/'imus-warning-marker.jpeg').convert('RGB');paper=Image.open(A/'jica-excerpt-mount.png').convert('RGB')
concrete=Image.open(A/'concrete-source.webp').convert('RGB').crop((380,350,540,900)).resize((1000,1000))
# Source-local polygons traced on this generated dry terrain; no measured geography.
channel=Image.new('L',(1000,1000));ImageDraw.Draw(channel).polygon([(110,0),(176,146),(170,332),(110,565),(0,817),(0,1000),(235,1000),(240,842),(267,667),(333,444),(391,207),(357,0)],fill=255)
wallpath=[(360,0),(393,205),(335,445),(270,670),(242,842),(237,1000)]
wmask=Image.new('L',(1000,1000));ImageDraw.Draw(wmask).line(wallpath,fill=255,width=26,joint='curve')
texture=water.resize((1100,1100),Image.Resampling.LANCZOS)
# All tiles share the SAME dry source and channel mask, not two separately generated places.
def model(phase=0,wall=True):
 im=terrain.copy();off=int(phase*28)%80;watercrop=texture.crop((20,off,1020,off+1000));im.paste(watercrop,(0,0),channel)
 if wall:
  im.paste(concrete,(0,0),wmask);d=ImageDraw.Draw(im);d.line([(x+7,y)for x,y in wallpath],fill=(53,59,55),width=5,joint='curve');d.line([(x-6,y)for x,y in wallpath],fill=(205,201,185),width=3,joint='curve')
 return im
models={k:model(0,k)for k in [False,True]}
def place(im,src,box,angle=0,alpha=1):
 x,y,w,h=map(round,box);a=ImageOps.fit(src,(w,h),method=Image.Resampling.LANCZOS).convert('RGBA')
 if FOCUS:a=a.filter(ImageFilter.GaussianBlur(FOCUS))
 if angle:a=a.rotate(angle,resample=Image.Resampling.BICUBIC,expand=True)
 if alpha<1:a.putalpha(round(255*alpha))
 im.paste(a,(x,y),a)
def lens(im,src,sourcebox,center,radius=190):
 crop=ImageOps.fit(src.crop(sourcebox),(radius*2,radius*2),method=Image.Resampling.LANCZOS)
 m=Image.new('L',crop.size);ImageDraw.Draw(m).ellipse((0,0,radius*2-1,radius*2-1),fill=255)
 x,y=center;im.paste(crop,(round(x-radius),round(y-radius)),m);d=ImageDraw.Draw(im);d.ellipse((x-radius,y-radius,x+radius,y+radius),outline=GOLD,width=9);d.ellipse((x-radius+12,y-radius+12,x+radius-12,y+radius-12),outline=IVORY,width=2)
def finish(im,s,light=False):
 tx(im,(58,1814),s,22,NAVY if light else IVORY)
 tx(im,(58,1860),'SILENT VISUAL STUDY · NOT A PROJECT PERFORMANCE RESULT',19,NAVY if light else GOLD)
 return im
# Native captions are prospective reading guides; they are not verified voice timings.
def scene(k,u,headings=True):
 global FOCUS
 t=u*4;FOCUS=(1-ease(t/.45))*2.4 if k in [0,3] else 0
 if k==0:
  im=base();place(im,hero,(-110,140,1250,1680))
  if headings:
   tx(im,(58,190),'Built.',128,IVORY,True)
   ImageDraw.Draw(im).rectangle((48,350,710,475),fill=GOLD)
   tx(im,(58,340),'Protected?',105,NAVY,True)
  v=ease((t-.5)/2.4);sx=520+380*v;sy=575+225*v
  # An inspection inset follows an actual source point; its leader shares that mapping.
  scale=1250/hero.width;crop_y=(hero.height*scale-1680)/2
  target=(-110+sx*scale,140+sy*scale-crop_y)
  ImageDraw.Draw(im).line((target[0],target[1],750,1165),fill=GOLD,width=3)
  lens(im,hero,(sx-120,sy-120,sx+120,sy+120),(750,1350),180)
  caption(im,'A visible wall is not a measure of protection.')
  tag(im,(58,1650),'FICTIONAL MODEL',n=23)
  return finish(im,'The question is the benefit—not only the structure.')
 if k==1:
  im=base();v=ease((t-.25)/1.5)
  # Water/source remains fixed while the intervention material is progressively added.
  mo=model(u,False);a=wmask.copy();ImageDraw.Draw(a).rectangle((0,round(1000*v),1000,1000),fill=0);mo.paste(models[True],(0,0),a)
  place(im,mo,(40,490,1000,1000))
  if headings:lines(im,(58,145),['Build the','comparison.'],83)
  tag(im,(58,1525),'ONE FICTIONAL SITE · SEPARATE PROJECT LAYER',n=23)
  caption(im,'Run the same storm with and without the project.')
  tx(im,(58,1650),'Terrain and homes stay fixed.',34,GOLD)
  return finish(im,'Conceptual scenario setup · results not calculated')
 if k==2:
  im=base(True)
  if headings:lines(im,(58,135),['Same storm.','One change.'],86,NAVY)
  # Same crop/scale/geometry in both panels; no invented flood-benefit output.
  for j,has in enumerate([True,False]):
   y=480+j*630;mo=model(u,has)
   if not has and t<1.8:
    # The second scenario initially inherits the same project; remove only its material.
    keep=wmask.copy();ImageDraw.Draw(keep).rectangle((0,0,1000,round(1000*ease((t-.4)/1.1))),fill=0);mo.paste(models[True],(0,0),keep)
   place(im,mo,(58,y,964,560));tag(im,(78,y+18),'WITH PROJECT'if has else('REMOVE PROJECT'if t<1.6 else'WITHOUT PROJECT'),GOLD if has else CORAL,26)
   for n in range(17):
    x=100+n*54;yy=y+100+int((t*80+n*31)%390);ImageDraw.Draw(im).line((x,yy,x-9,yy+31),fill=(235,241,234),width=2)
  caption(im,'Hold the other starting conditions comparable.')
  tx(im,(58,1690),'Same terrain. Same exposed homes. Same forcing.',27,NAVY)
  return finish(im,'Scenario setup only · no simulated protection estimate',True)
 if k==3:
  im=base();place(im,paper,(530,640,560,1080),angle=-8)
  # Actual site image replaces the conceptual model. The source remains distinct.
  place(im,field,(30,480,1020,635),angle=0)
  v=ease((t-.5)/1.6);cx=770-180*v;cy=1260+90*v
  ImageDraw.Draw(im).line((850,880,cx,cy-230),fill=GOLD,width=3)
  lens(im,field,(330,70,390,250),(cx,cy),230)
  if headings:lines(im,(58,145),['Check the','field evidence.'],82)
  caption(im,'Then test estimates against real observations.')
  tag(im,(58,425),'ACTUAL IMUS SOURCE PHOTO · JICA / DPWH',n=22)
  ImageDraw.Draw(im).rectangle((0,1635,1080,1710),fill=NAVY)
  tx(im,(58,1650),'A warning marker is not a continuous gauge record.',28,IVORY)
  return finish(im,'JICA FY2023 evaluation · printed p.15, Photo 3')
 if k==4:
  im=base(True);place(im,paper,(-70,330,920,1300),angle=5)
  if headings:lines(im,(58,145),['What the record','actually says.'],78,NAVY)
  # Keep the two kinds of evidence visible together; never recode missing as zero.
  v=ease((t-.25)/.65);x=round(1080-(1080-190)*v)
  ImageDraw.Draw(im).rectangle((x,585,x+805,845),fill=NAVY)
  tx(im,(x+30,615),'REPORTED IMPROVEMENT',25,GOLD);lines(im,(x+30,663),['Residents and a company','described less flooding.'],39,IVORY,False)
  v=ease((t-1.8)/.7);x=round(-900+1070*v)
  ImageDraw.Draw(im).rectangle((x,1130,x+820,1430),fill=CORAL)
  tx(im,(x+30,1160),'COMPARABLE MEASUREMENTS',25,NAVY);lines(im,(x+30,1210),['Flooded-area and household','actual values were unavailable.'],36,NAVY,False)
  caption(im,'Reported improvement. A measurement gap remains.')
  tx(im,(58,1580),'Overall project evaluation: satisfactory.',30,NAVY)
  tx(im,(58,1650),'Imus finding ≠ a verdict on every flood project.',28,NAVY)
  return finish(im,'JICA FY2023 · study Aug 2023–Nov 2024 · pp.1, 14–15',True)
 im=base();place(im,model(u,True),(650,150,500,620),angle=-7)
 place(im,field,(600,1110,530,540),angle=0,alpha=ease((t-.8)/.6))
 place(im,paper,(58,1380,400,350),angle=3,alpha=ease((t-1.8)/.6))
 if headings:
  lines(im,(58,180),['Ask for','the proof.'],92)
  lines(im,(58,725),['How much risk','is reduced?'],45,GOLD,False)
  if t>=.8:lines(im,(58,1160),['Who','benefits?'],61,IVORY,True)
  if t>=1.8:lines(im,(520,1670),['How verified?'],49,IVORY,True)
 caption(im,'How much safer—and how do you know?')
 return finish(im,'Modelled benefit + field checks + transparent limitations')
TIMES=[2.6,6.6,10.6,14.6,19.3,22.5]
if __name__=='__main__':
 for k,t in enumerate(TIMES):scene(k,(t-k*4)/4).save(O/f'{k+1:02}-scene.jpg',quality=96,subsampling=0)
 board=Image.new('RGB',(1620,1960),NAVY)
 for k,t in enumerate(TIMES):
  a=scene(k,(t-k*4)/4).resize((540,960));board.paste(a,(k%3*540,k//3*980));tx(board,(k%3*540+18,k//3*980+961),['01 / THE CLAIM','02 / THE MISSING COMPARISON','03 / THE CONTROL','04 / THE REALITY CHECK','05 / THE EVIDENCE LIMIT','06 / THE PAYOFF'][k],15,IVORY)
 board.save(O/'complete-sequence-board.jpg',quality=96)
 scene(2,.6,False).save(O/'heading-hidden-comparison.jpg',quality=96)
 if '--video' in sys.argv:
  out=P/'Flood-Proof-Visual-Study-v4b.mp4'
  cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pix_fmt','rgb24','-s','1080x1920','-r','12','-i','-','-vf','fps=30','-c:v','libx264','-preset','fast','-crf','18','-maxrate','16M','-bufsize','32M','-pix_fmt','yuv420p','-movflags','+faststart',str(out)]
  proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
  for i in range(288):
   t=i/12;k=min(5,int(t//4));im=scene(k,(t-k*4)/4)
   proc.stdin.write(im.tobytes())
   if i%48==0:print('rendered_seconds',i/12,flush=True)
  proc.stdin.close();assert proc.wait()==0
  print('video_bytes',out.stat().st_size,flush=True)
 receipt={str(p.relative_to(P)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}for p in O.glob('*.jpg')}
 (P/'RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
