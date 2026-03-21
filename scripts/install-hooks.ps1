# install-hooks.ps1
# Installs the git pre-commit hook for CatchUpAI_VL.
# Run this once after cloning or when the hook needs to be updated.
#
# Usage: powershell -ExecutionPolicy Bypass -File scripts/install-hooks.ps1

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectRoot = Split-Path -Parent $scriptDir
$hooksDir = Join-Path $projectRoot ".git\hooks"
$sourceHook = Join-Path $scriptDir "pre-commit"
$targetHook = Join-Path $hooksDir "pre-commit"

# Validate
if (-not (Test-Path $hooksDir)) {
    Write-Error "Not a git repository or .git/hooks not found at: $hooksDir"
    exit 1
}

if (-not (Test-Path $sourceHook)) {
    Write-Error "Source hook not found at: $sourceHook"
    exit 1
}

# Install
Copy-Item $sourceHook $targetHook -Force
Write-Host "[OK] Pre-commit hook installed: $targetHook"
Write-Host ""
Write-Host "Next steps to enable auto-translation:"
Write-Host ""
Write-Host "  1. Install Python dependency:"
Write-Host "       pip install anthropic"
Write-Host ""
Write-Host "  2. Set your Anthropic API key (current session):"
Write-Host '       $env:ANTHROPIC_API_KEY = "sk-ant-..."'
Write-Host ""
Write-Host "  3. To set permanently (User environment variable):"
Write-Host '       [System.Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "sk-ant-...", "User")'
Write-Host ""
Write-Host "  NOTE: Without ANTHROPIC_API_KEY, the hook will still:"
Write-Host "    - Sync CLAUDE.md -> GEMINI.md, AGENTS.md (KR+EN)"
Write-Host "    - Run validate-localization checks"
Write-Host "    - Warn you to manually update CLAUDE.en.md"
