#!/usr/bin/env python3
"""Centralia voice and punctuation-perfect SRT aligned to Edge TTS WordBoundary events."""
import asyncio,json,pathlib,subprocess
import edge_tts
OUT=pathlib.Path('dist/centralia-1962');OUT.mkdir(parents=True,exist_ok=True)
VOICE='en-US-AndrewNeural'
STARTS=[0,8,16,25,34,42,51,58,64]
LINES=[
"In Pennsylvania, a fire has burned beneath one town for more than sixty years. It's still burning today.",
"This is Centralia. In nineteen sixty two, a fire likely spread from a trash dump into abandoned coal mines.",
"Old mine tunnels linked coal seams. Heat moved underground, while fresh air kept feeding the flames.",
"Crews drilled, dug, and tried to stop it. But the fire kept moving through hidden passages.",
"In nineteen eighty three, Route sixty one cracked. Stopping the fire could cost over six hundred million dollars.",
"Then, forty two million dollars funded relocation. Families moved away, and entire streets began disappearing.",
"Now Centralia is nearly empty. The fire still burns beneath dangerous, unstable ground.",
"The town emptied, one home at a time. The fire didn't."
]
def run(args):
 p=subprocess.run(args,check=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 if p.returncode:raise RuntimeError('FFmpeg command failed: '+str(args)+'\n'+p.stderr.decode(errors='replace'))
 return p.stdout.decode(errors='replace').strip()
def fmt(s):
 n=round(max(0,s)*1000);return f'{n//3600000:02d}:{n//60000%60:02d}:{n//1000%60:02d},{n%1000:03d}'
async def main():
 words_all=[]
 for i,(line,start,end) in enumerate(zip(LINES,STARTS,STARTS[1:])):
  dst=OUT/f'voice-{i:02d}.mp3'; words=[]
  with dst.open('wb') as audio:
   async for chunk in edge_tts.Communicate(line,VOICE,rate='-2%',pitch='-2Hz',boundary='WordBoundary').stream():
    if chunk['type']=='audio':audio.write(chunk['data'])
    elif chunk['type']=='WordBoundary':words.append(dict(start=chunk['offset']/10_000_000,end=(chunk['offset']+chunk['duration'])/10_000_000))
  scripted=line.split()
  if len(words)!=len(scripted):raise RuntimeError(f'Word-boundary mismatch scene {i}: {len(words)} vs {len(scripted)}')
  duration=float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(dst)]))
  # Never stretch every paragraph to occupy its entire scene. A shorter take
  # should finish naturally, leaving musical/visual breathing room.
  scene_length=end-start
  usable=scene_length-.30
  proposed_tempo=duration/usable
  print(f'SCENE {i+1}: natural_voice={duration:.3f}s / window={usable:.3f}s / tempo_needed={proposed_tempo:.4f}',flush=True)
  if proposed_tempo>1.045:
   raise RuntimeError(
    f'SCENE {i+1} narration would sound rushed: {duration:.2f}s speech in {usable:.2f}s. '
    f'Rewrite its words instead of forcing {proposed_tempo:.2f}x speed.'
   )
  speed=max(1.0,proposed_tempo)
  actual_duration=duration/speed
  fade_out=max(0.15,actual_duration-.18)
  filtered=f'atempo={speed:.7f},afade=t=in:st=0:d=0.07,afade=t=out:st={fade_out:.3f}:d=0.15,apad,atrim=0:{scene_length}'
  run(['ffmpeg','-y','-v','error','-i',str(dst),'-af',filtered,'-ac','2','-ar','48000',str(OUT/f'part-{i:02d}.wav')])
  for w,token in zip(words,scripted):
   words_all.append(dict(text=token,scene=i,sentence_end=token.endswith(('.', '!', '?')),start=round(start+w['start']/speed,3),end=round(min(end-.04,start+w['end']/speed),3)))
 captions=[];group=[]
 def finish():
  if not group:return
  caption=' '.join(w['text'] for w in group).strip()
  captions.append(dict(start=round(group[0]['start'],3),end=round(max(group[-1]['end'],group[0]['start']+.42),3),text=caption))
  group.clear()
 for w in words_all:
  if group and (group[-1]['scene']!=w['scene'] or group[-1]['sentence_end'] or len(group)>=5 or len(' '.join(x['text'] for x in group+[w]))>36 or w['end']-group[0]['start']>1.60 or w['start']-group[-1]['end']>.6):finish()
  group.append(w)
  if w['sentence_end']:finish()
 finish()
 if len(captions)<35:raise RuntimeError('Not enough word-synced subtitles: '+str(len(captions)))
 with (OUT/'captions.srt').open('w') as f:
  for i,c in enumerate(captions,1):f.write(f"{i}\n{fmt(c['start'])} --> {fmt(c['end'])}\n{c['text']}\n\n")
 (OUT/'captions.json').write_text(json.dumps(captions,indent=2))
 concat=OUT/'parts.txt';concat.write_text(''.join(f"file 'part-{i:02d}.wav'\n" for i in range(8)))
 run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(concat),'-ac','2','-ar','48000',str(OUT/'narration.wav')])
 run(['ffmpeg','-y','-v','error','-i',str(OUT/'narration.wav'),'-c:a','libmp3lame','-b:a','160k','-ar','48000',str(OUT/'narration-embedded.mp3')])
 print('CENTRALIA NATURAL-PACE NARRATION:',len(words_all),'word events;',len(captions),'captions; all scenes <= 1.045x tempo.',flush=True)
asyncio.run(main())
