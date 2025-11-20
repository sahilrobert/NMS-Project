#!/usr/bin/env pwsh
Write-Host "Starting RCA Platform Web Dashboard (Windows PowerShell)"

# Ensure dependencies are installed
if (Test-Path .\requirements.txt) {
    Write-Host "Installing requirements..."
    python -m pip install -r .\requirements.txt
} else {
    Write-Host "No requirements.txt found. Skipping install."
}

Write-Host "Launching dashboard..."
python .\src\web_dashboard.py
