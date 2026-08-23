#!/usr/bin/env python3
"""M7 ③ STT 텍스트 → intent.json.

## 왜 LLM 을 쓰지 않는가

의도 분류에 LLM 을 한 번 더 부르면 **지연이 두 배가 된다.** M5·M6 실측에서
LLM 호출이 2.6초였고, 그 앞에 분류용 호출을 얹으면 5.2초다.
오늘 effort 를 낮춰 확보한 이득을 그대로 반납하는 셈이다.

intent 는 6개짜리 닫힌 집합이고 한국어 명령 어형은 정형적이다. 규칙으로 충분하고,
규칙은 빠르고 결정적이며 같은 입력에 같은 답을 준다.

대신 **확신이 없으면 unknown 으로 떨어뜨린다.** 억지로 하나를 고르지 않는다 —
분류를 틀리면 그 뒤 단계가 전부 엉뚱한 일을 하고, 그건 답을 못 하는 것보다 나쁘다.

## 호출어는 방어적으로 떼어 낸다

M4 openWakeWord 가 호출어를 음향으로 감지하고 그 뒤 구간을 STT 로 넘기므로,
원칙적으로 전사문에는 호출어가 없어야 한다. 그런데 M5 실측에서 호출어 '코엠씨'는
**11문장 중 정확 전사 0건**이었고 매번 다르게 나왔다(외임씨·포엠씨·QM씨·구MC·오엠씨·우엠씨).
경계에 걸쳐 일부가 전사문 앞에 남을 수 있다.

관찰된 오전사가 전부 `씨` 또는 `MC/엠씨` 로 끝났으므로 그 어형만 떼어 낸다.
"네," 같은 짧은 응답어까지 먹지 않도록 좁게 잡았다.

실행:
    python 03_classify_intent.py --live 21 --text "코엠씨, 오늘 3번 파트에서 뭘 다루나요?"
    python 03_classify_intent.py --live 21 --sample 12
    python 03_classify_intent.py --live 21 --suite        # M5 20문장 일괄 분류

산출:
    output/intent.json  (--suite 는 output/intent_suite.json)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (TOPIC, now_iso, out, read_json, trace,  # noqa: E402
                    validate_or_die, write_json)

# M5 문장 세트를 재사용한다. 새로 만들지 않는다 — 같은 문장으로 재야 비교가 된다.
M5_EXAMPLES = TOPIC / "05-STT-LLM-Harness" / "examples"

# ── 호출어 잔재 ───────────────────────────────────────────────────────
# M5 오전사 실측: 외임씨 · 포엠씨 · QM씨 · 구MC · 오엠씨 · MC · 우엠씨
RE_WAKE_RESIDUE = re.compile(r"^\s*[가-힣A-Za-z]{0,4}(?:씨|엠씨|MC|mc)\s*[,，]\s*")

# ── 의도 규칙 ─────────────────────────────────────────────────────────
# 순서가 우선순위다. 위쪽이 더 구체적인 신호.
INTENT_RULES = [
    # "하지 마" 를 stop 에 넣는다. unknown 으로 두면 HITL 을 기다리는 동안
    # AI 가 계속 말할 수 있다. 멈춰서 생기는 실패는 침묵이고,
    # 안 멈춰서 생기는 실패는 하지 말라는 발화다 — 후자가 훨씬 나쁘다.
    ("stop",           ("멈춰", "그만", "정지", "스톱", "중단해", "하지 마", "하지마")),
    ("advance_part",   ("다음 파트", "다음 순서", "넘어가", "다음으로")),
    ("repeat",         ("다시 한번", "다시 한 번", "다시 읽어", "한번 더", "반복해")),
    ("summarize_part", ("요약해", "정리해", "간추려")),
    ("answer_question", ("뭐예요", "뭔가요", "무엇", "어떤", "어디", "언제", "얼마",
                         "몇 ", "인가요", "나요?", "까요?", "맞나요", "확인해")),
]

# ── M2 App Boundary 제외 범위 ─────────────────────────────────────────
# app-boundary.md 의 11개 제외 항목 중 발화로 요청될 수 있는 것만 옮겼다.
# 경계 밖 요청은 되묻는 것이 아니라 거절하는 것이 정답이다 —
# 되물어 봐야 답이 바뀌지 않고, 진행자는 계속 시도하게 된다.
OUT_OF_SCOPE_RULES = [
    ("boundary.2_chat",     ("채팅", "챗", "댓글", "시청자 질문 찾"),
     "시청자 채팅 연동은 범위 밖 — 통제 불가 외부 입력은 프롬프트 인젝션 표면이다"),
    ("boundary.3_write",    ("저장해", "기록해", "파일에 써", "수정해줘", "노트에 적"),
     "볼트 쓰기는 범위 밖 — 앱은 읽기 전용이다 (방송 중 문서 변조 사고 방지)"),
    ("boundary.4_rag",      ("볼트에서 찾", "전체 검색", "볼트 검색", "아무 문서나"),
     "전체 볼트 검색은 범위 밖 — 'Vault에 있다 ≠ 오늘 방송에서 했다' (커버리지 원칙 위반)"),
    ("boundary.5_obs",      ("씬 바꿔", "장면 전환", "화면 전환해", "오비에스"),
     "OBS 씬 자동 제어는 범위 밖 — 방송 중 씬 오작동은 즉시 치명적이다"),
    ("boundary.7_history",  ("지난 회차", "저번 방송", "지난주 방송", "예전 방송"),
     "과거 회차 조회는 범위 밖 — Rundown 단일 문서만 신뢰 소스다 (컨텍스트 혼입)"),
    ("boundary.8_canvas",   ("캔버스", "canvas"),
     ".canvas 파싱은 범위 밖 — .md 가 정본이다"),
    ("boundary.11_lang",    ("영어로 말", "영어로 답", "in english"),
     "다국어 TTS 출력은 범위 밖 — 1차 목표는 한국어 방송이다"),
]


def detect_out_of_scope(text: str):
    low = text.lower()
    for rule_id, keys, why in OUT_OF_SCOPE_RULES:
        if any(k.lower() in low for k in keys):
            return rule_id, why
    return None, None


# 규칙이 걸리지 않았는데 물음표로 끝나면 질문으로 본다. 다만 확신은 낮게 잡는다.
CONF_STRONG, CONF_WEAK, CONF_NONE = 0.9, 0.6, 0.0

# ── 수량 표현 ─────────────────────────────────────────────────────────
KO_NUM = {"한": 1, "하나": 1, "두": 2, "둘": 2, "세": 3, "셋": 3, "네": 4, "넷": 4,
          "다섯": 5, "여섯": 6, "일곱": 7, "여덟": 8, "아홉": 9, "열": 10}
RE_QTY = re.compile(
    r"(\d+|" + "|".join(KO_NUM) + r")\s*(?:개|가지|건|줄|문장)")

# ── 길이 수준 (safety_policy.length_hardcut 과 짝) ─────────────────────
# 여기서는 수준만 정하고 강제는 ⑤ 게이트가 한다. 분류 단계가 문장을 자르면
# 무엇이 잘렸는지 verdict 에 남지 않는다.
LENGTH_TRIGGERS = [("detailed", ("상세히", "자세히")),
                   ("brief", ("간략히", "간단히", "짧게")),
                   ("default", ("정리해줘",))]


def strip_wake_residue(text: str) -> tuple[str, str | None]:
    m = RE_WAKE_RESIDUE.match(text)
    if not m:
        return text.strip(), None
    return text[m.end():].strip(), m.group(0).strip()


def detect_quantity(text: str) -> int | None:
    m = RE_QTY.search(text)
    if not m:
        return None
    tok = m.group(1)
    return int(tok) if tok.isdigit() else KO_NUM.get(tok)


def detect_length_level(text: str) -> str | None:
    for level, phrases in LENGTH_TRIGGERS:
        if any(p in text for p in phrases):
            return level
    return None


def classify(text: str) -> tuple[str, float]:
    low = text.lower()
    # 경계 확인이 의도 분류보다 먼저다. '채팅에서 질문 찾아줘' 는 형태만 보면
    # 질문 검색이지만, 답은 '못 한다'이지 '찾아본다'가 아니다.
    rule_id, _ = detect_out_of_scope(text)
    if rule_id:
        return "out_of_scope", CONF_STRONG
    for intent, keys in INTENT_RULES:
        if any(k.lower() in low for k in keys):
            return intent, CONF_STRONG
    if text.rstrip().endswith("?"):
        return "answer_question", CONF_WEAK
    return "unknown", CONF_NONE


def build_intent(text: str, ctx: dict | None) -> dict:
    body, residue = strip_wake_residue(text)
    intent, conf = classify(body)

    slots: dict = {}
    if intent == "out_of_scope":
        rule_id, why = detect_out_of_scope(body)
        slots["boundary_rule"] = rule_id
        slots["boundary_reason"] = why
    if residue:
        # 떼어 낸 것을 기록해 둔다. 오작동이 났을 때 "호출어를 잘못 먹었나"를
        # 5초 만에 확인할 수 있어야 한다.
        slots["_stripped_wake_residue"] = residue

    m = re.search(r"(\d+(?:\.\d+)?)\s*번?\s*파트", body)
    if m:
        slots["part_id"] = m.group(1)

    qty = detect_quantity(body)
    if qty is not None:
        slots["requested_quantity"] = qty

    level = detect_length_level(body)
    if level:
        slots["length_level"] = level

    # ── 모호성 플래그 (safety_policy.ambiguity_rules 와 연동) ──────────
    flags: list[str] = []
    if ctx is not None:
        cov = ctx.get("coverage_items", [])
        if ctx.get("coverage_state") == "undefined" or not cov:
            flags.append("no_coverage")
        elif qty is not None and qty != len(cov):
            # "질문 세 개만 요약해줘" 인데 화이트리스트가 2개면, 셋째를 어디서 가져올 것인가.
            # 추측해서 채우면 커버리지 밖 발화가 된다. 되묻는 것이 계약이다.
            flags.append("quantity_mismatch")

        # 완료된 항목을 앞으로 할 일로 착각한 요청.
        # 근거 풀에 '완료'로 적힌 항목의 어휘가 요청에 들어 있고, 요청이 미래형이면 의심한다.
        if intent in ("answer_question", "summarize_part"):
            future = any(k in body for k in ("할 건가요", "할 예정", "하나요", "진행하나",
                                             "언제 해", "앞으로"))
            if future:
                done_words = {w for e in ctx.get("evidence_pool", [])
                              if "완료" in e.get("quote", "")
                              for w in re.findall(r"[0-9A-Za-z가-힣]{3,}", e["quote"])}
                if done_words & set(re.findall(r"[0-9A-Za-z가-힣]{3,}", body)):
                    flags.append("completion_confusion")

    return {
        "transcript": text,
        "intent": intent,
        "slots": slots,
        "ambiguity_flags": flags,
        "confidence": conf,
        "created_at": now_iso(),
    }


# ── 실행 ──────────────────────────────────────────────────────────────

def load_ctx(live: str | None):
    if not live:
        return None
    p = out(f"broadcast_context.{live}.json")
    if not p.exists():
        sys.exit(f"{p.name} 없음. 먼저 02_resolve_context.py 를 실행하세요.")
    return read_json(p)


def load_samples():
    sys.path.insert(0, str(M5_EXAMPLES))
    from utterances import UTTERANCES          # noqa: E402
    return UTTERANCES


def show(it: dict) -> None:
    flags = ",".join(it["ambiguity_flags"]) or "-"
    slots = {k: v for k, v in it["slots"].items() if not k.startswith("_")}
    print(f"  {it['intent']:<16} conf={it['confidence']:.1f}  "
          f"모호성={flags:<20} slots={slots}")
    if it["slots"].get("boundary_reason"):
        print(f"      └ 경계 밖({it['slots']['boundary_rule']}): {it['slots']['boundary_reason']}")
    if "_stripped_wake_residue" in it["slots"]:
        print(f"      └ 호출어 잔재 제거: {it['slots']['_stripped_wake_residue']!r}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", help="broadcast_context.{live}.json — 모호성 판정에 필요")
    ap.add_argument("--text")
    ap.add_argument("--sample", help="M5 문장 번호 (예: 12)")
    ap.add_argument("--suite", action="store_true", help="M5 20문장 일괄 분류")
    args = ap.parse_args()

    ctx = load_ctx(args.live)

    if args.suite:
        rows = []
        print(f"M5 문장 세트 일괄 분류"
              + (f"  (커버리지 {len(ctx['coverage_items'])}개 기준)" if ctx else ""))
        for uid, kind, text in load_samples():
            it = build_intent(text, ctx)
            validate_or_die("intent", it, "03_classify_intent")
            rows.append({"id": uid, "kind": kind, **it})
            print(f"\n  [{uid}] {text}")
            show(it)
        path = write_json(out("intent_suite.json"), rows)
        unknown = sum(1 for r in rows if r["intent"] == "unknown")
        amb = sum(1 for r in rows if r["ambiguity_flags"])
        print(f"\n  분류 20건 · unknown {unknown}건 · 모호성 플래그 {amb}건 → {path.name}")
        trace("03_classify_intent", ok=True, mode="suite", n=len(rows),
              unknown=unknown, ambiguous=amb, output=path.name)
        return 0

    if args.sample:
        text = next((t for i, _, t in load_samples() if i == args.sample), None)
        if text is None:
            sys.exit(f"샘플 {args.sample} 없음 (01~20)")
    elif args.text:
        text = args.text
    else:
        sys.exit("--text 또는 --sample 또는 --suite 중 하나가 필요합니다")

    it = build_intent(text, ctx)
    validate_or_die("intent", it, "03_classify_intent")
    path = write_json(out("intent.json"), it)
    print(f"\n  발화: {text}")
    show(it)
    trace("03_classify_intent", ok=True, intent=it["intent"],
          confidence=it["confidence"], flags=it["ambiguity_flags"], output=path.name)
    print(f"  → {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
