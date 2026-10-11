# CURIO BUREAU — CREATIVE / MOTION / AUDIO SYSTEM AUDIT
**Audit date:** 11 October 2026  | **Version:** v1.0  | **Status:** evidence-based partial channel audit and actionable master bibles

**Purpose:** Establish one premium editorial identity across episodes while avoiding repeated layouts, low-detail drawings, narration gaps, misaligned captions and nominal-only 4K claims. This package contains the comparative study, working bibles, measurable QA and new episode master prompt. It **does not claim all seven original release files were found or fully watched**.


**Evidence labels:** **V** = sampled actual video frames/contact sheets; **A** = isolated narration WAV or exported audio measurement; **S** = available project source/QA files; **W** = externally retrieved written/video metadata. 'Not verified' always beats guessing. The contact sheets show sampled compositions; they cannot independently prove animation curves, full-film pacing, sound quality, or true audience retention. As of 2026-10-11, no channel analytics or exact named masters of 001–003 have been verified. A separate Samoa pilot and rebuilt WebM have been recovered and identified visually.

**Local evidence files in review bundle:** `evidence/EP001_PILOT_SAMPLED_CONTACT.jpg`, `evidence/EP001_REBUILT_SAMPLED_CONTACT.jpg`, `evidence/EP004_ACTUAL_RENDER_CONTACT.jpg`, `evidence/EP005_ACTUAL_RENDER_CONTACT.jpg`, `evidence/EP006_ACTUAL_RENDER_CONTACT.jpg`, `evidence/EP007_ACTUAL_RENDER_CONTACT.jpg`, `evidence/audio_gap_measurements.json`. The 004–007 sheets came from earlier actual encoded-film frame QA and additional extracted frames.


## Available films and exact status
| Episode | Video evidence | Scope | Status |
|---|---|---|---|
| 001 Samoa | `Curio_Bureau_The_Day_That_Disappeared_Pilot.mp4` (51s, 1080×1920) and `...REBUILT.webm` (~52.4s) recovered from Library | Timed frame samples; neither is the exactly named baseline master | PARTIAL / VERSION MISMATCH |
| 002 Centralia | Exact editorial MP4 not located | Earlier prompt describes it; do not assign observed scores | MISSING MASTER |
| 003 Niagara 1969 | Exact editorial MP4 not located | Earlier prompt describes it; do not assign observed scores | MISSING MASTER |
| 004 Lake Peigneur | `CURIO_BUREAU_004_4K_NATURAL_VOICE_REVISION.mp4` and design/project files | 4K metadata, frames, source, original 75s narration stem | DIRECT PARTIAL |
| 005 Boston Molasses Flood | `CURIO_BUREAU_EP005_4K_CAPTIONED_REVIEW.mp4` plus project documents | 4K metadata, frames, original scene-duration logs | DIRECT PARTIAL |
| 006 Dagen H | `CURIO_BUREAU_EP006_NATIVE4K_H264_REVIEW.mp4` and source ZIP | 4K metadata, frames, 77.9s voice stem, source | DIRECT PARTIAL |
| 007 Chicago building elevation | `CURIO_BUREAU_EP007_4K_MP4_REVIEW.mp4`, source ZIP | 4K metadata, frames, 77.3s voice stem, source | DIRECT PARTIAL |

## What the audit actually did
1. Verified MP4/WebM video size, duration, codecs, FPS and audio-stream metadata with ffprobe.
2. Reviewed multiple timed extracts and previously saved contact sheets from the real encoded exports, plus source-code design details.
3. Located a **previously unavailable Samoa pilot and rebuild** in the Library and sampled both, preventing a false '001 missing entirely' conclusion.
4. Measured >0.85s isolated-voice silence intervals with FFmpeg at −37 dBFS: **Episode 004 seven intervals** (3.04–5.37s); 006 and 007 **zero detected**. This is detector-dependent and not a claim of perfect speech performance.
5. Reviewed available 005 scene timing data corroborating long empty narration windows; checked use of fonts against actual project code when possible.
6. Researched verified external Vox/editorial and short-form benchmark references, but **did not decode or conduct frame-by-frame observation of those external videos**. Creative techniques are tied to producer interviews, descriptions, transcript excerpts and source metadata; no fabricated timestamps.

## Findings that matter most
- **P0:** Stop title-card-led and static openings; storyboard three frame-1 alternatives and compare on a phone at mute.
- **P0:** One final voice timeline is the source of truth; automatically fail >0.85s unexplained speech gaps and any >1.2s between passages.
- **P0:** No captions below the app UI: nominal center 42–58% picture height with real interface-mask tests.
- **P0:** Don't call any final export 4K without verifying **MP4 and WebM separately** and auditing visual asset resolution.
- **P1:** Solve the *asset complexity collapse* (detailed 007 photo-style art vs blocky midsection; repeated 006 buildings and vehicles) at concept/style-frame gate, BEFORE full render.
- **P1:** Replace template editing with a shot taxonomy, subject-owned hero mechanism, match cut logic and cross-episode repetition ledger.
- **P1:** Replace inaudible/simple pad scoring with composed music and provenance-checked Foley; listen critically on phone and headphones.

**Recommended reading order:** `01_COMPLETE_VIDEO_AUDIT` → `02_EPISODE_COMPARISON_MATRIX.xlsx` → `03_VISUAL_INCONSISTENCY_REPORT` → `06_VISUAL_IDENTITY_BIBLE` → `07_MOTION_ANIMATION_BIBLE` → `12_ANTI_REPETITION_SYSTEM` → `13_MASTER_PRODUCTION_BIBLE`. Operational teams can jump to `10_PRODUCTION_WORKFLOW_V2` and `11_QA_RELEASE_CHECKLIST`.

**Honesty clause:** These files are a substantive first evidence-grounded design system. A certified seven-release-media audit and clip-specific benchmark timing requires recovery of 001–003 named masters, uninterrupted viewing of each final film, externally playable reference footage and first-party TikTok/YouTube Studio retention data.

## Completed consolidated handoff
`13_CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md` is now a full self-contained set of governing rules plus verbatim detailed implementation modules 06–12. The original concise executive rulebook is retained as `13A_MASTER_BIBLE_EXECUTIVE_RULES.md`. The `02` workbook contains six tabs including scoring standards, evidence status and the editable shot fingerprint template.

## Start here for the NEXT episode
1. Read `13_CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md`.
2. Fill in `14_CURIO_BUREAU_FUTURE_EPISODE_MASTER_PROMPT.txt`.
3. Copy `SHOT_FINGERPRINT_BLANK.csv` into the project as the camera/shot originality ledger.
4. Run `tools/curio_video_qa.py` on MP4/WebM plus isolated narration, then perform the manual creative review.