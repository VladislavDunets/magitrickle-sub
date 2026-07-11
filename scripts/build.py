#!/usr/bin/env python3
"""Build MagiTrickle subscriptions from v2fly and official Telegram CIDRs."""

from __future__ import annotations

import ipaddress
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "sources" / "config.json"
OUTPUT_DIR = ROOT / "subscriptions"
USER_AGENT = "magitrickle-sub/1.1 (+https://github.com/VladislavDunets/magitrickle-sub)"

TELEGRAM_CIDR_URL = "https://core.telegram.org/resources/cidr.txt"


class V2FlyReader:
    def __init__(self, base_url: str, excluded_attributes: set[str]) -> None:
        self.base_url = base_url.rstrip("/")
        self.excluded_attributes = excluded_attributes
        self.cache: dict[str, set[str]] = {}
        self.active: set[str] = set()

    @staticmethod
    def download_text(url: str) -> str:
        request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            raise RuntimeError(f"HTTP {exc.code}: {url}") from exc
        except (urllib.error.URLError, TimeoutError) as exc:
            raise RuntimeError(f"cannot download {url}: {exc}") from exc

    def fetch(self, category: str) -> str:
        return self.download_text(f"{self.base_url}/{category}")

    def resolve(self, category: str) -> set[str]:
        if category in self.cache:
            return set(self.cache[category])
        if category in self.active:
            raise RuntimeError(f"cyclic v2fly include detected: {category}")

        self.active.add(category)
        result: set[str] = set()

        try:
            text = self.fetch(category)
            for raw_line in text.splitlines():
                line = raw_line.split("#", 1)[0].strip()
                if not line:
                    continue

                parts = line.split()
                token = parts[0]
                attributes = {
                    part[1:].lower()
                    for part in parts[1:]
                    if part.startswith("@") and len(part) > 1
                }
                if attributes & self.excluded_attributes:
                    continue

                if token.startswith("include:"):
                    included = token.removeprefix("include:").strip()
                    if included:
                        result.update(self.resolve(included))
                    continue

                converted = self.convert_rule(token)
                if converted:
                    result.add(converted)
        finally:
            self.active.remove(category)

        self.cache[category] = set(result)
        return result

    @staticmethod
    def convert_rule(token: str) -> str | None:
        token = token.strip()
        if not token:
            return None

        if token.startswith("domain:"):
            return normalize_domain(token.removeprefix("domain:"))

        if token.startswith("full:"):
            return normalize_domain(token.removeprefix("full:"))

        if token.startswith("regexp:"):
            expression = token.removeprefix("regexp:").strip()
            return expression or None

        if token.startswith("keyword:"):
            keyword = token.removeprefix("keyword:").strip()
            return f"*{keyword}*" if keyword else None

        return normalize_domain(token)


def normalize_domain(value: str) -> str | None:
    value = value.strip().lower().rstrip(".")
    if not value:
        return None
    if not re.fullmatch(r"[a-z0-9._-]+", value):
        return None
    return value


def fetch_telegram_cidrs() -> set[str]:
    """Download and validate official Telegram IPv4/IPv6 networks."""
    text = V2FlyReader.download_text(TELEGRAM_CIDR_URL)
    networks: set[str] = set()

    for raw_line in text.splitlines():
        value = raw_line.split("#", 1)[0].strip()
        if not value:
            continue

        try:
            network = ipaddress.ip_network(value, strict=False)
        except ValueError as exc:
            raise RuntimeError(
                f"invalid network in Telegram CIDR source: {value}"
            ) from exc

        # Normalize CIDRs, e.g. remove host bits if the source ever contains them.
        networks.add(network.with_prefixlen)

    if not networks:
        raise RuntimeError("official Telegram CIDR list is empty")

    if not any(":" not in item for item in networks):
        raise RuntimeError("Telegram CIDR list contains no IPv4 networks")

    return networks


def write_subscription(
    name: str,
    rules: set[str],
    source_description: str,
) -> None:
    path = OUTPUT_DIR / f"{name}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)

    header = [
        f"# MagiTrickle subscription: {name}",
        f"# Source: {source_description}",
        f"# Rules: {len(rules)}",
        "# Generated automatically. Do not edit manually.",
        "",
    ]
    path.write_text(
        "\n".join(header + sorted(rules)) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    try:
        config = json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        base_url = config["upstream"]["base_url"]
        subscriptions = config["subscriptions"]
        excluded = {
            str(value).lower()
            for value in config.get("exclude_attributes", [])
        }
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"invalid configuration: {exc}", file=sys.stderr)
        return 1

    reader = V2FlyReader(base_url, excluded)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    generated: set[str] = set()

    try:
        # Domain subscriptions from v2fly.
        for name, definition in subscriptions.items():
            categories = list(definition.get("v2fly", []))
            rules: set[str] = set()

            for category in categories:
                rules.update(reader.resolve(category))

            for item in definition.get("manual", []):
                normalized = normalize_domain(str(item))
                if normalized:
                    rules.add(normalized)

            if not rules:
                raise RuntimeError(f"subscription '{name}' is empty")

            write_subscription(
                name,
                rules,
                "v2fly/domain-list-community: " + ", ".join(categories),
            )
            generated.add(f"{name}.txt")
            print(f"{name}: {len(rules)} domain rules")

        # Separate official Telegram IP subscription.
        telegram_cidrs = fetch_telegram_cidrs()
        write_subscription(
            "telegram-ip",
            telegram_cidrs,
            TELEGRAM_CIDR_URL,
        )
        generated.add("telegram-ip.txt")
        ipv4_count = sum(":" not in item for item in telegram_cidrs)
        ipv6_count = sum(":" in item for item in telegram_cidrs)
        print(
            f"telegram-ip: {len(telegram_cidrs)} CIDRs "
            f"({ipv4_count} IPv4, {ipv6_count} IPv6)"
        )

    except RuntimeError as exc:
        print(f"build failed: {exc}", file=sys.stderr)
        return 2

    # Remove obsolete generated root-level txt files.
    for path in OUTPUT_DIR.glob("*.txt"):
        if path.name not in generated:
            path.unlink()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
