"""Pruning strategies for container images."""

from abc import ABC, abstractmethod
from typing import List
from datetime import datetime, timedelta

from registries.base import ImageVersion


class PruningStrategy(ABC):
    """Abstract base class for pruning strategies."""

    @abstractmethod
    def should_delete(self, version: ImageVersion, all_versions: List[ImageVersion]) -> bool:
        """Determine if a version should be deleted."""
        pass

    @abstractmethod
    def get_description(self) -> str:
        """Get a human-readable description of the strategy."""
        pass


class PruneUntaggedByAge(PruningStrategy):
    """Prune untagged images older than a specified age."""

    def __init__(self, days: float):
        self.days = days
        self.cutoff_date = datetime.now().astimezone() - timedelta(days=days)

    def should_delete(self, version: ImageVersion, all_versions: List[ImageVersion]) -> bool:
        return not version.is_tagged and version.created_at < self.cutoff_date

    def get_description(self) -> str:
        return f"Pruning untagged images older than {self.days} days (before {self.cutoff_date})"


class PruneAllUntagged(PruningStrategy):
    """Prune all untagged images."""

    def should_delete(self, version: ImageVersion, all_versions: List[ImageVersion]) -> bool:
        return not version.is_tagged

    def get_description(self) -> str:
        return "Pruning all untagged images"


class KeepLatestCount(PruningStrategy):
    """Keep only the latest N images, delete everything else."""

    def __init__(self, count: int):
        self.count = count

    def should_delete(self, version: ImageVersion, all_versions: List[ImageVersion]) -> bool:
        # Sort all versions by creation date (newest first)
        sorted_versions = sorted(all_versions, key=lambda v: v.created_at, reverse=True)

        # Find the index of this version in the sorted list
        try:
            index = next(i for i, v in enumerate(sorted_versions) if v.id == version.id)
            # Delete if this version is not in the top N
            return index >= self.count
        except StopIteration:
            # If we can't find the version, don't delete it
            return False

    def get_description(self) -> str:
        return f"Keeping only the latest {self.count} images (deleting all others)"
