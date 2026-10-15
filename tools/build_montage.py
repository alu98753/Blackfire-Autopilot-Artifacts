#!/usr/bin/env python3
"""Build deterministic cached montage backgrounds from private template PNGs.

Only generated montage outputs belong in this public repository. The source
`templates/` directory stays private.

Requires Pillow:
    python -m pip install Pillow
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
from pathlib import Path

from PIL import Image, ImageOps

GENERATOR_VERSION = 1
DEFAULT_WIDTH = 1600
DEFAULT_HEIGHT = 900
DEFAULT_OUTPUT_COUNT = 4
DEFAULT_COLUMNS = 5
DEFAULT_ROWS = 4


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--templates-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, default=Path("assets/montage"))
    parser.add_argument("--width", type=int, default=DEFAULT_WIDTH)
    parser.add_argument("--height", type=int, default=DEFAULT_HEIGHT)
    parser.add_argument("--count", type=int, default=DEFAULT_OUTPUT_COUNT)
    parser.add_argument("--columns", type=int, default=DEFAULT_COLUMNS)
    parser.add_argument("--rows", type=int, default=DEFAULT_ROWS)
    return parser.parse_args()


def discover_sources(root: Path) -> list[Path]:
    paths = sorted(p for p in root.rglob("*.png") if p.is_file())
    if not paths:
        raise SystemExit(f"No PNG files found under {root}")
    return paths


def source_hash(root: Path, paths: list[Path]) -> str:
    digest = hashlib.sha256()
    digest.update(f"generator:{GENERATOR_VERSION}\n".encode())
    for path in paths:
        rel = path.relative_to(root).as_posix()
        digest.update(rel.encode("utf-8"))
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def read_manifest(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None


def cache_valid(manifest: dict | None, digest: str, output_root: Path) -> bool:
    if not manifest or manifest.get("source_hash") != digest:
        return False
    files = manifest.get("files")
    return bool(files) and all((output_root / name).is_file() for name in files)


def open_tile(path: Path, size: tuple[int, int]) -> Image.Image | None:
    try:
        with Image.open(path) as image:
            rgb = image.convert("RGB")
            return ImageOps.fit(rgb, size, method=Image.Resampling.LANCZOS)
    except Exception:
        return None


def build_one(
    *,
    sources: list[Path],
    output: Path,
    seed: str,
    width: int,
    height: int,
    columns: int,
    rows: int,
) -> None:
    tile_w = max(1, width // columns)
    tile_h = max(1, height // rows)
    canvas = Image.new("RGB", (width, height), (7, 9, 13))

    rng = random.Random(seed)
    shuffled = list(sources)
    rng.shuffle(shuffled)
    needed = columns * rows
    if len(shuffled) < needed:
        repeats = (needed + len(shuffled) - 1) // len(shuffled)
        shuffled = (shuffled * repeats)[:needed]
    else:
        shuffled = shuffled[:needed]

    for index, path in enumerate(shuffled):
        tile = open_tile(path, (tile_w, tile_h))
        if tile is None:
            continue
        x = (index % columns) * tile_w
        y = (index // columns) * tile_h
        canvas.paste(tile, (x, y))

    canvas.save(output, format="JPEG", quality=82, optimize=True, progressive=True)


def main() -> int:
    args = parse_args()
    root = args.templates_root.resolve()
    output_root = args.output_root.resolve()
    if not root.is_dir():
        raise SystemExit(f"templates root does not exist: {root}")

    sources = discover_sources(root)
    digest = source_hash(root, sources)
    output_root.mkdir(parents=True, exist_ok=True)
    manifest_path = output_root / "manifest.json"
    existing = read_manifest(manifest_path)

    if cache_valid(existing, digest, output_root):
        print(f"CACHED source_hash={digest} files={len(existing['files'])}")
        return 0

    files: list[str] = []
    for i in range(args.count):
        name = f"montage-{i + 1:02d}.jpg"
        build_one(
            sources=sources,
            output=output_root / name,
            seed=f"{digest}:{i}",
            width=args.width,
            height=args.height,
            columns=args.columns,
            rows=args.rows,
        )
        files.append(name)

    manifest = {
        "generator_version": GENERATOR_VERSION,
        "source_hash": digest,
        "source_count": len(sources),
        "files": files,
    }
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"BUILT source_hash={digest} files={len(files)} sources={len(sources)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
