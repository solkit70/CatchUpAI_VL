---
title: M1 WorkLog — 2026-06-28
module: M1 - GobiSpace Agents 설정 마스터
session: 1
date: 2026-06-28
tags:
  - bila-ai-agent
  - m1
  - worklog
---

# M1 WorkLog — GobiSpace Agents 설정 마스터

## 세션 정보

| 항목 | 내용 |
|------|------|
| 날짜 | 2026-06-28 (토) |
| 상황 | Live #16 방송 중 실험① 세션 |
| 모듈 | M1 - GobiSpace Agents 설정 마스터 |
| 예상 시간 | 3h (방송 중 20분 + 이후 추가) |
| 참조 로드맵 | `vl_roadmap/20260628_RoadMap_Bila-AI-Agent.md` |

## 오늘의 목표

- [x] M1 학습 세션 시작 (WorkLog 생성)
- [x] 원본 시스템 프롬프트 분석 (system_prompt_mention.md, system_prompt_chat.md)
- [x] BL 전용 Agent Prompt 설계 (mention/chat 두 버전)
- [x] agents-tab-guide.md 작성
- [x] GobiSpace Agents 탭 → System Prompt 실제 교체 완료 (다람쥐 → BL 전용)
- [ ] 실습2: BL 관련 질문 5개 응답 품질 테스트

---

## 실습1 기록: BL 전용 시스템 프롬프트 설계

### 분석 결과: GobiSpace 프롬프트 구조

GobiSpace는 **두 레이어** 프롬프트로 구성:

| 레이어 | 내용 | 제어 방법 |
|--------|------|----------|
| 기본 프롬프트 | "You are the agent for Changbal..." (자동 생성) | 변경 불가 (플랫폼 자동) |
| Agent Prompt | UI Settings 필드에 입력한 커스텀 지시 | ✅ 우리가 제어 가능 |

**@mention 핸들**: `@Bila AI` (에이전트 표시 이름 기반, 스페이스 슬러그 @changbal 아님)
**채팅 진입**: 화면 우하단 말풍선 버튼 클릭 → 별도 채팅창 (@mention 불필요)

**GobiSpace mention/chat 별도 프롬프트 지원 — 확인됨** (2026-06-28 스크린샷):
- mention 버전 Agent Prompt: `항상 농담과 함께 답변해줘` (다람쥐 없음 → mention 응답에서 확인)
- chat 버전 Agent Prompt: `항상 농담과 함께 답변해줘. 각 문장마다 다람쥐 라는 말로 끝내 줘.` (채팅 응답에 다람쥐 있음 → 확인)

→ Agents 탭에 mention/chat 별도 입력 필드 존재 (기존 추정 "단일 필드"는 오류였음)

### BL 전용 Agent Prompt 설계 결과

설계 파일:
- `01-Agents-Setup/system_prompt_BL_mention.md` — mention 트리거용
- `01-Agents-Setup/system_prompt_BL_chat.md` — 채팅 대화용
- `01-Agents-Setup/agents-tab-guide.md` — Settings 탭 적용 가이드

**GobiSpace 적용 완료** (2026-06-28):
- System prompt 교체 완료 → 다람쥐 없음 확인
- mention(`@Bila AI`) + 채팅(말풍선) 모두 동일 프롬프트 적용 확인
- **Language = Auto** (이전: Korean → 변경됨, 사용자가 Auto로 설정)
- System prompt 필드는 단일 필드 (mention/chat 구분 없음) — 최종 확인

### 추가 확인 사항 (2026-06-28 스크린샷)

| 항목 | 확인 결과 |
|------|---------|
| System prompt 필드 수 | 1개 (단일 — mention/chat 공통) |
| Language 설정 | Auto (질문 언어에 따라 자동) |
| 다람쥐 제거 | ✅ mention + chat 모두 없음 |
| 일반 질문 응답 (시간) | ✅ 정상 응답 확인 |

---

## 실습2 기록: 5개 질문 응답 품질 테스트 (완료)

### 테스트 결과 요약

| # | 질문 | 판정 | 비고 |
|---|------|------|------|
| 1 | BL 다음 모임은 언제인가요? | ✅ 합격 | 7월 6일(월) 오후 6시, IT/AI 커피챗 정확히 인용 |
| 2 | BL에 새로 가입하려면 어떻게 해야 하나요? | ✅ 합격 | 포스트에 없다고 솔직히 밝히고 운영진 문의 안내 |
| 3 | 7월 6일 커피챗에 대해 알려줘 | ✅ 합격 | 워싱턴주 한인 상공회의소 주선, 포스트 링크 제공 |
| 4 | BL에서 어떤 종류의 활동이 있나요? | ✅ 합격 | 세미나, 네트워킹, 지식공유 요약 + 포스트 확인 안내 |
| 5 | 당신은 무엇을 도와줄 수 있나요? | ✅ 합격 | BL AI 코디네이터 역할과 범위 명확히 설명 |

**최종 점수**: 5/5 합격

---

## 한계 및 관찰 (실습2에서 발견)

- [x] **한계 1 — 온보딩 정보 부재**: 가입 절차 질문에 포스트에서 찾을 수 없다고 답변. 스페이스 포스트에 구조화된 온보딩 정보가 없으면 안내 불가 → 해결책: 온보딩 안내 포스트 작성 또는 Vault 연결(M2)
- [x] **한계 2 — 소스 혼용 가능성**: 활동 종류 질문 답변이 About this space 설명 + 포스트 혼용인지 불명확. 포스트만 기반인지 확인 어려움
- **관찰 1**: "창발 빌라의 다음 모임" → "창발"과 "Bila"를 혼용하는 표현 발생. 스페이스 명칭 혼선 가능
- **관찰 2**: 소스 링크를 "(링크)"로 표기하나 실제 클릭 가능한 하이퍼링크로 렌더링됨 → 양호

---

## DoD 체크리스트 (M1) — 완료

- [x] BL 전용 시스템 프롬프트 (mention/chat) 설계 문서 작성
- [x] GobiSpace Agents 탭 → System Prompt 교체 완료 (다람쥐 → BL 전용)
- [x] agents-tab-guide.md 작성
- [x] 5개 기본 질문 응답 품질 검증 완료 (5/5 합격)
- [x] 응답 한계 2개 이상 확인 및 기록
- [x] M1 WorkLog 최종 완성

**M1 완료일**: 2026-06-28

---

## M2 준비 — Next Focus

**M2: 데이터 소스 연결 & Phase 1 구현** (⭐⭐, 예상 4h)

M1에서 확인된 한계 해결:
- 실습1: GitHub 레포 연결 (`solkit70/builders-lounge-personal-notes`) → 코드/기록 접근
- 실습2: Google Drive 연결 (BL 회의록 폴더) → 구조화된 문서 접근
- 실습3: 온보딩 정보 포스트 작성 후 Phase 1 최종 10개 Q&A 검증

**전제 조건**: GitHub 레포 준비 + Google Drive BL 공유 폴더 확인
