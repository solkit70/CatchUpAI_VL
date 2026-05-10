from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from common import DATA_DIR, OUTPUT_DIR, read_json, write_json, write_text  # noqa: E402
from compose_guide import compose  # noqa: E402
from evaluate_trigger import evaluate  # noqa: E402
from retrieve_manual import retrieve  # noqa: E402


def expected_manual(scenario_id: str) -> str:
    return {
        "cli_missing": "gobi-cli-install",
        "auth_required": "gobi-cli-auth-status",
        "space_post_blocked": "gobi-cli-space-create-post",
        "desktop_custom_homepage_blocked": "gobi-desktop-applet-context-check",
        "version_mismatch": "gobi-cli-environment-version-check",
    }[scenario_id]


def main() -> None:
    contexts = read_json(DATA_DIR / "test_contexts.json")
    rules = read_json(DATA_DIR / "trigger_rules.json")
    index = read_json(DATA_DIR / "retrieval_index.json")
    results = []

    for context in contexts:
        scenario_id = context["id"]
        scenario_dir = OUTPUT_DIR / "scenarios" / scenario_id
        decision = evaluate(context, rules)
        retrieval = retrieve(context, decision, index)
        guide = compose(context, decision, retrieval)

        selected_manual = retrieval["selected_manual"]["manual_id"]
        passed = selected_manual == expected_manual(scenario_id)
        result = {
            "id": scenario_id,
            "passed": passed,
            "selected_rule": decision["selected_rule"]["rule_id"],
            "selected_manual": selected_manual,
            "expected_manual": expected_manual(scenario_id),
        }
        results.append(result)

        write_json(scenario_dir / "user_context.json", context)
        write_json(scenario_dir / "trigger_decision.json", decision)
        write_json(scenario_dir / "retrieval_result.json", retrieval)
        write_text(scenario_dir / "guide_response.md", guide)

    write_json(OUTPUT_DIR / "test_results.json", results)
    failed = [item for item in results if not item["passed"]]
    print(f"Scenarios passed: {len(results) - len(failed)}/{len(results)}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
