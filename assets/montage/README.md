# Generated montage assets

This directory contains only public-facing generated montage images plus `manifest.json`.

Do not copy the private Blackfire Autopilot template library into this repository.

Generate/update the montage from a local checkout that can access the private templates directory:

```powershell
python tools/build_montage.py `
  --templates-root C:\path\to\Blackfire-CV-Autopilot\templates `
  --output-root assets\montage
```

The generator computes a deterministic SHA-256 over source relative paths and bytes. If the hash matches the existing manifest and every listed output still exists, it reports `CACHED` and does not recompute the montage.
