# Curio Bureau

**Stories, systems, and surprises.** A motion-design production repository.

This repository is the **source of truth for production code and technical documentation**, not a replacement for the shared Google Drive sound-effects library.

## Branch policy
- `main`: stable project infrastructure and reviewed releases.
- `film/samoa-day-disappeared`: Samoa pilot film — *The Day That Disappeared*.
- `film/<slug>`: a separate branch for each future video.
- `brand/<topic>`, `tooling/<topic>`, `audio/<topic>`: dedicated branches for other projects or workstreams.
- Save meaningful milestones as commits; use pull requests to review and merge into `main`.
- Do not overwrite another topic's branch or force-push without a specific reason.

## New original sound-effects library (October 2026)
[Curio Bureau SFX v1 — 50 original audio cues](https://github.com/jonaslacandola0617/curio-bureau/releases/tag/curio-sfx-v1-original) · [FLAC/Catalog](audio/curio_sfx_v1/CATALOG.csv) · [Existing library audit](production/audio-sfx-v1/LIBRARY_AUDIT.md) · [Sound direction guide](production/audio-sfx-v1/SOUND_DIRECTION_GUIDE.md). The sound pack contains synthesized designs only; authentic period Foley and professionally directed narration remain future improvements.

## Governing production policy (October 2026)
**Authoritative, v1.3:** [Curio Bureau Master Production Bible](production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md), including the v1.2 tutorials-derived craft rules and **v1.3 first-party Vox graphics-only source-validated craft upgrades** (20 techniques adopted, 12 proposed, eight original moving technical tests).
**Start here:** [Project governance and reading order](production/bible/v1.1/README.md). [Motion Mastery Lab reference library](production/motion-lab/v1/README.md). [Graphics-only Vox Motion Mastery Lab v2 (adopted)](production/motion-lab/v2/README.md). [Future-film motion v1.3 adapter](production/prompts/FUTURE_EPISODE_MOTION_GRAPHICS_V13_ADDENDUM.md). [Episode 009 current master production prompt](production/prompts/EP009_NEXT_EPISODE_MASTER_PRODUCTION_PROMPT.md). [Episode 008 archived directive](production/prompts/EP008_NEXT_EPISODE_MASTER_PRODUCTION_PROMPT.md).
**For future ChatGPT sessions:** [Read-and-digest prompt (no video creation)](production/READ_AND_DIGEST_PROMPT_FOR_CHATGPT.md) and [AGENTS.md](AGENTS.md).

The October 2026 v1.1 audit under `production/bible/v1.1/` documents known gaps: earlier named Episode 001–003 masters were not all recovered, and Vox/viral-video studies did not include full external frame-by-frame playback or private audience analytics. Do not overstate observation coverage.

## Production specification
- Storytelling: Vox-inspired **editorial motion graphics**, with Curio Bureau's distinct identity.
- Palette: midnight navy `#0D1C2B`, ivory `#F5F0E7`, muted gold `#C8A26B`, coral `#D57864`.
- Master: **true native 2160 × 3840 vertical, 30fps**, separately verified **H.264/AAC MP4 and VP9/Opus WebM** with voice, audible music/SFX, and center-safe burned captions; optional 1080p derivative is NOT a master.
- Authoring: deterministic HTML canvas animation; preserve interactive play, scrub, replay, and Export WebM controls.
- SFX source: the separately maintained [Google Drive SFX folder](https://drive.google.com/drive/folders/1JsF-myJsH4rnyy0NI-OjDL6ZVrSVeC81). Do not commit the bulk library.
- A video is **not final** until rendered, checked for correct visuals, and verified to contain narration, music, and SFX. Code commits or draft exports must not be described as finished masters.

## Workflow
1. Create a dedicated project branch.
2. Commit scripts, scene descriptions, assets we own, and production code early.
3. Use GitHub Actions for repeatable browser/video builds where available.
4. Upload rendered media as GitHub Actions artifacts or Releases rather than committing large binary masters.
5. Review the render and soundtrack, then merge approved work to `main`.

The first production lives on `film/samoa-day-disappeared`.
