# 2026-08-16 FDE-Forward-Deployed-Engineer Final Retrospective

## Topic 완료 요약

`FDE-Forward-Deployed-Engineer` Topic은 미국 AI/테크 취업시장을 중심으로 Forward Deployed Engineer의 정의, 역사, 기업별 변형, 유사 직무와의 차이, 기술 스택, 채용 공고 분석, 배경별 커리어 전략, 포트폴리오와 영상화 기획까지 정리했다. M1-M10을 통해 FDE를 단순 직무명으로 보지 않고, customer-facing engineering, production adoption, field-to-product feedback이 결합된 역할로 다루었다.

## 모듈별 핵심 산출물

| 모듈 | 핵심 산출물 | 재사용 가치 |
|---|---|---|
| M1 | FDE 정의, 역사 타임라인, 2분 설명문 | FDE 입문 설명 |
| M2 | Palantir 원형 분석, 원형 vs AI FDE 비교 | 역사적 배경과 원형 이해 |
| M3 | 기업별 FDE archetype, candidate fit selector | 회사별 지원 전략 |
| M4 | 유사 직무 taxonomy, resume bullet 변환 | 직무명 오판 방지 |
| M5 | AI FDE delivery lifecycle, technical stack map | 실무 기술 범위 이해 |
| M6 | 미국 채용 공고 분석, 면접 루프, 보상/지역 메모 | 채용시장 분석 |
| M7 | 주니어 역량 체크리스트, 6개월 계획, 포트폴리오 brief | 학생/주니어 준비 |
| M8 | 시니어 전환 맵, 90일 계획, resume narrative | IT 시니어 전환 |
| M9 | 비IT 진입 경로, 12개월 계획, 글로벌 AX 비교 | 비IT/글로벌 문맥 |
| M10 | 포트폴리오 가이드, 프로젝트 spec, 영상 outline/script/storyboard | 최종 패키지와 영상 핸드오프 |

## 주요 인사이트

FDE는 engineering과 consulting의 중간이라는 설명만으로는 부족하다. 핵심은 고객 현장에서 모호한 문제를 받아 product와 technical system으로 구체화하고, 실제 사용과 adoption까지 책임지는 점이다. AI 시대의 FDE는 특히 model capability를 고객의 업무, 데이터, 권한, 보안, 운영 방식 안에 넣는 역할이므로 eval, observability, security boundary, rollout plan이 중요하다.

지원자 전략은 배경별로 달라야 한다. 주니어는 portfolio proof를 만들어야 하고, IT 시니어는 기존 delivery와 stakeholder 경험을 FDE 언어로 번역해야 하며, 비IT 배경자는 domain expertise를 살리되 technical minimum과 인접 역할 전략을 갖춰야 한다. 글로벌 문맥에서는 미국 FDE와 한국 AX, 일본 DX to AX, 유럽 regulated AI를 같은 개념으로 섞지 않고 role, organization, project language로 구분해야 한다.

## 산출물 품질 평가

| 기준 | 평가 |
|---|---|
| 학습 순서 | M1 정의에서 M10 포트폴리오/영상화까지 단계적으로 연결됨 |
| 실무성 | 공고 분석, 면접 준비, 포트폴리오 spec, career path가 포함됨 |
| 재사용성 | README와 하위 문서가 학습 순서대로 연결되어 다음 학습자가 따라갈 수 있음 |
| 영상화 가능성 | 6편 outline, episode script, visual storyboard로 Remotion 작업 전 단계 준비 완료 |
| 보완 필요 | 실제 최신 공고는 향후 지원 시점에 다시 확인해야 함 |

## 다음 단계

1. ~~Claude Code에게 `10-Capstone-Video/video/`의 3개 문서를 넘겨 Remotion 구현을 시작한다.~~ ✅ **완료 (2026-08-19)** — 6편 분할 시리즈가 아니라 **단일 장편 1편**으로 구현했고, 한국어·영어 두 언어판을 각각 렌더해 유튜브에 공개했다. 🇰🇷 28분 1초 https://youtu.be/U0L2oyE6Ph4 · 🇺🇸 27분 11초 https://youtu.be/A6Yx6Wx22cA. 파트 전환마다 해당 모듈로 가는 QR을 넣어 영상에서 문서로 되돌아오는 경로를 만들었고, 두 README에 영상 링크를 반영했다.
2. ~~영상 제작 전에 에피소드별 길이, 자막 언어, TTS 사용 여부, visual theme을 확정한다.~~ ✅ **완료 (2026-08-19)** — 언어별 나레이션 분리(한·영 각 1편), TTS 사용, 슬라이드 기반 visual theme으로 확정해 제작했다.
3. 포트폴리오 프로젝트 3개 중 하나를 실제 구현 대상으로 선택한다.
4. 지원자 유형별로 M7, M8, M9 문서를 별도 guide package로 재배치할 수 있다.

> **Capstone 영상화 마감 (2026-08-23 확인).** M10에서 영상 제작 전 기획/핸드오프까지로 범위를 끊었던 작업이 실제 제작·업로드까지 닫혔다. 남은 후속은 이 Topic 밖의 일 — SNS 홍보 잔여 플랫폼 게시(Facebook 계열·LinkedIn·Threads·X·bada.us·블로그)뿐이며, [[Research/2026-08-19 FDE 영상 SNS 홍보 글 by Claude Code|SNS 홍보 글 문서]]에서 추적한다. 업로드 메타데이터(제목·Description·챕터·태그)는 `AI/RemotionStudio/_archive/public/fde-career-0816/youtube-upload.md`에 있다.

## Topic 성공 기준 점검

- [x] 모든 모듈 완료
- [x] 최소 10개 산출물 폴더 생성
- [x] 기업별 FDE 모델 비교 리포트 완성
- [x] 미국 FDE 채용시장 분석표 완성
- [x] FDE 역량 매트릭스 완성
- [x] 학생/주니어, IT 시니어, 비IT 배경자 준비 가이드 완성
- [x] FDE 포트폴리오 프로젝트 가이드 완성
- [x] Remotion AI 영상 제작용 시리즈 outline, 대본, 스토리보드 완성
- [x] Topic Retrospective 작성

