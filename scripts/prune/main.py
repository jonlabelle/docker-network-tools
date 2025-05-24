#!/usr/bin/env python3

# -------------------------------------------------------------------------------------------------------
# Container Image Pruning Tool for Docker Hub and GitHub Container Registry (GHCR)
#
# This refactored tool provides a unified interface for managing container image lifecycle
# across multiple registries. It supports various pruning strategies and handles both
# Docker Hub and GitHub Container Registry with appropriate authentication methods.
#
# FEATURES:
# - Multi-registry support (Docker Hub, GHCR, or both)
# - Three pruning strategies: age-based, all-untagged, and keep-latest-N
# - Dry-run capability for safe testing
# - Verbose logging and error handling
# - Modular architecture with separate registry implementations
#
# ARCHITECTURE:
# - registries/: Registry-specific implementations
#   - base.py: Abstract base classes
#   - ghcr.py: GitHub Container Registry (token auth)
#   - dockerhub.py: Docker Hub (username/password auth)
#   - factory.py: Registry creation and management
# - strategies.py: Pruning strategy implementations
# - main.py: CLI interface and orchestration
#
# AUTHENTICATION:
# Set the following environment variables before running:
#
# For GitHub Container Registry:
#   export GHCR_TOKEN=<github_personal_access_token>
#
# For Docker Hub:
#   export DOCKER_USERNAME=<docker_hub_username>
#   export DOCKER_PASSWORD=<docker_hub_password_or_token>
#
# USAGE EXAMPLES:
#
# 1. Prune untagged images older than 7 days from both registries (dry-run):
#    $ python3 main.py --container network-tools --registry all --prune-untagged-age 7 --dry-run --verbose
#
# 2. Delete ALL untagged images from GHCR only:
#    $ python3 main.py --container network-tools --registry ghcr --prune-all-untagged --verbose
#
# 3. Keep only the latest 3 images in Docker Hub (delete everything else):
#    $ python3 main.py --container network-tools --registry dockerhub --keep-latest 3 --verbose
#
# 4. Aggressive cleanup - keep only latest 2 images across both registries:
#    $ python3 main.py --container network-tools --registry all --keep-latest 2 --verbose
#
# 5. Clean up old development images (30+ days, untagged only):
#    $ python3 main.py --container network-tools --registry all --prune-untagged-age 30 --verbose
#
# 6. Preview what would be deleted without making changes:
#    $ python3 main.py --container network-tools --registry all --keep-latest 5 --dry-run --verbose
#
# INTEGRATION WITH CI/CD:
# This tool is integrated into GitHub Actions workflows and automatically runs after
# successful image builds to maintain clean registries and manage storage usage.
#
# REFERENCES:
# - Original GHCR source: https://github.com/airtower-luna/hello-ghcr/
# - GitHub API docs: https://docs.github.com/en/rest/reference/packages
# - Docker Hub API docs: https://docs.docker.com/docker-hub/api/latest/
# -------------------------------------------------------------------------------------------------------

import sys
import argparse
from typing import List

from registries.factory import create_registry, create_all_registries
from registries.base import BaseRegistry
from strategies import PruneUntaggedByAge, PruneAllUntagged, KeepLatestCount

__author__ = "Jon LaBelle"
__version__ = "2.0"
__copyright__ = "Copyright (C) 2025 Jon LaBelle"
__license__ = "MIT"


def prune_registry(registry: BaseRegistry, strategy, dry_run: bool) -> int:
    """Prune a single registry using the given strategy."""
    print(f"\n=== {registry.registry_name} ===")
    print(strategy.get_description())

    try:
        versions = registry.list_versions()
    except Exception as e:
        print(f"Error listing versions from {registry.registry_name}: {e}")
        return 0

    if not versions:
        print("No images found")
        return 0

    deleted_count = 0

    for version in versions:
        if strategy.should_delete(version, versions):
            tag_info = f" (tags: {', '.join(version.tags)})" if version.tags else " (untagged)"

            if dry_run:
                print(f"Would delete image: {version.id}{tag_info}")
            else:
                success = registry.delete_version(version.id)
                if success:
                    print(f"Deleted image: {version.id}{tag_info}")
                    deleted_count += 1
                else:
                    print(f"Failed to delete image: {version.id}{tag_info}")

    return deleted_count


def main():
    parser = argparse.ArgumentParser(
        description='Prune container images from Docker Hub and/or GitHub Container Registry (GHCR)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:

  # Prune untagged images older than 7 days from GHCR (dry-run)
  python3 main.py --container network-tools --registry ghcr --prune-untagged-age 7 --dry-run

  # Prune all untagged images from Docker Hub
  python3 main.py --container network-tools --registry dockerhub --prune-all-untagged

  # Keep only the latest 3 images in both registries
  python3 main.py --container network-tools --registry all --keep-latest 3

Environment variables:

  GHCR_TOKEN        - GitHub personal access token (for GHCR)
  DOCKER_USERNAME   - Docker Hub username
  DOCKER_PASSWORD   - Docker Hub password or access token
        """
    )

    parser.add_argument('--container', required=True,
                        help='name of the container image')
    parser.add_argument('--registry', choices=['ghcr', 'dockerhub', 'all'], default='all',
                        help='which registry to prune (default: all)')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='print extra debug info')
    parser.add_argument('--dry-run', '-n', action='store_true',
                        help='do not actually prune images, just list which images would be pruned')

    # Pruning strategy options (mutually exclusive)
    strategy_group = parser.add_mutually_exclusive_group(required=True)
    strategy_group.add_argument('--prune-untagged-age', type=float, metavar='DAYS',
                                help='delete untagged images older than DAYS days')
    strategy_group.add_argument('--prune-all-untagged', action='store_true',
                                help='delete ALL untagged images')
    strategy_group.add_argument('--keep-latest', type=int, metavar='COUNT',
                                help='keep only the latest COUNT images (delete all others)')

    args = parser.parse_args()

    # Create pruning strategy
    if args.prune_untagged_age is not None:
        strategy = PruneUntaggedByAge(args.prune_untagged_age)
    elif args.prune_all_untagged:
        strategy = PruneAllUntagged()
    elif args.keep_latest is not None:
        strategy = KeepLatestCount(args.keep_latest)

    # Create registry instances
    registries: List[BaseRegistry] = []

    try:
        if args.registry == 'all':
            registries = create_all_registries(args.container, args.verbose)
        else:
            registries = [create_registry(
                args.registry, args.container, args.verbose)]
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if not registries:
        print("No registries available. Please check your environment variables.", file=sys.stderr)
        sys.exit(1)

    # Prune each registry
    total_deleted = 0
    for registry in registries:
        deleted_count = prune_registry(registry, strategy, args.dry_run)
        total_deleted += deleted_count

    # Summary
    print(f"\n=== Summary ===")
    if total_deleted == 0:
        print('No images qualified for deletion')
    else:
        action = "would have been deleted" if args.dry_run else "were deleted"
        print(f"{total_deleted} image{'' if total_deleted == 1 else 's'} {action}")


if __name__ == "__main__":
    main()
