# Curio Bureau 006 — Dagen H production handoff (Oct 10 2026)

## Completed render candidates
- Native 2160×3840, 30 FPS, **H.264/AAC MP4**, 2,338 video frames, **77.933 seconds**
- Native 2160×3840, 30 FPS, **VP9/Opus WebM**, **77.938 seconds**
- Both codecs contain 48,000 Hz stereo sound and original 1967-inspired road animation, new neural documentary narration, original composed score and designed Foley, and approximate burned captions.
- Verified MP4 loudness **−13.9 LUFS** and **−1.4 dBFS true peak**.
- Measured voice-scene gaps: **0.26–0.38 seconds**, final tail **1.1 seconds**. The isolated narration WAV contains no >0.85-second low-level gaps using a −37 dBFS silence detection threshold.
- Both final frames decode. Standalone interactive studio source and supporting research/QA package are supplied as conversation attachments.

## NOT FINAL
- Speech service produced no true WordBoundary events. Captions are estimated from word weights within measured scene-length clips; they are not forced-aligned.
- Original City/traffic art is entirely an illustrative reconstruction, with no rights-cleared archival 1967 photographs integrated into picture.
- The first-half buildings and cars, and later repeated road layouts, remain graphically simplified relative to the premium editorial-art benchmark.
- Music/traffic/clock/metal SFX are original synthesized sounds; high-quality recorded field Foley and human audition/creative approval are not done.
- Visuals rendered directly to native 4K canvas, but FFmpeg received high-quality JPEG frames through image2pipe, rather than the strict all-lossless-PNG intermediate required for the final master.
- Therefore status is **RENDER CANDIDATE / CREATIVE QA NOT PASSED**. Never label these as FINAL.

## Sources
Swedish transport museums (https://www.statensmuseermtf.se/vara-museer-och-samlingar/vara-samlingar/transporthistoria/vaghistoriska-samlingarna/trafikhistoria/hogertrafik), Sveriges Radio (https://www.sverigesradio.se/artikel/50-ar-med-hogertrafik and https://www.sverigesradio.se/artikel/6767655).
The selected narration conforms to these source-checked facts about 1955 vote, 1963 decision, the controlled 04:50 repositioning, the 05:00 rule change, and traffic restrictions.

Source and attachments are in the user's conversation workspace, not committed to the public repository, to avoid redistributing any font binaries or large media through GitHub.
