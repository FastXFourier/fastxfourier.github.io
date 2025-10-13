# Serve the MkDocs site reliably from the project venv
# Usage: Open PowerShell in the repo root and run: .\serve.ps1

$ProjectRoot = (Get-Location).Path
Write-Host "Project root: $ProjectRoot"

# Ensure venv python exists
$VenvPython = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
if (-Not (Test-Path $VenvPython)) {
    Write-Error "Could not find venv python at $VenvPython. Activate your venv or create one."; exit 1
}

# Add project root to PYTHONPATH for this session
$env:PYTHONPATH = $ProjectRoot
Write-Host "Set PYTHONPATH to $env:PYTHONPATH"

# Run mkdocs using the venv python
& $VenvPython -m mkdocs serve
