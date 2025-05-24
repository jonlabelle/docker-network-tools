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
        # Run the test suite
        result = subprocess.run([
            os.path.join(script_dir, "bin", "python"),
            test_runner
        ], cwd=script_dir)

        return result.returncode

    except Exception as e:
        print(f"❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
