#!/usr/bin/env python3
"""
Master test runner for the prune script.

This script runs all tests from the tests/ directory and provides a summary.
Usage: python test_runner.py
"""

import os
import sys
import subprocess

def main():
    """Run all tests from the tests directory."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_runner = os.path.join(script_dir, "tests", "run_all_tests.py")

    if not os.path.exists(test_runner):
        print("❌ Test runner not found at:", test_runner)
        return 1

    print("🧪 Running comprehensive test suite...")
    print(f"📁 Test directory: {os.path.join(script_dir, 'tests')}")
    print("=" * 60)

    try:
        # Determine which Python to use
        # Try virtual environment first, fall back to system Python
        venv_python = os.path.join(script_dir, "bin", "python")
        if os.path.exists(venv_python):
            python_cmd = venv_python
            print(f"🐍 Using virtual environment Python: {python_cmd}")
        else:
            python_cmd = sys.executable
            print(f"🐍 Using system Python: {python_cmd}")

        print(f"📄 Running test suite: {test_runner}")

        # Run the test suite
        result = subprocess.run([
            python_cmd,
            test_runner
        ], cwd=script_dir)

        return result.returncode

    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
