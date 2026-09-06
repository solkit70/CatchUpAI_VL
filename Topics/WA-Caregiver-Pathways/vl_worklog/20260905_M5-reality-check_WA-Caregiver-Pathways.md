# WorkLog - M5 확장: 육체적·정서적 현실 점검

**날짜**: 2026-09-05
**Topic**: WA-Caregiver-Pathways
**모듈**: M5 확장 (적합성 판별에 빠져 있던 축 보강)
**상태**: 완료
**작성 시각**: 2026-09-05

## 오늘의 학습 목표

사용자가 M6~M8 실행(교육 등록·지원)을 앞두고 "인간적으로 힘든 부분까지 고민해야 한다"고 판단했다. Perplexity AI에 직접 질문해 받은 종합 답변(`caregiver.txt`)을 근거로, M5 점수표에 없던 **육체적·정서적·대인관계 부담** 축을 하나의 챕터로 정리한다.

## 진행 내용

### 1. 원본 자료 검토

사용자가 제공한 `C:\Users\dougg\Downloads\caregiver.txt`를 전체 읽었다. 미국 caregiver 공통 요건, 목욕·배변 보조의 실제 난이도, 환자의 공격성 원인, 가족과의 관계 부담, 좋은/나쁜 기관 판별법, 자가 점검 질문 등을 담고 있다.

### 2. 기존 조사와 대조

M8에서 이미 확보한 [KWA 공식 직무기술서](../08-Application-and-Hire/examples/KWA%20-%20In-Home%20Caregiver%20Job%20Description%20(2022-08-22).pdf)의 "50 pounds 이상 힘 발휘", "gait belt·Hoyer lift·transfer board" 문구가 Perplexity 답변의 육체적 부담 서술과 정확히 일치함을 확인했다. 일반론이 아니라 **이 Topic이 실제로 지원을 검토 중인 기관의 공식 문서에 그대로 있는 내용**임을 교차 검증했다.

### 3. 산출물 작성

`05-Fit-and-Decision/guides/emotional-and-physical-reality.md`를 새로 작성했다. 10개 절(육체적 부담·심리적 적응·환자 유형별 난이도·감정노동·가족 관계·좋은 기관 판별·면접 질문 추가·자가 점검·보람·결정에 미치는 영향)로 구성하고, 원문은 블록쿼트로 보존했다.

### 4. 기존 문서 연결

- `05-Fit-and-Decision/README.md`에 새 문서를 학습 순서 4번으로 추가, "실행 보류" 섹션 신설
- `decisions/chosen-path.md`에 경고 노트 추가 + 재검토 조건에 항목 추가
- M8 문의 스크립트에 추가해야 할 질문 10개를 새 문서 7절에 정리 (기존 `kwa-firstchoice-application.md`는 아직 수정하지 않음 — 다음 세션에서 사용자가 실제 통화하기 전에 병합 검토)

### 5. 실제 caregiver 증언 조사 (같은 세션 후속 요청)

사용자가 "실제로 이 일을 하는/했던 사람들의 추천 또는 신중히 고려하라는 경험담"을 요청해 웹 조사를 추가했다. Reddit·Glassdoor·Indeed·Quora는 대부분 직접 열람이 봇 차단·유료 장벽으로 막혔다. 직접 열람에 성공한 자료(KUNR 뉴스, Progressive.org, Substack 개인 블로그, PayScale)와 검색엔진 요약으로만 확인한 자료(19thnews.org, Glassdoor, Indeed)를 구분해 `caregiver-testimonials.md`로 정리했다. KWA·First Choice 본인의 재직자 후기는 찾지 못했고, 대신 M4·M8 후보로 이미 등장한 Visiting Angels·Family Resource Home Care의 재직자 평가로 대체했다.

## 문제 해결 로그

| 문제 | 판단 | 처리 |
|------|------|------|
| 이 내용을 어느 모듈에 넣을지 애매함 (M5는 이미 완료 표시됨) | M5가 "적합성 판별"을 다루는 모듈이고, 이 축이 그 판별에 빠져 있던 부분이므로 M5 확장으로 처리. 새 로드맵 모듈을 임의로 만들지 않음 | `05-Fit-and-Decision/guides/`에 배치 |
| Perplexity 응답을 그대로 붙여넣을지, 재구성할지 | 원문 인용 규칙(AGENTS.md)에 따라 핵심 문장은 블록쿼트로 보존하되, 전체는 이 Topic의 실제 후보(KWA)에 맞게 재구성 | 절 구성 시 KWA 공식 문서와 교차 인용 |
| Roadmap.md의 M5 DoD가 이미 7/7로 표시돼 있음 | Roadmap 자체는 수정하지 않고 이 WorkLog와 README 업데이트로 확장 사실을 기록 | Roadmap 미수정 |

## DoD 체크리스트

- [x] 원본 자료(`caregiver.txt`) 전체 검토
- [x] 기존 M8 조사(KWA 공식 문서)와 교차 검증
- [x] `emotional-and-physical-reality.md` 작성 (10개 절)
- [x] M5 README·chosen-path.md에 상호 링크 및 실행 보류 상태 반영
- [x] WorkLog 작성
- [x] 실제 caregiver 증언 조사 및 `caregiver-testimonials.md` 작성 (후속 요청)

**완료율**: 6/6 (100%)

## Daily Retrospective

### What went well

Perplexity 답변을 그대로 붙여넣지 않고, 이미 확보한 KWA 공식 직무기술서와 대조해 "일반론이 아니라 이 기관에 실제로 적용된다"는 근거를 붙일 수 있었다.

### What could be improved

M8 `kwa-firstchoice-application.md`의 문의 스크립트에 이번에 나온 10개 질문을 아직 병합하지 않았다. 실제 통화 전에 병합해야 실행에 바로 쓸 수 있다.

### Insights

M5의 원래 점수표는 "경제적으로 감당 가능한가"만 물었다. "심리·신체적으로 감당 가능한가"는 다른 질문이고, 이건 자료 조사로 대신 답할 수 없다 — 사용자 본인의 성찰이 필요한 유일한 항목이다. VibeLearn 로드맵의 규칙 5(문의는 사용자가 직접)가 여기서도 같은 원칙으로 확장된다: **판단도 사용자가 직접**.

### Tomorrow's focus

- 사용자가 8절 자가 점검 질문에 답을 정리하면 그 결과를 `chosen-path.md`에 반영
- 통화 전에 `kwa-firstchoice-application.md`의 문의 스크립트에 이번 10개 질문 병합
- 실행(KWA/First Choice 지원)을 재개하기로 하면 M8로 복귀

## 참조 및 산출물

- `05-Fit-and-Decision/guides/emotional-and-physical-reality.md`
- `05-Fit-and-Decision/guides/caregiver-testimonials.md`
- `05-Fit-and-Decision/README.md`
- `05-Fit-and-Decision/decisions/chosen-path.md`
- 원본: `C:\Users\dougg\Downloads\caregiver.txt` (Perplexity AI, 2026-09-05)
- 웹 조사 출처는 `caregiver-testimonials.md` 하단 표 참조
