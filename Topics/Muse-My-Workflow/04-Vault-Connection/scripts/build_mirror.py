#!/usr/bin/env python3
"""Build a one-way Markdown mirror. Preview is the default; --apply copies files."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass
class Decision:
    path: str
    action: str
    reason: str
    count: int = 1


def relative_path(path: Path) -> str:
    value = path.as_posix()
    return value[2:] if value.startswith("./") else value


def parse_visibility(text: str) -> str | None:
    """Read a top-level YAML visibility scalar without requiring a YAML library."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None
    match = re.search(r"(?m)^---\s*$", text[4:])
    if not match:
        return None
    frontmatter = text[4 : 4 + match.start()]
    value = re.search(r"(?mi)^visibility\s*:\s*[\"']?([^\"'\s#]+)", frontmatter)
    return value.group(1).strip().lower() if value else None


def is_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def load_config(config_path: Path) -> dict:
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            "Config must use JSON syntax (which is also valid YAML); "
            f"could not parse {config_path.name}: {exc}"
        ) from exc
    if not isinstance(config, dict):
        raise ValueError("Config root must be an object")
    base = config_path.resolve().parent
    for key in ("source_root", "destination_root"):
        if not config.get(key):
            raise ValueError(f"Missing required config key: {key}")
        value = Path(config[key])
        config[key] = (base / value).resolve() if not value.is_absolute() else value.resolve()
    config.setdefault("include_paths", ["."])
    config.setdefault("exclude_paths", [".git", ".obsidian", "node_modules", "_Inbox_"])
    config.setdefault("allowed_extensions", [".md"])
    config.setdefault("allowed_visibility", ["public"])
    config.setdefault("max_file_bytes", 1_048_576)
    config["include_paths"] = [relative_path(Path(p)) for p in config["include_paths"]]
    config["exclude_paths"] = [relative_path(Path(p)) for p in config["exclude_paths"]]
    config["allowed_extensions"] = [str(ext).lower() for ext in config["allowed_extensions"]]
    config["allowed_visibility"] = [str(value).lower() for value in config["allowed_visibility"]]
    config["max_file_bytes"] = int(config["max_file_bytes"])
    return config


def matches_prefix(path: str, prefixes: list[str]) -> bool:
    return any(prefix in ("", ".") or path == prefix or path.startswith(prefix + "/") for prefix in prefixes)


def excluded_by_path(path: str, excluded: list[str]) -> bool:
    path_parts = [part.casefold() for part in Path(path).parts]
    for item in excluded:
        excluded_parts = [part.casefold() for part in Path(item).parts]
        if not excluded_parts:
            continue
        for offset in range(len(path_parts) - len(excluded_parts) + 1):
            if path_parts[offset : offset + len(excluded_parts)] == excluded_parts:
                return True
    return False


def classify(path: Path, rel: str, config: dict) -> tuple[str, str]:
    if path.is_symlink():
        return "EXCLUDE", "symbolic link"
    if not matches_prefix(rel, config["include_paths"]):
        return "EXCLUDE", "outside included paths"
    if excluded_by_path(rel, config["exclude_paths"]):
        return "EXCLUDE", "excluded path"
    if path.suffix.lower() not in config["allowed_extensions"]:
        return "EXCLUDE", "file type not allowed"
    size = path.stat().st_size
    if size > config["max_file_bytes"]:
        return "EXCLUDE", f"over size limit ({size} bytes)"
    try:
        content = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return "EXCLUDE", "not readable as UTF-8 text"
    if "🔒 내부 자료" in content:
        return "EXCLUDE", "internal marker"
    visibility = parse_visibility(content)
    if visibility == "internal":
        return "EXCLUDE", "visibility: internal"
    if visibility not in config["allowed_visibility"]:
        reason = f"visibility not allowed ({visibility})" if visibility else "missing visibility"
        return "EXCLUDE", reason
    return "INCLUDE", f"visibility: {visibility}"


def build_report(
    decisions: list[Decision], mode: str, source: Path, destination: Path, visibility: str
) -> str:
    included = sum(item.count for item in decisions if item.action == "INCLUDE")
    excluded = sum(item.count for item in decisions if item.action == "EXCLUDE")
    skipped = sum(item.count for item in decisions if item.action == "SKIP")
    exclusions: dict[tuple[str, str], int] = {}
    for item in decisions:
        if item.action != "INCLUDE":
            key = (item.action, item.reason)
            exclusions[key] = exclusions.get(key, 0) + item.count
    now = datetime.now().astimezone()
    lines = [
        "---",
        'title: "사본 미리 보기 보고서"',
        "author:",
        "  - Codex",
        f"created: {now.strftime('%Y-%m-%d %H:%M:%S')}",
        f"visibility: {visibility}",
        "tags:",
        "  - muse-my-workflow",
        "  - mirror-preview",
        "---",
        "",
        "# Mirror preview report",
        "",
        f"- Mode: **{mode}**",
        f"- Generated: {now.isoformat(timespec='minutes')}",
        f"- Source: `{source.name}`",
        f"- Destination: `{destination.name}`",
        f"- Include candidates: **{included}**",
        f"- Excluded: **{excluded}**",
        f"- Skipped: **{skipped}**",
        "",
        "| Relative path | Decision | Reason |",
        "|---|---|---|",
    ]
    for item in decisions:
        if item.action != "INCLUDE":
            continue
        safe_path = item.path.replace("|", "\\|")
        lines.append(f"| `{safe_path}` | {item.action} | {item.reason} |")
    for (action, reason), count in sorted(exclusions.items()):
        noun = "file" if count == 1 else "files"
        label = "excluded" if action == "EXCLUDE" else "skipped"
        lines.append(f"| `({count} {label} {noun})` | {action} | {reason} |")
    if not decisions:
        lines.append("| _(none)_ | EXCLUDE | no files found |")
    lines.extend(["", "No file contents are included in this report.", ""])
    return "\n".join(lines)


def run(
    config: dict,
    apply: bool,
    report_path: Path | None,
    overwrite: bool,
    report_visibility: str = "internal",
) -> list[Decision]:
    source: Path = config["source_root"]
    destination: Path = config["destination_root"]
    if not source.is_dir():
        raise ValueError(f"Source root does not exist or is not a directory: {source}")
    if source == destination or is_under(destination, source) or is_under(source, destination):
        raise ValueError("Source and destination must be separate sibling/independent directories")

    decisions: list[Decision] = []
    non_markdown = 0
    for path in source.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in config["allowed_extensions"]:
            non_markdown += 1
            continue
        rel = path.relative_to(source).as_posix()
        action, reason = classify(path, rel, config)
        if action == "INCLUDE" and apply:
            target = destination / Path(rel)
            if target.exists() and not overwrite:
                action, reason = "SKIP", "destination already exists; not overwritten"
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(path, target)
                reason = "copied"
        decisions.append(Decision(rel, action, reason))
    if non_markdown:
        label = "non-Markdown files" if non_markdown != 1 else "non-Markdown file"
        decisions.append(
            Decision(f"({non_markdown} {label})", "EXCLUDE", "file type not allowed", non_markdown)
        )
    decisions.sort(key=lambda item: item.path.casefold())

    if report_path:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(
            build_report(
                decisions,
                "APPLY" if apply else "PREVIEW ONLY",
                source,
                destination,
                report_visibility,
            ),
            encoding="utf-8",
        )
    return decisions


def demo_config(root: Path) -> dict:
    source = root / "synthetic-vault"
    destination = root / "synthetic-mirror"
    samples = {
        "public/guide.md": "---\ntitle: Guide\nvisibility: public\n---\nPublic sample.\n",
        "personal/journal.md": "---\nvisibility: personal\n---\nPersonal sample.\n",
        "internal/policy.md": "---\nvisibility: internal\n---\nInternal sample.\n",
        "unknown/note.md": "# No visibility marker\n",
        "media/clip.mp4": "synthetic media placeholder\n",
    }
    for name, content in samples.items():
        path = source / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    return {
        "source_root": source,
        "destination_root": destination,
        "include_paths": ["."],
        "exclude_paths": [".git", ".obsidian", "node_modules", "_Inbox_"],
        "allowed_extensions": [".md"],
        "allowed_visibility": ["public"],
        "max_file_bytes": 1_048_576,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, help="JSON-syntax YAML config file")
    parser.add_argument("--demo", action="store_true", help="run a safe preview over temporary fictional files")
    parser.add_argument("--report", type=Path, help="write a Markdown report to this path")
    parser.add_argument("--apply", action="store_true", help="copy approved files; preview is the default")
    parser.add_argument("--overwrite", action="store_true", help="allow replacing existing destination files")
    args = parser.parse_args()
    try:
        report_path = args.report.resolve() if args.report else None
        if args.demo:
            if args.config or args.apply or args.overwrite:
                raise ValueError("--demo cannot be combined with --config, --apply, or --overwrite")
            with tempfile.TemporaryDirectory(prefix="m4-preview-demo-") as tmp:
                decisions = run(demo_config(Path(tmp)), False, report_path, False, "public")
        else:
            if not args.config:
                raise ValueError("Provide --config or use --demo")
            config = load_config(args.config.resolve())
            decisions = run(config, args.apply, report_path, args.overwrite)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    included = sum(item.count for item in decisions if item.action == "INCLUDE")
    excluded = sum(item.count for item in decisions if item.action == "EXCLUDE")
    copied = sum(item.count for item in decisions if item.reason == "copied")
    print(f"Mode: {'APPLY' if args.apply else 'PREVIEW ONLY'}")
    print(f"Include candidates: {included}; excluded: {excluded}; copied: {copied}")
    exclusions: dict[tuple[str, str], int] = {}
    for item in decisions:
        if item.action != "INCLUDE":
            key = (item.action, item.reason)
            exclusions[key] = exclusions.get(key, 0) + item.count
    for (action, reason), count in sorted(exclusions.items()):
        print(f"{action} {count} | {reason}")
    if report_path:
        print(f"Report: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
