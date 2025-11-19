# Autonomous Network Management System (NMS)

## Overview

An intelligent, self-healing network management system that automatically:
- **Injects** random failures for chaos engineering
- **Detects** anomalies using real-time monitoring
- **Correlates** events to identify patterns
- **Analyzes** root causes using AI-driven logic
- **Remediates** issues automatically in seconds
- **Stabilizes** the network continuously

## Features

### 🔄 Autonomous Loop
The system runs continuously in a cycle:
```
Inject → Detect → Analyze → Remediate → Stabilize → Repeat
```

### 🎯 Key Capabilities
- **Auto-Failure Injection**: Randomly injects failures (high CPU, memory leaks, network issues, node failures)
- **Anomaly Detection**: Real-time monitoring with threshold-based detection
- **Event Correlation**: Identifies patterns and cascading failures
- **Root Cause Analysis**: AI-driven analysis to identify the source of issues
- **Auto-Remediation**: Automatic fixes applied in seconds
- **Network Stabilization**: Continuous optimization of network health

### 🎨 Dark Glass UI
Real-time dashboard featuring:
- Network topology visualization
- Live metrics and statistics
- System logs with color coding
- Incident tracking and statistics
- Dark glassmorphism design

### 📊 Monitoring & Metrics
- CPU usage
- Memory consumption
- Network latency
- Packet loss
- Node health status
- Incident statistics
- Auto-resolution rates

## Installation

### Prerequisites
- Python 3.8 or higher

### Setup

1. Clone the repository:
```bash
git clone https://github.com/sahilrobert/NMS-Project.git
cd NMS-Project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

```bash
# Run a quick demo
python cli.py demo

# Run tests
python cli.py test

# Start web server
python cli.py server

# Run in CLI mode (continuous cycles)
python cli.py run
```

### Start the NMS Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### Access the Dashboard

Open your web browser and navigate to:
```
http://localhost:5000
```

### Using the Dashboard

1. **Start the System**: Click the "Start" button to begin the autonomous cycle
2. **Monitor**: Watch real-time updates of network topology, metrics, and logs
3. **Observe**: See the system automatically detect and fix issues
4. **Stop**: Click "Stop" to pause the autonomous operations

## Architecture

### Core Components

#### 1. Failure Injector
- Randomly injects failures into network nodes
- Supports: high CPU, high memory, high latency, packet loss, node failures

#### 2. Anomaly Detector
- Real-time monitoring of all network nodes
- Threshold-based detection
- Multi-metric analysis

#### 3. Event Correlator
- Maintains a sliding window of events
- Identifies patterns and relationships
- Detects cascading failures

#### 4. Root Cause Analyzer
- Analyzes anomalies and correlations
- Provides confidence scores
- Suggests remediation strategies

#### 5. Auto-Remediator
- Executes automatic fixes
- Restarts processes, clears caches, optimizes routing
- Reboots nodes when necessary

#### 6. Network Stabilizer
- Continuously optimizes network metrics
- Gradual performance improvements
- Health percentage tracking

#### 7. Incident Tracker
- Logs all incidents
- Tracks resolution times
- Calculates auto-resolution rates

### Network Topology

The system manages a simulated network with:
- 3 Core Routers
- 5 Edge Switches
- 8 Servers
- Dynamic connections between nodes

## API Endpoints

### REST API

- `GET /api/status` - Get system status
- `GET /api/start` - Start the autonomous loop
- `GET /api/stop` - Stop the autonomous loop
- `GET /api/topology` - Get network topology
- `GET /api/metrics` - Get current metrics
- `GET /api/logs` - Get system logs
- `GET /api/incidents` - Get incident statistics

### WebSocket Events

- `metrics_update` - Real-time metrics updates
- `topology_update` - Network topology changes
- `logs_update` - New log entries
- `incidents_update` - Incident statistics
- `cycle_update` - Cycle completion updates

## Configuration

The system operates with these default thresholds:
- CPU usage: 80%
- Memory usage: 80%
- Latency: 50ms
- Packet loss: 5%

Cycle interval: 3 seconds

## Testing

Run basic tests:
```bash
python test_nms.py
```

## Examples

### Typical Cycle Output

```
Cycle 1: Injected high_cpu on server-3
Detected 1 anomalies
Found 0 correlated patterns
Identified 1 root causes
Applied 1 remediation actions
Network stability: 93.75%
```

## Performance

- **Detection Time**: < 1 second
- **Analysis Time**: < 0.5 seconds
- **Remediation Time**: < 2 seconds
- **Total Response Time**: < 4 seconds
- **Cycle Time**: 3 seconds

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Sahil Robert

## Acknowledgments

Built with:
- Flask & Flask-SocketIO for real-time communication
- NetworkX for topology management
- Scikit-learn for anomaly detection
- Chart.js for visualizations