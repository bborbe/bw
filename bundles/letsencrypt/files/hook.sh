#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

mkdir -p /etc/haproxy/ssl
DOMAINS_TXT="domains.txt"

# Different sed version for different os types...
_sed() {
	if [[ "${OSTYPE}" = "Linux" ]]; then
		sed -r "${@}"
	else
		sed -E "${@}"
	fi
}

add_to_haproxy() {
	domain="${1}"
	if [[ -r "/etc/letsencrypt.sh/certs/${domain}/privkey.pem" ]] && [[ -r "/etc/letsencrypt.sh/certs/${domain}/fullchain.pem" ]] ; then
		DOMAIN=$domain bash -c 'cat /etc/letsencrypt.sh/certs/$DOMAIN/privkey.pem /etc/letsencrypt.sh/certs/$DOMAIN/fullchain.pem > /etc/haproxy/ssl/$DOMAIN.pem'
		DOMAIN=$domain bash -c 'cat /etc/letsencrypt.sh/certs/$DOMAIN/privkey.pem /etc/letsencrypt.sh/certs/$DOMAIN/fullchain.pem >> /etc/haproxy/ssl/haproxy.pem'
	fi
}

restart_haproxy() {
	systemctl reload haproxy
}

clear_haproxy() {
	echo -n "" > /etc/haproxy/ssl/haproxy.pem
}

main() {
	clear_haproxy
	ORIGIFS="${IFS}"
	IFS=$'\n'
	for line in $(<"${DOMAINS_TXT}" tr -d '\r' | tr '[:upper:]' '[:lower:]' | _sed -e 's/^[[:space:]]*//g' -e 's/[[:space:]]*$//g' -e 's/[[:space:]]+/ /g' | (grep -vE '^(#|$)' || true)); do
		IFS="${ORIGIFS}"
		domain="$(printf '%s\n' "${line}" | cut -d' ' -f1)"
		echo "handle domain ${domain}" >&2
		add_to_haproxy "${domain}"
	done
	restart_haproxy
}

# Run script
main "${@:-}"
