# Rain Bird ESP-ME3 스마트홈 연동 가이드

**출처**: Smart Home Integration PDF (d42294)
**정리일**: 2026-03-03
**필요 장치**: LNK2 WiFi 모듈 (별도 구매)

---

## 준비물

| 항목 | 비고 |
|------|------|
| Rain Bird ESP-ME3 컨트롤러 | 기본 기기 |
| LNK2 WiFi 모듈 | 별도 구매 (ESP-ME3 하단 슬롯에 장착) |
| Rain Bird 앱 | iOS / Android 무료 다운로드 |
| Amazon Echo (Alexa) | 음성 제어 원하는 경우 |
| 2.4GHz WiFi 네트워크 | LNK2는 2.4GHz 전용 (5GHz 미지원) |

---

## 초기 설정 단계

### 1단계: LNK2 모듈 장착

1. 컨트롤러 전원 OFF
2. ESP-ME3 하단의 LNK 슬롯에 LNK2 모듈 꽂기
3. 컨트롤러 전원 ON
4. 컨트롤러 화면에 WiFi 아이콘 표시되는지 확인

### 2단계: Rain Bird 앱 설치 및 계정 생성

1. App Store / Google Play에서 "Rain Bird" 검색
2. 앱 설치 후 계정 생성 (이메일 필요)
3. 앱 로그인

### 3단계: 컨트롤러를 앱에 연결

1. Rain Bird 앱 → **Add Device**
2. ESP-ME3 선택
3. 홈 WiFi 네트워크 선택 및 비밀번호 입력
4. 컨트롤러와 앱 페어링 완료
5. 각 스테이션에 이름 부여 (예: "앞마당", "뒤뜰", "화단")

> 스테이션 이름을 알아보기 쉽게 설정하면 Alexa 음성 명령 편리

### 4단계: Alexa 연동 (선택)

1. Rain Bird 앱 → **Settings** → **Connected Home**
2. **Amazon Alexa** → Enable 클릭
3. Amazon 계정 로그인 및 권한 허용
4. Alexa 앱 → Skills → "Rain Bird" 검색 → Enable
5. Alexa가 자동으로 스프링클러 구역 검색 (Discover Devices)

---

## Alexa 음성 명령 (주요 명령어)

### 즉시 관수

```
"Alexa, ask Rain Bird to water [구역 이름] for [X] minutes"
"Alexa, ask Rain Bird to water [구역 이름]"
"Alexa, ask Rain Bird to start [구역 이름]"
```

**예시**:
- "Alexa, ask Rain Bird to water front yard for 15 minutes"
- "Alexa, ask Rain Bird to water zone 3 for 10 minutes"

### 관수 중지

```
"Alexa, ask Rain Bird to stop watering"
"Alexa, ask Rain Bird to stop [구역 이름]"
"Alexa, ask Rain Bird to pause irrigation"
```

### 관수 지연 및 재개

```
"Alexa, ask Rain Bird to delay watering for [X] days"
"Alexa, ask Rain Bird to suspend irrigation for [X] days"
"Alexa, ask Rain Bird to resume irrigation"
```

### 상태 확인

```
"Alexa, ask Rain Bird what's the status"
"Alexa, ask Rain Bird if [구역 이름] is running"
"Alexa, ask Rain Bird when did [구역 이름] last run"
```

### 프로그램 실행

```
"Alexa, ask Rain Bird to run program A"
"Alexa, ask Rain Bird to start program B"
```

---

## Rain Bird 앱 기능

### 원격 제어
- 집 밖에서도 스프링클러 제어
- 단일 구역 / 전체 프로그램 실행·중지
- 실시간 가동 상태 확인

### 스케줄 관리
- 컨트롤러 대신 앱에서 프로그래밍 가능
- 스케줄 저장 및 복원

### 기상 연동 (Weather Intelligence Plus)
- 기상 데이터 기반 자동 물 주기 조정
- 비 예보 시 자동 건너뜀
- 토양 유형, 경사도 등 입력 시 자동 최적화

### 알림
- 관수 시작/종료 알림
- Flow 경보 (누수, 파열 감지)
- 시스템 오류 알림

---

## 활용 시나리오 (Tehaleh WA 기준)

### 시나리오 1: 여행 중 물 주기 지연
```
상황: 5일 여행 출발, 비 예보 있음
명령: "Alexa, ask Rain Bird to delay watering for 3 days"
효과: 앱으로 상태 모니터링 + 귀가 후 자동 재개
```

### 시나리오 2: 잔디 깎기 전날 건너뜀
```
상황: 내일 잔디 깎기 예정, 오늘 관수 건너뛰고 싶음
명령: "Alexa, ask Rain Bird to delay watering for 1 day"
```

### 시나리오 3: 특정 구역 즉시 테스트
```
상황: 뒤뜰 스프링클러 헤드 교체 후 테스트
명령: "Alexa, ask Rain Bird to water back yard for 5 minutes"
```

### 시나리오 4: 여름 猛더위 비상 관수
```
상황: 예상보다 더워서 잔디가 스트레스 받는 상황
명령: "Alexa, ask Rain Bird to water front lawn for 20 minutes"
```

---

## 연결 문제 해결

| 문제 | 원인 | 해결책 |
|------|------|--------|
| 앱에서 컨트롤러 안 보임 | WiFi 연결 끊김 | 앱 재연결 또는 LNK2 재설정 |
| 5GHz WiFi 연결 안 됨 | LNK2는 2.4GHz 전용 | 라우터에서 2.4GHz 네트워크 확인 |
| Alexa 명령 인식 불가 | Skill 비활성화 | Alexa 앱 → Skills → Rain Bird 재활성화 |
| 원격 제어 안 됨 | 앱 로그인 만료 | 앱 재로그인 |

---

**관련 파일**: esp-me3-complete-guide.md, esp-me3-quick-reference.md
**다음 단계**: M2 학습에서 실제 LNK2 설치 및 앱 연동 실습
