# 10 — CURIO BUREAU PRODUCTION WORKFLOW V2
**Primary operational change:** decisions are approved before high-cost full 4K renders; final *voice* is the master timeline, while every visual beat receives a chosen composition and validated asset-quality target.

## New project structure
```
curio/episodes/008_slug/
  00_brief/{story_angle,claim_lock,research_sources,rights}.md
  01_hooks/{A,B,C}/(first_frame.png,hook_animatic.mp4,hook_eval.md)
  02_script/{narration.md,voice_final.wav,words.json,gaps.json}
  03_design/{palette.json,fonts.lock,style_frames/,shot_fingerprint.csv}
  04_assets/{archive/illustrations/maps/masks/LICENSES.csv}
  05_animation/{studio/,scene_manifest.json,render_tests/}
  06_audio/{voice/music/ambience/foley/effects/mix.wav,cue_sheet.csv}
  07_captions/{aligned_words.json,final.srt,ui_mask_previews/}
  08_render/{frames_4k_png/,master_4k.mp4,master_4k.webm}
  09_qa/{technical.json,art_review.md,sound_listen.md,source_audit.md,contact_sheets/}
```
Each scene manifest entry: `id, word_start, word_end, story_claim, source_ids, shot_family, hero_asset_ids, camera, layer_depths, state_changes, source_footnote, caption_free_region, SFX_ids, transition_type, QA_status`. Master audio word starts/ends are final timing authority.

## Stage 0 — Evidence retrieval and reality check
Locate all previous art references and per-episode source materials. No fabricated access. Inventories distinguish `verified local`, `library unmounted`, `external linked`, `not available`. Audit any reused SFX licenses before copying.

## Stage 1 — Historical research lock (P0 gate)
Every factual statement: source link, exact supporting phrase, event date, publication date, conflict/uncertainty, original image-rights status. If claim contested, script uses 'historians estimate' or it is removed. No spectacular animation contradicts event mechanics. Deliver claim_lock.csv/research.md. **Gate:** independent source check for numbers, human cost, geography, quoted lines.

## Stage 2 — Hook board and first-frame proof (P0/P1 gate)
Write 3 materially different hooks. Draw 3 actual phone-scale FIRST FRAME images and animate 0–5s versions with scratch voice. Evaluator must identify the anomalous physical action by ~1s and topic by ~3s. Decide angle before script. **Gate:** no blank logo, unrecognizable action or illegible center.

## Stage 3 — Narration recording FIRST (P0 gate)
Approve 65–85s human-paced script where actual duration is story-dependent. Record voice via approved narrator and save isolated WAV. Trim genuine leading/trailing quiet. Report all per-clip starts/ends, gaps, intra-clip silence, tail and pronunciation. If any >0.85s unintended pause or >1.2s hard-release gap, **ripple-edit**, rerecord or rewrite NOW. Do not fill scene slots with silence. Obtain verified word boundaries via forced alignment/manual test. **Gate:** voice + SRT approved.

## Stage 4 — Shot choreography and asset scope (P1 gate)
Create detailed beat sheet and 12–25 major shot descriptions, EACH with own composition family, physical system, camera, asset list, annotation and sound trigger. Print a shot family strip. No >2 consecutive same framing family unless progressive mechanism demonstrably changes. Lock subject-owned hero motion and minimum asset complexity. **Gate:** five style frames (opening, first abstract explanation, first real historic environment, most difficult mechanism, final insight) meet one art standard.

## Stage 5 — Low-cost animation animatic (P1 gate)
At 540×960/1080×1920 previews, sync actual narration, rough music/SFX. Every 2–3s there must be meaningfully new information or a consciously paced factual absorption beat. Review complete 0–5s, all act joins, largest graphic changes, muted phone test. **Gate:** editor/art director approve whole 75s storyline BEFORE 4K.

## Stage 6 — Asset building and evidentiary rights
Draw objects to exact hero quality: five major depth planes, recognizable architecture/machinery, source-aware geometry, original textures, max native raster res demands. Match palette and typography lock. Maintain source table per photo/sound; if license uncertain, swap to labeled original graphic. **Gate:** weakest 20% of shots are still credible as finished editorial illustrations.

## Stage 7 — Motion & camera engineering
Use deterministic `render(t)`, scene manifest state and single audio timeline. Separate camera, physical event, labels, safe captions and SFX triggers. Add instrumented snapshot mode `render(scene, t, debug=true)` and frame overlays showing boxes/shot families. Test full source on mobile preview and random-scrub consistency. **Gate:** no glitch/dynamic discontinuity; no unexpected static holds; no same asset repeating as entire environment.

## Stage 8 — Professional audio and subtitles (P0/P1 gate)
Compose/clear music with real development; use recorded/provenance tracked Foley where appropriate; VOICE/MUSIC/AMB/DETAIL/IMPACT stems; critical listening on headphones AND phone. Re-run measured voice gaps; align captions to approved final audio; check TikTok/Shorts overlays. Music should be audible *as music*, not just as spectrum energy. **Gate:** listeners pass intelligibility and specificity.

## Stage 9 — PRE-4K QC (mandatory cost saver)
Render 1080×1920 30fps proof with **final** music/voice/captions. Review entire video, scene joins, headings, 3 shot-family strips, intro/outro and source citations. Any P0 or P1 flaw sends film BACK to edit. Never begin 2,300-frame 4K encode without reviewer signoff.

## Stage 10 — Real native 4K render
Source HTML/SVG/Canvas renders lossless native 2160×3840 PNGs at exact frame N/30s. Do not resize 1080p video to 4K. Mix stereo 48kHz/24bit WAV; H.264 MP4 CRF~15 AAC ~320k + VP9/Opus WebM. Preserve exact typography and center captions in both.

## Stage 11 — Encoded-film QA (P0)
ffprobe verifies both output streams independently. Decode first/last, random midpoints, transitions and 100%-size pixel crops. Verify duration, FPS, no missing frames/truncation, fonts, source-asset effective resolution, visually readable captions with real UI masks, -14 to -12 LUFS and true-peak ≤-1 dBTP, no voice gaps, no buried SFX, montage rhythm, all claim citations. **Gate:** QA PASSED only when both technical and subjective creative criteria are green.

## Stage 12 — Publish learning loop
Save final promo/thumbnail, performance analytics at day 1/7/30, hypothesis vs observed retention, shot fingerprint and creative retrospective. Record which hook/visual explanation genuinely worked. Update Bible via changelog and version bump; don't silently overwrite inherited standards.

## Expensive mistake prevention
The previous production habit rendered 4K before correcting primitive artwork and caption issues. V2 requires **three explicit approvals** before final encode: (a) full storyboard asset quality, (b) full 1080p animatic playback with correct speech gaps, and (c) mobile caption/UI test. Rendering success cannot upgrade 'QA FAILED' to 'FINAL'.