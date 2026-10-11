#!/usr/bin/env python3
import asyncio,json,math,subprocess,pathlib,os
import numpy as np,soundfile as sf,edge_tts
ROOT=pathlib.Path(__file__).resolve().parents[1]; OUT=ROOT/'audio';OUT.mkdir(parents=True,exist_ok=True);SR=48000
PHRASES=[
[0,"In 1999, a spacecraft disappeared behind Mars."],
[0,"Its signal was supposed to return. It never did."],
[0,"The reason was hidden in two tiny units."],
[1,"NASA's Mars Climate Orbiter had traveled for nine months."],
[1,"It was built to study Martian weather from orbit."],
[2,"But its navigation teams were using different measurements."],
[2,"A ground software file recorded thruster impulse in pound-force seconds."],
[3,"The flight-navigation system expected newton-seconds."],
[3,"One pound-force second equals about four point four five newton-seconds."],
[3,"The numbers weren't converted at the software handoff."],
[4,"When its small thrusters fired, the navigation model underestimated their effect."],
[4,"Those subtle errors accumulated over the journey."],
[5,"At Mars, the team expected to skim around one hundred and fifty kilometers high."],
[5,"Instead, the orbiter may have passed at only sixty."],
[6,"It went behind the planet, and the signal vanished."],
[6,"Controllers waited for the spacecraft to reappear."],
[6,"No signal ever returned."],
[7,"The investigation found more than a simple unit error."],
[7,"Reviews and communication should have caught the mismatch. They didn't."],
[8,"The tiny interface had failed. And an entire spacecraft was gone."]
]
def decode(p):
 b=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','pipe:1'],capture_output=True,check=True).stdout
 return np.frombuffer(b,'<f4').reshape(-1,2).copy()
async def voice():
 out=[];t=0.;segments=[]
 for i,(scene,text) in enumerate(PHRASES):
  audio=[];w=[]
  async for x in edge_tts.Communicate(text,voice='en-US-AndrewNeural',rate='-1%',pitch='-1Hz').stream():
   if x['type']=='audio':audio.append(x['data'])
   if x['type']=='WordBoundary':w.append(x)
  p=OUT/('raw%02d.mp3'%i);p.write_bytes(b''.join(audio));x=decode(p)
  hop=480;z=np.max(abs(x),axis=1)
  bins=np.array([np.sqrt(np.mean(z[k:k+hop]**2)) for k in range(0,len(z),hop)])
  bins=np.convolve(bins,np.ones(5)/5,'same')
  ids=np.flatnonzero(bins>max(.0013,bins.max()*.018))
  if len(ids)<5:raise RuntimeError('silent clip')
  x=x[max(0,ids[0]*hop-4500):min(len(x),(ids[-1]+1)*hop+5000)]
  if i:
   gap=.23 if i%4 else .34
   out.append(np.zeros((round(gap*SR),2),np.float32));t+=gap
  st=t;t+=len(x)/SR;fade=min(900,len(x)//5)
  x[:fade]*=np.linspace(0,1,fade)[:,None];x[-fade:]*=np.linspace(1,0,fade)[:,None]
  out.append(x)
  segments.append(dict(i=i,scene=scene,text=text,start=round(st,4),end=round(t,4),duration=round(len(x)/SR,4),wordBoundaryEvents=len(w)))
 return np.concatenate(out),segments
def write_srt(seg):
 def ts(t):
  ms=round(t*1000);h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
  return '%02d:%02d:%02d,%03d'%(h,m,s,ms)
 (OUT/'captions.srt').write_text('\n\n'.join(str(i+1)+'\n'+ts(x['start'])+' --> '+ts(x['end'])+'\n'+x['text'] for i,x in enumerate(seg))+'\n')
def music(length):
 import mido
 M=mido.MidiFile(ticks_per_beat=480);tempo=714286;beat=tempo/1e6
 tracks=[];events=[]
 for chan,prog in [(0,0),(1,48),(2,45),(3,32),(4,46)]:
  tr=mido.MidiTrack();tr.append(mido.MetaMessage('set_tempo',tempo=tempo,time=0))
  tr.append(mido.Message('program_change',channel=chan,program=prog,time=0));M.tracks.append(tr);tracks.append(tr);events.append([])
 def note(ch,p,v,t,d):
  events[ch].extend([(round(t/beat*480),1,p,v),(round((t+d)/beat*480),0,p,0)])
 chords=[[45,48,52,57],[41,45,48,53],[38,41,45,50],[40,44,47,52]]
 for bar in range(math.ceil(length/(4*beat))):
  base=bar*4*beat;ns=chords[bar%4];late=bar>length/(8*beat)
  for n in ns:note(1,n+12,45 if not late else 54,base,3.6*beat)
  note(3,ns[0]-12,48,base,1.8*beat);note(3,ns[0]-12,42,base+2*beat,1.7*beat)
  for k,idx in enumerate([0,2,1,3,2,1,0,2]):note(0,ns[idx]+12,(61 if k%2==0 else 44)+(8 if late else 0),base+k*.5*beat,.32*beat)
  for k in [0,2]:note(2,ns[0]+24,39,base+k*beat,.42*beat)
  if bar%4==3:
   for k,n in enumerate(ns):note(4,n+24,42,base+beat*(k+.1),.7*beat)
 for ch,ev in enumerate(events):
  last=0
  for at,on,p,v in sorted(ev,key=lambda a:(a[0],a[1])):
   tracks[ch].append(mido.Message('note_on' if on else 'note_off',channel=ch,note=p,velocity=v,time=max(0,at-last)))
   last=at
 mid=OUT/'original_score.mid';M.save(mid)
 sf2='/usr/share/sounds/sf2/FluidR3_GM.sf2'
 if not os.path.exists(sf2):raise RuntimeError('No sampled instrument SF2, refusing sine-only fallback')
 subprocess.run(['fluidsynth','-ni',sf2,str(mid),'-F',str(OUT/'music_render.wav'),'-r','48000','-g','.60'],check=True,stdout=subprocess.DEVNULL)
 y=decode(OUT/'music_render.wav')
 if len(y)<length*SR:y=np.pad(y,((0,math.ceil(length*SR)-len(y)),(0,0)))
 y=y[:math.ceil(length*SR)].copy()
 env=np.ones(len(y),np.float32)*.38
 n0=min(len(y),SR*2);env[:n0]*=np.linspace(.22,1,n0)
 n1=min(len(y),SR*3);env[-n1:]*=np.linspace(1,0,n1)
 return y*env[:,None]
def foley(n,seg):
 rng=np.random.default_rng(188);y=np.zeros((n,2),np.float32)
 for x in seg:
  scene=x['scene'];t=x['start']+.25
  if scene not in (0,2,3,4,6):continue
  d=.55 if scene!=4 else .95
  u=np.arange(int(d*SR),dtype=np.float32)/SR
  if scene==4: s=.23*rng.standard_normal(len(u))*np.exp(-u*3)+.22*np.sin(2*np.pi*(85*u+40*u*u))*np.exp(-u*2)
  elif scene==6: s=.25*(np.sin(2*np.pi*860*u)+.2*np.sin(2*np.pi*1280*u))*np.exp(-u*3)
  else:s=.20*np.sin(2*np.pi*(650*u+420*u*u))*np.exp(-u*7)
  s*=np.minimum(1,u*55);p=round(t*SR);nn=min(len(s),len(y)-p)
  if nn>0:y[p:p+nn,0]+=.65*s[:nn];y[p:p+nn,1]+=.79*s[:nn]
 return y
async def main():
 v,s=await voice();duration=len(v)/SR+1.1;n=math.ceil(duration*SR);m=music(duration);fx=foley(n,s)
 v=np.pad(v,((0,n-len(v)),(0,0)));z=.90*v+.42*m+.95*fx;mx=np.max(abs(z))
 if mx>.86:z*=.86/mx
 for name,x in [('voice_24bit.wav',v),('music_24bit.wav',m),('sfx_24bit.wav',fx),('mix_raw.wav',z)]:sf.write(OUT/name,x,SR,subtype='PCM_24')
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(OUT/'mix_raw.wav'),'-af','loudnorm=I=-13.6:TP=-1.4:LRA=7','-ar','48000','-ac','2',str(OUT/'master_24bit.wav')],check=True)
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(OUT/'master_24bit.wav'),'-c:a','libmp3lame','-b:a','256k',str(OUT/'final_mix.mp3')],check=True)
 scenes={str(j):dict(start=min(x['start'] for x in s if x['scene']==j),end=max(x['end'] for x in s if x['scene']==j)) for j in range(9)}
 (OUT/'timeline.json').write_text(json.dumps(dict(duration=round(duration,4),speechEnd=round(len(v)/SR-1.1,4),fps=30,phrases=s,scenes=scenes),indent=2))
 write_srt(s)
 gaps=[round(b['start']-a['end'],3) for a,b in zip(s,s[1:])]
 (OUT/'voice_gap_QA.json').write_text(json.dumps(dict(gaps=gaps,maxGap=max(gaps),captionBasis='actual trimmed recorded spoken phrase files, not estimated word events'),indent=2))
 assert max(gaps)<.55
 print('AUDIO SUCCESS seconds=',round(duration,3),'max gap',max(gaps),'word bounds',sum(x['wordBoundaryEvents'] for x in s))
asyncio.run(main())
