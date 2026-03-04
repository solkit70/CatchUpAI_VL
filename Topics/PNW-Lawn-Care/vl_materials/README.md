# vl_materials — 참조 자료 현황

**업데이트**: 2026-03-03

---

## PDF 요약 현황

### ✅ 마크다운 요약 완료

| PDF 파일 | 내용 | 요약 MD 파일 |
|---------|------|------------|
| `man_ESP-ME3_QuickReference_en-es-fr.pdf` | 4단계 프로그래밍 차트, 수동 관수, ALERT 표시 | `esp-me3-quick-reference.md` |
| `man_ESP-ME3_SpecialFeatures_en-es-fr.pdf` | 저장/복원, Master Valve, Rain Sensor Bypass, 초기화, 유량 센서, 스테이션 간 지연 | `esp-me3-quick-reference.md` |
| `d41274_15ja20_esp-me3-user-manual-advanced-dom_en-en.pdf` | 전체 설치+기본/고급 프로그래밍, 특수 기능, 문제 해결 (18페이지 전체) | `esp-me3-complete-guide.md` |
| `d42294_smart_home_integration.pdf` | LNK2 WiFi 모듈 설정, Amazon Alexa 연동, 음성 명령 목록 | `alexa-smart-home-guide.md` |

---

### ⏳ 미처리 PDF (향후 필요 시 요약 예정)

| PDF 파일 | 추정 내용 | 우선순위 | 비고 |
|---------|---------|---------|------|
| `d41298_-_esp-me3_-_tech_spec_-_en.pdf` | 기술 사양서 (전압, 전류, 방수 등급 등) | 낮음 | 설치/수리 시 필요 |
| `d41296_-_esp-me3_-_sell_sheet_-_en.pdf` | 제품 소개 카탈로그 | 낮음 | 학습보다 구매 참고용 |
| `d42495_-_esp-2wire_-_compatible_flow_sensors_document-_pdf_digital.pdf` | ESP-ME3 호환 유량 센서 목록 | 중간 | Flow 센서 도입 시 필요 |
| `C_ESP4ME3.pdf` | 엔지니어링 설치 도면 (배선도) | 낮음 | 전문가 수준 설치 시 필요, 1페이지 도면 |

---

## 사진/동영상 현황

| 파일 | 종류 | 내용 추정 | 활용 계획 |
|------|------|---------|---------|
| `IMG_4406.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4407.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4408.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4408.MOV` | 동영상 | 스프링클러 작동 영상 | M2 학습 참조 |
| `IMG_4409.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4409.MOV` | 동영상 | 스프링클러 작동 영상 | M2 학습 참조 |
| `IMG_4410.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4410.MOV` | 동영상 | 스프링클러 작동 영상 | M2 학습 참조 |
| `IMG_4411.JPEG` | 사진 | 스프링클러 관련 | M1 lawn-audit 또는 M2 참조 |
| `IMG_4411.MOV` | 동영상 | 스프링클러 작동 영상 | M2 학습 참조 |

---

## 기타 파일

| 파일 | 내용 |
|------|------|
| `Info.txt` | 메모 (내용 미확인) |

---

## 미처리 PDF 대책 옵션

미처리 PDF가 필요해질 때 아래 방법 중 선택:

1. **Read 도구로 직접 읽기** — Claude Code가 PDF 직독 가능 (작은 PDF에 유리)
2. **학습 세션 중 요약** — 해당 내용이 필요한 모듈(M2/M3) 시작 시 그때 요약
3. **우선순위 낮은 것은 생략** — Sell sheet, Tech spec은 학습에 불필요할 수 있음
4. **PDF 전용 Skill 또는 앱 제작** — PDF를 자동으로 읽고 마크다운으로 요약하는 도구
   - Claude Code Skill: `/pdf-to-md` 형태로 PDF 경로 입력 → MD 요약 자동 생성
   - 참조: 이미 `youtube-to-md` Skill이 존재 — 같은 패턴으로 `pdf-to-md` Skill 제작 가능
   - 배치 처리: 여러 PDF를 한 번에 처리하는 스크립트 형태도 가능
