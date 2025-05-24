"""Registry factory for creating registry instances."""

import os
from typing import List

from .base import BaseRegistry
from .ghcr import GHCRRegistry
from .dockerhub import DockerHubRegistry


def create_registry(registry_type: str, container_name: str, verbose: bool = False) -> BaseRegistry:
    """Create a registry instance based on type and available credentials."""

    if registry_type.lower() in ['ghcr', 'github']:
        # GHCR uses token authentication
        token = os.environ.get('GHCR_TOKEN')
        if not token:
            raise ValueError('GHCR_TOKEN environment variable is required for GitHub Container Registry')

        return GHCRRegistry(token, container_name, verbose)

    elif registry_type.lower() in ['dockerhub', 'docker', 'hub']:
        # Docker Hub uses username/password authentication
        username = os.environ.get('DOCKER_USERNAME')
        password = os.environ.get('DOCKER_PASSWORD')

        if not username or not password:
            raise ValueError('DOCKER_USERNAME and DOCKER_PASSWORD environment variables are required for Docker Hub')

        return DockerHubRegistry(username, password, container_name, verbose)

    else:
        raise ValueError(f'Unsupported registry type: {registry_type}. Supported types: ghcr, dockerhub')


def create_all_registries(container_name: str, verbose: bool = False) -> List[BaseRegistry]:
    """Create registry instances for all available registries based on environment variables."""
    registries = []

    # Try to create GHCR registry
    try:
        ghcr = create_registry('ghcr', container_name, verbose)
        registries.append(ghcr)
    except ValueError as e:
        if verbose:
            print(f"Skipping GHCR: {e}")

    # Try to create Docker Hub registry
    try:
        dockerhub = create_registry('dockerhub', container_name, verbose)
        registries.append(dockerhub)
    except ValueError as e:
        if verbose:
            print(f"Skipping Docker Hub: {e}")

    if not registries:
        raise ValueError("No registries available. Please set the required environment variables.")

    return registries
