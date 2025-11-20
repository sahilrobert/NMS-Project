# Architecture Overview

This project is a small RCA (Root Cause Analysis) demo platform. High-level components:

- `src/web_dashboard.py` — Flask + Socket.IO based dashboard that consumes Kafka `network-alarms` topic and shows alarms, RCA results and device status.
- `src/alarm_generator.py` — (example) generates sample alarms for testing.
- `src/rca_processor.py` — (example) processes alarms to generate RCA results.

Data flow:
1. Alarms are produced (by devices or `alarm_generator`).
2. Kafka topic `network-alarms` holds alarm messages.
3. `web_dashboard.py` consumes Kafka messages and emits Socket.IO events to connected browsers.
4. Users can export CSV/JSON reports from the dashboard UI.
