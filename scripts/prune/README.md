# Container Image Pruning Script

[![test prune script](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml)

> Container image pruning script that supports both Docker Hub and GitHub Container Registry (GHCR).

## Overview

- Support both Docker Hub and GitHub Container Registry
- Use a modular architecture with separate registry implementations
- Provide multiple pruning strategies including a new "keep latest N images" option
- Better error handling and logging

## Architecture

### File Structure

```plaintext
scripts/prune/
├── main.py                # Main CLI script
├── strategies.py          # Pruning strategy implementations
├── requirements.txt       # Python dependencies
└── registries/
    ├── __init__.py
    ├── base.py            # Abstract base classes
    ├── factory.py         # Registry factory
    ├── ghcr.py            # GitHub Container Registry implementation
    └── dockerhub.py       # Docker Hub implementation
```

### Registry Implementations

- **GHCRRegistry**: Uses GitHub API with token authentication
- **DockerHubRegistry**: Uses Docker Hub API with username/password authentication

### Pruning Strategies

1. **PruneUntaggedByAge**: Delete untagged images older than specified days
2. **PruneAllUntagged**: Delete all untagged images
3. **KeepLatestCount**: Keep only the latest N images (NEW)

## Usage Examples

### Environment Variables

```bash
# For GitHub Container Registry
export GHCR_TOKEN=<your_github_token>

# For Docker Hub
export DOCKER_USERNAME=<your_docker_username>
export DOCKER_PASSWORD=<your_docker_password_or_token>
```

### Command Examples

```bash
# Prune untagged images older than 7 days from both registries
python main.py --container network-tools --registry all --prune-untagged-age 7 --verbose

# Keep only the latest 5 images in GHCR (delete everything else)
python main.py --container network-tools --registry ghcr --keep-latest 5 --verbose

# Dry run: see what would be deleted from Docker Hub
python main.py --container network-tools --registry dockerhub --prune-all-untagged --dry-run --verbose
```

### CLI Options

- `--container`: Name of the container image (required)
- `--registry`: Which registry to prune (`ghcr`, `dockerhub`, `all`)
- `--verbose`: Enable verbose output
- `--dry-run`: Show what would be deleted without actually deleting

**Pruning Strategies (mutually exclusive):**

- `--prune-untagged-age DAYS`: Delete untagged images older than DAYS
- `--prune-all-untagged`: Delete all untagged images
- `--keep-latest COUNT`: Keep only the latest COUNT images

## Integration with GitHub Actions

The script is integrated into two GitHub Actions workflows:

### Production Usage (`cd.yml`)

The script runs after successful image builds to clean up old untagged images:

```yaml
- name: Prune old untagged images
  run: python scripts/prune/main.py --container ${{ env.IMAGE_NAME }} --registry all --prune-untagged-age 7 --verbose
```

### Automated Testing (`test-prune-script.yml`)

The test suite runs automatically whenever files in the prune directory are modified:

- ✅ Unit tests (20 comprehensive tests)
- ✅ Integration tests (7 CLI tests)
- ✅ Help interface validation
- ✅ Dry-run functionality testing

This ensures that:

- All changes to the prune script are automatically tested
- Old untagged images are cleaned up automatically in production
- Storage usage is kept manageable
- Both Docker Hub and GHCR are maintained consistently

## Error Handling

- Graceful handling of missing credentials
- Registry-specific error reporting
- Continues processing other registries if one fails
- Detailed error messages in verbose mode

## Testing

The script includes a comprehensive test suite to ensure reliability and correctness. All tests are organized in the `tests/` directory.

### Test Structure

```plaintext
tests/
├── README.md              # Testing documentation
├── __init__.py           # Package initialization
├── test_prune.py         # Comprehensive unit tests (20 tests)
├── test_integration.py   # Integration tests (7 tests)
└── run_all_tests.py      # Master test runner
```

### Running Tests

**From the prune script root directory:**

```bash
python test_runner.py                    # Master test runner
```

****From the tests directory:**

```bash
python tests/run_all_tests.py           # Run all test suites
python tests/test_prune.py              # Unit tests only
python tests/test_integration.py        # Integration tests only
```

### Test Coverage

The test suite covers:

- ✅ All pruning strategies
- ✅ Registry factory functionality
- ✅ Error handling scenarios
- ✅ CLI argument parsing
- ✅ Dry-run functionality
- ✅ Multi-registry support
- ✅ Authentication handling

### Test Results

All tests are currently passing:

- 20/20 unit tests passed
- 7/7 integration tests passed

Run the test suite with `python test_runner.py` to generate current results.
