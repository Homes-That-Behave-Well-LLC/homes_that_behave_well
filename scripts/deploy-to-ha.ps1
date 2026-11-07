<#
.SYNOPSIS
    Deploys the HTBW Core custom integration to a Home Assistant
    installation's custom_components directory.

.DESCRIPTION
    Requires a clean, published, exact commit and fixed repository/HA-DEV paths.
    Run the complete validation suite and fetch origin before invoking this script.
    Mirrors only the integration, then verifies runtime file inventory and SHA256
    hashes. Existing runtime bytecode caches are excluded, not copied or removed.
    Never starts, stops, reloads, or configures Home Assistant.

.PARAMETER Commit
    Full commit hash that passed validation and was pushed to origin/main.

.PARAMETER DryRun
    Show what robocopy would do (via robocopy's own /L list-only mode)
    without copying, deleting, or creating anything.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [ValidatePattern('^[0-9a-f]{40}$')]
    [string]$Commit,
    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = [System.IO.Path]::GetFullPath((Split-Path -Path $PSScriptRoot -Parent))
if ($RepoRoot -ne "C:\HomesPlatformRepos\homes_that_behave_well") {
    throw "Deployment is authorized only from the fixed local repository."
}
$Source = Join-Path $RepoRoot "custom_components\htbw"
$Destination = "H:\custom_components\htbw"

function Invoke-CheckedGit {
    param([string[]]$GitArgs)
    $result = & git -C $RepoRoot @GitArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Git verification failed: $($GitArgs -join ' ')"
    }
    return $result
}

function Assert-ExactCommit {
    if ((Invoke-CheckedGit -GitArgs @("rev-parse", "HEAD")) -ne $Commit) {
        throw "HEAD does not match the requested tested commit."
    }
    if ((Invoke-CheckedGit -GitArgs @("rev-parse", "origin/main")) -ne $Commit) {
        throw "origin/main does not match the requested tested commit. Push and fetch first."
    }
    if (@(Invoke-CheckedGit -GitArgs @("status", "--porcelain", "--untracked-files=all")).Count) {
        throw "Refusing deployment from a dirty working tree."
    }
}

function Assert-NotLinked {
    param([string]$Path)
    if ((Test-Path -LiteralPath $Path) -and
        ((Get-Item -LiteralPath $Path -Force).Attributes -band
            [System.IO.FileAttributes]::ReparsePoint)) {
        throw "Refusing a linked deployment path: $Path"
    }
}

function Get-RuntimeFiles {
    param([string]$Root)
    return @(Get-ChildItem -LiteralPath $Root -File -Recurse -Force |
        Where-Object {
            $_.FullName -notmatch '[\\/]__pycache__[\\/]' -and $_.Extension -ne ".pyc"
        } |
        ForEach-Object { $_.FullName.Substring($Root.Length + 1) } |
        Sort-Object)
}

Assert-ExactCommit
$haDrive = Get-PSDrive -Name H -PSProvider FileSystem
$shareRoot = [string]$haDrive.DisplayRoot
if ($shareRoot.TrimEnd('\') -ne "\\10.1.2.156\config") {
    throw "H: is not mapped to the authorized HA-DEV configuration share."
}

if (-not (Test-Path -LiteralPath $Source -PathType Container)) {
    throw "Source path not found: $Source"
}

$destinationParent = Split-Path -Path $Destination -Parent
if (-not (Test-Path -LiteralPath $destinationParent -PathType Container)) {
    throw "Destination parent not found: $destinationParent"
}

foreach ($path in @(
    $RepoRoot, (Join-Path $RepoRoot "custom_components"), $Source,
    "H:\", $destinationParent, $Destination
)) {
    Assert-NotLinked -Path $path
}
foreach ($root in @($Source, $Destination)) {
    if (Test-Path -LiteralPath $root) {
        foreach ($item in Get-ChildItem -LiteralPath $root -Recurse -Force) {
            Assert-NotLinked -Path $item.FullName
        }
    }
}

$trackedPaths = @(Invoke-CheckedGit -GitArgs @(
    "ls-tree", "-r", "--name-only", $Commit, "--", "custom_components/htbw"
))
$expectedFiles = @($trackedPaths |
    ForEach-Object { $_.Substring("custom_components/htbw/".Length).Replace('/', '\') } |
    Sort-Object)
if ($expectedFiles.Count -eq 0 -or
    @(Compare-Object $expectedFiles (Get-RuntimeFiles -Root $Source)).Count) {
    throw "Source inventory differs from the exact committed runtime inventory."
}
if ((Get-Content -Raw -LiteralPath (Join-Path $Source "manifest.json") |
    ConvertFrom-Json).domain -ne "htbw") {
    throw "Source manifest is not the HTBW integration."
}
$sourceHashes = @{}
foreach ($file in $expectedFiles) {
    $gitPath = "custom_components/htbw/" + $file.Replace('\', '/')
    $blob = Invoke-CheckedGit -GitArgs @("rev-parse", "${Commit}:$gitPath")
    $worktreeBlob = Invoke-CheckedGit -GitArgs @(
        "hash-object", "--path=$gitPath", (Join-Path $Source $file)
    )
    if ($worktreeBlob -ne $blob) {
        throw "Source content differs from the requested commit: $file"
    }
    $sourceHashes[$file] = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $Source $file)).Hash
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
    "/NP"
    "/XJ"
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
Write-Host "Tested commit: $Commit"
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

if ($DryRun) {
    Write-Host "Dry run completed with robocopy exit code $exitCode. No files deployed."
    exit 0
}

Assert-ExactCommit
if (@(Compare-Object $expectedFiles (Get-RuntimeFiles -Root $Destination)).Count) {
    throw "Deployed runtime inventory does not match the committed source inventory."
}
foreach ($file in $expectedFiles) {
    $sourceHash = (Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $Source $file)).Hash
    $destinationHash = (
        Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $Destination $file)
    ).Hash
    if ($sourceHash -ne $sourceHashes[$file] -or $destinationHash -ne $sourceHashes[$file]) {
        throw "Source changed during deployment or deployed file hash differs: $file"
    }
}
Write-Host "Verified $($expectedFiles.Count) runtime files for commit $Commit at $([DateTime]::UtcNow.ToString('o'))."
Write-Host "Robocopy exit code: $exitCode. Runtime acceptance remains pending; Home Assistant was not restarted."
exit 0
