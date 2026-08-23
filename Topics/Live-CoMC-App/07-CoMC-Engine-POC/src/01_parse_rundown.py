#!/usr/bin/env python3
"""M7 실습 2 — ① Rundown .md → rundown_index.json.

M1 파싱 계약을 코드로 옮긴 것이다. 이 단계의 출력이 파이프라인 전체의 소스 데이터이고,
**안전장치 1층(컨텍스트 진입 차단)이 여기서 성립한다** — 금칙 섹션을 여기서 걸러 내지 못하면
이후 어느 단계도 그것을 알지 못한다. "말하지 마"라고 프롬프트에 지시하는 방식은 쓰지 않는다.
입력 자체에서 빼는 것이 방어다.

실행:
    python 01_parse_rundown.py                                  # 샘플 2편 모두
    python 01_parse_rundown.py --live 21
    python 01_parse_rundown.py --path "AI/Roundup/2026-08-17 - Live24 Weekly Rundown.md"

산출:
    output/rundown_index.{live}.json  (샘플 실행 시)
    output/rundown_index.json         (--path 단일 실행 시)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (DATA, out, now_iso, read_text, rel_to_vault, trace,  # noqa: E402
                    validate_or_die, vault_path, write_json)

# ── 정규식 (M1 case-table.md 실측 기반) ────────────────────────────────

# 케이스 1~5: 정수/소수 파트, 분 단위·미정·나머지 전부
RE_PART = re.compile(r"^##\s+(\d+(?:\.\d+)?)부:\s*(.+?)\s*\((.+?)\)\s*$")

# 번호 없이 괄호 시간 표기만 있는 H2. 실물: Live20 '## 주간 영상 (시간 미정)'
RE_H2_PAREN = re.compile(r"^##\s+(.+?)\s*\((.+?)\)\s*$")
RE_H2_ANY = re.compile(r"^##\s+(.+?)\s*$")
RE_H3_PAREN = re.compile(r"^###\s+(.+?)\s*\((.+?)\)\s*$")

# 케이스 6~8: 커버리지 줄
RE_COVERAGE = re.compile(r"^>\s*\*\*이번 방송 커버리지\*\*:\s*(.+?)\s*$")

RE_MINUTES = re.compile(r"(\d+)\s*분")

# ①(U+2460) ~ ⑳(U+2473)
CIRCLED = "".join(chr(0x2460 + i) for i in range(20))
RE_ITEM_SPLIT = re.compile(f"[{CIRCLED}]")

# 지시문은 항목 뒤가 아니라 **줄 전체의 맨 끝**에 자유 문장으로 붙는다 (M1 케이스 7).
RE_DIRECTIVE = re.compile(r"\s+[—–-]\s+(.+)$")

# ⚠️ 대시만으로는 지시문을 판정할 수 없다. 항목 제목 자체에 대시가 흔하다.
#    실물 대조 (2026-08-23 M7 실습 2):
#      Live20 2부 ④ "로드맵 우선 설계 — 시작은 신중하게, 재개는 간편하게"  ← 제목의 일부
#      Live21 3부 ② "...업데이트 — 이 두 개를 메인으로 진행하고, 시간이 남으면 ... 이어간다"  ← 지시문
#    구분되는 것은 대시가 아니라 **운영 동사**다. 지시문은 항목을 어떻게 다룰지 말하고,
#    부제는 항목이 무엇인지 말한다. 대시를 신호로 쓰면 부제를 발화 목록에서 잘라 내
#    말할 수 있는 것을 말하지 못하게 된다.
DIRECTIVE_HINTS = ("진행하", "이어간다", "이어서", "시간이 남으면", "메인으로",
                   "먼저 다루", "순서대로", "우선 진행", "생략", "건너뛰", "나중에")

# 금칙 섹션 키워드 → M3 excluded_sections.reason enum
# 순서가 곧 우선순위다. '보류된 인사이트 후보 (이번 방송 미편성)' 처럼 여러 개가 겹치면
# 가장 강한 신호(미편성 = 이번 회차에서 다루지 않기로 확정)를 택한다.
EXCLUDE_RULES = [("미편성", "unscheduled"), ("보류", "on_hold"), ("후보", "candidate")]

# 조건부 발화 허용 섹션. 실물은 '### 대기 목록 (시간이 남으면)' 하나뿐이라
# 관찰된 어형만 넣는다 — 없는 패턴을 미리 넣으면 오탐이 는다.
CONDITION_HINTS = ("남으면", "시간이 남", "여유가", "가능하면")

# is_final 판정.
# ⚠️ M3 스키마 설명은 "status가 '최종본'이면 true" 라고 적고 있으나,
#    2026-08-23 기준 볼트의 Rundown 14편 중 '최종본' 표기는 **0건**이다.
#    10편은 status 필드 자체가 없고, 나머지는 '방송 완료' 또는 '전 파트 커버리지 확정'이다.
#    설명을 그대로 구현하면 방송 투입 신호가 영원히 꺼진 채로 있게 된다.
#    그래서 실물 어형으로 판정한다. 근거는 vl_worklog 20260823 M7 참조.
FINAL_HINTS = ("최종본", "확정", "방송 완료")


# ── 파싱 ──────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    fm = {}
    for line in text[3:end].split("\n"):
        m = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def parse_time(raw: str) -> tuple[int | None, bool]:
    """(분, is_remainder). 파싱 불가는 None — 0으로 두면 '시간 없음'과 구분되지 않는다."""
    if "나머지" in raw:
        return None, True
    m = RE_MINUTES.search(raw)
    return (int(m.group(1)) if m else None), False


def parse_coverage(line: str) -> tuple[str, list[str], str | None]:
    """커버리지 줄 → (state, items, directive_note)."""
    m = RE_COVERAGE.match(line)
    if not m:
        return "undefined", [], None
    body = m.group(1).strip()
    if not body or body in ("미정", "TBD"):
        return "undefined", [], None

    raw_items = [x.strip() for x in RE_ITEM_SPLIT.split(body) if x.strip()]
    if not raw_items:
        return "undefined", [], None

    # 지시문은 마지막 항목 뒤에 붙는다. 항목 텍스트에서 떼어 내지 않으면
    # 발화 화이트리스트에 운영 지시문이 섞여 들어간다.
    directive = None
    dm = RE_DIRECTIVE.search(raw_items[-1])
    if dm and any(h in dm.group(1) for h in DIRECTIVE_HINTS):
        directive = dm.group(1).strip()
        raw_items[-1] = raw_items[-1][:dm.start()].strip()
        raw_items = [x for x in raw_items if x]

    return ("directive" if directive else "defined"), raw_items, directive


def exclude_reason(heading: str) -> str | None:
    for kw, reason in EXCLUDE_RULES:
        if kw in heading:
            return reason
    return None


def parse_rundown(md_path: Path) -> dict:
    text = read_text(md_path)
    fm = parse_frontmatter(text)
    lines = text.split("\n")

    parts: list[dict] = []
    excluded: list[dict] = []
    conditional: list[dict] = []

    cur: dict | None = None          # 지금 커버리지 줄을 받을 수 있는 파트
    cur_excluded = False             # 금칙 섹션 안이면 커버리지도 무시한다
    pending_h2: tuple[str, str] | None = None   # (제목, 괄호내용) — 커버리지가 오면 파트로 승격

    for line in lines:
        # ── H2 ────────────────────────────────────────────────────────
        if line.startswith("## "):
            heading = line[3:].strip()
            cur, pending_h2, cur_excluded = None, None, False

            reason = exclude_reason(heading)
            if reason:
                # 금칙이 파트 판정보다 먼저다. '주간 영상 후보 (이번 방송 코너 미편성)' 은
                # 괄호가 있어도 파트가 아니라 금칙 섹션이다.
                excluded.append({"heading": heading, "reason": reason})
                cur_excluded = True
                continue

            m = RE_PART.match(line)
            if m:
                pid, title, time_raw = m.group(1), m.group(2).strip(), m.group(3).strip()
                minutes, remainder = parse_time(time_raw)
                cur = {"id": pid, "sort_key": float(pid), "is_numbered": True,
                       "title": title, "time_raw": time_raw, "time_minutes": minutes,
                       "is_remainder": remainder,
                       "coverage_state": "undefined", "coverage_items": [],
                       "directive_note": None}
                parts.append(cur)
                continue

            mp = RE_H2_PAREN.match(line)
            if mp:
                # 아직 파트로 확정하지 않는다. 커버리지 줄이 따라오면 그때 승격한다 —
                # '## 방송 순서 (초안)' 같은 헤딩까지 파트로 만들면 안 되기 때문이다.
                pending_h2 = (mp.group(1).strip(), mp.group(2).strip())
            continue

        # ── H3 ────────────────────────────────────────────────────────
        if line.startswith("### "):
            m3 = RE_H3_PAREN.match(line)
            if m3 and any(h in m3.group(2) for h in CONDITION_HINTS):
                conditional.append({"heading": line[4:].strip(),
                                    "condition": m3.group(2).strip()})
            continue

        # ── 커버리지 줄 ───────────────────────────────────────────────
        if line.lstrip().startswith(">") and "이번 방송 커버리지" in line:
            if cur_excluded:
                continue
            state, items, directive = parse_coverage(line.strip())

            if cur is None and pending_h2 is not None:
                # 번호 없는 방송 구간. 커버리지를 가졌으므로 파트다.
                # 빼면 그 구간에서 말할 수 있는 것을 말하지 못하게 된다.
                title, time_raw = pending_h2
                minutes, remainder = parse_time(time_raw)
                cur = {"id": title, "sort_key": 900.0 + len(parts), "is_numbered": False,
                       "title": title, "time_raw": time_raw, "time_minutes": minutes,
                       "is_remainder": remainder,
                       "coverage_state": "undefined", "coverage_items": [],
                       "directive_note": None}
                parts.append(cur)
                pending_h2 = None

            if cur is not None:
                cur["coverage_state"] = state
                cur["coverage_items"] = items
                cur["directive_note"] = directive

    status = fm.get("status", "")
    index = {
        "source_path": rel_to_vault(md_path),
        "is_final": bool(status) and any(h in status for h in FINAL_HINTS),
        "parts": parts,
        "excluded_sections": excluded,
        "conditional_sections": conditional,
        "parsed_at": now_iso(),
    }
    if status:
        index["frontmatter_status"] = status
    return index


# ── 실행 ──────────────────────────────────────────────────────────────

SAMPLES = {
    "20": "2026-07-19 - Live20 Weekly Rundown.md",
    "21": "2026-07-26 - Live21 Weekly Rundown.md",
}


def report(idx: dict) -> None:
    print(f"\n── {Path(idx['source_path']).name}")
    print(f"   status: {idx.get('frontmatter_status', '(없음)')}  →  is_final={idx['is_final']}")
    print(f"   파트 {len(idx['parts'])}개 · 금칙 {len(idx['excluded_sections'])}개 · "
          f"조건부 {len(idx['conditional_sections'])}개")
    for p in idx["parts"]:
        tag = "" if p["is_numbered"] else "  [번호없음]"
        t = p["time_raw"] or "-"
        label = f"{p['id']}부" if p["is_numbered"] else p["id"]
        print(f"     {label:>12} {p['title'][:26]:<28} ({t}) "
              f"{p['coverage_state']:<9} 항목 {len(p['coverage_items'])}개{tag}")
        if p["directive_note"]:
            print(f"                └ 지시문(발화 제외): {p['directive_note'][:56]}")
    for e in idx["excluded_sections"]:
        print(f"     [금칙:{e['reason']}] {e['heading']}")
    for c in idx["conditional_sections"]:
        print(f"     [조건부] {c['heading']}  ← {c['condition']}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", choices=sorted(SAMPLES), help="샘플 회차")
    ap.add_argument("--path", help="볼트 상대 경로의 Rundown .md")
    args = ap.parse_args()

    if args.path:
        targets = [(None, vault_path(args.path))]
    elif args.live:
        targets = [(args.live, DATA / "rundown_samples" / SAMPLES[args.live])]
    else:
        targets = [(k, DATA / "rundown_samples" / v) for k, v in SAMPLES.items()]

    for live, md in targets:
        if not md.exists():
            sys.exit(f"파일 없음: {md}")
        idx = parse_rundown(md)
        validate_or_die("rundown_index", idx, "01_parse_rundown")
        name = f"rundown_index.{live}.json" if live else "rundown_index.json"
        path = write_json(out(name), idx)
        report(idx)
        covered = sum(len(p["coverage_items"]) for p in idx["parts"])
        trace("01_parse_rundown", ok=True, source=idx["source_path"],
              parts=len(idx["parts"]), coverage_items=covered,
              excluded=len(idx["excluded_sections"]),
              conditional=len(idx["conditional_sections"]), output=path.name)
        print(f"   → {path.name}  (커버리지 항목 총 {covered}개)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
