from pathlib import Path
import os,json,math,subprocess,sys,hashlib
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps,ImageFilter,ImageEnhance
from functools import lru_cache
P=Path(__file__).resolve().parent;ROOT=Path(os.getenv('CURIO_REPO_ROOT',str(P.parents[3])));A=P/'assets';R=P/'review';R.mkdir(exist_ok=True)
TL=json.loads((P/'timeline.json').read_text());W,H=1080,1920;N=(13,28,43);I=(245,240,231);G=(200,162,107);C=(213,120,100);B=(88,191,229)
FP=ROOT/'production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets'
@lru_cache(100)
def font(s,serif=False):
 f=ImageFont.truetype(str(FP/('Playfair900.ttf'if serif else'Manrope.ttf')),s)
 if not serif:f.set_variation_by_axes([650])
 return f
def txt(im,x,y,s,n=30,c=I,serif=False,anchor=None):ImageDraw.Draw(im).text((x,y),s,font=font(n,serif),fill=c,anchor=anchor)
def multi(im,x,y,ss,n=80,c=I,serif=True):
 for k,s in enumerate(ss):txt(im,x,y+k*n*1.16,s,n,c,serif)
def tag(im,x,y,s,c=G,n=24):
 d=ImageDraw.Draw(im);w=d.textbbox((0,0),s,font=font(n))[2]+26;d.rectangle((x,y,x+w,y+n+20),fill=c);txt(im,x+13,y+6,s,n,N)
def smooth(v):v=max(0,min(1,v));return v*v*(3-2*v)
def paste(im,src,box,blur=0):
 x,y,w,h=map(round,box);q=ImageOps.fit(src,(w,h),method=Image.Resampling.LANCZOS)
 if blur:q=q.filter(ImageFilter.GaussianBlur(blur))
 im.paste(q,(x,y))
@lru_cache(18)
def frame(kind,tick):
 fs=sorted((P/'frames'/kind).glob('*.jpg'));index=max(0,min(len(fs)-1,tick));return Image.open(fs[index]).convert('RGB')
mp=Image.open(A/'official-comparison.jpg').convert('RGB');basin=Image.open(A/'imus-basin.jpeg').convert('RGB');marker=Image.open(A/'imus-marker.jpeg').convert('RGB');excerpt=Image.open(A/'jica-excerpt.png').convert('RGB')
BND=TL['scene_boundaries']
def credit(im,s,light=False):
 txt(im,54,1765,s,23,N if light else I)
 txt(im,54,1810,'Source material: USACE / DVIDS; JICA evaluation',20,N if light else G)
 txt(im,54,1850,'U.S. government imagery does not imply endorsement.',19,N if light else I)
def caption(im,t):
 cap=next((a for a in TL['captions']if a['start']<=t<a['end']),None)
 if cap:
  s=cap['text'];n=35
  while ImageDraw.Draw(im).textbbox((0,0),s,font=font(n))[2]>978:n-=1
  ww=ImageDraw.Draw(im).textbbox((0,0),s,font=font(n))[2]+30;x=(W-ww)//2
  ImageDraw.Draw(im).rectangle((x,977,x+ww,1035),fill=N);txt(im,540,984,s,n,I,anchor='ma')
def contain(im,src,box):
 x,y,w,h=map(round,box);q=src.copy();q.thumbnail((w,h),Image.Resampling.LANCZOS);ImageDraw.Draw(im).rectangle((x,y,x+w,y+h),fill=(255,255,255));im.paste(q,(x+(w-q.width)//2,y+(h-q.height)//2))
def source_crop(centerx,centery,width):
 hh=width*1.3;return mp.crop((centerx-width/2,centery-hh/2,centerx+width/2,centery+hh/2))
def raw(t,headings=True,caps=True):
 # All authored state changes evaluate at12fps. Source footage is sampled at real elapsed time.
 qt=math.floor((t+1e-8)*12)/12;k=max(i for i,b in enumerate(BND)if qt>=b) if qt>=0 else 0;k=min(k,8);u=qt-BND[k];im=Image.new('RGB',(W,H),N)
 if k==0:
  q=frame('hickory',round(qt*12));paste(im,q,(0,430,1080,1250));ImageDraw.Draw(im).rectangle((0,0,1080,430),fill=N)
  if headings:
   multi(im,54,120,['Real footage.'],99)
   if u>2.3:tag(im,54,275,'HOW MUCH PROTECTION?',n=34)
  tag(im,54,1600,'OLD HICKORY DAM · 16 FEB 2025',n=24);credit(im,'USACE / San Luciano Vera · DVIDS 952614')
 elif k==1:
  q=frame('cordell',round((u+6)*12));paste(im,q,(0,0,1080,1920));ImageDraw.Draw(im).rectangle((0,0,1080,435),fill=N);ImageDraw.Draw(im).rectangle((0,1705,1080,1920),fill=N)
  if headings:multi(im,54,118,['Cumberland','River Basin'],87)
  tag(im,54,1500,'TENNESSEE, USA · FEBRUARY 2025',n=25);credit(im,'Cordell Hull Dam · USACE / Michael Davis · DVIDS 952620')
 elif k==2:
  # Retain the official source colors and geography; no new flood shapes are drawn.
  v=smooth(u/1.1);paste(im,mp,(0,430,1080,590));q=frame('hickory',round((u+18)*12));paste(im,q,(0,1090,1080,590))
  if headings:multi(im,54,130,['The published','comparison.'],82)
  if qt>=15.48232:
   roi=(550,300,1250,680);paste(im,mp.crop(roi),(0,1090,1080,590))
   # Exact source-pixel inspection box, not a new inundation boundary.
   sx=1080/mp.width;sy=590/mp.height;ImageDraw.Draw(im).rectangle((roi[0]*sx,430+roi[1]*sy,roi[2]*sx,430+roi[3]*sy),outline=G,width=4)
   tag(im,54,1100,'BLUE: WITH PROJECTS',B,29)
  if qt>=19.12232:tag(im,54,1180,'RED: ESTIMATED WITHOUT',C,29)
  ImageDraw.Draw(im).rectangle((0,1550,1080,1710),fill=N)
  txt(im,54,1610,'Same event. Two conditions.',37,I,True);credit(im,'USACE graphic 8910491 · published March 2025')
 elif k==3:
  q=source_crop(1040,570,700);paste(im,q,(0,430,1080,1250),blur=max(0,1-smooth(u/.45))*1.6)
  if headings:multi(im,54,120,['A counterfactual.'],84)
  tag(im,54,310,'ESTIMATED WITHOUT PROJECTS',C,27)
  ImageDraw.Draw(im).rectangle((0,1545,1080,1720),fill=N);multi(im,54,1570,['A modelled alternative.','Not another recorded flood.'],36,I,False);credit(im,'Source map retained · magnified source region')
 elif k==4:
  q=frame('hickory',round((u+28)*12));paste(im,q,(0,410,1080,1260));ImageDraw.Draw(im).rectangle((0,0,1080,410),fill=N)
  if headings:
   txt(im,54,125,'$734 million',106,I,True);tag(im,54,285,'USACE ESTIMATE',n=32)
  if u>3.7:
   ImageDraw.Draw(im).rectangle((54,1180,1026,1450),fill=N);multi(im,84,1215,['Avoided damage across','the Cumberland River Basin'],39,I,False)
  if u>6.1:tag(im,54,1550,'PRELIMINARY ANALYSIS',C,29)
  credit(im,'USACE analysis · published 12 March 2025')
 elif k==5:
  im=Image.new('RGB',(W,H),I);paste(im,basin,(0,420,1080,615));paste(im,marker,(560,1160,520,450))
  if headings:multi(im,54,120,['A different record.','Imus, Philippines.'],72,N)
  tag(im,54,1055,'INTERVIEWS REPORTED IMPROVEMENT',G,24)
  contain(im,excerpt,(54,1170,470,70));txt(im,54,1280,'Actual report excerpt',23,N)
  if u>4.8:
   ImageDraw.Draw(im).rectangle((54,1370,990,1565),fill=N);multi(im,80,1400,['Comparable flooded-area and','household actual values unavailable'],33,I,False)
  txt(im,54,1645,'Overall project evaluation: satisfactory.',29,N);credit(im,'JICA FY2023 evaluation · printed pp.1, 14–15',True)
 elif k==6:
  paste(im,basin,(0,450,1080,610));paste(im,marker,(0,1130,1080,590))
  if headings:multi(im,54,135,['Missing data'],92);tag(im,54,300,'DOES NOT MEAN ZERO BENEFIT',n=31)
  credit(im,'Actual Imus project photos · JICA / DPWH')
 elif k==7:
  # Question-led source hand-offs: actual event -> published comparison -> field record.
  if u<2.5:
   q=frame('cordell',round((u+45)*12));paste(im,q,(0,420,1080,1290));label='1  THE EVENT RECORD'
  elif u<5:
   paste(im,mp,(0,440,1080,610));paste(im,frame('hickory',round((u+38)*12)),(0,1110,1080,580));label='2  WITH / WITHOUT COMPARISON'
  else:
   paste(im,marker,(0,450,1080,665));contain(im,excerpt,(54,1280,972,145));label='3  CHECKS AGAINST OBSERVATIONS'
  if headings:multi(im,54,140,['Ask for the proof.'],83)
  tag(im,54,320,label,n=25);credit(im,'Distinct source roles · footage / estimate / field evidence')
 else:
  q=frame('hickory',round((u+50)*12));paste(im,q,(0,440,1080,1260))
  if headings:
   multi(im,54,130,['How much safer?'],86)
   if u>1.2:tag(im,54,310,'FOR WHOM?',n=31)
   if u>2.1:tag(im,54,1420,'HOW DO YOU KNOW?',n=31)
  credit(im,'How do you prove a flood-control project protects anyone?')
 # Source finishing is local and restrained; do not corrupt documentary colors or type.
 if caps:caption(im,t)
 txt(im,54,45,'CURIO BUREAU',22,G)
 return im

def stills():
 for j,t in enumerate([1.8,9,16.4,20,24,29.5,33.5,38,42.3,46.5,50,54.2,58.5]):raw(t).save(R/f'{j+1:02}-{t:.1f}s.jpg',quality=96,subsampling=0)
 board=Image.new('RGB',(1620,1960),N)
 for k,t in enumerate([1.8,16.4,24,29.5,42.3,54.2]):
  board.paste(raw(t).resize((540,960)),(k%3*540,k//3*980));txt(board,k%3*540+15,k//3*980+963,f'{t:.1f}s · ACTUAL SOURCE MATERIAL',14)
 board.save(R/'real-records-board.jpg',quality=96)
 raw(20,False,False).save(R/'heading-hidden-map.jpg',quality=96)
 raw(TL['ending_start']-.04).save(P/'ending-base.png')
def movie():
 out=P/'Curio-Flood-Proof-Real-Records-v5.mp4'
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pixel_format','rgb24','-s','1080x1920','-r','30','-i','-','-i',str(P/'audio/soundtrack.flac'),'-c:v','libx264','-preset','fast','-b:v','12M','-maxrate','16M','-bufsize','24M','-pix_fmt','yuv420p','-c:a','aac','-b:a','320k','-ar','48000','-ac','2','-movflags','+faststart',str(out)]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE);last=-1;buf=None;endstart=round(TL['ending_start']*30)
 for n in range(TL['frames']):
  if n>=endstart:im=Image.open(P/'ending'/f'{n-endstart:03}.png').convert('RGB');buf=im.tobytes()
  else:
   tick=math.floor((n/30+1e-8)*12)
   if tick!=last:buf=raw(tick/12).tobytes();last=tick
  proc.stdin.write(buf)
  if n%180==0:print('rendered_seconds',n/30,flush=True)
 proc.stdin.close();assert proc.wait()==0;print('ENCODED_ARCHIVE_PENDING',out.stat().st_size,hashlib.sha256(out.read_bytes()).hexdigest(),flush=True)
def chunk(start,end,file):
 cmd=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pixel_format','rgb24','-s','1080x1920','-r','30','-i','-','-an','-c:v','libx264rgb','-crf','0','-preset','veryfast','-threads','2',str(file)]
 proc=subprocess.Popen(cmd,stdin=subprocess.PIPE);last=-1;buf=None;endstart=round(TL['ending_start']*30)
 for n in range(start,end):
  if n>=endstart:buf=Image.open(P/'ending'/f'{n-endstart:03}.png').convert('RGB').tobytes()
  else:
   tick=math.floor((n/30+1e-8)*12)
   if tick!=last:buf=raw(tick/12).tobytes();last=tick
  proc.stdin.write(buf)
 proc.stdin.close();assert proc.wait()==0;print('CLOSED_CHUNK',start,end,str(file),flush=True)
if __name__=='__main__':
 if '--chunk'in sys.argv:chunk(int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
 else:
  stills()
  if '--video'in sys.argv:movie()
