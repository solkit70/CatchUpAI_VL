from __future__ import annotations

import argparse
from pathlib import Path

from common import DATA_DIR, OUTPUT_DIR, normalize, read_json, write_json


def score_entry(context: dict, decision: dict, entry: dict) -> int:
    signal = context.get("problem_signal", {})
    message = normalize(signal.get("message", ""))
    signal_type = signal.get("type", "")
    guide_type = decision.get("selected_rule", {}).get("guide_type")
    score = int(entry.get("priority", 0))

    if guide_type == entry.get("guide_type"):
        score += 50
    if signal_type in entry.get("problem_signals", []):
        score += 50
    for command in entry.get("commands", []):
        if normalize(command) in message:
            score += 30
    for term in entry.get("deprecated_terms", []):
        if normalize(term) in message:
            score += 30
    for goal in entry.get("user_goals", []):
        if normalize(goal) in message:
            score += 20
    if context.get("gobi_cli_version") and "v2.0.12" in entry.get("version_scope", ""):
        score += 15
    return score


def retrieve(context: dict, decision: dict, index: dict) -> dict:
    scored = []
    for entry in index.get("entries", []):
        item = dict(entry)
        item["score"] = score_entry(context, decision, entry)
        scored.append(item)
    scored.sort(key=lambda item: item["score"], reverse=True)

    selected = scored[0] if scored else None
    return {
        "selected_manual": selected,
        "candidates": scored[:5],
        "index_version": index.get("index_version"),
        "source_version": index.get("source_version"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Retrieve matching manual entries.")
    parser.add_argument("--context", type=Path, default=OUTPUT_DIR / "user_context.json")
    parser.add_argument("--decision", type=Path, default=OUTPUT_DIR / "trigger_decision.json")
    parser.add_argument("--index", type=Path, default=DATA_DIR / "retrieval_index.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "retrieval_result.json")
    args = parser.parse_args()

    result = retrieve(read_json(args.context), read_json(args.decision), read_json(args.index))
    write_json(args.output, result)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
