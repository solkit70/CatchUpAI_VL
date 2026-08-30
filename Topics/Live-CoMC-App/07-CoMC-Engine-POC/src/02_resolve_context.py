#!/usr/bin/env python3
"""M7 실습 2 — ② rundown_index + 주변 문서 → broadcast_context.json.

LLM(⑥)에 넘길 **발화 허용 범위와 근거 풀**을 조립한다. 이 단계의 출력이
LLM 이 볼 수 있는 세계의 전부다 — 여기 없는 것은 LLM 이 알 수 없고,
알 수 없으면 말할 수 없다. 그것이 안전장치 1층의 작동 방식이다.

세 가지를 지킨다.

  1. **금칙 섹션의 본문은 근거 풀에 절대 들어가지 않는다.**
     `forbidden_removed` 는 스키마상 const:true 인 불변식 플래그다. 참이라고 적는 것과
     참인 것은 다르므로, 조립이 끝난 뒤 실제로 대조해서 확인한다.

  2. **커버리지가 undefined 면 컨텍스트를 만들지 않는다.**
     빈 컨텍스트를 넘기면 LLM 은 근거 없이 답하려 든다. 만들지 않고 HITL 로 되묻는다.

  3. **current_part_id 는 인자로 받는다. 추정하지 않는다.**
     M2에서 확정한 "자동 전환 금지" 원칙이다. 시각 기반 추정은 ⑤ 단계(실습 5)에서
     `suggested_part_id` 로 따로 다루고, 이 단계는 권위값만 쓴다.

실행:
    python 02_resolve_context.py --live 21 --part 3
    python 02_resolve_context.py --live 20 --part "주간 영상"
    python 02_resolve_context.py --live 20 --part 2 --max-evidence 12

산출:
    output/broadcast_context.{live}.json
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (now_iso, out, read_json, read_text, trace,  # noqa: E402
                    validate_or_die, vault_path, write_json)

RE_WIKILINK = re.compile(r"\[\[([^\]|#]+)")
RE_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$")

# 근거로 쓸 섹션. 로드맵이 지정한 크로스 조회 대상이다.
DAILY_SECTION = "## Status Summary"
WEEKLY_SECTION = "## Priority Summary"

# 토큰 대조에서 버릴 조사·일반어. 이게 없으면 '있다' 같은 말로 아무 행이나 걸린다.
STOP = {"완료", "진행", "예정", "작업", "확인", "관련", "이번", "오늘", "정리",
        "가지", "부분", "내용", "상태", "항목", "메모", "우선순위"}


def frontmatter_links(text: str) -> list[str]:
    """frontmatter links: 목록의 위키링크 대상만 뽑는다."""
    if not text.startswith("---"):
        return []
    end = text.find("\n---", 3)
    head = text[3:end if end != -1 else len(text)]
    out_: list[str] = []
    in_links = False
    for line in head.split("\n"):
        if re.match(r"^links:\s*$", line):
            in_links = True
            continue
        if in_links:
            if re.match(r"^\s*-\s", line):
                m = RE_WIKILINK.search(line)
                if m:
                    out_.append(m.group(1).strip())
                continue
            if line.strip() and not line.startswith(" "):
                in_links = False
    return out_


def section_rows(path: Path, heading: str) -> list[str]:
    """지정 섹션의 표 행 텍스트를 돌려준다. 섹션이 없으면 빈 리스트."""
    if not path.exists():
        return []
    lines = read_text(path).split("\n")
    rows, inside = [], False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = line.strip() == heading
            continue
        if not inside:
            continue
        m = RE_TABLE_ROW.match(line.rstrip())
        if not m:
            continue
        cells = [c.strip() for c in m.group(1).split("|")]
        if not cells or all(set(c) <= set("-: ") for c in cells):
            continue                                  # 구분선
        if cells[0] in ("항목", "우선순위"):
            continue                                  # 헤더
        rows.append(" — ".join(c for c in cells if c))
    return rows


def tokens(text: str) -> set[str]:
    raw = re.findall(r"[0-9A-Za-z가-힣]{2,}", text)
    return {t for t in raw if t not in STOP and len(t) >= 2}


def relevant(row: str, keys: set[str]) -> bool:
    """근거 풀은 좁을수록 좋다.

    관련 없는 행까지 넣으면 LLM 이 커버리지 밖 주제를 '근거가 있다'고 믿을 재료가 된다.
    화이트리스트와 겹치는 토큰이 있을 때만 넣는다.
    """
    return bool(tokens(row) & keys)


def part_body_quotes(md_text: str, part_title: str, limit: int) -> list[str]:
    """해당 파트 본문에서 인용 가능한 줄을 뽑는다 (H3 제목과 불릿)."""
    lines = md_text.split("\n")
    quotes, inside = [], False
    for line in lines:
        if line.startswith("## "):
            if inside:
                break
            inside = part_title in line
            continue
        if not inside:
            continue
        s = line.strip()
        if s.startswith("### "):
            quotes.append(s[4:].strip())
        elif s.startswith(("- ", "* ")) and len(s) > 6:
            quotes.append(s[2:].strip())
        if len(quotes) >= limit:
            break
    return quotes


def build(live: str, part_id: str, max_evidence: int,
          allow_conditional: bool = False) -> dict:
    idx = read_json(out(f"rundown_index.{live}.json"))
    src = vault_path(idx["source_path"])
    md_text = read_text(src)

    part = next((p for p in idx["parts"] if p["id"] == part_id), None)
    if part is None:
        ids = ", ".join(p["id"] for p in idx["parts"])
        sys.exit(f"파트 '{part_id}' 없음. 가능한 값: {ids}")

    # ── 커버리지 미정이면 조립하지 않는다 ─────────────────────────────
    if part["coverage_state"] == "undefined" or not part["coverage_items"]:
        trace("02_resolve_context", ok=False, reason="coverage_undefined",
              live=live, part=part_id)
        print(f"\n⛔ {part_id}부 커버리지가 undefined 입니다 — 컨텍스트를 만들지 않습니다.")
        print("   빈 컨텍스트를 넘기면 LLM 이 근거 없이 답하려 든다. HITL 로 되묻는 것이 계약이다.")
        sys.exit(2)

    keys = tokens(" ".join(part["coverage_items"]) + " " + part["title"])

    # ── 근거 풀 ───────────────────────────────────────────────────────
    # 금칙 섹션은 01 단계에서 이미 파트 목록 밖으로 나갔다. 여기서는 파트 본문만 읽으므로
    # 금칙 본문이 들어올 경로가 구조적으로 없다. 그래도 뒤에서 대조해 확인한다.
    evidence: list[dict] = []
    rundown_rel = idx["source_path"]

    for q in part_body_quotes(md_text, part["title"], limit=max_evidence):
        evidence.append({"path": f"{rundown_rel}#{part['title']}", "quote": q})

    status_map: dict[str, str] = {}
    status_map["rundown"] = "final" if idx["is_final"] else "unconfirmed"

    for link in frontmatter_links(md_text):
        key = Path(link).name
        if link.endswith(".canvas"):
            # M1 계약: .md 가 정본이고 .canvas 는 시각화 사본이라 표기가 어긋날 수 있다.
            # 파서는 .canvas 를 신뢰하지 않는다. '없다'가 아니라 '안 본다'로 기록해야
            # 나중에 "왜 이 문서가 근거에 없지?" 를 5초 만에 답할 수 있다.
            status_map[key] = "skipped:canvas"
            continue
        p = vault_path(link + ".md")
        if not p.exists():
            status_map[key] = "missing_file"
            continue
        heading = WEEKLY_SECTION if "Weekly Progress" in link else DAILY_SECTION
        rows = section_rows(p, heading)
        if not rows:
            # 섹션이 없는 것과 파일이 없는 것은 다르다. 뭉뚱그리면
            # "문서가 낡았다"와 "문서를 못 찾았다"를 구분할 수 없다.
            status_map[key] = "missing_section"
            continue
        hits = [r for r in rows if relevant(r, keys)]
        status_map[key] = f"ok:{len(hits)}/{len(rows)}"
        for r in hits[:max_evidence]:
            evidence.append({"path": f"{link}#{heading[3:]}", "quote": r})

    # ── 불변식 확인 ───────────────────────────────────────────────────
    # forbidden_removed 를 true 로 적기 전에 실제로 참인지 대조한다.
    forbidden_headings = [e["heading"] for e in idx["excluded_sections"]]
    leaked = [e for e in evidence
              if any(h in e["path"] or h in e["quote"] for h in forbidden_headings)]
    if leaked:
        trace("02_resolve_context", ok=False, reason="forbidden_leak",
              count=len(leaked), sample=leaked[0]["quote"][:80])
        print(f"\n⛔ 금칙 섹션 내용이 근거 풀에 섞였습니다 ({len(leaked)}건). 중단합니다.",
              file=sys.stderr)
        sys.exit(1)

    # ── 조건부 섹션 게이팅 (safety_policy.conditional.time_gated) ──────
    #
    # M8 이전에는 조건부 섹션이 근거 풀에 무조건 들어 있었다. Live21 의
    # '대기 목록 (시간이 남으면)' 이 근거로 실려 있었고, 금칙 섹션을 묻는
    # 질문에 **그럴듯한 답을 만드는 재료**가 됐다.
    #
    # 조건이 '시간이 남으면' 같은 형태라 코드가 판정할 수 없다.
    # 판정할 수 없는 조건의 기본값은 '충족되지 않음'이어야 한다 — 모르면 넣지 않는다.
    withheld: list[dict] = []
    cond = idx.get("conditional_sections", [])
    if cond and not allow_conditional:
        keep = []
        for e in evidence:
            hit = next((c for c in cond
                        if c["heading"] in e["quote"] or c["heading"] in e["path"]), None)
            if hit:
                withheld.append({"heading": hit["heading"], "condition": hit["condition"],
                                 "reason": "조건 충족 여부를 코드가 판정할 수 없음 — "
                                           "기본값 제외 (--allow-conditional 로 편입)"})
            else:
                keep.append(e)
        evidence = keep

    ctx = {
        "current_part_id": part["id"],
        "coverage_state": part["coverage_state"],
        "coverage_items": part["coverage_items"],
        "evidence_pool": evidence,
        "status_map": status_map,
        # 이름만 넘긴다. 본문은 넘기지 않는다. 금칙 요청을 거절하려면
        # 무엇이 금칙인지 알아야 하고, 그건 이름만으로 충분하다.
        "excluded_headings": forbidden_headings,
        "withheld_conditional": withheld,
        "forbidden_removed": True,
        "assembled_at": now_iso(),
    }
    return ctx, part


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True, help="회차 (rundown_index.{live}.json)")
    ap.add_argument("--part", required=True,
                    help="current_part_id — 권위값. 추정하지 않고 명시적으로 받는다")
    ap.add_argument("--allow-conditional", action="store_true",
                    help="조건부 섹션을 근거 풀에 편입한다 (진행자가 조건 충족을 판정했을 때)")
    ap.add_argument("--max-evidence", type=int, default=8,
                    help="소스별 최대 근거 수 (기본 8). 근거 풀은 좁을수록 좋다")
    args = ap.parse_args()

    ctx, part = build(args.live, args.part, args.max_evidence,
                      allow_conditional=args.allow_conditional)
    validate_or_die("broadcast_context", ctx, "02_resolve_context")
    path = write_json(out(f"broadcast_context.{args.live}.json"), ctx)

    label = f"{part['id']}\ubd80" if part.get("is_numbered", True) else f"'{part['id']}'"
    print(f"\n\u2500\u2500 Live{args.live} / {label} {part['title']}")
    print(f"   커버리지 {ctx['coverage_state']} · 화이트리스트 {len(ctx['coverage_items'])}개")
    for i, it in enumerate(ctx["coverage_items"], 1):
        print(f"     {i}. {it[:64]}")
    if part.get("directive_note"):
        print(f"   지시문(발화 제외): {part['directive_note'][:70]}")

    print(f"\n   근거 풀 {len(ctx['evidence_pool'])}건")
    for e in ctx["evidence_pool"][:5]:
        print(f"     [{Path(e['path']).name[:34]}] {e['quote'][:58]}")
    if len(ctx["evidence_pool"]) > 5:
        print(f"     … 외 {len(ctx['evidence_pool']) - 5}건")

    print(f"\n   status_map {len(ctx['status_map'])}개")
    for k, v in list(ctx["status_map"].items())[:12]:
        print(f"     {k[:44]:<46} {v}")

    trace("02_resolve_context", ok=True, live=args.live, part=part["id"],
          coverage_items=len(ctx["coverage_items"]),
          evidence=len(ctx["evidence_pool"]),
          status_map=len(ctx["status_map"]), output=path.name)
    print(f"\n   → {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
