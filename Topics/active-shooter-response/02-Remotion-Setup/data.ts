// Active Shooter Response Training — active-shooter-0906
// 슬라이드 플랜: AI/RemotionStudio/src/active-shooter-0906/video-slide-plan.md
//
// 본 영상은 미 국토안보부(DHS) 행동 지침을 인포그래픽으로 전하는 공익안전 학습 영상입니다.

export const FPS = 30;
export const SEC = (s: number) => Math.ceil(s * FPS);

// ─── 오디오 패딩 ──────────────────────────────────────────────────────────
export const AUDIO_HEAD_PAD_SEC = 0.12;
export const AUDIO_TAIL_PAD_SEC = 1.2;

// ─── 에셋 준비 상황 ────────────────────────────────────────────────────────
export const PHOTOS_READY = false; // M2 단계: 이미지 생성 대기 중

// ─── 밝기 대역 및 테마 ──────────────────────────────────────────────────────
// 직전 2편(vibe-coding-0901, datacenter-workforce-0902)이 모두 L1 밝은 대역이었으므로,
// 이번 재난 대응 콘텐츠는 세련되면서도 진지한 L3 중간어둠 대역을 사용하여 다양성을 보장합니다.
export const BAND = 'L3' as const;

// ─── 테마 컬러 팔레트 (Slate Charcoal 테마) ───────────────────────────────
export const COLORS = {
  paper: '#161B22',        // Slate Charcoal - 전체 배경색
  paper2: '#21262D',       // Card Background - 글래스모피즘 카드 배경용 반투명 슬레이트
  grid: 'rgba(240, 246, 252, 0.035)',   // Dot Grid - 3.5% 불투명 도트 격자선
  gridSoft: 'rgba(240, 246, 252, 0.015)',
  ink: '#F0F6FC',          // Cool Off-White - 본문 및 제목 글자색
  inkSoft: '#8B949E',      // Slate Gray - 부제목 및 보조 설명 글자색
  inkFaint: '#4F565E',     // 비활성 텍스트
  signal: '#E24A4A',       // Crimson Red - 주요 경고, FIGHT 및 강세 컬러
  accent: '#FF9F43',       // Caution Orange - 주의 수칙, HIDE 및 서브 강조
  safe: '#2EC4B6',         // Teal Green - RUN 및 안전/경찰 대응 테마 컬러
  white: '#FFFFFF',
} as const;

// ─── 타입 정의 ─────────────────────────────────────────────────────────────
export type SlideType = 'title' | 'section' | 'bullet' | 'compare' | 'quote' | 'stat' | 'outro';

export interface Line {
  label?: string;
  text: string;
  note?: string;
  accent?: 'ink' | 'signal' | 'accent' | 'safe' | 'faint';
}

export interface SlideData {
  id: string;
  type: SlideType;
  eyebrow?: string;       // 상단 꼬리표 배지 이름
  title?: string;
  subtitle?: string;
  lines?: Line[];
  photo?: string;         // public/active-shooter-0906/images/ 아래 생성될 사진 파일명
  holdSec?: number;       // 나레이션 종료 후 머무는 추가 시간
  spec?: Record<string, unknown>; // 세부 컴포넌트용 특수 명세
}

// ─── 슬라이드 10장 구성 데이터 ─────────────────────────────────────────────
export const SLIDES: SlideData[] = [
  {
    id: 'S01',
    type: 'title',
    title: '총기난사 사건 대응 요령',
    subtitle: 'Active Shooter Response Training',
    spec: { subtitleKo: '미 국토안보부(DHS) 공식 가이드라인' },
  },
  {
    id: 'S02',
    type: 'section',
    title: 'PART 1. 생존을 위한 3대 원칙',
    subtitle: 'Run ➔ Hide ➔ Fight',
    spec: { icon: '🚨' },
  },
  {
    id: 'S03',
    type: 'bullet',
    eyebrow: '1단계. 뛴다',
    title: '뛴다 (Run / Evacuate)',
    photo: 'slide_03_run.png',
    spec: { badgeColor: 'safe', badgeText: '최우선순위' },
    lines: [
      { label: '🏃 탈출 계획', text: '주변 비상구와 탈출로를 즉각 머릿속으로 판단합니다.' },
      { label: '🎒 소지품 방기', text: '소지품을 챙기느라 단 1초도 멈추지 말고 빈손으로 대피합니다.', accent: 'signal' },
      { label: '🤝 독자적 대피', text: '타인이 동의하지 않더라도 절대 지체하지 않고 탈출합니다.' },
      { label: '👐 두 손 노출', text: '탈출하는 동안 두 손이 무장하지 않았음을 경찰에게 늘 보이게 합니다.', accent: 'safe' },
    ],
  },
  {
    id: 'S04',
    type: 'compare',
    eyebrow: '2단계. 숨는다',
    title: '숨는다 (Hide / Barricade)',
    spec: {
      badgeColor: 'accent',
      badgeText: '대피 불가 시',
      headers: ['자재 / 은신 구역', '방탄 보호력 (Cover)', '단순 은폐 (Concealment)'],
      rows: [
        ['콘크리트 벽 / 구조 기둥', '✓ 직접 사격 보호 가능', '✓ 시야 차단 가능'],
        ['철제 사물함 / 무거운 책상', '✓ 일부 사격 차단 가능', '✓ 시야 차단 가능'],
        ['유리문 / 텐트천 / 합판', '✗ 방탄 불가 (관통 위험)', '✓ 시야 차단 가능'],
      ],
    },
    lines: [
      { text: '문을 안에서 신속히 잠그고 무거운 가구로 철저히 바리케이드를 칩니다.', accent: 'accent' },
      { text: '스마트폰은 진동이 아닌 "완전 무음" 상태로 소리를 완전히 죽이고 대기합니다.' },
    ],
  },
  {
    id: 'S05',
    type: 'quote',
    eyebrow: '3단계. 싸운다',
    title: '싸운다 (Fight / Defend)',
    photo: 'slide_05_fight.png',
    spec: {
      badgeColor: 'signal',
      badgeText: '최후의 저항',
      quote: '자신의 생명이 즉각적으로 위협받는 극단의 순간, 마지막 수단으로 공격자를 저지하고 제압하십시오.',
      author: '— 미 국토안보부(DHS) 행동 강령',
    },
    lines: [
      { text: '소화기, 의자, 텀블러 등 주변의 모든 무거운 집기를 집어던져 방해하십시오.', accent: 'signal' },
      { text: '주변 사람들과 목소리를 모아 고함을 지르며 과감하고 적극적으로 제압합니다.' },
    ],
  },
  {
    id: 'S06',
    type: 'section',
    title: 'PART 2. 경찰 진입 시 조우 수칙',
    subtitle: 'Law Enforcement Response',
    spec: { icon: '🚓' },
  },
  {
    id: 'S07',
    type: 'bullet',
    eyebrow: '경찰 도착 시',
    title: '무장 경찰 대면 시 행동 원칙',
    photo: 'slide_07_police.png',
    spec: { badgeColor: 'safe', badgeText: '경찰 조우 시' },
    lines: [
      { label: '👐 양손 노출', text: '경찰이 볼 수 있게 양손을 높이 들고 손가락을 완전히 폅니다.', accent: 'safe' },
      { label: '🎒 물품 방기', text: '손에 쥔 가방, 재킷 등 모든 물건은 즉시 바닥에 내려놓습니다.' },
      { label: '🚫 접촉 금지', text: '경찰을 강제로 붙잡거나 갑자기 다가서지 않으며 비명을 삼갑니다.', accent: 'signal' },
      { label: '🚪 대피 방향', text: '질문하기 위해 멈추지 말고, 경찰들이 진입해 들어온 방향으로 신속히 나갑니다.' },
    ],
  },
  {
    id: 'S08',
    type: 'stat',
    eyebrow: '신고 프로토콜',
    title: '911 신고 시 제공할 5대 핵심 정보',
    spec: {
      badgeColor: 'accent',
      badgeText: '911 필수 정보',
      gaugeMax: 5,
    },
    lines: [
      { label: '1. 위치', text: '총기난사자의 현재 정확한 건물 내 위치' },
      { label: '2. 인원', text: '공격자(총격범)의 총 인원 수' },
      { label: '3. 인상착의', text: '공격자의 외모, 입고 있는 옷 색상 및 특징' },
      { label: '4. 무기', text: '소지하고 있는 총기 무기의 종류와 개수', accent: 'signal' },
      { label: '5. 피해', text: '현장 내부 피해자의 수와 대략적인 위치', accent: 'accent' },
    ],
  },
  {
    id: 'S09',
    type: 'bullet',
    eyebrow: 'EAP 요건',
    title: '대응 계획(EAP) 설계 요건',
    spec: { badgeColor: 'safe', badgeText: '안전 관리자 수칙', showQr: true },
    lines: [
      { label: '🗺️ 대피로', text: '시설 내에 최소 2개 방향 이상의 실질적이고 즉각적인 대피 경로를 확보합니다.' },
      { label: '🗣️ 방송 매뉴얼', text: '긴급 대피 방송을 위한 한/영 다국어 비상 안내 스크립트를 비치합니다.' },
      { label: '📂 안전 라이브러리', text: 'DHS 대응 강령 원본 및 실제 대피 계획 문서는 아래 QR 레포에서 상시 공유합니다.', accent: 'safe' },
    ],
  },
  {
    id: 'S10',
    type: 'outro',
    title: '안전한 커뮤니티를 위한 동참',
    subtitle: 'GitHub 안전 교육 라이브러리 개방',
    spec: { showLargeQr: true, cta: '구독과 좋아요로 이 지침을 널리 퍼뜨려주세요.' },
  },
];

// ─── QR 코드 목적지 URL ───────────────────────────────────────────────────
export const QR_URL =
  'https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/active-shooter-response';

// ─── 오디오 실측 길이에 맞출 가이드 기간 (Qwen3-TTS 연계 전 가예정치) ─────────
export const AUDIO_DURATIONS: Record<string, number> = {
  S01: 7.5,
  S02: 4.0,
  S03: 18.0,
  S04: 22.0,
  S05: 14.0,
  S06: 4.0,
  S07: 20.0,
  S08: 18.0,
  S09: 19.0,
  S10: 22.0,
};

export const getSlideDurationSec = (id: string): number => {
  const slide = SLIDES.find((s) => s.id === id);
  const base = (AUDIO_DURATIONS[id] ?? 5.0) + (slide?.holdSec ?? 0);
  
  if (slide?.type === 'section') return base;
  return base + AUDIO_HEAD_PAD_SEC + AUDIO_TAIL_PAD_SEC;
};

export const audioSrc = (id: string) =>
  `active-shooter-0906/audio/${id.toLowerCase()}.mp3`;

// ─── 트랜지션 및 러닝타임 계산 ─────────────────────────────────────────────
export const FADE_FRAMES = 16;
export const SECTION_FRAMES = 26;

export const TOTAL_FRAMES = (() => {
  let total = 0;
  for (const s of SLIDES) total += SEC(getSlideDurationSec(s.id));
  const sectionCount = SLIDES.filter((s) => s.type === 'section').length;
  const otherTrans = SLIDES.length - 1 - sectionCount;
  total -= sectionCount * SECTION_FRAMES + otherTrans * FADE_FRAMES;
  return total;
})();
