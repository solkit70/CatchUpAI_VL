---
title: "Muse 검증 결과 — link-traversal-test"
author:
  - Muse
created: 2026-11-18 06:28:55
visibility: internal
original_sha256: "ea6df7bf089150412e6619aff341a5ca303783d56edf61bedfda489ad4b859a0"
tags:
  - muse-my-workflow
  - research-verification
---

# KSDD-2026 Link Traversal Test (그래프 링크 추적 테스트)

**작성일:** 2026-11-18 (수) 오전 · **테스트일:** 2026-11-18
**목적:** 사용자 로컬 Obsidian 볼트의 그래프(위키링크) 구조를 Muse가 Dropbox에서 따라갈 수 있는지, 실제 질문 하나로 검증한다. 시작 노트 → 실제로 연 링크 대상의 경로·인용을 기록한다.
**저장 위치:** `~/workspace/goals/k-startup-demo-day-in-seattle/KSDD-2026/link-traversal-test.md` (Muse 내부, Dropbox 파일 수정 없음)

---

## 1. 선택한 질문

**"재외동포청에서 오시는 분들은 어떤 분들인가요?"** (사용자가 11/17 10:41 현장에서 실제로 한 질문)

이 질문을 고른 이유: 11/17 1차 답변이 "개별 이름은 확인한 자료에 없어요"였고, 5분 뒤 명단 시트로 해결됐다. 그래프 추적만으로 어디까지 답할 수 있었는지, 그리고 그 한계가 무엇인지 보이기 좋은 질문이다.

---

## 2. 시작 노트

- **Vault 경로 (노트 안의 링크 기준):** `AI/Initiatives/KACCWA/20261013_Startups/2026-10-13 K-Startup Demo in Seattle 한국 선정 5개 스타트업 자료 정리 by Claude Code.md`
- **Dropbox 경로 (대응):** `/KACCWA/20261013_Startups/2026-10-13 K-Startup Demo in Seattle 한국 선정 5개 스타트업 자료 정리 by Claude Code.md`
- **대응 규칙:** Vault 경로에서 접두사 `AI/Initiatives/`를 떼면 Dropbox `/KACCWA/` 아래 경로가 된다. 11/18 fetch로 확인: 8,104자, 위키링크 `[[...]]` 15개, 마크다운 링크 0개.
- **시작 노트의 링크 목록 (전수, 11/18 fetch 기준):**

| # | 링크 (Vault 경로) | Dropbox 대응 | 분류 |
|---|---|---|---|
| 1 | `AI/Initiatives/KACCWA/20261012_Program/2026-10-12 K-Startup Demo in Seattle 참가안내 최종본 정리와 초안 대비 변경점 by Claude Code` | `/KACCWA/20261012_Program/2026-10-12 K-Startup Demo in Seattle 참가안내 최종본 정리와 초안 대비 변경점 by Claude Code.md` | 범위 내 — 파일 존재 확인됨 (11/18 목록 조회) |
| 2 | `AI/Initiatives/KACCWA/20261011_Meeting/2026-10-11 K-Startup Demo Day 초청 현황과 박창수 액션 아이템 by Claude Code` | `/KACCWA/20261011_Meeting/2026-10-11 K-Startup Demo Day 초청 현황과 박창수 액션 아이템 by Claude Code.md` | 범위 내 — **이번 테스트에서 실제로 따라감 (아래 3절)** |
| 3 | `Tasks/items/2026-10-07 KACCWA K-Startup Demo Day 초청 및 행사 준비` | (Dropbox에 없음) | **범위 밖 — 확인할 항목** |
| 4 | `AI/Initiatives/KACCWA/20261013_Startups/01 이플로우 (EFLOW)/이플로우 영문 회사소개서.pdf` | `/KACCWA/20261013_Startups/01 이플로우 (EFLOW)/이플로우 영문 회사소개서.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 5 | `AI/Initiatives/KACCWA/20261013_Startups/01 이플로우 (EFLOW)/이플로우 영문 IR 피치덱.pdf` | `/KACCWA/20261013_Startups/01 이플로우 (EFLOW)/이플로우 영문 IR 피치덱.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 6 | `AI/Initiatives/KACCWA/20261013_Startups/02 세라 (SERA)/세라 영문 회사소개서 (1장).pdf` | `/KACCWA/20261013_Startups/02 세라 (SERA)/세라 영문 회사소개서 (1장).pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 7 | `AI/Initiatives/KACCWA/20261013_Startups/02 세라 (SERA)/세라 영문 IR.pdf` | `/KACCWA/20261013_Startups/02 세라 (SERA)/세라 영문 IR.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 8 | `AI/Initiatives/KACCWA/20261013_Startups/03 컴포지터 (COMPOSITER)/컴포지터 영문 회사소개서.pdf` | `/KACCWA/20261013_Startups/03 컴포지터 (COMPOSITER)/컴포지터 영문 회사소개서.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 9 | `AI/Initiatives/KACCWA/20261013_Startups/03 컴포지터 (COMPOSITER)/컴포지터 영문 IR 2026 Q3.pdf` | `/KACCWA/20261013_Startups/03 컴포지터 (COMPOSITER)/컴포지터 영문 IR 2026 Q3.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 10 | `AI/Initiatives/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 영문 회사소개서 (Deep Tech Networking Day 2026).pdf` | `/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 영문 회사소개서 (Deep Tech Networking Day 2026).pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 11 | `AI/Initiatives/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 회사소개 (1장 · Series A 개요).pdf` | `/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 회사소개 (1장 · Series A 개요).pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 12 | `AI/Initiatives/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 IP Stack 요약 (영문 1장).pdf` | `/KACCWA/20261013_Startups/04 보이노시스 (VOINOSIS)/보이노시스 IP Stack 요약 (영문 1장).pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 13 | `AI/Initiatives/KACCWA/20261013_Startups/05 소프티오닉스 (Softionics)/소프티오닉스 회사소개 (1장).pdf` | `/KACCWA/20261013_Startups/05 소프티오닉스 (Softionics)/소프티오닉스 회사소개 (1장).pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 14 | `AI/Initiatives/KACCWA/20261013_Startups/05 소프티오닉스 (Softionics)/소프티오닉스 영문 IR 피치덱.pdf` | `/KACCWA/20261013_Startups/05 소프티오닉스 (Softionics)/소프티오닉스 영문 IR 피치덱.pdf` | 범위 내 — 폴더 존재 확인됨, 개별 파일 미대조 |
| 15 | `AI/Initiatives/KACCWA/20261013_Startups/2026-10-13 한국 선정 5개사 참가자 연락처.txt` | `/KACCWA/20261013_Startups/2026-10-13 한국 선정 5개사 참가자 연락처.txt` | 범위 내 — 11/17 fetch로 이미 읽음 |

- **시작 노트 자체의 OKA 관련 내용:** 시작 노트는 5개사 자료 정리라 재외동포청 참석자 이름을 직접 적고 있지 않다. 그래서 2번 링크(초청 현황 노트)를 따라간다. 이것이 그래프 추적의 실제 동작이다 — 답이 없는 노트에서 답이 있는 노트로 링크를 따라 이동한다.

---

## 3. 실제로 따라간 링크 (1 hop)

- **따라간 링크:** `[[AI/Initiatives/KACCWA/20261011_Meeting/2026-10-11 K-Startup Demo Day 초청 현황과 박창수 액션 아이템 by Claude Code|초청 현황과 박창수 액션 아이템]]`
- **Dropbox 경로:** `/KACCWA/20261011_Meeting/2026-10-11 K-Startup Demo Day 초청 현황과 박창수 액션 아이템 by Claude Code.md`
- **확인 방법:** 11/18 `list_folder /KACCWA/20261011_Meeting`으로 파일 존재 확인 후 `fetch`로 읽음. 8,090자.
- **문서 기준일:** 2026-10-11 23:30 작성 (front matter `created`). 상태 "📋 박창수 확인 대기". `visibility: internal`, 본문 상단 "🔒 내부 자료 — 임원방 대화와 내부 일정이 들어 있어 볼트 밖으로 내보내지 않는다."

### 대상 노트에서 가져온 인용 (질문과 직접 관련)

> "한눈에 보면 **확정된 것은 한국 선발 5개 팀뿐**이고, 로컬 스타트업 5팀 · VC · 재외동포청 인사는 모두 아직 후보 단계다." (Summary)

> "| 재외동포청 인사 | 「동포청에서 오시는 누가 오시든」 | 인물 미정 | **정해진 것 없음** | [00:36:35] |" (1절 둘째 날 오전 행사 표)

> "| 오전 연사 · 내빈 | 5자리: 환영사 · 재외동포청 인사 · 총영사 축사 · KSC 센터장(Why Seattle) · 키노트 겸 투자자 세미나 | 환영사(오명규 회장) 1 | … | 재외동포청에서 누가 오는지 미정 |" (한눈에 보는 현황 표)

### 추적 결과 — 질문에 대한 답 (10/11 시점)

- **그래프 추적만으로 얻을 수 있는 답:** 10/11 시점에서는 재외동포청에서 누가 오는지 **미정**이었다. 인물 미정, 정해진 것 없음. 11/17 10:41 1차 답변("개별 이름은 확인한 자료에 없어요")과 일치한다.
- **추적의 한계 (중요):** 이 노트는 10/11 작성이다. 링크를 따라가면 **10/11 상태**를 얻을 수 있을 뿐, 11/15 명단 시트(김명호·전소윤 주무관, 전 일정 참석)라는 최신 상태를 얻을 수 없다. 그래프는 관계를 따라가지만 **최신성을 보장하지 않는다.** 최신 명단은 링크가 아니라 사용자가 공유한 시트에서 왔다. 그래서 답할 때는 "이 노트 기준 10/11에는 미정이었다"는 문서 기준일을 함께 밝혀야 한다.
- **2 hop 후보 (이번 테스트에서는 따라가지 않음):** 대상 노트의 `sources`에는 `[[AI/Initiatives/KACCWA/20261011_Meeting/2026-10-11 KACCWA Seattle Partners K-Startup Demo Day Prep Meeting Summary|10/11 회의 요약]]` 등이 있다. 해당 파일은 `/KACCWA/20261011_Meeting/` 목록에 존재함이 확인됐다. 필요하면 다음 hop으로 따라갈 수 있다.

---

## 4. 확인할 항목으로 남기는 것

### 범위 밖 링크 (Dropbox에 없어 따라갈 수 없음)

| 링크 | 상태 | 필요한 조치 |
|---|---|---|
| `Tasks/items/2026-10-07 KACCWA K-Startup Demo Day 초청 및 행사 준비` (시작 노트 #3) | Dropbox 루트에 `Tasks` 폴더 없음 (11/18 확인 — 루트에는 `KACCWA`와 `Muse M4 Test - Synthetic`만 있음) | `Tasks/items/` 폴더를 Dropbox에 올리면 따라갈 수 있다. 사용자가 올릴지 결정할 일 |
| `Ingest/Transcripts/2026-10-11_KACCWA_KSDD_Prep/2026-10-11 KACCWA Seattle Partners K-Startup Demo Day Prep Meeting - speaker-labeled transcript (draft)` (대상 노트 sources) | Vault 루트 기준 경로. Dropbox에 `Ingest` 폴더 없음 | `Ingest/` 폴더를 올리면 따라갈 수 있다. 전사 원문이 필요할 때만 |
| `Tasks/items/2026-10-07 KACCWA K-Startup Demo Day 초청 및 행사 준비` (대상 노트 related — 시작 노트 #3과 동일) | 상동 | 상동 |

### 동명·유사명 파일 (구별이 필요한 것)

| 파일 A | 파일 B | 구별 |
|---|---|---|
| `/KACCWA/20261011_Meeting/2026-10-11 KACCWA 36대 임원방 대화 정리 by Claude Code.md` | `/KACCWA/20261012_Program/2026-10-12 KACCWA 36대 임원방 대화 정리 - 회장 한국 방문 제안 by Claude Code.md` | 날짜(10-11 vs 10-12)와 부제(- 회장 한국 방문 제안)가 다르다. 같은 "임원방 대화 정리"라는 이름으로 부르면 안 된다. 전체 경로로 구별할 것 |
| 폼 가이드 2개: `2026-11-05 KSDD 참석자 명단 구글 폼 제작 가이드 by Claude Code.md` (v3 시트 표 방식) vs `2026-11-05 KSDD 참석자 명단 개선 폼 제작 가이드 by Claude Code.md` (v4 개선 폼) | 제목이 비슷하고 둘 다 "제작 전"이다 | v3/v4를 구별할 것. 실제 폼과 무관한 절차서라는 점도 함께 밝힐 것 (`call-review.md` 5-1절) |

### 경로 표기 변형 (확인할 항목)

- v4 가이드의 `related`에 `[[Initiatives/KACCWA/20261105_Form/2026-11-05 KSDD 참석자 명단 구글 폼 제작 가이드 by Claude Code|시트 표 방식 가이드]]`가 있다. 다른 링크의 `AI/Initiatives/...`와 달리 `AI/` 접두사가 없다. 같은 파일을 가리키는 것으로 보이나, 접두사 없는 표기가 볼트에서 어떻게 해석되는지는 미확인이다. 그래프 인덱스를 만들 때 표기 변형을 정규화할 항목으로 남긴다.

### 개별 존재 미대조 (폴더는 확인, 파일은 미대조)

- 시작 노트의 회사 PDF 링크 11개 (#4–#14): 상위 폴더(01 이플로우 ~ 05 소프티오닉스) 존재는 11/18 목록 조회로 확인했으나, PDF 파일 각각의 존재는 대조하지 않았다. 그래프 인덱스 구축 시 전수 대조할 항목이다.

---

## 5. 테스트 결론

- **따라가기는 된다.** 시작 노트(8,104자, 링크 15개)에서 초청 현황 노트(8,090자)까지 1 hop 추적이 실제로 동작했고, 질문에 대한 10/11 시점의 답(인물 미정)을 인용과 함께 가져왔다.
- **대응 규칙이 통한다.** Vault `AI/Initiatives/KACCWA/...`에서 접두사를 떼면 Dropbox `/KACCWA/...`가 된다. 이번에 따라간 링크는 그대로 맞아떨어졌다.
- **한계도 확인됐다.** (1) 링크는 최신성을 보장하지 않는다 — 10/11 노트는 11/15 명단 시트의 최신 상태를 모른다. 문서 기준일을 답에 함께 밝혀야 한다. (2) `Tasks/items/`, `Ingest/` 같은 볼트 내 다른 폴더 링크는 Dropbox에 없어 끊긴다. (3) 링크 없는 관련 자료(예: 10/14 숙박 기록)는 그래프로 찾을 수 없다 — 키워드 검색과 병행해야 한다.
- **다음 단계:** 전체 MD의 링크·백링크·한 줄 요약을 뽑은 그래프 인덱스를 만들면, 질문마다 탐색하지 않고 인덱스에서 출발할 수 있다. 그때 위 "확인할 항목"들(범위 밖 링크, 동명 파일, 표기 변형, PDF 개별 존재)을 함께 정리한다.
