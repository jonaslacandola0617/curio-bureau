# 07 — Curio Bureau v1.3 Companion: GRAPHICS-ONLY SCENE ENGINEERING

**Authority:** This is a supplemental technical module to the **single governing Master Bible v1.3**. It extends the older `production/bible/v1.1/07_CURIO_BUREAU_MOTION_ANIMATION_BIBLE.md`; it does not supersede the fixed brand, researched subject integrity, expressive voice/music, safe center captions, or true 4K dual-format film QA. See `production/motion-lab/v2/README.md`.

## Typed authored-graphics scene graph

```js
const scene = {
 fps:30, duration:4.2, evidenceSource:'citation_id',
 world:{source:{id:'diagram',geometry:'ORIGINAL',transform:t=>Mat3},children:[]},
 camera:{matrix:t=>Mat3},
 graphic:[{id:'part',owner:'diagram',geometry:'ORIGINAL',local:t=>Mat3}],
 masks:[{owner:'part',localShape:'ORIGINAL',z:4}],
 annotations:[{owner:'part',anchorLocal:[0.5,0.38],label:'ORIGINAL'}],
 captions:[{text:'claim',space:'screen',safeBand:[.42,.58]}],
 events:[{id:'node_reveal',time:1.5,fact:'fact002',voiceWord:'word201',sfx:null}]
}
```

### Four invariants
1. **Source-local tracking:** `pScreen=viewport*camera(t)*sourceParent(t)*graphicPart(t)*pLocal` for physically owned annotations; screen captions not under that product. Draw explicit occlusion plane rather than global blur.
2. **Absolute-time determinant:** `renderFrame(frame)` pure function of `frame/fps`. Scrub frames 0,25,50,75,100% in any order and receive identical geometry; no integration-delta drift.
3. **Meaningful states:** `context → first source → graphic action → numeric/causal interpretation → readable hold → next claim`. Word events move the source's physical or measured state, not arbitrary full-screen scale.
4. **No footage assets:** V3-A/V4-C overlays qualify but their filmed/archival photographic plates do not. Tests use neutral square/grid or original illustrations.

## Recommended separately validated families
- Matrix/numeric reveal: 01 original technical rig; V02 141–148s, V01 72–78s; visual data and interpretation on separate tracks.
- Causal node linkage: 05; V01 112–118s; connect only established anchored nodes.
- Original physical measurement: 03; V05 108–116s; independently timed mask/value/tick and source units.
- Multi-part mechanism: 04; V03 143–151s; articulated linkage proof, historic accuracy researched separately.
- Map/camera tracking: 08; V04 525–533s; lat/long/source projection only if own proven geometry, not copied source media.
- Archival evidence marking: 07; V02 445–452s; mark only real cited phrase in legally cleared material.
- Graphic-to-graphic transition: 06; V05 244–252s; cut when topology cannot honestly morph.

## Scene-fingerprint + release
`scene_id,source_type,information_before,information_after,representation,source_anchor,camera_family,mask,read_hold_s,caption_collision_check,source_license,technique_v2_id`.

Do not turn original prototype rigs into actual episode illustration assets. Each future film must meet the Bible's premium full-story design floor and independently encoded genuine 2160×3840/30fps MP4 + WebM checks. A Vimeo/YouTube video with 70% retention threshold has not been observed; never assert this without actual analytics.

**Evidence limits:** five sources with approximately 96 five-second-coarse intervals, 25 explicit R/P exclusions, 20 seven-state graphics-only source X-rays, 32 indexed techniques, and eight technical videos. Exact Vox private easing/keyframe histories, complete shot-per-frame segmentation and retention causality remain unknown.
