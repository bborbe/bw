import bwtv as teamvault

nodes['hm.rasp4'] = {
    'hostname': 'rasp4.hm.benjamin-borbe.de',
    'groups': {
        'raspbian-bullseye',
    },
    'metadata': {
        'backup_client': {
            'enabled': True,
        },
        'influxdb': {
            'enabled': True,
        },
        'grafana': {
            'enabled': True,
        },
        'telegraf': {
            'enabled': True,
            'mqtt_username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'mqtt_password': teamvault.password('9qNx3O', site='benjamin-borbe'),
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
                    'addresses': ['192.168.178.8/24'],
                    'routes': [
                        {
                            'to': '0.0.0.0/0',
                            'via': '192.168.178.1',
                        }
                    ],
                    'nameservers': ['8.8.8.8', '8.8.4.4'],
                },
            },
        },
        'mosquitto': {
            'enabled': True,
            'username': teamvault.username('9qNx3O', site='benjamin-borbe'),
            'password': teamvault.password('9qNx3O', site='benjamin-borbe'),
        },
    },
}
