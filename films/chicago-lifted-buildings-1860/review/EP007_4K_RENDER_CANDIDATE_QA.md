# EP007 Chicago — Native 4K Render Candidate QA (2026-10-11)
Status: RENDER CANDIDATE — NOT FINAL MASTER.

Deliverables completed in the conversation workspace:
- 78.533333-second H.264/AAC MP4, **native 2160x3840 / 30fps**, 2,356 frames, 48kHz stereo audio.
- 78.541-second VP9/Opus WebM, **native 2160x3840 / 30fps**, 2,356 encoded frames, 48kHz stereo audio.
- Both frames/streams decodable, including native 4K WebM final frame, with full video decoding for both formats returning exit code 0.
- Voice narration 77.312s, nine measured between-scene gaps of 0.25–0.37s, ~1.22s final tail.
- Encoded MP4 loudness -13.84 LUFS, true peak -1.45 dBTP.
- 11 actual MP4 encoded frame checkpoints, TikTok/YouTube Shorts centered-caption overlay contact sheets, voice/music/Foley stems.
- Actual historic nineteenth-century Edward Mendel engraving in archival beat, with cautious date attribution.
- Editable Python compositor, separate music/Foley Python generator, browser-openable 4K Canvas editor source and supporting research in user-delivered ZIP.

Release blockers:
1. TTS engine returned zero word timestamps; captions are only estimated phrase timing and need forced alignment/manual verification.
2. Some period facades, sewer engineering illustrations and jack mechanics are still visually simple; premium editorial 2D/2.5D creative QA not passed.
3. Generated illustrative photo raster starts at 941x1672 (resampled as background) although composition/encoded frames and vector text are native 4K.
4. Image-frame pipeline streams native raw RGB losslessly, not an archived full PNG sequence.
5. Subjective sound/phone listening, soundtrack instrument sample rights and rumble SFX license check remain open.

No claim of FINAL MASTER until every hard release gate has passed. The corrected MP4/WebM and studio source are user conversation attachments, not committed binary assets to GitHub.