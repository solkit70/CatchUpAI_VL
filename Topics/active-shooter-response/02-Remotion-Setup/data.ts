// Active Shooter Response Training — active-shooter-0908
// 슬라이드 플랜: Ingest/CatchUpAI_VL/Topics/active-shooter-response/02-Remotion-Setup/video-slide-plan.md
//
// 본 영상은 시민단체(NGO) 실무진과 자원봉사자들을 대상으로 한
// 공인 재난 대처 교육 경로(FEMA, ALERRT, ALICE) 및 자체 대응 자원(EAP, Tabletop, Stop the Bleed) 가이드 안내서입니다.

export const FPS = 30;
export const SEC = (s: number) => Math.ceil(s * FPS);

// ─── 오디오 패딩 ──────────────────────────────────────────────────────────
export const AUDIO_HEAD_PAD_SEC = 0.1;
export const AUDIO_TAIL_PAD_SEC = 0.4;

// ─── 에셋 준비 상황 ────────────────────────────────────────────────────────
export const PHOTOS_READY = false; // 이미지 대기 단계 (프리뷰 시에는 placeholder 구동)

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
  signal: '#ff4d4f',       // Crimson/Red - 최후 수단, FIGHT 및 강세 컬러
  accent: '#FF9F43',       // Caution Orange - 주의 수칙, HIDE 및 서브 강조
  safe: '#52c41a',         // Green - RUN 및 안전/경찰 대응 테마 컬러
  fema: '#1890ff',         // Blue - FEMA, 교육 및 안전망 키트 강조 컬러
  white: '#FFFFFF',
} as const;

// ─── 타입 정의 ─────────────────────────────────────────────────────────────
export type SlideType = 'title' | 'section' | 'bullet' | 'compare' | 'workflow' | 'stat' | 'outro';

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
  photo?: string;         // public/active-shooter-0908/images/ 아래 생성될 사진 또는 동영상 파일명
  holdSec?: number;       // 나레이션 종료 후 머무는 추가 시간
  spec?: Record<string, unknown>; // 세부 컴포넌트용 특수 명세
}

// ─── 슬라이드 12장 구성 데이터 (NGO 교육 경로 및 자원 가이드 기반 개편) ───
export const SLIDES: SlideData[] = [
  {
    id: 'S01',
    type: 'title',
    title: '시민단체를 위한 비상 대처 및 공인 교육 경로 가이드',
    subtitle: 'Active Shooter Response: NGO Training Guide',
    photo: 'slide_01_bg.mp4', // [AI_VIDEO] 배경 클립 지정
    spec: { subtitleKo: 'DHS 공식 행동 지침 및 안전망 자원 안내' },
  },
  {
    id: 'S02',
    type: 'bullet',
    eyebrow: '우리가 직면한 현실',
    title: '시애틀센터 참사와 시민단체의 안전망',
    photo: 'slide_02_context.png', // [AI_IMAGE] 삽입형
    spec: { badgeColor: 'signal', badgeText: '시애틀센터 총격 사건' },
    lines: [
      { label: '🚨 시애틀 참사', text: '지난 7월 26일 시애틀센터 축제 현장에서 발생한 갑작스러운 총격으로 7명의 사상자가 유발되었습니다.' },
      { label: '🛑 연쇄 락다운', text: '사건 직후 일대 상권 봉쇄 및 모노레일 전면 중단 등 도심 전반에 극도의 혼란이 초래되었습니다.', accent: 'signal' },
      { label: '👮 안전망 경고', text: '주시애틀총영사관은 단체 봉사자들의 사전 대처 계획(EAP) 숙지가 생사를 가를 핵심이라고 강조했습니다.', accent: 'safe' },
    ],
  },
  {
    id: 'S03',
    type: 'section',
    title: 'PART 1. 공인 비상대응 트레이닝 비교',
    subtitle: 'FEMA ➔ ALERRT ➔ ALICE',
    photo: 'slide_03_bg.mp4', // [AI_VIDEO] 섹션 배경 클립 지정
    spec: { icon: '🚨' },
  },
  {
    id: 'S04',
    type: 'compare',
    eyebrow: '공인 대응 트레이닝',
    title: '공공 안전 대응 교육 3대 솔루션 비교',
    spec: {
      badgeColor: 'fema',
      badgeText: '트레이닝 경로 가이드',
      headers: ['교육 프로그램명', '신청/수강 경로', '핵심 특징 및 대상'],
      rows: [
        ['FEMA IS-907.A', 'training.fema.gov', '무료 온라인 과정 / 1시간 이수 시 미 정부 공식 수료증 발급'],
        ['ALERRT CRASE', 'alerrt.org', 'Avoid-Deny-Defend 전술 드릴 / 지역 경찰서 무료 대면 훈련 매핑'],
        ['ALICE Navigate360', 'alicelearning.com', '능동형 대항 및 바리케이드 요령 / 민간 단체용 정교한 유료 솔루션'],
      ],
    },
    lines: [
      { text: '각 단체의 예산 규모와 자원봉사 교육 요건에 부합하는 트레이닝을 전략적으로 선정하십시오.', accent: 'fema' },
    ],
  },
  {
    id: 'S05',
    type: 'workflow',
    eyebrow: '온라인 이수 과정',
    title: 'FEMA IS-907.A 온라인 수강 절차',
    spec: {
      badgeColor: 'fema',
      badgeText: '1시간 무료 수료증',
      steps: [
        { num: '01', title: '학습 홈 접속', desc: 'FEMA 독립 학습 포털에 가입 및 로그인' },
        { num: '02', title: '비디오 이수', desc: '1시간 분량의 재난 대응 시뮬레이션 강의 시청' },
        { num: '03', title: '온라인 퀴즈', desc: '75% 이상 정답 통과 요건 (자유로운 재응시 가능)' },
        { num: '04', title: '이수증 획득', desc: '이메일로 미 정부 공식 이수증(PDF) 수신 보존' },
      ],
    },
  },
  {
    id: 'S06',
    type: 'workflow',
    eyebrow: '오프라인 전술 훈련',
    title: 'ALERRT CRASE 대면 교육 신청 방법',
    spec: {
      badgeColor: 'accent',
      badgeText: '무료 경찰 드릴',
      steps: [
        { num: '01', title: '교육 포털 탐색', desc: 'alerrt.org 에서 거주 주(State) 내의 오픈 클래스 확인' },
        { num: '02', title: '지역 경찰서 연락', desc: 'Local PD 공공안전 분과에 단체 무료 대면 훈련 가능성 질의' },
        { num: '03', title: '현장 실전 드릴', desc: '봉사자 전원이 대피, 차단(바리케이드), 물리 방어 실습 수행' },
      ],
    },
  },
  {
    id: 'S07',
    type: 'section',
    title: 'PART 2. 자체 비상 대처체계 및 안전 자원 구축',
    subtitle: 'EAP ➔ Tabletop ➔ Stop the Bleed',
    photo: 'slide_07_bg.mp4', // [AI_VIDEO] 섹션 배경 클립 지정
    spec: { icon: '🩹' },
  },
  {
    id: 'S08',
    type: 'bullet',
    eyebrow: '비상 대응 설계',
    title: 'EAP(비상대응계획) 수립과 봉사자 역할 한계',
    photo: 'slide_08_boundaries.png', // [AI_IMAGE] 삽입형
    spec: { badgeColor: 'accent', badgeText: '역할 경계 명문화' },
    lines: [
      { label: '📝 EAP 문서화', text: '비상 연락망 가동, 비상구 사전 개방 및 집결 장소 설계를 명문화하십시오.' },
      { label: '🛡️ 무장대항 금지', text: '자원봉사자는 사설 경비가 아니므로 범인을 직접 추적할 책임을 지지 않습니다.', accent: 'signal' },
      { label: '🚪 대피 안내 책무', text: '봉사자의 책무는 순수 대피 방향 지시 및 통제 연락망 기동으로 한정해야 법적 책임을 보호받습니다.', accent: 'safe' },
    ],
  },
  {
    id: 'S09',
    type: 'bullet',
    eyebrow: '무상 시뮬레이션',
    title: 'CISA 도상 모의 훈련 키트 활용법',
    photo: 'slide_09_tabletop.mp4', // [AI_VIDEO] 삽입형
    spec: { badgeColor: 'fema', badgeText: 'Tabletop-in-a-box' },
    lines: [
      { label: '📦 키트 무료 다운', text: '연방 국토안보부 CISA 가 배포하는 가상 재난 도상 훈련 패키지를 수집하십시오.' },
      { label: '🎲 가상 시나리오', text: '리더십과 실무 봉사자가 도면 위에 시나리오 카드를 배치하고 가상 훈련을 점검합니다.', accent: 'fema' },
      { label: '🔍 취업/보안 보강', text: '비상구 락 상태, 통신 음영 지역 대안, 병목 동선 등 실전 취약점을 도출해 EAP를 개정합니다.', accent: 'accent' },
    ],
  },
  {
    id: 'S10',
    type: 'stat',
    eyebrow: '의료 생존 확률',
    title: 'Stop the Bleed 지혈대 구비와 생존율',
    spec: {
      badgeColor: 'signal',
      badgeText: '최초 5분 골든타임',
      value: 35, // 35% 통계 카운트업
      caption: '의료진이 도달하기 전 대량 출혈사를 막기 위해, 표준 지혈대(Tourniquet) 구비와 지혈대 사용법 교육을 수료한 봉사자 배치 시 생존율 증가 수치',
    },
    lines: [
      { text: '대량 출혈 참사는 예방 가능한 즉각 사망 요인 1위입니다. 지혈 훈련(Stop the Bleed)에 전수 참가시키십시오.', accent: 'signal' },
    ],
  },
  {
    id: 'S11',
    type: 'bullet',
    eyebrow: '경찰 도착 시',
    title: '무장 경찰 진입 시 조우 수칙',
    photo: 'slide_11_police.mp4', // [AI_VIDEO] 삽입형
    spec: { badgeColor: 'safe', badgeText: '오발 저격 원천 예방' },
    lines: [
      { label: '👐 양손 노출', text: '경찰과 직면 시 즉시 양손을 머리 위로 올리고 손가락을 쫙 펴서 무장 상태가 아님을 증명하십시오.', accent: 'safe' },
      { label: '🎒 소지품 투기', text: '휴대폰이나 무기로 오인될 소지가 있는 물품을 즉시 던지듯 멀리하십시오.', accent: 'signal' },
      { label: '🚫 접촉 금지', text: '돌발적인 고함, 밀착, 경찰을 붙잡는 포옹 행동은 저격 대상으로 간주되어 절대 금지됩니다.' },
    ],
  },
  {
    id: 'S12',
    type: 'outro',
    title: '안전을 향한 따뜻한 연합',
    subtitle: '시민단체 비상 가이드 배포 오픈',
    photo: 'slide_12_qr.png', // [AI_IMAGE] 카드 QR형 삽입
    spec: { showLargeQr: true, cta: '우측의 QR코드를 스캔하여 한인 NGO 전용 비상 대응 가이드북 및 EAP 설계 양식을 다운로드하고, 공동체의 안전 연합에 지금 동참하십시오.' },
  },
];

// ─── QR 코드 목적지 URL ───────────────────────────────────────────────────
export const QR_URL =
  'https://github.com/solkit70/CatchUpAI_VL/tree/main/Topics/active-shooter-response';

// ─── 오디오 실측 길이에 맞출 가이드 기간 (재기획으로 인한 임시 가예정치) ─────────
export const AUDIO_DURATIONS: Record<string, number> = {
  S01: 15.0,
  S02: 17.5,
  S03: 4.0,
  S04: 19.0,
  S05: 22.0,
  S06: 22.0,
  S07: 4.0,
  S08: 20.0,
  S09: 20.0,
  S10: 17.0,
  S11: 17.0,
  S12: 16.5,
};

export const getSlideDurationSec = (id: string): number => {
  const slide = SLIDES.find((s) => s.id === id);
  const base = AUDIO_DURATIONS[id] ?? 5.0;

  // 섹션 슬라이드는 패딩 연산식에서 완전히 제외함 (4초 이하 고정)
  return base > 4 ? base + AUDIO_HEAD_PAD_SEC + AUDIO_TAIL_PAD_SEC : base;
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
