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
 base=np.array([245,240,231]if light else[13,28,43],dtype=np.float32)
 yy,xx=np.mgrid[:h,:w]
 if enabled:
  # Coarse fibers, fine tooth and gentle laid-paper ridges are separate scales.
  a=field(w,h,419,True)*7+field(w,h,701)*2.4
  a+=np.sin(yy*.61+np.sin(xx*.018))*1.3
  a+=np.cos(xx*.34+np.sin(yy*.011))*1.1
 else:a=np.zeros((h,w))
 return Image.fromarray(np.uint8(np.clip(base[None,None,:]+a[:,:,None],0,255)))

def hunt_envelope(u):
 if u<0 or u>.68:return 0
 # Initial rack, brief overshoot, then a sharp reading hold.
 return 5.5*math.exp(-((u-.15)/.105)**2)+2.0*math.exp(-((u-.39)/.09)**2)

def source(im,t,kind='photo',focus=None,hunt=0,moving=0):
 im=im.convert('RGB');w,h=im.size
 a=np.asarray(im,dtype=np.float32)
 if active('material_texture'):
  # A print has tooth; actual footage receives finer film texture, never fake water.
  amplitude=4.2 if kind=='print' else 2.5 if kind=='photo' else 1.0
  tooth=field(w,h,74,True)*amplitude+field(w,h,93)*amplitude*.48
  a+=tooth[:,:,None]
 if active('moving_grain'):
  bank=int(math.floor((t+1e-8)*12))%24
  grain=field(w,h,900+bank)*2.7+field(w,h,500+bank,True)*2.1
  a+=grain[:,:,None]
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
