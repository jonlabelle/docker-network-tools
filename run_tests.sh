#!/usr/bin/env bash

#
# For automated repository test only
#
# Called by ./docker-compose.test.yml
# See https://docs.docker.com/docker-hub/builds/automated-testing/

set -e
set -o pipefail

which ab \
    && which bash \
    && which fping \
    && which macchanger \
    && which mtr \
    && which nc \
    && which ngrep \
    && which nmap \
    && which netstat \
    && which libressl \
    && which drill \
    && which curl \
    && which git \
    && which find \
    && which python3 \
    && python3 -c 'import requests'
