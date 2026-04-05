---
title: "GOBI Vibe Guiding 시스템 맵"
created: 2026-04-03
tags:
  - gobi
  - vibe-guiding
  - system-map
  - reference
---

## 개요

GOBI에 Vibe Guiding을 적용하기 위해 파악하고 활용해야 할 시스템들의 전체 지도.

## 시스템 전체 구조

```
[소스 시스템]                    [문서화]                      [가이딩]
GitHub Repos                      ↓
  gobi-ai/gobi-web          Gobi Specs Sheet           Vibe Guiding
  gobi-ai/gobi-desktop   →  (Core Concept 채우기)  →   (Context → 사용자 안내)
  gobi-ai/gobi-cli              ↓
  gobi-ai/ai4pkm            docs.gobihq.com
  gobi-ai/ai4pkm-cli            ↓
                            User Manual
                         (aiforbetter.me 대체)
```

---

## 1. GitHub 레포지토리 (소스 코드)

| 레포 | 설명 | 접근 권한 |
|------|------|----------|
| gobi-ai/gobi-web | Gobi Space 웹 앱 | ✅ Accept 완료 |
| gobi-ai/gobi-desktop | Gobi Desktop (Mac/Windows) | ✅ Accept 완료 |
| gobi-ai/gobi-cli | Gobi CLI 도구 | 확인 필요 |
| gobi-ai/ai4pkm | AI4PKM Vault | 확인 필요 |
| gobi-ai/ai4pkm-cli | AI4PKM CLI 백엔드 | 확인 필요 |

- **GitHub 계정**: solkit70
- **초대자**: Mika (GitHub: @gpminsuk)

---

## 2. GOBI 제품군 (가이딩 대상)

| 제품 | 설명 | 스펙 시트 탭 |
|------|------|------------|
| Gobi Desktop | Mac/Windows GUI 앱, 로컬 파일 관리 | Gobi Desktop |
| Gobi Space | 웹 기반 팀 협업 공간, 사용자 네트워크 | Gobi Space |
| Gobi CLI | 지식과 Space를 연결하는 CLI 브릿지 | Gobi CLI |
| Gobi Mobile | 모바일 앱 | Gobi Mobile |
| Astra | (세부 파악 필요) | Astra |

---

## 3. 문서화 시스템

### Gobi Specs Google Sheet
- **링크**: https://docs.google.com/spreadsheets/d/1eWGs38ObnjRjOHFY2_Du0TENtM3CSj6I/edit?usp=sharing
- **공유자**: Greg Moon (greg@joingobi.com) — 편집 권한
- **컬럼**: File Name / Description of Spec / Link to Spec / Version / Status / Date Updated / **Core Concept**
- **나의 역할**: Core Concept 컬럼 채우기 (Greg과 협업)
- **탭**: Gobi Desktop / Gobi Space / Astra / Gobi CLI / Gobi Mobile

### docs.gobihq.com
- Greg이 각 제품의 core concepts 추가 중
- Vibe Learning의 인풋 소스로 활용 가능
- **상태**: 작성 중 (내용 파악 필요)

### 기존 사이트 (대체 예정)
- https://www.aiforbetter.me/
- https://pub.aiforbetter.me/

---

## 4. 내가 직접 운영하는 시스템

| 시스템 | 역할 |
|--------|------|
| Claude Code (VS Code) | Vibe Learning 실행, 문서 자동 생성 |
| Changsoo Vault (Obsidian) | 지식 저장소, 아이디어 파편 관리 |
| Gobi Desktop | 로컬 Brain/Context 관리 |
| Gobi CLI | Gobi Space 연동 |

---

## 5. 협업 채널

| 채널 | 용도 | 담당자 |
|------|------|--------|
| Slack (GOBI 팀) | 일상 소통, 작업 공유 | Mika, Greg, Jin |
| GitHub | 소스코드 협업 | Mika (gpminsuk) |
| Google Sheets | Specs 공동 작업 | Greg Moon |
| docs.gobihq.com | 공식 문서 도메인 | Greg |

---

## 6. Vibe Guiding 적용 파이프라인 (목표)

```
GitHub 소스코드
      ↓
Vibe Learning → Core Concept + User Manual 자동 생성
      ↓
CVL (Continuous Vibe Learning) → 코드 변경 시 자동 업데이트
      ↓
Vibe Guiding → 각 GOBI 사용자에게 맞춤 안내 제공
```

---

## 7. 우선순위 파악 필요 항목

- [ ] docs.gobihq.com 접속 및 내용 파악
- [ ] Gobi Specs 시트 — Core Concept 컬럼 채우기 (제품별)
- [ ] gobi-cli, ai4pkm, ai4pkm-cli 레포 접근 권한 확인
- [ ] Astra 제품이 무엇인지 파악
- [ ] Google Learn Your Way 직접 체험 후 설계에 반영
