#!/usr/bin/env bash
if [ -f requirements.txt ]; then
  echo "Installing Python packages from requirements.txt..."
  python3 -m pip install -r requirements.txt
else
  echo "requirements.txt not found in repository root. Create one listing needed packages (e.g., flask, flask-socketio, kafka-python)."
fi
