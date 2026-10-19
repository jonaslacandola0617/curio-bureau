# EPISODE_STATE: illustrated science trial

Updated 2026-10-19 (Asia/Manila). Branch `experiment/claude-illustrated-workflow-20261019`, based on main `791c871`.

## Status
- Stage: 1, topic decision. **No topic selected.** No narration, artwork, score or film exists for this experiment.
- Approvals for this experiment: none. Earlier Sun / Cold Metal / Pig War approvals do not transfer.
- Local workspace `D:\channel-animation` holds the prompt (byte identical to `CLAUDE_PRODUCTION_PROMPT.md`, sha256 `9b30b3f25a1356943a87f8dfbd409a090378d7b87ee8826f43b59109cb42d8da`) plus copies of this file and `CLAUDE.md`. GitHub branch is the source of truth.

## Verified capabilities (tested 2026-10-19)
| Capability | Result |
|---|---|
| Deterministic frame capture | PASS. Playwright 1.56 + Chromium 1194 in cloud workspace. 60 frames at 1080×1920 gave exactly 24 scene states (3/2 hold pattern); 60 shuffled seeks matched sequential renders byte for byte; bundled font loaded before capture. `qa/pipeline-test-20261019/` |
| FFmpeg encode/decode | PASS. Cloud ffmpeg 6.1.1: H.264 High, yuv420p, 30/1, 60 frames, AAC LC 48 kHz stereo 320k, faststart, full decode clean |
| Audio processing | PASS (technical). loudnorm + ebur128 true peak: test mix measured −13.0 LUFS. numpy/scipy present; `soundfile` and `sox` missing (pip/apt installable). Listening quality not tested |
| GitHub commit/push | PASS. Repo public, session has admin/push |
| GitHub Release upload | See receipt below |
| Browser preview | Built in browser pane reachable on owner's PC, but it cannot open files or localhost from the cloud workspace. Review previews go through hosted Artifact pages or GitHub; Playwright screenshots for frame review |
| Owner PC shell | Linux VM on Windows: node 22, ffmpeg 4.4, python 3.10, git; **no Chromium, no gh**, 2 CPU / 2.8 GB. Use only for file handoff, not capture |
| Narration (Bernard) | Voice ID `QMJTqaMXmGnG8TCm8WQG` (eleven_v3; earlier takes generated via Runway) resolves in the connected ElevenLabs workspace, listed as library voice "Clyde, Vintage Male Radio Announcer". No generation attempted (spends credits). Runway is not connected |
| Word alignment | ElevenLabs transcription is available for timestamps; accuracy untested |
| Long unattended renders | Cloud container is ephemeral; GitHub Actions workflows exist in repo but none for this preset |

## Available assets
- Locked ending: `production/engine/browser/brand.js` `london-bridge-v1` (sha256 `fad97f68e9a2333830e31479d6c86d7585641cde5101c6660ee9a5d7d5c44df8` at main `791c871`; not listed in `requirements.lock.json`). Needs Playfair Display 900 + Manrope 700.
- Fonts in repo: Manrope.ttf, Manrope800.ttf, PlayfairDisplay.ttf, Playfair900.ttf (`production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/assets/`). Licence record to be pinned for this preset.
- SFX: 50 cue original pack `audio/curio_sfx_v1` (48k/24bit FLAC, synthesized); `audio/generated-editorial-v1`; `production/audio/` inventory incl. restricted Drive items (do not copy into public repo).
- Shared engine (`production/engine/`): image led renderer, Sun preset validator. Reusable ideas, not this preset.
- Narrative study: nine caption findings on `research/kurzgesagt-topics-20261018` (`7a2768f`); caption files private, off repo.

## Unresolved dependencies
1. **Bernard path:** owner must confirm that ElevenLabs generation with voice ID `QMJTqaMXmGnG8TCm8WQG` and eleven_v3 is the approved Bernard (prior takes came via Runway), or supply Runway access. Until then, timing is provisional.
2. **Preset validator:** `production_standard.py` rejects any preset other than `sun-disappeared-v1`. Needs a branch-local `illustrated-science-trial-v1` declaration/validator before any episode config. Not built yet.
3. **Ending verification:** confirm `brand.js` above is the owner-approved exact ending (no lock entry exists).
4. **Font licences** for the new typography system (Manrope/Playfair are OFL; any new face needs owner approval).
5. **Reference study R.1/R.2** (frame by frame picture and sound study of Kurzgesagt) remains OPEN.
6. `soundfile`/`sox` install when audio work starts. Release download verification for public assets on each archive.
7. Kurzgesagt public process page could not be fetched this session (permission request timed out).

## Visual reference review
**Supplied references found:** none visual. The local folder contains only the prompt; the Claude Project has no documents; the repo contains no Kurzgesagt frames or clips. The only in repo images are Cold Metal art frames in the superseded photographic style, which are not references for this experiment.

**Observed (evidence actually examined):**
- Nine original caption exports were studied on 18 Oct (text only): narrative pattern = violated assumption, minimum mechanism, escalation through the same mechanism, a second reveal that changes the category, uncertainty restored, earned landing. No picture, motion, typography or sound was observed.
- Kurzgesagt's public process description (visual metaphor sketches, vector and pixel illustration, infographics, classic flat 2D with occasional 3D, voice led timing, specially composed music) is carried forward from the export; it was not re-read today.

**Proposed implementation (ours, not observed):** purpose built multi part vector assets with internal structure; consistent scientific colour roles; expressive characters only as teaching devices; explanation through assembly, cross section, transformation, tracking and scale change with an invariant held across transitions; anticipation/arrival/hold motion grammar at 12 states/s; flat colour with selective depth; typography and sound families chosen per episode. None of this claims to match Kurzgesagt's actual rigs, curves, layouts or mixes.

## Topic candidates (proposals, not selections)
1. **The reactor that breathed** (Oklo, Gabon): 2 billion year old natural fission reactors pulsed about 30 min on, about 2.5 h off, because their own heat boiled away the water that made the chain reaction possible. Sources: Meshik et al. 2004 PRL 93:182302; Shlyakhter (U-235 ≈3% then vs 0.72% now). Caveat: cannot happen in natural ore today.
2. **Mirror life:** a mirror image bacterium might be invisible to immune systems and predators because recognition depends on molecular handedness. Sources: Adamala et al. 2024 Science 10.1126/science.ads9158 and technical report. Caveat: no mirror organism exists; risk is expert assessment, not experiment; at least a decade (report: 10 to 30 years) away; dissent on where red lines fall.
3. **The day the Sun held still** (Precambrian 19.5 h day): a solar atmospheric tide resonance may have balanced the Moon's braking for about a billion years. Sources: Wu et al. 2023 Sci Adv 10.1126/sciadv.add2499; Mitchell & Kirscher 2023 Nat Geosci. Caveat: contested; Farhat et al. 2024 A&A 684:A49 finds the torque insufficient.
Recommendation given in chat: Oklo. **Awaiting owner selection.**

## Next action
Owner selects a topic (or rejects all three). Then: claims ledger, script draft, Bernard path decision, preset validator. No production before selection.

## Pipeline test archive
Pending (filled after Release upload).
