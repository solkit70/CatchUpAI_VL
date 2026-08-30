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
#
# ⚠️ 괄호 시간 표기는 **선택**이다 (M8 발견, 2026-08-30).
#    Live20·21 은 항상 '## 1부: 제목 (20분)' 이라 필수로 두었는데,
#    Live25 는 '## 1부: 지난 주 생성한 컨텐츠' — 괄호가 없다.
#    필수로 두면 파트로 인식되지 않고, 뒤따르는 커버리지 줄이 받을 파트를 잃어
#    **화이트리스트 15개가 통째로 사라진다.** 크래시도 경고도 없이.
# 이모지·기호 접두를 허용한다. Live11: '## 1️⃣ 1부: 이번 주 활동 수치'
# 접두를 요구하지 않으면 파트가 통째로 인식되지 않아 그 구간이 사라진다.
RE_PART = re.compile(
    r"^##\s+(?:[^\w\s]|\d️⃣)*\s*(\d+(?:\.\d+)?)부:\s*(.+?)"
    r"(?:\s*\((.+?)\))?\s*$")

# 번호 없이 괄호 시간 표기만 있는 H2. 실물: Live20 '## 주간 영상 (시간 미정)'
RE_H2_PAREN = re.compile(r"^##\s+(.+?)\s*\((.+?)\)\s*$")
RE_H2_ANY = re.compile(r"^##\s+(.+?)\s*$")
RE_H3_PAREN = re.compile(r"^###\s+(.+?)\s*\((.+?)\)\s*$")

# 케이스 6~8: 커버리지 줄
#
# ⚠️ 볼드 안에 수식어가 붙는 실물이 있다 (M8 발견, 2026-08-30).
#    Live22 2부: '**이번 방송 커버리지 (2026-08-09 방송 후 실제)**: ①...'
#    수식어를 허용하지 않으면 매칭에 실패하고, 실패는 undefined 로 떨어져
#    **항목 3개가 조용히 사라진다.**
RE_COVERAGE = re.compile(
    r"^>\s*\*\*이번 방송 커버리지(?:\s*\([^)]*\))?\s*\*\*:\s*(.+?)\s*$")

# 커버리지가 '없음'을 뜻하는 어형. 항목이 아니라 부재 선언이다.
#
# ⚠️ 이것을 항목으로 읽으면 **말하면 안 되는 것을 말해도 된다고 허가하는 것**이 된다.
#    Live25 주간 영상: '미편성 — 이번 회차 슬라이드에 없음' 이 통째로
#    발화 허용 항목 1개가 되어 있었다. 항목 소실(말 못 함)보다 나쁜 방향의 실패다.
NO_COVERAGE_FORMS = ("미정", "TBD", "tbd", "미편성", "없음", "해당 없음", "해당없음",
                     "추후", "미확정")

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


def parse_coverage(line: str) -> tuple[str, list[str], str | None, str | None]:
    """커버리지 줄 → (state, items, directive_note, anomaly).

    ## 못 읽은 것과 비어 있는 것은 다르다

    이 함수는 원래 실패를 전부 `undefined` 로 돌려보냈다. undefined 는
    HITL 로 넘어가므로 **안전해 보인다.** 그래서 아무도 눈치채지 못한다 —
    파이프라인은 성공을 보고하고, 파트는 조용히 발화 항목 0개가 된다.

    비어 있는 것(진짜 미편성)은 정상이고, 못 읽은 것은 버그다.
    같은 값으로 뭉뚱그리면 버그가 정상으로 위장된다.
    4번째 값 `anomaly` 가 그 둘을 가른다.
    """
    m = RE_COVERAGE.match(line)
    if not m:
        # 줄에 '이번 방송 커버리지' 가 있는데 정규식이 못 읽었다 = 파서 결함.
        return "undefined", [], None, "coverage_line_unparsed"
    body = m.group(1).strip()
    if not body:
        return "undefined", [], None, None

    # 부재 선언은 항목이 아니다. 앞부분만 봐서 판정한다 —
    # '미편성 — 이번 회차 슬라이드에 없음' 처럼 뒤에 설명이 붙는다.
    head = body.split("—")[0].split("–")[0].strip()
    if head in NO_COVERAGE_FORMS or body in NO_COVERAGE_FORMS:
        return "undefined", [], None, None

    raw_items = [x.strip() for x in RE_ITEM_SPLIT.split(body) if x.strip()]
    if not raw_items:
        return "undefined", [], None, None

    # 원문자(①②③)가 하나도 없으면 항목 목록이 아니다. 문장 하나를 통째로
    # 화이트리스트에 넣으면 그 문장 전체가 발화 허가가 된다.
    if not RE_ITEM_SPLIT.search(body):
        return "undefined", [], None, None

    # 지시문은 마지막 항목 뒤에 붙는다. 항목 텍스트에서 떼어 내지 않으면
    # 발화 화이트리스트에 운영 지시문이 섞여 들어간다.
    directive = None
    dm = RE_DIRECTIVE.search(raw_items[-1])
    if dm and any(h in dm.group(1) for h in DIRECTIVE_HINTS):
        directive = dm.group(1).strip()
        raw_items[-1] = raw_items[-1][:dm.start()].strip()
        raw_items = [x for x in raw_items if x]

    return ("directive" if directive else "defined"), raw_items, directive, None


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

    anomalies: list[dict] = []       # 못 읽은 줄. 빈 리스트가 정상이다
    cur: dict | None = None          # 지금 커버리지 줄을 받을 수 있는 파트
    cur_excluded = False             # 금칙 섹션 안이면 커버리지도 무시한다
    pending_h2: tuple[str, str] | None = None   # (제목, 괄호내용) — 커버리지가 오면 파트로 승격
    cur_h3: str | None = None        # 파트 안에서 마지막으로 지난 H3

    for ln, line in enumerate(lines, 1):
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

            cur_h3 = None
            m = RE_PART.match(line)
            if m:
                # 괄호 시간 표기는 선택이다. 없으면 group(3) 이 None 이다 —
                # 시간을 모르는 것이지 파트가 아닌 것이 아니다.
                pid, title = m.group(1), m.group(2).strip()
                time_raw = (m.group(3) or "").strip() or "시간 미표기"
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
            cur_h3 = line[4:].strip()
            m3 = RE_H3_PAREN.match(line)
            if m3 and any(h in m3.group(2) for h in CONDITION_HINTS):
                conditional.append({"heading": line[4:].strip(),
                                    "condition": m3.group(2).strip()})
            continue

        # ── 커버리지 줄 ───────────────────────────────────────────────
        if line.lstrip().startswith(">") and "이번 방송 커버리지" in line:
            if cur_excluded:
                continue
            state, items, directive, anomaly = parse_coverage(line.strip())
            if anomaly:
                anomalies.append({"kind": anomaly, "line_no": ln,
                                  "raw": line.strip()[:200]})

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
                # ⚠️ 파트는 **첫 커버리지 줄**만 갖는다 (M8 발견, 2026-08-30).
                #
                # 예전에는 뒤따르는 줄이 앞의 것을 덮어썼다. 그래서 파트의 발화
                # 허용 목록이 **통째로 다른 집합으로 바뀌어** 있었다.
                #
                #   Live16 3부  파트 직속 2항목 → 실험②의 3항목으로 대체
                #   Live17 4부  파트 직속 7항목 → 실험⑦의 3항목으로 대체
                #
                # 항목이 사라지는 것보다 나쁘다. 사라지면 말을 못 할 뿐이지만,
                # 대체되면 **엉뚱한 것을 말해도 된다고 허가**하게 된다.
                #
                # 실물에서 순서는 일정하다 — 파트 직속 줄이 항상 먼저 오고,
                # 그 뒤는 전부 '### 실험 ①②③' 같은 하위 섹션의 것이다.
                # 버리지 않고 따로 담는다. 진행자가 특정 실험을 진행할 때
                # 더 좁은 화이트리스트로 쓸 수 있는 정보다.
                if cur_h3 is None and not cur["coverage_items"]:
                    cur["coverage_state"] = state
                    cur["coverage_items"] = items
                    cur["directive_note"] = directive
                else:
                    cur.setdefault("subsection_coverage", []).append({
                        "heading": cur_h3 or "(파트 직속 · 중복 줄)",
                        "coverage_state": state,
                        "coverage_items": items,
                        "directive_note": directive,
                    })
            else:
                # 받을 파트가 없다. 헤딩을 못 읽었다는 뜻이고,
                # 이 줄의 발화 항목은 어디에도 실리지 않는다.
                anomalies.append({"kind": "coverage_without_part", "line_no": ln,
                                  "raw": line.strip()[:200]})

    status = fm.get("status", "")
    index = {
        "source_path": rel_to_vault(md_path),
        "is_final": bool(status) and any(h in status for h in FINAL_HINTS),
        "parts": parts,
        "excluded_sections": excluded,
        "conditional_sections": conditional,
        "parse_anomalies": anomalies,
        "parsed_at": now_iso(),
    }
    if status:
        index["frontmatter_status"] = status
    return index


# ── 실행 ──────────────────────────────────────────────────────────────

SAMPLES = {
    "20": "2026-07-19 - Live20 Weekly Rundown.md",
    "21": "2026-07-26 - Live21 Weekly Rundown.md",
    # M8에서 추가. 이 둘이 파서 결함 3종을 드러낸 실물이다 —
    # 22는 볼드 안 수식어, 25는 괄호 없는 파트 헤딩 + 부재 선언 오탐.
    "22": "2026-08-02 - Live22 Weekly Rundown.md",
    "25": "2026-08-23 - Live25 Weekly Rundown.md",
}


def report_anomalies(idx: dict) -> None:
    """못 읽은 줄을 반드시 눈에 보이게 한다.

    조용한 실패가 이 파서의 핵심 위험이다. 결과가 '안전한 값'(undefined)으로
    떨어지기 때문에 성공과 구분되지 않는다. 화면에 띄우지 않으면 아무도 모른다.
    """
    an = idx.get("parse_anomalies") or []
    if not an:
        return
    print(f"   ⚠ 못 읽은 줄 {len(an)}건 — 발화 항목이 소실됐을 수 있습니다")
    for a in an:
        print(f"       [{a['kind']}] L{a.get('line_no','?')}: {a['raw'][:88]}")


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
        report_anomalies(idx)
        covered = sum(len(p["coverage_items"]) for p in idx["parts"])
        trace("01_parse_rundown", ok=True, source=idx["source_path"],
              parts=len(idx["parts"]), coverage_items=covered,
              excluded=len(idx["excluded_sections"]),
              conditional=len(idx["conditional_sections"]),
              anomalies=idx.get("parse_anomalies", []), output=path.name)
        print(f"   → {path.name}  (커버리지 항목 총 {covered}개)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
