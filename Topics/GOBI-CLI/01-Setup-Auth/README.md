# M1 — 설치 & 인증 & 핵심 개념

> **모듈 번호**: M1
> **상태**: ✅ 완료
> **예상 학습 시간**: 3-4시간
> **실제 소요 시간**: ~2시간 (2026-03-29)

---

## 이 모듈에서 배우는 것

GOBI CLI를 처음 설치하고 인증하며, 플랫폼의 핵심 개념 5가지를 이해합니다.
이 모듈을 마치면 GOBI CLI를 사용할 준비가 완전히 갖춰집니다.

---

## 학습 순서 (이 순서대로 읽으세요)

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/installation-guide.md](concepts/installation-guide.md) | 설치 → 인증 → vault 초기화 단계별 가이드 |
| 2 | [concepts/core-concepts.md](concepts/core-concepts.md) | Vault / Space / Brain / Session / Thread 핵심 개념 + 전체 명령어 Quick Reference |

---

## M1 핵심 요약

```
설치:    npm install -g @gobi-ai/cli  →  gobi v0.6.15
인증:    gobi auth status  →  이미 로그인됨 (Changsoo Park)
초기화:  gobi init  →  vault "gobi-cli-study" 생성
           생성 파일: .gobi/settings.yaml, BRAIN.md
```

**5개 핵심 개념**:
```
Vault   → 최상위 컨테이너 (= GitHub Org)
Space   → 팀 협업 공간 (= GitHub Repo)
Brain   → AI 지식 자원 (= Wiki + AI)
Session → Brain과의 1:1 대화 (= ChatGPT 대화창)
Thread  → 팀 토론 (= GitHub Issues)
```

---

## M1 DoD 체크리스트

- [x] `npm install -g @gobi-ai/cli` 설치 완료 (v0.6.15)
- [x] `gobi auth status` — 인증 확인 (Changsoo Park)
- [x] `gobi init` — vault "gobi-cli-study" 생성
- [x] 전체 명령어 탐색 (`--help`) 완료
- [x] `core-concepts.md` 작성 완료
- [x] `installation-guide.md` 작성 완료
- [x] 추가 발견 명령어 문서화 (`sense`, `sync`)

---

## 이전 / 다음 모듈

| | 모듈 | 링크 |
|--|------|------|
| ◀ 이전 | - | (M1이 첫 번째 모듈) |
| 다음 ▶ | M2 — Brain & Session 명령어 마스터 | `../02-Brain-Session/README.md` |

---

> **방법론**: VibeLearn AI v2.0
> **작성자**: Changsoo (Claude Code 활용)
