#!/usr/bin/env python3
"""Check GitHub repository links using authenticated, cached Git tree metadata."""
import json
import re
import subprocess
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=None)
def api(endpoint):
    result = subprocess.run(
        ["gh", "api", endpoint], capture_output=True, text=True, timeout=30
    )
    if result.returncode:
        raise RuntimeError("GitHub metadata access failed: " + endpoint)
    return json.loads(result.stdout)


def check(url):
    parts = [unquote(p) for p in urlsplit(url).path.strip("/").split("/")]
    if len(parts) == 1:
        api("orgs/" + parts[0])
        return
    repository = "/".join(parts[:2])
    metadata = api("repos/" + repository)
    if len(parts) == 2:
        return
    if parts[2] not in {"blob", "tree"} or len(parts) < 4:
        raise RuntimeError("Unsupported GitHub link form: " + url)
    tail = "/".join(parts[3:])
    default = metadata["default_branch"]
    if tail == default or tail.startswith(default + "/"):
        ref = default
        target = tail[len(default):].lstrip("/")
    else:
        ref = parts[3]
        target = "/".join(parts[4:])
    commit = api("repos/" + repository + "/commits/" + quote(ref, safe=""))
    tree = api("repos/" + repository + "/git/trees/" + commit["sha"] + "?recursive=1")
    if tree.get("truncated"):
        raise RuntimeError("Truncated GitHub tree cannot prove link: " + url)
    entries = {entry["path"]: entry["type"] for entry in tree["tree"]}
    if not target and parts[2] == "tree":
        return
    expected = "blob" if parts[2] == "blob" else "tree"
    if entries.get(target) != expected:
        raise RuntimeError("Missing GitHub target: " + url)


def main():
    links = set()
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts or "node_modules" in file.parts:
            continue
        links.update(re.findall(r'https://github\.com/[^\s<>"`)]+', file.read_text()))
    for url in sorted(links):
        check(url)
    print(f"Validated {len(links)} GitHub links using authenticated repository metadata.")


if __name__ == "__main__":
    main()
