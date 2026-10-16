# Cold Metal — finished art review v1

**ART REVIEW. Owner decision pending. This is not a completed film or a render-ready freeze.**

[Five-checkpoint overview](Cold_Metal_Art_Review.jpg) · [Hardest passage, with headings hidden](Cold_Metal_Passage_Review.jpg) · [Local HTML gallery](REVIEW.html) · [All rendered states](rendered)

Seven actual 2160×3840 stills develop the same spoon/skin relationship: opening comparison, initial equilibrium condition, contact initial/intermediate/resolved, unequal transfer and photographic payoff. The five main art checkpoints are 01, 02, 04, 06 and 07. These are original Curio compositions, not copied Vox layouts.

## What the images establish

Two recognizable photographic-style spoon cutouts persist across comparisons. A separately layered hand reaches the same handle contact point. That point leads into a supporting print revealing qualitative outward heat flow. The print supports an invisible physical relationship; it does not replace the photographic scene with a freestanding vector world. A later paired contact view contrasts transfer while retaining the initial-temperature qualification.

The source-of-truth physics remains the project's RESEARCH.md: OpenStax §§13.1 and 14.5. Same initial temperature requires equilibrium under the stated setup; a warmer hand transfers energy toward cooler objects. No temperatures, heat-transfer ratios, timestamps or thermal-camera readings were fabricated.

The room condition is established as a clearly illustrative setup on the comparison surface, not an actual room photograph or filmed measurement. This refines the draft's room pullback while preserving its evidentiary qualification.

## Asset provenance and construction

- `assets/steel-spoon.png`, `wood-spoon.png`, `hand.png`: original built-in image_gen outputs, copied intact from the generated-image outputs. Synthetic photographic illustrations, not real experiment photographs. Generation prompts are in GENERATION_PROMPTS.json. None is diagnostic, historical or measured evidence.
- Playfair Display and Manrope: Google Fonts upstream, included under their respective OFL notices. Original variable fonts retained. Static 900 / 800 instances produced with fontTools from those files because the available static renderer did not resolve variable weights reliably; the final visual proof uses the actual thick outlines. Font source URLs are recorded in ASSETS.json.
- Substrate grain, fibers, print marks, source registration, selective shade, mild chromatic shadow edges and layouts are original code in art.cjs. Source images remain independent RGBA layers. No owner-private textures or third-party tutorial pixels were copied into public source.

This art review uses an original procedural fiber/grain treatment because owner texture bytes were not restored in this pilot. It does not claim to have used those private originals. Future finishing must be judged against the approved visual benchmark rather than the presence of a file slot.

## Actual review and limitations

The first render had a heading collision and washed-out equilibrium objects. Those were corrected before this checkpoint. The spoon and hand contact point now stays fixed through the three demanding states. The rate and payoff frames avoid the central caption band. Useful scientific labels remain in the heading-hidden review.

Renderer: native Skia through @napi-rs/canvas. It renders the actual art at 2160×3840, not an upscale of a smaller video. JPEG review files preserve the native dimensions. Actual raster source resolution remains independent of canvas dimensions: spoon assets are 887×1774 and the hand is 1774×887. Opening spoons are magnified about 1.33× over source pixels; the large hand about 1.40×; the small metal swatch is a more aggressive illustrative crop. These crops are fit for reviewing composition, not a passed final native-detail audit. Replace/reduce the highest crop magnifications before freezing the posting film, then compare changed art with the approved proof.

Static grain/material/colour are shown. Focus hunt, mechanical jitter, exposure cadence, moving grain, camera/transition blur, curve cuts, actual parallax and SFX synchronization require a moving proof; they have not been tested or certified by these stills. No audio was generated, mixed or presented as approved. No ending card was substituted: these are story art states, and the eventual film must restore the exact approved London Bridge ending.

The HTML gallery is static, has no external resources or scripts, and links to the actual files. Its links were checked structurally. A Chromium installation download failed, so no browser execution test is claimed for this gallery. The art itself was rendered and inspected through the independent native renderer.

## Owner decision needed before motion

Review the five checkpoints and the three-state contact passage. The decision concerns composition, image-led explanation and material appearance. Moving integration remains a separate decision.

Existing governing rule: [VISUAL_SEQUENCE_DIRECTION.md](../../../../art-direction/VISUAL_SEQUENCE_DIRECTION.md), §2: “Obtain owner art/sequence approval, then animate the hardest representative passage.” No approval was inferred from the request to try rendering a project. These concrete renders are the required reviewable art result.

After approval: resolve source-detail limits, implement the hardest moving passage, restore approved Bernard/ending resources, inventory and select existing SFX, create the original score, reconcile full speech/caption timing and protect the final word. Then obtain moving and whole-preview reviews, perform a clean restore rehearsal and freeze the package before native production.

## Reproduce this art checkpoint

```bash
node production/pre-render/pilot-20261016/cold-metal-pilot/art-v1/art.cjs
```

Requires Node and @napi-rs/canvas at `CODEX_PRIMARY_RUNTIME_NODE_MODULES`; versions are recorded in QA.json. Image generation is not rerun. The static font instances are already saved. This command only renders static source-backed art; it does not invoke the native-film gate or fabricate a pre-render-ready project.
