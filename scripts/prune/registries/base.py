"""Base registry interface for container image pruning."""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from datetime import datetime


class ImageVersion:
    """Represents a container image version."""

    def __init__(self, id: str, name: str, created_at: datetime, tags: List[str], metadata: Optional[Dict[str, Any]] = None):
        self.id = id
        self.name = name
        self.created_at = created_at
        self.tags = tags
        self.metadata = metadata or {}

    @property
    def is_tagged(self) -> bool:
        """Return True if the image has any tags."""
        return len(self.tags) > 0

    def __repr__(self) -> str:
        return f"ImageVersion(id={self.id}, name={self.name}, created_at={self.created_at}, tags={self.tags})"


class BaseRegistry(ABC):
    """Abstract base class for registry implementations."""

    def __init__(self, token: str, container_name: str, verbose: bool = False):
        self.token = token
        self.container_name = container_name
        self.verbose = verbose

    @abstractmethod
    def list_versions(self) -> List[ImageVersion]:
        """List all versions of the container image."""
        pass

    @abstractmethod
    def delete_version(self, version_id: str) -> bool:
        """Delete a specific version by ID. Returns True if successful."""
        pass

    @property
    @abstractmethod
    def registry_name(self) -> str:
        """Return the name of this registry."""
        pass
