@echo off
REM Double-click this file to set up the project: install Python and all
REM required libraries. After it finishes, open the .ipynb file in VS Code.

cd /d "%~dp0"

where uv >nul 2>nul
if errorlevel 1 (
    if not exist "%USERPROFILE%\.local\bin\uv.exe" (
        echo Installing uv (one-time setup)
        powershell -NoProfile -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    )
    set "PATH=%USERPROFILE%\.local\bin;%PATH%"
)

echo Installing dependencies ...
uv sync
if errorlevel 1 (
    echo.
    echo Setup failed. See the message above.
    pause
    exit /b 1
)

echo.
echo Setup complete. Open the notebook (.ipynb file) in VS Code.
echo When VS Code asks which Python interpreter to use, choose:
echo   %CD%\.venv\Scripts\python.exe
echo.
pause
