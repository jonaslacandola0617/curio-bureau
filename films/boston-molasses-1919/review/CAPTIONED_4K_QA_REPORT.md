# Curio Bureau 005 — Corrected 4K Review QA
Status: RENDER CANDIDATE — NOT FINAL MASTER (October 10, 2026).

Delivered in conversation: 76s native 2160x3840 30FPS captioned H264/AAC MP4, captioned VP9/Opus WebM, and 1080x1920 mobile MP4.
Verified: all 2280 video frames in MP4; 76.000s duration; 48kHz stereo; final frame decodable. WebM: 76.018s, VP9 2160x3840 30FPS, Opus 48kHz stereo.
Encoded MP4 EBU R128: -14.1 LUFS, 7.8 LU loudness range, -1.3 dBFS true peak. No audio silence intervals lasting 0.7s below -45dBFS.

Build failure was caused by Edge TTS returning speech with no WordBoundary metadata. Thus the initial SRT was EMPTY.
That failure was corrected by burning 36 syllable-weighted and scene-duration-based phrase captions into the revised MP4 and WebM. These cues are estimated, NOT verified word-level forced alignment.
Source generator patched to fail closed when captions are empty and add visibly marked fallback timing.

Creative QA remains below locked quality ceiling: simplified city facades and schematic fluid; limited archival usage; critical listening on headphones and phones incomplete.
An accurate video codec and LUFS target do NOT prove professional score, effects, or narration. Do NOT label as FINAL.

Sources and fact lock: preproduction/research.md, preproduction/asset_manifest.md.
Production source: studio/scene.js; scripts/render_ep005.js; scripts/audio_ep005.py.
Corrected videos are distributed as conversation artifacts, not committed to GitHub.