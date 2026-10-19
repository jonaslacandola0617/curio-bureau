# Pre-render infrastructure review — 19 October 2026

Decision: **HOLD FULL RENDER.** The finishing stack executes, but the implementation and enforcement are not complete. This audit does not approve motion, replace the Sun standard, or change the existing movie.

Authority: `production/approved-benchmarks/SUN_DISAPPEARED_PRODUCTION_STANDARD.md`, `production/engine/FINISHING_OUTPUT_CONTRACT.md`, `production/engine/FINISHING_CHECKLIST.md`, `production/engine/SUN_STANDARD_INTEGRATION.md`, and the full 57-item Sun release checklist. Reviewer: Codex, native code/runtime audit plus sampled encoded contact-sheet inspection; no continuous playback or independent listening claimed.

## Bound version

Current topic: **The Dead Star That Could Still Explode**, black-dwarf supernova. The nine saved caption references and historical pilot queue are not current episode commissions. Owner-adopted Sun craft remains governing.

- Capture source: `57faec9f882f1da03ba9c7b92cb68b7250c36e98`.
- Renderer SHA-256: `4e2049d887b4e87a71f7b04d9634b43b22a593622b4c3092c8c6b712181816b3`.
- Existing 26.033333s MP4: SHA-256 `e5acf887af2fb52634953c1143537ef9cee61960af64065cd9a5c29ba623d251`.
- All 18 frozen input hashes matched. No creative source, original audio, existing QA receipt, movie, Release or READY trigger was modified.

## Actual execution and remaining coverage

`audit.cjs` loads the frozen renderer in isolated VMs and removes one treatment at a time in memory. Native 1080×1920 still diagnostics only; no movie was produced. `NATIVE_EFFECT_AUDIT.json` records all pixel differences, zero opaque-caption differences and the hunt/blur settling envelope. These are execution findings, not aesthetic passes.

| Requirement | Finding | Status before next capture |
|---|---|---|
| Distinct paper, print and remnant materials/overlays | Paper/field fiber and speckle plus source-local remnant striations independently change pixels at 8s. Existing encoded contact sheet shows tactile paper/field treatment. Original procedural textures; recovered owner texture bitmaps are not loaded. | Execution proven; per-material native/phone close-ups still needed for stronger coverage. |
| Moving grain | Independently active; existing frozen-picture phone test measures temporal change 0.715 mean red levels. | Execution proven; retain final encoded review. |
| Transition/compound blur | Handoff blur independently active at 9.6667s. Gaussian transient reaches 4.863px at the sampled peak and rounds to 0.000px by 10.1667s. | Execution proven; normal-speed aesthetic review pending. |
| Focus hunt | Independently active at 9.6667s, sampled radius 1.696px; rounds to 0.000px by 10.1667s. | Execution proven; not a persistent defocus. |
| Selective source focus and shading | Both independently active; common center/scale, but blur mask feather .65–1.6 differs from shading .75–1.7. | REVISE: use one shared spatial field and prove selected/peripheral behavior. |
| Chromatic separation | Independent image-only ±.45px offsets affect pixels; captions untouched. | Execution proven. |
| Mechanical jitter and exposure | Independent .28px jitter and .014 exposure treatments affect pixels; captions untouched. | Execution proven. |
| Local ink bleed | Current lines are clean strokes. The finishing contract's “local rough ink” description overstates what is implemented. | REVISE: implement source-local ink spread for appropriate printed marks, with isolated evidence. No text halo or scientific value distortion. |
| Contour edge boil | A .55px marker translation is active, but is not a roughened/boiling contour. | REVISE: implement restrained source-attached contour variation, or a specific approved material-based exclusion. Translation alone cannot pass. |
| Clean overlays and protected captions | Labels/graphics/captions draw after image optics; every new isolated check yields zero opaque-caption difference. No shadow/glow/text-blur helper present. | Execution proven; final platform-mask and phone inspection pending. |
| Whole-scene 12fps / 30fps delivery | Quantized scene time includes optics, materials, keywords and captions; existing cadence evidence has no errors. Real-time audio retained. | Proven for the current excerpt; test full duration when built. |
| Meaningful operations, independent depth and camera | Existing timecoded mechanism ledger and subject transformation are present. The excerpt is not proof of full-film independent foreground/subject/background parallax or purposeful camera coverage. | Full-film shot/operation review still required; no blanket motion pass. |
| Exact London Bridge ending | Intentionally absent from the excerpt. | NOT APPLICABLE to excerpt; mandatory exact 30fps protected-ending proof for complete film. |
| Bernard, evolving score, action SFX, speech tail | Original Bernard master retained; 17 catalogued cues, three score sections and separate stems archived. Encoded levels measured. | Listening, exact word boundaries and complete-film ending remain independent open checks. |
| Source freeze and immediate archiving | Input hash loop, closed lossless chunks uploaded every two, immediate movie upload and fresh public-download verification exist. | Current version preserved. Expand next fingerprint to include workflow, validation dependencies, standards/ledger and all consumed cue inputs. |
| Shared validator enforcement | Custom `build_release.py` runs its local QA, but does not invoke `production_standard.validate_standard`, `finishing_audit.check` or `validate_finishing`. Existing generic release finishing check assumes an ending case after 30s, so cannot honestly certify this isolated excerpt. | REVISE: wire scope-aware pre-capture gates into the next build. Preserve mandatory full-film ending validation; do not fake an ending pass. |
| Shot-specific coverage manifest | No `FINISHING_COVERAGE.json` exists for motion-v1. Aggregate QA alone misses individual-effect omissions. | REVISE: hash-bound per-effect manifest, fresh individual proof and explicit exclusions required before capture. |
| Full 57-item acceptance and reference study | No complete film exists yet. Detailed direct Kurzgesagt AV study remains incomplete. | Keep open; caption exports, technical proof and art approval cannot complete these. |

## Required next implementation order

1. Preserve v1. Make a separately versioned source revision for the missing ink/contour treatments and unified focus field, with subject-specific coverage and proof. Do not add plastic sheen or other inappropriate materials just to tick a box.
2. Add mandatory pre-capture calls to the shared production-standard and finishing-coverage validators, with honest excerpt/full-film scope handling, fresh source/evidence hashes and fail-closed behavior. The complete-film path must require its actual exact ending and full duration ledger.
3. Inspect independently isolated native/phone diagnostic states and actual prior motion feedback. Freeze corrected source before any new moving capture; archive new expensive chunks and movies under new version identities.
4. Full-film integration remains gated by owner moving approval and complete-film creative/audio/caption/release checks. This infrastructure audit is not that approval.

No new render was started. The correct finding is **implemented in part, verified more precisely, corrections required**.
