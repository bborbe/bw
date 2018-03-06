#!/usr/bin/env python3

import argparse
import logging
import requests

LOG = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='co2mon')
parser.add_argument(
    '--debug',
    action='store_true',
    help='Activate debug loglevel',
)
parser.add_argument(
    '--openhab-url',
    action='store',
    help='openhab url',
    required=True,
)
parser.add_argument(
    '--openhab-username',
    action='store',
    help='openhab user',
)
parser.add_argument(
    '--openhab-password',
    action='store',
    help='openhab password',
)
parser.add_argument(
    '--key',
    action='store',
    help='key',
    required=True,
)
parser.add_argument(
    '--value',
    action='store',
    help='value',
    required=True,
)

args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

LOG.info('openhab %s', args.openhab_url)

if args.openhab_username and args.openhab_password:
    auth = (args.openhab_username, args.openhab_password)
else:
    auth = None

try:
    url = '{}/rest/items/{}/state'.format(args.openhab_url, args.key)
    LOG.debug('send %s to %s', args.value, url)
    res = requests.put(
        url,
        data=args.value,
        auth=auth,
        headers={'Content-type': 'text/plain'},
    )
    if int(res.status_code / 100) != 2:
        LOG.error('request %s=%s to openhab failed with status %d %s', args.key, args.value, res.status_code, res.text)
    else:
        LOG.info('send %s=%s successful to openhab', args.key, args.value)
except Exception as e:
    LOG.error(e)
