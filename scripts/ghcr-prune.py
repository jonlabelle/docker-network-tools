#!/usr/bin/python3

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

# -------------------------------------------------------------------------------------------------------
# Original source:
# https://github.com/airtower-luna/hello-ghcr/blob/e17ebc574711f4bcf85f8bd6b2380e226901778d/ghcr-prune.py
#
# Referenced in:
# https://github.community/t/delete-image-tag-from-github-container-registry/158852
#
# Examples:
# To delete untagged images older than 30 days (dry-run):
# $ export GHCR_TOKEN=<secret>
# $ python3 ghcr-prune.py --container network-tools --verbose --prune-age 30 --dry-run
# -------------------------------------------------------------------------------------------------------

# GitHub API documentation: https://docs.github.com/en/rest/reference/packages
github_api_accept = 'application/vnd.github.v3+json'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='List versions of a GHCR container image you own, and optionally delete (prune) old, untagged versions.')
    parser.add_argument('--token', '-t', action='store_true', help='ask for token input instead of using the GHCR_TOKEN environment variable')
    parser.add_argument('--container', default='hello-ghcr-meow', help='name of the container image')
    parser.add_argument('--verbose', '-v', action='store_true', help='print extra debug info')
    parser.add_argument('--prune-age', type=float, metavar='DAYS', default=None, help='delete untagged images older than DAYS days')
    parser.add_argument('--dry-run', '-n', action='store_true', help='do not actually prune images, just list which images would be pruned')

    args = parser.parse_args()

    if args.token:
        token = getpass.getpass('Enter Token: ')
    elif 'GHCR_TOKEN' in os.environ:
        token = os.environ['GHCR_TOKEN']
    else:
        raise ValueError('missing authentication token')

    sess = requests.Session()
    sess.headers.update({'Authorization': f'token {token}', 'Accept': github_api_accept})

    resp = sess.get(f'https://api.github.com/user/packages/container/{args.container}/versions')
    versions = resp.json()

    if args.verbose:
        reset = datetime.fromtimestamp(int(resp.headers["x-ratelimit-reset"]))
        print(f'{resp.headers["x-ratelimit-remaining"]} requests remaining until {reset}')
        print(versions)

    del_before = datetime.now().astimezone() - timedelta(days=args.prune_age) \
        if args.prune_age is not None else None
    if del_before:
        print(f'Pruning images created before: {del_before}')

    for version in versions:
        created = dateutil.parser.isoparse(version['created_at'])
        metadata = version["metadata"]["container"]
        # print(f'{version["id"]}\t{version["name"]}\t{created}\t{metadata["tags"]}')

        # prune old untagged images if requested
        if del_before is not None and created < del_before and len(metadata['tags']) == 0:
            if args.dry_run:
                print(f'Would delete: {version["id"]}')
            else:
                resp = sess.delete(f'https://api.github.com/user/packages/container/{args.container}/versions/{version["id"]}')
                resp.raise_for_status()
                print(f'Deleted: {version["id"]}')
