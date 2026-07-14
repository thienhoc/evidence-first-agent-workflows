#!/usr/bin/env python3
"""Dependency-free validator for the public evidence-first record examples."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def read(folder: Path, name: str) -> dict:
    path = folder / name
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{name}: {exc}")
    if not isinstance(value, dict):
        fail(f"{name}: root must be an object")
    return value


def require(record: dict, fields: tuple[str, ...], name: str) -> None:
    for field in fields:
        if not record.get(field):
            fail(f"{name}: missing {field}")


def main() -> int:
    folder = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("examples")
    capsule = read(folder, "capsule.json")
    checkpoint = read(folder, "checkpoint.json")
    execution = read(folder, "execution-record.json")

    require(capsule, ("id", "objective", "workstream", "sourceBoundary", "evidenceCeiling"), "capsule")
    require(checkpoint, ("capsuleId", "state", "nextAction", "updatedAt"), "checkpoint")
    require(execution, ("capsuleId", "verdict", "command", "artifacts"), "execution-record")

    if checkpoint["capsuleId"] != capsule["id"] or execution["capsuleId"] != capsule["id"]:
        fail("capsuleId does not match the capsule")
    if checkpoint["state"] not in {"READY", "IN_PROGRESS", "BLOCKED", "RESUME_OK", "DONE"}:
        fail("checkpoint state is invalid")
    if execution["verdict"] not in {"PASS", "FAIL", "BLOCKED", "PROPOSAL"}:
        fail("execution verdict is invalid")

    artifact_ids = [artifact.get("id") for artifact in execution["artifacts"]]
    if any(not artifact_id for artifact_id in artifact_ids):
        fail("every artifact needs an id")
    if len(artifact_ids) != len(set(artifact_ids)):
        fail("duplicate artifact id")
    if any("/Users/" in artifact.get("path", "") or "token" in artifact.get("path", "").lower() for artifact in execution["artifacts"]):
        fail("private-looking artifact path")

    print("PASS: 3 records validated; no duplicate artifact IDs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
