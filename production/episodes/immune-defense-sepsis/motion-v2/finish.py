"""Deterministic source-local material/optical stack; never applied to type or ending."""
from functools import lru_cache
import math
import numpy as np
from PIL import Image, ImageFilter

EFFECTS={'material_texture','moving_grain','motion_blur','selective_focus','focus_shading','focus_hunt','chromatic','mechanical_jitter','exposure','ink_bleed','edge_boil'}
DISABLED=set()
def active(name):return name not in DISABLED

@lru_cache(32)
def field(w,h,seed,coarse=False):
 rng=np.random.default_rng(seed)
 if coarse:
  x=rng.normal(0,1,(max(2,h//9),max(2,w//9))).astype(np.float32)
  return np.asarray(Image.fromarray(x,mode='F').resize((w,h),Image.Resampling.BILINEAR))
 return rng.normal(0,1,(h,w)).astype(np.float32)

@lru_cache(8)
def backing(w,h,light=False,enabled=True):
 # Background is the locked brand color. Material is composited at the front.
 return Image.new('RGB',(w,h),(245,240,231)if light else(13,28,43))

def hunt_envelope(u):
 if u<0 or u>.68:return 0
 # Initial rack, brief overshoot, then a sharp reading hold.
 return 5.5*math.exp(-((u-.15)/.105)**2)+2.0*math.exp(-((u-.39)/.09)**2)

def source(im,t,kind='photo',focus=None,hunt=0,moving=0):
 im=im.convert('RGB');w,h=im.size
 a=np.asarray(im,dtype=np.float32)
 if active('exposure'):a*=1+.008*math.sin(math.floor(t*6)*1.73)
 a=np.uint8(np.clip(a,0,255))
 if active('chromatic') and kind!='print':
  # At most one native pixel; no displaced map legend or scientific marks.
  a[:,:,0]=np.roll(a[:,:,0],1,axis=1)
  a[:,:,2]=np.roll(a[:,:,2],-1,axis=1)
 im=Image.fromarray(a)
 if focus is not None:
  cx,cy=focus;yy,xx=np.mgrid[:h,:w]
  f=np.clip((((xx/w-cx)/.72)**2+((yy/h-cy)/.48)**2-.18)/.9,0,1)
  if active('selective_focus'):
   mask=Image.fromarray(np.uint8(f*220)).filter(ImageFilter.GaussianBlur(18))
   im=Image.composite(im.filter(ImageFilter.GaussianBlur(2.7)),im,mask)
  if active('focus_shading'):
   # Exactly the same spatial field drives surrounding luminance and defocus.
   z=np.asarray(im,dtype=np.float32)*(1-.14*f[:,:,None]);im=Image.fromarray(np.uint8(z))
 if hunt and active('focus_hunt'):im=im.filter(ImageFilter.GaussianBlur(hunt))
 if moving and active('motion_blur'):
  # Finite multi-tap source integration, not a blurred type shadow.
  a=np.asarray(im,dtype=np.float32);dx=max(1,round(moving*5))
  a=(a*.5+np.roll(a,dx,axis=1)*.25+np.roll(a,-dx,axis=1)*.25)
  im=Image.fromarray(np.uint8(a))
 return im

def jitter(t,amount=1.3):
 if not active('mechanical_jitter'):return 0,0
 q=math.floor(t*6);return round(math.sin(q*2.31)*amount),round(math.cos(q*1.83)*amount*.6)

@lru_cache(6)
def paper_sheet(w,h):
 """Neutral paper formation and individual fibers; no cloudy background noise."""
 from PIL import ImageDraw
 rng=np.random.default_rng(20261021)
 formation=rng.normal(0,1,(max(3,h//24),max(3,w//24))).astype(np.float32)
 formation=np.asarray(Image.fromarray(formation,mode='F').resize((w,h),Image.Resampling.BICUBIC))
 tooth=rng.normal(0,1,(h,w)).astype(np.float32)
 fibers=Image.new('L',(w,h),128);d=ImageDraw.Draw(fibers)
 for k in range(round(w*h/650)):
  x=float(rng.uniform(-35,w));y=float(rng.uniform(-15,h));length=float(rng.uniform(7,53))
  slope=float(rng.normal(-.12,.23));shade=int(rng.choice([91,103,151,164]))
  d.line((x,y,x+length,y+length*slope),fill=shade,width=1 if k%5 else 2)
 f=np.asarray(fibers.filter(ImageFilter.GaussianBlur(.42)),dtype=np.float32)-128
 sheet=formation*3.2+tooth*2.1+f*.48
 sheet-=float(sheet.mean())
 return sheet.astype(np.float32)

@lru_cache(16)
def grain_bank(k):
 # Port of the established Cold Metal foreground grain bank, not background fill.
 rng=np.random.default_rng(9182+k*7717)
 n=128+(rng.random((512,512))+rng.random((512,512))-1)*115
 return np.asarray(Image.fromarray(np.uint8(n)).resize((1024,1024),Image.Resampling.NEAREST),dtype=np.float32)/255

def foreground(im,t):
 """Paper layer, then moving soft-light film grain OVER the assembled artwork.

 No geometry, color category, optical envelope or image/camera transform is changed.
 Caller adds the unchanged captions afterward; the locked ending bypasses this pass.
 """
 if not active('material_texture')and not active('moving_grain'):return im
 a=np.asarray(im,dtype=np.float32)/255;h,w=a.shape[:2]
 if active('material_texture'):
  # Zero-mean multiply keeps the brand hue; actual fibers read on light surfaces.
  a=np.clip(a*(1+paper_sheet(w,h)[:,:,None]*.0042),0,1)
 if active('moving_grain'):
  tick=int(math.floor((t+1e-8)*12));g=grain_bank(tick%16)
  ys=(np.arange(h)+(tick*83)%1024)%1024;xs=(np.arange(w)+(tick*137)%1024)%1024
  s=g[np.ix_(ys,xs)][:,:,None]
  root=np.where(a<=.25,((16*a-12)*a+4)*a,np.sqrt(a))
  mixed=np.where(s<=.5,a-(1-2*s)*a*(1-a),a+(2*s-1)*(root-a))
  a=a*.66+mixed*.34
 return Image.fromarray(np.uint8(np.clip(a*255+.5,0,255)))
