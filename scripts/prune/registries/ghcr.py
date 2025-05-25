"""GitHub Container Registry implementation."""

import sys
import requests
import dateutil.parser
from typing import List
from datetime import datetime

from .base import BaseRegistry, ImageVersion


class GHCRRegistry(BaseRegistry):
    """GitHub Container Registry implementation."""

    GITHUB_API = 'https://api.github.com/user/packages/container'
    GITHUB_API_ACCEPT = 'application/vnd.github.v3+json'

    @property
    def registry_name(self) -> str:
        return "GitHub Container Registry"

    def list_versions(self) -> List[ImageVersion]:
        """List all versions from GHCR."""
        sess = requests.Session()
        sess.headers.update({
            'Authorization': f'token {self.token}',
            'Accept': self.GITHUB_API_ACCEPT
        })

        resp = sess.get(f'{self.GITHUB_API}/{self.container_name}/versions')
        if resp.status_code != 200:
            sys.stderr.write(f'GitHub API returned status code: {resp.status_code}\n')
            sys.stderr.write(f'{resp.text}\n')
            sys.exit(1)

        versions_data = resp.json()

        if self.verbose:
            ratelimit_reset_at = datetime.fromtimestamp(int(resp.headers["x-ratelimit-reset"]))
            print(f'{resp.headers["x-ratelimit-remaining"]} requests remaining until {ratelimit_reset_at}')

        versions = []
        for version_data in versions_data:
            created = dateutil.parser.isoparse(version_data['created_at'])
            metadata = version_data["metadata"]["container"]

            version = ImageVersion(
                id=str(version_data['id']),
                name=version_data['name'],
                created_at=created,
                tags=metadata['tags'],
                metadata=version_data
            )
            versions.append(version)

        if self.verbose:
            print(f'Found {len(versions)} images in GitHub Container Registry')

        return versions

    def delete_version(self, version_id: str) -> bool:
        """Delete a version from GHCR."""
        sess = requests.Session()
        sess.headers.update({
            'Authorization': f'token {self.token}',
            'Accept': self.GITHUB_API_ACCEPT
        })

        resp = sess.delete(f'{self.GITHUB_API}/{self.container_name}/versions/{version_id}')

        try:
            resp.raise_for_status()
            return True
        except requests.exceptions.HTTPError:
            if self.verbose:
                print(f"Failed to delete version {version_id}: {resp.status_code} - {resp.text}")
            return False
