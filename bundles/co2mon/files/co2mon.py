#!/usr/bin/env python3

import argparse
import logging
import requests
import time

from CO2Meter import *
import paho.mqtt.client as paho


class Co2mon:

    def __init__(
        self,
        device,
        co2_name,
        temperatur_name,
        openhab_url,
        openhab_username,
        openhab_password,
        mqtt_host,
        mqtt_queue,
        mqtt_username,
        mqtt_password,
    ):
        self.device = device
        self.co2_name = co2_name
        self.temperatur_name = temperatur_name
        self.openhab_url = openhab_url
        self.openhab_username = openhab_username
        self.openhab_password = openhab_password
        self.mqtt_host = mqtt_host
        self.mqtt_queue = mqtt_queue
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password

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
        if self.mqtt_host and self.mqtt_queue:
            self.publish_mqtt_status(key=key, value=value)

    def publish_mqtt_status(self, key, value):
        try:
            client = paho.Client()
            if self.mqtt_username and self.mqtt_password:
                LOG.debug('set mqtt username and password')
                client.username_pw_set(username=self.mqtt_username, password=self.mqtt_password)
            LOG.debug('connecting to broker {}'.format(self.mqtt_host))
            res = client.connect(self.mqtt_host)
            if res != paho.MQTT_ERR_SUCCESS:
                raise Exception('connect failed: {}'.format(paho.error_string(res)))
            LOG.debug('publishing to {}'.format(self.mqtt_queue))
            queue = '{}/{}'.format(self.mqtt_queue, key)
            res = client.publish(queue, value)
            if res[0] != paho.MQTT_ERR_SUCCESS:
                raise Exception('publish failed: {}'.format(paho.error_string(res)))
            res = client.disconnect()
            if res != paho.MQTT_ERR_SUCCESS:
                raise Exception('disconnect failed: {}'.format(paho.error_string(res)))
            LOG.info('push %s=%s successful to mqtt', queue, value)
        except Exception as e:
            LOG.exception('send to mqtt failed')

    def publish_openhab_status(self, key, value):
        try:
            if self.openhab_username and self.openhab_password:
                auth = (self.openhab_username, self.openhab_password)
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
            LOG.exception('send to openhab failed')

    def run(self):
        LOG.info('use device %s', self.device)
        LOG.info('openhab %s', self.openhab_url)
        LOG.info('mqtt %s %s', self.mqtt_host, self.mqtt_queue)
        Meter = CO2Meter(self.device, callback=self.callback)
        while True:
            measurement = Meter.get_data()
            LOG.debug('measurement: %s', measurement)
            if 'co2' in measurement:
                self.publish_status(self.co2_name, '{0:.0f}'.format(measurement['co2']))
            if 'temperature' in measurement:
                self.publish_status(self.temperatur_name, '{0:.2f}'.format(measurement['temperature']))
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
        '--mqtt-username',
        action='store',
        help='mqtt user',
    )
    parser.add_argument(
        '--mqtt-password',
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
        '--openhab-username',
        action='store',
        help='openhab user',
    )
    parser.add_argument(
        '--openhab-password',
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
        openhab_username=args.openhab_username,
        openhab_password=args.openhab_password,
        mqtt_host=args.mqtt_host,
        mqtt_queue=args.mqtt_queue,
        mqtt_username=args.mqtt_username,
        mqtt_password=args.mqtt_password,
    )
    co2mon.run()


LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    # execute only if run as a script
    main()
