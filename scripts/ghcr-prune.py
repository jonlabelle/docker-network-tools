#!/usr/bin/python3

# -------------------------------------------------------------------------------------------------------
# Original source:
# https://github.com/airtower-luna/hello-ghcr/blob/e17ebc574711f4bcf85f8bd6b2380e226901778d/ghcr-prune.py
#
# Referenced in:
# https://github.community/t/delete-image-tag-from-github-container-registry/158852
#
# GitHub API documentation:
# https://docs.github.com/en/rest/reference/packages
#
# ---------
# Examples
# ---------
# # Store token in env var:
# $ export GHCR_TOKEN=<secret>
#
# # To delete untagged images older than 30 days (dry-run):
# $ python3 ghcr-prune.py --container network-tools --verbose --prune-age 30 --dry-run
#
# # To delete ALL untagged images (dry-run):
# $ python3 ghcr-prune.py --container network-tools --verbose --prune-all-untagged --dry-run
# -------------------------------------------------------------------------------------------------------

import argparse
import dateutil.parser
import getpass
import os
import requests
from datetime import datetime, timedelta

__author__ = "Fiona Klute"
__version__ = "0.1"
__copyright__ = "Copyright (C) 2021 Fiona Klute"
__license__ = "MIT"

github_api = 'https://api.github.com/user/packages/container'
github_api_accept = 'application/vnd.github.v3+json'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List versions of a GHCR container image you own, and optionally delete (prune) old, untagged versions.')
    parser.add_argument('--token', '-t', action='store_true', help='ask for token input instead of using the GHCR_TOKEN environment variable')
    parser.add_argument('--container', default='hello-ghcr-meow', help='name of the container image')
    parser.add_argument('--verbose', '-v', action='store_true', help='print extra debug info')
    parser.add_argument('--prune-age', type=float, metavar='DAYS', default=None, help='delete untagged images older than DAYS days (cannot be used in combination with --prune-all-untagged)')
    parser.add_argument('--prune-all-untagged', action='store_true', help='delete ALL untagged images (cannot be used in combination with --prune-age)')
    parser.add_argument('--dry-run', '-n', action='store_true', help='do not actually prune images, just list which images would be pruned')

    args = parser.parse_args()

    if args.token:
        token = getpass.getpass('Enter Token: ')
    elif 'GHCR_TOKEN' in os.environ:
        token = os.environ['GHCR_TOKEN']
    else:
        raise ValueError('missing authentication token')

    if args.prune_all_untagged is True and args.prune_age is not None:
        raise ValueError('--prune-age and --prune-all-untagged cannot be used together')

    sess = requests.Session()
    sess.headers.update({'Authorization': f'token {token}', 'Accept': github_api_accept})

    resp = sess.get(f'{github_api}/{args.container}/versions')
    versions = resp.json()

    # if args.verbose:
    #     ratelimit_reset_at = datetime.fromtimestamp(int(resp.headers["x-ratelimit-reset"]))
    #     print(f'{resp.headers["x-ratelimit-remaining"]} requests remaining until {ratelimit_reset_at}')
    #     print(versions)

    if args.prune_age is not None:
        del_before = datetime.now().astimezone() - timedelta(days=args.prune_age)
    else:
        del_before = None

    if del_before:
        print(f'Pruning images created before: {del_before}')
    elif args.prune_all_untagged is True:
        print('Pruning all untagged images')

    deleted_image_count = 0

    for version in versions:
        created = dateutil.parser.isoparse(version['created_at'])
        metadata = version["metadata"]["container"]

        # print(f'{version["id"]}\t{version["name"]}\t{created}\t{metadata["tags"]}')

        if args.prune_all_untagged:
            # Prune ALL untagged images
            if len(metadata['tags']) == 0:
                if args.dry_run:
                    print(f'Would delete untagged image: {version["id"]}')
                else:
                    resp = sess.delete(f'{github_api}/{args.container}/versions/{version["id"]}')
                    resp.raise_for_status()
                    print(f'Deleted untagged image: {version["id"]}')
                deleted_image_count = deleted_image_count + 1
        else:
            # Prune old untagged images:
            if del_before is not None and created < del_before and len(metadata['tags']) == 0:
                if args.dry_run:
                    print(f'Would delete old untagged image: {version["id"]}')
                else:
                    resp = sess.delete(f'{github_api}/{args.container}/versions/{version["id"]}')
                    resp.raise_for_status()
                    print(f'Deleted old untagged image: {version["id"]}')
                deleted_image_count = deleted_image_count + 1

    if deleted_image_count == 0:
        print('No images qualified for deletion')
    else:
        if args.dry_run:
            print(f'{deleted_image_count} image(s) would have been deleted')
        else:
            print(f'{deleted_image_count} image(s) were deleted')
