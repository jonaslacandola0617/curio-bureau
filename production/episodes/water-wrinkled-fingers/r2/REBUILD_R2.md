# R2 recovery and packaging

Restore the private R2 source checkpoint to preserve source images, texture/font rights, assets and the exact approved mix. Keep shared/finishing.js, shared/editorial-finish.js and shared/brand.js in their checkpoint locations. The compiled studio fingerprint is 1285adadec9743d53a4bd36cf5ab2950aacb7556d9d65c2e1aa8551c2a3f74d8. Do not regenerate media to repair delivery.

Restore and verify already-saved native chunks first; capture only missing ranges. The recovered master is byte-identical to the prior R2 master, SHA256 2185cdd4bea354cd3b3c2a04f37fe385a421bfe9d1f4cac87b697584f8a2775e.

package_player.py reads delivered/Wrinkled_Fingers_4K.webm and writes a self-contained offline HTML player. It decodes embedded base64 into a Blob URL once, avoiding repeated huge data-URL parsing on each download. test_player.cjs checks native metadata, seeking and two exact WebM downloads; requires the pinned headless browser under runtime/chrome-linux/headless_shell or CURIO_CHROME. PLAYER_QA.json contains the actual restored-output test, not the old R1 report.

All proprietary export media belong in versioned GitHub Release assets under the owner-adopted archive rule. DELIVERY_MANIFEST.json records current local export hashes; release upload remains pending until actual upload receipts are verified. Full-film owner review is separate and pending.
