---
title: Browser Userscript Settings - Obsidian Omnisearch Google CMDS
created: 2026-06-28 07:00:00
tags:
  - obsidian
  - omnisearch
  - tampermonkey
  - setup
---

## 목적

이 문서는 `Obsidian Omnisearch Google CMDS` userscript를 브라우저에 설치하고 현재 vault와 연결하기 위한 설정값을 기록한다. 브라우저 확장 설치, userscript 설치, localhost 권한 승인은 보안상 사용자가 직접 UI에서 승인해야 한다.

## 현재 확인된 상태

| 항목                                    | 상태                  |
| ------------------------------------- | ------------------- |
| Obsidian 실행                           | 실행 중                |
| Omnisearch plugin files               | 설치 완료               |
| Local REST API plugin files           | 설치 완료               |
| `.obsidian/community-plugins.json` 등록 | 완료                  |
| Tampermonkey 기본 프로필 설치                | 미확인                 |
| Omnisearch HTTP server port           | Obsidian UI에서 확인 필요 |
| Local REST API port/API key           | Obsidian UI에서 확인 필요 |

## Obsidian 초보자용 플러그인 설치 순서

현재 vault에는 `Omnisearch`와 `Local REST API with MCP` plugin 파일이 이미 `.obsidian/plugins/` 아래에 설치되어 있고, `.obsidian/community-plugins.json`에도 등록되어 있다. 그래도 Obsidian 화면에서 plugin이 보이지 않거나 활성화되어 있지 않을 수 있으므로, 아래 순서대로 UI에서 확인한다.

### 1. 현재 vault가 맞는지 확인

1. Obsidian을 연다.
2. 왼쪽 아래 톱니바퀴 아이콘을 눌러 Settings를 연다.
3. 화면 왼쪽 아래 또는 vault switcher에서 현재 vault 이름이 `Changsoo_Vault`인지 확인한다.
4. 다른 vault가 열려 있으면 `Open another vault` 또는 vault switcher에서 `Changsoo_Vault`를 연다.

### 2. Community plugins 사용 허용

1. Settings 왼쪽 메뉴에서 `Community plugins`를 선택한다.
2. `Restricted mode`가 켜져 있으면 끈다. Obsidian이 확인 창을 띄우면 community plugin 사용을 허용한다.
3. `Installed plugins` 목록이 보이는지 확인한다.

### 3. Omnisearch 설치 또는 활성화

1. Settings → `Community plugins`로 이동한다.
2. `Installed plugins` 목록에 `Omnisearch`가 있는지 찾는다.
3. `Omnisearch`가 보이면 오른쪽 toggle을 ON으로 켠다.
4. `Omnisearch`가 보이지 않으면 `Browse`를 누른다.
5. 검색창에 `Omnisearch`를 입력한다.
6. 검색 결과에서 `Omnisearch`를 선택한다.
7. `Install`을 누른 뒤, 설치가 끝나면 `Enable`을 누른다.
8. Settings 왼쪽 메뉴에 `Omnisearch` 항목이 새로 생겼는지 확인한다.

### 4. Omnisearch HTTP server 켜기

1. Settings 왼쪽 메뉴에서 `Omnisearch`를 선택한다.
2. 설정 화면에서 `HTTP server` 또는 `Enable HTTP server` 항목을 찾는다.
3. 해당 toggle을 ON으로 켠다.
4. HTTP server port를 확인한다. 기본값으로 `51361`이 보이면 그대로 사용한다.
5. port가 `51361`이 아니면 실제 표시된 port를 아래 `Userscript 설정값`의 `v1_port`에 사용한다.

### 5. Local REST API with MCP 설치 또는 활성화

`Local REST API with MCP`는 note 본문 미리보기와 note 열기 기능을 더 안정적으로 쓰기 위한 선택 plugin이다. 처음 테스트는 Omnisearch만으로도 시작할 수 있지만, 최종 사용 환경에서는 함께 설정하는 것이 좋다.

1. Settings → `Community plugins`로 이동한다.
2. `Installed plugins` 목록에 `Local REST API with MCP` 또는 `Local REST API`가 있는지 찾는다.
3. plugin이 보이면 오른쪽 toggle을 ON으로 켠다.
4. plugin이 보이지 않으면 `Browse`를 누른다.
5. 검색창에 `Local REST API`를 입력한다.
6. 검색 결과에서 `Local REST API with MCP`를 선택한다.
7. `Install`을 누른 뒤, 설치가 끝나면 `Enable`을 누른다.
8. Settings 왼쪽 메뉴에 `Local REST API with MCP` 항목이 생겼는지 확인한다.

### 6. Local REST API 설정 확인

1. Settings 왼쪽 메뉴에서 `Local REST API with MCP`를 선택한다.
2. `Enable HTTP server`, `Non-encrypted HTTP server`, 또는 비슷한 이름의 HTTP server 설정을 찾는다.
3. Google userscript와 연결하려면 local HTTP 접근이 필요하므로 해당 항목을 ON으로 켠다.
4. Local REST API port를 확인해서 아래 `Userscript 설정값`의 `v1_lrPort`에 입력한다.
5. API key를 복사해서 userscript의 `v1_lrKey`에 입력한다.
6. API key는 비밀번호처럼 취급한다. WorkLog나 문서에는 전체 값을 기록하지 않고 필요한 경우 앞뒤 일부만 마스킹해서 기록한다.

### 7. Obsidian 재시작 또는 reload

1. plugin을 설치하거나 활성화한 뒤 Obsidian을 한 번 재시작한다.
2. 재시작이 번거로우면 Command palette를 열고 `Reload app without saving`을 실행한다.
3. 다시 Settings로 들어가 `Omnisearch`가 enabled이고 HTTP server가 ON인지 확인한다.
4. Google 테스트 전에 Obsidian은 계속 켜 둔다. Obsidian이 꺼져 있으면 Google sidebar에서 localhost 검색 결과를 가져올 수 없다.

## Obsidian 설정 요약

1. Obsidian에서 현재 vault가 `Changsoo_Vault`인지 확인한다.
2. Settings → Community plugins에서 restricted mode를 끈다.
3. `Omnisearch`를 설치 또는 활성화한다.
4. Settings → Omnisearch에서 `HTTP server`를 켠다.
5. Omnisearch HTTP port를 확인한다. userscript 기본값은 `51361`이다.
6. `Local REST API with MCP`를 설치 또는 활성화한다.
7. Settings → Local REST API with MCP에서 non-encrypted HTTP server를 켠다.
8. Local REST API port와 API key를 확인한다. API key는 WorkLog에 전체 값을 쓰지 말고 마스킹한다.

## Userscript 설정값

| 필드 | 값 |
| --- | --- |
| `v1_port` | `51361` 또는 Obsidian Omnisearch 설정에서 확인한 실제 port |
| `v1_name` | `Changsoo_Vault` |
| `v1_vault` | `Changsoo_Vault` |
| `v1_color` | `#E39AAB` |
| `v1_root` | `C:\AI_study\2026\Changsoo_Vault` |
| `v1_lrPort` | Local REST API 설정에서 확인한 port |
| `v1_lrKey` | Local REST API 설정에서 복사한 API key |
| `vaultsParentDir` | `C:\AI_study\2026` |

## Browser 설정 순서

1. Tampermonkey를 설치한다.
2. Chrome/Edge extension details에서 다음을 확인한다.
   - `Allow User Scripts`: ON
   - Site access: `google.com` 또는 `On all sites`
   - localhost access prompt가 나오면 Always allow domain 선택
3. Raw userscript URL을 연다.
   - `https://raw.githubusercontent.com/johnfkoo951/obsidian-omnisearch-google-cmds/main/obsidian-omnisearch-google-cmds.user.js`
4. Tampermonkey install 화면에서 Install을 누른다.
5. Tampermonkey dashboard에서 `Obsidian Omnisearch in Google — CMDS`가 enabled인지 확인한다.
6. Script settings에서 위 `Userscript 설정값`을 입력한다.

## 성공 기준

- Google 검색 화면 오른쪽 sidebar에 `Omnisearch by CMDS` 또는 Obsidian result card가 표시된다.
- `VibeLearn`, `GOBI`, `Peter Thiel` 중 하나의 검색어에서 vault 내부 note result가 1개 이상 표시된다.
- result click 시 Obsidian에서 해당 note가 열린다.
