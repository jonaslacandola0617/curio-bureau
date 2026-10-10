#!/usr/bin/env python3
"""Produce a precisely scene-timed documentary narration using Microsoft's neural speech."""
import asyncio, os, subprocess, pathlib
import edge_tts

OUT=pathlib.Path("dist/samoa-2011");OUT.mkdir(parents=True,exist_ok=True)
VOICE=os.environ.get("CURIO_TTS_VOICE","en-US-AndrewNeural")
SEGMENTS=[
  (8.0,"On December twenty ninth, twenty eleven, Samoa did something extraordinary. It took an entire day off the calendar."),
  (8.0,"The next day was not Friday the thirtieth. It was Saturday, December thirty first. Friday simply never happened."),
  (9.0,"It wasn't magic or a broken clock. Samoa changed which side of the International Date Line its calendar followed."),
  (9.0,"For years, Samoa had been almost a full day behind Australia and New Zealand, making business between them a headache."),
  (8.0,"So Samoa chose to join its main trading partners on the other side of that invisible line through the Pacific."),
  (9.0,"When midnight arrived, the clock kept moving, but the date jumped forward. Twenty four hours vanished in a single night."),
  (7.0,"One strange detail? Employees were still entitled to pay for the Friday they never lived through."),
  (6.0,"Time zones aren't laws of nature. They're agreements. And Samoa decided to rewrite one."),
]
def run(args):
    p=subprocess.run(args,check=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return p.stdout.decode(errors='replace').strip()
async def speech():
    for i,(secs,text) in enumerate(SEGMENTS):
        path=OUT/("voice-%02d.mp3"%i)
        await edge_tts.Communicate(text,VOICE,rate="+7%",pitch="-2Hz").save(str(path))
        length=float(run(["ffprobe","-v","error","-show_entries","format=duration","-of","default=noprint_wrappers=1:nokey=1",str(path)]))
        # Fit speech inside the scene, then leave a quiet tail for visual punctuation.
        target=secs-.23
        speed=max(.55,min(1.7,length/target))
        filt="atempo=%.6f,apad,atrim=0:%.6f,afade=t=in:st=0:d=0.08,afade=t=out:st=%.6f:d=0.18"%(speed,secs,secs-.18)
        part=OUT/("part-%02d.wav"%i)
        run(["ffmpeg","-y","-v","error","-i",str(path),"-af",filt,"-ac","2","-ar","48000","-c:a","pcm_s16le",str(part)])
    concat=OUT/"parts.txt"
    concat.write_text("".join("file 'part-%02d.wav'\n"%i for i in range(len(SEGMENTS))))
    run(["ffmpeg","-y","-v","error","-f","concat","-safe","0","-i",str(concat),"-c:a","pcm_s16le",str(OUT/"narration.wav")])
    print("Scene-aligned narration ready:",OUT/"narration.wav")
asyncio.run(speech())
