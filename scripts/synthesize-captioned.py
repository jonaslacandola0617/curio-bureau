#!/usr/bin/env python3
"""Narration in timed 8-scene sections, word-boundary captions, SRT from spoken speech."""
import asyncio,json,pathlib,subprocess
import edge_tts

OUT=pathlib.Path('dist/samoa-2011');OUT.mkdir(parents=True,exist_ok=True)
VOICE='en-US-AndrewNeural'
STARTS=[0,8,16,25,34,42,51,58,64]
LINES=[
"On December twenty ninth, twenty eleven, Samoa did something extraordinary. It took an entire day off the calendar.",
"The next day was not Friday the thirtieth. It was Saturday, December thirty first. Friday simply never happened.",
"It wasn't magic or a broken clock. Samoa changed which side of the International Date Line its calendar followed.",
"For years, Samoa had been almost a full day behind Australia and New Zealand, making business between them a headache.",
"So Samoa chose to join its main trading partners on the other side of that invisible line through the Pacific.",
"When midnight arrived, the clock kept moving, but the date jumped forward. Twenty four hours vanished in a single night.",
"One strange detail? Employees were still entitled to pay for the Friday they never lived through.",
"Time zones aren't laws of nature. They're agreements. And Samoa decided to rewrite one."
]
def run(args):
 p=subprocess.run(args,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 return p.stdout.decode(errors='replace').strip()
def srt_time(s):
 n=round(max(0,s)*1000);return f"{n//3600000:02d}:{n//60000%60:02d}:{n//1000%60:02d},{n%1000:03d}"
async def main():
 all_words=[]
 for i,(line,start,end) in enumerate(zip(LINES,STARTS,STARTS[1:])):
  audio=OUT/f'voice-{i:02d}.mp3'
  words=[]
  with audio.open('wb') as output:
   async for chunk in edge_tts.Communicate(line,VOICE,rate='+6%',pitch='-2Hz',boundary='WordBoundary').stream():
    if chunk['type']=='audio':output.write(chunk['data'])
    elif chunk['type']=='WordBoundary':words.append(dict(text=chunk['text'],start=chunk['offset']/10_000_000,end=(chunk['offset']+chunk['duration'])/10_000_000))
  if len(words)<5:raise RuntimeError(f'TTS word boundary events unavailable for segment {i}')
  duration=float(run(['ffprobe','-v','error','-show_entries','format=duration','-of','default=noprint_wrappers=1:nokey=1',str(audio)]))
  target=end-start-.23
  speed=duration/target
  if not (.5<=speed<=1.95):raise RuntimeError(f'Narration pacing unsupported: {i} {speed}')
  # use chain of atempo filters to avoid clipping.
  raw=OUT/f'part-{i:02d}.wav'
  af=f'atempo={speed:.7f},apad,atrim=0:{end-start},afade=t=in:st=0:d=.07,afade=t=out:st={end-start-.12}:d=.12'
  run(['ffmpeg','-y','-v','error','-i',str(audio),'-af',af,'-ac','2','-ar','48000',str(raw)])
  for word in words:
   all_words.append(dict(text=word['text'],start=round(start+word['start']/speed,3),end=round(min(end-.05,start+word['end']/speed),3)))
 # subtitle groups: <=6 words and 1.8s, clipped scene-accurate intervals.
 captions=[]; group=[]
 def commit():
  if not group:return
  content=' '.join(w['text'].strip() for w in group).strip()
  if content:captions.append({'start':round(group[0]['start'],3),'end':round(max(group[-1]['end'],group[0]['start']+.52),3),'text':content})
  group.clear()
 for i,w in enumerate(all_words):
  if group and (len(group)>=5 or len(' '.join(t['text'] for t in group+[w]))>36 or (w['end']-group[0]['start'])>1.6 or w['start']-group[-1]['end']>.6):
   commit()
  group.append(w)
  if w['text'].endswith(('.', '!', '?')):commit()
 commit()
 if len(captions)<35:raise RuntimeError('Too few precise phrase captions: '+str(len(captions)))
 (OUT/'captions.json').write_text(json.dumps(captions,ensure_ascii=False,indent=2))
 with (OUT/'captions.srt').open('w') as out:
  for i,c in enumerate(captions,1):out.write(f"{i}\n{srt_time(c['start'])} --> {srt_time(c['end'])}\n{c['text']}\n\n")
 concat=OUT/'parts.txt';concat.write_text(''.join(f"file 'part-{i:02d}.wav'\n" for i in range(8)))
 run(['ffmpeg','-y','-v','error','-f','concat','-safe','0','-i',str(concat),'-ar','48000','-ac','2',str(OUT/'narration.wav')])
 print('Narration + word boundaries:',len(all_words),'phrases:',len(captions))
asyncio.run(main())
