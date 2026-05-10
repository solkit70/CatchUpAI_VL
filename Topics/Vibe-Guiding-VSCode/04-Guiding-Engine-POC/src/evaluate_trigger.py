from __future__ import annotations

import argparse
from pathlib import Path

from common import DATA_DIR, OUTPUT_DIR, normalize, read_json, write_json


def score_rule(context: dict, rule: dict) -> int:
    signal = context.get("problem_signal", {})
    signal_type = signal.get("type", "")
    message = normalize(signal.get("message", ""))
    score = 0

    if signal_type in rule.get("match_types", []):
        score += 60
    for keyword in rule.get("keywords", []):
        if normalize(keyword) in message:
            score += 20
    if rule.get("id") == "auth_required" and context.get("auth_status") in {"logged_out", "unknown"}:
        score += 15
    if rule.get("id") == "cli_missing" and not context.get("gobi_cli_version"):
        score += 25
    return score + int(rule.get("priority", 0))


def evaluate(context: dict, rules: dict) -> dict:
    scored = [
        {
            "rule_id": rule["id"],
            "guide_type": rule["guide_type"],
            "reason": rule["reason"],
            "score": score_rule(context, rule),
        }
        for rule in rules.get("rules", [])
    ]
    scored.sort(key=lambda item: item["score"], reverse=True)
    selected = scored[0] if scored else {
        "rule_id": "unknown",
        "guide_type": "fallback",
        "reason": "No trigger rule matched.",
        "score": 0,
    }
    return {
        "problem_signal": context.get("problem_signal", {}),
        "selected_rule": selected,
        "candidates": scored[:5],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate trigger rules.")
    parser.add_argument("--context", type=Path, default=OUTPUT_DIR / "user_context.json")
    parser.add_argument("--rules", type=Path, default=DATA_DIR / "trigger_rules.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "trigger_decision.json")
    args = parser.parse_args()

    decision = evaluate(read_json(args.context), read_json(args.rules))
    write_json(args.output, decision)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
