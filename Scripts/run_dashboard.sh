#!/usr/bin/env bash
echo "Starting RCA Platform Web Dashboard (Unix)"

if [ -f requirements.txt ]; then
  echo "Installing requirements..."
  python3 -m pip install -r requirements.txt
else
  echo "No requirements.txt found. Skipping install."
fi

echo "Launching dashboard..."
python3 src/web_dashboard.py
