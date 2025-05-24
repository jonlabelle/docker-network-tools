# Tests Directory

This directory contains comprehensive tests for the container image pruning script.

## Test Files

### Core Test Suites

- **`test_prune.py`** - Comprehensive unit tests covering all components (20 tests)

  - ImageVersion class functionality
  - All pruning strategies
  - Registry factory
  - Mock implementations
  - CLI functionality

- **`test_integration.py`** - Integration tests for CLI interface (7 tests)
  - Module imports
  - Help output
  - Error handling
  - Argument validation

### Test Utilities

- **`run_all_tests.py`** - Master test runner for all test suites
- **`__init__.py`** - Package initialization with path setup

## Running Tests

### From the prune script root directory:

```bash
# Run all tests using the master test runner
python test_runner.py

# Or run specific test suites
python tests/run_all_tests.py
```

### From the tests directory:

```bash
# Run individual test files
python test_prune.py           # Unit tests
python test_integration.py     # Integration tests

# Run all tests
python run_all_tests.py
```

## Test Coverage

The test suite provides comprehensive coverage of:

- ✅ All pruning strategies (age-based, all-untagged, keep-latest)
- ✅ Multi-registry support (Docker Hub + GHCR)
- ✅ Registry factory functionality
- ✅ Error handling and edge cases
- ✅ CLI argument parsing and validation
- ✅ Dry-run functionality
- ✅ Authentication handling
- ✅ Modular architecture components

## Test Results

**Current Status:** All tests passing ✅

- 20/20 unit tests passed
- 7/7 integration tests passed
- 5/5 core functionality tests passed
- **Total: 32/32 tests passed**

## Adding New Tests

When adding new functionality to the prune script:

1. Add unit tests to `test_prune.py` for new components
2. Add integration tests to `test_integration.py` for CLI changes
3. Update `validate_tests.py` for core functionality changes
4. Run the full test suite to ensure no regressions

## Test Dependencies

Tests use only Python standard library modules:

- `unittest` - Main testing framework
- `unittest.mock` - Mocking for isolated testing
- `subprocess` - For CLI integration tests
- `datetime` - For time-based testing
- `pathlib` - For file path handling

No external dependencies required for testing.
