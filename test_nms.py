"""
Test script for Autonomous NMS
Tests core functionality of all components
"""
import sys
import time
from nms_core import (
    NetworkNode,
    FailureInjector,
    AnomalyDetector,
    EventCorrelator,
    RootCauseAnalyzer,
    AutoRemediator,
    NetworkStabilizer,
    IncidentTracker,
    AutonomousNMS
)

def test_network_node():
    """Test NetworkNode creation"""
    print("Testing NetworkNode...")
    node = NetworkNode("test-node-1", "router")
    assert node.id == "test-node-1"
    assert node.type == "router"
    assert node.status == "healthy"
    assert 10 <= node.cpu_usage <= 30
    print("✓ NetworkNode test passed")

def test_failure_injector():
    """Test FailureInjector"""
    print("\nTesting FailureInjector...")
    nodes = [NetworkNode(f"node-{i}", "server") for i in range(3)]
    injector = FailureInjector(nodes)
    
    failure = injector.inject_random_failure()
    assert failure is not None
    assert "node_id" in failure
    assert "failure_type" in failure
    assert "severity" in failure
    print(f"✓ FailureInjector test passed - Injected: {failure['failure_type']}")

def test_anomaly_detector():
    """Test AnomalyDetector"""
    print("\nTesting AnomalyDetector...")
    detector = AnomalyDetector()
    
    # Create nodes with anomalies
    nodes = [NetworkNode("node-1", "server")]
    nodes[0].cpu_usage = 95  # High CPU
    
    anomalies = detector.detect(nodes)
    assert len(anomalies) > 0
    assert anomalies[0]["metric"] == "cpu_usage"
    print(f"✓ AnomalyDetector test passed - Detected {len(anomalies)} anomalies")

def test_event_correlator():
    """Test EventCorrelator"""
    print("\nTesting EventCorrelator...")
    correlator = EventCorrelator()
    
    # Add multiple events for same node
    for i in range(3):
        correlator.add_event({
            "node_id": "node-1",
            "metric": f"metric-{i}",
            "timestamp": time.time()
        })
    
    correlations = correlator.correlate()
    assert len(correlations) > 0
    assert correlations[0]["event_count"] >= 2
    print(f"✓ EventCorrelator test passed - Found {len(correlations)} correlations")

def test_root_cause_analyzer():
    """Test RootCauseAnalyzer"""
    print("\nTesting RootCauseAnalyzer...")
    analyzer = RootCauseAnalyzer()
    
    anomalies = [{
        "node_id": "node-1",
        "metric": "high_cpu",
        "timestamp": time.time()
    }]
    
    root_causes = analyzer.analyze(anomalies, [])
    assert len(root_causes) > 0
    assert "root_cause" in root_causes[0]
    assert "confidence" in root_causes[0]
    print(f"✓ RootCauseAnalyzer test passed - Found {len(root_causes)} root causes")

def test_auto_remediator():
    """Test AutoRemediator"""
    print("\nTesting AutoRemediator...")
    nodes = [NetworkNode("node-1", "server")]
    nodes[0].cpu_usage = 95
    
    remediator = AutoRemediator(nodes)
    root_causes = [{
        "node_id": "node-1",
        "affected_metrics": ["high_cpu"]
    }]
    
    actions = remediator.remediate(root_causes)
    assert len(actions) > 0
    assert actions[0]["result"] == "success"
    assert nodes[0].cpu_usage < 95  # Should be fixed
    print(f"✓ AutoRemediator test passed - Applied {len(actions)} actions")

def test_network_stabilizer():
    """Test NetworkStabilizer"""
    print("\nTesting NetworkStabilizer...")
    nodes = [NetworkNode("node-1", "server") for i in range(3)]
    stabilizer = NetworkStabilizer(nodes)
    
    result = stabilizer.stabilize()
    assert "healthy_nodes" in result
    assert "total_nodes" in result
    assert "health_percentage" in result
    print(f"✓ NetworkStabilizer test passed - Health: {result['health_percentage']}%")

def test_incident_tracker():
    """Test IncidentTracker"""
    print("\nTesting IncidentTracker...")
    tracker = IncidentTracker()
    
    tracker.log_incident("high_cpu", "warning", "node-1")
    tracker.resolve_incident(1, auto=True)
    
    stats = tracker.get_stats()
    assert stats["stats"]["total_incidents"] == 1
    assert stats["stats"]["auto_resolved"] == 1
    print(f"✓ IncidentTracker test passed - Tracked {stats['stats']['total_incidents']} incidents")

def test_autonomous_nms():
    """Test AutonomousNMS integration"""
    print("\nTesting AutonomousNMS...")
    nms = AutonomousNMS()
    
    # Test topology creation
    assert len(nms.nodes) == 16  # 3 routers + 5 switches + 8 servers
    
    # Run one cycle
    cycle_data = nms.run_cycle()
    assert "cycle" in cycle_data
    assert "phases" in cycle_data
    assert "detect" in cycle_data["phases"]
    
    # Test data retrieval
    topology = nms.get_topology()
    assert "nodes" in topology
    
    metrics = nms.get_metrics()
    assert "summary" in metrics
    
    logs = nms.get_logs()
    assert isinstance(logs, list)
    
    incidents = nms.get_incidents()
    assert "stats" in incidents
    
    print(f"✓ AutonomousNMS test passed - Cycle {cycle_data['cycle']} completed")

def run_all_tests():
    """Run all tests"""
    print("=" * 60)
    print("Running Autonomous NMS Test Suite")
    print("=" * 60)
    
    try:
        test_network_node()
        test_failure_injector()
        test_anomaly_detector()
        test_event_correlator()
        test_root_cause_analyzer()
        test_auto_remediator()
        test_network_stabilizer()
        test_incident_tracker()
        test_autonomous_nms()
        
        print("\n" + "=" * 60)
        print("✓ ALL TESTS PASSED!")
        print("=" * 60)
        return 0
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1
    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(run_all_tests())
