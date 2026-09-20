#!/usr/bin/env python3
"""M7 ④ broadcast_context + intent → answer_draft.json.

M5 의 LLMProvider 어댑터를 그대로 쓴다. 새로 만들지 않는다 —
스키마 다운그레이드·재검증·재시도가 이미 거기 있고, 두 벌이 되면 반드시 어긋난다.

## 이 단계가 하지 않는 일

**프롬프트에 "말하지 마"라고 쓰지 않는다.** 금칙 섹션은 ① 단계에서 빠졌고
② 단계가 불변식으로 확인했다. LLM 이 볼 수 있는 것은 evidence_pool 뿐이므로
말하지 말라고 지시할 대상이 애초에 없다. 지시로 막는 방어는 지시를 어기면 뚫린다.

**생성을 막아야 할 때는 생성하지 않는다.** safety_policy 의 모호성 3규칙은
`block_generation: true` 다. 일단 만들어 놓고 뒤에서 거르는 것이 아니라,
만들기 전에 멈추고 진행자에게 되묻는다. 만들어 둔 답은 언젠가 새어 나간다.

## 프로바이더 설정은 레지스트리에서 읽는다

2026-08-23 실측으로 폴백 순서는 openai → gemini → claude, 기본 effort 는
openai=minimal / gemini=low 다. 코드에 박지 않는다 —
근거는 05-STT-LLM-Harness/guides/llm-latency-sweep.md.

실행:
    python 04_compose_answer.py --live 21
    python 04_compose_answer.py --live 21 --provider claude
    python 04_compose_answer.py --live 20 --intent-file ../output/intent.json

산출:
    output/answer_draft.json
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from common import (TOPIC, clear_overlay, load_safety_policy, out,  # noqa: E402
                    read_json, trace, validate_or_die, write_json)

M5_EXAMPLES = TOPIC / "05-STT-LLM-Harness" / "examples"
LLM_RUNTIME = TOPIC / "05-STT-LLM-Harness" / "guides" / "llm_registry.runtime.json"

# 생성 자체를 막는 의도. 제어 명령은 답변을 만들 일이 없다.
CONTROL_INTENTS = {"advance_part", "stop", "repeat"}

# ── CVL 4 (2026-09-17) 캐주얼 레인 ────────────────────────────────────
# 「Rundown 만 근거」로는 방송이 딱딱하다는 진행자 요청. 원칙(근거 없으면 침묵)은 그대로 두고
# **근거 풀을 바꾼다** — 이 의도들은 broadcast_context 가 아니라 casual_brief(②-b) 를 본다.
# 파트 화이트리스트·다른 파트 거절은 적용하지 않는다 (방송 내용이 아니라 주간 맥락·날씨·잡담이다).
# ⑤ 는 같은 인용 검사를 브리프 풀에 대해 한다 — 틀린 말을 막는 층은 그대로다.
CASUAL_INTENTS = {"small_talk", "weekly_recap", "insight", "filler", "broadcast_status", "greet_viewer"}
VIEWERS_FILE = lambda: out("private") / "viewers.json"   # noqa: E731  {"계정이름": "메모"} — 진행자가 관리
CASUAL_BRIEF = lambda live: out("private") / f"casual_brief.{live}.json"  # noqa: E731

# 의도별로 브리프에서 꺼내 쓰는 근거 종류. 전부 넣으면 프롬프트가 1만 자를 넘고 답이 산만해진다.
CASUAL_KINDS = {
    "small_talk":       ("weather", "persona"),
    "weekly_recap":     ("recap", "last_live"),
    "insight":          ("insight",),
    "filler":           ("recap", "insight", "last_live", "filler", "weather"),
    "broadcast_status": ("broadcast", "recap"),
    "greet_viewer":     ("viewer",),
}

SYSTEM_CASUAL = """너는 「Catch Up AI」 라이브 방송의 AI 공동 MC 「코엠씨」다. 진행자는 창수님이다.

누구에게 말하나 (9/18 진행자 결정):
- **말하는 상대는 시청자다.** 「시청자 여러분」에게 말한다. 질문을 창수님이 했더라도 답은 시청자에게 한다.
- 창수님에게 대답하는 말투로 끝내지 않는다 — 「…예요, 창수님」「창수님, …」 같은 호칭 붙임 금지. 창수님은 3인칭으로 언급만 한다 (「창수님이 이번 주에 …」).
- 이번 주 기록·오늘 방송은 **Catch Up AI 의 활동**으로 소개한다 — 「Catch Up AI 에서는 이번 주에 …」「오늘 방송에서는 …」.

말투 — 진짜 방송 진행처럼, 쉽게 (9/18 진행자 피드백: 「무슨 얘기인지 이해가 힘들다」):
- 존댓말이지만 가볍고 따뜻하게. 방송 발화체. 리액션 한 마디("네, 좋아요", "오, 그건요")는 괜찮다.
- **처음 듣는 시청자도 알아듣게.** 기록에 있는 추상어·업무 용어(「검증 층」「운영 철학」「우선순위를 잡다」「비즈니스화」「오케스트레이터」)를 그대로 읽지 않는다 — 무슨 일이 있었는지 **구체적인 상황**으로 바꿔 말한다. 예: 「현장에서만 드러나는 검증 층」→「직접 방송에 써 보니 책상에서는 안 보이던 문제가 나오더라고요」.
- **맥락부터.** 어떤 일이 있었는지 한 문장 → 그래서 무엇을 느꼈는지 한 문장. 배경 없이 결론만 던지지 않는다.
- 여러 항목이 있으면 **두세 개만 골라** 제대로 풀어 말한다. 전부 읊지 않는다.
- 첫 문장은 「시청자 여러분」으로 시작해도 좋다. 매 문장 반복하지는 않는다.
- 문장은 짧게, 한 문장에 한 가지. 목록을 읊지 말고 이야기하듯 이어라.

절대 규칙:
- 아래 근거 목록에 있는 사실만 말한다. 근거에 없는 사실·숫자·날짜·이름은 만들지 않는다.
- 모든 문장에 근거를 붙인다. claim_map 의 evidence_quote 는 근거 목록의 원문을 그대로 옮긴다.
- evidence_path 는 근거 목록에 있는 경로만 쓴다.
- 근거 줄 앞의 날짜·「창수님 말:」 같은 표시는 근거의 라벨이다 — 그대로 읽지 말고 자연스럽게 풀어 말한다.
- 근거가 부족하면 아는 만큼만 짧게 말하고 멈춘다. 추측으로 채우지 않는다.
- 근거에 「사용자」가 나오면 창수님을 뜻한다 — 「사용자」라는 말은 쓰지 않는다.
- 날짜는 근거에 적힌 날짜를 「9월 19일」처럼 말로 쓴다 (「9/19」 꼴은 음성이 분수로 읽는다). 어제·내일·지난주 같은 상대 표현으로 바꾸지 않는다 — 계산이 틀리면 방송 사고다.
- 「…라고 하셨어요」 같은 같은 어미를 연달아 반복하지 않는다. 문장마다 어미를 바꿔 이야기하듯 이어라."""


def casual_evidence(brief: dict, intent_name: str, live: str, intent: dict | None = None) -> list[dict]:
    kinds = CASUAL_KINDS.get(intent_name, ("recap",))
    pool = [e for e in brief["evidence_pool"] if e["kind"] in kinds]
    if intent_name == "greet_viewer":
        # 근거 = 진행자가 방금 말한 이름 + viewers.json 메모. 시청자에 대해 그 밖의 것은 말하지 않는다.
        names = (intent or {}).get("slots", {}).get("viewer_names", [])
        notes = read_json(VIEWERS_FILE()) if VIEWERS_FILE().exists() else {}
        for n in names:
            memo = notes.get(n)
            pool.append({"path": "transcript#viewer", "kind": "viewer",
                         "quote": f"진행자가 알려 준 시청자: {n} 님이 지금 방송에 참여해 댓글을 남겼다"
                                  + (f". 메모: {memo}" if memo else "")})
    if "persona" in kinds:
        pe = brief.get("persona", {})
        pool.append({"path": "casual_brief#persona", "kind": "persona",
                     "quote": f"코엠씨는 {pe.get('show', 'Catch Up AI 라이브')}의 AI 공동 MC 다. 진행자는 {pe.get('host', '창수님')}. "
                              "시청자 여러분에게 Catch Up AI 의 활동을 소개하고, 오늘 방송의 Rundown 과 이번 주 기록을 근거로만 말하며, 근거가 없으면 말하지 않는다"})
    if intent_name in ("filler", "broadcast_status"):
        # 진행자가 자리를 비운다는 사실 자체가 근거다 — 「창수님이 곧 돌아오십니다」를 말하려면 이것이 있어야 한다.
        # 없으면 모델이 그 문장에 근거를 못 붙여 스키마 위반으로 전부 실패한다 (CVL 4 실측).
        pool.append({"path": "transcript#host", "kind": "host",
                     "quote": "창수님이 방금 잠깐 자리를 비운다고 말했고, 곧 돌아와서 방송을 이어간다"})
    if "broadcast" in kinds:
        # 방송 전체 진행 — rundown_index 의 파트 목록과 커버리지 상태를 근거로 만든다 (파트 경계를 넘는 유일한 의도)
        ip = out(f"rundown_index.{live}.json")
        if ip.exists():
            idx = read_json(ip)
            ss = out("session_state.json")
            cur = read_json(ss).get("current_part_id") if ss.exists() else None
            for part in idx["parts"]:
                state = {"defined": "확정", "directive": "지시", "undefined": "미정"}.get(part["coverage_state"], part["coverage_state"])
                items = " · ".join(part["coverage_items"]) if part["coverage_items"] else "항목 없음"
                where = " (지금 진행 중)" if str(part["id"]) == str(cur) else ""
                pool.append({"path": f"rundown_index.{live}#{part['id']}", "kind": "broadcast",
                             "quote": f"방송 순서 {part['id']}부 「{part['title']}」{where}: 커버리지 {state} — {items}"})
    return pool


def build_casual_prompt(pool: list[dict], intent: dict, max_sentences: int) -> str:
    ev = "\n".join(f"- path: {e['path']}\n  quote: {e['quote']}" for e in pool)
    ask = {
        "small_talk": "시청자 여러분에게 인사하거나 날씨를 전하라 (질문은 진행자가 했어도 답은 시청자에게). 날씨는 근거의 도시·기온·하늘을 그대로.",
        "weekly_recap": "Catch Up AI 가 이번 주에 한 활동을 시청자 여러분에게 소개하듯 들려줘라. 날짜 순서로, 굵직한 것 서너 개만 골라 각각 무엇을 왜 했는지 쉽게. 창수님은 3인칭.",
        "insight": "이번 주 활동에서 창수님이 얻은 깨달음을 시청자 여러분에게 전해라 — 두세 개만 골라, 각각 「어떤 일이 있었는지(근거의 '배경')」한 문장 + 「그래서 뭘 느꼈는지」한 문장. 어려운 말은 쉬운 상황 설명으로 바꾼다. '…라고 하셨어요' 연속 반복 금지.",
        "filler": "창수님이 잠깐 자리를 비운다. 그동안 시청자 여러분이 지루하지 않게 Catch Up AI 의 이번 주 활동·오늘 방송 기대 포인트를 가볍게 소개하라. 마지막 문장은 창수님이 곧 돌아온다는 말로.",
        "broadcast_status": "오늘 방송에서 지금까지 한 것과 앞으로 남은 순서를 시청자 여러분에게 안내하라. 파트 순서대로, 지금 진행 중인 파트를 짚어라.",
        "greet_viewer": "근거에 있는 시청자를 계정 이름 그대로 「○○ 님」이라 부르며 반갑게 인사하고 참여와 댓글에 감사를 전해라. 메모가 있으면 한마디 덧붙이고, 없으면 지어내지 않는다. 2~3문장, 따뜻하게.",
    }[intent["intent"]]
    import datetime as _dt
    today = _dt.date.today()
    wd = "월화수목금토일"[today.weekday()]
    return f"""[오늘] {today.isoformat()} ({wd})

[근거 목록 — 이번 주 기록 · 오늘 방송 순서 · 날씨]
{ev}

[진행자/시청자 발화]
{intent['transcript']}

{ask} 문장은 최대 {max_sentences}개."""

SYSTEM = """너는 「Catch Up AI」 라이브 방송의 AI 공동 MC 「코엠씨」다. 말하는 상대는 시청자 여러분이다 — 진행자(창수님)에게 대답하는 말투(「…예요, 창수님」)를 쓰지 않는다.

절대 규칙:
- 아래 근거 목록에 있는 내용만 말한다. 근거에 없으면 추측하지 않는다.
- 모든 문장에 근거를 붙인다. claim_map 의 evidence_quote 는 근거 목록의 원문을 그대로 옮긴다.
- evidence_path 는 근거 목록에 있는 경로만 쓴다.
- 커버리지 화이트리스트 밖의 주제를 꺼내지 않는다.
- 방송 발화체로, 문장당 한 호흡에 읽을 수 있는 길이로 쓴다.
- 날짜는 「9월 16일」처럼 말로 쓴다 — 「9/16」은 음성 합성이 분수로 읽는다 (9/17 실청)."""


def build_prompt(ctx: dict, intent: dict, max_sentences: int) -> str:
    ev = "\n".join(f"- path: {e['path']}\n  quote: {e['quote']}"
                   for e in ctx["evidence_pool"])
    cov = "\n".join(f"- {c}" for c in ctx["coverage_items"])
    # ⚠️ M10 리허설 1회차 수정 (2026-09-06) — 「내용 없는 발화」를 고친다.
    #
    # 예전 지시는 *"위 근거만 사용해"* 였다. 그런데 근거 풀은 섹션 헤딩이고,
    # 질문의 실제 답(오늘 다루는 항목 이름)은 **화이트리스트에만** 있었다.
    # 모델은 시킨 대로 근거만 써서, 게이트를 통과하지만 아무것도 말하지 않는
    # 답을 만들었다.
    #
    #   질문  오늘 2부에서 진행할 실험이 뭐가 있나요?
    #   답    …후보 전체 목록 중에서 선별된 항목들입니다.   ← 이름을 하나도 안 말함
    #
    # 방어를 푸는 변경이 아니다. M8 게이트 규칙 5의 신뢰 출처 표에
    # **「커버리지 화이트리스트 — 정의상 말해도 되는 것」** 이 이미 들어 있다.
    # 게이트는 근거로 인정하는데 프롬프트만 쓰지 말라고 하던 **정의 불일치**를 맞춘 것이다.
    #
    # 화이트리스트 밖은 여전히 못 말한다 — 그 제약은 문구에 그대로 남아 있고,
    # 게이트 규칙 3·4 가 독립적으로 다시 검사한다.
    # 내부 용어 누출 금지 — 리허설 2회차에서 실물로 나왔다 (2026-09-06):
    #   "오늘 2부 실험은 **화이트리스트에 있는** 'CoMC 앱 개발...'로 진행합니다."
    # 시청자는 이 시스템의 내부 구조를 모른다. '화이트리스트·커버리지·근거 목록'은
    # 앱이 스스로를 설명하는 말이지 방송에서 할 말이 아니다.
    _style = ("답변에는 '화이트리스트'·'커버리지'·'근거 목록' 같은 내부 용어를 쓰지 말고, "
              "방송에서 그대로 읽을 수 있는 자연스러운 존댓말로 쓴다.")
    # ⚠️ Live #27 사고 8·9 (2026-09-13) — 두 규칙을 더한다.
    #
    # 사고 8  확정 커버리지를 "후보"라고 말했다 (3/3 재현). 근거 풀에 `### 후보` 제목이
    #         들어 있었고 확정 항목은 없었다. ② 가 근거 풀을 고쳤고(「[확정]」 줄 · 후보 제외),
    #         여기서는 그 표기의 뜻을 모델에게 알려 준다.
    # 사고 9  "CoMC 어디까지 왔나" 에 항목 이름만 읊고 상태를 말하지 않았다. 상태 질문이면
    #         「[확정 항목 현재 상태]」 줄의 상태를 한 문장으로 말하게 한다.
    #
    # 둘 다 ⑤ 게이트가 독립적으로 다시 검사한다 (cross_part · content_empty). 프롬프트는
    # 확률을 옮기고 게이트는 하한을 만든다 — M10 규칙 8 과 같은 구조.
    _status = ("근거 목록에서 '[확정]' 은 이번 방송에서 확정된 항목이고 '후보'는 확정이 아니다 — "
               "확정 항목을 후보라고 부르지 않는다. 대괄호 라벨('[확정]' 등)은 근거의 표시일 뿐이므로 "
               "답에 대괄호나 그 라벨을 쓰지 않는다 — 9/17 실사용에서 '[확정]' 이 그대로 읽힌 사고. ")
    if is_status_question(intent["transcript"]):
        _status += ("질문이 진행 상태를 묻고 있다 — 각 항목에 대해 '[확정 항목 현재 상태]' 줄에 적힌 "
                    "상태(완료·진행 중·대기 등)를 한 문장으로 말한다. 항목 이름만 나열하지 않는다. ")
    ask = {"answer_question":
           "위 항목과 근거만 사용해 시청자 질문에 답하는 초안을 만들어라. "
           "질문이 '무엇을 다루는가'를 묻는 경우 항목 이름을 그대로 말한다. " + _status + _style,
           "summarize_part":
           "위 항목과 근거만 사용해 현재 파트를 요약하는 초안을 만들어라. " + _status + _style}[
        intent["intent"]]
    return f"""[커버리지 화이트리스트 — 오늘 이 파트에서 말해도 되는 항목. 이 범위 밖은 말하지 않는다]
{cov}

[근거 목록]
{ev}

[커버리지 상태]
{ctx['coverage_state']}

[진행자/시청자 발화]
{intent['transcript']}

{ask} 문장은 최대 {max_sentences}개."""


# ── 상태 질문 · 다른 파트 질문 판정 (사고 9 · 10) ─────────────────────────
#
# 규칙 기반이다. ③ 이 LLM 없이 의도를 분류하듯, 이 두 판정도 문자열로 한다.
# 판정 기준이 코드에 적혀 있어야 사고 뒤에 "왜 그렇게 답했나"를 5초 안에 답할 수 있다.
STATUS_KEYWORDS = ("어디까지", "상태", "진행", "현황", "됐나", "됐어", "얼마나", "끝났")


def is_status_question(text: str) -> bool:
    return any(k in text for k in STATUS_KEYWORDS)


def other_part_mentioned(text: str, ctx: dict) -> dict | None:
    """질문이 현재 파트가 아닌 파트를 가리키는가.

    사고 10 (Live #27) — 2부 진행 중 「주간 영상은 뭐예요?」에 2부 항목을 "이번 주 영상"으로
    답했다. 주간 영상 파트는 커버리지 undefined 라 컨텍스트가 없었고, 모델은 손에 있는
    근거(2부)로 답했다. **다른 파트를 묻는 질문은 이 파트 근거로 답할 수 없다.**

    판정: 다른 파트의 제목 어휘가 질문에 들어 있거나, 「N부」가 현재 파트 번호와 다르면.
    현재 파트 제목의 어휘는 제외한다 — 두 파트가 같은 단어를 공유할 수 있다.
    """
    import re as _re
    cur_id = str(ctx.get("current_part_id") or "")
    for m in _re.finditer(r"(\d)\s*부", text):
        if m.group(1) != cur_id:
            return {"id": m.group(1), "title": f"{m.group(1)}부", "by": "part_number"}
    cur_words = set(_re.findall(r"[가-힣A-Za-z]{2,}", " ".join(
        [str(ctx.get("current_part_title") or "")] + list(ctx.get("coverage_items", [])))))
    for p in ctx.get("other_parts", []):
        title = _re.sub(r"^\d+\.\s*", "", p["title"])          # "3. 주간 영상" → "주간 영상"
        words = [w for w in _re.findall(r"[가-힣A-Za-z]{2,}", title) if w not in cur_words]
        if words and all(w in text for w in words):
            return {"id": p["id"], "title": title, "by": "title",
                    "coverage_state": p.get("coverage_state")}
    return None


def max_sentences_for(intent: dict, policy: dict) -> int:
    levels = policy["length_hardcut"]["levels"]
    return levels.get(intent["slots"].get("length_level", "default"), levels["default"])


def refuse(reason: str, detail: str, **fields) -> int:
    trace("04_compose_answer", ok=False, reason=reason, **fields)
    print(f"\n⛔ 생성하지 않습니다 — {detail}")
    print("   만들어 두고 뒤에서 거르는 것이 아니라, 만들기 전에 멈춘다.")
    # 사고 11 — 거절했으면 화면도 비운다. 옛 초안이 남아 있으면 시청자는 그것을 답으로 읽는다.
    clear_overlay("04_compose_answer", reason)
    print("   화면을 비웠습니다 (overlay.json text=\"\").")
    return 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", required=True)
    ap.add_argument("--intent-file", help="기본값 output/intent.json")
    ap.add_argument("--provider", help="폴백 무시하고 지정 프로바이더만")
    ap.add_argument("--effort", choices=["minimal", "low", "medium", "high"],
                    help="레지스트리의 default_effort 를 덮어쓴다 (M8 effort 스윕용). "
                         "실전에서는 쓰지 않는다 — 근거는 llm-latency-sweep.md 다")
    ap.add_argument("--dump-prompt", help="LLM 에 보낸 프롬프트 전문을 이 경로에 저장 "
                                          "(M8 실습 2 — 금칙 섹션 미노출 증명)")
    args = ap.parse_args()

    intent = read_json(Path(args.intent_file) if args.intent_file else out("intent.json"))
    policy = load_safety_policy()
    casual = intent["intent"] in CASUAL_INTENTS

    ctx_path = out(f"broadcast_context.{args.live}.json")
    if casual:
        # 캐주얼 레인 — 브리프가 근거 풀이다. 파트 컨텍스트는 보지 않는다.
        bp = CASUAL_BRIEF(args.live)
        if not bp.exists():
            return refuse("no_brief", f"{bp.name} 없음 — 02b_build_casual_brief.py 를 먼저 실행 (start_comc 가 한다)")
        brief = read_json(bp)
        pool = casual_evidence(brief, intent["intent"], args.live, intent)
        if not pool:
            return refuse("no_brief_evidence", f"브리프에 '{intent['intent']}' 용 근거가 없습니다")
        ctx = {"evidence_pool": pool, "coverage_items": brief.get("topics", []),
               "coverage_state": "defined", "current_part_id": None}
    else:
        ctx = read_json(ctx_path)

    # ── 생성 전 차단 ──────────────────────────────────────────────────
    if intent["intent"] == "out_of_scope":
        return refuse("out_of_scope",
                      intent["slots"].get("boundary_reason", "M2 App Boundary 제외 범위"),
                      rule=intent["slots"].get("boundary_rule"))
    if intent["intent"] == "unknown":
        return refuse("unknown_intent",
                      "의도를 분류하지 못했습니다. 진행자에게 되묻습니다 (HITL)")
    if intent["intent"] in CONTROL_INTENTS:
        return refuse("control_intent",
                      f"'{intent['intent']}' 는 제어 명령이라 답변 생성 대상이 아닙니다")
    # 사고 10 — 다른 파트를 묻는 질문은 이 파트 근거로 답하지 않는다. LLM 호출 전에 멈춘다.
    op = None if casual else other_part_mentioned(intent.get("transcript", ""), ctx)
    if op:
        return refuse("cross_part",
                      f"질문이 현재 파트({ctx['current_part_id']})가 아닌 "
                      f"'{op['title']}' 를 가리킵니다 — 이 파트 근거로 답하지 않습니다. "
                      f"진행자가 파트를 바꾸거나 되묻습니다 (HITL)",
                      target_part=op["id"], by=op["by"])
    if intent["ambiguity_flags"]:
        rules = {r["signal"].split("'")[1]: r for r in policy["ambiguity_rules"]}
        for f in intent["ambiguity_flags"]:
            r = rules.get(f)
            if r and r.get("block_generation"):
                return refuse("ambiguity", f"{f} — 되물을 말: \"{r['prompt']}\"",
                              flag=f, rule=r["id"])

    # ── 생성 ──────────────────────────────────────────────────────────
    sys.path.insert(0, str(M5_EXAMPLES))
    from llm_providers import SchemaViolation, build  # noqa: E402

    rt = read_json(LLM_RUNTIME)
    order = [args.provider] if args.provider else rt["fallback_order"]
    if casual:
        # 인사·날씨는 짧게, 시간 끌기·회고·진행 안내는 길게 (casual = 8문장 · 450자)
        intent["slots"].setdefault("length_level", "default" if intent["intent"] in ("greet_viewer", "small_talk") else "casual")
    max_s = max_sentences_for(intent, policy)

    prompt = (build_casual_prompt(ctx["evidence_pool"], intent, max_s) if casual
              else build_prompt(ctx, intent, max_s))
    system = SYSTEM_CASUAL if casual else SYSTEM
    if intent["slots"].get("lang") == "en":
        # CVL 4 — 진행자가 「영어로」라고 하면 영어로. 인용은 그대로 한국어 원문이어야 게이트가 대조한다.
        prompt += chr(10) * 2 + ("[언어] 답 문장(sentences)은 자연스러운 영어로 쓴다 — 시청자에게 말하듯. "
                   "claim_map 의 evidence_quote 는 번역하지 말고 근거 목록의 원문(한국어) 그대로 옮긴다. "
                   "고유명사(Chrome Remote Desktop, CoMC, Builders Lounge)는 그대로 쓴다.")

    # ── 프롬프트 지문 ─────────────────────────────────────────────────
    # 전문을 trace 에 매번 넣으면 파일이 불어나고 같은 내용을 두 벌 갖게 된다.
    # 대신 해시만 남긴다. build_prompt 는 (ctx, intent, max_s) 에 대해 결정적이므로
    # 나중에 저장된 컨텍스트로 다시 만들어 해시를 맞춰 보면
    # **그때 보낸 것이 이것임을 증명할 수 있다.**
    # 증명이 성립해야 "금칙 섹션이 프롬프트에 없었다"를 사후에 확인할 수 있다.
    fingerprint = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
    if args.dump_prompt:
        dp = Path(args.dump_prompt)
        dp.parent.mkdir(parents=True, exist_ok=True)
        dp.write_text(prompt, encoding="utf-8")
        print(f"   프롬프트 전문 저장: {dp.name} (sha256 {fingerprint[:16]})")

    attempts: list[dict] = []

    for name in order:
        cfg = rt["providers"].get(name)
        if cfg is None:
            attempts.append({"provider": name, "error": "런타임 레지스트리에 없음"})
            continue
        eff = args.effort or cfg.get("default_effort")
        t0 = time.time()
        try:
            # build() 도 try 안이다 — 키 없는 폴백 프로바이더(GEMINI_API_KEY 미설정)가 KeyError 로
            # 프로세스를 죽여 ④ 전체가 실패하던 것을 CVL 4 에서 봤다. 폴백은 건너뛰는 것이지 죽는 것이 아니다.
            p = build(name, cfg["model"], cfg.get("cost_per_1k_tokens"), effort=eff)
            r = p.complete(system, prompt, max_retries=1)
        except SchemaViolation as e:
            attempts.append({"provider": name, "error": "계약 위반", "detail": e.errors[:3],
                             "ms": round((time.time() - t0) * 1000)})
            print(f"  · {name}: 재검증 실패 → 다음 프로바이더로  ({'; '.join(e.errors[:2])[:160]})")
            continue
        except Exception as e:
            attempts.append({"provider": name, "error": f"{type(e).__name__}",
                             "detail": str(e)[:160],
                             "ms": round((time.time() - t0) * 1000)})
            print(f"  · {name}: {type(e).__name__} → 다음 프로바이더로")
            continue

        wall = round((time.time() - t0) * 1000)
        draft = r.draft
        validate_or_die("answer_draft", draft, "04_compose_answer")
        path = write_json(out("answer_draft.json"), draft)

        print(f"\n── {name} ({r.model}, effort={eff or '기본값'}) · {wall}ms · 시도 {r.attempts}회")
        print(f"   문장 {draft['length_sentences']}개 (상한 {max_s}) · "
              f"coverage={draft['coverage_state']}")
        for i, s in enumerate(draft["sentences"]):
            print(f"     [{i}] {s}")
        trace("04_compose_answer", ok=True, provider=name, model=r.model, lane="casual" if casual else "broadcast",
              prompt_sha256=fingerprint, prompt_chars=len(prompt),
              evidence_paths=sorted({e["path"] for e in ctx["evidence_pool"]}),
              effort=eff, latency_ms=wall, attempts=r.attempts,
              sentences=draft["length_sentences"], max_sentences=max_s,
              fallback_skipped=[a["provider"] for a in attempts], output=path.name)
        print(f"   → {path.name}")
        return 0

    trace("04_compose_answer", ok=False, reason="all_providers_failed", attempts=attempts)
    print("\n⛔ 모든 프로바이더 실패 → HITL 로 넘깁니다. 추측 발화는 하지 않습니다.",
          file=sys.stderr)
    for a in attempts:
        print(f"   - {a['provider']}: {a.get('error')} {a.get('detail','')}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
