# Serve the MkDocs site reliably from the project venv
# Usage: Open PowerShell in the repo root and run: .\serve.ps1

$ProjectRoot = (Get-Location).Path
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-Not (Test-Path $VenvPython)) { Write-Error "Venv python not found at $VenvPython"; exit 1 }

$env:PYTHONPATH = $ProjectRoot
Write-Host "Starting mkdocs with python: $VenvPython"
& $VenvPython -m mkdocs serve --dev-addr 127.0.0.1:8000
