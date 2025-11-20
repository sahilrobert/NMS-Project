#!/usr/bin/env pwsh
if (Test-Path .\requirements.txt) {
    Write-Host "Installing Python packages from requirements.txt..."
    python -m pip install -r .\requirements.txt
} else {
    Write-Host "requirements.txt not found in repository root. Create one listing needed packages (e.g., flask, flask-socketio, kafka-python)."
}
