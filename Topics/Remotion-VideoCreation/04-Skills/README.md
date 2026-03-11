# M4 - Remotion Skills (AI 영상 생성)

Remotion Agent Skills를 활용하여 자연어 프롬프트로 영상을 생성하고, 반복 개선 워크플로우를 학습한 모듈입니다.

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/skills-overview.md](concepts/skills-overview.md) | Remotion Agent Skills 개념 및 아키텍처 |
| 2 | [concepts/prompt-tips.md](concepts/prompt-tips.md) | 효과적인 프롬프트 작성법 (AI 영상 생성 최적화) |
| 3 | [guides/skills-workflow.md](guides/skills-workflow.md) | Skills 워크플로우 가이드 (기본 생성 → 반복 개선) |

**이전 모듈**: [03-Motion-Graphics](../03-Motion-Graphics/) | **다음 모듈**: [05-Rendering](../05-Rendering/)

---

## 학습 요약

| 항목 | 내용 |
|------|------|
| 학습일 | 2026-02-09 |
| 소요 시간 | 약 3시간 |
| 생성 영상 | 3개 (SkillsHelloWorld, ChannelIntro, ExplanationScene) |
| 핵심 기술 | Agent Skills, 반복 개선(Iteration), Series 패턴 |

## 생성한 컴포넌트

### 1. SkillsHelloWorld (첫 AI 영상)
- **파일**: `my-first-video/src/SkillsHelloWorld.tsx`
- **설명**: Skills best practice를 적용한 기본 텍스트 애니메이션
- **기법**: 페이드인 + 스케일업 + 페이드아웃, Zod 스키마 Props
- **핵심**: 시간을 초 단위(`2 * fps`)로 계산, `extrapolateRight: "clamp"` 필수

### 2. ChannelIntro (반복 개선 3회)
- **파일**: `my-first-video/src/ChannelIntro.tsx`
- **설명**: 유튜브 채널 인트로 영상. 3번의 반복 개선으로 완성
- **최종 구조**: 7개 레이어 (그라데이션 배경, 별, 빛줄기, 장식 원, 파티클, 콘텐츠, 웨이브)
- **기법**: 글자별 스태거 등장, 펄스 글로우, 네온 구독 버튼, SVG 웨이브, 스케일아웃 퇴장

### 3. ExplanationScene (설명 영상)
- **파일**: `my-first-video/src/ExplanationScene.tsx`
- **설명**: Series 패턴으로 장면을 순차 배치하는 설명 영상
- **구조**: HeadingScene(2초) + PointScene x3(각 3초) = 11초
- **기법**: Series 자동 순차 배치, 로컬 프레임, 프로그래스 인디케이터

## 폴더 구조

```
04-Skills/
├── README.md                    # 이 파일
├── concepts/
│   ├── skills-overview.md       # Skills 개념 및 아키텍처
│   └── prompt-tips.md           # 효과적인 프롬프트 작성법
├── examples/
│   └── (컴포넌트 파일은 my-first-video/src/에 위치)
└── guides/
    └── skills-workflow.md       # Skills 워크플로우 가이드
```

## 핵심 인사이트

1. **Skills = AI 교사**: SKILL.md로 AI에게 Remotion 모범 사례를 가르치는 구조
2. **반복 개선이 핵심**: 기본 생성 → 구체적 피드백 → 재생성 사이클이 가장 효과적
3. **Series vs Sequence**: 전체 화면 교체는 Series, 같은 화면 내 순차 등장은 frame-delay
4. **Props 재사용성**: 데이터만 교체하면 다른 주제의 영상을 즉시 생성 가능

## 참조

- [Agent Skills 공식 문서](https://www.remotion.dev/docs/ai/skills)
- Skills 규칙 파일: `my-first-video/.agents/skills/remotion-best-practices/rules/`
