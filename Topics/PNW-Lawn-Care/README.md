# PNW-Lawn-Care — Topic README

> **방법론**: VibeLearn AI v2.0
> **상태**: ✅ 완료
> **학습 기간**: 2026-03-03 ~ 2026-04-05 (약 5주)
> **총 학습 시간**: ~20h
> **위치**: Tehaleh, WA (Pierce County, USDA Zone 8b)

---

## 📌 이 Topic은 무엇인가

태평양 북서부(PNW) 기후 특성에 맞는 **계절별 잔디 관리**와 **Rain Bird ESP-ME3 스프링클러 시스템 마스터링**을 다룹니다.

> **핵심 한 줄**: "PNW 잔디는 여름 건기를 위해 봄에 준비하고, 스프링클러는 Seasonal Adjust 하나로 계절을 탄다."

**내 마당 정보**:
| 항목 | 내용 |
|------|------|
| 위치 | Tehaleh, WA / Pierce County / Zone 8b |
| 면적 | 앞마당 2,265 sq ft + 뒷마당 6,656 sq ft = **약 8,920 sq ft** |
| 잔디 종류 | Cool-season (Tall Fescue / Perennial Ryegrass / Kentucky Bluegrass 혼합) |
| 스프링클러 | Rain Bird ESP-ME3 (8 스테이션 운영 중) |

---

## 🎬 영상

이 Topic으로 제작해 공개한 영상 4편입니다.

| 주제 | 버전 | 링크 |
|---|---|---|
| PNW 잔디 관리 + 초개인화 | 🇰🇷 한국어 | https://youtu.be/ZIhc46O6ZRw (5:35) |
| PNW 잔디 관리 + 초개인화 | 🇺🇸 English | https://youtu.be/jLS0NKtstdI (4:30) |
| Tehaleh HOA 강좌 현장 취재 | 🇰🇷 한국어 | https://youtu.be/EHLzj4dZlmo (8:12) |
| Tehaleh HOA 강좌 현장 취재 | 🇺🇸 English | https://youtu.be/gpa3tBJxRM4 (8:21) |

## 📚 모듈 학습 순서

처음 이 폴더를 여는 분은 아래 순서대로 진행하세요.

| 순서 | 모듈 | 내용 | 상태 |
|------|------|------|------|
| 1 | [M1: PNW 잔디 기초 + 봄 준비](01-Spring-Basics/README.md) | PNW 기후 이해, 봄 3대 작업, 마당 현황 진단 | ✅ 완료 |
| 2 | [M2: Rain Bird ESP-ME3 마스터](02-Sprinkler-Master/README.md) | 컨트롤러 완전 이해, 봄 스케줄 설정, Cycle+Soak | ✅ 완료 |
| 3 | [M3: 여름 관리 + 문제 진단](03-Summer-Troubleshoot/README.md) | 휴면 vs. 고사 구분, 잔디 문제 진단, 여름 관수 스케줄 | ✅ 완료 |
| 4 | [M4: 연간 계획 + Topic 마무리](04-Annual-Plan/README.md) | 가을 관리, 연간 캘린더, Winterizing, 자기 평가 | ✅ 완료 |

## 🧾 실제 관리 기록

- [2026 실행 로그](maintenance-log-2026.md) — 주간 일정 관리와 WorkLog에 흩어져 있던 제초제, 비료, 잔디깎이, Dethatching, 스프링클러 세팅, 상태 관찰 기록을 날짜순으로 통합.

---

## 🌿 핵심 교훈 4가지

**1. PNW 잔디는 여름을 위해 봄에 준비한다**
7~8월 건기에 Cool-season 잔디는 스트레스를 받습니다. 봄(3~4월)에 Pre-emergent + 비료로 뿌리를 강하게 만들어두는 것이 여름 생존의 열쇠.

**2. Pre-emergent가 최우선 — 단 Overseeding은 8~10주 후에**
Pre-emergent 살포 후 8~10주 동안 Overseeding 불가. 봄 = Pre-emergent 우선, Overseeding은 9월로.

**3. 갈색 잔디 = 죽은 게 아니다 (Dormancy)**
PNW 여름 건기에 잔디가 갈색이 돼도 뿌리는 살아있습니다. 가을 우기가 오면 자연 회복.

**4. Seasonal Adjust 하나로 계절을 탄다**
각 스테이션 런타임을 매번 바꾸지 않아도 됩니다. Seasonal Adjust % 하나로 전체 조정.

---

## 📅 연간 핵심 타이밍 (Tehaleh WA 기준)

| 시기 | 핵심 작업 |
|------|---------|
| **3월 중순** | Pre-emergent 살포 (잡초 예방 — 골든 타임) |
| **3~4월** | 봄 비료, 스프링클러 재가동 (Seasonal Adjust 70%) |
| **5~6월** | Seasonal Adjust 80~90%로 조정 |
| **7~8월** | 여름 관수 피크 (Seasonal Adjust 100~110%) |
| **9월** | Overseeding (가장 중요 — 연간 1회) |
| **10월** | 가을 비료, 낙엽 관리 |
| **11월** | 스프링클러 Winterizing |

---

## 📁 폴더 구조

```
PNW-Lawn-Care/
├── README.md                    ← 지금 보고 있는 파일 (Topic 전체 안내)
├── topic_info.md                ← Topic 기본 정보
├── 01-Spring-Basics/            ← M1 산출물
├── 02-Sprinkler-Master/         ← M2 산출물
├── 03-Summer-Troubleshoot/      ← M3 산출물
├── 04-Annual-Plan/              ← M4 산출물
├── vl_roadmap/                  ← 학습 로드맵
├── vl_worklog/                  ← 세션별 학습 일지
├── vl_prompts/                  ← 이 Topic용 프롬프트
└── vl_materials/                ← 참조 자료 (ESP-ME3 가이드 등)
```

---

## 🎓 Topic 완료 성과

| 산출물 | 내용 |
|--------|------|
| PNW 기후 + 잔디 이해 | Cool-season 3종 특성, 연간 생장 주기 |
| 봄 작업 완료 | Pre-emergent 2포대 살포 (2026-04-03) |
| ESP-ME3 완전 이해 | Program A/B/C 설정, Cycle+Soak, Seasonal Adjust |
| 문제 진단 가이드 | 10가지 잔디 문제 진단표 완성 |
| 연간 캘린더 | Tehaleh WA 기준 12개월 관리 일정 |
| Winterizing 체크리스트 | 시즌 마무리 + 봄 재가동 절차 |

**자기 평가**: [M4/self-assessment-complete.md](04-Annual-Plan/self-assessment-complete.md)

---

**방법론**: VibeLearn AI v2.0
**저작**: Changsoo (Claude Code 활용)
