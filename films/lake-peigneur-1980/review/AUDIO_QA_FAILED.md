# EP004 Audio QA — FAILED (2026-10-10)

**Status: QA FAILED. DO NOT PUBLISH OR LABEL FINAL.**

## Confirmed production errors

- Narration in the MP4 uses temporary offline eSpeak, not the professional voice recorded for the project. Its artificial delivery is unacceptable for the Curio Bureau release specification.
- The purported "score" is a procedural low-frequency synthesis bed, not an adequately composed and perceptibly audible documentary music score.
- The source sound mix computes `mix = voice + score * (.28 - .115 * active)`, reducing the combined score and SFX to approximately 16.5–28% of their prior amplitude. Within `score`, actual user-library effects were also loaded at source gains ~0.13–0.26. Thus sound events can be effectively buried.
- The prior -14.16 LUFS / -1.23 dBTP figure only establishes overall mix loudness and peak compliance, NOT adequate music audibility, SFX audibility, voice quality, or cinematic dynamics.
- The subtitle groups are approximate, not aligned to the approved final spoken recording.
- Audio release QA was not completed with perceptual listening; passing ffprobe checks was wrongly presented as significant completion.

## Required correction before any release

1. Reject eSpeak narration completely. Use recorded natural documentary voice at its original pace; retime scenes rather than accelerate speech.
2. Compose/license an audible, appropriately evolving real music track with an actual musical arc (not only low-frequency sine tones).
3. Re-design layered diegetic and transition SFX; use the real source library with documented provenance, correct gains, and audible scene-specific purpose.
4. Build a 48 kHz stereo mix using separate voice/music/ambience/SFX/impact buses, with sidechain-style ducking only when voice requires it. Listen on both headphones and a phone speaker.
5. Regenerate word-synchronized captions and SRT from the final voice recording.
6. Inspect entire encoded release at natural playback volume and recheck LUFS, true peak, clipping, masking, and intentional dynamic progression.

The existing 75-second 4K MP4 is a rejected technical motion draft only; it is not an approved Curio Bureau product.