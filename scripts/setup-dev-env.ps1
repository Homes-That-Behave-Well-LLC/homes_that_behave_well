<#
.SYNOPSIS
    Installs the HA 2026.11.0 development/test dependencies in .venv.
.DESCRIPTION
    Requires an existing Python 3.14.2+ interpreter (3.14.x, Windows x64).
    Uses normal pip dependency resolution and requires pip check to pass.
    Never launches Home Assistant or creates a Home Assistant runtime.
.PARAMETER PythonPath
    Full path to the Python interpreter used to create the virtual environment.
.PARAMETER Recreate
    Remove only this repository's .venv and recreate it before installing.
#>
param(
    [Parameter(Mandatory = $true)]
    [string]$PythonPath,
    [switch]$Recreate
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoRoot = Split-Path -Path $PSScriptRoot -Parent
$VenvPath = Join-Path $RepoRoot ".venv"
$VenvPython = Join-Path $VenvPath "Scripts\python.exe"
$RequirementsPath = Join-Path $RepoRoot "requirements-dev.txt"
$BasePython = (Resolve-Path -LiteralPath $PythonPath).Path

function Invoke-CheckedPython {
    param([string]$Executable, [string[]]$PythonArgs)
    & $Executable @PythonArgs
    if ($LASTEXITCODE -ne 0) {
        throw "Python command failed with exit code ${LASTEXITCODE}: $($PythonArgs -join ' ')"
    }
}

$checkInterpreter = @'
import sys, sysconfig
if not ((3, 14, 2) <= sys.version_info[:3] < (3, 15, 0)):
    raise SystemExit('Use Python 3.14.2 or newer in the 3.14 series for HA 2026.11.0.')
if sysconfig.get_platform() != 'win-amd64':
    raise SystemExit('This Windows setup requires an x64 Python interpreter, not ARM64 Python.')
print('Python', sys.version.split()[0], sysconfig.get_platform())
'@
Invoke-CheckedPython -Executable $BasePython -PythonArgs @("-c", $checkInterpreter)

if (Test-Path -LiteralPath $VenvPath) {
    $venvItem = Get-Item -LiteralPath $VenvPath -Force
    if ($venvItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint) {
        throw "Refusing to modify a linked virtual environment: $VenvPath"
    }
    if ($Recreate) {
        Write-Host "Recreating repository-local virtual environment: $VenvPath"
        Remove-Item -LiteralPath $VenvPath -Recurse -Force
    }
}

if (-not (Test-Path -LiteralPath $VenvPath)) {
    Invoke-CheckedPython -Executable $BasePython -PythonArgs @("-m", "venv", $VenvPath)
}
Invoke-CheckedPython -Executable $VenvPython -PythonArgs @("-c", $checkInterpreter)
Invoke-CheckedPython -Executable $VenvPython -PythonArgs @(
    "-m", "pip", "install", "--disable-pip-version-check", "--progress-bar", "off",
    "-r", $RequirementsPath
)
Invoke-CheckedPython -Executable $VenvPython -PythonArgs @("-m", "pip", "check")

$checkPackages = @'
from importlib.metadata import version
for package in ('homeassistant', 'pytest-homeassistant'):
    actual = version(package)
    if actual != '2026.11.0':
        raise SystemExit(f'{package}: expected 2026.11.0, installed {actual}')
    print(f'{package} {actual}')
'@
Invoke-CheckedPython -Executable $VenvPython -PythonArgs @("-c", $checkPackages)
Write-Host "Dependencies validated. Run the integration tests, Ruff, and mypy before deployment."
