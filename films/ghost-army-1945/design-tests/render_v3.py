#!/usr/bin/env python3
"""Render distinct browser Canvas frames for original Ghost Army editorial collage review."""
import json, subprocess
from pathlib import Path
from PIL import Image, ImageDraw
from io import BytesIO
from playwright.sync_api import sync_playwright

HERE=Path(__file__).resolve().parent
HTML=HERE/"CURIO_GHOST_ARMY_COLLAGE_V3_PLAYER.html"
OUT=HERE/"rendered"
OUT.mkdir(exist_ok=True)
FPS=24
DURATION=16
frames=FPS*DURATION
silent=OUT/"v3_video_silent.mp4"
final=OUT/"CURIO_GHOST_ARMY_COLLAGE_V3_REVIEW.mp4"
montage=Image.new("RGB",(360*4,640*2),(230,219,195))
checks=[0,1.6,3.1,4.1,5.6,8.3,12.5,15.1]
positions=[round(f*FPS) for f in checks]
ff=[
 "ffmpeg","-nostdin","-hide_banner","-loglevel","error","-y",
 "-f","image2pipe","-framerate",str(FPS),"-vcodec","png","-i","-",
 "-c:v","libx264","-pix_fmt","yuv420p","-preset","veryfast",
 "-crf","20","-r",str(FPS),"-movflags","+faststart",str(silent)
]
with sync_playwright() as pw:
    browser=pw.chromium.launch(headless=True,args=["--no-sandbox","--disable-dev-shm-usage"])
    page=browser.new_page(viewport={"width":850,"height":1340},device_scale_factor=1)
    page.goto(HTML.as_uri(),wait_until="load")
    page.wait_for_function("typeof window.renderAt === 'function'")
    errors=[]
    page.on("pageerror",lambda e: errors.append(str(e)))
    proc=subprocess.Popen(ff,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        canvas=page.locator("#stage")
        for n in range(frames):
            page.evaluate("(t) => window.renderAt(t)",n/FPS)
            frame=canvas.screenshot(type="png",animations="disabled")
            if n in positions:
                im=Image.open(BytesIO(frame)).convert("RGB")
                tile=im.resize((360,640),Image.Resampling.LANCZOS)
                i=positions.index(n)
                montage.paste(tile,((i%4)*360,(i//4)*640))
            proc.stdin.write(frame)
            if n%72==0: print(f"frames {n}/{frames}",flush=True)
        proc.stdin.close()
        if proc.wait(timeout=180)!=0:
            raise RuntimeError("ffmpeg video encoder error: "+proc.stderr.read().decode()[-2000:])
    except Exception:
        try:proc.kill()
        except Exception: pass
        raise
    finally:
        browser.close()
    if errors: raise RuntimeError("browser javascript errors: "+str(errors[:10]))
montage.save(OUT/"CURIO_GHOST_ARMY_COLLAGE_V3_CONTACT.jpg",quality=90)

ROOT=HERE.parents[2] # repo root? films/ghost-army-1945/design-tests => parents[2] is films, not repo
ROOT=HERE.parents[2] if (HERE.parents[2]/"production").exists() else HERE.parents[3]
audio=ROOT/"production/audio/original-sfx-v1/wav"
# Sounds synthesized specifically for Curio Bureau, not archival effects.
events=[
 ("ambience__control_room_low.wav",-24,0,True),
 ("archival__paper_rustle.wav",-9,0,False),
 ("mechanical__latch_small.wav",-10,2450,False),
 ("transitions__paper_camera_push.wav",-8,3480,False),
 ("transitions__quick_reframe.wav",-10,7250,False),
 ("telemetry__receiver_ping.wav",-13,8300,False),
 ("archival__document_stack.wav",-8,11410,False),
 ("reveals__answer_glint.wav",-10,13900,False)
]
args=["ffmpeg","-nostdin","-hide_banner","-loglevel","error","-y","-i",str(silent)]
for name,db,ms,loop in events:
    if loop:args+=["-stream_loop","-1"]
    args+=["-i",str(audio/name)]
filt=[]
for j,(name,db,ms,loop) in enumerate(events,1):
    filt.append(f"[{j}:a]volume={db}dB,adelay={ms}:all=1[a{j}]")
filt.append("".join(f"[a{j}]" for j in range(1,len(events)+1))+f"amix=inputs={len(events)}:duration=longest:dropout_transition=0,atrim=0:{DURATION},alimiter=limit=0.90[combined]")
args+=["-filter_complex",";".join(filt),"-map","0:v:0","-map","[combined]","-c:v","copy","-c:a","aac","-b:a","192k","-t",str(DURATION),"-movflags","+faststart",str(final)]
subprocess.run(args,check=True)
info=json.loads(subprocess.check_output(["ffprobe","-v","quiet","-print_format","json","-show_streams","-show_format",str(final)]))
v=next(s for s in info["streams"] if s["codec_type"]=="video")
a=next(s for s in info["streams"] if s["codec_type"]=="audio")
assert v["width"]==720 and v["height"]==1280
assert v["avg_frame_rate"]=="24/1" and v["nb_frames"]==str(frames)
assert a["codec_name"]=="aac"
assert abs(float(info["format"]["duration"])-DURATION)<.2
qa={"file":final.name,"duration_seconds":float(info["format"]["duration"]),"rendered_distinct_canvas_frames":frames,"fps":FPS,"width":720,"height":1280,"video_codec":v["codec_name"],"audio_codec":a["codec_name"],"sfx":len(events),"story_status":"original illustrative collage, not historical footage","art_direction_status":"review candidate only, not approved"}
(OUT/"V3_RENDER_QA.json").write_text(json.dumps(qa,indent=2))
silent.unlink()
print(json.dumps(qa,indent=2))
