# Captions and final acceptance contract

## Subtitles
- Burn Manrope directly onto **MP4 and WebM**; deliver `captions.srt` too.
- Derive time ranges from neural TTS **WordBoundary** events (adjusted to any tempo processing), not invented scene starts.
- Phrases of 2–5 words, <= ~36 characters where possible, at 1–2 lines.
- Compose safe lower-third at x=110..970, baseline y~1565, far above platform control area.
- Contrast ≥4.5:1 against backing; restrained ivory on midnight overlay and gold emphasis for historical nouns.
- Captions cannot cover the primary documentary evidence; move evidence upper within the design.

## Layout gating
- Master 1080x1920; minimum x margin 84; editorial top 120; critical text y <= 1650.
- Use actual measured Playfair/Manrope text, fit width <=912, and assert no title/caption overflow.
- Top/side letterforms plus rotated documents must be pixel inspected; purposefully cropped photography okay, clipped core text never okay.
- At 0,10,...100%, every boundary, major transition and last frame: render PNG contact sheets with exact final fonts, inspect and repair.

## Technical gating
- Verify 1080x1920, CFR 30, duration >=63.5 sec, H.264 yuv420p and AAC 48k stereo; no silent master.
- MP4 CRF 16–18 slow or better; no upscale from small preview.
- SFX presence measured from actual mixed audio; voice and music measurable and audible.
- Extract audio sample and compare to intended cue sheet.
- Export from deterministic fixed-time frames plus offline audio when feasible; browser preview and WebM still available.
- Run only marked QA PASSED when both automated media checks and human visual listening review pass. A GitHub Actions green check alone is not sufficient.
