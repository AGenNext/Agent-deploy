#!/usr/bin/env python3
"""Deployment gate — validates all required conditions before a deploy proceeds."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("ERROR: PyYAML required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]

MATURITY_THRESHOLDS = {
    "dev": 0.0,       # gates 1-3 only in dev
    "staging": 0.5,
    "prod": 0.9,
}

REQUIRED_PROTOCOLS = [
    "protocols/deployment-protocol.md",
    "protocols/release-protocol.md",
    "contracts/deployment-contract.md",
]

REQUIRED_RUNBOOKS = [
    "runbooks/install-microk8s.md",
]


def fail(msg: str) -> None:
    print(f"GATE FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def check_protocols() -> None:
    print("Checking protocol documents...")
    for path in REQUIRED_PROTOCOLS + REQUIRED_RUNBOOKS:
        full = ROOT / path
        if not full.exists():
            fail(f"Missing required document: {path}")
        ok(path)


def check_release_contracts() -> None:
    print("Checking release contracts...")
    for contract_path in (ROOT / "release").glob("*.release.yaml"):
        data = yaml.safe_load(contract_path.read_text())
        release = data.get("release", {})
        gates = release.get("gates", [])
        if not gates:
            fail(f"{contract_path.name}: no gates defined")
        for gate in gates:
            if gate.get("required") and not gate.get("command"):
                fail(f"{contract_path.name}: gate '{gate['name']}' is required but has no command")
        ok(contract_path.name)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", required=True, choices=["dev", "staging", "prod"])
    parser.add_argument("--version", required=True)
    args = parser.parse_args()

    print(f"\nDeployment gate: env={args.env} version={args.version}\n")

    check_protocols()
    check_release_contracts()

    print(f"\nAll deployment gate checks passed for {args.env}.")


if __name__ == "__main__":
    main()
