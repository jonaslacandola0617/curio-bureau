CURRENT OWNER STANDARD (18 October 2026): Sun-disappearance full film is approved and governs new production. Apply production/approved-benchmarks/SUN_DISAPPEARED_PRODUCTION_STANDARD.md and production/templates/sun-standard/RELEASE_CHECKLIST.md. Whole scene/camera states12fps, native1080×1920/30fps posting MP4, exact30fps shared ending, meaningful change about every1.5–2s, clean text/graphics with no soft halo; preserve independent factual/audio/caption/creative/export evidence. Older mandatory4K/WebM and caption-haze instructions are superseded for new work.

# 11 — MASTER QA / RELEASE CHECKLIST (P0/P1/P2)
A checked automatic condition certifies only that condition; it never certifies subjective artistic excellence.

## P0 — Mandatory release gates
- [ ] HISTORICAL CLAIMS: final script numbers, dates, geographical references and legal/causal language each cite sources; speculation separated from fact.
- [ ] RIGHTS: original archive/license/provenance register with item-specific permissions; original reconstructions appropriately labeled.
- [ ] TRUE 4K MP4: actual 2160×3840, 30fps, H.264, AAC stereo 48kHz, original native pixels, no 1080p upscale; ffprobe record.
- [ ] TRUE 4K WEBM: actual 2160×3840, 30fps, VP9, Opus 48kHz stereo; ffprobe record.
- [ ] COMPLETE: video decodes; all planned frames incl first/last, duration/ending; no truncated sections.
- [ ] NATURAL VOICE: no eSpeak or unapproved synthetic rate, clipped/mispronounced first/last words or missing segments.
- [ ] VOICE GAPS: isolated WAV detector report, all intentional/discretionary; >0.85s unplanned editorial FAIL; >1.20s between passages absolute FAIL; no >3s narrative dead zones.
- [ ] CAPTIONS: verified to actual final WAV word timings, burned centered 42–58% and legible in real platform-mask previews for BOTH encoded MP4 and WebM, plus SRT.
- [ ] AUDIO: clearly audible music and genuine SFX appropriate to visible action in ACTUAL encodes; critical headphones/phone passes; no clipping or missing channel.
- [ ] AUDIO LOUDNESS: integrated ~−14 to −12 LUFS; true peak ≤−1 dBTP, checked on encoded MP4 and WebM; tone not sacrificed for measurement.
- [ ] BRAND FONTS: actual Playfair and Manrope paths/hashes verified in render, no fallback or horizontal glyph clipping.
- [ ] HUMAN RELEASE APPROVAL: footage watched at normal speed and phone size by creator/art director; no P0 open.

## P1 — Creative quality gates
- [ ] FRAME 0 already has one visible consequence and no blank slate/logo pre-roll.
- [ ] 0–1s is intelligible at small phone-size without sound; 0–3s tells unusual premise; 0–5s leaves a question.
- [ ] 3 differing hook animatics evaluated before production; rationale attached.
- [ ] 5 style frames approved, including MOST DIFFICULT mechanism shot, not only title/cover.
- [ ] Full-film environment detail comparable to first-frame quality; no visible clip-art or placeholder human/vehicle/machine.
- [ ] No three consecutive shots with same family/camera/hero treatment without a meaningful new physical state.
- [ ] Camera movement is semantic, not generic animated movement; transitions connect real forms when appropriate.
- [ ] Source evidence is visible as proof; not hidden in tiny cards or falsely historical.
- [ ] Music has identifiable rhythmic/harmonic development; SFX actually recognizable on small phone speakers.
- [ ] Final spoken claim and closing graphic align; tail 0.8–1.8s; no slow static logo hold.

## P2 — Finishing
- [ ] Grain, paper shadow, halftone, temperature and gold-line weights consistent where used.
- [ ] Accents semantically coded; coral used for consequences, not all decorative movement.
- [ ] Cropped archival stills have dates, credit and sufficient effective source resolution.
- [ ] Encoded stroke widths and fine labels remain crisp at 100% video pixels.
- [ ] Lower-third/right-side app controls obscure no critical action or metadata.
- [ ] Source project, ZIP, sound stems, licensing and QA report exist and versions match export hashes.

## Recommended automated commands
```bash
ffprobe -v error -show_streams -show_format -of json Curio_Bureau_4K_MASTER.mp4 > qa/mp4_ffprobe.json
ffprobe -v error -show_streams -show_format -of json Curio_Bureau_4K_MASTER.webm > qa/webm_ffprobe.json
ffmpeg -i voice.wav -af silencedetect=noise=-37dB:d=0.85 -f null - 2>qa/voice_gaps.txt
ffmpeg -i Curio_Bureau_4K_MASTER.mp4 -af ebur128=peak=true -vn -f null - 2>qa/audio_loudness.txt
ffmpeg -sseof -0.4 -i Curio_Bureau_4K_MASTER.mp4 -frames:v 1 qa/last.png
```

Suggested procedural `qa/technical.json`:
```
{ "mp4":{"w":2160,"h":3840,"fps":30,"video_codec":"h264","audio_codec":"aac"},
  "webm":{"w":2160,"h":3840,"fps":30,"video_codec":"vp9","audio_codec":"opus"},
  "voice_max_gap_s":0.0,"captions_final_aligned":false,"font_hashes":{},
  "sampled_frames_checked":[],"archive_rights_pass":false,
  "phone_ui_caption_pass":false,"subjective_art_approved":false,"release":"RENDER CANDIDATE" }
```
The values here are a schema example, **not actual passing data**.

## Regression suite based on identified defects
- **004:** fail for multiple 3–5s gaps, static intro, low captions, poor lake/miner detail.
- **005:** fail for long scene-padding gaps, repeated wave/city, low caption placement, plate diagram oversimplification.
- **006:** fail for repeated environment geometry despite correct gap metric, unless new camera/physical understanding shown.
- **007:** fail if rasterized hero art is not matched by the vector construction scenes, even if 4K file technically passes.

## Release labels
`WIP → DESIGN REVIEW → ANIMATIC → AUDIO COMPLETE → RENDER CANDIDATE → CREATIVE QA PASSED + TECHNICAL QA PASSED → FINAL MASTER`. A missing or unverified required item keeps status at `RENDER CANDIDATE` or `QA FAILED`. Passing FFmpeg is never enough.