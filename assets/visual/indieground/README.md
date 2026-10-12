# Indieground visual materials — Curio Bureau

Owner-supplied material library, registered 12 October 2026. The owner uses these packs when creating a retro/vintage editorial style and identified them as a needed improvement over the test's procedural surface finish.

**This public directory contains the catalog and usage guidance. The original texture and cutout images are imported into `local/`, which is Git-ignored. Raw binaries are not distributed by this repository.** The original licensed ZIPs remain in the owner's private uploaded files. Their filenames and SHA-256 values make the library reproducible without exposing the source graphics.

## Contents verified

13 received packs: 65 texture JPGs and 73 punk-letter PNG files, totaling 138 images. The letter pack's README describes 72; the actual archive also contains `L-01 copia.png`, which is explicitly cataloged rather than silently discarded. Dimensions are measured from the image files; some portrait assets differ from the orientation stated in the pack README.

`indieground-freebies-textures-fabric.zip` failed to reach the working environment and is marked **missing**, not inspected or imported.

| Pack | Files | Primary editorial role |
| --- | ---: | --- |
| Vintage paper | 5 | Printed atlas, archival document surface, warm paper substrate |
| Folded paper | 5 | Creased map/document with recognizable fold structure |
| Glued paper | 5 | Pasted poster, repaired/pasted archive or tactile collage substrate |
| Plastic | 5 | Transparent sleeve/wrap with selective specular wrinkles |
| Photocopy noise | 5 | Reproduction character and local print-density variation |
| Dark grunge | 5 | Worn dark surface, used selectively |
| Bubble wrap | 5 | Packaging material where the object/story needs it |
| Abstract | 5 | Subject-specific graphic accents |
| Acid | 5 | Subject-specific damaged/experimental color treatment |
| Gradients | 5 | Deliberate color atmosphere; distinct from analytical focus gradients |
| Graffiti | 10 | Contextual wall/pasted-street material |
| Holographic | 5 | Foil/reflection material when relevant |
| Punk letters | 73 | Selective cutout headline; not a replacement for brand captions |

## Import your licensed copies

```bash
python3 tools/import_indieground_assets.py /path/to/your/zip-folder
# Or import the primary paper/plastic groups only:
python3 tools/import_indieground_assets.py /path/to/your/zip-folder --pack vintagepaper --pack foldedpaper --pack plastic --pack photocopynoise
```

The importer validates archive hashes, exact members, member sizes and image hashes before writing. It preserves the supplied notices, excludes macOS resource forks, reports missing packs, and creates `local/IMPORT_REPORT.json` with stable asset IDs and paths. It never downloads guessed resources, replaces a missing texture with procedural noise, or publishes the library.

## License and public-source boundary

Every supplied README points to [Indieground terms](https://indieground.net/terms-conditions/). The [Freebies License and Prohibited Uses](https://indieground.net/licenses/) allow use in finished personal/commercial designs but exclude redistribution of the source assets. Checked 12 October 2026. This repository is public; ZIPs, original JPG/PNG files, standalone derivative texture sheets, raw public download URLs and source assets embedded as base64 must not be committed or attached to public Releases without additional permission.

Flattened finished artwork/video and private owner-side authoring are different from distributing a source pack. Keep public source projects dependent on each user's own licensed local import. Do not change repository visibility or create a new shared asset repository as a workaround without a deliberate owner decision.

## Production direction

See [material direction](../../../production/visual-assets/INDIEGROUND_MATERIAL_DIRECTION.md) and [tutorial effects direction](../../../production/visual-assets/TUTORIAL_EFFECTS_DIRECTION.md). The Bible remains v1.4. Texture choices support the explanation; they do not certify a Vox match or establish historical authenticity.
