#!/usr/bin/env python3
"""
Integration tests for the prune script.

These tests validate the actual script functionality without requiring
real registry credentials.
"""

import os
import sys
import subprocess
import tempfile
from pathlib import Path

# Get the script directory (parent of tests)
script_dir = Path(__file__).parent.parent

def run_command(cmd, env=None):
    """Run a command and return the result."""
    if env is None:
        env = os.environ.copy()

    try:
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
            env=env,
            cwd=script_dir
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def test_help_output():
    """Test that the help output works."""
    print("Testing help output...")

    returncode, stdout, stderr = run_command("python3 main.py --help")

    if returncode != 0:
        print(f"❌ Help command failed: {stderr}")
        return False

    if "container" not in stdout or "registry" not in stdout:
        print(f"❌ Help output missing expected content")
        return False

    print("✅ Help output works correctly")
    return True

def test_missing_credentials():
    """Test behavior when credentials are missing."""
    print("Testing missing credentials handling...")

    # Clear all authentication environment variables
    clean_env = {k: v for k, v in os.environ.items()
                 if k not in ['GHCR_TOKEN', 'DOCKER_USERNAME', 'DOCKER_PASSWORD']}

    returncode, stdout, stderr = run_command(
        "python3 main.py --container test --registry all --prune-all-untagged --dry-run",
        env=clean_env
    )

    if returncode == 0:
        print("❌ Command should have failed without credentials")
        return False

    if "environment variable" not in stderr.lower():
        print(f"❌ Expected credential error message, got: {stderr}")
        return False

    print("✅ Missing credentials handled correctly")
    return True

def test_invalid_registry():
    """Test behavior with invalid registry type."""
    print("Testing invalid registry handling...")

    returncode, stdout, stderr = run_command(
        "python3 main.py --container test --registry invalid --prune-all-untagged --dry-run"
    )

    if returncode == 0:
        print("❌ Command should have failed with invalid registry")
        return False

    print("✅ Invalid registry handled correctly")
    return True

def test_mutually_exclusive_options():
    """Test that strategy options are mutually exclusive."""
    print("Testing mutually exclusive strategy options...")

    returncode, stdout, stderr = run_command(
        "python3 main.py --container test --registry ghcr --prune-all-untagged --keep-latest 5"
    )

    if returncode == 0:
        print("❌ Command should have failed with conflicting options")
        return False

    if "not allowed" not in stderr:
        print(f"❌ Expected mutual exclusion error, got: {stderr}")
        return False

    print("✅ Mutually exclusive options handled correctly")
    return True

def test_missing_required_args():
    """Test missing required arguments."""
    print("Testing missing required arguments...")

    # Missing container
    returncode, stdout, stderr = run_command(
        "python3 main.py --registry ghcr --prune-all-untagged"
    )

    if returncode == 0:
        print("❌ Command should have failed without container name")
        return False

    # Missing strategy
    returncode, stdout, stderr = run_command(
        "python3 main.py --container test --registry ghcr"
    )

    if returncode == 0:
        print("❌ Command should have failed without pruning strategy")
        return False

    print("✅ Missing required arguments handled correctly")
    return True

def test_import_structure():
    """Test that all modules can be imported."""
    print("Testing module imports...")

    import_tests = [
        "from registries.base import ImageVersion, BaseRegistry",
        "from registries.factory import create_registry, create_all_registries",
        "from registries.ghcr import GHCRRegistry",
        "from registries.dockerhub import DockerHubRegistry",
        "from strategies import PruneUntaggedByAge, PruneAllUntagged, KeepLatestCount",
        "import main"
    ]

    for import_test in import_tests:
        returncode, stdout, stderr = run_command(f"python3 -c '{import_test}'")
        if returncode != 0:
            print(f"❌ Import failed: {import_test}")
            print(f"   Error: {stderr}")
            return False

    print("✅ All modules import correctly")
    return True

def test_version_info():
    """Test that version information is accessible."""
    print("Testing version information...")

    returncode, stdout, stderr = run_command(
        "python3 -c 'import main; print(main.__version__)'"
    )

    if returncode != 0:
        print(f"❌ Could not access version info: {stderr}")
        return False

    if "2.0" not in stdout:
        print(f"❌ Unexpected version: {stdout}")
        return False

    print("✅ Version information accessible")
    return True

def main():
    """Run integration tests."""
    print("Running integration tests for prune script...\n")

    tests = [
        test_import_structure,
        test_version_info,
        test_help_output,
        test_missing_credentials,
        test_invalid_registry,
        test_mutually_exclusive_options,
        test_missing_required_args,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
            failed += 1
        print()

    print(f"Results: {passed} passed, {failed} failed")

    if failed > 0:
        print("❌ Some tests failed")
        return 1
    else:
        print("✅ All tests passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
