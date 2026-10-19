# CLAUDE.md: illustrated science trial (experiment scope only)

Branch: `experiment/claude-illustrated-workflow-20261019`. Preset: `illustrated-science-trial-v1`.
Full brief: `CLAUDE_PRODUCTION_PROMPT.md` in this folder (sha256 `9b30b3f2…8d2`). Read `EPISODE_STATE.md` before any work; it holds the live status, decisions and next action.

## Scope and authority
- Applies only to work in `production/experiments/claude-illustrated-science/`. Root `AGENTS.md`, the Master Bible and `main` policy stay unchanged and keep governing the main channel. Never edit them from this experiment, never merge this file into `main` policy, never relabel earlier approvals as approvals of this experiment.
- Inside this folder the owner's explicit experiment instructions (19 Oct 2026) outrank conflicting older repository rules. Latest explicit owner instruction wins.
- No topic is selected. Do not write final narration, polished art or a film until the owner selects one. A recommendation is not a selection.

## Overrides of older repository rules (recorded conflicts)
| Older rule (main) | Experiment rule |
|---|---|
| Image led photographic layers; schematics must be printed paper figures, not freestanding vector scenes | Original Kurzgesagt *inspired* illustrated vector worlds are the primary picture. No photo collage, paper dominance or antique palette |
| Playfair Display 900 for all titles/keywords | Typography designed for this system; Manrope remains caption default unless owner approves a change. Playfair only inside the locked ending |
| Cold Metal material/optical finishing, grain, paper, jitter, ink bleed | Decide per episode; record use or NOT APPLICABLE with reason. Clean flat colour is valid |
| `production_standard: sun-disappeared-v1`, `visual_style: image-led`, `material_profile: image-led-v1` | Declare `illustrated-science-trial-v1` with its own visual/material profile. Never declare the Sun preset while bypassing its photographic validators |
| Navy/ivory/gold/coral identity palette carrying scenes | Palette assigned by scientific role per episode; brand ending colours untouched |
| Pilot queue (Mint, Onion Tears, Knuckle); black dwarf selected on the research branch | Main channel decisions only. Not this experiment's queue |
| Old mandatory native 4K MP4+WebM | Native 1080×1920/30 H.264 master (already main's default since 17 Oct) |

## Inherited rules that stay mandatory
- Delivery 1080×1920, 30fps, H.264 High yuv420p, 12 Mbps target / 16 max / 24 buffer, AAC 48 kHz stereo 320 kbps, faststart. No upscale, no WebM renamed to MP4.
- Scene, camera, material and optics evaluated at 12 states/s: `sceneTime = floor((frame/30 + 1e-8) * 12) / 12`. Captions and keyword overlays use the scheduled state. Audio is never quantized. Locked ending runs on real 30fps output time.
- A meaningful explanatory change about every 1.5 to 2 s (relationship, transformation, consequence, evidence, viewpoint, connected cut). Caption swaps, texture crawl, idle drift do not count. Longer holds need a timecoded reason. Keep a motion ledger.
- Natural narration timing: actual decoded Bernard speech drives picture. Gaps 0.12 to 0.55 s normal; unplanned >0.85 s flag, >1.20 s release fail. Never speed speech. Protect final word plus 0.8 to 1.8 s tail before the ending.
- Captions: short phrases centred in the 42 to 58% band, crisp, no glow/halo/blurred duplicate/soft shadow backdrop. Estimated timing labelled estimated.
- Sound: original evolving score; existing SFX catalogues first (`audio/curio_sfx_v1`, `audio/generated-editorial-v1`, `production/audio/README.md`); cue sheet; about −14 to −12 LUFS, ≤ −1 dBTP; listen to the encoded mix.
- Separate reviews, each tied to exact artifact/version/hash: (1) owner art and sequence review of ≥5 finished states incl. narration hidden check and hardest transition; (2) owner moving preflight of the hardest passage with final art, real voice, music, SFX, captions; (3) complete encoded film review against all 57 acceptance IDs. Never invent approvals or claim a film exists when only code exists.
- Research: claims ledger with primary source and location, evidence category, caveat, visual and confidence. Caveats survive into posts.
- GitHub is the persistent store. Freeze/hash source before capture; archive every completed MP4 (tests included) as its own Release immediately; verify a fresh download and SHA-256; mark `ENCODED_ARCHIVE_PENDING` if archiving fails. Never commit secrets, third party transcripts or reference frames.

## Engine method
Browser HTML/Canvas/SVG/JS. `renderFrame(frameIndex)` is pure: seeded randomness, no wall clock, fonts loaded before capture, seek equals sequential render. Player UI never appears in capture. Capture with Playwright Chromium in the cloud workspace, encode with FFmpeg. Working pattern proven in `qa/pipeline-test-20261019/`.
