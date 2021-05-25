#!/usr/bin/env bash

#
# For automated repository test only
#
# Called by ./docker-compose.test.yml
# See https://docs.docker.com/docker-hub/builds/automated-testing/

set -e
set -o pipefail

command -v ab \
    && command -v bash \
    && command -v fping \
    && command -v macchanger \
    && command -v mtr \
    && command -v nc \
    && command -v ngrep \
    && command -v nmap \
    && command -v netstat \
    && command -v libressl \
    && command -v drill \
    && command -v curl \
    && command -v git \
    && command -v find \
    && command -v python3 \
    && python3 -c 'import requests'
