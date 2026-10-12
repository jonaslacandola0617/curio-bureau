# CURIO BUREAU — BRAND, WORKFLOW, FILM RELEASE, AND CREATIVE GATES
**Status:** transfer synopsis of the adopted `main` Bible **v1.4**, which binds the refined Ghost Army-derived editorial art/motion directing principles, and repository `AGENTS.md`. Where there is any mismatch, read the COMPLETE canonical Bible and current user direction; this synopsis does not supersede them.

## 1. Channel identity and audience promise
**Name:** CURIO BUREAU. **Tagline:** *Stories, systems, and surprises.* Derived from rebranding prior 404 Files tech-internet-lore channel; fresh broad short educational documentary identity.
**Editorial subject focus:** extraordinary but sourced historical/engineering events, everyday systems with surprising design/incentive consequences, forgotten technology, real mysteries and events. Fascinating, accessible and fact-grounded, not manufactured conspiracy. Educational but emotionally cinematic. Viral potential via high-stakes question, paradox or curiosity gap, not clickbait fraud.
**Format:** vertical phone-first narrated Shorts/TikTok with premium purposeful 2D/2.5D motion, mixed archival documentary visuals, confident storyteller voice and source honesty. Every episode must be original in topic-specific composition and visual reasoning; avoid six consecutive near-identical shots.

## 2. Fixed brand
| Element | Authoritative choice | Execution notes |
|---|---|---|
| Primary brand | Midnight navy `#0D1C2B` | Ink, story structure, often caption box |
| Primary light | Ivory `#F5F0E7` | Page/negative space, not forced beige filter over all imagery |
| Accent | Gold `#C8A26B` | Editorial selection, clear strokes, fine caption edge |
| Secondary accent | Coral `#D57864` | Contrast/emphasis, meaning must be stable |
| Display serif | **Playfair Display** | Big editorial titles, high-impact dates and short framing phrases |
| UI / info / captions | **Manrope** | Center captions, maps, units, small evidence labels and interface text |
| Motto | **Stories, systems, and surprises.** | Use with discretion; don't fill every frame with unnecessary channel furniture |
| Brand focus | Comprehension + tactile design | Historical materials retain fitting other color tones and source fonts |

Do not infer effective fonts from CSS declarations alone. Verify actual font loads and rendered glyphs. Do not ship third-party proprietary font binaries as part of handoff or final user deliverables.

### Layout/titles
Vertical 9:16. Source-native headlines/quotes remain readable when shown as evidence. Typography has jobs—identity, explanation, emphasis, source—not one bouncing title style. Source labels and annotations remain perceptually anchored to corresponding visual objects. Avoid repeat “FIELD NOTES / 01” frames or an oversized Playfair headline on EVERY scene.

### Caption discipline
All burned subtitles in BOTH true release exports **normally in vertical center-safe band 42–58%** of total height, horizontally centered, and composed around subject/phone UI. Curio known accepted style based on Episode 008: **one single rounded semi-transparent midnight/navy rectangle**, subtle warm-gold border, well-measured short wrapped Manrope phrases; NOT multiple separate full-width flat bars. The Episode 009 feedback made this explicit. Keep hero faces, critical diagrams, labels and evidence away from caption zone; test TikTok/Shorts overlays on real encoded frames.
Word/phrase boundaries must align to actual verified narration. Estimate-only captions cannot be called aligned and are not final; produce SRT when needed.

## 3. Story design
- One hook question or surprising visual from frame zero; establish stakes and inquiry quickly, not generic voice introduction.
- Research sources before story: prefer museum/archive/institution/primary source, label contested details and approximate figures. For historical content separate established facts, disputed claims, illustrative recreations and artistic metaphor.
- Build progression: initial viewer mental model → unexpected challenge → grounded source object/event → explanatory mechanism → consequences/scale → emotionally clear insight. Not every episode must use this exact sequence.
- Draft a factual claim-to-source ledger before maps/data; no invented document passages or masquerading stock illustrations as archival evidence.
- Visual storyboard for all difficult propositions: chosen representation, initial/middle/resolved state, invariant, eye path, meaningful motion, next-shot inherited relationship. Compare at least two representations for major abstract claims and reject decorative ones.
- Art and editing must not compete. The highest-craft source imagery should be visible at beginning AND through weakest difficult middle shot and final context, or intentionally replaced by professionally designed clear abstraction where reasoned.
- Avoid overly long isolated cards, constant zooming, repetitive sky/flood/street/diagram pan motifs or switch-like identical transitions. Evaluate sliding six-shot fingerprints.

## 4. Actual delivery workflow
**Repository:** `https://github.com/jonaslacandola0617/curio-bureau`. `main` = stable adopted docs/approved infrastructure, episode `film/<slug>` branches, review experiments on separate `design/<name>` or analogous branch. Do NOT change/force-push main or adopted Bible without explicit user approval. Meaningful milestones committed. GitHub Actions handles repeatable browser render and media QA; upload resulting MP4/WebM to artifacts/releases rather than committing large binaries to main.
**Authoring:** original editable HTML/Canvas/SVG/JavaScript animation, absolute deterministic time per frame (`renderFrame(frame)` / `renderAt(t)`), appropriate Web Audio/MediaRecorder, play/pause/scrub/replay and preferably built-in **full-length, synchronized WebM export**. Scene graph local+camera+screen coordinate systems; semantic masks; camera/occluder depth; attach annotation to parent object; no indiscriminate transition preset.
**Review stages (for actual authorized episode):** source lock → script/voice emotion map → **editorial shot-to-shot relationships, invariants, transitions and intermediate states BEFORE final images** → alternative hook/voice auditions → purpose-built component/layer assets → 5 difficult first/middle/end styleframes → audio scene cue map → animated hardest-motion preflight → offline frame renders actual native output → narration captions and sound mastering → objective QA and subjective playthrough. Approved visual treatment isn't necessarily the same as an executable render.
**Don't build another Ghost Army video from this handoff alone**: the current user specifically requested export; next agent should await explicit production request.

### Native final masters (STRICT)
| Field | Required |
|---|---|
| Picture | **2160×3840 actual native-detail** vertical 9:16, **30fps**, not resized 1080p |
| MP4 | Independently encoded **H.264** video / **48 kHz AAC** audio (yuv420p typical) |
| WebM | Independently encoded **VP9** video / **48 kHz Opus** audio |
| Audio | Expressive narration + audible score + synchronized purposeful SFX/ambience, coherent buses |
| Captions | Manrope, center-safe, burned in both files, word/phrase checked, SRT |
| UI | Browser-openable source with usable playback/scrub/preview and WebM export where applicable |
| QA | `ffprobe`/actual decode verification, real distinct frames, phone-scale and platform-overlay inspection, encoded audio loudness/listening, duration/sync, rights/source list |
| Status | Never label FINISHED/FINAL if only code committed, render queued, format simulated, voice missing or artist review failed |

A 16s 1080×1920/24fps Ghost Army concept test is **not** a final Curio episode; V4 had synthetic effects but no VO or full score.

### Voice/expressive audio
User values richer, emotionally directed *human-sounding* delivery (changes of stress, pitch contour, urgency, doubt, relief). Mechanical GuyNeural TTS with just rate/pitch control previously sounded insufficiently expressive. Prepare emotional intention per line, scene-level auditions in contrasting delivery styles and real listening checks. Narrative sound should have tension, development, release, distinction among physical/archive/radio/ambience/material effects. Audible music is NOT an almost inaudible synthetic hum. Source/cue/licensing noted.
Normal narration breath gap **0.12–0.55s**; unexpected **>0.85s editorial fail** and **>1.20s release fail**, measured in isolated stem even if music masks it. Do not alter voice cadence just to fit rigid scene slots. Compose picture timing from actual performance when real episode is authorized.
Approx target -14 to -12 LUFS integrated, final true peak <= -1 dBTP by project mix evaluation (not automatic guarantee), and separate phone/headphone listening. Episode 009 owner requested VO and SFX +~3 dB compared with music, but boosting sound is not substitute for more emotionally performed voice. Original release prep script and R2 changelog are on `film/ghost-army-1945`.

### SFX assets (already in repo)
- Primary **50-cue original Curio SFX** FLAC pack: `audio/curio_sfx_v1/`, CSV/JSON catalog, grouped categories: ambient, archival, cinematic, editorial, mechanical, motion, science, audition MP3.
- Supplemental **32 original synthetic WAV sounds**: `production/audio/original-sfx-v1/wav`, catalogs and generation script.
- Separate user Drive SFX library (bulk not committed): `https://drive.google.com/drive/folders/1JsF-myJsH4rnyy0NI-OjDL6ZVrSVeC81`.
- Review actual source rights before using Drive/Mixkit/Freesound content in public film/repo; original synthesized SFX should not be misidentified as field recordings.
- Every paper rustle, radio tick, sound cue should support an actual material/narrative event. A “whoosh on every object” is not tasteful sound direction.

## 5. Adopted research and quality lineage
- Bible v1.1 foundations: `production/bible/v1.1/*` visual, motion, audio/caption, hook, workflow, QA, anti-repetition audits.
- v1.2: `production/motion-lab/v1/` nine tutorial/demo sources, generic acquired mechanics, 5 styleframes and difficult moving QA.
- v1.3: `production/motion-lab/v2/` five **actual Vox-titled films** with graphics-only isolation, 20 adopted generics / 12 proposed, eight neutral graphics technical test renders. No evidence of precise source project curves/effects/audio.
- **Adopted v1.4:** user-approved visual-thought and art/motion standard with the two explicit refinements: storyboard editorial sequence before polished art, and assess procedural graphics on specificity and explanatory craft rather than method. Adopted 12 Oct on owner's explicit authorization. This does NOT make rejected V1–V4 videos approved.
- Most recent owner rejection: V4 “just another presentation.” This outranks assistant “success” claims based on codec verification.

## 6. Why artistic approval is a separate test
Never confuse: “animation applied,” “source imagery downloaded,” “correct unit counts,” “media format verified,” “technically valid parallax,” or “camera matched another shot” with an elegant, inventive visual argument. An amazing infographic can still be dull when the next shot is just another similar infographic. Art direction must solve rich compositions, credible identity, purposeful transformations, semantic attention and connecting imagery. The user shouldn't be expected to critique the same template repeatedly.

**Handoff status:** Official canonical Bible is now **v1.4 adopted** and previous v1.3/v1.2/v1.1 safeguards survive. Export/update was explicitly authorized; making a new Ghost Army video is NOT authorized as a consequence of the transfer.
