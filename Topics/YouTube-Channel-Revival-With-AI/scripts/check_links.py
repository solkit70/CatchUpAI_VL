#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""문서의 상대 링크가 실제 파일을 가리키는지 확인한다 — **모듈을 닫을 때 돌린다.**

왜 필요한가 (2026-09-10 실제 사고):
    M1 의 README 를 **로드맵의 「계획된 산출물」에서 그대로 옮겨 써 놓고**
    실제로 만든 것과 대조하지 않았다. 계획에만 있던 `concepts/*.md` 두 개를
    끝내 쓰지 않았는데 README 는 그대로 링크하고 있었다.

    로컬에서는 **빈 폴더**라 눈에 잘 안 띄었고, 빈 폴더는 git 이 추적하지 않으므로
    **GitHub 에서는 폴더 자체가 사라져** 「없는 페이지」로 보였다.
    채널 주인이 GitHub 에서 읽다가 발견했다.

쓰는 법:

    python scripts/check_links.py            # 이 토픽 전체
    python scripts/check_links.py <경로>      # 다른 폴더
    python scripts/check_links.py --all      # 템플릿 자리표시자까지 전부 보기

깨진 링크가 있으면 **종료 코드 1** 로 끝난다 — 다른 스크립트에서 이어 붙일 수 있다.
"""
from __future__ import annotations

import os
import re
import sys
import urllib.parse

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

# `[텍스트](경로)` — 외부 URL·앵커는 건너뛴다
#
# 🔴 괄호를 **한 겹까지 허용**한다. 파일명에 괄호가 들어가는 일이 실제로 있다 —
#    `KWA - In-Home Caregiver Job Description (2022-08-22).pdf`
#    `[^)]+` 로만 잡으면 `(2022-08-22` 에서 끊겨 **멀쩡한 링크를 깨졌다고 신고**한다.
#    (이 버그를 2026-09-10 에 실제로 겪었다 — 오탐 4건)
LINK = re.compile(r"\[([^\]]*)\]\(((?:[^()]|\([^()]*\))+)\)")

# 들여다보지 않을 곳 — 데이터·비밀·캐시
SKIP_DIRS = {".secrets", "__pycache__", "data", ".git", "node_modules"}

# 🔴 템플릿 안의 «예시» 링크는 깨진 게 정상이다.
#    vl_prompts/ 의 프롬프트 템플릿이 `concepts/overview.md` 같은 자리표시자를 보여준다.
TEMPLATE_DIRS = ("vl_prompts",)


def is_template(rel_path: str) -> bool:
    return any(rel_path.startswith(d + "/") for d in TEMPLATE_DIRS)


def walk(root: str):
    """(마크다운 파일 절대경로, 토픽 기준 상대경로) 와 빈 폴더 목록을 낸다."""
    empty = []
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        if not fns and not dns:
            empty.append(os.path.relpath(dp, root).replace(os.sep, "/"))
        for fn in fns:
            if fn.endswith(".md"):
                p = os.path.join(dp, fn)
                yield p, os.path.relpath(p, root).replace(os.sep, "/"), empty


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    show_all = "--all" in sys.argv
    root = os.path.abspath(args[0]) if args else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    broken, skipped, ok_n, empty = [], [], 0, []
    for path, rel, empty_ref in walk(root):
        empty = empty_ref
        with open(path, encoding="utf-8") as f:
            body = f.read()
        for text, target in LINK.findall(body):
            t = target.strip()
            if t.startswith(("http://", "https://", "#", "mailto:")):
                continue
            t = t.split("#")[0].strip()
            if not t:
                continue
            # 🔴 `%20` 같은 퍼센트 인코딩을 풀어야 파일시스템에서 찾을 수 있다.
            #    공백이 든 파일명을 링크하면 마크다운에서는 보통 인코딩해 적는다.
            t = urllib.parse.unquote(t)
            if os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), t))):
                ok_n += 1
            elif is_template(rel) and not show_all:
                skipped.append((rel, t))
            else:
                broken.append((rel, t, text[:46]))

    print(f"■ 상대 링크 — ✅ 정상 {ok_n}  ·  🔴 깨짐 {len(broken)}"
          + (f"  ·  (템플릿 예시 {len(skipped)}개 제외)" if skipped else ""))
    print(f"  대상: {root}\n")

    if broken:
        cur = None
        for src, tgt, text in sorted(broken):
            if src != cur:
                print(f"  📄 {src}")
                cur = src
            print(f"      ❌ {tgt}   ({text})")
        print()

    # 빈 폴더 — README 가 가리키고 있으면 위와 함께 잡히지만, 안 가리켜도 알려준다
    if empty:
        print(f"■ 빈 폴더 {len(empty)}개 — **git 이 추적하지 않아 GitHub 에 안 올라간다**\n")
        for d in sorted(empty):
            print(f"  📁 {d}")
        print("\n  → 문서를 채우거나, 폴더를 지우고 README 에 «생략 사유»를 적는다.")
        print("     (예: `02-Hypothesis-Testing/README.md` — \"M1 의 P5 분석 문서에 이미 있어 생략\")")

    if not broken and not empty:
        print("  깨진 링크도 빈 폴더도 없다.")
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
