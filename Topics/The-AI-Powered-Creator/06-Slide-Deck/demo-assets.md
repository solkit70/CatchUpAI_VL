---
title: "데모 자산 목록 — The AI Powered Creator"
created: 2026-06-21 20:00:00
tags:
  - the-ai-powered-creator
  - m6-slide-deck
  - demo-assets
---

# 데모 자산 목록

**발표일**: 2026-06-26 (금)
**사용 슬라이드**: S1~S7 (오프닝 데모), S15 (워크플로우 다이어그램)

---

## 영상 자산 (사용자 제공 예정)

### 완성본 — S1 재생용

| 항목 | 상태 | 설명 |
|------|------|------|
| Tehaleh 소개 영상 MP4 | ✅ 한국어·영어 렌더링 완료 | `tehaleh-intro-0619.mp4`, `tehaleh-intro-0619-en.mp4` |
| YouTube 업로드 | ✅ 한국어·영어 완료 | [한국어 영상](https://youtu.be/Cucvcz9bVPU) · [영어 영상](https://youtu.be/YygPvJbKPvU) |
| YouTube 배포 메타데이터 | ✅ 준비 완료 | 제목, Description, Chapter, 태그 |
| YouTube 썸네일 | 🔄 프롬프트 준비 완료 | 1280×720, `TEHALEH` 포함 한국어 문구 |
| 사전 링크 공지 | ⏳ 발표 D-1 | 참가자에게 링크 공유 |

YouTube 제목, Description, Chapter, 태그, 썸네일 문구와 이미지 생성 프롬프트의 단일 관리 위치는 [[20260621_M1-M4_Tehaleh-Community-Video#YouTube 업로드 메타데이터|Tehaleh 영상 YouTube 업로드 메타데이터]]이다. 이후 배포 문안의 변경과 최종 공개 URL도 이 섹션에 기록하고, 발표에서는 결과물뿐 아니라 메타데이터와 썸네일을 만드는 Distribution 단계까지 제작 사례로 사용한다.

### 5단계 클립 — S3~S7용 (사용자 편집 예정)

| 슬라이드 | 클립 이름 | 소요 시간 | 내용 | 상태 |
|---------|---------|---------|------|------|
| S3 | `clip_01_roadmap.mp4` | 20~30초 | VibeLearn AI Roadmap 작성 화면 | ⏳ 편집 대기 |
| S4 | `clip_02_research.mp4` | 20~30초 | tehaleh-research.md 작성 화면 | ⏳ 편집 대기 |
| S5 | `clip_03_slideplan.mp4` | 20~30초 | video-slide-plan.md 작성 화면 | ⏳ 편집 대기 |
| S6 | `clip_04_remotion.mp4` | 20~30초 | VS Code 코딩 + Remotion Studio 미리보기 | ⏳ 편집 대기 |
| S7 | `clip_05_audio.mp4` | 20~30초 | gen_audio.py 실행 + 렌더링 화면 | ⏳ 편집 대기 |

**클립 편집 가이드**:
- 원본: 이번 Live #15 방송 중 녹화된 작업 화면 5개
- 각 20~30초로 편집 (핵심 동작 부분만)
- 자막 불필요 (슬라이드에 설명 텍스트 표시)
- 클립 저장 위치 (권장): `public/presentation-0626/clips/`

---

## 이미지 자산 (스크린샷)

| 슬라이드 | 자산 | 설명 |
|---------|------|------|
| S3 | VibeLearn AI Roadmap 완성본 스크린샷 | 4개 모듈 구조가 보이는 화면 |
| S4 | tehaleh-research.md 완성 스크린샷 | 6개 섹션 구조 |
| S5 | video-slide-plan.md 스크린샷 | 15장 슬라이드 목록 |
| S8/S9 | CUA_VL 폴더 구조 스크린샷 (선택) | Skills, Topics 구조 |
| S13 | 채널 화면 스크린샷 (선택) | YouTube Catch Up AI |

---

## 다이어그램 자산

| 슬라이드 | 자산 | 위치 |
|---------|------|------|
| S15 | 기록→배포 순환 다이어그램 | `05-Content-Workflow/ai-creator-workflow.md` → Mermaid → 이미지 추출 |

**Mermaid → 이미지 추출 방법**:
1. Obsidian에서 `ai-creator-workflow.md` 열기
2. Mermaid 다이어그램 우클릭 → 이미지로 저장
3. 또는 mermaid.live에서 렌더링 후 PNG 다운로드

---

## 슬라이드 도구 결정 사항

**추천**: Google Slides (클립 삽입 + 실시간 편집 용이)

| 항목 | Google Slides | PowerPoint |
|------|-------------|-----------|
| 클립 삽입 | YouTube 직접 삽입 가능 | MP4 로컬 삽입 |
| 클라우드 | 자동 저장 | 로컬 파일 |
| 발표 현장 | 브라우저로 발표 | 파일 필요 |

---

## 사전 준비 체크리스트

### D-3 (2026-06-23까지)
- [ ] 5개 클립 편집 완료 (`clip_01` ~ `clip_05`)
- [x] Tehaleh 영상 Qwen3-TTS 한국어·영어 최종 오디오 교체 완료
- [x] Tehaleh 영상 한국어·영어 최종 MP4 렌더링 완료

### D-2 (2026-06-24까지)
- [x] 한국어·영어 YouTube 업로드
- [ ] 한국어·영어 커스텀 썸네일 적용 최종 확인
- [ ] 발표 슬라이드 (Google Slides / PPT) 제작 시작
- [ ] S15 Mermaid 다이어그램 이미지 추출

### D-1 (2026-06-25)
- [ ] 슬라이드 최종본 완성
- [ ] 참가자에게 Tehaleh 영상 YouTube 링크 공지
- [ ] 발표 장소 프로젝터 + 오디오 연결 테스트 계획

### D-Day (2026-06-26)
- [ ] 발표 장소 도착 후 화면 연결 확인
- [ ] 클립 재생 테스트 (소리 포함)
- [ ] Tehaleh 영상 재생 테스트

---

*M6 산출물 — 2026-06-21, VibeLearn AI*
