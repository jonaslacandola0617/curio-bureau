# Curio Bureau 001 — Samoa V2 Director's Cut — QA Report

**Status:** RENDER CANDIDATE — automated technical checks PASSED, editorial still subject to the creator's final listening and approval. No claim of a human auditory audition.

## Exact rendered build

- Master build: https://github.com/jonaslacandola0617/curio-bureau/actions/runs/38018553197
- Master source commit: `2b560f91de76165e26de4c5cce6a638af178d2e0`
- Artifact: `curio-bureau-samoa-v2-qa`, ID `11656814556`, expires 2026-11-24.
- Film length: 64 seconds; 1920 native frames at 1080 x 1920 / 30fps.
- Source: `films/samoa-2011/vox/` and scripts under `scripts/`.
- Complete voice, music, 43 timed SFX cues using 10 sounds from the user's Google Drive, 46 phrases of word-aligned burnt captions and external SRT.
- High-quality MP4 H264 CRF16 with AAC 48kHz stereo (measured duration and codec in `master-probe.json`), separate narrated WebM and self-contained HTML.
- Soundtrack analyzer measured approx **-14.0 LUFS integrated**, **-1.3 dBFS true peak**, LRA about 1.7 LU.

## Actual pixels reviewed

Real master-generated frame screenshots and contact sheet committed under `films/samoa-2011/review/sha-2b560f91de76/`.

- First frame: Playfair title is immediately legible; print calendar partially visible and develops over following frames.
- Business scene t=26 and t=30: weekday offsets between Samoa and Australia/NZ visibly differ; note explicit workweek overlap.
- Geo scene t=20: Natural Earth projected land outlines, an annotated Samoa point, and schematic International Date Line (as marked).
- Statute scene t=54: actual Act No.6 of 2011 named, Sec 8 visibly referenced, a clearly marked editorial paraphrase replaces generic filler lines.
- Conclusion at t=60 and final 63.96: key Playfair sentence and masthead completely inside frame with protected subtitle lane.

Visual contact sheets and native 37-frame audit passed; the script also performs measured-title overflow checks. Screenshots do not prove every interpolated frame is artistically flawless.

## Subtitle check

- The TTS generated 145 real WordBoundary events across 145 script tokens, resynced to the eight narration windows.
- The 46 SRT phrases now restore original punctuation and split at real sentence boundaries.
- Verified concluding `nature.` / `They're agreements.` / `And Samoa decided to rewrite` instead of erroneous `nature They're` caption.
- Captions burned into both outputs, Manrope loaded and tested in Chromium.

## Limitations / open QA

- Final **critical listening** to the user's actual music/SFX balance has NOT been performed by a human. Technical loudness and signal stream checks passed, but listening is still required to confirm the subjective mix.
- The soundtrack is a composed procedural documentary score rather than a commercial licensed music track.
- Maps are explanatory and not intended for legal surveying; date-line depiction is schematic.
- The public release `samoa-vox-001` is obsolete. A new `samoa-vox-002` GitHub Release was attempted twice and rejected **HTTP 403 Resource not accessible by integration** despite Actions having `contents:write`. The accepted V2 bundle is available in the run artifact and all source is committed here.

## Access

Open https://github.com/jonaslacandola0617/curio-bureau/actions/runs/38018553197 and download the **curio-bureau-samoa-v2-qa** artifact under Artifacts. It contains MP4, WebM, HTML, SRT, screenshots, frame-review.jpg, and technical reports.

The V2 artifact is stored for 45 days under the repository's GitHub Actions retention policy.
