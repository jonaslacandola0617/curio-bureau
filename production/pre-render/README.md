# Curio Bureau pre-render queue

## Default delivery — owner update, 17 October 2026

Native **1080 × 1920 at 30 fps** is now the standard final posting format. Use high-quality H.264 MP4 (12 Mbps target,16 Mbps peak ceiling) and AAC 48 kHz stereo 320 kbps.4K is optional when explicitly requested. Apply [the 1080p delivery standard](../engine/DELIVERY_1080P_STANDARD.md). Older mandatory 4K statements below are superseded for new production; historical exports remain unchanged. Keep all visual/audio/whole-film quality gates and immediate versioned GitHub archiving.


A pre-render project is a frozen, restorable production source that can reproduce its approved film without new creative decisions. A topic list, narration draft or storyboard is not render-ready.

This operational pilot implements the existing Bible v1.4.5, image-led direction, rendered-translation safeguard and GitHub archive policy. It does not replace them. **Owner authorized a five-project pilot on 16 October 2026; a 350-project production commitment has not been measured or established.**

Start with [the updated pilot review](pilot-20261016/README.md). Cold Metal is now owner accepted as a complete published-film benchmark. The remaining four pilots have revised complete-story plans; three are new-post candidates and Recorded Voice is calibration. Zero packages are newly claimed frozen RENDER_READY.

## Stages and review boundaries

| Stage | Work that actually exists | Exit evidence |
|---|---|---|
| STORY_SEQUENCE_DRAFT | Source/uncertainty ledger, three distinct hook approaches, draft narration, connected sequence states, asset requirements | Reviewed claim scope and chosen visual approach; no asset completion claim |
| ART_REVIEW | Acquired and cleared source images, masks/repairs, five demanding finished checkpoints, hardest passage initial/intermediate/resolved, heading-hidden comparison | Owner art/sequence decision tied to actual reviewed images and hashes |
| MOTION_REVIEW | Hardest moving passage, actual source-owned actions, sound-led hook, readable holds, active material/optics | Owner motion decision tied to reviewed video/source |
| FULL_PREVIEW_REVIEW | Whole film at review resolution (720p early,1080p final output inspection) with final complete Bernard speech, evolving score, audible action SFX, real aligned captions and locked ending | Full-film owner review plus phone/UI, listening/tail, facts/rights and technical evidence |
| RENDER_READY | Frozen source and dependencies, settings, checksums, evidence records, actual GitHub saved bytes, successful restoration rehearsal | Offline readiness validator passes; live GitHub archive verification remains a separate recorded action |
| DELIVERED | Actual native 1080p posting MP4, QA and permanent download receipts;4K/WebM/browser outputs when requested | Encoded artistic/audio/technical review; GitHub download-back hashes match; source/verified chunks recoverable |

Do not mark a stage complete by filling a checkbox or generating a contract. Automated checks inspect bytes and records; the owner supplies actual creative decisions. Existing approvals apply only to their identified artifacts. A changed shot, mix or preview needs the relevant review again.

## What freezes before 4K

1. **Evidence and story:** exact narration, factual sources, uncertainty boundaries, approved hook and shot contract. Research access limits remain visible until resolved.
2. **Picture:** actual licensed image bytes, effective resolution at the tightest crop, masks/hidden-region repairs, scene scripts, timings, annotations, layer anchors, local texture inputs, fonts, approved material/optics execution and exact London Bridge endcard. Every adapter-owned extra input is listed.
3. **Sound and captions:** untouched voice master, aligned words, pronunciation/gap/tail reports, original score and all SFX cues/stems, final mix, centered platform-safe captions. No implicit regeneration or percentage-only loudness approval.
4. **Reproduction environment:** source commit, engine and governance file hashes, dependency/tool versions (Python, Node, Playwright/browser, FFmpeg, fonts), exact build commands, preview and test evidence. Capture actual installed versions during production, not invented defaults. Browser/encoder upgrades trigger a smoke/review check; pixel or codec identity across toolchain changes is not assumed.
5. **Persistence:** small cleared source and reports in Git; large proprietary source/recovery/exports in GitHub Releases. Restricted source stays private. Restore the package into a separate clean working directory and verify its input hashes before declaring it ready. A manifest without the actual asset bytes is not a backup.

The freeze fingerprint includes the listed input bytes and settings. Keep decision evidence as immutable, hash-listed files; store their binding to the freeze in the manifest, outside those files, to avoid recursive hashes. Preserve original owner messages, reviewed asset hashes and scope. Never fabricate an owner approval or “refresh” one to cover unreviewed changes. Reconcile the final freeze to the actual approved artifacts before recording final gate bindings.

## Implementation and enforcement

`production/engine/pre_render.py` validates a `package.json`. Required input roles: story, research, sequence, source, asset, font, voice, mix, captions, finishing, ending, requirements and preview. Also list all review evidence files with role `proof`.

Each input has `path` relative to the manifest (absolute private restored paths are allowed locally), `role`, `sha256`, and `archive`. An asset also needs `rights_status: cleared` plus its source/license record in the rights evidence. This string does not itself establish rights.

Archive records:

- Git: `kind: git`, `commit` (40-character saved commit), exact pinned GitHub `url`, and `verified_at`. The offline validator checks the local Git object at that commit against the declared SHA-256. A separate real GitHub read-back must establish the receipt before it is recorded.
- Release: `kind: github-release`, actual download `url`, `size`, `sha256`, `verified_at`. Receipt values must come from successful actual byte upload and download-back, not projected paths. The offline validator matches the receipt to restored local bytes; it does not probe remote availability.

`gates` contains facts_rights, owner_art_sequence, owner_motion, owner_full_preview, phone_captions, audio_listening_tail, technical_preflight and restore_rehearsal. Each requires `status: approved`, `date`, `reviewer`, `evidence_path` pointing to a hash-listed file, and `fingerprint` matching the final freeze. The three owner gates require `reviewer: owner`. `unresolved_findings` must be empty. A record checker cannot authenticate who wrote a quote or certify artistry; its role is to stop omissions and accidental drift.

Pilot episode adapters must add an episode-relative `pre_render_manifest` to `episode.json`. Native rendering then calls this guard **before building or encoding**. A missing/unready package stops the render. Existing approved sources without that field retain their rebuild path; the guard is not a retroactive rewrite of historical episodes. The five registered pilot IDs are enforced in code: removing their binding also blocks native production. The current integration is opt-in for other new episodes, not a claim of universal engine enforcement.

```bash
python3 production/engine/pre_render.py production/pre-render/pilot-20261016/cold-metal-pilot/package.json --episode /path/to/episode --project /path/to/restored-project
python3 -m unittest discover -s production/engine/tools -p test_pre_render.py -v
```

The first command intentionally exits nonzero for today's drafts. Once all gates pass, use the existing `curio.py plan`, then `render`, then `package`. No second renderer was added. Existing whole-visual/audio caching remains: unchanged outputs reuse, audio-only changes remux where valid, visual/timing changes render again. There is no new per-shot render cache or unattended render farm in this pilot.

## Daily work, recovery and cost control

Keep five candidates in story research, **one** active finished-art passage, and **one** motion/full-preview item at a time during calibration. Do not build hundreds of moderate scripts and call them production inventory. Cold Metal now has owner complete-film acceptance. Finish its separate freeze/restore evidence; complete Mint, Onion Tears and the observational Knuckle film using full-preview gates. Recorded Voice remains a reuse/calibration candidate. Scale only from measured workflow.

For each project log research, source acquisition, design, revisions, voice/audio, animation, render and QA separately in [the metrics sheet](pilot-20261016/metrics.csv). Enter actual wall time, retries, tool/token usage when observable, asset generation counts and storage sizes. Do not estimate actual token usage from memory. Record missing telemetry as unknown.

Only then calculate sustainable daily capacity and schedule. Fifty fully developed pre-render packages per day is an unproven target; story ideas and finished productions have very different throughput. The bottleneck may be source rights, composition, owner review, audio or restoration rather than encoding. Hold back time-sensitive topics until close to publication and recheck evidence before posting.

On interruption, read queue + relevant project manifest/review + changed canonical files. Restore actual bytes, verify hashes, resume the next incomplete gate. Do not replay the entire conversation, reload unchanged manuals repeatedly, regenerate saved voice/SFX, or rerender to repair a download link. During native export preserve verified integer-frame chunks and GitHub byte receipts per NATIVE_RENDER_RECOVERY.md; resume missing/invalid ranges only. Chunk recovery does not guarantee automatic per-shot edit caching.
