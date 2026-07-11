#!/usr/bin/env python3
"""Generate MagiTrickle-compatible subscriptions from sources/catalog.json."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "sources" / "catalog.json"
OUT_DIR = ROOT / "subscriptions"

BUNDLES = {
    "ai/all-ai": [
        "ai/openai", "ai/anthropic", "ai/google-ai", "ai/perplexity"
    ],
    "dev/all-dev": [
        "dev/github", "dev/docker", "dev/jetbrains", "dev/cursor"
    ],
    "media/all-media": [
        "media/youtube", "media/twitch", "media/spotify", "media/netflix"
    ],
    "social/all-social": [
        "social/discord", "social/telegram", "social/reddit"
    ],
    "gaming/all-gaming": [
        "gaming/steam", "gaming/xbox", "gaming/playstation", "gaming/epic-games"
    ],
    "bundles/developer": [
        "ai/openai", "ai/anthropic", "ai/google-ai",
        "dev/github", "dev/docker", "dev/jetbrains", "dev/cursor",
        "social/discord"
    ],
    "bundles/gamer": [
        "gaming/steam", "gaming/xbox", "gaming/playstation",
        "gaming/epic-games", "social/discord", "media/twitch"
    ],
}


def normalize(value: str) -> str:
    value = value.strip().lower().rstrip(".")
    if not value or value.startswith("#"):
        return ""
    return value


def write_list(name: str, values: list[str], title: str | None = None) -> None:
    clean = sorted({normalize(v) for v in values if normalize(v)})
    path = OUT_DIR / f"{name}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    header = [
        f"# MagiTrickle subscription: {title or name}",
        "# Generated automatically. One rule per line.",
        "",
    ]
    path.write_text("\n".join(header + clean) + "\n", encoding="utf-8")


def main() -> int:
    try:
        catalog: dict[str, list[str]] = json.loads(
            CATALOG_PATH.read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read catalog: {exc}", file=sys.stderr)
        return 1

    for name, values in catalog.items():
        write_list(name, values)

    for bundle_name, members in BUNDLES.items():
        merged: list[str] = []
        for member in members:
            if member not in catalog:
                print(f"Unknown bundle member: {member}", file=sys.stderr)
                return 2
            merged.extend(catalog[member])
        write_list(bundle_name, merged)

    everything: list[str] = []
    for values in catalog.values():
        everything.extend(values)
    write_list("bundles/everything", everything)

    print(f"Generated {len(catalog) + len(BUNDLES) + 1} subscriptions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
