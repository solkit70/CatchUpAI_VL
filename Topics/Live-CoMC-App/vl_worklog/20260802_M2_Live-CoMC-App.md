# WorkLog - M2: 파이프라인 아키텍처와 App Boundary 확정

**날짜**: 2026-08-02
**Topic**: Live-CoMC-App
**모듈**: M2 - 파이프라인 아키텍처와 App Boundary 확정
**학습 시간**: M1에 이어 같은 세션에서 연속 진행

---

## 🎯 오늘의 학습 목표

- [x] 실습 1: 파이프라인 다이어그램 작성
- [x] 실습 2: app-boundary.md 작성
- [x] 실습 3: 기술 선택 비교표 작성

---

## 📚 진행 내용

### 1. 실습 1 — 파이프라인 다이어그램 작성

**과정**: 승인된 설계안(`ethereal-puzzling-seahorse.md`)의 원 파이프라인(①Wake→②VAD→③STT→④Intent→⑤Context→⑥LLM→⑦Verify→⑧Overlay+⑨TTS)을 그대로 9단계 Mermaid 다이어그램으로 옮기고, 각 화살표에 실제 데이터(오디오 버퍼, `broadcast_context.json`, `claim_map` 등)를 명시했다.

**결과**: `concepts/pipeline-diagram.md`. M1에서 검증한 `broadcast_context.json`이 ⑤단계 입력이라는 연결점을 명시적으로 표시해, M1 산출물이 M2 아키텍처에 실제로 어떻게 쓰이는지 연결했다.

### 2. 실습 2 — app-boundary.md 작성

**과정**: 원 계획서의 MVP 경계 표(포함 항목 미정의, 제외 9개)를 그대로 가져오되, 포함 범위를 M1~M9 모듈 산출물에 1:1로 매핑해 11개로 정리했다(M10 리허설은 "기능"이 아니라 "검증 활동"이라 포함 목록에서 제외). 제외 범위는 원안 9개에 "모바일/웹 버전"·"다국어 TTS 출력" 2개를 추가해 11개로 확장했다.

**결과**: `guides/app-boundary.md`. 원안과 대조해 누락 없음을 확인(실습 2 DoD 요구사항).

**메모/인사이트**: "컴포넌트별 절대 하지 말아야 할 일" 목록을 작성하면서, 안전 검증 게이트가 "LLM 자기평가에 위임하지 않는다"는 원칙이 계획서에는 안전장치 섹션에만 있었는데 여기서 컴포넌트 단위 금지 규칙으로 다시 명문화되어 M3·M8 설계의 전제 조건으로 더 명확해졌다.

### 3. 실습 3 — 기술 선택 비교표 작성

**과정**: 볼트 파일 접근·오디오 I/O·OBS 연동·개발 속도 4기준으로 Electron/Tauri/순수 Python을 비교했다.

**결과**: `guides/tech-choice.md`. Electron 채택(OBS Browser Source 궁합 + 파일 기반 파이프라인 재사용 + 프로세스 분리), Tauri 기각(Rust 학습 비용이 90h 일정 내 리스크), 순수 Python도 참고로 기각(OBS 연동 위해 결국 HTTP 서버가 필요해 Electron과 구조가 수렴).

---

## 🐛 문제 해결 로그

특이 문제 없음.

---

## 📊 DoD 체크리스트

- [x] 9단계 파이프라인 다이어그램 완성
- [x] `app-boundary.md`에 포함 11개 + 제외 11개 항목 전부 등재
- [x] 기술 선택 비교표 완성 (Electron 채택 근거 명시)
- [x] "컴포넌트별 절대 하지 말아야 할 일" 목록 작성
- [x] README 작성 완료
- [x] WorkLog 작성 완료

**완료율**: 6/6 (100%) — M2 DoD 전체 달성

---

## 💡 Daily Retrospective

### What went well (잘된 점)
- M1 산출물(파서 규칙, 금칙 섹션 구분)을 M2 아키텍처 문서에 실제로 연결해 모듈 간 단절 없이 진행했다

### What could be improved (개선할 점)
- 포함 범위 11개 항목은 모듈 매핑을 그대로 가져온 것이라 다소 기계적이다. M3 이후 실제 스키마 작업을 하면서 항목이 더 세분화될 수 있음을 열어둔다

### Insights (인사이트)
- "이 문서에 없는 기능 요청은 v2로 미룬다"는 원칙이 문서 한 장으로 명문화되니, 앞으로 M7·M9에서 범위가 흔들릴 때 되돌아볼 구체적 근거가 생겼다

### Tomorrow's focus (다음에 할 것)
- M3 - 데이터 계약과 안전 정책 스펙 시작 (7종 JSON 스키마, `safety_policy.json`, LLM 3사 스키마 정규화 설계) — 난이도⭐⭐/9h로 M1·M2보다 크므로 별도 세션으로 분리 권장

---

## 📎 참조 및 산출물

**생성된 파일/폴더**:
- `02-Architecture-and-Boundary/concepts/pipeline-diagram.md`
- `02-Architecture-and-Boundary/guides/app-boundary.md`
- `02-Architecture-and-Boundary/guides/tech-choice.md`
- `02-Architecture-and-Boundary/README.md`

**참조 자료**:
- `C:\Users\dougg\.claude\plans\ethereal-puzzling-seahorse.md` (승인된 설계안)
- `Topics/Vibe-Guiding-VSCode/02-Architecture-Design/poc-boundary.md` (템플릿 참조)
- M1 산출물: `01-Concept-and-Rundown-Contract/`

**다음 세션 준비사항**:
- 없음 — M2 완료, M3(9h, ⭐⭐)로 진행 가능. M3는 시간이 크므로 여러 세션에 걸쳐 진행될 가능성 높음

---

**작성자**: solkit70
**방법론**: VibeLearn AI
