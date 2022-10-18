#!/usr/bin/env python3

import argparse
import logging
import time

import paho.mqtt.client as paho
import smbus2
import bme280

port = 1
address = 0x77
bus = smbus2.SMBus(port)
bme280.load_calibration_params(bus, address)


class Bme280:

    def __init__(
        self,
        mqtt_host,
        mqtt_queue,
        mqtt_username,
        mqtt_password,
        pressure_name,
        humidity_name,
        temperatur_name,

    ):
        self.mqtt_host = mqtt_host
        self.mqtt_queue = mqtt_queue
        self.mqtt_username = mqtt_username
        self.mqtt_password = mqtt_password
        self.pressure_name = pressure_name
        self.humidity_name = humidity_name
        self.temperatur_name = temperatur_name

    def publish_status(self, key, value):
        LOG.debug('publish status: %s=%s', key, value)
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

    def run(self):
        LOG.info('mqtt %s %s', self.mqtt_host, self.mqtt_queue)

        while True:
            data = bme280.sample(bus, address)
            LOG.debug('temperature: {} {} {}'.format(data.temperature, data.humidity, data.pressure))
            self.publish_status(self.temperatur_name, '{0:.0f}'.format(data.temperature))
            self.publish_status(self.humidity_name, '{0:.0f}'.format(data.humidity))
            self.publish_status(self.pressure_name, '{0:.0f}'.format(data.pressure))
            time.sleep(60)


def main():
    parser = argparse.ArgumentParser(description='bme280')
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Activate debug loglevel',
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

    parser.add_argument(
        '--pressure-name',
        action='store',
        help='pressure name',
    )
    parser.add_argument(
        '--humidity-name',
        action='store',
        help='humidity name',
    )
    parser.add_argument(
        '--temperatur-name',
        action='store',
        help='temperatur name',
    )

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    service = Bme280(
        pressure_name=args.pressure_name,
        humidity_name=args.humidity_name,
        temperatur_name=args.temperatur_name,
        mqtt_host=args.mqtt_host,
        mqtt_queue=args.mqtt_queue,
        mqtt_username=args.mqtt_username,
        mqtt_password=args.mqtt_password,
    )
    service.run()


LOG = logging.getLogger(__name__)

if __name__ == "__main__":
    # execute only if run as a script
    main()
