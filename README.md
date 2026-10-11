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

## Governing production policy (October 2026)
**Authoritative:** [Curio Bureau Master Production Bible](production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md).
**Start here:** [Project governance and reading order](production/bible/v1.1/README.md).
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
