# Episode 009 — Owner Review Feedback and R2 Revision Contract

**Owner feedback received October 12, 2026.** Episode 008 screenshot versus Episode 009 at the opening indicates inconsistent subtitle treatment. EP008 uses one centered rounded semi-transparent dark box, fine warm-gold edge and measured Manrope phrase wrap; EP009 used multiple full-width separate flat bars. Owner says general animation quality is valid and SFX are good, the voice emotion is improved but still not expressive enough. Owner requested raising **narration and SFX by about 2–4 dB** and preparing publishing copy.

## Applied for R2 (not yet a release signoff)
- **Captions:** EP009's separate bars replaced with same core `caption(t)` code geometry/style as EP008: 916-unit wide one rounded translucent navy panel centered near logical y=946, stroke warm-gold, 38px Manrope 800, actual glyph-based wrap and 120ms appearing/disappearing alpha ramps. This is a style consistency correction. **It does not fix missing word-level alignment**, which remains a distinct hold.
- **Audio mixing:** Narration bus +3.0 dB and designed SFX bus +3.0 dB *relative to the unchanged score bus*, with a warmer final integrated loudness target of **−12 LUFS**, true peak goal **−1.0 dBTP**. Final ratio and absolute perceived loudness depend on limiter/mastering; measure encoded R1→R2 and listen, never equate exact bus gain to a guaranteed 3dB louder final encode.
- **Emotional delivery:** Current GuyNeural synthetically varied rates/pitches but full emotional performance still lacks owner-targeted dramatic emphasis. R2 does not fabricate an emotional voice improvement from gain alone; future options include recording an actual voice actor, voice-line direction, emphasis retakes, and human auditioned A/B comparisons. Do not call TTS objectively 'more emotional' without human judgment.
- **Creative approval:** owner said the animation is valid and designed SFX are valid, but asked caption design consistency and an additional boost. Do not call FINAL until R2 full encoded footage reviewed and word-precise captions approved.

## Required technical QA after render
1. Visually compare center captions R2 to EP008 reference screenshots and ensure no introduced collision with tank/speaker/radio.
2. Actual encoded MP4+WebM 2160×3840/30, H264/AAC & VP9/Opus.
3. Measure actual R2 LUFS and true peak from decoded audio. Ensure no clipping or perceptual harshness; phone+headphone mix audit.
4. Verify recorded narration intervals; no extended silent gaps, and no caption ahead/behind words.
5. Owner full-speed judgment of emotional narration; raising levels is not a substitute for inflection.

## Status
R2 is **REVIEW CANDIDATE** until owner confirms both picture+sound. Publishing copy can be released separately but should not link an unverified FINAL.
