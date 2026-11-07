<#
.SYNOPSIS
    Creates/updates the repository-local Python development and
    automated-test environment for HTBW Core custom-integration work
    (Issue #201).

.DESCRIPTION
    On a platform PyPI already publishes wheels for (Linux, macOS, Windows
    x86_64), this is exactly: create .venv, then
    `pip install -r requirements-dev.txt` (pytest-homeassistant-custom-
    component, ruff, mypy) -- the same, ordinary approach the sibling
    concierge/voice_identity/asset_intelligence repositories already use.

    This development machine is Windows on ARM64. PyPI has no win_arm64
    wheel for several of pytest-homeassistant-custom-component's own
    exact-pinned transitive dependencies (aiohttp==3.11.11,
    cryptography==50.0.2, plus ciso8601 and lru-dict at any version), and
    no C/C++/Rust toolchain is installed here to build them from source.
    Where that is detected, a documented, minimal compatibility layer is
    applied so the same test suite still runs. This is a development/test
    -environment concern only:

    - It does not change this integration's own requirements (manifest.json
      declares none).
    - It does not change what H:, the actual Home Assistant deployment
      target, needs.
    - A contributor on a wheel-covered platform never reaches the ARM64
      branch below.

    See scripts/dev-env-arm64-deps.txt and scripts/dev-env-arm64-shims/ for
    the exact, version-controlled substitutions this applies.

.PARAMETER Recreate
    Delete and recreate .venv from scratch before installing.
#>
param(
    [switch]$Recreate
)

Set-StrictMode -Version Latest

$RepoRoot = Split-Path -Path $PSScriptRoot -Parent
$VenvPath = Join-Path $RepoRoot ".venv"
$Python = Join-Path $VenvPath "Scripts\python.exe"
$RequirementsPath = Join-Path $RepoRoot "requirements-dev.txt"

function Invoke-Pip {
    # Runs `python -m pip <args>`, merging stderr into stdout as plain text
    # (pip routinely prints advisory warnings to stderr; PowerShell would
    # otherwise surface those as terminating errors under a strict
    # $ErrorActionPreference) and throws only on a genuine non-zero pip
    # exit code.
    param([Parameter(ValueFromRemainingArguments = $true)][string[]]$PipArgs)
    & $Python -m pip @PipArgs 2>&1 | ForEach-Object { Write-Host $_ }
    if ($LASTEXITCODE -ne 0) {
        throw "pip $($PipArgs -join ' ') failed with exit code $LASTEXITCODE"
    }
}

if ($Recreate -and (Test-Path $VenvPath)) {
    Write-Host "Removing existing virtual environment: $VenvPath"
    Remove-Item -Recurse -Force $VenvPath
}

if (-not (Test-Path $VenvPath)) {
    Write-Host "Creating virtual environment: $VenvPath"
    python -m venv $VenvPath
}

Write-Host "Upgrading pip"
Invoke-Pip install --upgrade pip --quiet

$isArm64Windows = $env:PROCESSOR_ARCHITECTURE -eq "ARM64"

if (-not $isArm64Windows) {
    Write-Host "Installing requirements-dev.txt"
    Invoke-Pip install -r $RequirementsPath
    Write-Host "Development environment ready: $VenvPath"
    exit 0
}

Write-Host "ARM64 Windows detected: applying the documented platform compatibility layer"
Write-Host "  (see this script's own header comment, and scripts/dev-env-arm64-deps.txt)"

Write-Host "  [1/6] homeassistant==2025.1.4 --no-deps"
Invoke-Pip install "homeassistant==2025.1.4" --no-deps

Write-Host "  [2/6] pytest-homeassistant-custom-component==0.13.205 --no-deps"
Invoke-Pip install "pytest-homeassistant-custom-component==0.13.205" --no-deps

Write-Host "  [3/6] acme --no-deps (its own metadata requires cryptography>=47, which lacks a wheel;"
Write-Host "        acme is needed only so hass_nabucasa.remote imports, and is never exercised by these tests)"
Invoke-Pip install acme --no-deps

Write-Host "  [4/6] hass_nabucasa --no-deps (required transitively by homeassistant.config_entries;"
Write-Host "        its real further dependencies are satisfied explicitly below instead of through its own metadata)"
Invoke-Pip install hass_nabucasa --no-deps

Write-Host "  [5/6] the bluetooth stack pytest-homeassistant-custom-component's own 'hass' fixture mocks"
Write-Host "        unconditionally for every test, --no-deps (its own metadata chain also reaches cryptography>=47)"
$bluetoothPackages = @(
    "bluetooth_auto_recovery", "bluetooth-adapters", "bluetooth-data-tools", "habluetooth",
    "bleak", "bleak-retry-connector", "aiooui", "PyRIC", "btsocket", "uart-devices",
    "usb-devices", "winrt-Windows.Devices.Bluetooth", "winrt-Windows.Devices.Bluetooth.Advertisement",
    "winrt-Windows.Devices.Bluetooth.GenericAttributeProfile", "winrt-Windows.Devices.Enumeration",
    "winrt-Windows.Devices.Radios", "winrt-Windows.Foundation", "winrt-Windows.Foundation.Collections",
    "winrt-Windows.Storage.Streams", "winrt-runtime"
)
Invoke-Pip install @bluetoothPackages --no-deps

Write-Host "  [6/6] every remaining real dependency, resolved together normally"
$armDepsPath = Join-Path $PSScriptRoot "dev-env-arm64-deps.txt"
Invoke-Pip install -r $armDepsPath

Write-Host "  Installing the two dependencies with no win_arm64 wheel at any version (committed pure-Python stand-ins)"
$sitePackages = (& $Python -c "import sysconfig; print(sysconfig.get_path('purelib'))").Trim()
$shimsDir = Join-Path $PSScriptRoot "dev-env-arm64-shims"
Copy-Item (Join-Path $shimsDir "ciso8601.py") (Join-Path $sitePackages "ciso8601.py") -Force
Copy-Item (Join-Path $shimsDir "lru.py") (Join-Path $sitePackages "lru.py") -Force

Write-Host "  Verifying imports"
& $Python -c "import homeassistant.core, homeassistant.config_entries, homeassistant.helpers.area_registry, homeassistant.helpers.entity_registry, homeassistant.helpers.device_registry, homeassistant.helpers.issue_registry, homeassistant.helpers.selector, pytest_homeassistant_custom_component; from pytest_homeassistant_custom_component import patch_time; print('HTBW dev environment import check: OK')"
if ($LASTEXITCODE -ne 0) {
    throw "Import verification failed"
}

Write-Host "Development environment ready: $VenvPath (ARM64 Windows compatibility layer applied)"
