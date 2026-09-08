// Active Shooter Response Training — active-shooter-0908
// 슬라이드 플랜: Ingest/CatchUpAI_VL/Topics/active-shooter-response/02-Remotion-Setup/video-slide-plan.md
//
// 본 영상은 미 국토안보부(DHS) 및 시민단체 전문 훈련/대응 자원을 반영한 공익안전 학습 영상입니다.

export const FPS = 30;
export const SEC = (s: number) => Math.ceil(s * FPS);

// ─── 오디오 패딩 ──────────────────────────────────────────────────────────
export const AUDIO_HEAD_PAD_SEC = 0.1;
export const AUDIO_TAIL_PAD_SEC = 0.12;

// ─── 에셋 준비 상황 ────────────────────────────────────────────────────────
export const PHOTOS_READY = false; // M2 단계: 이미지 생성 대기 중

// ─── 밝기 대역 및 테마 ──────────────────────────────────────────────────────
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
  signal: '#ff4d4f',       // Crimson/Red - 주요 경고, FIGHT 및 강세 컬러
  accent: '#FF9F43',       // Caution Orange - 주의 수칙, HIDE 및 서브 강조
  safe: '#52c41a',         // Green - RUN 및 안전/경찰 대응 테마 컬러
  fema: '#1890ff',         // Blue - FEMA, 교육 및 안전망 키트 강조 컬러
  white: '#FFFFFF',
} as const;

// ─── 타입 정의 ─────────────────────────────────────────────────────────────
export type SlideType = 'title' | 'section' | 'bullet' | 'compare' | 'quote' | 'stat' | 'outro';

export interface Line {
  label?: string;
  text: string;
  note?: string;
  accent?: 'ink' | 'signal' | 'accent' | 'safe' | 'fema' | 'faint';
}

export interface SlideData {
  id: string;
  type: SlideType;
  eyebrow?: string;       // 상단 꼬리표 배지 이름
  title?: string;
  subtitle?: string;
  lines?: Line[];
  photo?: string;         // public/active-shooter-0908/images/ 아래 생성될 사진 파일명
  holdSec?: number;       // 나레이션 종료 후 머무는 추가 시간
  spec?: Record<string, unknown>; // 세부 컴포넌트용 특수 명세
}

// ─── 슬라이드 12장 구성 데이터 ─────────────────────────────────────────────
export const SLIDES: SlideData[] = [
  {
    id: 'S01',
    type: 'title',
    title: '총기난사 대응 및 비상 대처',
    subtitle: 'Active Shooter Response Training',
    spec: { subtitleKo: 'DHS 공식 지침 및 시민단체(NGO) 안전망 가이드' },
  },
  {
    id: 'S02',
    type: 'bullet',
    eyebrow: '실제 위협 사례',
    title: '우리가 직면한 현실과 안전 공지',
    photo: 'slide_02_context.png',
    spec: { badgeColor: 'signal', badgeText: '시애틀센터 총격 사건' },
    lines: [
      { label: '🚨 시애틀 축제', text: '7월 26일 시애틀센터 축제 축제 현장에서 발생한 총격으로 3명이 사망하고 4명이 부상했습니다.' },
      { label: '🛑 대형 락다운', text: '모노레일 운행이 중단되고 인근 대형 병원이 전면 봉쇄되는 등 대혼란이 유발되었습니다.', accent: 'signal' },
      { label: '👮 긴급 안전공고', text: '주시애틀총영사관은 즉각 3대 행동 수칙(Run, Hide, Fight)을 숙지하라고 강력 경고했습니다.', accent: 'safe' },
    ],
  },
  {
    id: 'S03',
    type: 'section',
    title: 'PART 1. 생존을 위한 3대 원칙',
    subtitle: 'Run ➔ Hide ➔ Fight',
    spec: { icon: '🚨' },
  },
  {
    id: 'S04',
    type: 'bullet',
    eyebrow: '폭력 진행 궤도',
    title: '가해자의 4단계 행동 징후 식별',
    photo: 'slide_04_prevention.png',
    spec: { badgeColor: 'accent', badgeText: '사전 식별 가이드' },
    lines: [
      { label: '1. 분노 축적', text: '괴롭힘, 해고, 불화 등 개인적인 불만에서 공격 의도가 싹틉니다.' },
      { label: '2. 연구 및 기획', text: '타겟 시설을 고르고 구체적인 공격 시각과 방법을 연구합니다.' },
      { label: '3. 자원 수집', text: '실제 총기와 탄약, 기폭물 등 범행 물품을 수집·비축합니다.', accent: 'signal' },
      { label: '4. 모의 연습', text: '보안을 점검하기 위해 예행연습(Dry Runs)을 실행합니다. 이 시기 신고가 차단의 핵심입니다.', accent: 'accent' },
    ],
  },
  {
    id: 'S05',
    type: 'bullet',
    eyebrow: '물리적 보안',
    title: '출입 통제와 문의 중요성',
    photo: 'slide_05_protection.png',
    spec: { badgeColor: 'signal', badgeText: '상시 잠금 유지' },
    lines: [
      { label: '🚪 문 고정 금지', text: '편의를 위해 소방문 출입문을 열어두는 행위(Propping doors)는 방어선을 무력화합니다.', accent: 'signal' },
      { label: ' Complacency', text: '"우리 시설은 안전하겠지" 하는 문단속 불감증이 실제 참사로 연결됩니다.' },
      { label: '🔒 상시 잠금', text: '모든 외벽 및 내장 소방문은 상시 안전을 위해 반드시 굳건히 잠겨 있어야 합니다.' },
    ],
  },
  {
    id: 'S06',
    type: 'bullet',
    eyebrow: '1단계. 뛴다',
    title: '뛴다 (Run / Evacuate)',
    photo: 'slide_06_run.png',
    spec: { badgeColor: 'safe', badgeText: '최우선 대안' },
    lines: [
      { label: '🏃 탈출 계획', text: '안전한 탈출 경로가 확보되어 있다면 주저 없이 현장을 빠져나갑니다.' },
      { label: '🎒 소지품 방기', text: '짐을 챙기거나 소지품을 찾기 위해 가던 길을 멈추어서는 절대 안 됩니다.', accent: 'signal' },
      { label: '🤝 독자적 대피', text: '타인이 동행을 거부하더라도 설득하느라 지체하지 말고 나 혼자서라도 즉각 탈출합니다.' },
      { label: '🚫 정지 금지', text: '건물 밖으로 나왔더라도 안전 구역에 도달할 때까지 달리기를 멈추지 마십시오.', accent: 'safe' },
    ],
  },
  {
    id: 'S07',
    type: 'bullet',
    eyebrow: '2단계. 숨는다',
    title: '숨는다 (Hide / Barricade)',
    photo: 'slide_07_hide.png',
    spec: { badgeColor: 'accent', badgeText: '차선책 대피' },
    lines: [
      { label: '🔒 은신처 대피', text: '탈출로가 차단되었다면 신속히 문을 잠그고 불을 꺼 내부 기척을 숨기십시오.' },
      { label: '🧱 바리케이드', text: '문이 잠기지 않는다면 책상, 사물함 등 무거운 집기를 문 앞에 단단히 쌓아 방벽을 칩니다.', accent: 'accent' },
      { label: '🔇 완전 무음', text: '벨소리와 진동 파동조차 어둠 속의 표적이 되므로 스마트폰은 무조건 완전 무음 세팅합니다.', accent: 'signal' },
      { label: '⬇️ 바닥 밀착', text: '문을 향한 맹목적 총격을 피하기 위해 문에서 멀리 떨어진 벽 구석 바닥에 바짝 엎드리십시오.' },
    ],
  },
  {
    id: 'S08',
    type: 'quote',
    eyebrow: '3단계. 싸운다',
    title: '싸운다 (Fight / Defend)',
    photo: 'slide_08_fight.png',
    spec: {
      badgeColor: 'signal',
      badgeText: '최후의 수단',
      quote: '무장한 공격자와 일대일로 조우했고 선택의 여지가 없다면, 내 적극적인 행동만이 생명을 건질 마지막 장벽임을 assume하고 절대적인 파괴력으로 반격하십시오.',
      author: '— 미 국토안보부(DHS) 행동 수칙',
    },
    lines: [
      { text: '망설임은 금물입니다. 가해자가 완전히 제압되고 무력화될 때까지 저항을 멈추지 마십시오.', accent: 'signal' },
      { text: '가위, 소화기, 텀블러, 펜, 하드커버 책 등 주변의 무거운 집기를 적극적으로 무기화하여 급소를 강타하십시오.' },
    ],
  },
  {
    id: 'S09',
    type: 'bullet',
    eyebrow: '경찰 도착 시',
    title: '무장 경찰 진입 조우 요령',
    photo: 'slide_09_police.png',
    spec: { badgeColor: 'safe', badgeText: '오발 사고 원천 방지' },
    lines: [
      { label: '👐 양손 노출', text: '경찰과 마주치면 즉시 양손을 머리 위로 높이 들고 손가락을 완전히 벌리십시오.', accent: 'safe' },
      { label: '🎒 손 비우기', text: '스마트폰, 물통 등 오해를 부를 모든 물건을 즉시 던지듯 손에서 멀리하십시오.', accent: 'signal' },
      { label: '🚫 접촉 금지', text: '경찰관에게 안기거나 옷을 붙잡는 등 돌발 행동은 저격으로 이어질 수 있어 절대 금지됩니다.' },
      { label: '🚪 진입로 탈출', text: '경찰관들이 들어온 방향을 향해 신속하고 조용히 빠져나가십시오.' },
    ],
  },
  {
    id: 'S10',
    type: 'compare',
    eyebrow: '자원봉사자 교육',
    title: '시민단체의 공인 안전 교육 연합 경로',
    spec: {
      badgeColor: 'fema',
      badgeText: '전문 안전 자격 획득',
      headers: ['교육 프로그램명', '수강 경로 / 링크', '주요 내용 및 특징'],
      rows: [
        ['FEMA IS-907.A Course', 'training.fema.gov', '무료 온라인 과정 / 퀴즈 합격 시 미 정부 공식 수료증 발급'],
        ['ALERRT CRASE ADD 훈련', 'alerrt.org', 'Avoid, Deny, Defend 모델 / 지역 경찰서 무료 대면 드릴 연계'],
        ['ALICE Navigate360', 'alicelearning.com', '능동형 대항 및 전술 락다운 가이드 / 민간 단체용 정규 솔루션'],
      ],
    },
    lines: [
      { text: '시민단체 실무진 및 리더십은 자원봉사 교육의 일환으로 FEMA 무료 교육 수강을 강력 권장합니다.', accent: 'fema' },
    ],
  },
  {
    id: 'S11',
    type: 'bullet',
    eyebrow: 'NGO 안전 키트',
    title: '단체 안전망 고도화 3대 유틸리티',
    photo: 'slide_11_ngokit.png',
    spec: { badgeColor: 'fema', badgeText: '시민단체 자구책' },
    lines: [
      { label: '📝 EAP 가이드', text: '자체 비상대응계획(Emergency Action Plan)을 설계하고 리더 회의에서 즉각 명문화하십시오.' },
      { label: '🎲 Tabletop Box', text: 'CISA 제공 도상 모의 훈련 키트를 통해 적은 비용으로 단체의 연락망과 EAP를 수시 점검하십시오.', accent: 'fema' },
      { label: '🩹 Stop the Bleed', text: '대량 출혈사를 막기 위해 단체 내 표준 지혈대(Tourniquet)를 구비하고 지혈 훈련을 실시하십시오.', accent: 'signal' },
    ],
  },
  {
    id: 'S12',
    type: 'outro',
    title: '안전을 향한 따뜻한 연대',
    subtitle: 'NGO 안전 가이드북 QR 배포 오픈',
    spec: { showLargeQr: true, cta: 'QR코드를 스캔하여 NGO 전용 대응 가이드북을 전수 다운로드하고 안전한 연합에 동참하십시오.' },
  },
];

// ─── QR 코드 목적지 URL ───────────────────────────────────────────────────
export const QR_URL =
  'https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/active-shooter-response';

// ─── 오디오 실측 길이에 맞출 가이드 기간 (Qwen3-TTS 연계 전 가예정치) ─────────
export const AUDIO_DURATIONS: Record<string, number> = {
  S01: 7.0,
  S02: 12.0,
  S03: 4.5,
  S04: 18.0,
  S05: 16.0,
  S06: 20.0,
  S07: 22.0,
  S08: 16.0,
  S09: 20.0,
  S10: 22.0,
  S11: 22.0,
  S12: 18.0,
};

export const getSlideDurationSec = (id: string): number => {
  const slide = SLIDES.find((s) => s.id === id);
  const base = (AUDIO_DURATIONS[id] ?? 5.0) + (slide?.holdSec ?? 0);

  if (slide?.type === 'section') return base;
  return base + AUDIO_HEAD_PAD_SEC + AUDIO_TAIL_PAD_SEC;
};

export const audioSrc = (id: string) =>
  `active-shooter-0908/audio/${id.toLowerCase()}.mp3`;

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
