#!/usr/bin/env python3
"""Curio Bureau 003 - word-accurate captions and truly natural-pace narration."""
import asyncio,json,pathlib,subprocess
import edge_tts
OUT=pathlib.Path('dist/niagara-1969');OUT.mkdir(parents=True,exist_ok=True)
VOICE='en-US-AndrewNeural'
STARTS=[0,7,15,23,32,42,51,58,64]
LINES=[
"In nineteen sixty nine, engineers did something extraordinary. They nearly stopped the American Falls at Niagara.",
"They weren't stopping all of Niagara. Only the American Falls. Nearby Horseshoe Falls kept roaring.",
"They built a temporary rock dam upstream, directing water around the island toward Horseshoe Falls.",
"With the water gone, the cliff stood exposed. Cracks, unstable rock, and a mountain of fallen stone.",
"Engineers drilled into the rock, mapped fractures, and measured water pressure. They needed to understand erosion.",
"More than five months later, they removed the dam. On November twenty fifth, the American Falls began flowing again.",
"In nineteen seventy five, the commission advised leaving the natural rock and erosion processes alone.",
"Sometimes saving a natural wonder means letting nature change it."
]
def run(args):
 p=subprocess.run(args,check=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode:raise RuntimeError('Command failed: '+str(args)+'\n'+p.stderr.decode(errors='replace'))
 return p.stdout.decode(errors='replace').strip()
def srt(s):
 n=round(max(0,s)*1000)
 return f'{n//3600000:02d}:{n//60000%60:02d}:{n//1000%60:02d},{n%1000:03d}'
async def main():
 all_words=[]
 rates=[]
 for i,(line,start,end) in enumerate(zip(LINES,STARTS,STARTS[1:])):
  name=OUT/f'voice-{i:02d}.mp3';bounds=[]
  with name.open('wb') as audio:
   async for c in edge_tts.Communicate(line,VOICE,rate='-2%',pitch='-2Hz',boundary='WordBoundary').stream():
    if c['type']=='audio':audio.write(c['data'])
    elif c['type']=='WordBoundary':bounds.append(dict(start=c['offset']/10_000_000,end=(c['offset']+c['duration'])/10_000_000))
  scripted=line.split()
  if len(bounds)!=len(scripted):raise RuntimeError(f'Word-boundary mismatch scene {i+1}: {len(bounds)} vs {len(scripted)}')
  duration=float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(name)]))
  window=end-start-.28
  ratio=duration/window
  print(f'NIAGARA SCENE {i+1}: voice={duration:.3f}s window={window:.3f}s, needed_tempo={ratio:.4f}',flush=True)
  if ratio>1.045:raise RuntimeError(f'NIAGARA VOICE TOO FAST in scene {i+1}: requires {ratio:.3f}x. Shorten narration; never force atempo.')
  # Deliberately preserve natural speaking rate even if speech finishes early.
  if duration>window:raise RuntimeError(f'NIAGARA scene {i+1} barely misses target; rewrite, do not stretch.')
  rates.append(1.0)
  filtered=f'afade=t=in:st=0:d=0.08,afade=t=out:st={max(0.15,duration-.17):.3f}:d=0.16,apad,atrim=0:{end-start}'
  run(['ffmpeg','-y','-v','error','-i',str(name),'-af',filtered,'-ac','2','-ar','48000',str(OUT/f'part-{i:02d}.wav')])
  for word,b in zip(scripted,bounds):
   all_words.append(dict(text=word,scene=i,last_sentence=word.endswith(('.', '!', '?')),start=round(start+b['start'],3),end=round(min(end-.045,start+b['end']),3)))
 groups=[];current=[]
 def flush():
  if not current:return
  text=' '.join(w['text'] for w in current)
  groups.append(dict(start=round(current[0]['start'],3),end=round(max(current[-1]['end'],current[0]['start']+.46),3),text=text))
  current.clear()
 for w in all_words:
  if current and (current[-1]['scene']!=w['scene'] or current[-1]['last_sentence'] or len(current)>=5 or len(' '.join(z['text'] for z in current+[w]))>38 or w['end']-current[0]['start']>1.7 or w['start']-current[-1]['end']>.55):flush()
  current.append(w)
  if w['last_sentence']:flush()
 flush()
 if len(groups)<32:raise RuntimeError(f'Only {len(groups)} subtitle phrases, need >=32')
 with (OUT/'captions.srt').open('w') as fh:
  for i,c in enumerate(groups,1):fh.write(f"{i}\n{srt(c['start'])} --> {srt(c['end'])}\n{c['text']}\n\n")
 (OUT/'captions.json').write_text(json.dumps(groups,indent=2))
 concat=OUT/'parts.txt';concat.write_text(''.join(f"file 'part-{i:02d}.wav'\n" for i in range(8)))
 run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(concat),'-ac','2','-ar','48000',str(OUT/'narration.wav')])
 run(['ffmpeg','-y','-v','error','-i',str(OUT/'narration.wav'),'-c:a','libmp3lame','-b:a','160k','-ar','48000',str(OUT/'narration-embedded.mp3')])
 (OUT/'speech-audit.json').write_text(json.dumps(dict(scene_starts=STARTS,recorded_speed_ratios=rates,caption_groups=len(groups),word_events=len(all_words),text=LINES),indent=2))
 print(f'NIAGARA NATURAL VOICE PASS: {len(all_words)} word events, {len(groups)} caption groups, no speed-up.',flush=True)
asyncio.run(main())
