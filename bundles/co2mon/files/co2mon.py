#!/usr/bin/env python3

import argparse
import time
import logging
import requests

from CO2Meter import *
import paho.mqtt.client as paho


class Co2mon:

    def __init__(
        self,
        device,
        co2_name,
        temperatur_name,
        openhab_url,
        openhab_user,
        openhab_pass,
        mqtt_host,
        mqtt_queue,
        mqtt_user,
        mqtt_pass,
    ):
        self.device = device
        self.co2_name = co2_name
        self.temperatur_name = temperatur_name
        self.openhab_url = openhab_url
        self.openhab_user = openhab_user
        self.openhab_pass = openhab_pass
        self.mqtt_host = mqtt_host
        self.mqtt_queue = mqtt_queue
        self.mqtt_user = mqtt_user
        self.mqtt_pass = mqtt_pass

    def callback(self, sensor, value):
        LOG.debug('callback called with %s %s', sensor, value)
        if sensor == CO2METER_CO2:
            self.publish_status(self.co2_name, '{0:.0f}'.format(value))
        if sensor == CO2METER_TEMP:
            self.publish_status(self.temperatur_name, '{0:.2f}'.format(value))

    def publish_status(self, key, value):
        LOG.debug('publish status: %s=%s', key, value)
        if self.openhab_url:
            self.publish_openhab_status(key=key, value=value)
        if self.mqtt_host:
            self.publish_mqtt_status(key=key, value=value)

    def publish_mqtt_status(self, key, value):
        try:
            client = paho.Client()
            if self.mqtt_user and self.mqtt_pass:
                LOG.debug('set mqtt username and password')
                client.username_pw_set(username=self.mqtt_user, password=self.mqtt_pass)
            LOG.debug('connecting to broker {}'.format(self.mqtt_host))
            res = client.connect(self.mqtt_host)
            if res != paho.MQTT_ERR_SUCCESS:
                raise Exception('connect failed: {}'.format(paho.error_string(res)))
            LOG.debug('publishing to {}'.format(self.mqtt_queue))
            res = client.publish(self.mqtt_queue, '{}={}'.format(key, value))
            if res[0] != paho.MQTT_ERR_SUCCESS:
                raise Exception('publish failed: {}'.format(paho.error_string(res)))
            res = client.disconnect()
            if res != paho.MQTT_ERR_SUCCESS:
                raise Exception('disconnect failed: {}'.format(paho.error_string(res)))
            LOG.debug('message published')
        except Exception as e:
            LOG.error(e)

    def publish_openhab_status(self, key, value):
        try:
            if self.openhab_user and self.openhab_pass:
                auth = (self.openhab_user, self.openhab_pass)
            else:
                auth = None
            url = '{}/rest/items/{}/state'.format(self.openhab_url, key)
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

    def run(self):
        LOG.info('use device %s', self.device)
        LOG.info('openhab %s', self.openhab_url)
        Meter = CO2Meter(self.device, callback=self.callback)
        while True:
            measurement = Meter.get_data()
            LOG.debug('measurement: %s', measurement)
            if 'co2' in measurement:
                self.publish_status(self.openhab_co2_name, '{0:.0f}'.format(measurement['co2']))
            if 'temperature' in measurement:
                self.publish_status(self.openhab_temperatur_name, '{0:.2f}'.format(measurement['temperature']))
            time.sleep(60)


def main():
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

    # Paramter names
    parser.add_argument(
        '--co2-name',
        action='store',
        help='name for co2',
        default='CO2',
    )
    parser.add_argument(
        '--temperatur-name',
        action='store',
        help='name for temperatur',
        default='TEMP',
    )

    # mqtt Params
    parser.add_argument(
        '--mqtt-host',
        action='store',
        help='mqtt host',
    )
    parser.add_argument(
        '--mqtt-queue',
        action='store',
        help='mqtt queue',
    )
    parser.add_argument(
        '--mqtt-user',
        action='store',
        help='mqtt user',
    )
    parser.add_argument(
        '--mqtt-pass',
        action='store',
        help='mqtt password',
    )

    # openHAB Params
    parser.add_argument(
        '--openhab-url',
        action='store',
        help='openhab url',
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

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    co2mon = Co2mon(
        device=args.device,
        co2_name=args.co2_name,
        temperatur_name=args.temperatur_name,
        openhab_url=args.openhab_url,
        openhab_user=args.openhab_user,
        openhab_pass=args.openhab_pass,
        mqtt_host=args.mqtt_host,
        mqtt_queue=args.mqtt_queue,
        mqtt_user=args.mqtt_user,
        mqtt_pass=args.mqtt_pass,
    )
    co2mon.run()


LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    # execute only if run as a script
    main()
