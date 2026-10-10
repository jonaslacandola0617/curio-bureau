# Curio Bureau 002 — Centralia | Natural-Voice Correction v2

**This version replaces the original Centralia audio**, whose speech accelerated especially around 38 seconds and 55 seconds.

Fixed by rewriting the voiceover to fit each scene, NOT by time-stretching. All eight segments used actual TTS playback tempo **1.0x** (natural speed); earlier speech finishes naturally without manipulation. Word timestamps and all 37 burned-caption segments were regenerated from the revised narration.

Actual natural voice durations by scene: [6.984,7.464,6.624,6.216,7.344,7.632,6.240,3.600] seconds.
Scene windows: [8,8,9,9,8,9,7,6] seconds. No segment required a speed-up.

Files:
- `Curio_Bureau_Centralia_NATURAL_VOICE_v2.mp4` — upload-ready, H.264 1080x1920 30fps with narration, audible music and Drive SFX, burned-in captions
- `Curio_Bureau_Centralia_NATURAL_VOICE_v2.webm` — alternative video
- `Curio_Bureau_Centralia_NATURAL_VOICE_v2.html` — interactive voice-embedded animation studio
- `captions_v2.srt` — word-aligned subtitle file
- Review sheet and verified codec/loudness checks

Confirmed GitHub Actions master: https://github.com/jonaslacandola0617/curio-bureau/actions/runs/38025113382
Exact sound and source revision: `a5f991a27ff67c02d39f95f7fe615f81875d9a25`.
GitHub source branch: `film/centralia-underground-fire`.
The initial `delivery/centralia-002` branch contains the older incorrectly paced audio. Do not use that version.
