# 기술 선택 비교표 — Electron vs Tauri vs 순수 Python

**모듈**: M2 - 파이프라인 아키텍처와 App Boundary 확정
**실습**: 실습 3 — 기술 선택 비교표 작성

---

## 비교표

| 기준 | Electron + Python 사이드카 | Tauri + Python 사이드카 | 순수 Python (Tk/PyQt) |
|---|---|---|---|
| 볼트 파일 접근 | Node `fs`로 간단 (읽기 전용) | Rust 파일 API, 바인딩 추가 학습 필요 | Python 표준 라이브러리로 직접, 가장 간단 |
| 오디오 I/O | Web Audio API + `sounddevice`(Python 사이드카)로 이중화 | 유사하나 Rust 오디오 생태계가 더 낮은 성숙도 | `sounddevice`/`pyaudio` 그대로 사용, 오버레이 렌더링은 별도 창 필요 |
| OBS 연동 (Browser Source) | 내장 HTTP 서버로 `localhost:PORT/overlay` 서빙 → 자연스러운 궁합 | 동일하게 가능하나 Rust HTTP 서버 학습 비용 발생 | Flask 등으로 가능하나 데스크톱 UI와 별도 프로세스 관리 필요 |
| 개발 속도 (1인, 3개월) | React/HTML/CSS로 오버레이 UI 재사용 가능, 생태계 성숙 | 이진 크기·성능은 우수하나 **Rust 학습 곡선 자체가 프로젝트 리스크** | 가장 빠르게 시작 가능하나 OBS Browser Source 연동을 위해 결국 HTTP 서버를 별도로 얹어야 해 구조가 Electron과 유사해짐 |

## 결론

**Electron + Python 사이드카 채택.** OBS Browser Source가 HTML/CSS/JS를 그대로 렌더링하므로 오버레이 개발이 웹 개발과 동일해지고, Python 사이드카가 M1~M8에서 만든 파일 기반 파이프라인 스크립트를 재작성 없이 그대로 실행 엔진으로 쓸 수 있다. 프로세스가 분리되어 있어 Python 엔진이 죽어도 Electron 셸의 패닉 스톱·오버레이가 살아남는다는 안전상 이점도 크다.

**Tauri 기각.** 이진 크기와 메모리 효율은 우수하지만, Rust 학습 비용이 90시간(12주)이라는 이미 촉박한 일정 안에서 그 자체로 프로젝트 리스크가 된다. 안전장치 설계나 실시간 오디오 파이프라인처럼 이 프로젝트의 핵심 학습 목표와 무관한 곳에 시간을 쓰게 된다.

**순수 Python 기각(참고)**: 가장 빠르게 시작할 수 있어 보이지만, OBS Browser Source 요구사항 때문에 결국 HTTP 서버를 추가로 얹어야 해 "단일 프로세스"라는 장점이 사라지고, UI 개발 생산성도 Electron보다 낮다.
