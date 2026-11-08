---
title: "WorkLog - M4 볼트 연결 해법 · Claude Code Remote Control"
author:
  - Codex
created: 2026-11-08 04:16:06
tags:
  - muse-my-workflow
  - worklog
---

## 세션 정보

**날짜**: 2026-11-08  
**Topic**: Muse-My-Workflow  
**모듈**: M4 - 볼트 연결 해법 · 실습 3  
**진행 에이전트**: Codex  
**이전 WorkLog**: [11/5 M4 WorkLog](20261105_M4_Muse-My-Workflow.md#다음-세션에-넘길-것) — 가상 자료와 시나리오 비교표를 준비했다.

## 🎯 오늘의 학습 목표

E · Claude Code Remote Control로 집에서 시작한 가상 작업을 휴대폰에서 이어가고 새 결과 Markdown을 집 PC에서 확인한다. 승인 범위는 가상 파일 3개다. 실제 볼트 사본 범위 결정과 C · Google Drive 시험은 다음 세션으로 미루고, 시험 파일 삭제나 연결 해제는 별도 확인을 받는다.

## 📚 진행 내용

[가상 시험 폴더](../04-Vault-Connection/examples/trial-vault/)의 `continuation-note.md`, `event-catalog.md`, `planning-brief.md`만 볼트 밖 로컬 임시 시험 폴더에 복사했다. 세 사본 모두 원본과 SHA-256이 일치했다.

Claude Code v2.1.272를 해당 폴더에서 시작했다. `--restricted`로 파일 도구의 작업 범위를 제한하고 `--tools Read,Write`, `--strict-mcp-config`, `--no-chrome`을 적용했다. 새 결과 파일 이름은 `m4-e-remote-result.md`로 지정했다. E는 Claude Code가 집 PC의 로컬 세션을 휴대폰에서 조작하는 대안 경로다. [Claude Code 공식 안내](https://code.claude.com/docs/en/remote-control)

구독 계정 로그인 후 로컬 세션에서 `/rc active`를 확인했다. 집 PC에서 Claude에 가상 파일 3개를 읽고 현재 상태와 다음 작업을 요약하도록 요청했다. Claude는 겹치는 시간인 10:30–11:00을 찾고 다음 요청에서 새 파일에 결과를 쓰겠다고 답했다. 휴대폰에서 같은 세션을 열어 이어서 파일 작성을 요청하도록 안내했다.

### 결과 검증

휴대폰에서 보낸 요청을 같은 집 PC 세션이 받았고, 단일 파일 생성 확인 뒤 로컬 Claude Code가 29줄을 썼다. **04:25 PST**에 집 PC의 시험 폴더에 생성된 `m4-e-remote-result.md`를 직접 열었다. AI 글쓰기 실습과 자동화 실험실의 겹침 시간 **10:30–11:00**, 공개 데모 시간 **13:00–14:00**과 준비 목록이 가상 행사표·요청서와 일치했다.

시험 폴더에는 입력 3개와 결과 1개가 있었고, 세 입력 사본의 SHA-256이 시험 전 값과 볼트의 가상 원본에 모두 일치했다. 따라서 휴대폰에서 작업을 이어간 S4와 집 PC에서 결과를 확인한 S2는 가상 범위에서 통과했다. [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md#시나리오-비교)

## 🐛 문제 해결 로그

로컬 세션에 `Not logged in · Run /login`이 표시됐다. 사용자가 브라우저에서 로그인한 뒤 `/remote-control`을 실행해 해결했다. 결과의 YAML `author`에는 계정 이메일이 자동으로 들어갔다. 결과 원본은 시험 폴더에 그대로 두고 이 기록에는 이메일 주소를 옮기지 않았다.

## 📊 DoD 체크리스트

- [x] 해법 8가지 확인표 — 모든 행에 출처 종류 · 날짜
- [ ] 시나리오 5개 × 시험한 해법 결과표 (실패 포함)
- [ ] 사본 규칙 박창수 승인 · 미리 보기 보고서에 내부 표시 문서 0개
- [ ] 첫 업로드는 박창수 승인 뒤 실행, 받는 곳 회수 확인
- [ ] 작업 종류별 경로표 · 되돌리는 법
- [x] 공개 문서에 실제 사본 설정 · 계정 정보 없음 · 산출물 폴더 README 작성
- [x] README 링크가 실제 파일을 가리키는지 확인 (`check_links.py`)
- [ ] WorkLog (🎬 · 🎓 칸 포함) · Module Retrospective 작성

**진행 상태** — M4 3/8. E 가상 시험 S2·S4 통과. 전체 시나리오 비교와 사본 정책 결정은 남아 있다.

## 후속 세션 — C · Google Drive 준비 (04:55 PST)

두 항목 승인에 따라 가상 자료 3개와 기존 `visibility: public` 미리 보기 후보 3개를 임시 로컬 폴더에 각각 준비했다. 후보 파일은 미리 보기 보고서에서 INCLUDE로 나온 세 파일이며, 각각의 frontmatter에 `visibility: public`이 있고 `visibility: internal` 표식과 `🔒 내부 자료` 표식이 없음을 확인했다. 원본 볼트 파일은 수정하지 않았다.

개인 Drive에서 `Muse M4 Test - Synthetic` 폴더를 만들었다. 처음에는 브라우저 자동화가 Windows 파일 선택 창을 감지하지 못했다. 사용자가 선택 창이 뒤늦게 열리는 것을 확인해 주었고, 재시도에서는 업로드 버튼을 누르기 전에 브라우저의 파일 선택 이벤트를 기다리도록 설정했다. `continuation-note.md`, `event-catalog.md`, `planning-brief.md`를 올린 뒤 Drive의 `3 uploads complete` 메시지와 파일 세 개를 확인했다.

승인된 `public` 후보 3개는 개인 Drive의 별도 폴더 `Muse M4 Approved Public Preview`에 올렸다. Drive의 `3 uploads complete` 메시지와 폴더에 표시된 세 Markdown 파일을 확인했다.

Muse 탭은 로그인 화면에서 멈췄다. 로그인 후 Google 동의 화면에서 Muse가 요청하는 접근 범위를 확인하고, 가상 파일 검색·결과 작성·집 PC 회수를 시험한다.

## 💡 Daily Retrospective

- **잘한 점** — 모바일의 완료 메시지를 집 PC의 실제 파일과 대조했고, 입력 세 개의 해시도 전후로 비교했다.
- **개선할 점** — 다음 원격 실습에서는 가상 폴더를 준비할 때 집 PC의 Claude Code 인증 상태도 함께 확인한다.
- **인사이트** — 집 PC에서 실행 중인 세션에 모바일로 접속하는 것과, 별도 클라우드 저장소에서 파일을 회수하는 것은 검증 조건이 다르다. 비교표에는 E의 성과를 로컬 세션 인계로 분류한다.

## 🎬 영상 재료

휴대폰의 가상 작업 요청과 집 PC의 새 결과 파일을 나란히 보여 줄 수 있다. 영상용 결과 화면은 계정 이메일이 담긴 작성자 필드를 제외하고 구성한다.

## 🎓 가르칠 때

가상 행사 표의 겹침 시간 10:30–11:00을 기대값으로 제시한다. 실제 결과가 맞는지, 휴대폰 요청으로 집 PC에 파일이 생성됐는지, 입력 해시가 유지됐는지를 각각 확인한다.

## 다음 세션에 넘길 것

1. 실제 볼트 사본 범위를 검토하고 C · Google Drive 시험의 폴더·권한 범위를 사용자와 정한다. E의 S2·S4 결과를 [시나리오 비교표](../04-Vault-Connection/guides/seamless-scenarios.md#시나리오-비교)의 비교 기준으로 사용한다.
2. E 시험 폴더와 원격 세션은 보존했다. 삭제와 연결 해제는 사용자에게 먼저 묻는다.
