# C. AI 미팅 봇 동의 문제 — Otter.ai, Fireflies, Zoom AI

> **핵심 질문**: AI 미팅 봇이 회의에 참가해 녹음할 때, WA 주 all-party consent 요건을 충족하는가?

## 주요 서비스별 동의 고지 방식

| 서비스 | 동의 메커니즘 | WA 주 충족 여부 |
|--------|------------|--------------|
| **Zoom AI Companion** | 호스트 녹화 시 플랫폼이 자동으로 전 참가자에게 알림 | ✅ 충족 |
| **MS Copilot in Teams** | 녹화 시작 전 배너 알림 | ✅ 충족 |
| **Google Meet AI (Gemini)** | 녹화 알림 표시 | ✅ 충족 |
| **Otter.ai (OtterPilot)** | 봇 참가 시 채팅 메시지 전송 — 비활성화 가능 | ⚠️ 불충분 가능성 |
| **Fireflies.ai** | 봇이 회의 참가 — 고지 방식 일관성 없음 | ⚠️ 불충분 |

## 실제 소송 사례 (2025-2026)

### Otter.ai 집단 소송 (2025년 8-9월 제기, 연방법원 계류 중)

**법원**: 캘리포니아 북부 연방지방법원 (N.D. California)
**주요 원고**: Justin Brewer (캘리포니아 거주)

> 브루어는 Otter.ai 계정이 없었다. 그러나 상대방이 OtterPilot을 실행한 상태에서 2025년 2월 영업 전화에 참가했고, 봇이 녹음 중임을 전혀 몰랐다.

**핵심 주장**:
- Otter.ai를 "무단 제3자 도청자"로 규정
- Single-consent 모델이 캘리포니아 같은 all-party consent 주에서 위험
- 소송 모션-투-디스미스 청문: 2026년 5월 20일 예정
- **의의**: AI 봇이 수십 년 된 도청법 적용을 받는지 최초 연방 판단

### Fireflies.ai BIPA 소송 (2025년 12월 18일 제기)

**사건명**: Cruz v. Fireflies.AI Corp., No. 3:25-cv-03399
**법원**: 일리노이 중부 연방지방법원 (C.D. Illinois)
**원고**: Katelin Cruz (일리노이 비영리단체 미팅 참가자)

> 크루즈는 Fireflies 계정이 없었다. 비영리단체가 Fireflies를 활성화한 가상 미팅에 참가했고, 봇이 그녀의 **성문(voiceprint)**을 생성했다.

**핵심 주장**:
- Illinois BIPA(생체정보 보호법) 위반 — 성문이 생체정보에 해당
- 동의 없는 생체정보 수집 및 저장

**두 소송의 차이**:
- Otter: **도청법(Wiretap statute)** 위반 주장
- Fireflies: **BIPA(생체정보법)** 위반 주장 — 더 광범위한 파급 효과 가능

### Otter.ai "통화 후에도 계속 청취" 논란
별도 소송에서 Otter.ai 봇이 **통화 종료 후에도 계속 청취**했다는 주장이 제기됨. 기술적 오류인지 의도된 설계인지 조사 중.

## WA 주에서 AI 미팅 봇 사용 시 Constructive Consent 충족 여부

| 상황 | 판단 | 이유 |
|------|------|------|
| Zoom 호스트 내장 녹화 + 자동 알림 | ✅ 충족 | 플랫폼이 보장 |
| 미팅 시작 전 "AI 봇 사용 중" 구두 안내 | ✅ 충족 | Constructive consent |
| 봇이 채팅으로 참가 알림 전송 | ⚠️ 불확실 | 못 본 경우 동의 미성립 |
| 봇이 참가했지만 아무 알림 없음 | ❌ 위법 | All-party consent 위반 |
| 캘린더 초대에 "AI 봇 사용" 명시 | ✅ 충족 | 사전 고지 |

## 안전한 AI 봇 사용 절차 (WA 주 기준)

```
[단계 1] 미팅 초대 단계
  캘린더 초대에 명시: "이 미팅은 AI 봇(Otter.ai/Fireflies 등)으로
  기록됩니다. (This meeting will be recorded with AI assistance.)"

[단계 2] 미팅 시작 직후
  구두 안내: "오늘 미팅은 [서비스명]으로 녹음됩니다. 괜찮으시면
  계속 진행하겠습니다."

[단계 3] 채팅창 공지 (보강 조치)
  "This meeting is being recorded using AI notetaking."

→ 이 3단계를 모두 수행하면 WA 주 constructive consent 충족
```

## BIPA 확산과 WA 주 시사점

Illinois BIPA는 **성문(voiceprint)**을 생체정보로 분류해 별도 보호.
WA 주에는 별도 생체정보법(MY Health MY Data Act, 2023)이 있으나 현재는 건강데이터 중심.
그러나 AI 미팅 봇이 대화에서 성문을 추출하는 경우, 향후 WA 주 법적 해석이 확대될 가능성 있음.

## 핵심 인사이트

> AI 봇 소송이 묻는 핵심 질문: **"봇은 대화에 참여한 '당사자'인가, 아니면 '도청 장치'인가?"**
> — 연방법원의 판단에 따라 수십 개 서비스의 비즈니스 모델이 달라진다.

---
*연구일: 2026-06-07 | VibeLearn AI M6-C*
*주요 출처: tldv.io (2026 AI Meeting Recorder Lawsuits), Epstein Becker Green (Fireflies BIPA), recordinglaw.com*
