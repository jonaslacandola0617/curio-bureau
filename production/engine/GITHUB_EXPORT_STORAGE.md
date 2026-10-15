# GitHub export storage — owner directive, 15 October 2026

Status: ADOPTED. The owner explicitly directed that all Curio Bureau proprietary exports be included in the project's GitHub repository assets / Releases for persistent storage and backup. This supplements the native render recovery rules and supersedes the default use of Drive or chat file storage for proprietary outputs. It does not change artistic approvals, rights, or the locked render/audio standards.

## Required storage
- Commit source code, reusable original assets appropriate for Git, scripts, captions/posts, rights records, small QA and hash manifests.
- Attach large proprietary outputs as assets of a versioned GitHub Release: master MP4, posting MP4, native WebM, browser player, original export packages, and expensive render recovery bytes where appropriate.
- Use an episode/revision tag, such as water-wrinkled-fingers-r2. Describe review status honestly: a review release is not owner approval or a social-media publication.
- Actions artifacts are build transport, not the sole archive: they expire. Promote required outputs to Release assets before declaring durable delivery.
- Keep each Release asset below GitHub's current per-file limit (under 2 GiB at adoption). Split larger recovery files with ordered parts and whole/part hashes. A manifest referencing missing local bytes is not a backup.
- GitHub remains the primary archive for proprietary exports. Do not introduce a different primary storage destination without owner direction. Existing backups remain intact; this directive does not authorize their deletion.
- Respect existing item-level rights and privacy for third-party raw assets, reference tutorials, credentials and signed URLs. Publish original/cleared export media with required attribution; don't silently turn a nonredistributable reference into a public raw asset.

## Delivery gate
1. Check repository identity, export hash, revision, native format and actual QA.
2. Check the destination Release and existing assets before uploading; avoid duplicating uncertain writes.
3. Upload actual bytes, not a progress record or a link to temporary storage.
4. Read back asset ID, name, uploaded state, byte size and digest where available. Retain receipts in the episode delivery manifest.
5. Verify downloads against SHA-256 when the provider does not expose a matching digest.
6. Return only observed Release/download URLs. Keep local evidence until the archive and links are verified.
7. If upload/authentication is unavailable, say archive pending; do not claim the export is backed up. Offer the existing review copy without falsely calling its temporary link permanent.

## Recovery
Pin source/mix fingerprints and exact frame coverage. Save closed, verified lossless render chunks to GitHub Release assets at least every two chunks; stop accumulating unprotected work if saving fails. A lossy native recovery proxy can be retained as an explicitly labeled additional fallback, but must never be called lossless or silently substituted into the final master pipeline.

## Platform references checked at adoption
- https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository

Review: Jonas Lacandola / owner direction in conversation, 15 October 2026. Implemented as Bible v1.4.5, storage-only amendment.

