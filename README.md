# Blackfire Autopilot public distribution

This public repository is the distribution surface for **Blackfire Autopilot**, an automation tool for **Blackfire Crusade**.

It contains two intentionally separate surfaces:

- **GitHub Releases** — immutable, versioned runtime/release artifacts.
- **Public website** — product overview, feature explanation, demo/download entry points, and public-facing assets.

The Blackfire Autopilot source code, architecture, internal task packages, and private template library remain outside this public repository.

## Website

The V1 landing page is implemented at the repository root (`index.html`, `styles.css`, `script.js`) so it can be published directly with GitHub Pages after the branch is merged and Pages is enabled.

Product/content contract: [`docs/site-v1.md`](docs/site-v1.md)

## Montage assets

`tools/build_montage.py` generates deterministic, cached background montage images from a supplied private `templates/` directory. The source images are not published here; only generated public-facing montage outputs should be committed.

The generator hashes the selected source PNG bytes and paths. When the source hash is unchanged and all outputs still exist, it exits without rebuilding.

## Artifact boundary

Release artifacts remain immutable once published. Expanding this repository to also host the public website does **not** change that release-asset contract.
