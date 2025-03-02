@echo off
setlocal EnableDelayedExpansion

REM Check if Chocolatey is installed
where choco >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo Chocolatey is not installed. Installing Chocolatey...
    powershell -NoProfile -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
    REM Refresh PATH after Chocolatey install
    for /f "tokens=2 delims==" %%i in ('wmic os get Path /value ^| find "="') do set "OS_PATH=%%i"
    set "PATH=%OS_PATH%;%ProgramData%\chocolatey\bin"
)

REM Check if Python is installed (either python or py)
where python >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PYTHON_CMD=python"
    goto :PYTHON_FOUND
)

where py >nul 2>nul
if %ERRORLEVEL% equ 0 (
    set "PYTHON_CMD=py"
    goto :PYTHON_FOUND
)

echo Python is not installed. Please install Python and try again.
exit /b 1

:PYTHON_FOUND
REM Find the repository root using Git
for /f "delims=" %%i in ('git rev-parse --show-toplevel 2^>nul') do set "REPO_ROOT=%%i"
if not defined REPO_ROOT (
    echo This script must be run from within the repository.
    exit /b 1
)

REM Navigate to the repository root
cd /d "%REPO_ROOT%" || (
    echo Failed to change directory.
    exit /b 1
)

REM Navigate to the src directory and run cli.py
cd /d "%REPO_ROOT%\src" && %PYTHON_CMD% cli.py

endlocal
