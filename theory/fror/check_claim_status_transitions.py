#!/usr/bin/env python3
"""Validate FROR claim status transitions from YAML files."""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    print("ERROR: Missing dependency 'PyYAML'.")
    print("Install with: python3 -m pip install --user PyYAML")
    raise SystemExit(2) from exc

STATUS_ORDER = ["Conjecture", "Protocol", "Validated", "Core"]
STATUS_IDX = {name: i for i, name in enumerate(STATUS_ORDER)}


def parse_registry(path: Path) -> dict[str, str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    claims: dict[str, str] = {}
    for item in data.get("claims", []):
        if not isinstance(item, dict):
            continue
        claim_id = item.get("claim_id")
        status = item.get("status")
        if isinstance(claim_id, str) and isinstance(status, str):
            claims[claim_id] = status
    return claims


def parse_event_log(path: Path) -> dict[str, list[dict[str, str]]]:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for item in data.get("events", []):
        if not isinstance(item, dict):
            continue
        claim_id = item.get("claim_id")
        if not isinstance(claim_id, str):
            continue
        event: dict[str, str] = {}
        for key in ("event_id", "event_type", "from_status", "to_status", "timestamp"):
            val = item.get(key)
            if isinstance(val, str):
                event[key] = val
        grouped[claim_id].append(event)
    return grouped


def validate(registry: dict[str, str], event_log: dict[str, list[dict[str, str]]]) -> list[str]:
    errors: list[str] = []

    for claim_id, target_status in registry.items():
        events = event_log.get(claim_id, [])
        if not events:
            errors.append(f"{claim_id}: missing events")
            continue

        prev_status: str | None = None
        for i, ev in enumerate(events, start=1):
            ev_type = ev.get("event_type", "")
            to_status = ev.get("to_status")
            from_status = ev.get("from_status")

            if to_status not in STATUS_IDX:
                errors.append(f"{claim_id}#{i}: unknown to_status={to_status!r}")
                continue

            if ev_type != "Claim.Override":
                if prev_status is None:
                    if to_status != "Conjecture":
                        errors.append(
                            f"{claim_id}#{i}: first transition must end in Conjecture, got {to_status}"
                        )
                    if from_status not in (None, "", "null"):
                        errors.append(
                            f"{claim_id}#{i}: first transition must not have from_status={from_status}"
                        )
                else:
                    if from_status and from_status != prev_status:
                        errors.append(
                            f"{claim_id}#{i}: from_status={from_status} does not match previous={prev_status}"
                        )
                    delta = STATUS_IDX[to_status] - STATUS_IDX[prev_status]
                    if delta < 0:
                        errors.append(
                            f"{claim_id}#{i}: backward transition {prev_status}->{to_status} is not allowed"
                        )
                    elif delta > 1:
                        errors.append(
                            f"{claim_id}#{i}: skip-level transition {prev_status}->{to_status} is not allowed"
                        )

            prev_status = to_status

        if prev_status != target_status:
            errors.append(
                f"{claim_id}: registry status={target_status}, derived status={prev_status}"
            )

    for claim_id in event_log:
        if claim_id not in registry:
            errors.append(f"{claim_id}: present in event log but absent in registry")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate FROR claim status transitions")
    parser.add_argument(
        "--registry",
        default="claims_registry.yaml",
        help="Path to claims_registry.yaml",
    )
    parser.add_argument(
        "--events",
        default="claim_event_log.yaml",
        help="Path to claim_event_log.yaml",
    )
    args = parser.parse_args()

    reg_path = Path(args.registry)
    ev_path = Path(args.events)

    registry = parse_registry(reg_path)
    event_log = parse_event_log(ev_path)
    errors = validate(registry, event_log)

    if errors:
        print("FAIL")
        for e in errors:
            print(f"- {e}")
        return 1

    print("OK")
    print(f"validated_claims={len(registry)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
