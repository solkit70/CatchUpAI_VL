# CoMC 방송 기동 — 창 하나 (CVL 3, 2026-09-17)
#
#   사용:  comc              (C:\Users\dougg\comc.cmd — 어느 폴더에서든. 회차는 최신 Rundown 에서 자동)
#          comc 29           (회차 지정)
#          powershell -ExecutionPolicy Bypass -File start_comc.ps1 -Live 28
#
#   이 창 하나에 오버레이 서버(8777) · 재생기 · 핫키 · 엔진이 다 들어 있다 (comc_console.py).
#   브라우저 탭 http://127.0.0.1:8778/ 이 자동으로 열린다 — 질문 · 모드 · 패닉 · 파트 · 프리플라이트 · 캐주얼 브리프 전부 거기서.
#   OBS Browser Source 는 그대로 http://127.0.0.1:8777/ 을 본다.
#
# 끝낼 때: 이 창에서 Ctrl+C — 전부 같이 꺼진다.
# ⚠️ 이 파일은 UTF-8 BOM 으로 저장돼 있어야 한다 — PowerShell 5.1 은 BOM 이 없으면 한글을 깨뜨린다.
# (CVL 2 의 「창 4개」판은 폐기 — operator-guide.md 「왜 창 하나로 바꿨나」 참조.)
param([string]$Live = "", [switch]$NoBrowser)

$env:PYTHONUTF8 = "1"
chcp 65001 | Out-Null
$here  = Split-Path -Parent $MyInvocation.MyCommand.Path
$topic = (Resolve-Path (Join-Path $here "..\..\..")).Path
$src   = Join-Path $topic "07-CoMC-Engine-POC\src"
$vault = (Resolve-Path (Join-Path $topic "..\..\..\..")).Path

# 회차를 안 주면 AI\Roundup 의 가장 큰 「LiveNN Weekly Rundown」 번호를 쓴다 — 매주 명령을 바꾸지 않아도 되게
if (-not $Live) {
  $nums = Get-ChildItem (Join-Path $vault "AI\Roundup") -Filter "* - Live* Weekly Rundown.md" |
          ForEach-Object { if ($_.Name -match "Live(\d+) Weekly Rundown") { [int]$Matches[1] } }
  if ($nums) { $Live = [string]($nums | Sort-Object | Select-Object -Last 1) } else { $Live = "28" }
  Write-Host "회차 자동 감지: Live #$Live   (다른 회차는  comc 29  처럼)"
}

# 0. 오늘 Rundown 파싱 + 1부 컨텍스트 + 모드 REVIEW (이 창에서, 결과가 보이게)
Push-Location $src
python 01_parse_rundown.py --live $Live
python 02_resolve_context.py --live $Live --part 1
python 06_render_output.py --live $Live --set-mode REVIEW --reason "broadcast start - REVIEW"
# 0-b. 캐주얼 브리프 (CVL 4) — 이번 주 기록 + 서울·시애틀 날씨. 코엠씨의 잡담·주간 회고 근거
python 02b_build_casual_brief.py --live $Live
Pop-Location

# 1. 콘솔 — 이 창을 차지한다. Ctrl+C 로 끝.
Set-Location -LiteralPath $here
if ($NoBrowser) { python comc_console.py --live $Live --no-browser }
else            { python comc_console.py --live $Live }
