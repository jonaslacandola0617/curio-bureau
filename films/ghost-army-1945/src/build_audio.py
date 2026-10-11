#!/usr/bin/env python3
"""EP009 ORIGINAL Ghost Army documentary narration, cue-directed score and owned SFX."""
import asyncio,json,math,subprocess,pathlib,os,csv,hashlib
import numpy as np, soundfile as sf,edge_tts
ROOT=pathlib.Path(__file__).resolve().parents[1]; OUT=ROOT/'audio';OUT.mkdir(parents=True,exist_ok=True)
REPO=ROOT.parents[1];LIB=REPO/'audio'/'curio_sfx_v1';SR=48000
# Dialogue delivered in scene order, driven by actual produced voice recording.
PHRASES=[
 [0,"This tank was supposed to fool an entire army."],
 [0,"And it was made of air."],
 [1,"In World War Two, America assembled a secret force of about eleven hundred specialists."],
 [1,"Their job was not to fight like an ordinary division."],
 [1,"It was to look like one."],
 [2,"Artists raised rubber tanks and artillery where real armor should have been."],
 [2,"From a distance, the illusion was remarkably convincing."],
 [3,"But a fake tank couldn't sound like an army."],
 [3,"So engineers used enormous speakers to play recordings of troops and vehicles."],
 [4,"And radio operators sent false messages, imitating units that simply weren't there."],
 [5,"Fake vehicle tracks, dummy guns, sound, and radio."],
 [5,"Every clue told the enemy the same story."],
 [6,"In March nineteen forty-five, during Operation Viersen, the deception helped conceal a real Allied crossing of the Rhine."],
 [6,"This little unit could imitate two divisions."],
 [7,"Roughly thirty thousand troops, suggested by just eleven hundred specialists."],
 [7,"An illusion that helped misdirect German attention."],
 [8,"The remarkable part wasn't the rubber tanks."],
 [8,"It was how so many convincing details made an army out of nothing."]
]
DIRECTION={
0:('surprised disbelief','upward curious arc','tank / air',+5,+1),
1:('confidential contextual','even but alert','secret / look',-1,-2),
2:('technical wonder','bright pace','rubber / convincing',+4,+2),
3:('suspense and discovery','short dramatic breath','sound / speakers',-3,-3),
4:('quiet intent','confident investigative','false / never',+1,0),
5:('system reveal','energized cadence','every clue / same',+3,+1),
6:('historical stakes','measured urgency','March / crossing',-2,-1),
7:('human-scale astonishment','deliberate emphasis','thirty thousand / eleven hundred',-5,-1),
8:('reflective earned payoff','slower warm landing','nothing',-6,-2)}
SFX=[
 (0,.05,'cinematic','CB_CINEMATIC_micro_emphasis_v1.flac',.35,'opening visual contradiction'),
 (0,1.7,'motion','CB_MOTION_document_focus_v1.flac',.29,'tank surface macro reveal'),
 (1,.12,'ambient','CB_AMBIENT_workshop_floor_v1.flac',.20,'quiet illustrated field/workshop bed'),
 (2,.22,'mechanical','CB_MECHANICAL_screw_jack_turn_v1.flac',.43,'inflatable valve and construction motion'),
 (2,1.60,'mechanical','CB_MECHANICAL_wood_stress_v1.flac',.25,'fabric/structural deformation illustrative'),
 (3,.22,'cinematic','CB_CINEMATIC_suspense_riser_v1.flac',.38,'audio contrast before speaker explanation'),
 (3,2.10,'ambient','CB_AMBIENT_workshop_floor_v1.flac',.34,'imagined moving vehicle sonic illusion'),
 (4,.11,'science','CB_SCIENCE_radio_search_v1.flac',.32,'fictional Morse-like radio texture not authentic recording'),
 (4,1.9,'science','CB_SCIENCE_data_pulse_v1.flac',.31,'false encoded-traffic concept'),
 (5,.24,'motion','CB_MOTION_parallax_swish_v1.flac',.29,'observational camera cut'),
 (5,2.03,'editorial','CB_EDITORIAL_evidence_lock_v1.flac',.43,'three evidence types converge'),
 (6,.16,'cinematic','CB_CINEMATIC_investigative_sting_v1.flac',.27,'historical geographic turn'),
 (6,3.02,'motion','CB_MOTION_map_route_draw_v1.flac',.32,'conceptual Rhine route reveal'),
 (7,.15,'editorial','CB_EDITORIAL_hard_fact_punctuate_v1.flac',.36,'force size comparison'),
 (7,1.8,'cinematic','CB_CINEMATIC_restrained_boom_v1.flac',.27,'consequence underscored once'),
 (8,.21,'cinematic','CB_CINEMATIC_warm_resolution_v1.flac',.32,'reflective ending')
]
def decode(p):
 p=subprocess.run(['ffmpeg','-v','error','-i',str(p),'-ar','48000','-ac','2','-f','f32le','pipe:1'],capture_output=True,check=True)
 return np.frombuffer(p.stdout,'<f4').reshape(-1,2).copy()
async def render_voice(text,voice,rate,pitch,path,word_data=None):
 audio=[];w=[]
 async for x in edge_tts.Communicate(text,voice=voice,rate=rate,pitch=pitch).stream():
  if x['type']=='audio':audio.append(x['data'])
  elif x['type']=='WordBoundary':w.append(dict(text=x.get('text'),offset=x.get('offset'),duration=x.get('duration')))
 if not audio:raise RuntimeError("TTS returned no data")
 path.write_bytes(b''.join(audio))
 if word_data is not None:word_data.extend(w)
 return decode(path)
async def auditions():
 arr=[("A","en-US-GuyNeural","+7%","+3Hz"),
      ("B","en-US-AndrewNeural","-2%","-2Hz")]
 for ident,voice,rate,pitch in arr:
  for spot,text in [("OPEN","This tank was supposed to fool an entire army. And it was made of air."),
                    ("TURN","But a fake tank couldn't sound like an army. So engineers used enormous speakers.")]:
   await render_voice(text,voice,rate,pitch,OUT/f'VOICE_AUDITION_{spot}_{ident}.mp3')
 (OUT/'VOICE_AB_QA.md').write_text(
  '# EP009 real audition files (CREATIVE SIGNOFF PENDING)\\n'
  'Four genuine independently synthesized A/B speech clips exist. Alternative A: GuyNeural +7%, pitch +3Hz. B: AndrewNeural -2%, pitch -2Hz. '
  'Chosen A was used for production based on purposeful faster opening and dynamic line-level pace; cannot claim human emotional listening occurred in this automation. '
  'A trained human/owner must listen to both opening and twist comparisons in real playback and select/replace before FINAL.\\n')
async def voice():
 parts=[];seg=[];t=0
 for i,(scene,text) in enumerate(PHRASES):
  rate,pitch=DIRECTION[scene][-2:]
  words=[]
  x=await render_voice(text,'en-US-GuyNeural',f'{rate:+d}%',f'{pitch:+d}Hz',OUT/f'raw{i:02d}.mp3',words)
  hop=480
  bins=np.array([np.sqrt(np.mean(x[j:j+hop]**2)) for j in range(0,len(x),hop)])
  bins=np.convolve(bins,np.ones(5)/5,'same')
  ok=np.flatnonzero(bins>max(.0012,bins.max()*.020))
  if len(ok)<5:raise RuntimeError('Silent narration phrase '+str(i))
  off=max(0,ok[0]*hop-4300);end=min(len(x),(ok[-1]+1)*hop+4900)
  x=x[off:end]
  if i:
   gap=.20 if i%3 else .28
   parts.append(np.zeros((round(gap*SR),2),np.float32));t+=gap
  start=t;t+=len(x)/SR
  fade=min(900,len(x)//5)
  x[:fade]*=np.linspace(0,1,fade)[:,None];x[-fade:]*=np.linspace(1,0,fade)[:,None]
  parts.append(x)
  seg.append(dict(i=i,scene=scene,text=text,start=round(start,4),end=round(t,4),
    duration=round(len(x)/SR,4),wordBoundaryEvents=len(words),emotional_intent=DIRECTION[scene][0]))
 return np.concatenate(parts),seg
def music(length,seg):
 import mido
 M=mido.MidiFile(ticks_per_beat=480);tempo=625000;beat=tempo/1e6
 tracks=[];events=[]
 # piano, strings, cello, bass, harp, flute
 for chan,prog in [(0,0),(1,48),(2,42),(3,32),(4,46),(5,73)]:
  tr=mido.MidiTrack();tr.append(mido.MetaMessage('set_tempo',tempo=tempo,time=0));tr.append(mido.Message('program_change',channel=chan,program=prog,time=0));M.tracks.append(tr);tracks.append(tr);events.append([])
 def note(ch,p,v,t,d):
  events[ch].extend([(round(t/beat*480),1,p,v),(round((t+d)/beat*480),0,p,0)])
 chords=[[45,52,57,60],[41,48,53,57],[38,45,50,53],[40,47,52,55],
         [45,52,57,60],[41,48,53,57],[43,50,55,58],[45,52,57,60]]
 for bar in range(math.ceil(length/(4*beat))):
  base=bar*4*beat;ns=chords[(bar//2)%len(chords)];progress=base/max(1,length)
  tension=.7 if progress<.22 else (1 if progress<.67 else (.85 if progress<.88 else .5))
  for n in ns:note(1,n+12,round(42*tension),base,3.7*beat)
  for n in [ns[0],ns[2]]:note(2,n+12,round(31*tension),base+.12*beat,3.2*beat)
  note(3,ns[0]-12,round(47*tension),base,1.8*beat);note(3,ns[0]-12,round(37*tension),base+2*beat,1.7*beat)
  for k,idx in enumerate([0,2,1,3,2,1,0,2]):
   note(0,ns[idx]+12,round((58 if k%2==0 else 40)*tension),base+k*.5*beat,.33*beat)
  if bar%3==1:
   for k,n in enumerate(ns):note(4,n+24,round(28*tension),base+beat*(k+.1),.6*beat)
  if progress>.68 and bar%2==0:
   for k,n in enumerate(ns[1:]):note(5,n+24,round(29*tension),base+beat*(k+.2),.85*beat)
 for ch,ev in enumerate(events):
  last=0
  for at,on,p,v in sorted(ev,key=lambda q:(q[0],q[1])):
   tracks[ch].append(mido.Message('note_on' if on else 'note_off',channel=ch,note=p,velocity=v,time=max(0,at-last)));last=at
 fn=OUT/'original_score.mid';M.save(fn);sf2='/usr/share/sounds/sf2/FluidR3_GM.sf2'
 if not os.path.exists(sf2):raise RuntimeError('Instrument soundfont unavailable; no tone-only substitute')
 subprocess.run(['fluidsynth','-ni',sf2,str(fn),'-F',str(OUT/'music_render.wav'),'-r','48000','-g','.68'],stdout=subprocess.DEVNULL,check=True)
 y=decode(OUT/'music_render.wav')
 n=math.ceil(length*SR)
 if len(y)<n:y=np.pad(y,((0,n-len(y)),(0,0)))
 y=y[:n].copy()
 env=np.ones(n,np.float32)*.43
 # Sound is mixed deliberately, not an inaudible bed.
 for j in range(n):
  tt=j/SR
  env[j]*=(.50 if tt<6 else .88 if tt<length*.25 else 1.10 if tt<length*.75 else .74)
 n0=min(n,SR*1);env[:n0]*=np.linspace(.55,1,n0)
 n1=min(n,SR*2);env[-n1:]*=np.linspace(1,0,n1)
 return y*env[:,None]
def collect_sfx(n,seg):
 y=np.zeros((n,2),np.float32);list_entries=[]
 for scene,shift,category,fn,gain,purpose in SFX:
  hits=[p for p in seg if p['scene']==scene]
  if not hits:continue
  t=hits[0]['start']+shift;at=round(t*SR)
  path=LIB/category/fn
  if not path.exists():raise RuntimeError('Source first-party cue absent: '+str(path))
  fx,fr=sf.read(path,always_2d=True,dtype='float32')
  if fr!=SR:raise RuntimeError('Sample-rate mismatch '+str(path))
  take=min(len(fx),n-at)
  if take>0:y[at:at+take]+=fx[:take]*gain
  list_entries.append(dict(scene=scene,start_s=round(t,3),word_sync='PHRASE-APPROXIMATION (word alignment unverified)',
   source_file=str(path.relative_to(REPO)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
   category=category,source_truth='first-party DESIGNED synthesis, NOT historic recorded audio',
   gain=gain,visual_event=purpose,license_status='original first-party',mix_bus='DESIGNED_SFX'))
 with (OUT/'audio_cue_sheet.csv').open('w',newline='') as f:
  wr=csv.DictWriter(f,fieldnames=list(list_entries[0]));wr.writeheader();wr.writerows(list_entries)
 return y
def srt(seg):
 def ts(t):
  m=round(t*1000);h,m=divmod(m,3600000);mi,m=divmod(m,60000);ss,m=divmod(m,1000)
  return f'{h:02d}:{mi:02d}:{ss:02d},{m:03d}'
 (OUT/'captions.srt').write_text('\n\n'.join(f'{i+1}\n{ts(x["start"])} --> {ts(x["end"])}\n{x["text"]}' for i,x in enumerate(seg))+'\n')
async def main():
 await auditions()
 v,seg=await voice();speech_duration=len(v)/SR;duration=speech_duration+1.15
 n=math.ceil(duration*SR)
 m=music(duration,seg)
 fx=collect_sfx(n,seg)
 v=np.pad(v,((0,n-len(v)),(0,0)))
 # R2: +3.0 dB vocal/SFX relative to music, true-peak limited finished master.
 # Keep music present; raising every bus equally before loudnorm would be cancelled by normalization.
 voice_gain=10**(3.0/20)
 sfx_gain=10**(3.0/20)
 z=(.94*voice_gain)*v + .61*m + (.85*sfx_gain)*fx
 peak=float(np.max(abs(z)))
 if peak>.87:z*=.87/peak
 (OUT/'AUDIO_MIX_REVISION_R2.json').write_text(json.dumps({
   'mix_request':'raise perceived narration and SFX 2-4 dB', 
   'chosen_relative_voice_gain_db':3.0,
   'chosen_relative_sfx_gain_db':3.0,
   'music_source_gain_unchanged':True,
   'master_target_lufs':-12.0,
   'master_true_peak_ceiling_dbTP':-1.0,
   'source_basis':'gain changes applied to separately-rendered voice and SFX buses before final loudnorm',
   'qa_limit':'Final actual perceived gain requires encoded-file measurements and human audition; not guaranteed to be exactly +3dB absolute versus R1'
  },indent=2))
 for name,x in [('voice_24bit.wav',v),('music_24bit.wav',m),('sfx_24bit.wav',fx),('mix_raw.wav',z)]:
  sf.write(OUT/name,x,SR,subtype='PCM_24')
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(OUT/'mix_raw.wav'),'-af','loudnorm=I=-12.0:TP=-1.0:LRA=7','-ar','48000','-ac','2',str(OUT/'master_24bit.wav')],check=True)
 subprocess.run(['ffmpeg','-y','-v','error','-i',str(OUT/'master_24bit.wav'),'-c:a','libmp3lame','-b:a','256k',str(OUT/'final_mix.mp3')],check=True)
 scenes={str(i):dict(start=min(x['start'] for x in seg if x['scene']==i),end=max(x['end'] for x in seg if x['scene']==i)) for i in range(9)}
 (OUT/'timeline.json').write_text(json.dumps(dict(duration=round(duration,4),speechEnd=round(speech_duration,4),fps=30,phrases=seg,scenes=scenes),indent=2))
 srt(seg)
 gaps=[round(b['start']-a['end'],3) for a,b in zip(seg,seg[1:])]
 (OUT/'voice_gap_QA.json').write_text(json.dumps(dict(gaps=gaps,maxGap=max(gaps),wordAlignment='UNVERIFIED, source phrase clip boundaries only',humanAudition='PENDING',sceneTiming='actual produced voice clip duration'),indent=2))
 assert max(gaps)<.55
 (OUT/'AUDIO_HUMAN_CREATIVE_GATE.md').write_text(
  '# EP009 audio review gating\nA/B voice audition files were genuinely generated; chosen voice GuyNeural was directed with scene-level rate/pitch cues and a rewritten script. '
  'However, a TTS voice profile plus automatic signal QA does not prove engaging human emotional delivery. Full subjective A/B auditions on phone/headphones and word-level alignment remain OPEN. '
  'This audio is a REVIEW CANDIDATE only. All SFX are from original synthesized Curio pack; not genuine 1945 recordings.\n')
 print('EP009 AUDIO SUCCESS: duration=',round(duration,2),'maxGap=',max(gaps),'AB=4 clips','SFX=',len(SFX),'wordBoundaries=',sum(x['wordBoundaryEvents'] for x in seg),flush=True)
asyncio.run(main())
