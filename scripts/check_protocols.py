#!/usr/bin/env python3
"""Check that all required protocol and runbook documents exist."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "protocols/deployment-protocol.md",
    "protocols/release-protocol.md",
    "contracts/deployment-contract.md",
    "runbooks/install-microk8s.md",
    "release/creativework.release.yaml",
]


def main() -> None:
    errors = []
    for path in REQUIRED:
        full = ROOT / path
        if not full.exists():
            errors.append(f"missing: {path}")
        else:
            print(f"  ok: {path}")

    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    print("\nAll protocol documents present.")


if __name__ == "__main__":
    main()
