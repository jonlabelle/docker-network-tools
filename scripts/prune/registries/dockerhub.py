"""Docker Hub registry implementation."""

import sys
import requests
import dateutil.parser
from typing import List, Dict, Any
from datetime import datetime

from .base import BaseRegistry, ImageVersion


class DockerHubRegistry(BaseRegistry):
    """Docker Hub registry implementation."""

    DOCKER_HUB_API = 'https://hub.docker.com/v2'

    def __init__(self, username: str, password: str, container_name: str, verbose: bool = False):
        # For Docker Hub, we use username/password instead of token
        super().__init__(password, container_name, verbose)
        self.username = username
        self.password = password
        self._auth_token = None

    @property
    def registry_name(self) -> str:
        return "Docker Hub"

    def _get_auth_token(self) -> str:
        """Get authentication token for Docker Hub API."""
        if self._auth_token:
            return self._auth_token

        auth_data = {
            'identifier': self.username,
            'secret': self.password
        }

        resp = requests.post(f'{self.DOCKER_HUB_API}/auth/token', json=auth_data)
        if resp.status_code != 200:
            sys.stderr.write(f'Docker Hub auth failed: {resp.status_code}\n')
            sys.stderr.write(f'{resp.text}\n')
            sys.exit(1)

        self._auth_token = resp.json()['access_token']
        return self._auth_token

    def list_versions(self) -> List[ImageVersion]:
        """List all versions from Docker Hub."""
        token = self._get_auth_token()

        sess = requests.Session()
        sess.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        # Get repository info first
        repo_url = f'{self.DOCKER_HUB_API}/repositories/{self.username}/{self.container_name}/'
        repo_resp = sess.get(repo_url)
        if repo_resp.status_code != 200:
            sys.stderr.write(f'Docker Hub repository not found: {repo_resp.status_code}\n')
            sys.stderr.write(f'{repo_resp.text}\n')
            sys.exit(1)

        # Get all tags for the repository
        tags_url = f'{self.DOCKER_HUB_API}/repositories/{self.username}/{self.container_name}/tags/'

        versions = []
        page_size = 100
        page = 1

        while True:
            params = {
                'page_size': page_size,
                'page': page
            }

            resp = sess.get(tags_url, params=params)
            if resp.status_code != 200:
                sys.stderr.write(f'Docker Hub API error: {resp.status_code}\n')
                sys.stderr.write(f'{resp.text}\n')
                break

            data = resp.json()

            for tag_data in data.get('results', []):
                # Docker Hub doesn't have version IDs like GHCR, so we use the digest
                tag_id = tag_data.get('digest', tag_data['name'])
                created = dateutil.parser.isoparse(tag_data['last_updated'])

                # Extract tags - Docker Hub has one tag per entry
                tags = [tag_data['name']] if tag_data['name'] != 'latest' or tag_data.get('tag_status') == 'active' else []

                version = ImageVersion(
                    id=tag_id,
                    name=tag_data['name'],
                    created_at=created,
                    tags=tags,
                    metadata=tag_data
                )
                versions.append(version)

            # Check if there are more pages
            if not data.get('next'):
                break
            page += 1

        if self.verbose:
            print(f'Found {len(versions)} images in Docker Hub')

        return versions

    def delete_version(self, version_id: str) -> bool:
        """Delete a version from Docker Hub."""
        token = self._get_auth_token()

        sess = requests.Session()
        sess.headers.update({
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        })

        # For Docker Hub, we need to delete by tag name, not digest
        # Find the version by ID to get the tag name
        versions = self.list_versions()
        version_to_delete = None
        for version in versions:
            if version.id == version_id:
                version_to_delete = version
                break

        if not version_to_delete:
            if self.verbose:
                print(f"Version {version_id} not found")
            return False

        # Delete the tag
        delete_url = f'{self.DOCKER_HUB_API}/repositories/{self.username}/{self.container_name}/tags/{version_to_delete.name}/'

        resp = sess.delete(delete_url)

        try:
            resp.raise_for_status()
            return True
        except requests.exceptions.HTTPError:
            if self.verbose:
                print(f"Failed to delete tag {version_to_delete.name}: {resp.status_code} - {resp.text}")
            return False
