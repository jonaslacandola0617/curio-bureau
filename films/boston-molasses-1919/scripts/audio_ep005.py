#!/usr/bin/env python3
"""Curio Bureau 005: neural word-timed narration, harmonically composed original score,
and layered bespoke sound effects. Writes separate QA stems and 48 kHz 24-bit mix."""
import asyncio, os, json, pathlib, subprocess, math
import numpy as np
import soundfile as sf
import edge_tts
from scipy.signal import butter, sosfilt

RATE=48000; DUR=76; N=RATE*DUR
BASE=pathlib.Path("out")
BASE.mkdir(exist_ok=True,parents=True)
V=BASE/"voice"
V.mkdir(exist_ok=True)
SCENES=[
 (0,8, "This wave that tore through Boston wasn't water. It was molasses."),
 (8,18,"In nineteen nineteen, a giant tank beside Commercial Street held more than two million gallons of it."),
 (18,28,"Residents had noticed leaks. But the massive steel walls kept standing, until January fifteenth."),
 (28,36,"Then the tank ruptured. Metal tore apart, and the flood burst into the neighborhood."),
 (36,48,"People were trapped beneath wreckage and thick molasses. Twenty-one people died. About a hundred and fifty were injured."),
 (48,62,"Rescuers struggled through debris and sticky streets. Cleanup crews finally used salt water from Boston Harbor to wash away the mess."),
 (62,76,"The owners first claimed sabotage. But a later investigation found negligence. The true tragedy? The warning signs had been there all along.")
]
def peak(x):return float(np.max(np.abs(x)))
def rms(x):return float(np.sqrt(np.mean(x*x)+1e-16))
def stereo(x):return np.column_stack([x,x]).astype(np.float32)
def write(path,arr): sf.write(str(path),np.clip(arr,-.995,.995),RATE,subtype="PCM_24")
def place(dest,src,start):
    j=int(start*RATE);m=min(len(src),len(dest)-j)
    if m>0:dest[j:j+m]+=src[:m]
async def narration():
    v=np.zeros((N,2),np.float32)
    words=[];timings=[]
    for i,(start,end,text) in enumerate(SCENES):
        outfile=V/("scene_%02d.mp3"%i)
        communic=edge_tts.Communicate(text=text,voice="en-US-AndrewNeural",rate="-3%",pitch="-2Hz")
        b=[];word=[]
        async for chunk in communic.stream():
            if chunk["type"]=="audio":b.append(chunk["data"])
            elif chunk["type"]=="WordBoundary":
                word.append({"text":chunk["text"],"start":start+chunk["offset"]/1e7,
                            "end":start+(chunk["offset"]+chunk["duration"])/1e7})
        outfile.write_bytes(b"".join(b))
        z=subprocess.run(["ffmpeg","-v","error","-i",str(outfile),
                 "-f","f32le","-acodec","pcm_f32le","-ac","2","-ar",str(RATE),"-"],
                 capture_output=True,check=True).stdout
        audio=np.frombuffer(z,np.float32).reshape((-1,2)).copy()
        length=len(audio)/RATE
        if length>(end-start-.22):
            raise RuntimeError("Narration scene %d has duration %.3f s but budget %.3f s"%(
                i,length,end-start))
        fade=min(int(.02*RATE),len(audio)//8)
        audio[:fade]*=np.linspace(0,1,fade)[:,None]
        audio[-fade:]*=np.linspace(1,0,fade)[:,None]
        place(v,audio,start)
        # HARD EDITORIAL QA: prevent 3–5 second narration dead zones.
        # A measured narration should usually flow to the next beat, allowing
        # only an intentional short breath. Re-time the picture and score,
        # or rewrite/record the narration; do NOT speed-stretch the voice.
        gap=(end-start)-length
        if gap>1.20:
            raise RuntimeError(
                f"EDITORIAL PACING QA FAILED: scene {i+1} has {gap:.2f}s "
                f"without narration. Rebuild scene durations, picture, "
                f"caption map and music cues; do not deliver this timing.")
        timings.append({"start":start,"end":end,"actual_length":round(length,3),
                       "voice_gap":round(gap,3),
                       "text":text,"word_count":len(word)})
        words.extend(word)
    level=rms(v)
    v*=.105/max(level,1e-6)
    v=np.clip(v,-.86,.86)
    write(BASE/"voice.wav",v)
    cues=[]
    # Native neural word boundary metadata; dynamic word groups are NOT
    # automatically stamped at scene changes.
    current=[]
    for w in words:
        if current and (len(current)>=4 or w["end"]-current[0]["start"]>1.85 or
                        w["start"]-current[-1]["end"]>.6):
            cues.append({"start":round(current[0]["start"],3),
                         "end":round(current[-1]["end"]+.07,3),
                         "text":" ".join(e["text"] for e in current)})
            current=[]
        current.append(w)
    if current:cues.append({"start":round(current[0]["start"],3),
              "end":round(min(76,current[-1]["end"]+.08),3),
              "text":" ".join(e["text"] for e in current)})
    if not words:
        # Some Edge TTS responses contain audio with NO WordBoundary events.
        # Without this guard the old pipeline silently delivered zero captions.
        # Estimate time cues from the measured recorded durations, and mark
        # their provenance. This is a working fallback, NOT verified forced
        # alignment, and must not be advertised as exact word boundaries.
        import re
        timings_by_scene=timings
        for seg in timings_by_scene:
            start=seg["start"]; words_here=seg["text"].split()
            duration=seg["actual_length"]
            def weight(tok):
                w=re.sub(r"[^A-Za-z]","",tok).lower()
                syl=len(re.findall(r"[aeiouy]+",w)) or 1
                return .45+.5*syl+.045*min(len(w),9)+(.30 if re.search(r"[,.?!:]$",tok) else 0)
            weights=[weight(w) for w in words_here]
            total=sum(weights)
            accum=0.; j=0
            while j<len(words_here):
                k=j
                while k+1<len(words_here):
                    phrase=" ".join(words_here[j:k+2])
                    nextdur=(sum(weights[j:k+2])/total)*duration
                    if k-j+1>=4 or len(phrase)>34 or nextdur>1.65:break
                    k+=1
                    if re.search(r"[.!?]$",words_here[k]):break
                st=start+duration*(sum(weights[:j])/total)
                en=start+duration*(sum(weights[:k+1])/total)
                cues.append({"start":round(max(0,st-.01),3),
                             "end":round(min(76,en+.03),3),
                             "text":" ".join(words_here[j:k+1]),
                             "source":"ESTIMATED_FROM_RECORDED_SCENE_DURATION"})
                j=k+1
        (BASE/"caption_alignment_method.txt").write_text(
          "WordBoundary metadata was unavailable from the TTS service.\\n"
          "Captions are syllable-weighted estimates from measured recording "
          "durations and REQUIRE manual listening/forced alignment before FINAL.\\n")
    if not cues: raise RuntimeError("No caption timing data generated. FAIL release.")
    (BASE/"captions.json").write_text(json.dumps(cues,indent=2))
    (BASE/"word_boundaries.json").write_text(json.dumps(words,indent=2))
    (BASE/"voice_timing.json").write_text(json.dumps(timings,indent=2))
    def tc(s):
        ms=round(s*1000);h=ms//3600000;ms%=3600000;m=ms//60000;ms%=60000
        return f"{h:02d}:{m:02d}:{ms//1000:02d},{ms%1000:03d}"
    with open(BASE/"captions.srt","w") as f:
      for j,c in enumerate(cues):f.write(f"{j+1}\n{tc(c['start'])} --> {tc(c['end'])}\n{c['text']}\n\n")
    return v,timings,cues

def adsr(num,attack=.03,decay=.12,sustain=.3,release=.2):
    e=np.ones(num,np.float32)*sustain
    n=max(1,min(num,int(attack*RATE)))
    e[:n]=np.linspace(0,1,n)
    m=max(n,min(num,n+int(decay*RATE)))
    e[n:m]=np.linspace(1,sustain,m-n)
    r=max(m,min(num,int(release*RATE)))
    e[-r:]*=np.linspace(1,0,r)
    return e
def synth_note(freq,secs,kind="felt"):
    n=int(secs*RATE);t=np.arange(n,dtype=np.float32)/RATE
    if kind=="felt":
        z=(.85*np.sin(2*math.pi*freq*t)+.22*np.sin(2*math.pi*freq*2*t)
          +.11*np.sin(2*math.pi*freq*3*t)+.05*np.sin(2*math.pi*freq*4*t))
        env=np.exp(-2.4*t)*np.minimum(1,t*36)
    elif kind=="string":
        z=(.55*np.sin(2*math.pi*freq*t+.025*np.sin(t*5))+
           .2*np.sin(2*math.pi*freq*2.01*t)+.09*np.sin(2*math.pi*freq*3*t))
        env=np.minimum(1,t*5)*np.minimum(1,(secs-t)*2.6)
    else:
        z=np.sin(2*math.pi*freq*t)+.11*np.sin(2*math.pi*freq*2*t)
        env=np.exp(-1.5*t)
    return (z*env).astype(np.float32)
def pitch(midi):return 440*2**((midi-69)/12)

def score():
    m=np.zeros((N,2),np.float32)
    tempo=84;beat=60/tempo
    chords=[[50,53,57,62],[46,50,53,58],[53,57,60,65],[48,52,55,60],
            [50,53,57,62],[46,50,53,58],[55,58,62,67],[45,49,52,57]]
    for measure in range(27):
        start=measure*4*beat
        chord=chords[measure%len(chords)]
        factor=.55 if start>47 and start<62 else (1.15 if 27<start<44 else .85)
        for j,note in enumerate(chord[1:]):
            delay=start+.24*j
            a=synth_note(pitch(note+12),3.65,"string")*.075*factor
            place(m,stereo(a*np.array([.92,.84],np.float32)[0]),delay) # stereo variation below
        for k in range(8):
            if start+k*beat/2>DUR:break
            midi=chord[(k+[0,1,2,3,2,1,3,1][k])%4]+12
            note=synth_note(pitch(midi),1.2,"felt")*.112*factor
            j=int((start+k*beat/2)*RATE);ln=min(len(note),N-j)
            if ln>0:
                pan=.25+.5*((k%4)/3);m[j:j+ln,0]+=note[:ln]*(1-pan)
                m[j:j+ln,1]+=note[:ln]*pan
        bass=synth_note(pitch(chord[0]-12),2.8,"bass")*.23*factor
        place(m,stereo(bass),start)
    # actual rhythmic shaker/noise percussion, not a sine-only "music" claim
    rng=np.random.default_rng(33019)
    for b in np.arange(0,75,beat):
        dur=.09;n=int(dur*RATE)
        tt=np.arange(n)/RATE
        noise=rng.standard_normal(n).astype(np.float32)
        h=sosfilt(butter(3,2500,btype="highpass",fs=RATE,output="sos"),noise)
        sh=(h*np.exp(-40*tt)*.01).astype(np.float32)
        place(m,stereo(sh),b)
    # wide, slight room echo
    for lag,g in [(4100,.13),(8200,.07),(12900,.042)]:
        m[lag:,1]+=m[:-lag,0]*g
        m[lag:,0]+=m[:-lag,1]*g
    m*=.043/max(rms(m),1e-6)
    write(BASE/"music.wav",m)
    return m

def build_sfx():
    fx=np.zeros((N,2),np.float32)
    rng=np.random.default_rng(1919)
    def noise(secs,lo,hi):
        n=int(secs*RATE)
        a=rng.standard_normal(n).astype(np.float32)
        if lo:a=sosfilt(butter(3,lo,btype="highpass",fs=RATE,output="sos"),a).astype(np.float32)
        if hi:a=sosfilt(butter(3,hi,btype="lowpass",fs=RATE,output="sos"),a).astype(np.float32)
        return a/(np.max(np.abs(a))+.0001)
    def add(start,arr,g=.2,pan=.5):
        arr=arr*g
        j=int(start*RATE);l=min(len(arr),N-j)
        if l>0:
            fx[j:j+l,0]+=arr[:l]*(1-pan)*1.5
            fx[j:j+l,1]+=arr[:l]*pan*1.5
    # initial mechanical impact with multi-resonance steel, broadband crack and wake
    t=np.arange(int(2.7*RATE))/RATE
    metal=np.sin(2*math.pi*(58*t+9*t*t))*.2+np.sin(2*math.pi*133*t)*.12
    crack=noise(2.7,120,11000)*np.exp(-8*t)
    add(0,metal*np.exp(-1.2*t)+crack,.45,.47)
    # rolling viscous surge with shaped low/mid-noise, wave crests and stereo response
    for start,dur,g in [(0.5,6,.16),(30.0,12,.28),(39.0,6,.23)]:
        a=noise(dur,75,2100);tt=np.arange(len(a))/RATE
        env=np.minimum(1,tt/1.1)*np.minimum(1,(dur-tt)/1.8)
        env*=.55+.45*np.sin(2*math.pi*(.58*tt))**2
        add(start,a*env,g,.32 if int(start)%2 else .67)
    # tank leaks (individual liquid drops), stressed panel scrape, rupture
    for start in [18.8,19.4,20.6,21.4,22.1,23.2,24.4]:
        tt=np.arange(int(.15*RATE))/RATE
        drop=np.sin(2*math.pi*(370-650*tt)*tt)*np.exp(-36*tt)
        add(start,drop,.26,.73)
    for start in [23.7,25.6,27.1]:
        a=noise(1.2,220,4900)
        tt=np.arange(len(a))/RATE
        scr=a*np.exp(-2.5*tt)*(.5+.5*np.sin(2*math.pi*28*tt)**2)
        add(start,scr,.20,.32)
    # tank separation with flanging steel, hard shell groan
    d=5;t=np.arange(int(d*RATE))/RATE
    metallic=(np.sin(2*math.pi*(85*t+18*t*t))+
              .32*np.sin(2*math.pi*(269*t-2.3*t*t)))*np.exp(-.8*t)
    massive=noise(d,50,3200)*np.exp(-1.5*t)
    add(29.2,metallic*.5+massive*.9,.42,.5)
    # heavy collision details
    for start in [37.0,38.4,41.4,43.2,44.7]:
        n=int(1.1*RATE);tt=np.arange(n)/RATE
        debris=noise(1.1,180,8300)*np.exp(-6.2*tt)
        debris+=np.sin(2*math.pi*81*tt)*np.exp(-3*tt)*.2
        add(start,debris,.22,.15+(start%3)/4)
    # cleanup spray (hissy running water, sound moves across field)
    n=int(8*RATE);tt=np.arange(n)/RATE
    hiss=noise(8,900,9800)
    hiss*=np.minimum(1,tt/2)*np.minimum(1,(8-tt)/1)
    add(53,hiss,.12,.66)
    # cut to investigation with muted paper + low tick
    for start in [62.1,65.1,69.3]:
        a=noise(.55,450,7400)*np.exp(-9*np.arange(int(.55*RATE))/RATE)
        add(start,a,.09,.57)
    fx=np.clip(fx,-.85,.85)
    write(BASE/"sfx.wav",fx)
    return fx

def make_mix(voice,music,fx):
    mono=np.max(np.abs(voice),axis=1)
    # moving RMS detector with 120ms window
    envelope=np.convolve(mono,np.ones(512,np.float32)/512,"same")
    env=np.minimum(1,envelope/.065)
    duck=(.92-.35*env).astype(np.float32)
    mix=voice+music*duck[:,None]+fx
    # soft 1.5dB peak reserve before FFmpeg true-peak mastering
    mix=np.tanh(mix*1.12)/1.12
    mix*=.83/max(peak(mix),.001)
    write(BASE/"premaster_24bit.wav",mix)
    print("STEMS",json.dumps({"voice_rms":rms(voice),"music_rms":rms(music),
       "effects_rms":rms(fx),"premaster_rms":rms(mix),"premaster_peak":peak(mix)}))
    # master loudness with FFmpeg; also make preview track for studio
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",
       str(BASE/"premaster_24bit.wav"),"-af","loudnorm=I=-13.5:TP=-1.5:LRA=9",
       "-ar","48000","-ac","2","-c:a","pcm_s24le",
       str(BASE/"master_mix.wav")],check=True)
    subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y","-i",
        str(BASE/"master_mix.wav"),"-c:a","libmp3lame","-b:a","256k",
        str(BASE/"master_mix.mp3")],check=True)

async def main():
    voice,timing,cues=await narration()
    music=score();fx=build_sfx()
    make_mix(voice,music,fx)
    print("TIMINGS:",json.dumps(timing))
    print("CAPTIONS",len(cues))
if __name__=="__main__":asyncio.run(main())
