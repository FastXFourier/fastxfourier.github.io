@echo off
REM Serve the MkDocs site using the repo venv python
SET PROJECT_ROOT=%~dp0
SET VENV_PY=%PROJECT_ROOT%\.venv\Scripts\python.exe
IF NOT EXIST "%VENV_PY%" (
  echo Venv python not found at %VENV_PY%
  exit /b 1
)
set PYTHONPATH=%PROJECT_ROOT%
"%VENV_PY%" -m mkdocs serve --dev-addr 127.0.0.1:8000
