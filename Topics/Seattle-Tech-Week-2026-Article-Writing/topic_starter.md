# VibeLearn AI Topic Starter - Seattle-Tech-Week-2026-Article-Writing

> **개정 이력**: 2026-08-12 v2로 개정. v1은 외부 2차 자료만으로 기사를 작성해 현장 트랜스크립트 30개를
> 한 줄도 쓰지 않았다. v2는 1차 자료 정독을 출발점으로 재설계한다. v1 원문의 미치환 플레이스홀더
> (`$topicName`, `$source1`, `$source2`)도 이번에 수정했다.

## 📌 Topic 기본 정보

Topic 이름: Seattle-Tech-Week-2026-Article-Writing

설명: (v2 재진행) Seattle Tech Week 2026을 취재 기반 기사 연재로 완성하는 Topic이다. v1은 GeekWire·Madrona·McKinsey·Gartner 등 외부 2차 자료만으로 기사 초안을 만들었고, 사용자가 직접 참석·녹화·업로드한 현장 트랜스크립트 30개(8,703줄)를 한 줄도 인용하지 않았다. 그 결과 현장에 가지 않은 사람도 쓸 수 있는 문헌 리뷰가 되었고, 생동감과 기고 가치가 부족했다. v2의 전제는 명확하다. 이 기사의 유일한 차별점은 사용자가 그 자리에 있었다는 사실이다. 따라서 1차 자료를 전량 정독해 인용·장면·수치를 채굴하는 것이 출발점이며, 외부 자료는 전면이 아니라 배경으로 강등한다. 최종 산출물은 한인 매체 기고용 한국어 연재 2~3편이다.

학습 목적:
- 현장 트랜스크립트 30개(8,703줄)를 전량 정독해 인용 가능한 발언·구체 수치·장면을 Evidence Bank로 구축한다
- 외부 2차 자료를 기사의 전면이 아니라 배경 근거로 재배치한다
- 현장 증거를 중심으로 한인 매체 기고용 한국어 연재 2~3편을 설계하고 집필한다
- 모든 인용을 트랜스크립트 원문과 대조해 화자명·소속·수치의 정확성을 보장한다
- v1이 실패한 원인(로드맵에 1차 자료 정독 과제가 없었음)을 방법론 차원에서 교정한다

예상 기간: 1.5~2주 (총 13~16시간, 1차 자료 채굴 5~6시간 + 연재 구조 설계 2~3시간 + 집필 4~5시간 + 검증/기고 패키지 2시간)

## 🎯 학습 목표

- [ ] 현장 트랜스크립트 30개에서 인용 가능한 발언을 타임스탬프·화자·소속과 함께 추출할 수 있다
- [ ] 추상적 주장 대신 구체적 장면과 수치로 트렌드를 입증할 수 있다
- [ ] 외부 2차 자료를 현장 증거의 배경으로 배치하는 구조를 설계할 수 있다
- [ ] 한인 매체 독자에게 맞는 연재 2~3편의 각 편 역할과 리드를 확정할 수 있다
- [ ] 모든 인용을 원문 대조로 검증하고 기고 가능한 원고 패키지를 만들 수 있다

## 🛠️ 학습 환경

OS: Windows 11

주요 도구 및 기술 스택:
- Claude Code / VibeLearn AI 프로세스
- 로컬 Obsidian Vault: `C:\AI_study\2026\Changsoo_Vault`
- 1차 자료: `Ingest/YouTube/videos/2026/` 내 현장 트랜스크립트 30개 (Whisper 전사, 타임스탬프·화자·소속 메타데이터 포함)
- 기존 v1 산출물: `01-Source-Map-Research/` ~ `04-Synthesis-Report/` (배경 자료로 재사용)
- Markdown 기반 Evidence Bank 및 기사 원고

사전 지식:
필수:
- Seattle Tech Week 2026 현장 참석 경험 (사용자 본인)
- 현장 트랜스크립트 30개의 위치와 메타데이터 구조
- 기사형 콘텐츠의 기본 구조(리드, 근거, 인용, 결론)
- v1 초안의 한계에 대한 이해 (현장 자료 미사용)

권장:
- 한인 매체 기고문의 분량·문체 관행
- 시애틀 AI/스타트업 생태계 배경
- 인용 표기와 팩트체크 기본 원칙

## 📚 참조 자료

**1차 자료 (최우선 — v1에서 미사용)**
- `Ingest/YouTube/videos/2026/` 내 Seattle Tech Week 현장 트랜스크립트 30개 (총 8,703줄)
  - Seattle Spark + AI 4개 / AI Startup Secret Sauce 5개 / Startup425 Eastside Summit 3 5개
  - Startup425 AI Demo Day 9개 / ACM Data Conclave 2개 / InformsCon 3개 / Biuty AI 1개
- `Ingest/YouTube/playlists/ai-startup-pitch-showcases-and-workshops/_index.md`

**v1 산출물 (배경 자료로 재사용)**
- `01-Source-Map-Research/`, `02-Trend-Analysis/`
- `04-Synthesis-Report/01-seattle-tech-week-2026-analysis-report.md` — 2023~2026 연대기 프레임(유효)
- `04-Synthesis-Report/05-main-analysis-article-draft.md` — v1 초안(재작성 대상)

**외부 2차 자료 (배경으로 강등)**
- GeekWire Seattle Tech Week tag: https://www.geekwire.com/tag/seattle-tech-week/
- Madrona 연도별 회고 2023~2025
- McKinsey AI transformation / trust 2026, Gartner 소비자 AI 조사 2026

vl_materials/ 폴더에 추가할 자료:
- `evidence-index.md` — 트랜스크립트 30개 채굴 진행 추적표
- `quote-bank.md` — 인용 후보 원문(영어) + 한국어 번역 + 출처(영상 링크·타임스탬프)
- `numbers-bank.md` — 구체 수치와 맥락
- `article-outlet-notes.md` — 한인 매체 기고 규격 메모

## 🎓 학습 접근 방식

- [x] 실습 중심, 필요한 이론만 (권장)

시간 투자 계획:
- 전체 학습 시간: 13~16시간
- 학습 가능 요일: 필요 시 여러 세션으로 분할
- 1회당 학습 시간: 1~3시간

특별히 집중하고 싶은 영역:
- 1차 자료 정독을 통한 인용·장면·수치 채굴 (v1의 최대 결함 교정)
- 추상 명제가 아니라 구체 증거로 트렌드를 입증하는 서술
- 한인 매체 독자에게 맞는 연재 구성과 각 편의 역할 분담
- 인용 정확성 검증 절차

**Template Version**: 1.0 · **Created**: 2026-08-09 · **Revised**: 2026-08-12 (v2) · **Methodology**: VibeLearn AI
