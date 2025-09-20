# Container Image Pruning Script

[![test prune script](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml/badge.svg)](https://github.com/jonlabelle/docker-network-tools/actions/workflows/test-prune-script.yml)

> Container image pruning script that supports both Docker Hub and GitHub Container Registry (GHCR).

## Usage

```console
usage: main.py [-h] --container CONTAINER
  [--registry {ghcr, dockerhub, all}]
  [--verbose] [--dry-run]
  (--prune-untagged-age DAYS | --prune-all-untagged | --keep-latest COUNT)
```

### Environment Variables

To use the script, you need to set up environment variables for authentication.
The script supports both [Docker Hub](https://hub.docker.com) and [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry).

**Docker Hub variables:**

```bash
export DOCKER_USERNAME=<your_docker_username>
export DOCKER_PASSWORD=<your_docker_password_or_token>
```

**GitHub Container Registry variables:**

```bash
export GHCR_TOKEN=<your_github_token>
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

### Examples

```bash
# Prune untagged images older than 7 days from both registries
python main.py --container network-tools --registry all --prune-untagged-age 7 --verbose

# Keep only the latest 5 images in GHCR (delete everything else)
python main.py --container network-tools --registry ghcr --keep-latest 5 --verbose

# Dry run: see what would be deleted from Docker Hub
python main.py --container network-tools --registry dockerhub --prune-all-untagged --dry-run --verbose
```

## Testing

```bash
python test_runner.py  # Run all tests
```

> For comprehensive testing documentation, see [`tests/README.md`](tests/README.md).
