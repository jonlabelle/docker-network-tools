"""
Test suite for the container image pruning tool.

This package contains comprehensive tests for all components of the prune script:

- Unit tests for core functionality
- Integration tests for CLI interface
- Validation tests for quick checks
- Test utilities and runners

Run all tests with: python run_all_tests.py
"""

import sys
import os

# Add the parent directory (prune script root) to Python path
# This allows test files to import the main modules
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)
