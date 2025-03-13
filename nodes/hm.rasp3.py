import bwtv as teamvault

nodes['hm.rasp3'] = {
    'hostname': 'rasp3.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bookworm',
    },
    'metadata': {
        'backup_client': {
            'enabled': True,
        },
        'kernel_modules': {
            'i2c-dev': {},
        },
        'golang': {
            'enabled': True,
            'arch': 'armv6l',
            'version': '1.16.4',
            'os': 'linux',
        },
        'netplan': {
            'enabled': True,
            'ethernets': {
                'eth0': {
                    'dhcp4': False,
                    'dhcp6': False,
                    'addresses': ['192.168.178.2/24'],
                    'routes': [
                        {
                            'to': '0.0.0.0/0',
                            'via': '192.168.178.1',
                            'metric': '100',
                        }
                    ],
                    'nameservers': ['8.8.8.8', '8.8.4.4'],
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
            'enabled': True,
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
