# M1 — 설치 & 인증 & 핵심 개념

> **모듈 번호**: M1
> **상태**: 완료, CVL 업데이트 완료
> **최초 작성일**: 2026-03-29
> **CVL 업데이트**: 2026-05-10 (GOBI CLI v2.0.12)

## 이 모듈에서 배우는 것

GOBI CLI를 설치하고 인증한 뒤, v2.0.12 기준의 핵심 개념을 이해합니다. 이 모듈의 중심은 `gobi vault init`, device-code 인증, `PUBLISH.md`, Vault/Space/Post/Session/Saved/Draft/Media/Sense의 역할 구분입니다.

## 학습 순서

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/installation-guide.md](concepts/installation-guide.md) | 설치, 인증, `gobi vault init`, `PUBLISH.md` 생성 흐름 |
| 2 | [concepts/core-concepts.md](concepts/core-concepts.md) | v2.0.12 기준 핵심 개념과 전체 명령어 Quick Reference |

## M1 핵심 요약

```text
설치:    npm install -g @gobi-ai/cli  ->  gobi v2.0.12
인증:    gobi auth login / gobi auth status
초기화:  gobi vault init
발행:    PUBLISH.md -> gobi vault publish
동기화:  gobi vault sync
```

핵심 개념:

| 개념 | 역할 |
|---|---|
| Vault | 최상위 지식 컨테이너 |
| PUBLISH.md | `vault publish`의 원본 파일 |
| Space | 커뮤니티 협업 공간 |
| Post/Reply | v0.6.x의 Thread/Reply에 해당하는 협업 단위 |
| Global | 개인 포스트와 글로벌 피드 |
| Session | 1:1 AI 대화 |
| Saved | 개인 노트와 북마크 |
| Draft | 에이전트 standing guidance |
| Media | 이미지/영상 생성 |
| Sense | 활동/전사 데이터 |

## M1 DoD 체크리스트

- [x] GOBI CLI 설치 및 버전 확인
- [x] `gobi auth login/status` 인증 흐름 정리
- [x] `gobi vault init` 기반 Vault 초기화 정리
- [x] `PUBLISH.md` 구조 정리
- [x] `core-concepts.md` v2.0.12 기준 업데이트
- [x] `installation-guide.md` v2.0.12 기준 업데이트
- [x] v0.6.x 명령어와 v2.0.12 명령어 차이 문서화

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| 이전 | - | M1이 첫 번째 모듈 |
| 다음 | M2 — Vault/Global/Session 명령어 | [../02-Brain-Session/README.md](../02-Brain-Session/README.md) |

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
