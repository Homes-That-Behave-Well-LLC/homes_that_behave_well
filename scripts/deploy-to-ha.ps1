<#
.SYNOPSIS
    Deploys the HTBW Core custom integration to a Home Assistant
    installation's custom_components directory.

.DESCRIPTION
    Mirrors custom_components/htbw from this repository to
    H:\custom_components\htbw using robocopy /MIR, so the destination ends
    up byte-for-byte matching the source (including removing files at the
    destination that no longer exist at the source).

    This script only copies files. It never starts, stops, restarts,
    configures, or otherwise touches a running Home Assistant instance. H:
    is expected to already be an existing, separately-managed Home
    Assistant deployment; this script does not create or initialize one.

.PARAMETER Source
    The integration folder to copy from. Defaults to this repository's own
    custom_components/htbw.

.PARAMETER Destination
    The target custom_components/htbw folder on the Home Assistant host.
    Defaults to H:\custom_components\htbw.

.PARAMETER DryRun
    Show what robocopy would do (via robocopy's own /L list-only mode)
    without copying, deleting, or creating anything.
#>
param(
    [string]$Source = "C:\HomesPlatformRepos\homes_that_behave_well\custom_components\htbw",
    [string]$Destination = "H:\custom_components\htbw",
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
    throw "Source path not found: $Source"
}

$destinationParent = Split-Path -Path $Destination -Parent
if (-not (Test-Path -LiteralPath $destinationParent -PathType Container)) {
    throw "Destination parent not found: $destinationParent"
}

if (-not $DryRun -and -not (Test-Path -LiteralPath $Destination -PathType Container)) {
    New-Item -ItemType Directory -Path $Destination | Out-Null
}

$robocopyArgs = @(
    $Source
    $Destination
    "/MIR"
    "/R:2"
    "/W:1"
    "/NFL"
    "/NDL"
    "/NP"
    "/XD"
    ".git"
    ".github"
    ".venv"
    "__pycache__"
    ".pytest_cache"
    ".mypy_cache"
    ".ruff_cache"
    "tests"
    "docs"
    "/XF"
    "*.pyc"
    "Thumbs.db"
)

if ($DryRun) {
    $robocopyArgs += "/L"
}

Write-Host "Deploying HTBW Core (domain: htbw)"
Write-Host "Source: $Source"
Write-Host "Destination: $Destination"
if ($DryRun) {
    Write-Host "Mode: DRY RUN (no files will be copied, deleted, or created)"
}

& robocopy @robocopyArgs
$exitCode = $LASTEXITCODE

# robocopy exit codes 0-7 all indicate success (combinations of "files
# copied", "extra files present", "mismatched files", etc.); 8 or higher
# indicates at least one failure.
if ($exitCode -ge 8) {
    throw "Robocopy failed with exit code $exitCode"
}

Write-Host "Deployment completed with robocopy exit code $exitCode"
