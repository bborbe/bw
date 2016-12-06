#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

CONFIG=/etc/letsencrypt.sh/config.sh /opt/letsencrypt.sh/letsencrypt.sh --cron
