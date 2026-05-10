from __future__ import annotations

import argparse
import platform
import subprocess
from pathlib import Path

from common import DATA_DIR, OUTPUT_DIR, read_json, write_json


def run_command(args: list[str]) -> dict:
    try:
        result = subprocess.run(args, capture_output=True, text=True, timeout=8, check=False)
        return {
            "ok": result.returncode == 0,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except FileNotFoundError:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": "command not found"}
    except subprocess.TimeoutExpired:
        return {"ok": False, "returncode": None, "stdout": "", "stderr": "command timed out"}


def collect_from_system(sample: dict | None = None) -> dict:
    sample = sample or {}
    gobi_version = run_command(["gobi", "--version"])
    auth_status = run_command(["gobi", "auth", "status"]) if gobi_version["ok"] else None
    space_list = run_command(["gobi", "space", "list"]) if gobi_version["ok"] else None

    context = {
        "os": f"{platform.system()} {platform.release()}".strip(),
        "python_version": platform.python_version(),
        "user_level": sample.get("user_level", "beginner"),
        "gobi_cli_version": sample.get("gobi_cli_version") or (gobi_version["stdout"] if gobi_version["ok"] else None),
        "auth_status": sample.get("auth_status") or ("authenticated" if auth_status and auth_status["ok"] else "unknown"),
        "active_space": sample.get("active_space"),
        "available_commands": sample.get("available_commands", []),
        "problem_signal": sample.get("problem_signal", {"type": "unknown", "message": ""}),
        "raw_checks": {
            "gobi_version": gobi_version,
            "auth_status": auth_status,
            "space_list": space_list,
        },
    }
    return context


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect or copy user context for Vibe Guiding POC.")
    parser.add_argument("--sample", type=Path, default=DATA_DIR / "user_context.sample.json")
    parser.add_argument("--output", type=Path, default=OUTPUT_DIR / "user_context.json")
    parser.add_argument("--system", action="store_true", help="Try to collect live system data.")
    args = parser.parse_args()

    sample = read_json(args.sample)
    context = collect_from_system(sample) if args.system else sample
    write_json(args.output, context)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
