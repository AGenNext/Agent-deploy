#!/usr/bin/env python3
"""Post-deploy smoke tests for Agent Platform."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
import urllib.error

ENV_URLS = {
    "dev": "http://localhost:8001",
    "staging": "https://staging-api.agennext.com",
    "prod": "https://api.agennext.com",
}


def get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=10) as r:
        return json.loads(r.read())


def post(url: str, body: dict) -> dict:
    data = json.dumps(body).encode()
    req = urllib.request.Request(
        url, data=data,
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read())


def fail(msg: str) -> None:
    print(f"SMOKE FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", required=True, choices=["dev", "staging", "prod"])
    args = parser.parse_args()

    base = ENV_URLS[args.env]
    print(f"\nSmoke test: {args.env} ({base})\n")

    # Gate 1: Health
    try:
        h = get(f"{base}/health")
    except Exception as e:
        fail(f"Health endpoint unreachable: {e}")

    if h.get("status") != "ok":
        fail(f"Health status not ok: {h}")
    ok(f"health — status={h['status']} db={h.get('db')}")

    if h.get("db") != "connected":
        fail(f"DB not connected: {h.get('db')}")
    ok("SurrealDB connected")

    # Gate 2: Objective run
    try:
        result = post(f"{base}/objectives/run", {
            "goal": "smoke test objective",
            "priority": 1,
        })
    except Exception as e:
        fail(f"Objective run failed: {e}")

    obj = result.get("objective", {})
    if obj.get("status") not in ("completed", "running"):
        fail(f"Unexpected objective status: {obj.get('status')}")
    ok(f"objective run — status={obj.get('status')}")

    print(f"\nAll smoke tests passed for {args.env}.")


if __name__ == "__main__":
    main()
