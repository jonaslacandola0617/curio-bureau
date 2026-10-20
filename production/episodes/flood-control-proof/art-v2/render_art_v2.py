from pathlib import Path
import os,hashlib,json,math
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageFilter,ImageChops,ImageEnhance
HERE=Path(__file__).resolve().parent;OUT=HERE/'review';OUT.mkdir(exist_ok=True)
ROOT=Path(os.environ.get('CURIO_REPO_ROOT',str(HERE.parents[3])))
FP=ROOT/'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets'
N=(13,28,43);I=(245,240,231);G=(200,162,107);C=(213,120,100);B=(139,207,221)
W,H=1080,1920
RNG=np.random.default_rng(20261020)
def font(s,serif=False,weight=650):
 f=ImageFont.truetype(str(FP/('Playfair900.ttf' if serif else 'Manrope.ttf')),s)
 if not serif:f.set_variation_by_axes([weight])
 return f
def text(im,x,y,s,size=28,col=I,serif=False,anchor=None):ImageDraw.Draw(im).text((x,y),s,font=font(size,serif),fill=col,anchor=anchor)
def heading(im,ss):
 for i,s in enumerate(ss):text(im,62,158+i*88,s,78,I,True)
def tag(im,x,y,s,col=G,size=25):
 d=ImageDraw.Draw(im);w=d.textbbox((0,0),s,font=font(size))[2]+28;d.rectangle((x,y,x+w,y+size+22),fill=col);text(im,x+14,y+7,s,size,N)
def base(kind,light=False):
 im=Image.new('RGB',(W,H),I if light else N);d=ImageDraw.Draw(im)
 # Object surfaces carry material; background stays stable and subordinate.
 if not light:
  for y in range(310,1850,120):d.line((0,y,1080,y-36),fill=(17,34,49),width=1)
 col=N if light else I
 text(im,62,52,'CURIO BUREAU',22,G);text(im,1018,52,kind,19,col,anchor='ra');d.line((62,98,1018,98),fill=G,width=2)
 text(im,1018,112,'CONCEPTUAL ILLUSTRATION',23,C if light else G,anchor='ra')
 text(im,62,1824,'NOT A REAL PROJECT · NOT A HYDRAULIC RESULT',22,col)
 text(im,62,1864,'STATIC ART v2 / MOTION, FOCUS AND SOUND PENDING',19,col)
 return im
def caption(im,s,y=965):
 d=ImageDraw.Draw(im);w=d.textbbox((0,0),s,font=font(33))[2]+34;x=(W-w)//2
 d.rectangle((x,y-5,x+w,y+48),fill=(8,20,31));text(im,540,y,s,33,I,anchor='ma')
def cut(name):
 p=Image.open(HERE/'assets'/name).convert('RGBA');a=p.getchannel('A');a=a.point(lambda x:255 if x>235 else 0).filter(ImageFilter.MinFilter(3));p.putalpha(a)
 return p.crop(a.getbbox())
wall=cut('wall.webp');home=cut('home.webp');soil=Image.open(HERE/'assets/soil.webp').convert('RGB')
def placed(p,x,y,w=None,h=None):
 if h is not None:w=round(p.width*h/p.height)
 else:h=round(p.height*w/p.width)
 out=Image.new('RGBA',(W,H));p=p.resize((w,h),Image.Resampling.LANCZOS);out.alpha_composite(p,(x,y));return out
wallplane=placed(wall,155,500,h=1050);wallmask=wallplane.getchannel('A')
# Same source wall and exact alpha are used in all three main section states.
TERRAIN=Image.new('L',(W,H));ImageDraw.Draw(TERRAIN).polygon([(0,1490),(400,1490),(430,1250),(1080,1250),(1080,1920),(0,1920)],fill=255)
soilplane=Image.new('RGBA',(W,H));s=soil.resize((1080,720),Image.Resampling.LANCZOS);soilplane.paste(s,(0,1200));soilplane.putalpha(TERRAIN)
def water_surface(im,mask,phase=0,col=(40,128,157),strength=218):
 yy,xx=np.indices((H,W));arr=np.zeros((H,W,4),np.uint8)
 shade=np.clip(.78+.12*np.sin(yy*.012)+.05*np.cos(xx*.026+yy*.037),.6,1.06)
 for k,c in enumerate(col):arr[:,:,k]=np.clip(c*shade+10,0,255)
 # Promote before multiplication to retain physical alpha.
 arr[:,:,3]=(np.array(mask,dtype=np.uint16)*strength//255).astype('uint8')
 layer=Image.fromarray(arr);spec=Image.new('RGBA',(W,H));d=ImageDraw.Draw(spec)
 rr=np.random.default_rng(104+phase)
 for j in range(260):
  x=int(rr.integers(0,W));y=int(rr.integers(380,1730));l=int(rr.integers(8,83));d.line((x,y,x+l,y+rr.integers(-3,4)),fill=(177,230,232,int(rr.integers(35,130))),width=int(rr.integers(1,3)))
 for j in range(70):
  x=int(rr.integers(0,W));y=int(rr.integers(410,1610));r=int(rr.integers(1,4));d.ellipse((x-r,y-r,x+r,y+r),outline=(185,225,226,100),width=1)
 spec.putalpha(ImageChops.multiply(spec.getchannel('A'),mask));layer=Image.alpha_composite(layer,spec);im.alpha_composite(layer)
def fluid_mask(stage):
 m=Image.new('L',(W,H));d=ImageDraw.Draw(m)
 if stage<3:
  top=802 if stage==1 else 698
  points=[(0,top)]+[(x,top+3*math.sin(x*.035))for x in range(0,460,8)]+[(460,1490),(0,1490)]
  d.polygon(points,fill=255)
 else:
  d.polygon([(0,452),(390,452),(470,454),(564,459),(624,479),(657,533),(677,622),(672,925),(662,1152),(1080,1152),(1080,1250),(622,1250),(621,810),(620,555),(607,518),(550,514),(430,514),(430,1490),(0,1490)],fill=255)
 m=ImageChops.subtract(m,wallmask);m=ImageChops.subtract(m,TERRAIN)
 return m

def section(stage,hide_heading=False):
 im=base('WALL / GROUND / WATER').convert('RGBA')
 titles={1:['A wall is','only the start.'],2:['Look beneath','the surface.'],3:['And beyond','its limit?']}
 if not hide_heading:heading(im,titles[stage])
 im.alpha_composite(placed(home,820,987,w=245))
 ground=soilplane.copy()
 if stage>=2:
  # Front section is removed while the physical terrain remains the fluid exclusion mask.
  a=ground.getchannel('A');ImageDraw.Draw(a).polygon([(305,1260),(935,1260),(935,1550),(305,1550)],fill=0);ground.putalpha(a)
 im.alpha_composite(wallplane);im.alpha_composite(ground)
 if stage>=2:
  # Wall is revealed at the actual component, not redrawn as a generic T icon.
  im.alpha_composite(wallplane)
 water_surface(im,fluid_mask(stage),stage)
 d=ImageDraw.Draw(im)
 if stage<3:
  level=802 if stage==1 else 698;d.line((0,level,428,level),fill=(186,230,230),width=4)
  tag(im,62,600,'RIVER SIDE',size=24);tag(im,790,849,'HOME SIDE',size=24)
 else:
  d.line((0,452,390,452,470,454,564,459,624,479,657,533),fill=(192,238,235),width=4)
  for x in [642,653,664]:d.line((x,650,x-4,1090),fill=(181,229,230,160),width=2)
  tag(im,62,590,'ABOVE THE CREST',col=C,size=26)
  text(im,695,1333,'LANDWARD FLOW',27,B)
 if stage==2:
  tag(im,62,1620,'FOUNDATION EXPOSED IN SECTION',size=26)
  d.line((382,1618,458,1512),fill=G,width=3)
 elif stage==1:
  text(im,62,1640,'The buried part is still hidden.',35,I,True)
 else:
  text(im,62,1652,'A limit is not a corruption verdict.',35,I,True)
 caption(im,{1:'A completion photo cannot show the whole system.',2:'Inspect the foundation—not only the visible wall.',3:'Water can cross a barrier when it exceeds its crest.'}[stage])
 return im.convert('RGB')

def doorway(wet):
 im=base('HOME-LEVEL EVIDENCE').convert('RGBA');heading(im,['What reached','the doorstep?'] if wet else ['Check the model','against reality.'])
 im.alpha_composite(placed(home,40,450,w=1000))
 m=Image.new('L',(W,H));d=ImageDraw.Draw(m);level=1110 if wet else 1490
 points=[(0,level)]+[(x,level+4*math.sin(x*.028))for x in range(0,1081,8)]+[(1080,1650),(0,1650)];d.polygon(points,fill=255)
 # Physical water acts in front of the doorway; when it recedes the material stain is exposed.
 water_surface(im,m,7 if wet else 8,col=(43,125,146),strength=210 if wet else 190)
 if not wet:
  tag(im,62,1580,'ILLUSTRATIVE HIGH-WATER STAIN',size=25)
  ImageDraw.Draw(im).line((465,1580,342,1140),fill=G,width=3)
  text(im,62,1700,'Field records must check model estimates.',31,I)
 else:tag(im,62,1680,'ILLUSTRATION · NOT A FIELD RECORD',size=25)
 caption(im,'The water reaches a home—not a completion certificate.' if wet else 'Then check estimates against real observations.')
 return im.convert('RGB')

def comparison():
 im=base('CONTROLLED COMPARISON',light=True).convert('RGBA')
 lines=['Same input.','One change.']
 for i,s in enumerate(lines):text(im,62,158+i*88,s,78,N,True)
 # Two literal section models share terrain and input area; no real-world prediction is claimed.
 V=40000.;width=420.;left=180.;right=240.;bed=580.;land=460.;crest=340.
 level_with=bed-V/left;level_without=(left*bed+right*land-V)/width
 def tank(y,withwall):
  x=90;bar=x+378;rightedge=x+890
  def Y(z):return y+(z-300)*1.4
  bedy=round(Y(bed));landy=round(Y(land));bottom=round(Y(650))
  # One coordinate system controls the terrain, water, wall and home contact points.
  dr=ImageDraw.Draw(im)
  dr.polygon([(x,bottom),(rightedge,bottom),(rightedge+24,bottom-22),(rightedge+24,bottom+17),(rightedge,bottom+39),(x,bottom+39)],fill=(171,190,188,255))
  terrain=Image.new('L',(W,H));td=ImageDraw.Draw(terrain)
  td.polygon([(x,bedy),(bar,bedy),(bar,landy),(rightedge,landy),(rightedge,bottom),(x,bottom)],fill=255)
  material=Image.new('RGBA',(W,H));material.paste(soil.resize((890,500)),(x,y));material.putalpha(terrain);im.alpha_composite(material)
  localwall=None
  if withwall:
   wh=round(Y(620)-Y(crest));ww=round(wall.width*wh/wall.height)
   wa=wall.resize((ww,wh)).getchannel('A');row=np.array(wa)[round(wh*.35)]
   stemleft=int(np.flatnonzero(row>235)[0])
   localwall=placed(wall,bar-stemleft,round(Y(crest)),h=wh)
   im.alpha_composite(localwall)
  hw=210;hh=round(home.height*hw/home.width)
  im.alpha_composite(placed(home,x+675,landy-hh,w=hw))
  yy=Y(level_with if withwall else level_without)
  m=Image.new('L',(W,H));d=ImageDraw.Draw(m)
  d.rectangle((x+3,yy,rightedge-3,bedy),fill=255)
  if withwall:d.rectangle((bar,yy,rightedge,bedy),fill=0)
  m=ImageChops.subtract(m,terrain)
  if localwall is not None:m=ImageChops.subtract(m,localwall.getchannel('A'))
  water_surface(im,m,11 if withwall else 12,strength=205)
  dr=ImageDraw.Draw(im);dr.line((x,y+25,x,bottom,rightedge,bottom,rightedge,y+25),fill=(124,155,158),width=4)
  dr.line((x+8,y+30,x+8,bottom-8),fill=(239,250,244),width=3)
  tag(im,x,y-14,'WITH PROJECT' if withwall else 'WITHOUT PROJECT',G if withwall else C,26)
 tank(475,True);tank(1120,False)
 caption(im,'Change the project. Keep the forcing comparable.',y=1010)
 text(im,62,1755,'Equal-input teaching model · not a hydraulic simulation',25,N)
 return im.convert('RGB'),{'status':'synthetic teaching geometry only','unit_depth_input_area':V,'with_project_surface_y':level_with,'without_project_surface_y':level_without,'with_project_area':left*(bed-level_with),'without_project_area':left*(bed-level_without)+right*(land-level_without),'no_actual_project_result':True}
frames={'01-home-water':doorway(True),'02-wall-visible':section(1),'03-foundation-reveal':section(2),'04-overtopping':section(3),'04-overtopping-heading-hidden':section(3,True),'05-home-after-water':doorway(False)}
frames['06-matched-inputs'],calc=comparison()
for name,im in frames.items():
 im.save(OUT/(name+'.png'));im.save(OUT/(name+'.webp'),lossless=True,method=6)
# Scene-family proof: three different constructed visual problems, not six headings on one plate.
board=Image.new('RGB',(1440,875),N)
for i,name in enumerate(['01-home-water','04-overtopping','06-matched-inputs']):
 im=frames[name].resize((480,853),Image.Resampling.LANCZOS);board.paste(im,(i*480,0));text(board,i*480+18,855,['HOME / MATERIAL EVIDENCE','SECTION / FLUID BOUNDARY','MODEL / MATCHED INPUT'][i],15,I)
board.save(OUT/'art-v2-triptych.jpg',quality=96)
seq=Image.new('RGB',(1440,875),N)
for i,name in enumerate(['02-wall-visible','03-foundation-reveal','04-overtopping']):
 seq.paste(frames[name].resize((480,853),Image.Resampling.LANCZOS),(i*480,0));text(seq,i*480+18,855,['VISIBLE WALL','BURIED SECTION REVEALED','CREST EXCEEDED'][i],15,I)
seq.save(OUT/'wall-operation-states.jpg',quality=96)
(HERE/'ILLUSTRATIVE_GEOMETRY.json').write_text(json.dumps(calc,indent=2)+'\n')
receipt={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size':Image.open(p).size}for p in sorted(OUT.glob('*'))}
(HERE/'RENDER_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'frames':list(frames),'archival_bytes':sum(p.stat().st_size for p in OUT.glob('*.webp')),'geometry':calc},indent=2))
