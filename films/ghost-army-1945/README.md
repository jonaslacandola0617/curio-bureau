# Curio Bureau Episode 009 — THE ARMY THAT WASN'T THERE

**Current status: ART / AUDIO PREFLIGHT; candidate production, NOT final.** Historical subject: World War II Ghost Army (U.S. Army 23rd Headquarters Special Troops) and Operation Viersen, March 1945. Brand authority: main-branch `production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md` v1.2 and `production/prompts/EP009_NEXT_EPISODE_MASTER_PRODUCTION_PROMPT.md`.

## Creative promise
A visually imposing American tank is revealed to be rubber and air, then the story shows how loudspeakers, false radio traffic, and misleading military staging projected the appearance of two divisions from a much smaller deception unit. The unique story mechanism is **visual spectacle that cannot work without sound**. All footage is **original Canvas editorial illustration**, explicitly marked `ILLUSTRATIVE RECONSTRUCTION`. The film does not pretend to show actual 1945 footage, or use original WWII radio/battle sounds.

## Factual sources
- U.S. Army: [Ghost Army explained](https://www.army.mil/article/247350) and [sonic deception recording project](https://www.army.mil/article/240486)
- National WWII Museum: [Ghost Army: Canvas and Camouflage](https://www.nationalww2museum.org/war/articles/ghost-army-canvas-and-camouflage) and [2020 exhibition facts](https://www.nationalww2museum.org/war/articles/wwii-museum-exhibit-ghost-army)
- Full topic comparison, true-versus-inferred claims and image/audio provenance: `docs/TOPIC_AND_RESEARCH_LOCK.md`.

## Technical workflow
- `src/studio_template.html`: native **2160×3840 Canvas** original artwork and deterministic 30fps absolute-time scenes, browser-openable playback/scrub/WebM where supported.
- `src/build_audio.py`: actual AI-synthesized narration clips (GuyNeural), two genuine A/B narrator voice versions for the opening and the twist, separate original MIDI-rendered music and **16 logged cues** using Curio's original 50-SFX pack. The audio generation outputs 48kHz 24-bit stereo WAV stems, MP3 preview, phrase-timed SRT, timing JSON, cue sheet and honest audio QA. Human evaluation has NOT been completed.
- `src/preflight.py`: 27 sampled moving-state frames across 9 scenes with strict full-pixel native-4K and real font checks. QA snapshots should not be confused with full-speed creative motion approval.
- `src/render.py`: full native source scene output through lossless PNG frame pipe to high-quality H.264/AAC MP4, separate VP9/Opus WebM, probe/last-frame decode and evidence-based human creative blockers.
- Workflow `.github/workflows/ep009-ghost-army-preflight.yml` runs audio and art previews. Full native-4K release workflow runs only after art preflight passes.

## Outputs expected, not assumed complete
`CURIO_BUREAU_EP009_NATIVE4K_MP4_REVIEW.mp4`, `CURIO_BUREAU_EP009_NATIVE4K_WEBM_REVIEW.webm`, `CURIO_BUREAU_EP009_SOURCE_REVIEW.zip`, `EP009_NATIVE4K_CONTACT_SHEET.jpg`, audio cue manifest and `ENCODE_QA.json`.

## Release blockers
- No human/owner sign-off yet for actual performed vocal acting, audio A/B choices, full headphone and mobile playback.
- Word boundaries in Edge voice stream have been **zero** in the initial audio pass. Phrase timing is taken from real trimmed speech clips, but precise spoken-word subtitle alignment remains unverified.
- Historical material is independently sourced at story level but the drawn period objects are **interpretative illustrations**, not archive-perfect designs or an eyewitness reconstruction.
- Until actual scene playback, final headphone-mix audition, rights and caption checks pass, user-facing videos must remain `REVIEW CANDIDATE`, never `FINAL MASTER`.

## How to inspect
First view the 27-frame storyboard contact `review/EP009_SHOT_PREFLIGHT_CONTACT.jpg`; then the downloadable GitHub Actions voice auditions and soundtrack preflight; next both encoded 4K review movies, with phone/safe-caption and factual inspection. Leave episode-specific feedback via repo QA notes before production revision.

Originality guard: Do not incorporate museum photos, copied Vox art/tutorial clips, external proprietary music or downloaded commercial stock SFX into this public repo. The original Curio SFX library is in `audio/curio_sfx_v1`. For real authentic physical Foley, rights-cleared recordings can be reviewed individually from Google Drive.
