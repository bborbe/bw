import bwtv as teamvault

nodes['hm.rasp3'] = {
    'hostname': 'rasp3.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bookworm',
    },
    'metadata': {
        'openvpn-client': {
            'enabled': True,
            'name': 'rasp3',
        },
        'backup_client': {
            'enabled': True,
        },
        'kernel_modules': {
            'i2c-dev': {},
        },
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'os': 'linux',
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'addresses': ['192.168.50.2/24'],
                    'routes': [
                        {
                            'to': '0.0.0.0/0',
                            'via': '192.168.50.1',
                            'metric': '100',
                        },
                    ],
                    'nameservers': {
                        'addresses': ['8.8.8.8', '8.8.4.4'],
                        'search': ['hm.benjamin-borbe.de'],
                    },
                },
            },
        },
        'iptables': {
            'enabled': True,
            'nat_interfaces': [],
            'rules': {
                'filter': {
                    # allow forward
                    '-A FORWARD -j ACCEPT',
                },
            },
        },
        'bme280': {
            # Disabled 2026-08-16: the MQTT broker rasp4 was decommissioned and its
            # successor (homeassistant.hm.benjamin-borbe.de) has no MQTT listener,
            # so this published nowhere. To re-enable: flip to True, repoint
            # mqtt-host to the live broker, and ensure rasp3 has a route to it.
            'enabled': False,
            'mqtt-host': 'rasp4.hm.benjamin-borbe.de',
            'mqtt-username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt-password': teamvault.password('9qNx3O', site='benjamin-borbe'),
            'mqtt-queue': 'sensors',
            'pressure-name': 'rasp3/pressure',
            'humidity-name': 'rasp3/humidity',
            'temperatur-name': 'rasp3/temperatur',
        },
    },
}
