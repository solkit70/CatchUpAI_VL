# WorkLog - M1: AI 에이전트 서비스 정체 확인

**날짜**: 2026-10-04
**Topic**: AI-Agent-Apps-Compare
**모듈**: M1 - 네 서비스 정체 확인 (초기 진행 후 갱신)
**학습 시간**: Live #30 방송 중 (Topic 시작 · Roadmap 생성 포함, M1 조사 ~07:42 PDT)

> 아래 진행 과정과 회고는 2026-10-04 방송 당시의 기록이다. 2026-10-09 갱신 기준과 현재 산출물은 하단 「범위 업데이트」를 우선한다.

## 🎯 오늘의 학습 목표

- [x] 네 비교 대상의 만든 회사 · 공식 URL · 공개된 출시/접근 정보 확인 (Instinct의 미확정 사항은 별도 표시)
- [x] 서비스 카드 4장
- [x] 확인 필요 목록
- [x] 모듈 README · WorkLog

## 📚 진행 내용

### 1. Topic 시작 · Roadmap

**과정**: 방송 중 만든 시작 프롬프트로 `topic_starter.md` → `roadmap_prompt.md`(템플릿 그대로, [1단계]만 채움) → 기간 검토(1~2주 「그대로 진행」) → 6개 모듈 Roadmap → `daily_learning_prompt.md`. 사용자 요청으로 학습 목적에 「모든 작업이 끝나면 그 결과로 영상을 만든다」를 넣고 M6 를 Capstone 영상으로 정했다.

### 2. 공식 페이지 찾기

**과정**:
1. 세 서비스를 웹 검색으로 찾고 회사를 고정했다 — Grok Bot = xAI, Muse = Meta, Dots = OpenAI
2. 공식 페이지를 직접 열었다: docs.x.ai ✅ · about.fb.com ✅ · openai.com · help.openai.com ❌(403)
3. 403 인 OpenAI 는 공식 도움말의 검색 요약 + 언론 보도로 교차 확인했다

**결과**: [vl_materials/official-sources.md](../vl_materials/official-sources.md)

**메모/인사이트**: 방송 전에 「Dots 는 무료로 써 볼 수 있을 것」이라고 기대했지만, **Pro · Business Premium 전용**이었다. 무료 실습 대상은 Muse 하나로 줄었다.

**범위 조정 (사용자 결정)**: 박창수는 ChatGPT Pro 사용자라 새 결제 없이 Dots 를 쓸 수 있다 → **Dots 도 실습 범위에 포함**. 규칙은 「무료만」에서 「새 결제 없음 — 무료 플랜 + 이미 쓰는 구독」으로 바꿨다. Grok Bot 만 조사 · 비교.

### 3. 한 줄 카드 (10/4 당시 세 장, 현재 네 장으로 갱신)

**결과**: [01-Identify-Services/guides/service-cards.md](../01-Identify-Services/guides/service-cards.md) · [concepts/agent-vs-chatbot.md](../01-Identify-Services/concepts/agent-vs-chatbot.md)

## 🐛 문제 해결 로그

### 문제 1: OpenAI 공식 페이지 자동 읽기 차단

**증상**: openai.com · help.openai.com 이 HTTP 403
**원인**: 자동 수집 차단
**해결**: 도움말 검색 요약과 언론 보도로 교차 확인하고, 원문 확인은 「확인 필요」로 남겼다 (브라우저로 직접 열기)

### 문제 2: Grok Bot 접근 플랜 정보 불일치

**증상**: 요약 사이트는 「SuperGrok Heavy · Cursor Ultra 만」, 공식 문서는 「모든 유료 Cursor 개인 플랜 · SuperGrok」
**해결**: 공식 문서 기준으로 기록하고 불일치를 카드에 남겼다. 어느 쪽이든 무료는 아니다

## 📊 DoD 체크리스트

- [x] 네 서비스 카드 작성 (회사 · 공식 URL · 한 줄 설명 · 접근 방법)
- [x] 모든 사실에 출처 + 확인 날짜 (OpenAI 원문은 확인 필요로 표시)
- [x] 동명 제품 구분 표시
- [x] 「확인 필요」 목록 정리
- [x] 모듈 README 작성
- [x] 🔴 README 링크 확인 (`check_links.py`) — 깨짐 0
- [x] WorkLog + Daily Retrospective 작성

**완료율**: 7/7 (100%)

## 💡 Daily Retrospective

### What went well (잘된 점)
- 방송 중에 Topic 시작부터 M1 완료까지 한 번에 진행했다
- 요약 사이트와 공식 문서가 다를 때 공식 기준으로 정리하는 원칙이 바로 효과를 냈다

### What could be improved (개선할 점)
- OpenAI 처럼 자동 읽기가 막힌 공식 페이지는 방송 화면에서 직접 열어 보여 주는 편이 낫다

### Insights (인사이트)
- 세 회사가 같은 달에 같은 구조(전용 클라우드 컴퓨터 + 승인 경계)의 에이전트를 냈다 — 「답하는 AI」에서 「일을 맡는 AI」로의 전환이 업계 공통 흐름이다
- 하지만 무료로 쓸 수 있는 건 Meta 하나 — 「누구나 써 볼 수 있느냐」가 시청자에게는 가장 중요한 비교 기준이다

### Tomorrow's focus (내일 집중할 것)
- M2: 확인 필요 1 · 3 · 4 해결, 다섯 기준 비교표
- M3 준비: Muse 가입은 사용자가 직접 (미국 · 성인 대상 확인) · ChatGPT 데스크톱 앱/웹에 Dots 안내가 떴는지 확인 (점진 출시)

## 🔄 범위 업데이트 (2026-10-09)

M1을 진행한 뒤 비교 대상과 사용 조건이 바뀌어 현재 산출물을 갱신했다. 비교 대상은 기존 세 서비스(Grok Bot · Muse · Dots)에 **Instinct**를 추가해 네 개로 정리했다. Instinct의 공식 페이지는 문자·전화로 개인 업무를 맡기는 비서라고 설명하며, 회사명은 개인정보 정책의 법인 표기인 Spear Street Technology, Inc.로 기록했다. 출시 시점·초대 정책 등 공식 페이지에서 확인되지 않는 세부사항은 확정하지 않고 확인 필요로 남겼다.

ChatGPT Plus로는 Dots를 사용할 수 없으므로 이전 WorkLog의 「Pro 사용자라 실습에 포함」 기록은 당시 잘못 파악했던 내용을 보존하는 역사적 메모로 남기고, 현재 판정은 **조사·비교만**으로 정정했다. Instinct도 대기 명단 승인 전까지 조사·비교만 한다. M1 카드와 README를 네 서비스 기준으로 갱신했다.

**확인 자료**: [Instinct 공식 소개](https://instinct.com/) · [개인정보 정책](https://instinct.com/privacy-policy) · [서비스 약관](https://instinct.com/terms). 공식 소개·정책 확인일: 2026-10-09.

### 갱신 후 상태

- M2의 네 서비스 비교표와 승인·개인정보 비교도 2026-10-09에 갱신했다.
- Instinct의 공식 접근·가격·초대 조건은 확인되지 않은 부분을 미확정으로 표시한다.

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `topic_starter.md` · `vl_prompts/` · `vl_roadmap/` — Topic 설정
- `01-Identify-Services/` — M1 산출물
- `vl_materials/official-sources.md` — 출처 목록

**작성자**: 박창수 + Claude Code
**방법론**: VibeLearn AI
