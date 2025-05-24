#!/usr/bin/env python3
"""
Test suite for the container image pruning tool.

This test suite covers:
- Image version data structures
- Pruning strategies
- Registry factory functionality
- Mock registry implementations
- End-to-end command line interface
"""

import unittest
import sys
import os
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime, timedelta
from io import StringIO

# Add the parent directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from registries.base import ImageVersion, BaseRegistry
from strategies import PruneUntaggedByAge, PruneAllUntagged, KeepLatestCount
from registries.factory import create_registry, create_all_registries
import main


class TestImageVersion(unittest.TestCase):
    """Test the ImageVersion data structure."""

    def setUp(self):
        self.now = datetime.now().astimezone()

    def test_tagged_image(self):
        """Test a tagged image."""
        version = ImageVersion("v1", "test", self.now, ["latest", "v1.0"])
        self.assertTrue(version.is_tagged)
        self.assertEqual(version.tags, ["latest", "v1.0"])

    def test_untagged_image(self):
        """Test an untagged image."""
        version = ImageVersion("v2", "test", self.now, [])
        self.assertFalse(version.is_tagged)
        self.assertEqual(version.tags, [])

    def test_metadata(self):
        """Test image with metadata."""
        metadata = {"size": 100, "digest": "sha256:abc123"}
        version = ImageVersion("v3", "test", self.now, ["dev"], metadata)
        self.assertEqual(version.metadata["size"], 100)
        self.assertEqual(version.metadata["digest"], "sha256:abc123")


class TestPruningStrategies(unittest.TestCase):
    """Test the pruning strategies."""

    def setUp(self):
        self.now = datetime.now().astimezone()

        # Create a set of test images with different ages and tags
        self.versions = [
            ImageVersion("v1", "old-tagged", self.now - timedelta(days=30), ["v1.0"]),
            ImageVersion("v2", "old-untagged", self.now - timedelta(days=20), []),
            ImageVersion("v3", "recent-tagged", self.now - timedelta(days=5), ["latest"]),
            ImageVersion("v4", "recent-untagged", self.now - timedelta(days=2), []),
            ImageVersion("v5", "newest", self.now - timedelta(hours=1), ["dev"]),
        ]

    def test_prune_untagged_by_age(self):
        """Test pruning untagged images by age."""
        strategy = PruneUntaggedByAge(10)  # 10 days

        to_delete = [v for v in self.versions if strategy.should_delete(v, self.versions)]

        # Should only delete old untagged image (v2)
        self.assertEqual(len(to_delete), 1)
        self.assertEqual(to_delete[0].id, "v2")

        # Test description
        self.assertIn("10", strategy.get_description())
        self.assertIn("untagged", strategy.get_description())

    def test_prune_all_untagged(self):
        """Test pruning all untagged images."""
        strategy = PruneAllUntagged()

        to_delete = [v for v in self.versions if strategy.should_delete(v, self.versions)]

        # Should delete both untagged images (v2, v4)
        self.assertEqual(len(to_delete), 2)
        deleted_ids = [v.id for v in to_delete]
        self.assertIn("v2", deleted_ids)
        self.assertIn("v4", deleted_ids)

        # Test description
        self.assertIn("all untagged", strategy.get_description().lower())

    def test_keep_latest_count(self):
        """Test keeping only the latest N images."""
        strategy = KeepLatestCount(3)

        to_delete = [v for v in self.versions if strategy.should_delete(v, self.versions)]

        # Should delete the 2 oldest images (v1, v2)
        self.assertEqual(len(to_delete), 2)
        deleted_ids = [v.id for v in to_delete]
        self.assertIn("v1", deleted_ids)
        self.assertIn("v2", deleted_ids)

        # Test description
        self.assertIn("3", strategy.get_description())
        self.assertIn("latest", strategy.get_description())

    def test_keep_latest_count_edge_cases(self):
        """Test keep latest with edge cases."""
        # Keep more than available
        strategy = KeepLatestCount(10)
        to_delete = [v for v in self.versions if strategy.should_delete(v, self.versions)]
        self.assertEqual(len(to_delete), 0)

        # Keep only 1
        strategy = KeepLatestCount(1)
        to_delete = [v for v in self.versions if strategy.should_delete(v, self.versions)]
        self.assertEqual(len(to_delete), 4)  # Should keep only the newest


class MockRegistry(BaseRegistry):
    """Mock registry for testing."""

    def __init__(self, name, versions=None, fail_delete=False):
        super().__init__("mock_token", "test_container", verbose=False)
        self._name = name
        self._versions = versions or []
        self._fail_delete = fail_delete
        self._deleted_versions = []

    @property
    def registry_name(self):
        return self._name

    def list_versions(self):
        return self._versions

    def delete_version(self, version_id):
        if self._fail_delete:
            return False
        self._deleted_versions.append(version_id)
        return True


class TestRegistryFactory(unittest.TestCase):
    """Test the registry factory."""

    @patch.dict(os.environ, {'GHCR_TOKEN': 'test_token'})
    def test_create_ghcr_registry(self):
        """Test creating GHCR registry with token."""
        registry = create_registry('ghcr', 'test-container')
        self.assertEqual(registry.registry_name, "GitHub Container Registry")

    @patch.dict(os.environ, {'DOCKER_USERNAME': 'testuser', 'DOCKER_PASSWORD': 'testpass'})
    def test_create_dockerhub_registry(self):
        """Test creating Docker Hub registry with credentials."""
        registry = create_registry('dockerhub', 'test-container')
        self.assertEqual(registry.registry_name, "Docker Hub")

    def test_create_registry_missing_credentials(self):
        """Test creating registry without credentials."""
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(ValueError):
                create_registry('ghcr', 'test-container')

            with self.assertRaises(ValueError):
                create_registry('dockerhub', 'test-container')

    def test_create_registry_invalid_type(self):
        """Test creating registry with invalid type."""
        with self.assertRaises(ValueError):
            create_registry('invalid', 'test-container')

    @patch.dict(os.environ, {
        'GHCR_TOKEN': 'test_token',
        'DOCKER_USERNAME': 'testuser',
        'DOCKER_PASSWORD': 'testpass'
    })
    def test_create_all_registries(self):
        """Test creating all available registries."""
        registries = create_all_registries('test-container')
        self.assertEqual(len(registries), 2)

        registry_names = [r.registry_name for r in registries]
        self.assertIn("GitHub Container Registry", registry_names)
        self.assertIn("Docker Hub", registry_names)


class TestPruneRegistry(unittest.TestCase):
    """Test the prune_registry function."""

    def setUp(self):
        self.now = datetime.now().astimezone()
        self.versions = [
            ImageVersion("v1", "tagged", self.now - timedelta(days=10), ["latest"]),
            ImageVersion("v2", "untagged", self.now - timedelta(days=5), []),
        ]

    def test_prune_registry_success(self):
        """Test successful pruning."""
        registry = MockRegistry("Test Registry", self.versions)
        strategy = PruneAllUntagged()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            deleted_count = main.prune_registry(registry, strategy, dry_run=False)

        self.assertEqual(deleted_count, 1)
        self.assertEqual(registry._deleted_versions, ["v2"])

        output = mock_stdout.getvalue()
        self.assertIn("Test Registry", output)
        self.assertIn("Deleted image: v2", output)

    def test_prune_registry_dry_run(self):
        """Test dry run mode."""
        registry = MockRegistry("Test Registry", self.versions)
        strategy = PruneAllUntagged()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            deleted_count = main.prune_registry(registry, strategy, dry_run=True)

        self.assertEqual(deleted_count, 0)
        self.assertEqual(registry._deleted_versions, [])

        output = mock_stdout.getvalue()
        self.assertIn("Would delete image: v2", output)

    def test_prune_registry_delete_failure(self):
        """Test handling delete failures."""
        registry = MockRegistry("Test Registry", self.versions, fail_delete=True)
        strategy = PruneAllUntagged()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            deleted_count = main.prune_registry(registry, strategy, dry_run=False)

        self.assertEqual(deleted_count, 0)
        output = mock_stdout.getvalue()
        self.assertIn("Failed to delete image: v2", output)

    def test_prune_registry_no_images(self):
        """Test registry with no images."""
        registry = MockRegistry("Empty Registry", [])
        strategy = PruneAllUntagged()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            deleted_count = main.prune_registry(registry, strategy, dry_run=False)

        self.assertEqual(deleted_count, 0)
        output = mock_stdout.getvalue()
        self.assertIn("No images found", output)

    def test_prune_registry_list_error(self):
        """Test handling list_versions errors."""
        registry = MockRegistry("Failing Registry", self.versions)
        registry.list_versions = Mock(side_effect=Exception("API Error"))
        strategy = PruneAllUntagged()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            deleted_count = main.prune_registry(registry, strategy, dry_run=False)

        self.assertEqual(deleted_count, 0)
        output = mock_stdout.getvalue()
        self.assertIn("Error listing versions", output)
        self.assertIn("API Error", output)


class TestMainFunction(unittest.TestCase):
    """Test the main CLI function."""

    def setUp(self):
        self.test_args = [
            'main.py',
            '--container', 'test-container',
            '--registry', 'all',
            '--prune-all-untagged',
            '--dry-run',
            '--verbose'
        ]

    @patch('main.create_all_registries')
    @patch('main.prune_registry')
    @patch('sys.argv', ['main.py', '--container', 'test-container', '--registry', 'all', '--prune-all-untagged', '--dry-run', '--verbose'])
    def test_main_success(self, mock_prune, mock_create_registries):
        """Test successful main execution."""
        # Mock registries
        mock_registry = MockRegistry("Test Registry")
        mock_create_registries.return_value = [mock_registry]
        mock_prune.return_value = 2

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main.main()

        output = mock_stdout.getvalue()
        self.assertIn("Summary", output)
        self.assertIn("2 images would have been deleted", output)

    @patch('main.create_all_registries')
    @patch('sys.argv', ['main.py', '--container', 'test-container', '--registry', 'all', '--prune-all-untagged', '--dry-run', '--verbose'])
    def test_main_no_registries(self, mock_create_registries):
        """Test main with no available registries."""
        mock_create_registries.side_effect = ValueError("No credentials")

        with patch('sys.stderr', new_callable=StringIO) as mock_stderr:
            with self.assertRaises(SystemExit):
                main.main()

        error_output = mock_stderr.getvalue()
        self.assertIn("No credentials", error_output)


class TestCommandLineInterface(unittest.TestCase):
    """Test command line argument parsing."""

    def test_help_output(self):
        """Test that help can be displayed."""
        parser = main.argparse.ArgumentParser(
            description='Prune container images from Docker Hub and/or GitHub Container Registry (GHCR)',
            formatter_class=main.argparse.RawDescriptionHelpFormatter,
        )

        # Add the same arguments as main
        parser.add_argument('--container', required=True)
        parser.add_argument('--registry', choices=['ghcr', 'dockerhub', 'all'], default='all')
        parser.add_argument('--verbose', '-v', action='store_true')
        parser.add_argument('--dry-run', '-n', action='store_true')

        strategy_group = parser.add_mutually_exclusive_group(required=True)
        strategy_group.add_argument('--prune-untagged-age', type=float, metavar='DAYS')
        strategy_group.add_argument('--prune-all-untagged', action='store_true')
        strategy_group.add_argument('--keep-latest', type=int, metavar='COUNT')

        # This should not raise an exception
        help_text = parser.format_help()
        self.assertIn("container", help_text)
        self.assertIn("registry", help_text)


if __name__ == '__main__':
    # Create a test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Add all test classes
    test_classes = [
        TestImageVersion,
        TestPruningStrategies,
        TestRegistryFactory,
        TestPruneRegistry,
        TestMainFunction,
        TestCommandLineInterface,
    ]

    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed
    sys.exit(0 if result.wasSuccessful() else 1)
