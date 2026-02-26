# Topic: Clearly-BRD-PRD

**방법론**: CUA_VL (VibeLearn AI)
**기간**: 2026-02-01 ~ 2026-02-15
**상태**: ✅ 완료
**총 학습 시간**: 약 9.5시간 (3개 모듈)

---

## 개요

Clearly 앱을 활용한 BRD(Business Requirements Document)와 PRD(Product Requirements Document) 작성 방법론을 학습하고, 실제 프로젝트(Catch Up AI 2026 Homepage)의 BRD/PRD를 작성하여 AI 코딩 도구(Claude Code) 연동까지 완료한 학습 기록입니다.

### 학습 목표 달성

- [x] Clearly 앱의 기능과 사용 방법 이해
- [x] BRD와 PRD의 개념 및 차이점 이해
- [x] Vibe Coding에서 요구사항 문서의 중요성 이해
- [x] 실습을 통해 Catch Up AI 홈페이지 BRD/PRD 작성
- [x] Choose Output Tool을 통한 AI 코딩 도구 연동 (추가 달성)

---

## 모듈 구조

| 모듈 | 제목 | 기간 | 시간 | 상태 |
|------|------|------|------|------|
| M1 | Clearly 개요 및 핵심 개념 | 02/01 | ~3h | ✅ 완료 |
| M2 | Catch Up AI BRD/PRD 실습 | 02/08~02/15 | ~5.5h | ✅ 완료 (3 Sessions) |
| M3 | 문서화 및 사용 가이드 | 02/15 | ~1h | ✅ 완료 |

---

## 폴더 구조

```
Clearly-BRD-PRD/
├── README.md                      # 이 파일 (Topic 전체 소개)
├── topic_info.md                  # Topic 기본 정보
│
├── 01-Clearly-Overview/           # M1 산출물
│   ├── README.md
│   ├── concepts/
│   │   ├── what-is-clearly.md     # Clearly 소개
│   │   ├── brd-vs-prd.md          # BRD vs PRD 비교
│   │   └── vibe-coding-role.md    # Vibe Coding에서의 역할
│   └── guides/
│       ├── clearly-quick-start.md # 빠른 시작 가이드
│       └── clearly-usage-guide.md # 상세 사용 가이드 (M3 산출물)
│
├── 02-CatchUpAI-BRD-PRD/          # M2 산출물
│   ├── README.md
│   ├── brd/                       # BRD 문서 (v1, v2, v3)
│   ├── prd/                       # PRD 문서 (v1, v2)
│   ├── claude-code-output/        # Choose Output Tool 산출물
│   │   ├── .claude/settings.json
│   │   ├── CLAUDE.md
│   │   ├── PRD.md
│   │   └── REFERENCE_DOCUMENT.md
│   └── notes/
│       ├── wizard-experience.md   # Wizard 사용 경험
│       └── clearly-bug-report.md  # 버그 리포트 (4건)
│
├── vl_prompts/                    # 학습 프롬프트
├── vl_roadmap/                    # 학습 로드맵
├── vl_worklog/                    # 학습 일지 (4개 파일)
│   ├── 20260201_M1_Clearly-BRD-PRD.md
│   ├── 20260208_M2_Clearly-BRD-PRD.md
│   ├── 20260214_M2_Clearly-BRD-PRD.md
│   ├── 20260215_M2_Clearly-BRD-PRD.md
│   └── 20260215_Clearly-BRD-PRD_Final_Retrospective.md
└── vl_materials/                  # 참조 자료
```

---

## 핵심 산출물

### 교과서 품질 문서 (다른 학습자를 위한)

| 문서 | 위치 | 설명 |
|------|------|------|
| Clearly 소개 | `01-Clearly-Overview/concepts/what-is-clearly.md` | Clearly가 무엇인지 |
| BRD vs PRD | `01-Clearly-Overview/concepts/brd-vs-prd.md` | 두 문서의 차이점 |
| Vibe Coding 역할 | `01-Clearly-Overview/concepts/vibe-coding-role.md` | 왜 요구사항 문서가 중요한지 |
| **Clearly 사용 가이드** | `01-Clearly-Overview/guides/clearly-usage-guide.md` | 전체 워크플로우 상세 가이드 (핵심) |

### 실습 산출물

| 문서 | 위치 | 설명 |
|------|------|------|
| BRD v3 (최종) | `02-CatchUpAI-BRD-PRD/brd/catchupai-2026-brd-v3.md` | 3회 반복으로 완성된 BRD |
| PRD v2 (최종) | `02-CatchUpAI-BRD-PRD/prd/catchupai-2026-prd-v2.md` | 12개 섹션 상세 PRD |
| Claude Code Output | `02-CatchUpAI-BRD-PRD/claude-code-output/` | AI 코딩 도구 설정 파일 |

### YouTube 소개 영상

| 버전 | 링크 | 길이 |
|------|------|------|
| 🇰🇷 한국어 | [AI가 질문 몇 가지로 BRD/PRD를 만들어준다? \| Clearly 앱 실사용 후기](https://youtu.be/crK2aO_uXkQ?si=pPe0YaNHMnTte_b7) | 16:28 |
| 🇺🇸 영어 | [AI Writes Your BRD & PRD in Minutes? \| Honest Clearly App Review](https://youtu.be/KwQOpU__BKo?si=J2A_irhEPO_tCYPf) | 13:48 |

---

## 핵심 인사이트

1. **반복이 품질을 만든다**: BRD/PRD는 반복(iteration)할수록 품질이 향상됨 (v1 → v2 → v3)
2. **Clearly의 핵심 가치**: BRD/PRD를 AI 코딩 도구 설정 파일로 자동 변환 — Vibe Coding의 출발점
3. **Wizard의 적응성**: 동일 프로젝트도 매번 다른 질문 생성 — AI가 답변 내용에 따라 적응
4. **실전 워크어라운드**: 대시보드 버그 대응으로 항상 로컬 백업 필수

---

## 시작하기

이 Topic의 내용을 따라 학습하려면:

1. `01-Clearly-Overview/concepts/` 폴더의 개념 문서 읽기
2. `01-Clearly-Overview/guides/clearly-usage-guide.md`로 전체 흐름 파악
3. https://www.clearlyreqs.com/ 에서 직접 실습
4. `02-CatchUpAI-BRD-PRD/`의 실제 BRD/PRD를 참고하며 자신의 프로젝트 작성

---

**작성자**: CUA_VL 학습자
**방법론**: CUA_VL (VibeLearn AI)
