#!/usr/bin/env python3
"""Validate Agent-deploy release contracts.

This keeps release/*.release.yaml enforceable by checking required gates and publish rules.
"""

from __future__ import annotations

from pathlib import Path
import sys

try:
    import yaml
except ImportError as exc:
    raise SystemExit("ERROR: PyYAML is required: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "release" / "creativework.release.yaml"
REQUIRED_GATES = ["vocabulary", "grammar", "graph", "review", "commit", "deploy"]
REQUIRED_FIELDS = ["canonical_id", "version", "status", "schema_type", "source_path"]


def fail(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def main() -> None:
    if not CONTRACT.exists():
        fail(f"missing {CONTRACT.relative_to(ROOT)}")

    data = yaml.safe_load(CONTRACT.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail("release contract root must be an object")

    release = data.get("release")
    if not isinstance(release, dict):
        fail("release object is required")

    if release.get("artifact_type") != "schema:CreativeWork":
        fail("artifact_type must be schema:CreativeWork")

    fields = release.get("required_fields")
    if not isinstance(fields, list):
        fail("required_fields must be a list")
    for field in REQUIRED_FIELDS:
        if field not in fields:
            fail(f"required_fields missing {field}")

    gates = release.get("gates")
    if not isinstance(gates, list):
        fail("gates must be a list")

    gate_by_name = {gate.get("name"): gate for gate in gates if isinstance(gate, dict)}
    for gate_name in REQUIRED_GATES:
        gate = gate_by_name.get(gate_name)
        if not gate:
            fail(f"missing required gate {gate_name}")
        if gate.get("required") is not True:
            fail(f"gate {gate_name} must be required")
        if not gate.get("owner"):
            fail(f"gate {gate_name} missing owner")
        if not gate.get("command"):
            fail(f"gate {gate_name} missing command")
        if not gate.get("output"):
            fail(f"gate {gate_name} missing output")

    publish = release.get("publish")
    if not isinstance(publish, dict):
        fail("publish object is required")
    if publish.get("requires_all_gates") is not True:
        fail("publish.requires_all_gates must be true")

    print(f"ok: {CONTRACT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
