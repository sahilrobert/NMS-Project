# Usage

Quick steps to run the RCA Platform Web Dashboard locally.

Prerequisites:
- Python 3.8+ installed
- (Optional) Kafka running if you want real-time data

1. Install dependencies:

   Windows (PowerShell):

   ```powershell
   .\scripts\install_requirements.ps1
   ```

   Unix / WSL:

   ```bash
   ./scripts/install_requirements.sh
   ```

2. Start the dashboard (this will also start the built-in Kafka consumer thread which expects Kafka at `localhost:9092`):

   Windows (PowerShell):

   ```powershell
   .\scripts\run_dashboard.ps1
   ```

   Unix / WSL:

   ```bash
   ./scripts/run_dashboard.sh
   ```

3. Open your browser at `http://localhost:5000` to view the dashboard.

Notes:
- If you don't have Kafka, the dashboard will still run but won't receive real-time messages.
- The main dashboard entrypoint is `src/web_dashboard.py`.
