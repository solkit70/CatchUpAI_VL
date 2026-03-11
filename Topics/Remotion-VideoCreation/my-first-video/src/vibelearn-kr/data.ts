// VibeLearn AI 소개 영상 (KR) - 슬라이드 데이터
// 오디오 길이: Python mutagen으로 측정 (2026-02-27)

export const FPS = 30;
export const SEC = (s: number) => Math.ceil(s * FPS);

// 디자인 시스템 (Dark Tech)
export const COLORS = {
  bg: '#0a0a1a',
  bgAlt: '#0d0d2b',
  primary: '#00bcd4',   // cyan
  accent: '#ffd700',    // gold
  coral: '#ff6b6b',     // coral (문제 강조)
  green: '#4ade80',     // green (해결책)
  text: '#ffffff',
  textMuted: '#94a3b8',
  card: 'rgba(255,255,255,0.05)',
  cardBorder: 'rgba(0,188,212,0.2)',
};

// 섹션 색상 (섹션마다 다른 accent)
export const SECTION_COLORS = {
  intro: '#00bcd4',      // Section 1: cyan
  problem: '#ff6b6b',   // Section 2: coral
  intro2: '#ffd700',    // Section 3: gold
  howto: '#4ade80',     // Section 4: green
  casestudy: '#a78bfa', // Section 5: purple
  outro: '#00bcd4',     // Section 6: cyan
};

// 오디오 길이 (초) - Python mutagen 측정값
export const AUDIO_DURATIONS: Record<number, number> = {
  0: 34.80, 1: 23.86, 2: 23.86, 3: 21.96, 4: 20.40,
  5: 7.85,  6: 22.85, 7: 27.22, 8: 22.06, 9: 17.02,
  10: 26.40, 11: 15.96, 12: 16.32, 13: 24.12, 14: 15.50,
  15: 24.82, 16: 17.95, 17: 16.80, 18: 21.00, 19: 18.46,
  20: 16.80, 21: 22.97, 22: 24.12, 23: 12.55,
};

// 총 오디오 길이: 495.65초
// 섹션 전환 5개 × 2초 = 10초
// 총 영상 길이: ~505초 = 15150 프레임

export const SECTION_HEADER_FRAMES = SEC(2); // 60 frames

export type SlideType =
  | 'title'
  | 'bullet'
  | 'cycle'
  | 'definition'
  | 'wordbreakdown'
  | 'workflow'
  | 'step'
  | 'stat'
  | 'timeline'
  | 'compare'
  | 'folder'
  | 'summary'
  | 'outro';

export interface BulletItem {
  emoji?: string;
  text: string;
  sub?: string;
}

export interface SlideData {
  id: number;
  type: SlideType;
  section: 1 | 2 | 3 | 4 | 5 | 6;
  title: string;
  emoji?: string;
  items?: BulletItem[];
  content?: string;
  sub?: string;
  audioSrc: string;
}

export interface SectionHeaderData {
  section: 2 | 3 | 4 | 5 | 6;
  number: string;
  title: string;
  color: string;
}

export const SECTION_HEADERS: SectionHeaderData[] = [
  { section: 2, number: '섹션 2', title: '문제 제기', color: SECTION_COLORS.problem },
  { section: 3, number: '섹션 3', title: 'VibeLearn AI 소개', color: SECTION_COLORS.intro2 },
  { section: 4, number: '섹션 4', title: '어떻게 사용하는가', color: SECTION_COLORS.howto },
  { section: 5, number: '섹션 5', title: '케이스 스터디', color: SECTION_COLORS.casestudy },
  { section: 6, number: '섹션 6', title: '아웃트로', color: SECTION_COLORS.outro },
];

const audio = (n: number) => `vibelearn-kr/audio/slide_${n}.mp3`;

export const SLIDES: SlideData[] = [
  // ─── 섹션 1: 인트로 ───────────────────────────────────────
  {
    id: 0,
    type: 'title',
    section: 1,
    title: 'VibeLearn AI',
    sub: 'AI와 함께 체계적으로 배우는 새로운 방법',
    content: 'Catch Up AI | 2026',
    audioSrc: audio(0),
  },
  {
    id: 1,
    type: 'bullet',
    section: 1,
    title: '오늘 영상에서 배울 것',
    emoji: '📋',
    items: [
      { emoji: '🤔', text: '왜 AI로 배워도 지식이 안 쌓이는가?' },
      { emoji: '💡', text: 'VibeLearn AI란 무엇인가?' },
      { emoji: '🔄', text: '4단계 워크플로우: 어떻게 작동하는가?' },
      { emoji: '🛠️', text: '실제 사용법 (단계별 데모)' },
      { emoji: '📊', text: '케이스 스터디: 9.5시간으로 YouTube 영상까지' },
      { emoji: '🚀', text: '지금 바로 시작하는 방법' },
    ],
    audioSrc: audio(1),
  },
  {
    id: 2,
    type: 'bullet',
    section: 1,
    title: '이런 분께 꼭 필요한 영상입니다',
    emoji: '🙋',
    items: [
      { emoji: '😓', text: '유튜브 강의 봐도 일주일이면 잊어버리는 분' },
      { emoji: '🤖', text: 'ChatGPT로 공부하는데 대화가 끊기면 처음부터 다시인 분' },
      { emoji: '📚', text: '혼자 공부해도 정리가 안 돼서 다른 사람에게 설명 못하는 분' },
      { emoji: '✨', text: 'AI와 함께 체계적으로 배우고 싶은 분' },
    ],
    audioSrc: audio(2),
  },
  // ─── 섹션 2: 문제 제기 ────────────────────────────────────
  {
    id: 3,
    type: 'cycle',
    section: 2,
    title: '대부분의 학습이 이런 패턴입니다',
    emoji: '😩',
    items: [
      { emoji: '▶️', text: '강의 시청' },
      { emoji: '💡', text: '이해했다!' },
      { emoji: '🌫️', text: '일주일 후... 망각' },
      { emoji: '🔁', text: '다시 검색' },
    ],
    audioSrc: audio(3),
  },
  {
    id: 4,
    type: 'bullet',
    section: 2,
    title: 'AI로 공부할 때만의 새로운 문제',
    emoji: '🤖',
    items: [
      { emoji: '💨', text: '대화가 끊기면 맥락 소멸', sub: '새 창 열면 처음부터' },
      { emoji: '🎲', text: 'AI마다 다른 가이드', sub: '일관성 없는 답변' },
      { emoji: '🏝️', text: '혼자만의 지식', sub: '다른 사람이 재사용 불가' },
      { emoji: '📉', text: '진도 추적 불가', sub: '어디까지 했는지 모름' },
    ],
    audioSrc: audio(4),
  },
  {
    id: 5,
    type: 'compare',
    section: 2,
    title: '네 가지 문제를 한 번에 해결하려면?',
    emoji: '🎯',
    items: [
      { emoji: '💨', text: '대화 끊김 → WorkLog로 맥락 유지' },
      { emoji: '🎲', text: '제각각 가이드 → 폴더 구조로 일관성' },
      { emoji: '🏝️', text: '혼자만의 지식 → 교과서 품질 문서화' },
      { emoji: '📉', text: '진도 불투명 → Roadmap + DoD 체크리스트' },
    ],
    audioSrc: audio(5),
  },
  // ─── 섹션 3: VibeLearn AI 소개 ───────────────────────────
  {
    id: 6,
    type: 'definition',
    section: 3,
    title: 'VibeLearn AI, 한 줄 소개',
    emoji: '✨',
    content: '"배우고 싶어" 한마디면\nAI가 학습 전과정을 이끌어준다',
    sub: 'github.com/solkit70/VibeLearn-AI',
    audioSrc: audio(6),
  },
  {
    id: 7,
    type: 'wordbreakdown',
    section: 3,
    title: 'VibeLearn AI가 의미하는 것',
    emoji: '💬',
    items: [
      { emoji: '🎵', text: 'Vibe', sub: 'AI 코딩 도구로 자유롭게 흐르듯 학습' },
      { emoji: '📖', text: 'Learn', sub: '체계적 구조로 지식을 쌓는 행위' },
      { emoji: '🤖', text: 'AI', sub: '전과정을 자동 처리하는 파트너' },
    ],
    audioSrc: audio(7),
  },
  {
    id: 8,
    type: 'definition',
    section: 3,
    title: '가장 중요한 설계 원칙 하나',
    emoji: '🎨',
    content: '방법론을 배우지 않아도\n방법론이 작동해야 한다',
    sub: '"배우고 싶어" → 나머지는 AI가 알아서',
    audioSrc: audio(8),
  },
  {
    id: 9,
    type: 'workflow',
    section: 3,
    title: 'VibeLearn AI 4단계 워크플로우',
    emoji: '🔄',
    items: [
      { emoji: '🎯', text: 'Phase 1: Topic 설정', sub: 'AI가 대화로 자동 수집' },
      { emoji: '🗺️', text: 'Phase 2: Roadmap 생성', sub: '모듈별 학습 계획 자동 생성' },
      { emoji: '📅', text: 'Phase 3: 일일 학습', sub: '매일 계획 → 실습 → WorkLog' },
      { emoji: '🏆', text: 'Phase 4: 완료 & 회고', sub: '교과서 품질 산출물 완성' },
    ],
    audioSrc: audio(9),
  },
  // ─── 섹션 4: 어떻게 사용하는가 ───────────────────────────
  {
    id: 10,
    type: 'bullet',
    section: 4,
    title: '어떤 주제에도 적용 가능합니다',
    emoji: '🌐',
    items: [
      { emoji: '💻', text: 'Python · JavaScript · TypeScript' },
      { emoji: '🤖', text: 'AI · ML · 프롬프트 엔지니어링' },
      { emoji: '⚛️', text: 'React · Next.js · Remotion' },
      { emoji: '📊', text: '비즈니스 분석 · BRD · PRD' },
      { emoji: '🎨', text: '디자인 · UI/UX · 영상 제작' },
      { emoji: '🌍', text: '외국어 · 자격증 · 취미' },
      { emoji: '📈', text: '데이터 분석 · SQL · 통계' },
      { emoji: '🎓', text: '분야 무관 — 무엇이든 가능' },
    ],
    audioSrc: audio(10),
  },
  {
    id: 11,
    type: 'bullet',
    section: 4,
    title: '시작하기 전 필수물',
    emoji: '🛠️',
    items: [
      { emoji: '✅', text: '필수: 파일 접근 가능한 AI 도구', sub: 'Claude Code, Cursor, VS Code+Copilot' },
      { emoji: '⭕', text: '선택: GitHub 계정', sub: '없어도 시작 가능' },
      { emoji: '⭕', text: '선택: 학습 주제 미리 정하기', sub: '대화 중 정해도 OK' },
    ],
    audioSrc: audio(11),
  },
  {
    id: 12,
    type: 'step',
    section: 4,
    title: 'VibeLearn AI 저장소 받기',
    emoji: '📥',
    content: 'Step 1',
    items: [
      { emoji: '📦', text: 'git clone https://github.com/solkit70/VibeLearn-AI' },
      { emoji: '💾', text: '또는 GitHub에서 ZIP 다운로드' },
      { emoji: '✅', text: 'CLAUDE.md, templates/ 폴더 확인' },
    ],
    audioSrc: audio(12),
  },
  {
    id: 13,
    type: 'step',
    section: 4,
    title: 'AI 도구에서 폴더 열기',
    emoji: '💻',
    content: 'Step 2',
    items: [
      { emoji: '🤖', text: 'Claude Code: claude . 실행' },
      { emoji: '⚡', text: 'Cursor: cursor . 실행' },
      { emoji: '🔵', text: 'VS Code + Copilot: code . 실행' },
    ],
    audioSrc: audio(13),
  },
  {
    id: 14,
    type: 'step',
    section: 4,
    title: '이게 전부입니다',
    emoji: '🗣️',
    content: 'Step 3',
    sub: '"Python 기초를 배우고 싶어."',
    items: [
      { emoji: '🎯', text: '→ AI가 Topic 정보 수집' },
      { emoji: '🗺️', text: '→ Roadmap 자동 생성' },
      { emoji: '📅', text: '→ 매일 학습 가이드' },
    ],
    audioSrc: audio(14),
  },
  // ─── 섹션 5: 케이스 스터디 ───────────────────────────────
  {
    id: 15,
    type: 'stat',
    section: 5,
    title: '실제 케이스 — Clearly 앱 학습',
    emoji: '📊',
    items: [
      { emoji: '⏱️', text: '9.5h', sub: '총 학습 시간' },
      { emoji: '📄', text: '22개', sub: '생성된 산출물' },
      { emoji: '🎬', text: '2개', sub: 'YouTube 영상 완성' },
    ],
    audioSrc: audio(15),
  },
  {
    id: 16,
    type: 'timeline',
    section: 5,
    title: '학습 타임라인',
    emoji: '🗓️',
    items: [
      { emoji: '📖', text: 'M1: 개념 정립', sub: '2h — 5개 문서 생성' },
      { emoji: '🛠️', text: 'M2: BRD/PRD 실습', sub: '3h — 4개 실습 예제' },
      { emoji: '🎬', text: 'M3: 소개 영상 제작', sub: '4.5h — KR+EN 영상 완성' },
    ],
    audioSrc: audio(16),
  },
  {
    id: 17,
    type: 'compare',
    section: 5,
    title: '만약 VibeLearn AI 없었다면?',
    emoji: '❓',
    items: [
      { emoji: '❌', text: '체계 없이 → VibeLearn AI로 → 폴더 구조 자동 생성' },
      { emoji: '❌', text: '기록 없이 → VibeLearn AI로 → WorkLog 실시간 작성' },
      { emoji: '❌', text: '산출물 없이 → VibeLearn AI로 → 22개 재사용 가능 문서' },
      { emoji: '❌', text: '혼자만 → VibeLearn AI로 → 공유 가능한 교과서' },
    ],
    audioSrc: audio(17),
  },
  {
    id: 18,
    type: 'folder',
    section: 5,
    title: '실제 산출물 미리보기',
    emoji: '📁',
    items: [
      { emoji: '📁', text: 'Clearly-BRD-PRD/' },
      { emoji: '📂', text: '01-Product-Overview/', sub: '제품 개요 5개 문서' },
      { emoji: '📂', text: '02-BRD-PRD-Practice/', sub: 'BRD/PRD 실습 4개' },
      { emoji: '📂', text: '03-Intro-Video/', sub: 'KR+EN 영상 + 스크립트' },
    ],
    audioSrc: audio(18),
  },
  // ─── 섹션 6: 아웃트로 ────────────────────────────────────
  {
    id: 19,
    type: 'bullet',
    section: 6,
    title: '한 번 배우면 어떤 주제에도 적용',
    emoji: '🔁',
    items: [
      { emoji: '1️⃣', text: 'Topic 1 완료 → 교과서 품질 산출물 축적' },
      { emoji: '2️⃣', text: 'Topic 2 → 더 빠르게, 더 깊게' },
      { emoji: '3️⃣', text: 'Topic 3 → Capstone 영상까지 자동화' },
      { emoji: '♾️', text: '반복할수록 지식 베이스가 커진다' },
    ],
    audioSrc: audio(19),
  },
  {
    id: 20,
    type: 'compare',
    section: 6,
    title: '익숙해지면 더 잘 활용하는 방법',
    emoji: '💡',
    items: [
      { emoji: '🌱', text: '기본 (처음 사용자)', sub: '"Python 기초를 배우고 싶어."' },
      { emoji: '🚀', text: '고급 (익숙해진 후)', sub: '"Python 기초, JS 2년 경력, 데이터 분석 목적, 3주 가용, 매일 2시간."' },
    ],
    audioSrc: audio(20),
  },
  {
    id: 21,
    type: 'step',
    section: 6,
    title: '지금 바로 시작하는 방법',
    emoji: '🚀',
    content: '30분 안에 시작',
    items: [
      { emoji: '1️⃣', text: 'GitHub에서 저장소 받기', sub: 'github.com/solkit70/VibeLearn-AI' },
      { emoji: '2️⃣', text: 'AI 도구에서 폴더 열기', sub: 'Claude Code, Cursor, VS Code' },
      { emoji: '3️⃣', text: '이 한 마디만 하면 됩니다', sub: '"___를 배우고 싶어."' },
    ],
    audioSrc: audio(21),
  },
  {
    id: 22,
    type: 'summary',
    section: 6,
    title: '오늘 영상 요약',
    emoji: '📝',
    items: [
      { emoji: '💡', text: 'VibeLearn AI란?', sub: 'AI가 이끄는 체계적 학습 방법론' },
      { emoji: '🎨', text: '핵심 설계', sub: '"배우고 싶어" 한마디 → 자동 처리' },
      { emoji: '🔄', text: '4단계', sub: 'Topic 설정 → Roadmap → 일일 학습 → 완료' },
      { emoji: '📊', text: '케이스', sub: '9.5h → 22개 문서 + YouTube 2개' },
      { emoji: '🔗', text: '시작', sub: 'github.com/solkit70/VibeLearn-AI' },
    ],
    audioSrc: audio(22),
  },
  {
    id: 23,
    type: 'outro',
    section: 6,
    title: '함께 만들어가는 VibeLearn AI',
    emoji: '🤝',
    content: 'Catch Up AI',
    sub: '오늘 배울 주제를 정하고\n"___를 배우고 싶어." 라고 말해보세요!',
    items: [
      { emoji: '⭐', text: 'GitHub Star & Watch' },
      { emoji: '🐛', text: 'Issues로 피드백' },
      { emoji: '👍', text: '구독 & 좋아요' },
    ],
    audioSrc: audio(23),
  },
];

// 전체 프레임 계산
const audioTotalFrames = Object.values(AUDIO_DURATIONS).reduce(
  (sum, d) => sum + SEC(d),
  0
);
const sectionHeaderFrames = SECTION_HEADERS.length * SECTION_HEADER_FRAMES; // 5 * 60
export const TOTAL_FRAMES = audioTotalFrames + sectionHeaderFrames;
