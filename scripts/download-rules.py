#!/usr/bin/env python3
"""Download upstream rule sets; never modify rules/ALan.yaml or rules/myProxy_ip.yaml."""

from __future__ import annotations

import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

RULES = {
    "private.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/private.yaml",
    "cn.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/cn.yaml",
    "not-cn.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/geolocation-!cn.yaml",
    "ai.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-ai-chat-!cn.yaml",
    "github.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/github.yaml",
    "youtube.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/youtube.yaml",
    "google.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/google.yaml",
    "microsoft.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/microsoft.yaml",
    "telegram.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/telegram.yaml",
    "netflix.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/netflix.yaml",
    "tiktok.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/tiktok.yaml",
    "apple-cn.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/apple@cn.yaml",
    "category-games.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-games.yaml",
    "category-porn.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geosite/category-porn.yaml",
    "cn-ip.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/cn.yaml",
    "google-ip.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/google.yaml",
    "netflix-ip.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/netflix.yaml",
    "telegram-ip.yaml": "https://testingcf.jsdelivr.net/gh/MetaCubeX/meta-rules-dat@meta/geo/geoip/telegram.yaml",
}

def download(url: str, retries: int = 3) -> str | None:
    for attempt in range(1, retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=60) as resp:
                return resp.read().decode("utf-8")
        except (urllib.error.URLError, TimeoutError, UnicodeDecodeError) as exc:
            print(f"[WARN] {attempt}/{retries}: {exc}", file=sys.stderr)
            if attempt < retries:
                time.sleep(2)
    print(f"[ERROR] download failed: {url}", file=sys.stderr)
    return None

def main() -> int:
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "rules")
    output.mkdir(parents=True, exist_ok=True)
    failed = 0
    for filename, url in RULES.items():
        content = download(url)
        if content is None:
            failed += 1
            continue
        (output / filename).write_text(content, encoding="utf-8", newline="\n")
        print(f"[OK] {filename}")
    # Personal files are intentionally not listed in RULES and are never touched.
    return 1 if failed else 0

if __name__ == "__main__":
    raise SystemExit(main())
