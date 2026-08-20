#!/usr/bin/env python3
"""M5 실습 1 — 낭독 문장 세트(정답 데이터).

guides/utterance-script.md 와 같은 내용을 코드에서 쓰기 위한 형태로 둔다.
문서와 코드 중 하나만 고치면 WER 계산이 조용히 틀어지므로,
문장을 바꿀 때는 반드시 두 곳을 함께 고친다.

일부러 어렵게 만든 세트다:
  - 영어 기술 용어가 한국어 문장에 섞인다 (RAG, Remotion, API, FDE …)
  - 호출어 "코엠씨" 는 사전에 없는 단어라 전사기가 임의로 바꿔 쓴다
  - 숫자·단위가 들어간다 (세 개, 3번, 몇 분)
쉬운 문장으로 재면 실제 방송 조건에서 무너진다.
"""

# (번호, 유형, 정답 문장)
UTTERANCES = [
    ("01", "question", "코엠씨, 오늘 방송에서 다루는 주제가 뭐예요?"),
    ("02", "question", "RAG하고 파인튜닝 중에 어떤 걸 먼저 배워야 하나요?"),
    ("03", "question", "지금 쓰시는 TTS 모델이 Qwen3-TTS 맞나요?"),
    ("04", "question", "비전공자도 FDE로 취업할 수 있을까요?"),
    ("05", "question", "이 코드는 GitHub에 공개되어 있나요?"),
    ("06", "question", "API 비용은 한 달에 얼마나 나오나요?"),
    ("07", "question", "로컬 GPU 없이도 이 작업이 가능한가요?"),
    ("08", "question", "지난주에 만든 영상 길이가 몇 분이었죠?"),
    ("09", "question", "Remotion하고 After Effects 중에 뭐가 더 빠른가요?"),
    ("10", "question", "방금 말씀하신 자료는 어디서 받을 수 있나요?"),

    ("11", "command", "코엠씨, 방금 질문 다시 한번 읽어줘."),
    ("12", "command", "코엠씨, 지금까지 나온 질문 세 개만 요약해줘."),
    ("13", "command", "코엠씨, 다음 파트로 넘어가자."),
    ("14", "command", "코엠씨, 이 주제는 나중에 다루겠다고 안내해줘."),
    ("15", "command", "코엠씨, 채팅창에서 반복되는 질문 찾아줘."),
    ("16", "command", "코엠씨, 지금 몇 분 지났는지 알려줘."),
    ("17", "command", "코엠씨, 그 답변은 근거가 없으니까 하지 마."),
    ("18", "command", "코엠씨, 오늘 런다운 3번 파트 내용 확인해줘."),
    ("19", "command", "코엠씨, 시청자 이름은 부르지 말고 답해줘."),
    ("20", "command", "코엠씨, 여기서 잠깐 멈춰줘."),
]

WAKE_WORD = "코엠씨"

# WER 계산 시 정답/가설 양쪽에서 제거할 문자 (구두점 차이로 오류율이 부풀지 않게)
PUNCT = ",.?!·…\"'`~"


def normalize(text: str) -> str:
    """WER 비교용 정규화. 구두점 제거 + 공백 정리 + 소문자화.

    영문 기술 용어의 대소문자(GitHub vs github)나 물음표 유무로
    오류를 세면 실제 알아들었는지와 무관한 수치가 나온다.
    """
    for ch in PUNCT:
        text = text.replace(ch, " ")
    return " ".join(text.lower().split())


def by_id(uid: str):
    for u in UTTERANCES:
        if u[0] == uid:
            return u
    raise KeyError(uid)


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    q = sum(1 for _, t, _ in UTTERANCES if t == "question")
    c = sum(1 for _, t, _ in UTTERANCES if t == "command")
    print(f"문장 {len(UTTERANCES)}개 — 질문형 {q} / 명령형 {c}")
    print(f"호출어 '{WAKE_WORD}' 포함: "
          f"{sum(1 for _, _, s in UTTERANCES if WAKE_WORD in s)}개")
    for uid, typ, s in UTTERANCES:
        print(f"  {uid} [{typ[:4]}] {s}")
