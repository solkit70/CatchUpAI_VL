---
title: "WorkLog — M5 자막과 인트로 실습"
author:
  - "Codex"
created: "2026-10-29 20:52:35"
tags:
  - ai-event-video-editing
  - effects
---

## 오늘의 학습 목표

승인된 계획에 따라 M5 미완료 항목을 이어서 확인했다. 기존 데모는 수정하지 않았고, 짧은 발언 구간으로 로컬 전사 시험을 진행했다.

- [x] CapCut 템플릿과 생성형 인트로의 공식 자료·실제 접근 여부 확인
- [x] 영어 발언 자막 로컬 시험 및 결과 평가
- [x] 새 음악·외부 이미지 사용 여부와 권리 확인 범위 기록
- [x] M5 상태·산출물 문서 갱신
- [ ] Premiere/CapCut 프로젝트 전달 실증

## 진행 내용

### 1. 인트로 경로 조사와 실제 생성

초기에는 CapCut 공식 Intro Creator와 템플릿 사양을 확인했지만 로그인 요구로 실습이 보류됐다. 이후 사용자가 로그인한 CapCut Video Studio에서 Seedance 2.0 Mini로 5초·16:9·720p 인트로를 만들었다. 화면은 생성 1건의 비용을 60 credits로 표시했다. CapCut 템플릿 편집기는 로그인 뒤에도 네트워크 오류와 무한 로딩이 이어져 템플릿 인트로는 아직 만들지 못했다. 따라서 두 결과의 정식 품질·시간·비용 비교 및 M5 인트로 DoD는 미완료다. → [인트로 비교 기록](../05-HandsOn-Effects/intro-template-vs-generative.md)

### 2. 발언 자막 로컬 시험

기존 2분 37초 데모의 영어 발화에서 25초 WAV 샘플을 만들고 로컬 Whisper tiny와 medium으로 전사했다. 처음 요청한 `tiny.en` 모델은 캐시에 없고 네트워크 다운로드도 되지 않아 중단했다. 이미 캐시된 tiny/medium 모델을 사용해 외부 업로드 없이 시험을 끝냈다.

tiny는 다수의 영어 단어와 기술 용어를 다른 표현으로 바꾸어 사용할 수 없었다. medium은 문맥과 분절이 개선됐지만 시작 부분·`PR review` 등 기술 용어·마지막 문장에 오인식이 남았다. 기존 영상의 medium 전사와 구간 대조는 참고일 뿐 정답 검증이 아니다. SRT는 임시 시험 폴더에만 남겼고 최종 데모에 자막을 합성하지 않았다. 결과적으로 자막 초안에는 사람의 발화 대조와 교정이 필요하다는 평가를 기록했다. → [효과·자막 시험 기록](../05-HandsOn-Effects/ai-directed-effects.md)

### 3. 자산 권리와 편집기 전달

이번 세션에는 새 음악이나 외부 이미지를 사용하지 않았다. 기존 데모 카드의 그래픽은 코드로 만든 것이고, 로컬 설치 글꼴 및 원본 촬영본의 모든 사용 권리까지 재확인한 것은 아니다. 법적 권리 판단으로 확대하지 않는다.

초기 Program Files 경로와 명령 목록 조회에서는 Premiere Pro/CapCut 설치 실행 파일을 찾지 못했다. 후속 점검에서는 사용자 AppData의 CapCut 9.2.0.3931과 열린 창을 확인했지만 접근성 트리에 편집 컨트롤이 나타나지 않았다. 브라우저 AI Creator 생성은 이후 성공했으며, XML·프로젝트 전달 실증은 여전히 미완료다.

## M5 DoD — 로드맵 기준

- [ ] 인트로 2가지(템플릿·생성형) 비교 — Seedance 2.0 Mini 결과 생성, CapCut 템플릿 편집기는 네트워크 오류로 로딩 실패
- [x] AI 지시로 효과·자막 넣기 시도와 평가 — 기존 효과 초안과 로컬 자막 ASR 시험 기록
- [x] 3분 이내 데모 렌더 및 사용자 리뷰 — 2026-10-25 기록
- [x] 음악·이미지 사용 범위 기록 — 새 음악·외부 이미지 미사용, 원본·글꼴의 전체 권리 검증은 미실시
- [x] 산출물 폴더·README
- [x] 링크 검사 — 기존 검사 결과 2026-10-25, 변경한 문서는 기존 README 링크 대상에 영향 없음
- [x] WorkLog·Daily Retrospective

**완료율**: 6/7

## Daily Retrospective

### 잘된 점

외부 업로드 없이 로컬 음성 샘플만 사용해 tiny와 medium 모델의 자막 품질 차이를 확인했고, CapCut 로그인 후 Seedance 2.0 Mini 생성까지 진행했다. 생성형 영상 결과가 있어도 템플릿 쪽 렌더가 실패했으므로 두 결과 비교를 완료 처리하지 않았다.

### 개선할 점

기존 medium 전사도 검증된 정답은 아니므로, 게시할 자막에는 영상 청취와 문장 교정이 필요하다. CapCut 템플릿 편집기는 로그인 후 네트워크 오류가 발생해 템플릿 제작과 Premiere/CapCut 프로젝트 전달을 실증하지 못했다.

### 인사이트

이 짧은 영어 발화 시험에서는 medium이 tiny보다 문맥을 잘 잡았지만, 모델 크기만으로 전문 용어의 정확성과 게시 품질을 보장하지 못했다.

### 다음 세션

1. CapCut 템플릿 편집기의 네트워크 문제가 해결되면 같은 5초·16:9 조건으로 템플릿을 렌더해 Seedance 결과와 비교한다.
2. Premiere/CapCut 접근이 가능해지면 기존 데모의 전달 형식·재편집 가능 여부를 확인한다.
3. 필요 시 Whisper 초안 한 구간을 사람 발화와 대조해 수정량을 기록한다.

## 참조 및 산출물

- [인트로 방식과 공식 자료 확인](../05-HandsOn-Effects/intro-template-vs-generative.md)
- [AI 지시 효과·발언 자막 시험](../05-HandsOn-Effects/ai-directed-effects.md)
- [M5 README](../05-HandsOn-Effects/README.md)
- [CapCut Intro Creator](https://www.capcut.com/create/intro-maker)
- [CapCut Introduction Templates](https://www.capcut.com/template/social/introduction)
- [Seedance 2.5 공식 발표](https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5)

## 2026-10-29 추가 세션 — CapCut 인트로 실습

사용자가 CapCut에 직접 로그인한 뒤 AI Creator 작업 공간이 열렸다. 첫 생성 시도에서 선택된 Seedance 2.0 Fast는 업그레이드가 필요하다고 표시되어 Seedance 2.0 Mini로 바꾸었다. 텍스트 프롬프트만 사용해 5초·16:9·720p 결과를 생성했으며 UI에 60 credits가 표시됐다. 별도 결제나 유료 체험은 시작하지 않았다. 생성 직후 미리보기의 일부 프레임에서 어두운 남색 배경·청록색 광선과 입자를 보았고 중앙 여백이 확보된 듯 판단했으나, MP4 다운로드 후 전체 프레임 검토에서 그 판단이 틀렸음이 확인됐다.

같은 템플릿 `INTRODUCTION 16:9`의 상세는 16:9·3개 클립·8초·624.61K uses로 표시됐다. 사용 버튼으로 로그인된 편집기를 열었지만 `Network error. Check your internet connection and try again.` 오류가 나타났다. 편집기 내 새로고침과 페이지 전체 새로고침, 안내 팝업 닫기 후에도 편집 자산이 계속 로딩되어 템플릿 렌더는 실패했다. 사용 횟수는 품질 평가가 아니다.

두 방법의 비교에서는 생성형 결과만 완성됐다. 템플릿 최종물·편집 시간·비용이 없으므로 M5 인트로 비교 DoD는 미완료이고 M5는 6/7이다. 다음에는 편집기 연결이 복구되면 템플릿을 같은 조건으로 제작해 비교한다.

## 2026-10-30 추가 검증 — Seedance 출력 파일

기존 생성 영상의 다운로드 메뉴를 확인해 MP4를 저장하고 2,015,277 bytes, 5.062초, 1280×720·24fps H.264, AAC 44.1kHz 스테레오임을 읽었다. FFmpeg 전체 디코드는 통과했다. 전체 구간의 대표 프레임 검토에서 중앙의 생성 문구 `Penhin`과 좌측 상단 `Ai` 표기가 드러났다. 그러므로 이전 미리보기 일부에서 중앙 여백을 확인했다고 쓴 평가는 수정한다. 오디오 스트림은 비무음이지만 직접 듣지 않아 유형은 미확인으로 둔다. 재생성·추가 크레딧 사용·결제는 하지 않았다. 다운로드 확인은 템플릿 결과 비교를 대체하지 않으므로 M5는 6/7이다. 상세 사양과 한계는 [M5 인트로 결과](../05-HandsOn-Effects/intro-template-vs-generative.md#2026-10-29-다운로드와-전체-프레임-확인)에 기록했다.
