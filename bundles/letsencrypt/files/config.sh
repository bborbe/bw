#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

HOOK="/etc/letsencrypt.sh/hook.sh"
BASEDIR="/etc/letsencrypt.sh/"
CONTACT_EMAIL="${email}"
WELLKNOWN="/var/www/letsencrypt.sh/.well-known/acme-challenge"
