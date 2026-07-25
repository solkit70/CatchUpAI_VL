# WorkLog - M1: 신청 접수 Form + 영상 안내 문구

**날짜**: 2026-07-21
**Topic**: VibeCoding-Onboarding-Program
**모듈**: M1 - 신청 접수 Form + 영상 안내 문구
**학습 시간**: 새벽 세션 (Fable Monthly spend limit 2회 중단 후 재개)

---

## 🎯 오늘의 학습 목표

- [x] 대상 독자 언어로 Form 문항 4개 + 인사말 설계 (실습 1)
- [ ] 실제 Google Form 제작·Sheets 연동·테스트 제출 (실습 2 — 사용자 진행)
- [x] Build with AI 영상용 신청 안내 문구 초안 (실습 3 — 리뷰 대기)

---

## 📚 진행 내용

### 1. Topic 재작성 (M1 착수 전)

대상 독자(도메인 지식은 풍부하지만 컴퓨터가 낯선 분들) 기준으로 topic_starter, roadmap_prompt,
Roadmap(v2.0, 5모듈), daily_learning_prompt를 전면 재작성했다. 로드맵 상단에 "🧭 대상 독자 기준"
섹션(쉬운 언어 / 한 번에 한 걸음 / 격려+현실 / 이중 용도)을 두어 모든 모듈이 공유하는 원칙으로 삼았다.

### 2. 실습 1 — Form 문항 설계

- 제목: "바이브 코딩 첫걸음 — 온보딩 신청서"
- 인사말: "코딩을 몰라도 괜찮습니다"로 시작, 이선생님 사례를 짧게 포함해 동일시 유도
- 문항 4개: 성함 / 이메일(형식 검증) / 사는 곳(나라+주까지만, 워싱턴주 오프라인 안내 언급) /
  만들고 싶은 앱(예시 3개를 대상 독자의 삶에서 — 상담 경험, 가게 단골손님, 손주 이야기)
- Google Forms에서 만드는 순서 9단계(진행자용) 포함
- → `01-Application-Form/form-questions.md`

### 3. 실습 3 — 영상 신청 안내 문구

- 설명란용(전체) / 아웃트로 화면 텍스트용(짧은) / 아웃트로 나레이션 추가 문장(선택) 3종 작성
- 나레이션 추가는 Qwen3-TTS 교체 전이므로 지금 결정하면 재생성 1회로 반영 가능함을 명시
- → `01-Application-Form/video-cta.md`

---

## 🐛 문제 해결 로그

### 문제 1: Fable Monthly spend limit 반복 도달로 작업 중단

**증상**: 로드맵 재작성 + M1 산출물 작성 중 "You've hit your monthly spend limit" 메시지로 세션
중단 (총 3회 — $25, $40, $70 한도에서 각각).
**원인**: Fable 5는 Usage Credit 과금 — 로드맵·문서 대량 작성 작업의 크레딧 소모가 예상보다 빠름.
로드맵 마무리 + M1 문서 2개 작업만으로 약 $17.93 소모.
**해결**: 사용자가 한도를 $25→$40→$70→$100으로 네 차례 상향하며 재개. 다만 마지막에는 한도를
올리는 대신 **모델을 바꾸는 결정**을 내림 — 다음 작업(M1 실습 2, Google Form 실제 제작)부터는
Fable 대신 Sonnet으로 진행하기로 함. 이 경험 전체를 Fable Credit 소모 실험 문서와 Live20 Rundown
주간 영상 후보("한도를 네 번 올리고, 결국 모델을 바꾸다")로 기록.

---

## 📊 DoD 체크리스트

- [x] 4개 문항 + 인사말이 대상 독자 언어로 작성됨 (Section 분기 반영해 5문항으로 확정)
- [x] 실제 Google Form 제작·Sheets 연동 완료
- [x] 테스트 제출 성공 (🇺🇸 미국→Section 2 노출 / 🇰🇷 한국→Section 2 건너뜀 양쪽 분기 확인, 테스트 응답 삭제 완료)
- [x] 배포용 링크 확보·문서화 (`form-link.md`)
- [ ] 영상 신청 안내 문구 사용자 승인
- [x] WorkLog 작성

**완료율**: 5/6 — 영상 안내 문구 최종 승인만 남음

---

## 💡 Daily Retrospective

### What went well
- 대상 독자 기준을 로드맵의 제1원칙으로 명문화하니, Form 인사말·예시 문구가 자연스럽게 그 톤으로 나옴

### What could be improved
- 처음부터 대상 독자 기준을 물어보고 시작했으면 재작성 없이 한 번에 갈 수 있었음

### Insights
- "예시 문구"가 눈높이의 핵심 — "애플리케이션 아이디어를 기술하세요"와 "손주에게 들려줄 이야기를
  모아 주는 앱" 사이의 거리가 이 프로그램이 메우려는 거리와 같다

### Tomorrow's focus
- 영상 신청 안내 문구(`video-cta.md`) 최종 승인 → M1 완료(6/6)
- M2(온보딩 여정 커리큘럼) 착수

---

## 📎 참조 및 산출물

**생성된 파일**:
- `01-Application-Form/form-questions.md`: Form 문항·인사말·제작 순서
- `01-Application-Form/video-cta.md`: 영상 신청 안내 문구 3종
- `01-Application-Form/README.md`: 모듈 안내
- `01-Application-Form/form-link.md`: 배포 링크 + 테스트 완료 기록

**배포 링크**: https://docs.google.com/forms/d/e/1FAIpQLScLIGwXR4SR467JJcRbVWkoKZP9Xd0bhHDSM64noospnK1X8w/viewform

**다음 세션 준비사항**:
- 영상 신청 안내 문구 승인 후 Build with AI 영상 설명란에 반영

---

**작성자**: Changsoo (with Claude, VibeLearn AI)
