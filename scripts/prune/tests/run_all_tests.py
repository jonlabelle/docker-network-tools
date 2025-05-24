#!/usr/bin/env python3
"""
Run all tests for the prune script.

This script executes all test suites and provides a summary of results.
"""

import os
import sys
import subprocess

def run_test_suite(command, name):
    """Run a test suite and return results."""
    print(f"\n{'='*60}")
    print(f"Running: {name}")
    print(f"{'='*60}")

    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=os.path.dirname(os.path.dirname(__file__)),  # Run from parent directory
            timeout=60
        )

        if result.returncode == 0:
            print(f"✅ {name} - PASSED")
            return True
        else:
            print(f"❌ {name} - FAILED (exit code: {result.returncode})")
            return False

    except subprocess.TimeoutExpired:
        print(f"❌ {name} - TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ {name} - ERROR: {e}")
        return False

def main():
    """Run all test suites."""
    print("Running comprehensive test suite for prune script...")

    test_suites = [
        ("./bin/python tests/test_prune.py", "Comprehensive Unit Tests"),
        ("./bin/python tests/test_integration.py", "Integration Tests"),
    ]

    passed = 0
    total = len(test_suites)

    for command, name in test_suites:
        if run_test_suite(command, name):
            passed += 1

    print(f"\n{'='*60}")
    print(f"TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total Test Suites: {total}")
    print(f"Passed: {passed}")
    print(f"Failed: {total - passed}")
    print(f"Success Rate: {(passed/total)*100:.1f}%")

    if passed == total:
        print("\n🎉 ALL TESTS PASSED!")
        print("✅ Script is ready for production deployment")
        return 0
    else:
        print(f"\n❌ {total - passed} test suite(s) failed")
        print("🔧 Review and fix issues before deployment")
        return 1

if __name__ == "__main__":
    sys.exit(main())
