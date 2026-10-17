# Mint v2 recovery

Picture source commit:0f897eccd22931966f31b3f371608a0945266992. Native1080×1920,30fps,1201frames. Source assets/fonts remain the tracked art-v2/cold-metal font assets. The original voice MP3 is tracked under this revision. See SOURCE_FINGERPRINT.json for all hashes.

The exact shared mix is preserved as Mint-Mix-v1.flac in the earlier mint-full-v1-review-20261017 Release. Decoding that lossless FLAC back to WAV with the production FFmpeg build was verified to restore the exact WAV SHA256 f089911d25da80480a507849ea02395f1cc455c658c0ea4e62e090fdf509a958. No narration or SFX regeneration is needed. Materialize audio/mix.wav and retain the fingerprint guard.

All five Mint-v2-lossless-* FFV1 chunks are attached to mint-full-v2-review-20261017. Download their observed archive URLs from RECOVERY.json, verify each SHA256/decoded frame count, and place them under chunks/. Only verified downloaded bytes retain DURABLE status. Run encode.py to build the complete MP4 from those exact picture/audio inputs. Do not substitute v1 chunks into the v2 sequence.

FROZEN_FRAME_RESTORE_QA.json proves22native frames across every scene and join reproduced identically from a separate clean source checkout. It does not claim a second full movie rebuild or human approval. Previous source tags and movie assets remain preserved.
