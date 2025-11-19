"""
Autonomous Network Management System (NMS)
Auto-injects failures, detects anomalies, correlates events, 
identifies root cause, and auto-fixes in seconds.
"""
import random
import time
import threading
from datetime import datetime
from collections import deque
from typing import Dict, List, Any
import json

class NetworkNode:
    """Represents a network node"""
    def __init__(self, node_id: str, node_type: str):
        self.id = node_id
        self.type = node_type
        self.status = "healthy"
        self.cpu_usage = random.uniform(10, 30)
        self.memory_usage = random.uniform(20, 40)
        self.latency = random.uniform(1, 10)
        self.packet_loss = 0.0
        self.connections = []
        
    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "status": self.status,
            "cpu_usage": round(self.cpu_usage, 2),
            "memory_usage": round(self.memory_usage, 2),
            "latency": round(self.latency, 2),
            "packet_loss": round(self.packet_loss, 2),
            "connections": self.connections
        }

class FailureInjector:
    """Auto-injects random failures into the network"""
    def __init__(self, network_nodes: List[NetworkNode]):
        self.nodes = network_nodes
        self.failure_types = [
            "high_cpu",
            "high_memory", 
            "high_latency",
            "packet_loss",
            "node_down"
        ]
        
    def inject_random_failure(self) -> Dict[str, Any]:
        """Inject a random failure into a random node"""
        if not self.nodes:
            return None
            
        node = random.choice(self.nodes)
        failure_type = random.choice(self.failure_types)
        
        timestamp = datetime.now().isoformat()
        
        if failure_type == "high_cpu":
            node.cpu_usage = random.uniform(85, 99)
            node.status = "degraded"
        elif failure_type == "high_memory":
            node.memory_usage = random.uniform(85, 99)
            node.status = "degraded"
        elif failure_type == "high_latency":
            node.latency = random.uniform(100, 500)
            node.status = "degraded"
        elif failure_type == "packet_loss":
            node.packet_loss = random.uniform(10, 50)
            node.status = "degraded"
        elif failure_type == "node_down":
            node.status = "down"
            node.cpu_usage = 0
            
        return {
            "timestamp": timestamp,
            "node_id": node.id,
            "failure_type": failure_type,
            "severity": "critical" if failure_type == "node_down" else "warning"
        }

class AnomalyDetector:
    """Detects anomalies in network metrics"""
    def __init__(self):
        self.thresholds = {
            "cpu_usage": 80,
            "memory_usage": 80,
            "latency": 50,
            "packet_loss": 5
        }
        
    def detect(self, nodes: List[NetworkNode]) -> List[Dict[str, Any]]:
        """Detect anomalies in network nodes"""
        anomalies = []
        timestamp = datetime.now().isoformat()
        
        for node in nodes:
            if node.cpu_usage > self.thresholds["cpu_usage"]:
                anomalies.append({
                    "timestamp": timestamp,
                    "node_id": node.id,
                    "metric": "cpu_usage",
                    "value": node.cpu_usage,
                    "threshold": self.thresholds["cpu_usage"],
                    "severity": "warning"
                })
            if node.memory_usage > self.thresholds["memory_usage"]:
                anomalies.append({
                    "timestamp": timestamp,
                    "node_id": node.id,
                    "metric": "memory_usage",
                    "value": node.memory_usage,
                    "threshold": self.thresholds["memory_usage"],
                    "severity": "warning"
                })
            if node.latency > self.thresholds["latency"]:
                anomalies.append({
                    "timestamp": timestamp,
                    "node_id": node.id,
                    "metric": "latency",
                    "value": node.latency,
                    "threshold": self.thresholds["latency"],
                    "severity": "warning"
                })
            if node.packet_loss > self.thresholds["packet_loss"]:
                anomalies.append({
                    "timestamp": timestamp,
                    "node_id": node.id,
                    "metric": "packet_loss",
                    "value": node.packet_loss,
                    "threshold": self.thresholds["packet_loss"],
                    "severity": "critical"
                })
            if node.status == "down":
                anomalies.append({
                    "timestamp": timestamp,
                    "node_id": node.id,
                    "metric": "status",
                    "value": "down",
                    "threshold": "healthy",
                    "severity": "critical"
                })
                
        return anomalies

class EventCorrelator:
    """Correlates events to identify patterns"""
    def __init__(self):
        self.event_window = deque(maxlen=100)
        
    def add_event(self, event: Dict[str, Any]):
        """Add event to correlation window"""
        self.event_window.append(event)
        
    def correlate(self) -> List[Dict[str, Any]]:
        """Correlate events to find patterns"""
        correlations = []
        
        # Group events by node
        node_events = {}
        for event in self.event_window:
            node_id = event.get("node_id")
            if node_id:
                if node_id not in node_events:
                    node_events[node_id] = []
                node_events[node_id].append(event)
        
        # Find nodes with multiple issues
        for node_id, events in node_events.items():
            if len(events) >= 2:
                correlations.append({
                    "timestamp": datetime.now().isoformat(),
                    "node_id": node_id,
                    "event_count": len(events),
                    "event_types": [e.get("metric", e.get("failure_type")) for e in events],
                    "pattern": "multiple_issues"
                })
                
        return correlations

class RootCauseAnalyzer:
    """Identifies root cause of issues"""
    def __init__(self):
        self.analysis_rules = {
            "high_cpu": "Process overload or resource leak",
            "high_memory": "Memory leak or cache overflow",
            "high_latency": "Network congestion or routing issue",
            "packet_loss": "Network hardware failure or congestion",
            "node_down": "Critical system failure or power loss",
            "multiple_issues": "Cascading failure or infrastructure problem"
        }
        
    def analyze(self, anomalies: List[Dict[str, Any]], correlations: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyze root cause"""
        root_causes = []
        
        # Check correlations first (higher priority)
        for corr in correlations:
            if corr["pattern"] == "multiple_issues":
                root_causes.append({
                    "timestamp": datetime.now().isoformat(),
                    "node_id": corr["node_id"],
                    "root_cause": self.analysis_rules["multiple_issues"],
                    "affected_metrics": corr["event_types"],
                    "confidence": 0.85
                })
        
        # Analyze individual anomalies
        for anomaly in anomalies:
            metric = anomaly.get("metric")
            if metric in self.analysis_rules:
                root_causes.append({
                    "timestamp": datetime.now().isoformat(),
                    "node_id": anomaly["node_id"],
                    "root_cause": self.analysis_rules[metric],
                    "affected_metrics": [metric],
                    "confidence": 0.70
                })
                
        return root_causes

class AutoRemediator:
    """Auto-fixes detected issues"""
    def __init__(self, nodes: List[NetworkNode]):
        self.nodes = nodes
        self.remediation_actions = {
            "high_cpu": self.fix_high_cpu,
            "high_memory": self.fix_high_memory,
            "high_latency": self.fix_high_latency,
            "packet_loss": self.fix_packet_loss,
            "node_down": self.fix_node_down
        }
        
    def remediate(self, root_causes: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Apply remediation actions"""
        actions = []
        
        for cause in root_causes:
            node_id = cause["node_id"]
            node = next((n for n in self.nodes if n.id == node_id), None)
            
            if not node:
                continue
                
            for metric in cause["affected_metrics"]:
                if metric in self.remediation_actions:
                    action = self.remediation_actions[metric](node)
                    if action:
                        actions.append(action)
                        
        return actions
    
    def fix_high_cpu(self, node: NetworkNode) -> Dict[str, Any]:
        """Fix high CPU usage"""
        node.cpu_usage = random.uniform(20, 40)
        node.status = "healthy" if node.status == "degraded" else node.status
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": node.id,
            "action": "restart_processes",
            "result": "success",
            "message": "CPU usage normalized"
        }
    
    def fix_high_memory(self, node: NetworkNode) -> Dict[str, Any]:
        """Fix high memory usage"""
        node.memory_usage = random.uniform(30, 50)
        node.status = "healthy" if node.status == "degraded" else node.status
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": node.id,
            "action": "clear_cache",
            "result": "success",
            "message": "Memory usage normalized"
        }
    
    def fix_high_latency(self, node: NetworkNode) -> Dict[str, Any]:
        """Fix high latency"""
        node.latency = random.uniform(5, 15)
        node.status = "healthy" if node.status == "degraded" else node.status
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": node.id,
            "action": "optimize_routing",
            "result": "success",
            "message": "Latency normalized"
        }
    
    def fix_packet_loss(self, node: NetworkNode) -> Dict[str, Any]:
        """Fix packet loss"""
        node.packet_loss = random.uniform(0, 2)
        node.status = "healthy" if node.status == "degraded" else node.status
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": node.id,
            "action": "reset_interface",
            "result": "success",
            "message": "Packet loss resolved"
        }
    
    def fix_node_down(self, node: NetworkNode) -> Dict[str, Any]:
        """Fix down node"""
        node.status = "healthy"
        node.cpu_usage = random.uniform(20, 40)
        node.memory_usage = random.uniform(30, 50)
        node.latency = random.uniform(5, 15)
        return {
            "timestamp": datetime.now().isoformat(),
            "node_id": node.id,
            "action": "reboot_node",
            "result": "success",
            "message": "Node restored"
        }

class NetworkStabilizer:
    """Stabilizes the network after remediation"""
    def __init__(self, nodes: List[NetworkNode]):
        self.nodes = nodes
        
    def stabilize(self) -> Dict[str, Any]:
        """Stabilize network metrics"""
        for node in self.nodes:
            if node.status == "healthy":
                # Gradually optimize metrics
                node.cpu_usage = max(10, node.cpu_usage - random.uniform(1, 5))
                node.memory_usage = max(20, node.memory_usage - random.uniform(1, 5))
                node.latency = max(1, node.latency - random.uniform(0.5, 2))
                node.packet_loss = max(0, node.packet_loss - random.uniform(0.1, 0.5))
                
        healthy_count = sum(1 for n in self.nodes if n.status == "healthy")
        total_count = len(self.nodes)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "healthy_nodes": healthy_count,
            "total_nodes": total_count,
            "health_percentage": round((healthy_count / total_count) * 100, 2) if total_count > 0 else 0
        }

class IncidentTracker:
    """Tracks incidents and statistics"""
    def __init__(self):
        self.incidents = []
        self.stats = {
            "total_incidents": 0,
            "auto_resolved": 0,
            "manual_intervention": 0,
            "avg_resolution_time": 0
        }
        
    def log_incident(self, incident_type: str, severity: str, node_id: str):
        """Log a new incident"""
        incident = {
            "id": len(self.incidents) + 1,
            "timestamp": datetime.now().isoformat(),
            "type": incident_type,
            "severity": severity,
            "node_id": node_id,
            "status": "open",
            "resolution_time": None
        }
        self.incidents.append(incident)
        self.stats["total_incidents"] += 1
        
    def resolve_incident(self, incident_id: int, auto: bool = True):
        """Mark incident as resolved"""
        if incident_id <= len(self.incidents):
            incident = self.incidents[incident_id - 1]
            incident["status"] = "resolved"
            incident["resolution_time"] = datetime.now().isoformat()
            
            if auto:
                self.stats["auto_resolved"] += 1
            else:
                self.stats["manual_intervention"] += 1
                
    def get_stats(self) -> Dict[str, Any]:
        """Get incident statistics"""
        recent_incidents = [i for i in self.incidents[-10:]]
        return {
            "stats": self.stats,
            "recent_incidents": recent_incidents
        }

class AutonomousNMS:
    """Main autonomous NMS orchestrator"""
    def __init__(self):
        # Initialize network topology
        self.nodes = self._create_network_topology()
        
        # Initialize components
        self.failure_injector = FailureInjector(self.nodes)
        self.anomaly_detector = AnomalyDetector()
        self.event_correlator = EventCorrelator()
        self.root_cause_analyzer = RootCauseAnalyzer()
        self.auto_remediator = AutoRemediator(self.nodes)
        self.stabilizer = NetworkStabilizer(self.nodes)
        self.incident_tracker = IncidentTracker()
        
        # System state
        self.running = False
        self.cycle_count = 0
        self.logs = deque(maxlen=100)
        
    def _create_network_topology(self) -> List[NetworkNode]:
        """Create initial network topology"""
        nodes = []
        
        # Core routers
        for i in range(3):
            node = NetworkNode(f"core-router-{i+1}", "router")
            nodes.append(node)
            
        # Edge switches
        for i in range(5):
            node = NetworkNode(f"edge-switch-{i+1}", "switch")
            nodes.append(node)
            
        # Servers
        for i in range(8):
            node = NetworkNode(f"server-{i+1}", "server")
            nodes.append(node)
            
        # Create connections
        for i, node in enumerate(nodes):
            # Connect to 2-3 other nodes
            num_connections = random.randint(2, 3)
            connections = random.sample([n.id for n in nodes if n.id != node.id], 
                                       min(num_connections, len(nodes) - 1))
            node.connections = connections
            
        return nodes
    
    def add_log(self, message: str, level: str = "info"):
        """Add log entry"""
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "level": level,
            "message": message
        })
        
    def run_cycle(self) -> Dict[str, Any]:
        """Run one cycle of the autonomous loop"""
        self.cycle_count += 1
        cycle_data = {
            "cycle": self.cycle_count,
            "timestamp": datetime.now().isoformat(),
            "phases": {}
        }
        
        # Phase 1: Inject failure (20% chance)
        if random.random() < 0.2:
            failure = self.failure_injector.inject_random_failure()
            if failure:
                cycle_data["phases"]["inject"] = failure
                self.add_log(f"Injected {failure['failure_type']} on {failure['node_id']}", "warning")
                self.incident_tracker.log_incident(
                    failure['failure_type'],
                    failure['severity'],
                    failure['node_id']
                )
        
        # Phase 2: Detect anomalies
        anomalies = self.anomaly_detector.detect(self.nodes)
        cycle_data["phases"]["detect"] = {"anomalies": anomalies, "count": len(anomalies)}
        
        if anomalies:
            self.add_log(f"Detected {len(anomalies)} anomalies", "warning")
            for anomaly in anomalies:
                self.event_correlator.add_event(anomaly)
        
        # Phase 3: Correlate events
        correlations = self.event_correlator.correlate()
        cycle_data["phases"]["correlate"] = {"correlations": correlations, "count": len(correlations)}
        
        if correlations:
            self.add_log(f"Found {len(correlations)} correlated event patterns", "info")
        
        # Phase 4: Analyze root cause
        root_causes = self.root_cause_analyzer.analyze(anomalies, correlations)
        cycle_data["phases"]["analyze"] = {"root_causes": root_causes, "count": len(root_causes)}
        
        if root_causes:
            self.add_log(f"Identified {len(root_causes)} root causes", "info")
        
        # Phase 5: Remediate
        remediation_actions = self.auto_remediator.remediate(root_causes)
        cycle_data["phases"]["remediate"] = {"actions": remediation_actions, "count": len(remediation_actions)}
        
        if remediation_actions:
            self.add_log(f"Applied {len(remediation_actions)} remediation actions", "success")
            # Resolve incidents
            for action in remediation_actions:
                if len(self.incident_tracker.incidents) > 0:
                    # Find open incident for this node
                    for incident in reversed(self.incident_tracker.incidents):
                        if incident["node_id"] == action["node_id"] and incident["status"] == "open":
                            self.incident_tracker.resolve_incident(incident["id"])
                            break
        
        # Phase 6: Stabilize
        stability = self.stabilizer.stabilize()
        cycle_data["phases"]["stabilize"] = stability
        self.add_log(f"Network stability: {stability['health_percentage']}%", "info")
        
        return cycle_data
    
    def get_topology(self) -> Dict[str, Any]:
        """Get network topology"""
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "timestamp": datetime.now().isoformat()
        }
    
    def get_metrics(self) -> Dict[str, Any]:
        """Get current metrics"""
        return {
            "nodes": [node.to_dict() for node in self.nodes],
            "summary": {
                "total_nodes": len(self.nodes),
                "healthy": sum(1 for n in self.nodes if n.status == "healthy"),
                "degraded": sum(1 for n in self.nodes if n.status == "degraded"),
                "down": sum(1 for n in self.nodes if n.status == "down"),
                "avg_cpu": round(sum(n.cpu_usage for n in self.nodes) / len(self.nodes), 2),
                "avg_memory": round(sum(n.memory_usage for n in self.nodes) / len(self.nodes), 2),
                "avg_latency": round(sum(n.latency for n in self.nodes) / len(self.nodes), 2)
            },
            "timestamp": datetime.now().isoformat()
        }
    
    def get_logs(self) -> List[Dict[str, Any]]:
        """Get recent logs"""
        return list(self.logs)
    
    def get_incidents(self) -> Dict[str, Any]:
        """Get incident statistics"""
        return self.incident_tracker.get_stats()
