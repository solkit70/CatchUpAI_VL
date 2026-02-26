# validate-localization.ps1
# Runs 5 quality gate checks on Korean/English document pairs.
#
# Usage: powershell -ExecutionPolicy Bypass -File scripts/validate-localization.ps1
# Exit code: 0 = all checks passed, 1 = one or more checks failed

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir

$failCount = 0
$passCount = 0

function Pass($msg) {
    Write-Host "  [PASS] $msg" -ForegroundColor Green
    $script:passCount++
}

function Fail($msg) {
    Write-Host "  [FAIL] $msg" -ForegroundColor Red
    $script:failCount++
}

function Header($title) {
    Write-Host ""
    Write-Host "=== $title ===" -ForegroundColor Cyan
}

# Required pairs: Korean source -> English target
$requiredPairs = @(
    @{ Ko = "README.md";                             En = "README.en.md" },
    @{ Ko = "GETTING_STARTED.md";                   En = "GETTING_STARTED.en.md" },
    @{ Ko = "CLAUDE.md";                             En = "CLAUDE.en.md" },
    @{ Ko = "GEMINI.md";                             En = "GEMINI.en.md" },
    @{ Ko = "AGENTS.md";                             En = "AGENTS.en.md" },
    @{ Ko = "templates/topic_starter.md";            En = "templates/topic_starter.en.md" },
    @{ Ko = "templates/roadmap_prompt_template.md";  En = "templates/roadmap_prompt_template.en.md" },
    @{ Ko = "templates/daily_learning_prompt.md";    En = "templates/daily_learning_prompt.en.md" },
    @{ Ko = "templates/quick_start_prompt.md";       En = "templates/quick_start_prompt.en.md" },
    @{ Ko = "templates/workflow_guide.md";           En = "templates/workflow_guide.en.md" }
)

# --- Check 1: Pair Check ---
Header "Check 1: Pair Check (every Korean doc has an English pair)"
foreach ($pair in $requiredPairs) {
    $koPath = Join-Path $projectRoot $pair.Ko
    $enPath = Join-Path $projectRoot $pair.En
    $koExists = Test-Path $koPath
    $enExists = Test-Path $enPath
    if (-not $koExists) {
        Fail "Korean source missing: $($pair.Ko)"
    } elseif (-not $enExists) {
        Fail "English pair missing: $($pair.En)"
    } else {
        Pass "$($pair.Ko) <-> $($pair.En)"
    }
}

# --- Check 2: Placeholder Check ---
Header "Check 2: Placeholder Check (variables match between language pairs)"
$placeholderPattern = '\{[A-Z_]+\}'
foreach ($pair in $requiredPairs) {
    $koPath = Join-Path $projectRoot $pair.Ko
    $enPath = Join-Path $projectRoot $pair.En
    if (-not (Test-Path $koPath) -or -not (Test-Path $enPath)) { continue }

    $koContent = Get-Content $koPath -Raw -Encoding UTF8
    $enContent = Get-Content $enPath -Raw -Encoding UTF8

    $koPlaceholders = ([regex]::Matches($koContent, $placeholderPattern) | ForEach-Object { $_.Value } | Sort-Object -Unique)
    $enPlaceholders = ([regex]::Matches($enContent, $placeholderPattern) | ForEach-Object { $_.Value } | Sort-Object -Unique)

    $missing = @($koPlaceholders | Where-Object { $enPlaceholders -notcontains $_ })
    $extra   = @($enPlaceholders | Where-Object { $koPlaceholders -notcontains $_ })

    if ($missing.Count -gt 0 -or $extra.Count -gt 0) {
        Fail "$($pair.En) - missing: $($missing -join ', ') | extra: $($extra -join ', ')"
    } else {
        Pass "$($pair.En) - placeholders match"
    }
}

# --- Check 3: Structure Check ---
Header "Check 3: Structure Check (English files have required headings)"
$headingChecks = @(
    @{ File = "README.en.md";                          Headings = @("Overview", "Goals", "Core Philosophy") },
    @{ File = "GETTING_STARTED.en.md";                 Headings = @("Quick Start", "Step") },
    @{ File = "CLAUDE.en.md";                          Headings = @("Activation Conditions", "VibeLearn AI Workflow", "Core Rules") },
    @{ File = "templates/topic_starter.en.md";         Headings = @("Topic") },
    @{ File = "templates/roadmap_prompt_template.en.md"; Headings = @("Roadmap", "Module") },
    @{ File = "templates/daily_learning_prompt.en.md"; Headings = @("Daily", "Step") },
    @{ File = "templates/quick_start_prompt.en.md";    Headings = @("Quick") },
    @{ File = "templates/workflow_guide.en.md";        Headings = @("Workflow") }
)
foreach ($check in $headingChecks) {
    $filePath = Join-Path $projectRoot $check.File
    if (-not (Test-Path $filePath)) {
        Fail "$($check.File) - file not found"
        continue
    }
    $content = Get-Content $filePath -Raw -Encoding UTF8
    $allFound = $true
    foreach ($heading in $check.Headings) {
        if ($content -notmatch $heading) {
            Fail "$($check.File) - heading not found: '$heading'"
            $allFound = $false
        }
    }
    if ($allFound) {
        Pass "$($check.File) - all required headings found"
    }
}

# --- Check 4: Anti-Fake-Translation Check ---
Header "Check 4: Anti-Fake-Translation Check (English files must not contain mostly Korean)"
foreach ($pair in $requiredPairs) {
    $enPath = Join-Path $projectRoot $pair.En
    if (-not (Test-Path $enPath)) { continue }

    $content = Get-Content $enPath -Raw -Encoding UTF8
    $totalChars = $content.Length
    if ($totalChars -eq 0) {
        Fail "$($pair.En) - file is empty"
        continue
    }

    # Count Hangul syllable characters (U+AC00 to U+D7A3)
    $hangulCount = 0
    foreach ($char in $content.ToCharArray()) {
        $code = [int][char]$char
        if ($code -ge 0xAC00 -and $code -le 0xD7A3) {
            $hangulCount++
        }
    }
    $hangulRatio = $hangulCount / $totalChars
    $ratioPercent = [math]::Round($hangulRatio * 100, 1)

    if ($hangulRatio -gt 0.15) {
        Fail "$($pair.En) - Korean ratio too high: ${ratioPercent}% (threshold: 15%)"
    } else {
        Pass "$($pair.En) - Korean ratio OK: ${ratioPercent}%"
    }
}

# --- Check 5: Encoding Check ---
Header "Check 5: Encoding Check (files must be readable as UTF-8)"
$allFiles = @()
foreach ($pair in $requiredPairs) {
    $allFiles += $pair.Ko
    $allFiles += $pair.En
}
$allFiles = $allFiles | Sort-Object -Unique

foreach ($file in $allFiles) {
    $filePath = Join-Path $projectRoot $file
    if (-not (Test-Path $filePath)) { continue }
    try {
        $utf8 = New-Object System.Text.UTF8Encoding($true)
        $bytes = [System.IO.File]::ReadAllBytes($filePath)
        $null = $utf8.GetString($bytes)
        Pass "$file - UTF-8 OK"
    } catch {
        Fail "$file - encoding error: $_"
    }
}

# --- Summary ---
Write-Host ""
Write-Host "==============================" -ForegroundColor Yellow
Write-Host "SUMMARY: $passCount passed, $failCount failed" -ForegroundColor Yellow
Write-Host "==============================" -ForegroundColor Yellow

if ($failCount -gt 0) {
    Write-Host "Localization validation FAILED. Fix the issues above." -ForegroundColor Red
    exit 1
} else {
    Write-Host "All checks passed. Localization looks good!" -ForegroundColor Green
    exit 0
}
