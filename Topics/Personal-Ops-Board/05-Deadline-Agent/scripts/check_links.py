"""Check relative Markdown links within the M5 module learning materials."""
from __future__ import annotations

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlparse

MODULE = Path(__file__).resolve().parents[1]
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check(root: Path = MODULE) -> list[str]:
    errors = []
    for source in sorted(root.rglob("*.md")):
        content = source.read_text(encoding="utf-8")
        for raw in LINK.findall(content):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            parsed = urlparse(target)
            if parsed.scheme or target.startswith("#"):
                continue
            destination = (source.parent / unquote(parsed.path)).resolve()
            if not destination.is_file():
                errors.append(f"{source.relative_to(root).as_posix()}: {target}")
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("Broken local Markdown links:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    count = len(list(MODULE.rglob("*.md")))
    print(f"M5 links checked: {count} Markdown files; broken links=0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
