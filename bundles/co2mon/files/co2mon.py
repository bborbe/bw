#!/usr/bin/env python3

import argparse
import time
import logging
import requests

from CO2Meter import *

LOG = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='co2mon')
parser.add_argument(
    '--debug',
    action='store_true',
    help='Activate debug loglevel',
)
parser.add_argument(
    '--device',
    action='store',
    help='device name of co2mini',
    required=True,
)
parser.add_argument(
    '--openhab-url',
    action='store',
    help='openhab url',
    required=True,
)
parser.add_argument(
    '--openhab-user',
    action='store',
    help='openhab user',
)
parser.add_argument(
    '--openhab-pass',
    action='store',
    help='openhab password',
)
parser.add_argument(
    '--openhab-co2-name',
    action='store',
    help='openhab name for co2',
    default='CO2',
)
parser.add_argument(
    '--openhab-temperatur-name',
    action='store',
    help='openhab name for temperatur',
    default='TEMP',
)
parser.add_argument(
    '--openhab-humidity-name',
    action='store',
    help='openhab name for humidity',
    default='HUM',
)

args = parser.parse_args()

if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

LOG.info('use device %s', args.device)
LOG.info('openhab %s', args.openhab_url)


def callback(sensor, value):
    LOG.debug('callback called with %s %s', sensor, value)
    if sensor == CO2METER_CO2:
        publish_openhab_status(args.openhab_co2_name, '{0:.0f}'.format(value))
    if sensor == CO2METER_TEMP:
        publish_openhab_status(args.openhab_temperatur_name, '{0:.2f}'.format(value))
    if sensor == CO2METER_HUM:
        publish_openhab_status(args.openhab_temperatur_name, '{0:.2f}'.format(value))


Meter = CO2Meter(args.device, callback=callback)

if args.openhab_user and args.openhab_pass:
    auth = (args.openhab_user, args.openhab_pass)
else:
    auth = None


def publish_openhab_status(key, value):
    try:
        url = '{}/rest/items/{}/state'.format(args.openhab_url, key)
        LOG.debug('send %s to %s', value, url)
        res = requests.put(
            url,
            data=value,
            auth=auth,
            headers={'Content-type': 'text/plain'},
            timeout=(10, 60),
        )
        if int(res.status_code / 100) != 2:
            LOG.error('request %s=%s to openhab failed with status %d %s', key, value, res.status_code, res.text)
        else:
            LOG.info('send %s=%s successful to openhab', key, value)
    except Exception as e:
        LOG.error(e)


while True:
    measurement = Meter.get_data()
    LOG.debug('measurement: %s', measurement)
    if 'co2' in measurement:
        publish_openhab_status(args.openhab_co2_name, '{0:.0f}'.format(measurement['co2']))
    if 'temperature' in measurement:
        publish_openhab_status(args.openhab_temperatur_name, '{0:.2f}'.format(measurement['temperature']))
    time.sleep(60)
