#!/usr/bin/env python3
"""
Command-line interface for Autonomous NMS
Usage: python cli.py [command]

Commands:
  demo     - Run a quick demo
  test     - Run test suite
  server   - Start web server
  run      - Run continuous cycles (CLI mode)
"""
import sys
import time
import subprocess

def run_demo():
    """Run the demo"""
    print("Running demo...")
    subprocess.run([sys.executable, "demo.py"])

def run_tests():
    """Run test suite"""
    print("Running tests...")
    subprocess.run([sys.executable, "test_nms.py"])

def start_server():
    """Start web server"""
    print("Starting web server...")
    print("Access dashboard at: http://localhost:5000")
    subprocess.run([sys.executable, "app.py"])

def run_cli():
    """Run in CLI mode"""
    from nms_core import AutonomousNMS
    
    print("=" * 70)
    print("Autonomous NMS - CLI Mode")
    print("=" * 70)
    print("Press Ctrl+C to stop")
    print()
    
    nms = AutonomousNMS()
    print(f"Initialized network with {len(nms.nodes)} nodes")
    print()
    
    try:
        while True:
            cycle_data = nms.run_cycle()
            
            # Print cycle summary
            print(f"Cycle {cycle_data['cycle']} - {cycle_data['timestamp']}")
            
            phases = cycle_data['phases']
            
            if 'inject' in phases:
                inj = phases['inject']
                print(f"  ⚠️  Injected: {inj['failure_type']} on {inj['node_id']}")
            
            if 'detect' in phases and phases['detect']['count'] > 0:
                print(f"  🔍 Detected: {phases['detect']['count']} anomalies")
            
            if 'remediate' in phases and phases['remediate']['count'] > 0:
                print(f"  🔧 Remediated: {phases['remediate']['count']} issues")
            
            if 'stabilize' in phases:
                health = phases['stabilize']['health_percentage']
                health_icon = "✅" if health == 100 else "⚠️" if health >= 75 else "❌"
                print(f"  {health_icon} Health: {health}%")
            
            print()
            time.sleep(3)
            
    except KeyboardInterrupt:
        print("\nStopping...")
        metrics = nms.get_metrics()
        print(f"\nFinal network health: {(metrics['summary']['healthy'] / metrics['summary']['total_nodes']) * 100:.1f}%")
        print("Goodbye!")

def show_help():
    """Show help message"""
    print(__doc__)

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == "demo":
        run_demo()
    elif command == "test":
        run_tests()
    elif command == "server":
        start_server()
    elif command == "run":
        run_cli()
    elif command in ["help", "-h", "--help"]:
        show_help()
    else:
        print(f"Unknown command: {command}")
        show_help()

if __name__ == "__main__":
    main()
