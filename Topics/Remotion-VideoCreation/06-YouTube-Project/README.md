# M6 - Capstone: 유튜브 설명 영상 제작

M1~M5에서 배운 기술을 통합하여 "VibeLearn AI 소개" 유튜브 영상을 완성한 Capstone 프로젝트입니다.

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/video-production-flow.md](concepts/video-production-flow.md) | 영상 기획→제작→렌더링 전체 플로우 |
| 2 | [guides/storyboard.md](guides/storyboard.md) | 장면별 스토리보드 (5개 장면 구성) |
| 최종 | `my-first-video/out/VibeLearnIntro_final.mp4` | 완성된 46초 소개 영상 |

**이전 모듈**: [05-Rendering](../05-Rendering/) | **다음 모듈**: 없음 (Capstone 완료)

---

## 영상 정보

| 항목 | 내용 |
|------|------|
| 제목 | VibeLearn AI 소개 - AI와 함께 배우는 방법 |
| 길이 | 46초 (1380프레임) |
| 해상도 | 1920 x 1080 (Full HD) |
| FPS | 30fps |
| 코덱 | H.264 |
| 파일 크기 | 16 MB |
| 최종 파일 | `my-first-video/out/VibeLearnIntro_final.mp4` |

## 장면 구성

| # | 장면 | 길이 | 컴포넌트 | 출처 |
|---|------|------|----------|------|
| 1 | 채널 인트로 | 6초 | ChannelIntro | M4 재활용 |
| 2 | "VibeLearn AI란?" 타이틀 | 5초 | TitleCard | M3 재활용 |
| 3 | 핵심 원칙 3가지 | 15초 | ExplanationScene | M4 재활용 (데이터 변경) |
| 4 | 학습 워크플로우 | 14초 | WorkflowScene | **M6 신규** |
| 5 | 아웃트로 + CTA | 6초 | OutroScene | **M6 신규** |

## 기술 활용

### Core (수동 코딩)
- Series로 전체 장면 순차 배치 (VibeLearnIntro.tsx)
- WorkflowScene: Sequence + spring + interpolate 조합
- OutroScene: spring + pulse 애니메이션

### Skills (AI 생성 기반)
- ChannelIntro: M4에서 반복 개선으로 완성
- ExplanationScene: M4에서 Series 패턴으로 생성

### 재활용 전략
- 기존 컴포넌트 3개 재활용 (Props만 변경)
- 새 컴포넌트 2개 제작
- **Core + Skills 하이브리드** 접근으로 효율 극대화

## 폴더 구조

```
06-YouTube-Project/
├── README.md                      # 이 파일
├── concepts/
│   └── video-production-flow.md   # 영상 기획→제작→렌더링 플로우
├── guides/
│   └── storyboard.md              # 장면별 스토리보드
└── examples/
    └── (코드는 my-first-video/src/에 위치)
```

## 관련 파일

- `my-first-video/src/VibeLearnIntro.tsx` — 전체 통합 컴포넌트
- `my-first-video/src/WorkflowScene.tsx` — 워크플로우 장면 (신규)
- `my-first-video/src/OutroScene.tsx` — 아웃트로 장면 (신규)
- `my-first-video/out/VibeLearnIntro_final.mp4` — 최종 렌더링 파일
