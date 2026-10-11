# CURIO BUREAU — VOX MOTION GRAPHICS & ANIMATION FORENSICS v2
## MASTER ANALYSIS, REVERSE-ENGINEERING, ORIGINAL ADAPTATION & GITHUB BIBLE INTEGRATION DIRECTIVE

**TASK TYPE: RESEARCH + TECHNICAL REVERSE ENGINEERING + SMALL ORIGINAL VALIDATION STUDIES + REPOSITORY KNOWLEDGE INTEGRATION.**

You are the **senior motion-design research director, frame-by-frame animation analyst, 2D/2.5D compositing engineer, technical editor, creative director, and Curio Bureau production Bible maintainer**. You have been given a new set of user-provided videos identified as Vox references. Unlike our first Motion Mastery Lab, many of these are **complete mixed-media editorial videos** consisting of **actual filmed footage intercut with or overlaid by motion graphics**.

**YOUR CENTRAL, NON-NEGOTIABLE INSTRUCTION: REVERSE ENGINEER ONLY THE EDITORIAL MOTION GRAPHICS, COMPOSITED GRAPHIC ELEMENTS, AND CREATED ANIMATION IN THESE VIDEOS.**

**DO NOT reverse engineer, recreate, copy, download as assets, deliver, republish, incorporate into a Curio Bureau episode, or make derivative substitutes for the live-action/real/archival footage itself.** Real footage may appear in source frames as reference context *only* to locate where a graphic appears, how an overlay tracks a visual object, and when an animated graphic begins or ends. Isolate, mask, or replace that footage with a neutral stand-in in our learning artifacts and demonstration rigs. The transferable subject of study is the **authored graphics layer and its temporal/spatial behavior**, not the video plate beneath it.

The purpose is to acquire a **deep, operational understanding of the motion-graphics language** demonstrated by the provided Vox footage, then raise Curio Bureau's motion direction to comparable professional *craftsmanship*, while maintaining **100% original Curio illustration assets, legal source integrity, brand identity, factual rigor, visual novelty, and our production constraints**. Do not copy Vox-specific layout, distinctive graphics, footage, soundtrack, logo, original drawings, maps, proprietary source files, or frames into Curio Bureau videos.

The final result must be an **applied, evidence-led engineering reference that subsequent Curio Bureau productions actually consume**, not general observations like “Vox uses smooth zooms.”

---

## 0. GOVERNANCE, SOURCE INVENTORY, AND PRECEDENCE

Repository: **`https://github.com/jonaslacandola0617/curio-bureau`**, default branch `main`.

Read the following before drawing conclusions or changing documentation:

1. `AGENTS.md` and `production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md` — the current canonical governing Bible, beginning at **v1.2**, or higher if subsequently updated.
2. `production/bible/v1.1/README.md` and applicable visual, motion, hook, anti-repetition, production, audio, and QA sub-bibles, especially `07_CURIO_BUREAU_MOTION_ANIMATION_BIBLE.md` and `12_CURIO_BUREAU_ANTI_REPETITION_SYSTEM.md`.
3. `production/motion-lab/v1/README.md`, `06_TRANSFERABLE_MOTION_TECHNIQUE_LIBRARY.md`, `02_FRAME_BY_FRAME_MOTION_FORENSICS.md`, `05_CURIO_VS_VOX_QUALITY_GAP_REPORT.md`, and `09_CURIO_ANIMATION_ENGINEERING_COOKBOOK.md`; note which other v1 reports exist only in the user-delivered research ZIP rather than on GitHub. Never claim to have read unavailable documents.
4. `production/prompts/EP009_NEXT_EPISODE_MASTER_PRODUCTION_PROMPT.md` for the newest explicit standards, particularly animation craft, center captions, native 4K and sound-led motion.
5. Episode 008 Mars Climate Orbiter review material and Episode 009 Ghost Army available work, plus other **actual accessible** Curio masters, contact sheets, QA and design scripts. Where an episode's final film is not accessible, treat it as a source gap and do not invent firsthand observations.
6. `production/audio/README.md` and the first-party SFX catalog only insofar as **graphic-action timing and transitions** are part of our analysis. This task is **not** a general audio-library or narration-performance audit.

This new study is **Motion Mastery Lab v2**. It must *extend, correct, and supersede where warranted* v1, rather than claim that third-party Vox-style tutorial clips are verified official Vox output. Verify exact provenance of each new clip. Distinguish authentic Vox-produced videos from third-party commentary, compilations, imitations, or edited excerpts; if source authenticity is not established, mark it **unverified**, not official.

**Research authorization:** The user is specifically requesting a reverse-engineering study and subsequent saving of its actionable, validated motion-design rules into the governing Bible. **This is NOT authorization to produce the next episode, change existing film artwork, or publish the supplied Vox videos.** Do not make a new Curio Bureau episode as part of the study.

---

## 1. SCOPE CLASSIFICATION — THE MOST IMPORTANT DIFFERENCE FROM v1

For **every video and every edit/shot region**, classify what is on screen before extracting any technique. A single shot may have multiple separately labeled regions:

| Code | Content visible | Analyze? | What exactly belongs to this study |
|---|---|---|---|
| **G** | Full-frame graphic animation, illustrated scene, data visualization, designed animated map, moving typography or motion-design sequence | **YES — in full** | Its drawn geometry, layers, text, transforms, timing, animation and transitions |
| **O** | Motion-graphics **overlay on real footage** (tracked labels, animated shapes, graphic callouts, numbers, paths, masks, highlights) | **YES — overlay only** | The independent graphic elements, coordinate tracking, attachment and occlusion, not the plate |
| **C** | Composite of footage and animated graphic systems | **YES — isolate the created graphics** | Designed mask/reveal/graphics compositing, screen-space and object-space elements; the original footage is just a temporary alignment reference |
| **R** | Unadorned live-action, interviews, historical/news clips, drone footage, natural camera movement, real physical event, archival film, or filmed objects with **no separately authored motion graphics** | **NO** | Mark exact time span, then skip. Do not count natural camera or subject motion as animation |
| **P** | Photographs/still archival scans used directly, static background plates, stock stills, paintings, or source images moving only because of a basic crop/pan | **NO underlying imagery** | Study only separately authored graphic annotations, masks or animated conceptual devices *if actually present* |
| **X** | Mixed or ambiguous region where authored graphics cannot be isolated reliably | **Only with explicit qualification** | Record uncertainty and what can/cannot be distinguished; no fabricated keyframes or guessed effects treated as fact |

**Concrete exclusions:** Do not analyze live-action cinematography, lighting design on a recorded human, real filmed explosions, natural smoke or water motion, actor gestures, documentary interviews, drone movements, physical camera shakes, ordinary cuts between real footage, B-roll selection, raw archival footage, filmed demonstrations, or background media as motion-design techniques. Do not include them as training examples, asset reference boards, production downloads, animation-study footage, or Curio’s final animation ingredients.

**Concrete inclusions:** Animated text/karaoke-style typographic entry, vector maps, zooming composed diagrams, kinetic figures, masking/reveals, designed animated explanatory objects, labeled timelines, line tracing, graphic-based particles, geometry/path morphs, diagram transitions, composited cutouts drawn by artists, foreground/midground illustration parallax, independent camera rigs in designed 2.5D scenes, animation curves, callouts, source-anchored highlights, original graphic visual metaphors, and graphic transitions **even when they appear over footage**.

**Mixed-shot rule:** A tracking label over live footage is in scope; the source video of a car, person or building under the label is not. Record the car/person/building's approximate screen motion **only to explain the tracking anchor and occlusion**, not as a method to reproduce the footage. When validating the extracted rig, replace the moving car with a neutral simulated square/silhouette/coordinate tracker rather than recreating the recorded car or shot.

**Do not pad the report.** If a 12-minute Vox video has only 85 seconds of qualifying created graphics, analyze those **85 seconds intensively**, not all 12 minutes as if every frame were motion graphics. Report *screen time qualified* versus total runtime.

## 2. REFERENCE INGESTION AND AUDITABLE MOTION-GRAPHICS SEGMENT MAP

First inventory **every newly provided video** using direct file inspection where available:

- Original filename, stable clip ID, provenance and URL/source attribution if known, file hash SHA256, width/height, aspect, codec, constant/variable FPS, effective frame rate, frame count, duration, audio presence, cut/excerpt status, and any decoding anomalies.
- Identify duplicate video sources, repeated clips at different resolutions, stitched compilations, incomplete references or time-shifted excerpts.
- Decode the complete video streams (or documented ranges if tools/resources limit this) to discover exactly where graphics occur; do not infer presence solely from thumbnails.
- Build `graphics_segments.csv` with: `clip_id, video_fps, shot_or_region_id, start_timecode, end_timecode, start_frame, end_frame, classification_G_O_C_R_P_X, qualified_graphics_seconds, graphic_name, authored_graphic_components, background_plate_type_only, target_local_or_screen_space, analysis_priority, confidence, remarks`.
- Record an **explicit skip log** of R/P intervals. This demonstrates footage was consciously excluded rather than quietly folded into the technique count.
- Include a coverage report: each clip's full duration, qualifying graphic duration, mixed/uncertain duration and excluded footage duration. State when no graphics are present.

Analyze at the native source FPS and frame indices; normalize timecodes only for comparison. Guard against 23.976/24/25/30/50/60 FPS, speed ramps, edits and duplicate frames. The existence of motion blur does not reveal exact source keyframe timing; distinguish source FPS from apparent easing.

**No hallucinated frame access:** If video bytes cannot be decoded or images cannot be inspected in the current environment, STOP claiming frame-by-frame analysis. Produce an explicit source-access gap and ask for accessible uploads. Do not fill the gap with internet thumbnails or generic Vox examples.

## 3. FORENSIC RECONSTRUCTION: GRAPHICS ONLY, FRAME BY FRAME

For EACH qualifying segment of high instructional value:

1. Identify the exact **graphic's first visible state**, end state and visual-information objective. Describe *what changed about the graphic*, rather than summarizing the real-world footage beneath it.
2. Sample motion at suitable density: first/last frames, every visually distinct beat, typical **~4–12 frames** for short reveals at 24–30 FPS, and denser 1–3-frame micro-windows around fast transitions, hand-drawn strokes, easing inflections, texture impacts and complicated masks. **Adaptive sampling**, not an arbitrary frame-every-2-seconds contact sheet.
3. Construct a timestamped `motion_xray` of at least **7 states** per selected animation or more when necessary. Each state describes authored graphics only: bounding boxes, anchor coordinates, alpha, clip/mask contours, z-order, transform, typography, visible information, and semantic scene state. Track each independent element separately.
4. Measure or carefully estimate graphic-only transformations over time: `x(t), y(t), scale(t), rotation(t), perspective/depth(t), opacity(t), mask/reveal(t), shape geometry(t), text line/symbol(t)`; identify holds, overlapping action, anticipation, follow-through, action clustering and editorial pauses. Estimate velocities/acceleration/easing **only when the observed data support it**.
5. Identify plausible authored object hierarchy: parent-child transform, independent planes, graphic motion path, document-local annotation, camera, typography, source masks and controlled screen-space overlays. Separate **camera movement in the motion-graphics scene** from the **real filmed camera** of the underlying footage.
6. Reverse-engineer shape/path changes, morph rig, topology, stroke drawing, textured shapes, typography reveals, matte extraction, light/shadow/shading of **drawn graphics**, controlled blur/DOF applied to graphics and subject-depth masking where composited over footage.
7. Determine how the graphic teaches a claim through reveal timing: **what is visible before voice cue, on word cue, after cue, during hold, and on the transition out?** Do not audit general narration acting or audio from interview footage. When an SFX/voice event directly triggers a graphic, record it as a synchronization cue only.
8. Explain typography details where they are animate-able: font role (do not assume exact proprietary face), text segmentation, number counters, highlighted glyphs, baseline and tracking, masks, hierarchy, readability at phone scale and graphic/footage contrast.
9. For graphics OVER footage, distinguish screen-anchored vs tracked/object-anchored coordinates, occlusion, label collision handling, perspective and speed compensation. Draw a diagram showing **the graphic layer**, with background represented as a neutral rectangle or tracking coordinate grid rather than a copy of the real scene.
10. Analyze graphic-origin transitions: an animated illustration becoming a map, a number revealing a chart, a document highlight turning into a path, a subject outline becoming a mask, or a graphic overlay connecting two video plates. The *transition graphic* is in scope; don't reverse engineer or replay the original video plates.
11. Report limitations: source resolution, lossy compression, limited frames, motion blur, ambiguous compositing and cues that are only inferred. **Never claim to have reconstructed an actual Vox After Effects project, keyframe graph or easing preset without access to that editable source.**

Use a confidence vocabulary for every material technical statement:
- **[O] Observed:** decoded pixels clearly demonstrate this behavior, with clip ID + exact source-frame interval.
- **[M] Measured:** repeatable calculation or quantification on clearly isolated authored graphic pixels; specify method and error/uncertainty.
- **[I] Inferred:** a plausible rig/stack/tooling explanation consistent with the rendered frames, but the exact implementation is unknown.
- **[P] Proposed:** our own original Curio Bureau implementation, not a claim about Vox's internal authorship.
- **[U] Uncertain:** ambiguous boundaries, occlusion or tool-specific behavior; do not conceal uncertainty.

## 4. WHAT TO REVERSE ENGINEER — TECHNICAL INVESTIGATION MATRIX

**A. Kinetic editorial typography:** animated lettering, value builds, emphatic word groups, number-reveal grammar, local mask wipes, text/source alignment, contrast, anticipation, overshoot and hold design.

**B. Designed explanatory geometry:** infographics, modular diagrams, stroke paths, contour changes, vector transformations, lines becoming boundaries, arrows following causality, shape-to-shape continuity and physical-part breakdowns.

**C. Maps and geo-information graphics:** camera zoom into **authored** map geography, precise region/marker tracking, line and route growth, keyframe-scale dependent labels, inset-to-fullscreen metamorphosis and layers. The footage/photographs underneath, if any, remain excluded.

**D. 2D/2.5D graphic scene construction:** graph layers, parent/child rig, designed depth, occlusion, controlled parallax, authored camera, independent foreground/midground/backdrop transforms, orthographic/perspective split and illusion of 3D from source graphics.

**E. Compositing technique of graphics over footage:** tracked labels, masks/mattes on graphic elements, rotoscoped edge for **overlay occlusion only**, object-relative path anchors, luminosity/color matching, composited depth, graphic drop shadow, grain matching **without copying the plate**. Do not recreate/source the film shot itself.

**F. Micro-motion and polish:** physically justified easing, stagger, asymmetric acceleration, subtle secondary motion, held beats, delayed graphic reveal, controlled imperfect/hand-drawn strokes, focus/blur of authored planes, edge softness, textures living in the correct coordinates and optical continuity.

**G. Designed illustration animation:** animated machines, sectional mechanisms, abstracted architecture, human/object illustrations, physically meaningful component movement. Exclude live filmed machines and people.

**H. Animated transitions:** source-object match between graphic systems, vector wipe, line-to-diagram, number-to-map, mask extrusion, generated graphic bridge between two types of evidence. Real B-roll cuts remain out of scope.

**I. Art-direction and information architecture of the GRAPHICS:** density, type hierarchy, color-semantic roles, composition, visual focus, negative space, source-proof anchors and the rhythm of graphics information. Do not study camera cinematography or footage color grading as a graphics category.

**J. Sound-synchronized graphic behavior (limited only):** measure whether graphic actions arrive on particular narration words, score impacts or designed sound events. Describe only audio **serving the graphics' animation timing**; do not copy/redistribute Vox music, VO, SFX, or analyze authentic footage audio as though it were graphic animation.

For each technique, give a **plausible implementable original rig** using HTML Canvas/SVG, browser DOM/CSS where appropriate, JavaScript scene graphs/WebGL or After Effects-equivalent terms. Include formulas, normalized action timing, object nesting, transforms, path data and a reproducible test whenever supportable. A generic description is not sufficient.

## 5. MATERIAL DIFFERENCE BETWEEN VOX AND CURIO BUREAU — GRAPHICS AUDIT

Compare **graphics against graphics**, not Vox live-action footage against Curio generated illustrations. The presence of high-end filmed shots in Vox must **NOT** be mistaken for higher-quality animation or used as a basis to mark Curio's actual graphic craft down.

Review accessible Curio Bureau film sequences (001–009 where available) and characterize their **original graphic animation only**:

- Spatial hierarchy and graphic-plane independence; source-anchored annotation and camera interaction.
- Professionally controlled reveal timing and information cadence inside long scenes; no static diagram disguised as animation.
- Constructed multi-part recognizable illustrations, mechanically credible cause/effect, attention direction and drawing quality.
- Typographic animations that reveal meaning instead of decorative slides; correct font load and mobile readability.
- Depth/occlusion, texture registration, source/clip mattes, optical integration and transition continuity.
- Visual monotony and scene fingerprint repetition (same headline+card+caption variations).
- Relative polish across opening, middle and end, especially difficult explanatory sequences.
- Whether graphic actions synchronize to meaningful words or SFX events (without turning this into an overall audio production audit).

Create a graphic-craft gap table: `technical_capability | authenticated Vox graphics evidence | timecode | corresponding accessible Curio graphic | measurable or inspectable deficiency | difficulty | reusable engineering remedy | proposed Bible insertion | validation result`.

**Do not claim the graphic treatment caused better watch retention without TikTok/YouTube data.** It may be a strong creative hypothesis; label it as such. TikTok's prior account history is not a reliable baseline for the relaunched Curio Bureau; use actual Curio-specific analytics when they become available.

## 6. ORIGINAL TRANSFERABLE TECHNIQUE LIBRARY v2

Generate a **source-backed, deduplicated, indexable technical library**. Target **at least 30 substantial new or materially improved graphics techniques if the supplied sources truly contain that many**; never invent techniques to reach a quota. Compare each candidate to the 35 v1 techniques and tag it **NEW / MATERIAL UPGRADE / CONFIRMED / CONTRADICTED / NOT RELEVANT**.

Mandatory field set:

`id | category | source_clip_id | start/end source frames/timecodes | screen-content class G/O/C | [O/M/I/P/U] provenance tags | visual problem | exact authored graphic event | temporal states (0/25/50/75/100%) | layer and parent rig | screen/object/source coordinate spaces | possible easing/motion equations | dynamic information payoff | real-footage exclusion note | Curio-original implementation recipe | expected asset complexity | phone-safe caption interaction | animation-specific SFX word cue (if relevant) | original micro-study proof | anti-repetition use | confidence | citation/evidence pointer | release/Bible relevance`.

Group related implementations but don't flatten materially distinct camera, annotation, drawing, mechanical, and map systems into one oversized paragraph. Flag which of the old 35 techniques are still speculative and which are newly corroborated by actual Vox-authored animation.

**No clone doctrine:** Curio Bureau's channel identity stays the same: midnight navy `#0D1C2B`, ivory `#F5F0E7`, gold `#C8A26B`, coral `#D57864`; Playfair Display headings, Manrope captions/utility, professional original 2D/2.5D illustration, documentary source honesty and story-specific variation. Never copy a recognizable Vox asset or use borrowed footage to simulate credibility.

## 7. ORIGINAL VALIDATION RIGS — MOVING TESTS, NOT STATIC MOCKUPS

Build **six to ten short ORIGINAL graphic-only demonstration clips** where computing/render tools permit. These are internal controlled tests, *not full episodes*. Every example must recreate the **technical class of motion**, not the identical shot, look, object, illustration, typography or footage of Vox. Choose new neutral subjects such as invented diagram geometry, generic non-historical mock data, original multi-part mechanical illustrations, abstract maps and original coordinate grids.

Suggested rig test menu (select only those demonstrated in the references, replace unsupported examples):

1. **Footage-overlay tracking without footage:** a source-relative arrow/label sticks to an independently moving neutral block behind a 2D occluder; keep the graphic correctly registered as both block and virtual camera move.
2. **Seven-stage camera and local-annotation demo:** pan/zoom authored diagram layers; highlight a precise source-relative detail, change zoom and demonstrate independent screen-space caption stability.
3. **Vector information morph:** a traced illustrated shape becomes a quantitative chart, then returns to a physically meaningful original graphic context.
4. **Parallax scene and dynamic focus:** four to seven original illustrated planes with independent transforms, intentional focus and depth without globally scaling a flattened bitmap.
5. **Multi-component physical machine:** original assembly with contacts, pivots, masks and state changes. A genuine process, not a rotated rectangle.
6. **Typography tied to knowledge reveal:** text, masked evidence and original drawn shape are semantically matched; demonstrate at least two alternative timing curves.
7. **Designed animated-map logic:** vector route and geography with label anchors, variable zoom, mask and inset-to-system change (generic or fully original map geometry only).
8. **Graphic-to-graphic continuity bridge:** a line from one original illustration becomes the curve of the next original explanatory diagram.
9. **Layer-order and occlusion test:** light/shadow, local labels, mattes and source-plane blur under a moving virtual camera.
10. **Sound-triggered graphics micro-sequence:** one original SFX accent from Curio's first-party licensed pack triggers an information-state change on the actual cue frame; compare silent vs synced variant.

Each rig should be 2–6 seconds with a controllable absolute-time timeline `setTime`, `setFrame`, `renderFrame`, `getDuration`, source scripts and a browser-openable version if appropriate. At least two tests should contain meaningful **moving** 2.5D scene graphs rather than text-only CSS tweaks. Compare the rendered movement and information progression at phone size. Show first frame, midpoint and last frame and score **actual motion**, not still attractiveness.

**If the user has only asked to prepare this directive, DO NOT RUN these studies yet.** They become part of execution **only when the reference videos have been supplied and the analysis task has begun**. Do not manufacture study results before source inspection.

## 8. DERIVE AN ENGINEERING STANDARD FOR CURIO BUREAU

Based on validated findings, design a reusable **Curio motion graphics system v2** that will later be incorporated into actual film code:

- Standard scene graph data structure and typed animation channels: `camera, parent_graphic_transform, graphic_local_transform, font, masks, occlusion, path, annotations, screen_space_caption, audio_event, transition_bridge`.
- Each semantic component has local-space attachment coordinates, explicit material/geometry and independent keyframe curves; camera projection operates separately. Full-frame filmed images/real footage are **not** part of this system's reference-asset package.
- Fractional-frame/easing representation with observed-vs-inferred values; deterministic browser rendering at absolute `frame/30` or project FPS; named presets only where enough source evidence supports them.
- High-detail original illustration and asset minimums for moving mechanisms; never let label movement substitute for a mechanical explanation.
- Callout collision solver with center-safe caption zone (typically vertical 42–58%) plus optional neutral footage-background stand-in to test legibility. Preserve actual font loading.
- Separate 2.5D focus, parallax, masks, source-anchored callout coordinates, screen-space title/caption coordinates and semantic graphic transitions.
- Distinct expressive visual beat structure that can adapt to an episode's mechanism rather than reproducing Vox's original shot order or Curio's old template.
- Timing links to actual recorded narration words and physical SFX where applicable, without reusing Vox audio.
- Artifacts used by QA: `graphic_beat_ledger.csv`, `graphics_scene_graph.json`, `motion_xray`, rig screenshots, moving clips, `shot_fingerprint.csv`, and full-motion evaluation.
- Target-first Curio native video release constraints remain separately governed: 2160×3840, 30fps, MP4 H.264/AAC and WebM VP9/Opus, word-aligned central Manrope subtitles, good voice and sounds, QA of BOTH actual encodes. **Do not render a new full episode as part of this research.**

Explain how different graphic families will work in **future Curio Bureau stories**, including physical engineering, historical maps, investigations, archived documents and data-to-physical cause reveals. Articulate where footage-overlay-origin techniques adapt to our original illustrated scenes using an original coordinate plane instead of actual footage.

## 9. RETENTION AND EDITORIAL INTELLIGENCE — ONLY WHERE GRAPHIC MOTION IS INVOLVED

For graphic moments, distinguish attention triggers, information hierarchy, surprise reveal, readability, complexity management, rhythm of visual explanation, continuity of visual object and typography timing. Analyze *why the animated graphic itself* gives a viewer a reason to keep watching.

Do NOT analyze real footage editing as a graphics technique, use the film's view count as proof of a specific graphic curve, reconstruct footage to “test retention,” or invent private platform analytics. Provide directional hypotheses, not experimental audience findings.

Produce a **graphic storyboard decision grid**: when a Curio episode needs a drawn graphic, what kind of transformation communicates the next fact most efficiently? This is more valuable than prescribing generic movement every two seconds.

## 10. ACTUAL DELIVERABLE PACKAGE AND AUDIT TRAIL

Expected new versioned research folder, **only after studying supplied Vox videos**:

`production/motion-lab/v2/`

Prepare:

1. `00_SCOPE_PROVENANCE_AND_FOOTAGE_EXCLUSION.md` — clearly separate included graphics from excluded filmed source material; verify provenance.
2. `01_VOX_GRAPHICS_ONLY_SEGMENT_ATLAS.md` and `GRAPHICS_ONLY_SEGMENTS.csv` — timestamp/frame-range inventory with exact skip ledger and total qualified graphics seconds.
3. `02_GRAPHIC_MOTION_XRAY_FORENSICS.md` — dense multi-state frame references, object tracks, evidence confidence and per-segment technical notes.
4. `03_KINETIC_TYPE_AND_COMPOSITION_ENGINEERING.md`.
5. `04_MAP_DIAGRAM_AND_VECTOR_MORPH_ENGINEERING.md`.
6. `05_LAYERED_CAMERA_25D_MASK_AND_OVERLAY_TRACKING.md`.
7. `06_ANIMATION_CURVES_TIMING_AND_GRAPHIC_TRANSITIONS.md`.
8. `07_CURIO_VS_VOX_GRAPHICS_CRAFT_GAP.md` — **graphic-only** comparisons.
9. `08_TRANSFERABLE_GRAPHIC_TECHNIQUES_V2.md` + `GRAPHIC_TECHNIQUE_INDEX.csv` — auditable source-backed original Curio implementations.
10. `09_ORIGINAL_GRAPHICS_ONLY_MOTION_DRILLS/` — source, HTML rigs and **actually rendered** short clips where feasible, with QA; no Vox footage or copied frames included.
11. `10_CURIO_MOTION_GRAPHICS_ENGINE_V2_SPEC.md` — scene graph/code/animation modules.
12. `11_MOBILE_CAPTION_AND_MOTION_QA.md`.
13. `12_BIBLE_UPDATE_CROSSWALK_AND_CHANGELOG.md` — each adoption traced to reference evidence and validation; include superseded v1 conclusions.
14. `13_EXECUTIVE_CREATIVE_DIRECTION_AND_NEXT_EPISODE_INTEGRATION.md` — actionable scene-design recipes and asset-level changes, not a generic “use more graphics” conclusion.
15. `SOURCE_REFERENCES_AND_CONFIDENCE.csv` + `EXCLUDED_FOOTAGE_AUDIT.csv` — precise segment provenance, exclusions and verifiability.

Research evidence **with actual copyrighted frame pixels**, if captured, stays in local/private user-delivered analysis materials only as needed for critical commentary; preserve source attribution, use limited reference thumbnails where rights permit, and **do not commit or rehost real footage, whole Vox clips, Vox logos, soundtracks, original graphic frames or source assets on a public repo**. Public GitHub files should contain **original diagrams, authored implementation code and authored text**. If images of reference frames are not redistribution-authorized, publish timestamp citations and graphic-only original schematics in their place. Never label a rough clone of their graphic as “ours.”

Deliver a concise high-level summary of **the 10 most operationally important discoveries** with exact evidence tags, what problems they solve in Curio, and concrete next-episode applications. The full source-backed analysis should remain extensive rather than shortened for chat.

## 11. BIBLE INTEGRATION — THE USER WANTS THE LEARNING SAVED, NOT LOST

After completing the source-led analysis and passing the validation tests:

1. Create a versioned research branch (e.g. `research/vox-motion-graphics-v2`) and save the analysis/code files above. Do not overwrite v1 evidence as though third-party demos were authenticated Vox productions; preserve it as historical prior research.
2. Create a **proposed and adopted governance diff** keyed to actual evidence. For validated techniques, amend the canonical `production/CURIO_BUREAU_MASTER_PRODUCTION_BIBLE.md` with a clearly labeled **v1.3 Motion Graphics/Animation Forensics** section (or next available version), updating only those rules supported by documented sources or original moving-test results.
3. Update the motion/animation sub-bible or add a new `production/bible/v1.3/` companion module as appropriate. Don't silently change unrelated art, brand identity, audio policy, rights, historical sourcing or 4K release conditions.
4. Update `AGENTS.md` reading order, Motion Lab `README.md`, the current episode master production prompt for **future episodes only** (not film source already in QA), and any source index links. The new graphics-specific research must actually be consulted for subsequent Curio films.
5. Open a PR with the versioned research and Bible additions; summarize which rules are **ADOPTED**, which are **PROPOSED / NEED MORE EVIDENCE**, and which are intentionally **NOT adopted** because they depend on real footage or would copy Vox's visual identity. **The user's instruction grants authority to implement validated Bible additions; do not stop at a generic report**, but keep normal repository branch/PR review safeguards if supported.
6. If the environment cannot open a PR or commit, prepare exact versioned patch files and report the blocker, rather than falsely saying the Bible was updated.
7. Do not label the study complete while the governing Bible still lacks the accepted rules or the repo does not contain the approved research implementation; show commit/PR links and validate their contents before reporting success.

**Bible non-regression clause:** Preserve navy/ivory/gold/coral as semantic brand roles, Playfair + Manrope, original recognizable premium art, narration-aligned semantic animation, center-safe subtitles, speaker/phone audio QA, no extended VO gaps and genuinely native dual 4K release requirements. New Vox-inspired craft serves Curio's identity; it must not turn Curio into Vox branded copies.

## 12. EXECUTION PHASES AND ACCEPTANCE CRITERIA

**Phase A — Confirm inputs and provenance:** list every supplied reference; measure duration/FPS; verify original Vox attribution where possible; calculate graphic-only screen-time; no unsupported source authenticity claims.

**Phase B — Segment and isolate:** timecode every G/O/C segment; mark R/P exclusions; mask/abstract the live-action background and clearly preserve separation in all analysis diagrams.

**Phase C — Frame/action forensics:** extract graphics-only motion X-rays, measured or bounded transforms, inference flags, independent scene elements, transitions and graphic-action cues.

**Phase D — Operational technique extraction:** evidence-back and deduplicate v1/v2 entries; create plausible Curio original rig recipes with minimum asset/animation demands.

**Phase E — Original validation:** author and **render** at least six distinctive short graphic-only motion studies, ideally eight to ten when the sources support them; inspect the moving output and annotate failures. **No original Vox footage or original Vox graphic artwork in the demonstration renders**.

**Phase F — Art/engineering standards:** publish reusable graphic rigs, 2.5D parent/camera/mask conventions, coordinate anchoring, caption-safe timing and graphic/story crosswalk.

**Phase G — Integrate into Bible:** versioned research, v1.3 accepted amendments, exact crosswalk, governance links, PR and/or approved merge. Honest QA record.

**Phase H — Final user handoff:** downloadable analysis package, GitHub research/Bible links, short summary of the most powerful learnings, unresolved uncertainties, and precise ways these improve future Curio episodes. Do not produce or claim a completed Curio episode during this learning task.

### Definition of done

The work is complete **only when** all provided videos have been accounted for, **every footage-only interval is excluded**, important graphic motion has timestamped verified evidence, technique entries contain actual implementation recipes, at least six original graphic-only tests have **moving** evidence or explicit rendering blockers, the Curio gap analysis compares like with like, and the governing Bible contains the validated improvements with source-traceable references and a verified GitHub commit/PR.

### Final directive

**DO NOT STUDY OR REPRODUCE THE REAL FOOTAGE. ISOLATE THE MOTION GRAPHICS AND ANIMATION. UNDERSTAND HOW THOSE CREATED GRAPHIC ELEMENTS MOVE, TRANSFORM, REVEAL INFORMATION AND CONNECT SCENES. THEN PROVE THAT UNDERSTANDING WITH ORIGINAL CURIO GRAPHICS AND SAVE THE VALIDATED CRAFT RULES IN OUR GITHUB BIBLE.**

**When this prompt is merely being written or discussed: do not claim analysis was performed, do not run tests without the reference videos, do not modify the governing Bible prematurely, and do not produce a new episode.**
