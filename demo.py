#!/usr/bin/env python3
"""
Quick demo of the Autonomous NMS
Runs the system for a few cycles and shows the results
"""
import time
from nms_core import AutonomousNMS

def demo():
    print("=" * 70)
    print("Autonomous Network Management System - Demo")
    print("=" * 70)
    print()
    
    # Initialize NMS
    print("Initializing NMS...")
    nms = AutonomousNMS()
    print(f"✓ Created network topology with {len(nms.nodes)} nodes")
    print(f"  - 3 Core Routers")
    print(f"  - 5 Edge Switches")
    print(f"  - 8 Servers")
    print()
    
    # Show initial state
    metrics = nms.get_metrics()
    print("Initial Network State:")
    print(f"  Healthy: {metrics['summary']['healthy']}/{metrics['summary']['total_nodes']}")
    print(f"  Avg CPU: {metrics['summary']['avg_cpu']}%")
    print(f"  Avg Memory: {metrics['summary']['avg_memory']}%")
    print(f"  Avg Latency: {metrics['summary']['avg_latency']}ms")
    print()
    
    # Run autonomous cycles
    print("Starting Autonomous Cycle...")
    print("-" * 70)
    
    for i in range(5):
        print(f"\nCycle {i+1}:")
        cycle_data = nms.run_cycle()
        
        # Show what happened in this cycle
        phases = cycle_data['phases']
        
        if 'inject' in phases:
            inj = phases['inject']
            print(f"  [INJECT] {inj['failure_type']} on {inj['node_id']} ({inj['severity']})")
        
        if 'detect' in phases and phases['detect']['count'] > 0:
            print(f"  [DETECT] Found {phases['detect']['count']} anomalies")
        
        if 'correlate' in phases and phases['correlate']['count'] > 0:
            print(f"  [CORRELATE] Identified {phases['correlate']['count']} patterns")
        
        if 'analyze' in phases and phases['analyze']['count'] > 0:
            print(f"  [ANALYZE] Determined {phases['analyze']['count']} root causes")
        
        if 'remediate' in phases and phases['remediate']['count'] > 0:
            print(f"  [REMEDIATE] Applied {phases['remediate']['count']} fixes")
            for action in phases['remediate']['actions']:
                print(f"    → {action['action']} on {action['node_id']}: {action['message']}")
        
        if 'stabilize' in phases:
            stab = phases['stabilize']
            print(f"  [STABILIZE] Network health: {stab['health_percentage']}%")
        
        time.sleep(2)  # Wait between cycles
    
    print()
    print("-" * 70)
    
    # Show final statistics
    print("\nFinal Statistics:")
    incidents = nms.get_incidents()
    stats = incidents['stats']
    print(f"  Total Incidents: {stats['total_incidents']}")
    print(f"  Auto-Resolved: {stats['auto_resolved']}")
    print(f"  Manual Intervention: {stats['manual_intervention']}")
    
    if stats['total_incidents'] > 0:
        auto_rate = (stats['auto_resolved'] / stats['total_incidents']) * 100
        print(f"  Auto-Fix Rate: {auto_rate:.1f}%")
    
    metrics = nms.get_metrics()
    print(f"\nFinal Network Health: {(metrics['summary']['healthy'] / metrics['summary']['total_nodes']) * 100:.1f}%")
    
    print()
    print("=" * 70)
    print("Demo Complete!")
    print()
    print("To access the web dashboard:")
    print("  1. Run: python app.py")
    print("  2. Open: http://localhost:5000")
    print("  3. Click 'Start' to begin autonomous operation")
    print("=" * 70)

if __name__ == "__main__":
    demo()
