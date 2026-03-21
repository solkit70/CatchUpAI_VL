#!/usr/bin/env python3
"""
translate-claude.py
Translates changes in CLAUDE.md to CLAUDE.en.md using Claude API.

Called automatically by the pre-commit hook when CLAUDE.md is staged.

Requirements:
  - ANTHROPIC_API_KEY environment variable set
  - pip install anthropic

Usage (manual):
  python scripts/translate-claude.py
"""

import os
import subprocess
import sys


def get_repo_root():
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout.strip()


def get_staged_diff(filename):
    """Get the staged diff for a specific file."""
    result = subprocess.run(
        ["git", "diff", "--cached", filename],
        capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    # Always write with LF line endings (UTF-8 without BOM)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def main():
    # ── 1. Check API key ──────────────────────────────────────────────────────
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("⚠️  ANTHROPIC_API_KEY is not set.")
        print("   Auto-translation skipped. Please manually update CLAUDE.en.md.")
        print("   To enable auto-translation:")
        print("     Windows: $env:ANTHROPIC_API_KEY = 'sk-ant-...'")
        print("     Or add it to your system environment variables permanently.")
        sys.exit(1)

    # ── 2. Check anthropic package ────────────────────────────────────────────
    try:
        import anthropic
    except ImportError:
        print("❌ 'anthropic' package is not installed.")
        print("   Run: pip install anthropic")
        sys.exit(1)

    # ── 3. Get staged diff ────────────────────────────────────────────────────
    diff = get_staged_diff("CLAUDE.md")
    if not diff.strip():
        print("ℹ️  No staged changes in CLAUDE.md. Skipping translation.")
        sys.exit(0)

    # ── 4. Read source files ──────────────────────────────────────────────────
    repo_root = get_repo_root()
    claude_md_path = os.path.join(repo_root, "CLAUDE.md")
    claude_en_path = os.path.join(repo_root, "CLAUDE.en.md")

    kr_content = read_file(claude_md_path)
    en_content = read_file(claude_en_path)

    # ── 5. Call Claude API ────────────────────────────────────────────────────
    print("   Calling Claude API...")
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are updating the English version (CLAUDE.en.md) of a Korean AI system prompt file (CLAUDE.md).

## Task
The Korean CLAUDE.md has been modified. Update CLAUDE.en.md to reflect these changes.

## Rules
1. Only translate/update the parts that CHANGED (shown in the diff below with + lines)
2. Keep existing English text in CLAUDE.en.md unchanged where there are NO Korean changes
3. Maintain the same English writing style and terminology as the existing CLAUDE.en.md
4. Keep technical terms as-is: VibeLearn AI, WorkLog, DoD, Retrospective, topic_info.md,
   vl_prompts, vl_roadmap, vl_worklog, vl_materials, YYYYMMDD, etc.
5. File path conventions: Korean uses .md, English uses .en.md (e.g., roadmap_prompt.en.md)
6. Return ONLY the complete updated CLAUDE.en.md content — no explanations, no markdown fences

## Git diff of CLAUDE.md (changes to incorporate)
{diff}

## Current CLAUDE.en.md (base to update)
{en_content}

## Current CLAUDE.md full content (context only)
{kr_content}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8192,
        messages=[{"role": "user", "content": prompt}]
    )

    updated_en = response.content[0].text.strip()

    # ── 6. Sanity check ───────────────────────────────────────────────────────
    if len(updated_en) < len(en_content) * 0.5:
        print("❌ Translation result is suspiciously short. Aborting to be safe.")
        print(f"   Original: {len(en_content)} chars, Result: {len(updated_en)} chars")
        sys.exit(1)

    # ── 7. Write result ───────────────────────────────────────────────────────
    write_file(claude_en_path, updated_en)
    print("   ✅ CLAUDE.en.md updated successfully.")
    sys.exit(0)


if __name__ == "__main__":
    main()
