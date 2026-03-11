# M1 - 환경 설정 & 첫 영상

## 📖 학습 순서

이 폴더를 처음 여는 분은 아래 순서대로 읽으세요.

| 순서 | 문서 | 설명 |
|------|------|------|
| 1 | [concepts/remotion-overview.md](concepts/remotion-overview.md) | Remotion 개념 개요 (React로 영상 만들기) |
| 2 | [guides/setup-guide.md](guides/setup-guide.md) | 환경 설정 가이드 (Node.js, 프로젝트 생성, Studio 실행) |

**이전 모듈**: 없음 (첫 번째 모듈) | **다음 모듈**: [02-Core-Basics](../02-Core-Basics/)

---

## 개요
Remotion 개발 환경을 구축하고, Hello World 템플릿을 수정하여 첫 영상을 만드는 모듈입니다.

## 환경
- Node.js: v22.15.0
- Remotion: template-helloworld (최신)
- OS: Windows

## 학습 내용

### 핵심 개념
- Remotion = React로 영상을 만드는 프레임워크
- Composition = React 컴포넌트 + 영상 메타데이터 (width, height, fps, durationInFrames)
- Root.tsx = Composition을 등록하는 진입점
- Remotion Studio = 브라우저 기반 실시간 프리뷰 환경 (localhost:3000)

### 프로젝트 구조
```
my-first-video/
├── src/
│   ├── Root.tsx              ← Composition 등록
│   ├── HelloWorld.tsx        ← 메인 영상 컴포넌트
│   └── HelloWorld/
│       ├── Logo.tsx          ← 로고
│       ├── Title.tsx         ← 제목
│       ├── Subtitle.tsx      ← 부제
│       ├── Arc.tsx           ← 호 도형
│       ├── Atom.tsx          ← 원자 도형
│       └── constants.ts
├── remotion.config.ts
├── package.json
└── tsconfig.json
```

### 수정 실습 결과
| 항목 | 변경 전 | 변경 후 |
|------|---------|---------|
| 제목 | "Welcome to Remotion" | "CatchUp AI" |
| 제목 색상 | 검정 (#000000) | 흰색 (#FFFFFF) |
| 배경 | 흰색 (white) | 진한 네이비 (#1a1a2e) |
| 로고 색 | 민트+하늘 | 코랄레드+청록 |
| 영상 길이 | 5초 (150프레임) | 7초 (210프레임) |

## 실행 방법
```bash
cd my-first-video
npm install
npm run dev
# 브라우저에서 http://localhost:3000 열기
```

## 다음 모듈
M2 - Remotion Core 기초 (interpolate, spring, Sequence 심화)
