"""
Flask web server for Autonomous NMS
Provides REST API and real-time WebSocket updates
"""
from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
import threading
import time
from nms_core import AutonomousNMS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nms-secret-key-2024'
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')

# Global NMS instance
nms = AutonomousNMS()
nms_thread = None

def background_nms_loop():
    """Background thread that runs the NMS cycle continuously"""
    while nms.running:
        try:
            # Run one cycle
            cycle_data = nms.run_cycle()
            
            # Emit updates to all connected clients
            socketio.emit('cycle_update', cycle_data)
            socketio.emit('metrics_update', nms.get_metrics())
            socketio.emit('logs_update', nms.get_logs())
            socketio.emit('incidents_update', nms.get_incidents())
            
            # Wait before next cycle (3 seconds)
            time.sleep(3)
        except Exception as e:
            print(f"Error in NMS cycle: {e}")
            time.sleep(1)

@app.route('/')
def index():
    """Serve main dashboard"""
    return render_template('dashboard_simple.html')

@app.route('/api/start')
def start_nms():
    """Start the autonomous NMS"""
    global nms_thread
    
    if not nms.running:
        nms.running = True
        nms_thread = threading.Thread(target=background_nms_loop, daemon=True)
        nms_thread.start()
        return jsonify({"status": "started", "message": "Autonomous NMS started"})
    return jsonify({"status": "already_running", "message": "NMS is already running"})

@app.route('/api/stop')
def stop_nms():
    """Stop the autonomous NMS"""
    nms.running = False
    return jsonify({"status": "stopped", "message": "Autonomous NMS stopped"})

@app.route('/api/status')
def get_status():
    """Get NMS status"""
    return jsonify({
        "running": nms.running,
        "cycle_count": nms.cycle_count
    })

@app.route('/api/topology')
def get_topology():
    """Get network topology"""
    return jsonify(nms.get_topology())

@app.route('/api/metrics')
def get_metrics():
    """Get current metrics"""
    return jsonify(nms.get_metrics())

@app.route('/api/logs')
def get_logs():
    """Get logs"""
    return jsonify({"logs": nms.get_logs()})

@app.route('/api/incidents')
def get_incidents():
    """Get incident statistics"""
    return jsonify(nms.get_incidents())

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    print('Client connected')
    # Send initial data
    emit('topology_update', nms.get_topology())
    emit('metrics_update', nms.get_metrics())
    emit('logs_update', nms.get_logs())
    emit('incidents_update', nms.get_incidents())

@socketio.on('disconnect')
def handle_disconnect():
    """Handle client disconnection"""
    print('Client disconnected')

@socketio.on('request_data')
def handle_data_request(data):
    """Handle data request from client"""
    data_type = data.get('type')
    if data_type == 'topology':
        emit('topology_update', nms.get_topology())
    elif data_type == 'metrics':
        emit('metrics_update', nms.get_metrics())
    elif data_type == 'logs':
        emit('logs_update', nms.get_logs())
    elif data_type == 'incidents':
        emit('incidents_update', nms.get_incidents())

if __name__ == '__main__':
    print("Starting Autonomous NMS Server...")
    print("Access the dashboard at: http://localhost:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)
